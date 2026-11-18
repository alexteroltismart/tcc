# Contexto — Steward & Humburg (2000): modelagem do Raven SCS-700 com controle do carreador

Arquivo: `referencias base/Steward_2000_ModelingRavenSCS700.pdf` (15 p.).

- **Título:** Modeling the Raven SCS-700 Chemical Injection System with Carrier Control with Sprayer Simulation
- **Autores:** Brian L. Steward (Iowa State University) e Dan S. Humburg (South Dakota State University). O trabalho vem da dissertação de mestrado de Steward (1994, SDSU).
- **Publicação:** *Transactions of the ASAE*, v. 43, n. 2, p. 231–245, 2000. Avaliado pela Power & Machinery Division da ASAE. Apoio da Raven Industries.
- **Relação com o meu TCC:** é a **origem do modelo `ΔP = K·Q²`** usado por Rosa, Terra & Drews (2019) na eq. (13), que cita "o conceito de Steward & Humburg (2000)". Diferente do Rosa, este artigo **tem dinâmica, atuador, controlador em malha fechada e simulação**, que é exatamente o que falta ao Rosa (ver `Rosa_Terra_Drews_2019_barra_pulverizacao.md` §6d). É a referência de método mais próxima do que o meu TCC precisa fazer.

---

## 1. Ideia do artigo
Na **injeção direta**, o defensivo (*chemical*) é injetado na água (*carrier*) já na linha, em vez de vir pré-misturado no tanque. Sem controle do carreador, a vazão de água fica constante e só a injeção varia com a velocidade. O problema é o **atraso de transporte** do ponto de injeção até os bicos (Koo et al., 1987; Way et al., 1992; Sudduth et al., 1995). Com **controle do carreador**, a vazão de água e a de defensivo mudam juntas, mantendo a concentração e reduzindo esse efeito. Porém as **dinâmicas diferentes** dos dois subsistemas criam variações transitórias de concentração, e ninguém tinha modelado isso.

**Objetivos:**
1. modelar o subsistema químico do SCS-700 e projetar um controlador para ele;
2. modelar o subsistema do carreador;
3. simular três tipos de pulverizador com e sem controle do carreador;
4. identificar os componentes e as variáveis que limitam o desempenho.

Hipótese: os dois subsistemas são **dinamicamente desacoplados**. Ela foi verificada em ensaio (§2).

Referência de tolerância: o **USDA (1989) recomenda erro de aplicação ≤ 5%** da dose; levantamentos de campo mostram erros bem maiores (Rider & Dickey, 1982; Ozkan, 1987; Grisso et al., 1988).

## 2. Subsistema químico (bomba injetora)
- **Bomba de pistão** de curso ajustável (deslocamento positivo): vazão ∝ rotação do eixo. Acionada por **motor CC de ímã permanente** (Stature Electric 5075-005) via correia dentada.
- **Carga da bomba** modelada como torque linear na velocidade (`m_s`) e na pressão de saída (`m_p`). Levantado em bancada (Fig. 2) com 100–1700 rpm e 0–689 kPa. Inércia da bomba desprezada frente ao atrito. Não houve interação entre velocidade e pressão.
- **Sensores:** tacogerador CC (realimentação proporcional, filtro passa-baixas de 10,8 Hz contra ruído de comutação) e sensor de dente de engrenagem Hall com 27 dentes (posição/frequência).
- **Controlador:** **PI por PLL** (*phase-locked loop*, Geiger, 1981). A referência é uma onda quadrada com a frequência desejada do sensor de dentes. Ela incrementa um contador e a realimentação decrementa: **o contador é o integrador** do erro. Saída por DAC → amplificador diferencial (subtrai o tacômetro) → **PWM de 6 kHz em ponte FET** no motor. Implementado em hardware.
- **Modelo (Fig. 3):** contínuo (quantização desprezada). A malha fechada é de **4ª ordem**, polos em −607, −36,9 ± j179 e **−2,28 (dominante)**, zero em −68.
- **Validação:** tempo de subida 10–90% **simulado 0,95 s × medido 0,9 s** (degraus 260 ↔ 990 rpm). O tempo não mudou com pressão de 0 a 1241 kPa nem com o curso da bomba → controle robusto à carga e evidência de desacoplamento entre os subsistemas.

Tabela 1 (parâmetros do subsistema químico): H₁ = 7,34; H₂ = 0,04 V/bit; filtro 68 rad/s; polias 22/36 e 1,5; K_V1 = 0,0429 V/(rad/s); motor: ganho elétrico 172,7 N·m/V·s, polo elétrico 610 rad/s, ganho mecânico 5,10 (rad/s²)/mN·m, polo mecânico 1,0 rad/s; m_s = 1,34 mN·m/(rad/s); m_p = 0,613 mN·m/kPa.

## 3. Subsistema do carreador (hidráulica) — a parte que mais me interessa
Bancada (Fig. 4): **bomba centrífuga** Hypro 9202C movida por motor CA, **válvula borboleta de 1"** (Raven 445) acionada por motorredutor CC, fluxômetro de turbina Raven RFM55, **5 reguladores de vazão** (Spraying Systems 4916-250) fazendo papel de bicos, mangueiras de 1 1/4" e 3/4", tanque de 50 gal.

**Lei de orifício turbulento para todos os componentes, exceto a bomba** (Merritt, 1967):

| eq. | expressão | significado |
|---|---|---|
| (1) | `Q = C_D·A₀·√(2ΔP/ρ)` | orifício turbulento |
| **(2)** | **`ΔP = K_Q·Q²`**, com `K_Q = ρ/(2·C_D²·A₀²)` | coeficiente pressão-vazão [kPa/(L/min)²] de cada componente |
| (3) | `K_QV(θ) = A·exp(c₃θ³ + c₂θ² + c₁θ)` | válvula: K em função do ângulo do disco θ (ajuste polinomial de ln K) |
| (4) | `P_PUMP = a₂Q² + a₁Q + a₀` | curva da bomba centrífuga (2ª ordem) |
| (5) | `P_PUMP = ΔP_V + ΔP_N + ΔP_FM + ΔP_P` | equação de malha: bomba = válvula + bicos + fluxômetro + tubulação |
| **(6)** | `a₂Q² + a₁Q + a₀ = [K_QV(θ) + K_QN + K_QFM + K_QP]·Q²` | resolvida pela fórmula de Bhaskara (raiz positiva) → Q(θ) |

- **Bicos em paralelo:** `K_QN = K_bico / 5²`, "pois K_Q é inversamente proporcional ao quadrado da área". É a mesma conclusão que tirei da Tabela 1 do Rosa (`R_eq(n) = R₁/n²`), agora com fonte publicada.
- **Valores (Tabela 2):** K_QN = 0,012; **K_QP (tubulação) = 0,022**; K_QFM = 0,0011; K_QV de 7,5·10⁻⁴ (aberta) a 4,6 kPa/(L/min)². Bomba: a₂ = −0,0086 kPa/(L/min)², a₁ = 0,22 kPa/(L/min), a₀ = 364,4 kPa. Válvula: A = 7,54·10⁻⁴ kPa/(L/min)², c₃ = −5,98447·10⁻⁶ °⁻³, c₂ = 1,7727·10⁻³ °⁻², c₁ = −0,01418 °⁻¹.
- **Fluxômetro:** 72 pulsos/galão, período de 0,83 s a 0,015 s. Na simulação a amostragem foi fixada em **0,2 s** (pior caso para Q > 15 L/min). Isso vira um limitante sério (§5).
- **Motor da válvula:** modelo em **espaço de estados** de 3 estados (corrente de armadura, velocidade do rotor, ângulo do disco), eq. (7), com saída não linear `Q = F(x₃)`, eq. (8). Discretizado por exponencial de matriz com T = 0,2 s (Franklin et al., 1990). R_a = 18,6 Ω, L_a = 24,9 mH, K_T = 98,3 mN·m/A, K_V2 = 0,0983 V/(rad/s), J_m = 0,00925 mN·m·s², B_m = 0,00847 mN·m·s, redução 1/1263.
- **Saturação:** o motor só recebe a tensão do sistema (12 V), então a **velocidade angular da válvula é limitada** (0,9 rpm no eixo da válvula).
- **Controlador:** **proporcional amostrado**, com ZOH: `v_a2 = G₁·K_FM·(Q_ref − Q)`, saturado em ±12 V, eq. (9). Só simulado, não implementado.
- **Validação:** Q(θ) do modelo bate com o medido em 9 ângulos (Fig. 9: ~95 L/min aberta, caindo para ~5 L/min a 90°). Rise time simulado ≈ rise time do controlador comercial Raven (Tabela 3).

## 4. Resultados dos controladores
- **G₁ = 20**, degrau 18,9 → 56,8 L/min: subida ≈ 2,5 s, pequeno sobressinal, erro em regime nulo.
- **G₁ = 40**, mesmo degrau: **mesma subida** (atuador saturado, válvula girando na velocidade máxima) e **oscilação** em regime. Em degrau menor (18,9 → 28,4 L/min), G₁ = 40 é estável. Como o sistema é não linear, **a estabilidade depende do ganho e do ponto de operação da válvula**; não dá para falar em estabilidade global.
- **Três limitações de hardware:** (1) saturação de tensão → velocidade máxima da válvula; (2) taxa lenta de leitura do fluxômetro; (3) relação não linear entre ângulo, pressão e vazão.
- **Tabela 3:** o controlador Raven tem subida parecida com a do P simulado, mas acomodação maior, porque "empurra" o motor devagar perto do setpoint. Dobrar a velocidade da válvula (1,8 rpm) **corta a subida pela metade**, mas com G₁ = 20 o sistema fica **instável** em 3 dos 5 degraus; foi preciso cair para G₁ = 10. **Atuador mais rápido exige ganho menor ou amostragem mais rápida** (atraso na malha).

## 5. Simulação dos pulverizadores
- **Três configurações** de Way et al. (1992): barra particular (*private broadcast*), barra comercial (*commercial broadcast*) e aplicação em faixa (*private band*). Diferem em velocidade e no layout da tubulação e dos bicos (Grisso et al., 1988).
- **Cenário:** rampa de velocidade de 1,6 km/h/s até +30% (≈ variação máxima de vazão que mantém o padrão do bico, segundo Ayers et al., 1990). Velocidade amostrada a cada 0,1 s e média por período do controlador. Atraso de transporte calculado por bico (método de Way et al., 1992), sem difusão do produto na água.
- **Métrica:** **% da área com erro de taxa > 5%** em 402 m percorridos (Figs. 11–16 são superfícies de erro × distância × posição na barra).

**Tabela 4 (resumo, % de área inaceitável):**

| configuração | barra particular | barra comercial | faixa |
|---|---|---|---|
| baseline (com carreador, 0,5 s, 0,9 rpm) | 1,37 | 4,02 | 1,29 |
| **sem controle do carreador** | 2,69 | **7,80** | 5,60 |
| velocidade amostrada a 0,3 s | 1,12 | 0,23 | 1,15 |
| velocidade amostrada a 0,1 s | 0,64 | 0,00 | 1,08 |
| válvula a 3,5 rpm (G₁ = 10) | 1,34 | 2,56 | 1,00 |
| válvula a 1,8 rpm | 1,36 | 2,92 | 1,00 |
| 0,1 s + 1,8 rpm | **0,12** | **0,17** | **0,79** |

- Sem controle do carreador, os resultados batem com Way et al. (1992): 8,9 / 2,7 / 5,1%. Logo, **o atraso de transporte domina** o erro nesse caso.
- A variação de concentração causada pela diferença de dinâmica entre os subsistemas ficou em **~4,5% no máximo** (Fig. 17), dentro da tolerância e pequena perto dos erros de atraso e amostragem.

## 6. Conclusões (dos autores)
1. O modelo do subsistema químico prevê a resposta ao degrau e ela não depende da pressão.
2. O modelo hidráulico não linear descreve bem a relação vazão × ângulo da válvula.
3. A **saturação de tensão limita a velocidade da válvula** e, portanto, a rapidez das mudanças de vazão; a **taxa de leitura do fluxômetro** limita quanto se pode acelerar a válvula sem instabilidade.
4. Injeção com controle do carreador é superior à injeção simples, por causa do atraso de concentração.
5. Os dois controladores não precisam ter dinâmica idêntica, mas a diferença deve ser minimizada.
6. Amostrar a velocidade mais rápido e acelerar a válvula reduz o erro; acelerar demais a válvula leva à instabilidade por causa da amostragem lenta da vazão.

Limitação reconhecida: o modelo do carreador é **específico da bancada**, mas **a metodologia é aplicável** a outras configurações. A faixa de atuação do controle do carreador é limitada pela faixa de pressão útil dos bicos; os autores citam os **bicos modulados/PWM** (Giles et al., 1996) como forma de ampliá-la.

---

## 7. Observações minhas (úteis para o TCC)

**a) Esta é a estrutura de modelo que eu devo seguir.** Bomba (curva de 2ª ordem) = soma dos `K·Q²` de válvula, bicos, fluxômetro e tubulação, eq. (6). Para o meu caso:
- `K_QN` vira **função do número de bicos abertos**: `K_QN(n) = K_bico/n²`, ligando direto com o estado de cada bico que vem nos logs;
- o atuador pode ser a válvula (como aqui) ou a **rotação da bomba** (os coeficientes a₀, a₁, a₂ escalam com a rotação pelas leis de afinidade; preciso de fonte para isso);
- a equação de malha continua sendo resolvida por Bhaskara a cada passo de simulação.

**b) Conferência do modelo com os números da Tabela 2.** Válvula toda aberta: ΣK = 0,00075 + 0,012 + 0,022 + 0,0011 = 0,03585. Então `0,04445·Q² − 0,22·Q − 364,4 = 0` → **Q ≈ 93 L/min**, coerente com os ~95 L/min da Fig. 9 em 0°. A pressão nos bicos fica em 0,012·93² ≈ **104 kPa (~1 bar)**. Os parâmetros do artigo são consistentes e servem de **exemplo numérico** para testar a minha implementação antes de usar dados da Jacto.

**c) Aqui a tubulação NÃO é desprezível:** K_QP = 0,022 é quase o dobro de K_QN = 0,012. No Rosa a perda ao longo da barra saiu desprezível. A diferença vem da escala (≈ 90 L/min aqui × ≤ 5,6 L/min lá). Numa barra comercial de 27–36 m com dezenas de bicos, a vazão total fica mais perto deste caso. Argumento para incluir a tubulação no meu modelo.

**d) Lições de controle para o meu projeto:**
- modelar **saturação do atuador** (velocidade máxima da válvula ou rampa/limite de rotação da bomba); ela domina o tempo de subida e esconde ganho alto demais;
- modelar o **período de amostragem do sensor de vazão** e o atraso na malha; foi o que gerou instabilidade quando aceleraram a válvula;
- o controlador deles é só **P**. Um **PI/PID** com anti-windup é a evolução natural e justifica o meu TCC. O PLL do subsistema químico já é um PI e pode ser citado como exemplo de integrador por contador;
- tratar a estabilidade **por ponto de operação** (linearizar em torno de θ e de n bicos abertos), já que o sistema não é globalmente linear.

**e) Diferença de problema:** o artigo trata de mudança de **velocidade** (vazão total varia ±30% e todos os bicos abertos). O meu trata de **abertura/fechamento bico a bico**, que muda a carga hidráulica (`K_QN`) de forma abrupta. Isso é uma perturbação na planta, não uma mudança de referência, e é mais rápido que a rampa de velocidade deles.

**f) Métrica reaproveitável:** "% da área com erro > 5%" (tolerância USDA) é uma boa métrica para os mapas de taxa aplicada (`rate_lha` nos GeoTIFFs) e para comparar controladores na simulação.

**g) Referências daqui que valem buscar:**
- **Merritt (1967)**, *Hydraulic Control Systems*: base da lei de orifício;
- **Franklin, Powell & Workman (1990)**, *Digital Control of Dynamic Systems*: discretização;
- **Giles, Henderson & Funk (1996)**: controle digital de vazão e gota com bicos PWM, ponte para o modo "Localizada PWM" dos logs;
- **Way et al. (1992)** e **Sudduth et al. (1995)**: atraso de transporte;
- Gebhardt et al. (1974): primeiro controle automático de pulverizador;
- **USDA/EPA (1989)**: origem da tolerância de 5%.

## Como citar (ABNT)
STEWARD, B. L.; HUMBURG, D. S. Modeling the Raven SCS-700 chemical injection system with carrier control with sprayer simulation. **Transactions of the ASAE**, St. Joseph, v. 43, n. 2, p. 231-245, 2000.

O DOI não aparece no PDF. Antes de citar, preciso confirmá-lo na ASABE Technical Library, pelo título.
