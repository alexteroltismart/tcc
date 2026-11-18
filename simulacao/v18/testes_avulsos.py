"""Testes avulsos refeitos para a v17 (ganhos por alocação de polos; anti-windup só no limite de posição)."""
import sys, math, inspect, importlib.util, numpy as np
sys.path.insert(0, r"D:\tech\tcc\simulacao")
import modelo_barra as m

spec = importlib.util.spec_from_file_location("v07", r"D:\tech\tcc\simulacao\v07\modelo_barra.py")
v07 = importlib.util.module_from_spec(spec); spec.loader.exec_module(v07)
v07.FAIXA = m.FAIXA
src = inspect.getsource(v07.simular)
old = "if not (sat_pos or sat_vel):"
assert old in src
ns = vars(v07)
exec(src.replace(old, 'if ti != math.inf and not sat_pos:'), ns)   # mesmo anti-windup da v12

kg = m.ganho_kg(4)["Kg"]
tun, _ = m.sintonia_polos(kg, m.BASE)
G = {"P": tun["P"], "PI": tun["PI"], "PI+FF": tun["PI"]}
KC, TI = tun["PI"]
cen = m.cenarios()

print("== H6: pressão instantânea x mangueira (v07, C_h 0,5 mL), anti-windup só posição ==", flush=True)
difs = []
for c in ("C2", "C3"):
    ev, tf = cen[c]
    for modo, (kc, ti) in G.items():
        a = m.metricas(m.simular(ev, tf, modo, m.BASE, kc, ti), ev)["fora_pct"]
        mv = "PI" if modo == "P" else modo
        s = ns["simular"](ev, tf, mv, v07.BASE, kc, ti)
        b = v07.metricas(s, ev)["fora_pct"]
        difs.append(abs(b - a))
        print(f"{c} {modo:6s} H6 {a:5.2f}%  mangueira {b:5.2f}%  dif {b - a:+.2f} p.p.", flush=True)
print(f"maior diferença: {max(difs):.2f} p.p.")
lo, hi = 0.5, 10
ev = [(0.0, 7), (0.5, 6)]
for _ in range(12):
    mid = (lo + hi) / 2
    s = ns["simular"](ev, 10, "PI", v07.BASE, mid, math.inf)
    if np.ptp(s["P"][s["t"] > 8]) > 1e-4:
        hi = mid
    else:
        lo = mid
print(f"Kc-limite (só P) com mangueira: {hi:.3f}", flush=True)

print("== passo de integração (C3) ==", flush=True)
ev, tf = cen["C3"]
for dt in (1e-3, 2e-3, 1e-2):
    print(f"dt={dt * 1000:.0f} ms  " + "  ".join(
        f"{mo} {m.metricas(m.simular(ev, tf, mo, m.BASE, *G[mo], dt=dt), ev)['fora_pct']:.2f}%" for mo in G), flush=True)

print("== ruído no sensor (7 bicos, 20 s, PI sem FF, anti-windup só posição) ==", flush=True)
par = m.BASE
def sim(kc, ti, sig, seed=1, tf=20):
    rng = np.random.default_rng(seed); cada = int(round(m.TS / m.DT)); n = 7
    alpha = m.alpha_ff(n); bias = alpha; p = m.P_REF; integ = 0; ac = alpha; curso = 0; P = []
    for k in range(int(round(tf / m.DT))):
        if k % cada == 0:
            e = p + rng.normal(0, sig) - m.P_REF; u = bias + kc * (e + integ / ti)
            if not ((u >= 1 and e > 0) or (u <= 0 and e < 0)):
                integ += e * m.TS
            ac = min(max(bias + kc * (e + integ / ti), 0), 1)
        v = min(max((ac - alpha) / par["tau_a"], -par["w_max"]), par["w_max"]); a0 = alpha
        alpha = min(max(alpha + v * m.DT, 0), 1); curso += abs(alpha - a0)
        p = m.p_regime(n * m.K + m.KV_MAX * alpha); P.append(p)
    P = np.array(P)
    return curso, ((P < 0.9 * m.P_REF) | (P > 1.1 * m.P_REF)).mean() * 100
for sig in (0.035, 0.07):
    r = {nome: sim(kc, ti, sig) for nome, kc, ti in (("Kc 0,33", 0.334, 0.2), ("polos", KC, TI))}
    print(f"ruído {sig / 3.5 * 100:.0f}%: curso Kc0,33 {r['Kc 0,33'][0]:.2f}  polos {r['polos'][0]:.2f}  razão {r['polos'][0] / r['Kc 0,33'][0]:.2f}  "
          f"fora polos {r['polos'][1]:.1f}%  fora Kc0,33 {r['Kc 0,33'][1]:.1f}%", flush=True)
