# Merritt (1967) — trechos citáveis no TCC

**Referência (ABNT):** MERRITT, H. E. **Hydraulic control systems**. New York: John Wiley & Sons, 1967. A entrada já está nas Referências do TCC.

**Arquivo e páginas:**
- `referencias base/Hydraulic Control Systems -- Herbert E Merritt -- K1 Version.pdf`, digitalizado e **sem camada de texto**. Ler as páginas como imagem.
- Página do livro = página do PDF − 8.
- Tudo abaixo foi conferido na imagem da página em 04/11/2026.
- Citação: (MERRITT, 1967, p. X).

| O que | Conteúdo (como no livro) | Nº | Seção / página | Uso no TCC (v14) |
|---|---|---|---|---|
| Módulo de compressibilidade efetivo | O líquido, o ar preso e o recipiente (mangueiras, carcaças) se combinam como resistências em paralelo: $1/\beta_e = 1/\beta_c + 1/\beta_l$. A principal fonte de complacência mecânica são as **linhas hidráulicas** | (2-14) a (2-22); (2-23) para tubo de parede grossa | 2-5, p. 14–16 | 3.4: a mangueira estica e o líquido se comprime |
| **Continuidade com compressibilidade** | $\sum Q_{in} - \sum Q_{out} = \dfrac{dV_0}{dt} + \dfrac{V_0}{\beta}\dfrac{dP}{dt}$. O segundo termo é a vazão de compressibilidade, que descreve a vazão resultante das mudanças de pressão | **(3-53)** | 3-8, p. 52–53 | 3.4.1 (H6): o termo $V/\beta$ é a capacitância desprezada; também a conferência com mangueira (4.2) |
| Resistências usadas na análise dinâmica | Em geral só as resistências inseridas de propósito (orifícios) entram na análise dinâmica; as de tubos, curvas e conexões costumam ser desprezadas | texto | 3-8, p. 52 | H2: perda na tubulação desprezada |
| Orifício de área fixa ou variável | "an orifice is a sudden restriction of short length… and may have a fixed or variable area" | texto | 3-4, p. 39 | 3.3.3: a válvula como orifício de área variável |
| **Equação do orifício** | $Q = C_d A_0 \sqrt{\dfrac{2}{\rho}(P_1 - P_2)}$; Bernoulli e continuidade entre a montante e a veia contraída (3-29 a 3-31) | **(3-33)**, (3-34) | 3-4, p. 41 | 3.3.1 e 3.3.3: $q = K\sqrt P$ e $Q_v = K_v\sqrt P$ |
| $C_d$ típico | $C_d \approx 0{,}60$ para orifícios de aresta viva em escoamento turbulento | (3-35) | 3-4, p. 42 | 2.4.2 (opcional) |
| Válvulas de alívio e de vazão | Válvulas de segurança ou alívio "usually a spring loaded ball or poppet"; válvulas de controle de vazão vão "from simple two-way **needle**, globe, and gate valves" até válvulas compensadas | texto | 11-1, p. 321 | 3.3.2 (PCV por mola) e 3.3.3 (válvula agulha) |
| Válvula de alívio de um estágio | A pressão sentida é comparada com a força da mola; a diferença move o carretel, que controla a vazão para manter a pressão | (11-1) a (11-4) | 11-2, p. 321–323 | 3.3.2 (PCV) |
| **Fonte regulada por desvio (*bypass*)** | Com bomba de **deslocamento fixo**, o regulador "bypass the flow not being used by the load" para manter a pressão; **"The common relief valve is of this variety"**. Tem a desvantagem de circular a vazão inteira pela válvula de alívio quando não há carga | texto; Fig. 12-4 (p. 338) | 12-1 e 12-2, p. 337–338 | 3.3.2 / H4: bomba de pistão + PCV como fonte cuja pressão cai com a vazão; também a válvula de alívio como atuador (2.3) |
| Saturação | "The most common nonlinearity in control systems is saturation" | Fig. 10-3 | 10-3, p. 277 | 3.4.2 (limites de posição e velocidade) e 2.7.2 |

## Observações

- Merritt usa unidades inglesas (psi, in.³/s). As equações citadas são independentes de unidade.
- A Eq. 3-53 é o argumento formal da H6. Com volume fixo, a pressão só demora para mudar por causa do termo $(V_0/\beta)\,dP/dt$. Numa mangueira curta e cheia, $V_0/\beta$ é pequeno, e a pressão acompanha a válvula quase na hora.
- A p. 337 é o melhor apoio para a interpretação da fonte (H4). O texto do artigo de Rosa não explica por que a vazão cai com a pressão; o Merritt mostra que esse é o comportamento esperado de uma bomba fixa com válvula de alívio em desvio.
