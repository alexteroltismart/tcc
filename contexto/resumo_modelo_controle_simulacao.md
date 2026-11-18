# Resumo do modelo, da estratégia de controle e da simulação (v14)

Este resumo segue `contexto/14.md` (seções 3.3 a 3.7 e o Cap. 4) e o script `simulacao/modelo_barra.py`.

- Unidades: pressão em kgf/cm², vazão em L/min e tempo em s.
- Os números das equações são os da v14.

---

## 1. Sistema de referência

- **Bancada:** a de Rosa, Terra e Drews Jr (2019), com:
  - barra de 5 m e **7 bicos** FanTip 0,2/110°, cada um com uma solenoide liga-desliga;
  - **bomba de pistão** com uma válvula de controle de pressão por mola (**PCV**) que devolve o excesso ao tanque;
  - uma **válvula agulha** de alívio, movida por servomotor, que é o atuador do controle.
- **Dados usados:**
  - a Tabela 1: pressão e vazão para n = 1 a 7 bicos abertos, com a válvula de alívio fechada;
  - a Tabela 2: o ensaio manual com a válvula, usado só como comparação qualitativa.

## 2. Modelo estático (seção 3.3)

Três caminhos se encontram num único nó de pressão P:

```
Fonte (bomba + PCV) ──Q_s──► nó P ──Q_barra = nK√P──► n bicos (alvo)
                                 └──Q_v = K_v(α)√P──► válvula de alívio (volta ao tanque)
```

**Hipóteses**
- **H1:** escoamento permanente, líquido incompressível e barra horizontal.
- **H2:** perda de pressão ao longo da barra desprezível, então todos os bicos têm a mesma P.
- **H3:** bicos iguais, todos seguindo a lei de orifício.
- **H4:** a fonte (bomba, PCV e perdas antes da barra) é uma curva de 2º grau.
- **H5:** a válvula é linear, com K_v proporcional à abertura.

**Equações**

| Parte | Equação | Valor |
|---|---|---|
| Bico (lei de orifício) | q = K√P (3.1) | K = 0,425 (L/min)/√(kgf/cm²), média das 7 linhas da Tabela 1 (3.2) |
| Barra com n bicos | Q_barra = nK√P (3.3) | — |
| **Resistência equivalente (modelo do trabalho)** | **R_eq(n) = R₁/n², com R₁ = 1/K²** (3.4) | R₁ ≈ 5,54 com o K ajustado; 5,58 medido com 1 bico |
| Fonte (mínimos quadrados) | P = a₂Q² + a₁Q + a₀ (3.5–3.6) | a₂ = −0,0355; a₁ = −0,2018; a₀ = 5,815 |
| Fonte invertida (Bhaskara) | Q_s(P) (3.7) | Q_s = 0 se P ≥ a₀ |
| Válvula | Q_v = K_v(α)√P e K_v = K_v,max·α (3.8–3.9) | K_v,max = 3,5 (escolha de projeto) |
| **Ponto de operação** (balanço no nó) | **Q_s(P) = [nK + K_v(α)]√P** (3.10) | resolvida por **bissecção** em [0, a₀], 100 iterações |

**Validação**
- Os pontos medidos são reproduzidos com erro máximo de **0,7% na pressão e 2,3% na vazão**.
- Na validação cruzada "deixa um de fora", o erro máximo foi de **0,9% e 2,7%**.
- O modelo R₁/n² tem erro relativo máximo de 5,9%, contra 18,5% da fórmula empírica de 4 coeficientes de Rosa (Eq. 2.9).

**Consequências de projeto**
- A válvula de alívio só **baixa** a pressão, então P_ref precisa ser menor que a pressão com 7 bicos e a válvula fechada (3,56). Foi adotado **P_ref = 3,5 kgf/cm²**.
- O ganho da planta K_g = ∂P/∂α vale **−2,66 kgf/cm² para qualquer n**. Por isso uma única sintonia serve para todos os casos (3.13; consequência da H5).

## 3. Modelo dinâmico (seção 3.4)

- **H6, pressão instantânea:** a mangueira é curta e cheia, então a capacitância V/β é pequena. A cada instante, P é a pressão de equilíbrio da Eq. 3.10, e só a válvula tem dinâmica.
- **Atuador da válvula**, primeira ordem com limite de velocidade:
  - dα/dt = sat±ω_max[(α_c − α)/τ_a], com 0 ≤ α ≤ 1 (3.11);
  - τ_a = 0,2 s e ω_max = 0,5 s⁻¹ (curso completo em 2 s), os dois **estimados**;
  - longe do comando, a válvula anda em rampa; perto dele, aproxima-se de forma exponencial.
- **Integração:** método de Euler com Δt = 1 ms, α_{k+1} = α_k + Δt·(dα/dt)_k (3.12).

## 4. Estratégia de controle (seção 3.5)

**Papéis na malha**
- Variável controlada: a pressão P.
- Variável manipulada: a abertura α.
- Perturbação: o número de bicos abertos n(t), que o sistema de comando conhece.

**Erro:** e = P − P_ref. É o contrário do usual porque **abrir a válvula baixa P**.

**Os três controladores** saem de uma mesma lei discreta, executada a cada T_s = 50 ms:

```
I_k  = I_{k-1} + e_k·T_s            (3.16)  só se o comando não estiver no limite de posição (anti-windup)
α_c,k = α_ff(n_k) + K_c·(e_k + I_k/T_i)   (3.17)
```

| Controlador | Diferença | Ganhos (Ziegler-Nichols) |
|---|---|---|
| **P** | sem integral (T_i = ∞); α_ff trocado por uma abertura fixa α₀ | K_c = 0,5·K_cr = **1,46** |
| **PI** | com integral; α₀ fixo | K_c = 0,45·K_cr = **1,32**; T_i = P_cr/1,2 = **0,083 s** |
| **PI+FF** | com integral e *feedforward* | iguais aos do PI |

**Feedforward** (3.14): é o modelo estático invertido para P = P_ref.
- α_ff(n) = [Q_s(P_ref)/√P_ref − nK]/K_v,max.
- É uma reta: cada bico que fecha pede +0,121 de abertura.
- Com 7 bicos, α_ff = 0,023; com 1 bico, 0,752.

**Anti-windup:** integração condicional (Fernandes e Goldemberg, 2001). A soma I_k fica congelada quando o comando está no **limite de posição** e o erro pede para ir além. O limite de velocidade não congela o integrador.

**Sintonia, pelo 2º método de Ziegler-Nichols (ganho crítico)**, feita no próprio simulador:
1. só a ação P, com 7 bicos;
2. um bico fecha em t = 0,5 s;
3. bissecção em K_c, de 0,5 a 10, procurando o menor ganho que oscila sem parar.

Resultados:
- K_cr = **2,93** e P_cr = **0,100 s**, igual a 2·T_s;
- a oscilação vem da **amostragem**: a planta contínua sozinha não oscilaria;
- a teoria discreta dá K_cr = 3,02.

**Função de transferência** (seção 3.5.5, segundo Ogata). O modelo é linearizado em torno de n = 7 e P_ref, sem limite de velocidade e sem amostragem:

| Bloco | Função |
|---|---|
| Válvula | ΔA/ΔA_c = 1/(τ_a s + 1) (3.18) |
| Planta | ΔP = K_g·ΔA + K_n·ΔN, com K_n = ∂P/∂n = **−0,323** por bico (3.19) |
| PI | C(s) = K_c(1 + 1/(T_i s)) (3.20) |
| Malha fechada com distúrbio | ΔP/ΔN = K_n / [1 + C(s)\|K_g\|/(τ_a s + 1)] (3.21) |
| P | G_P = K_n(τ_a s + 1)/(τ_a s + 1 + K_c\|K_g\|) (3.22) |
| PI | G_PI = K_n T_i s(τ_a s + 1)/[τ_a T_i s² + T_i(1 + K_c\|K_g\|)s + K_c\|K_g\|] (3.23) |
| PI+FF | G_PI+FF = K_n τ_a T_i s²/[mesmo denominador] (3.24) |

O que as funções de transferência mostram:
- **Erro do P** pelo teorema do valor final: 0,323/(1 + 3,9) = **0,066 kgf/cm²**, igual à Eq. 2.14 e ao simulador (3,57).
- **O PI zera o erro**, por causa do s no numerador.
- **O FF não muda a estabilidade**, porque o denominador é o mesmo.
- Os polos do PI são **−11,3 ± j9,1**, com ω_n = 14,5 rad/s e ζ = 0,78, o que dá t_s ≈ 4/(ζω_n) = **0,36 s**.
- **Limite do modelo:** a função de transferência contínua seria estável com qualquer ganho, porque não vê a amostragem. Ela serve para entender a malha; a sintonia e os resultados vêm do simulador.

## 5. Simulação (seções 3.6 e 3.7)

**Programa:** `simulacao/modelo_barra.py`, em Python 3 com **só numpy e matplotlib**, sem biblioteca de controle. Leva cerca de 3 min e grava `resultados.json` e `figuras/`.

**Laço, a cada 1 ms:**
1. troca n se houver evento;
2. a cada 50 ms, roda o controlador (erro, anti-windup e comando pelas Eqs. 3.16–3.17);
3. move a válvula (Eqs. 3.11–3.12);
4. calcula a pressão pela bissecção da Eq. 3.10 (H6);
5. guarda os valores.

**Cenários** (C4, o de erro de modelo, foi retirado na v13):

| Cenário | Sequência | Duração |
|---|---|---|
| C1 | 7 → 1 → 7, um bico por vez, a cada 2 s | 26 s |
| C2 | 7 → 4 (t = 2 s) → 1 (t = 8 s): degraus de 3 bicos, como a Tabela 2 | 14 s |
| C3 | um bico sorteado troca a cada 0,1–0,5 s, com semente fixa (66 trocas) | 20 s |

**Configurações:**
- malha aberta, P, PI e PI+FF;
- C2 e C3 também com ω_max = 0,5, 1 e 2 s⁻¹.

**Métricas** (Eqs. 3.25–3.27):
- **faixa de tolerância ±10% em P** (ISO 16122-2, item 4.5.4), ou seja, de 3,15 a 3,85 kgf/cm². Corresponde a cerca de ±5% na vazão do bico;
- **tempo fora da faixa** (%), IAE, desvio máximo;
- **tempo de acomodação** em ±2%.

**Conferências automáticas**, que interrompem o script se falharem:
- K = 0,425 e os erros do ajuste;
- P_ref atingível;
- K_g igual para todo n;
- K_cr dentro de 5% do valor teórico e P_cr = 2T_s;
- K_c < K_cr e T_i ≥ T_s;
- K_n = K_g·K/K_v,max;
- polos lineares estáveis.

**Testes avulsos**, em `simulacao/testes_avulsos.py`:
- pressão com mangueira em vez de instantânea: diferença máxima de **0,6 ponto percentual**, e K_cr com mangueira ≈ 5,0;
- passo de 2 ms: diferença de ≤ 0,1 ponto; passo de 10 ms: o PI+FF muda 1,1 ponto;
- ruído de 1–2% no sensor: a válvula se move 2,5–3,4× mais do que com K_c = 0,33.

## 6. Principais resultados (Cap. 4)

**Tempo fora da faixa:**

| Cenário | Malha aberta | P | PI | PI+FF |
|---|---|---|---|---|
| C1 | 69,2% | 10,2% | **0,0%** | **0,0%** |
| C2 | 85,7% | 46,6% | 7,5% | **6,8%** |
| C3 | 90,5% | 26,9% | **8,9%** | 9,7% |

- **P:** deixa um erro permanente, previsto pela Eq. 2.14. Com 4 bicos a pressão fica em 3,70 kgf/cm² (a conta dá 3,71); com 1 bico, em 3,90, já fora da faixa.
- **PI:** zera o erro. Fica 100% do tempo na faixa no C1 e cerca de 91% no C3. O pico do C2 (cerca de 30%) é **instantâneo** e não depende do controlador; a válvula leva cerca de 0,9 s para corrigir.
- **PI+FF:**
  - ajuda nas trocas espaçadas (C1 e C2);
  - piora um pouco o C3, porque a válvula passa cerca de 77% do tempo na velocidade máxima e não chega à posição calculada antes da próxima troca;
  - com a válvula 4× mais rápida (ω_max = 2 s⁻¹), o FF volta a ajudar: no C3, 1,0% contra 1,4% do PI.
- **Gargalo:** a **velocidade da válvula**. A Figura 21 mostra a função de transferência contra o simulador: sem o limite de velocidade, o simulador segue a função de transferência; com o limite, a correção é bem mais lenta.

**Conclusão do trabalho:** a hipótese foi **confirmada em parte e só em simulação**. τ_a, ω_max e a curva da válvula foram estimados, e a validação com medições no tempo continua pendente.
