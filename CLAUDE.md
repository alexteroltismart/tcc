# TCC — pulverização agrícola (drone/avião)

## Dados (`dados/`, não versionado)

Um voo = um `qfield_project` (QGIS/QField) + um pacote de GeoTIFFs.

**Vetor** — GeoPackage, EPSG:32721, ler com `geopandas.read_file()`:
- `Spraying.gpkg` / `Transport.gpkg` — linhas do trajeto, 150 feições. Colunas em
  português com espaços e parênteses (`'taxa (L/ha)'`, `'pressão (kPa)'`, `'volume (L)'`).
- `field_limits.gpkg` — polígonos dos talhões (layer chama-se `temp`), `area_ha`, `field_name`.

**Raster** — `.../merge/<variavel>/<AAAAMMDD>_1_<id>_<variavel>.tif`:
COG, LZW, EPSG:32721 (UTM 21S), pixel 0.25 m, ~9000×8200, com overviews.
Variáveis: `app`, `rate_lha`, `cdd`, `pressure_dbar`, `speed_kmh`, `elevation_m`,
`margin_cm`, `sensitivity`, `var`.

> **DN = valor físico direto.** Banda 1 é Byte paletado (0 = nodata), mas o índice
> da paleta É o valor, não um código. Não há `scale`/`offset` porque não precisa.
> Camadas que exigem 1 casa decimal guardam valor×10 (ver tabela). Calibrado por
> balanço de massa, não por informação do fornecedor — ver "Calibração".

| camada | DN → unidade | conferência |
|---|---|---|
| `rate_lha` | ×1 → L/ha | ∫DN·área = 9089 L vs 9244.7 L do vetor (1.7%) |
| `speed_kmh` | **×0.1** → km/h | 173.1 DN vs 17.25 km/h do vetor |
| `pressure_dbar` | **×0.1** → bar (dbar) | 41.9 DN vs 4.19 do vetor (coluna diz kPa, é bar) |
| `sensitivity` | ×1 | 2.0 = `sensibilidade` do vetor |
| `elevation_m` | ×1 → m | 47–192 m |
| `margin_cm` | ×1 → cm | constante 50 |
| `cdd`, `var` | ? | unidade não identificada, não usar no texto ainda |

Tudo em EPSG:32721 (UTM 21S) — vetor e raster no mesmo CRS, não precisa reprojetar.

**A camada `app` é categórica, não contínua.** Só 4–5 DNs, os mesmos em todos os 13 voos:
`{1, 250, 214, 179, 125}`. Ordenados por área decrescente e por taxa média crescente —
consistente com nº de sobreposições (1×, 2×, 3×, 4×, 5×), mas o mapeamento DN→classe
não está em lugar nenhum do pacote. Confirmar com o fornecedor antes de usar no texto.
`margin_cm` é constante (DN 50) em todo o voo.

## Ferramentas

Já instalado: `geopandas`, `shapely`, `rasterio`, `rasterstats`, `numpy`, `pandas`,
`matplotlib`, `osgeo.gdal`, e o CLI `gdalinfo`/`gdal_translate`.

Instalar com `pip install --user --break-system-packages` (o ambiente é PEP 668).

Não usar: `rioxarray`/`xarray`/`dask` (raster de 74 MB cabe na RAM, overhead sem ganho),
`pyqgis` (não precisa do QGIS pra ler `.gpkg`/`.tif`), `folium` (matplotlib basta pra TCC).

Padrões:
- estatística por talhão → `rasterstats.zonal_stats(gdf, tif, stats=[...])`
- recorte por polígono → `rasterio.mask.mask(src, geoms, crop=True)`
- visualizar rápido → ler overview: `src.read(1, out_shape=(1, h//16, w//16))`

## Calibração DN → unidade física

Resolvida por **balanço de massa** (2026-08-19), sem depender do fornecedor: a soma
`Σ DN · área_do_pixel` sobre os dois rasters `rate_lha` de 09/09 dá 9088.9 L contra
9244.7 L de `volume (L)` do `Spraying.gpkg` → fator 1.017. A área também fecha:
278.79 ha de raster contra 283.82 ha de `total de hectares (ha)`. A folga de ~1.8%
é borda/sobreposição. Logo DN = L/ha, ×1.

Armadilha que custou tempo: o pacote de 09/09 tem **dois** rasters (dois ids de voo,
`6vb7jxf21v` e `6vb7qjnnn9`) e um `Spraying.gpkg` que cobre os dois. Somar só um dá
fator 1.77 e parece que existe escala escondida. Sempre agregar todos os ids da data.

Colunas do vetor que NÃO servem de referência:
- `taxa (L/ha)` = 89.8 constante — é o setpoint, não o aplicado.
- `hectares aplicados (ha)` (Σ 29.5) — área com bico aberto no modo Localizada PWM,
  não a área coberta pelo voo. Usar `total de hectares (ha)` pra comparar com raster.

`.../qfield_project(1)/` é cópia idêntica de `.../qfield_project/` — ignorar.

## Checagem

`python3 check.py` — smoke test da pilha (vetor+raster, CRS, zonal stats) e do
balanço de massa que sustenta a calibração DN→L/ha.
