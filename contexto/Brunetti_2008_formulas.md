# Brunetti (2008) — fórmulas citáveis no TCC

**Referência (ABNT):** BRUNETTI, F. **Mecânica dos fluidos**. 2. ed. rev. São Paulo: Pearson Prentice Hall, 2008. ISBN 978-85-7605-182-4.

- **Arquivos:**
  - PDF: `referencias base/Mecânica dos Fluidos Único -- Franco Brunetti ...pdf`. A página do PDF é a página do livro + 16.
  - Texto completo: `referencias base/Brunetti_2008_Mecanica_dos_Fluidos.md`, extraído automaticamente. As equações saem quebradas nele, então use este arquivo para isso.
- **Conferência:** todas as equações abaixo foram conferidas na imagem da página do livro (04/11/2026). Nº = numeração do próprio livro. "Sem nº" = equação que aparece no texto sem número.
- **Citação:** autor-data com página, p. ex. (BRUNETTI, 2008, p. 213).

**Notação do livro:**
- trabalha com **cargas** (energia por unidade de peso, em metros), com $\gamma = \rho g$;
- uma diferença de pressão vira carga por $h = \Delta p/\gamma$;
- $D_H$ é o diâmetro hidráulico, igual ao diâmetro interno $D$ em tubo circular.

---

## 1. Propriedades e regime de escoamento

| O que | Fórmula (como no livro) | Nº | Seção / página | Uso no TCC (v10) |
|---|---|---|---|---|
| Massa específica | $\rho = m/V$ | (1.5) | 1.6, p. 8 | símbolo $\rho$ |
| Peso específico | $\gamma = G/V$ | (1.6) | 1.7, p. 8 | só para a passagem carga ↔ pressão |
| Viscosidade dinâmica (lei de Newton) | $\tau = \mu \, \dfrac{dv}{dy}$ | (1.3) | 1.4, p. 4 | definição de $\mu$ na Eq. 2.1 |
| **Número de Reynolds** | $Re = \dfrac{\rho v D}{\mu} = \dfrac{v D}{\nu}$ | **(3.1)** | 3.2, p. 69 | **Eq. 2.1** |
| Limites do regime em tubos | laminar $Re < 2000$; transição $2000 < Re < 2400$; turbulento $Re > 2400$ | sem nº | 3.2, p. 69 | ver observação A |
| Reynolds com diâmetro hidráulico | $Re = \dfrac{\rho v D_H}{\mu} = \dfrac{v D_H}{\nu}$ | (7.12) | 7.6, p. 176 | — |

## 2. Vazão e continuidade

| O que | Fórmula | Nº | Seção / página | Uso no TCC |
|---|---|---|---|---|
| Vazão em volume | $Q = V/t$ | (3.2) | 3.5, p. 72 | — |
| **Vazão × velocidade média** | $Q = v A$ | **(3.3)** | 3.5, p. 72 | passo 3 da dedução da Eq. 2.3 ($Q_t = A_1 v_1$) |
| Continuidade (fluido qualquer) | $\rho_1 v_1 A_1 = \rho_2 v_2 A_2$ | (3.12) | 3.6, p. 75 | — |
| **Continuidade (incompressível)** | $Q_1 = Q_2 \;\text{ou}\; v_1 A_1 = v_2 A_2$ | **(3.13)** | 3.6, p. 75 | **2ª parte da Eq. 2.2**; também justifica somar vazões no nó (Eq. 3.8) |

## 3. Energia (Bernoulli)

| O que | Fórmula | Nº | Seção / página | Uso no TCC |
|---|---|---|---|---|
| Hipóteses de Bernoulli | regime permanente; sem máquina; sem atrito; propriedades uniformes; incompressível; sem troca de calor | lista a)–f) | 4.3, p. 87 | justificar "escoamento que não muda com o tempo" na 2.4.2 |
| **Equação de Bernoulli** | $z_1 + \dfrac{v_1^2}{2g} + \dfrac{p_1}{\gamma} = z_2 + \dfrac{v_2^2}{2g} + \dfrac{p_2}{\gamma}$ | **(4.6)** | 4.3, p. 88 | **1ª parte da Eq. 2.2**: com $z_1 = z_2$ e multiplicando por $\gamma = \rho g$, sai $P_1 + \tfrac12 \rho v_1^2 = P_2 + \tfrac12 \rho v_2^2$ |
| Energia para fluido real | $H_1 = H_2 + H_{p1,2}$ | (4.19) | 4.6, p. 95 | ideia de "perda de carga" nas restrições |

## 4. Orifício e coeficiente de descarga (base da Eq. 2.3 e da R_F,D)

| O que | Fórmula | Nº | Seção / página | Uso no TCC |
|---|---|---|---|---|
| Velocidade teórica no orifício | $v_{2T} = \sqrt{2g\left(h + \dfrac{p_1 - p_2}{\gamma}\right)}$ | (8.7) | 8.5.1, p. 212 | — |
| Coeficiente de velocidade | $C_v = v_{2r}/v_{2T}$ | (8.9) | 8.5.1, p. 212 | perdas por atrito |
| Vazão teórica | $Q_T = v_{2T} A_o$ | (8.11) | 8.5.1, p. 212 | $Q_t$ |
| **Coeficiente de contração (veia contraída)** | $C_c = A_c/A_o$, com $C_c < 1$ | **(8.12)** | 8.5.1, p. 212 (Fig. 8.8) | *vena contracta* na 2.4.2 |
| Vazão real | $Q = C_v C_c Q_T$ | (8.14) | 8.5.1, p. 213 | — |
| **Coeficiente de descarga** | $C_D = Q/Q_T$, logo $C_D = C_v C_c$ | **(8.15)** | 8.5.1, p. 213 | **$C_D = Q_r/Q_t$ da 2.4.2** |
| **Lei do orifício** | $Q = C_D A_o \sqrt{2g\left(h + \dfrac{p_1 - p_2}{\gamma}\right)}$ | sem nº (logo após 8.15) | 8.5.1, p. 213 | com $h = 0$: $Q = C_D A_o \sqrt{2\Delta P/\rho}$ → **Eq. 3.1** ($q = K\sqrt{P}$) e **$R_{F,D}$ da Eq. 2.5** |
| Orifício no fim de tubo (com velocidade de aproximação) | $Q = \dfrac{C_D A_o}{\sqrt{1 - C_c^2 (D_o/D_1)^4}} \sqrt{2g\,\dfrac{p_1}{\gamma}}$ | sem nº (após 8.16) | 8.5.1, p. 213 | — |
| **Venturi** | $Q = \dfrac{C A_2}{\sqrt{1 - (D_2/D_1)^4}} \sqrt{2g\,\dfrac{p_1 - p_2}{\gamma}}$ | **(8.20)** | 8.5.2, p. 216 | **mesma forma da Eq. 2.3** (ver observação B) |

## 5. Perda de carga em tubos (base da R_F,T)

| O que | Fórmula | Nº | Seção / página | Uso no TCC |
|---|---|---|---|---|
| Perda distribuída = diferença de cargas | $h_{f1,2} = H_1 - H_2 = \Delta H$ | (7.6) | 7.3, p. 170 | — |
| Perda em trecho horizontal | $h_{f1,2} = \left(\dfrac{p_1}{\gamma} + z_1\right) - \left(\dfrac{p_2}{\gamma} + z_2\right)$ | (7.7) | 7.3, p. 170 | com $z_1 = z_2$: $\Delta p = \gamma\, h_f$ |
| **Fórmula universal (Darcy-Weisbach)** | $h_f = f\,\dfrac{L}{D_H}\,\dfrac{v^2}{2g}$ | **(7.10)** e (7.14) | 7.4, p. 173; 7.6, p. 176 | **$R_{F,T}$ da Eq. 2.5** (ver observação C) |
| Rugosidade relativa | $D_H/\varepsilon$ | (7.13) | 7.6, p. 176 | — |
| Fator de atrito laminar | $f = 64/Re$ (para $Re < 2000$) | (7.11) | 7.5, p. 175 | — |
| **Diagrama de Moody-Rouse** | $f = f(Re,\, D_H/k)$ | Figura 7.16 | 7.6, p. 176–177 | **$f_a$ "tirado do diagrama de Moody"** (2.4.3) |
| Perda singular (válvulas, conexões) | $h_s = k_s\,\dfrac{v^2}{2g}$ | (7.16) | 7.8, p. 184 | forma quadrática das perdas em válvulas, como a $R_{F,D}$ |
| Valores de $k_s$ | gaveta aberta 0,2; globo aberta 10; cotovelo 90° 0,9; retenção 0,5 | tabela | 7.8, p. 185 | opcional, para ilustrar |
| Comprimento equivalente | $h_{f_{eq}} = f\,\dfrac{L_{eq}}{D_H}\,\dfrac{v^2}{2g}$ | sem nº | 7.8, p. 185 | — |

---

## Observações para o texto

**A. Limites de Reynolds diferentes de Garcia.**
- O TCC (2.4.1) usa os de Garcia (2005) via Rosa: laminar < 1100 e turbulento > 3500.
- Brunetti (p. 69) dá 2000 e 2400.
- Os próprios Rosa et al. avisam que as faixas variam entre autores.
- Sugestão: citar os dois e dizer que os limites mudam conforme o autor. Na bancada, Re vai de cerca de 1700 a 9400, então o regime é turbulento na maior parte dos ensaios pelos dois critérios.

**B. A Eq. 2.3 do TCC e o Venturi (8.20) são a mesma expressão.** Basta dividir numerador e denominador por $A_1/A_2$:
$$A_1\sqrt{\frac{2\Delta P}{\rho[(A_1/A_2)^2-1]}} = \frac{A_2}{\sqrt{1-(A_2/A_1)^2}}\sqrt{\frac{2\Delta P}{\rho}}, \qquad (A_2/A_1)^2 = (D_2/D_1)^4$$
Com $\gamma = \rho g$, $2g\,\Delta p/\gamma = 2\Delta p/\rho$. Assim a Eq. 2.3 pode citar **(BRUNETTI, 2008, p. 216, Eq. 8.20)** como fonte original da forma.

**C. Como sai a $R_{F,T}$ da Eq. 2.5 a partir do Brunetti.** Em tubo horizontal, $\Delta p = \gamma h_f$ (Eq. 7.7). Com a Eq. 7.10 e $v = Q/A_i$ (Eq. 3.3):
$$\Delta p = \gamma f \frac{L}{D}\frac{v^2}{2g} = f\frac{L}{D}\frac{\rho v^2}{2} = \frac{f\,L\,\rho}{2\,D\,A_i^2}\,Q^2$$
O resultado é exatamente $R_{F,T}$, com $f_a = f$. Da mesma forma, a lei do orifício com $h = 0$ dá $\Delta p = \dfrac{\rho}{2C_D^2A_o^2}\,Q^2 = R_{F,D}\,Q^2$. As duas resistências da Eq. 2.5 saem, portanto, de fórmulas do Brunetti, sem precisar de "apud".

**D. O que o Brunetti não cobre:**
- a associação de resistências em paralelo (Eq. 2.8) não aparece como fórmula pronta;
- ela sai de Brunetti (Eq. 3.13), porque as vazões se somam no nó, mais a lei do orifício, com a mesma $\Delta p$ em todos os bicos;
- isso pode ser escrito como dedução própria, citando as duas.

**E. Mapa rápido: equação do TCC → citação sugerida.**

| TCC v10 | Citar |
|---|---|
| 2.1 Reynolds | BRUNETTI, 2008, Eq. 3.1, p. 69 (+ GARCIA/HUGHES) |
| 2.2 Bernoulli + continuidade | BRUNETTI, 2008, Eqs. 4.6 (p. 88) e 3.13 (p. 75) |
| 2.3 vazão real com $C_D$ | BRUNETTI, 2008, Eqs. 8.12–8.15 (p. 212–213) e 8.20 (p. 216) |
| 2.4–2.5 resistência ($R_{F,D}$, $R_{F,T}$) | BRUNETTI, 2008, lei do orifício (p. 213) e Eq. 7.10 (p. 173); Moody, Fig. 7.16 (p. 177) |
| 2.8 paralelo | dedução própria com Eq. 3.13 + lei do orifício |
| 3.1 $q = K\sqrt{P}$ | BRUNETTI, 2008, p. 213 (lei do orifício com $h = 0$) |
