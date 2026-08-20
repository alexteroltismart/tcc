"""Smoke test da pilha geoespacial. Roda: python3 check.py"""
import glob
import geopandas as gpd
import rasterio
from rasterstats import zonal_stats

QF = "dados/1/20250909-20250909-1-WQB20210006_qfield_project/qfield_project"
TIF = glob.glob("dados/1/*20250909-20250909_tifs/**/rate_lha/*.tif", recursive=True)[0]

talhoes = gpd.read_file(f"{QF}/field_limits.gpkg")
passadas = gpd.read_file(f"{QF}/Spraying.gpkg")
assert len(talhoes) == 5 and len(passadas) == 150
assert "taxa (L/ha)" in passadas.columns

with rasterio.open(TIF) as src:
    assert src.crs.to_epsg() == 32721 and src.nodata == 0
    assert src.colormap(1), "raster é paletado (DN = valor físico, ver CLAUDE.md)"
    assert src.res == (0.25, 0.25)

# vetor e raster ja estao em EPSG:32721
stats = zonal_stats(talhoes.to_crs(src.crs), TIF, stats=["mean", "count"], nodata=0)
cobertos = [s for s in stats if s["count"]]
assert cobertos, "nenhum talhão intersecta o raster — CRS errado?"
print(f"ok — {len(cobertos)}/{len(stats)} talhões cobertos, L/ha médio "
      f"{cobertos[0]['mean']:.1f}")

# calibracao DN->L/ha: balanco de massa sobre TODOS os rasters da data
integral = 0.0
for t in glob.glob("dados/1/*20250909-20250909_tifs/**/rate_lha/*.tif", recursive=True):
    with rasterio.open(t) as src:
        band = src.read(1)
        integral += band[band > 0].sum() * abs(src.res[0] * src.res[1]) / 1e4
fator = passadas["volume (L)"].sum() / integral
assert 0.95 < fator < 1.05, f"DN nao e mais L/ha direto: fator {fator:.3f}"
print(f"ok — balanco de massa: DN = L/ha x {fator:.3f}")
