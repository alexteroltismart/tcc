"""Teste à parte (v19): efeito do anti-windup no C2 e no C3, com o controlador em tempo real.
Variantes: 'posicao' (a do texto), 'pos+vel' (congela também com a válvula na velocidade máxima,
como na v11) e 'nenhum'. Não entra nos números do script principal."""
import sys, math, inspect
sys.path.insert(0, r"D:\tech\tcc\simulacao")
sys.stdout.reconfigure(encoding="utf-8")
import modelo_barra as m

src = inspect.getsource(m.simular)
alvo = 'if modo != "P" and not sat_pos:'
assert alvo in src
ns = dict(vars(m))
variantes = {
    "posicao": alvo,
    "pos+vel": 'if modo != "P" and not (sat_pos or abs(min(max(u, 0.0), 1.0) - alpha) / par["tau_a"] >= par["w_max"]):',
    "nenhum": 'if modo != "P":',
}
kg = m.ganho_kg(4)["Kg"]
tun, _ = m.sintonia_polos(kg, m.BASE)
cen = m.cenarios()
for nome, cond in variantes.items():
    exec(src.replace(alvo, cond).replace("def simular(", f"def simular_{nome.replace('+', '_')}("), ns)
    f = ns[f"simular_{nome.replace('+', '_')}"]
    out = []
    for c in ("C2", "C3"):
        ev, tf = cen[c]
        for modo in ("PI", "PI+FF"):
            r = m.metricas(f(ev, tf, modo, m.BASE, *tun["PI"]))
            out.append(f"{c} {modo} {r['fora_pct']:.1f}% IAE {r['IAE']:.2f}")
    print(f"{nome:8s}: " + " | ".join(out), flush=True)
