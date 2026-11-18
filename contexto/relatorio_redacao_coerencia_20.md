# Relatório de redação e coerência — versão 20

Data: 09/11/2026. Base: `contexto/20.md`, com todas as mudanças de hoje: 2.6.1 (linearização), ganho de malha na 2.6, Tabela 3 na 3.5.4, ponto de operação na 3.3.4 e na 3.5.2, e a abertura nova da 3.5.2. As linhas citadas são as do 20.md nesta data. Nenhuma alteração foi feita no texto.

**Critérios pedidos pelo autor:**
1. **Redação:** clareza, termos consistentes, repetição, ordem das ideias.
2. **Coerência:** o que um capítulo diz precisa bater com o outro.
3. **Regra principal:** *nenhum conceito novo deve surgir na metodologia*. Tudo o que o Cap. 3 usa como ferramenta precisa ter sido apresentado no Cap. 2.

Para o item 3, cada conceito usado no Cap. 3 foi procurado, por script, no texto inteiro, e foi anotado o lugar onde aparece pela primeira vez. A tabela da seção 2 resume o que saiu.

Legenda: 🔴 corrigir antes da entrega; 🟡 recomendado; 🟢 opcional.
Nas sugestões de citação: ✔ = trecho conferido no livro nesta sessão; [a conferir] = só pelo sumário.

---

## 1. Parecer geral

A linha do trabalho (problema → modelo → controle → simulação → conclusão) está clara, e as mudanças de hoje melhoraram a base do Cap. 3. Agora estão no Cap. 2 a linearização, o ponto de operação, o ganho de malha e a perturbação com referência nula.

Ainda há três problemas de fundo:
1. **A fundamentação não apresenta as ferramentas de controle que o Cap. 3 usa mais:** transformada de Laplace, função de transferência, sistema de 1ª ordem, estabilidade pelos polos e diagrama de blocos. Hoje a função de transferência é **usada** no Cap. 2 (2.6, 2.6.1 e 2.6.2) e só **definida** no Cap. 3 (3.5.4, l. 852).
2. **Os métodos numéricos e estatísticos só aparecem na metodologia:** mínimos quadrados, bissecção, Euler, diferença centrada, soma de retângulos, derivada implícita, validação cruzada, RMSE e R². O autor já tinha anotado o Euler e os mínimos quadrados.
3. **Kg e Kn estão deduzidos duas vezes:** pela derivada implícita na 3.5.2 e peça por peça na Tabela 3 da 3.5.4. A derivada implícita é justamente um conceito que não está no Cap. 2 (item C1).

---

## 2. Conceitos que surgem na metodologia sem base na fundamentação

| # | Conceito | Onde aparece primeiro | Gravidade | Sugestão (onde no Cap. 2 e o que citar) |
|---|---|---|---|---|
| N1 | **Transformada de Laplace e função de transferência** | Usada na 2.6 (l. 340), 2.6.1 e 2.6.2 (Eq. 2.10, $C(s)/R(s)$); definida só na 3.5.4 (l. 852) | 🔴 | Subseção curta antes da 2.6.1: a transformada leva derivadas em multiplicação por $s$, e a função de transferência é saída/entrada com condições iniciais nulas. Ogata p. 13 ✔ (já citado na 3.5.4); Castrucci seções 2.3 e 2.4 [a conferir]. A definição sai da 3.5.4, que passa a remeter ao Cap. 2. |
| N2 | **Sistema de 1ª ordem e constante de tempo** | 3.4.2 (válvula, Eq. 3.12) | 🔴 | Na mesma subseção de N1: $1/(\tau s + 1)$, 63,2% em $\tau$ e 2% em $4\tau$. Ogata p. 147 ✔; Castrucci seção 3.4 ✔. A 3.4.2 fica só com os números da válvula. |
| N3 | **Estabilidade pelos polos** (parte real negativa; coeficientes positivos no 2º grau) | 3.5.5, l. 940 ("estáveis com qualquer ganho positivo, porque todos os coeficientes… são positivos") | 🔴 | Uma frase na 2.6.2, que já fala de polos mas não diz quando a malha é estável. Castrucci seções 3.2 e 3.3 (Routh) [a conferir]. |
| N4 | **Diagrama de blocos** | 3.5, Figura 12 | 🟡 | A 2.6 já lista as partes da malha. Uma frase dizendo que elas se representam em blocos ligados por somadores e setas. Castrucci seção 2.6 ✔; Ogata p. 16–17 ✔. |
| N5 | **Derivada implícita / regra da cadeia** | 3.5.2, l. 785–799 | 🔴 | **Melhor solução: não precisar dela** (ver C1). Se ficar, uma linha na 2.6.1 dizendo que, quando a relação é dada por uma equação $F(x, y) = 0$, a derivada sai de $dF = 0$. |
| N6 | **Mínimos quadrados** (e equações normais) | 3.3.2 | 🟡 | Já anotado pelo autor. Chapra p. 393 ✔. |
| N7 | **Bissecção** | 3.3.4 | 🟡 | Mesma subseção de N6, "Métodos numéricos". Chapra p. 101–102 ✔. |
| N8 | **Método de Euler** | 3.4.3 | 🟡 | Já anotado pelo autor. Chapra p. 588 e 592 ✔. |
| N9 | **Diferença centrada** | 3.5.2, l. 831 | 🟢 | Hoje é só conferência; uma frase em N6–N8 basta. Chapra p. 75 ✔. |
| N10 | **Soma de retângulos (integral discreta)** | 3.5.3 | 🟡 | A Eq. 2.13 (anti-windup) **já é discreta** e usa $\Delta t$ sem explicar. Uma frase na 2.7.2 ou em N6–N8. Chapra p. 493 ✔; Castrucci seção 12.2.2 ✔. |
| N11 | **Validação cruzada, RMSE e R²** | 3.6.4 e 4.1 | 🟡 | A validação cruzada **não tem referência nenhuma** no texto. RMSE e R² aparecem só nos resultados. Sugestão: um parágrafo "Como avaliar o ajuste de um modelo". Chapra p. 384 ✔ para R²; para a validação cruzada, [REF. PENDENTE]. |
| N12 | **Capacitância hidráulica / compressibilidade** | 3.4.1 | 🟡 | O lugar natural é a 2.4.2, que já diz "Esse é um modelo estático… não o tempo que a pressão leva para mudar". Uma frase: o volume da linha e a compressibilidade dão um atraso $(V/\beta)\,dP/dt$. Merritt p. 53 ✔; Ogata p. 90–92 ✔. |
| N13 | **Limite de velocidade do atuador** | 3.4.2 | 🟡 | A 2.7.2 fala só do limite de posição. Uma frase: além do curso, o atuador tem velocidade máxima. Merritt p. 277 ✔. |
| N14 | **Amostragem / leitura a intervalos** | 3.5.3 ("sem intervalo de amostragem") e 3.8 | 🟡 | Uma frase na 2.6 sobre o controlador digital ler o sensor a cada período. Castrucci seção 12.6 ✔ (regra dos 10×). |
| N15 | **IAE** | 3.6.4 | 🟢 | A 2.6.2 já define $M_p$ e $t_s$; o IAE caberia ali como mais um critério de desempenho. Castrucci seções 9.2 e 9.8 [a conferir]. Hoje o IAE não tem citação. |
| N16 | **Realimentação negativa** | 3.5.5 | 🟢 | Uma oração na 2.6 ("Malha aberta e malha fechada"): a correção tem sinal oposto ao erro. |
| N17 | **Curva de carga** | 3.3.4 e 4.1 (Figura 17) | 🟢 | Uma frase na 2.4.3: a curva $P \times Q$ da barra é a curva de carga, e o ponto de operação é o cruzamento com a curva da fonte. |
| N18 | **Variável controlada / manipulada** | 3.5, l. 732 (Ogata p. 2–3) | 🟢 | A lista de partes da malha na 2.6 pode dar o nome: pressão = variável controlada, abertura = variável manipulada. |

**Não são problema:**
- tags ISA e PCV, porque descrevem a bancada (3.2);
- semente aleatória, que é detalhe do método;
- Bhaskara, que é matemática do ensino médio;
- ganho da planta e ganho do distúrbio, que são definições do próprio trabalho e aparecem na 2.6 com remissão.

**Caminho de menor esforço:** criar duas subseções curtas no Cap. 2.
- **2.6.x "Função de transferência e resposta de 1ª e 2ª ordem"**: cobre N1, N2, N3 e N4, juntando-se à 2.6.2.
- **2.8 "Métodos numéricos e avaliação do modelo"**: cobre N6 a N11.

As outras são frases soltas em seções que já existem. Estimativa: mais 900 a 1.200 palavras.

---

## 3. Coerência

🔴 **C1. Kg e Kn deduzidos duas vezes.** Na 3.5.2 (l. 785–829) saem pela derivada implícita de $F(P, C)$. Na 3.5.4, a Tabela 3 monta os mesmos valores somando as peças linearizadas. Isso contraria a decisão da v20 de calcular Kg "de um jeito só" (item 3 do plano), e a derivada implícita é um conceito novo na metodologia (N5).
- **Sugestão (recomendada):** a Tabela 3 e a conta da soma sobem para a 3.5.2 e viram **a** dedução. Ela usa só o que a 2.6.1 ensina: derivada de cada função no ponto de operação mais o balanço de vazões. A derivada implícita, com $F(P, C)$ e as Eqs. 3.15–3.17, sai ou fica numa frase como conferência. O denominador 2,462 continua com a mesma leitura física: saídas 0,817 mais fonte 1,645.
- **Ganho:** some um conceito novo, some uma dedução repetida, e a 3.5.4 fica só com a planta, a válvula e a remissão. A numeração do Cap. 3 muda (saem até 3 equações).

🟡 **C2. Ordem dentro da 3.5.** A 3.5.2 já faz a linearização (derivadas no ponto de operação), mas é a 3.5.4 que anuncia "o modelo foi linearizado". Quem lê em ordem vê a conta antes do motivo.
- Com C1 aplicado, basta a 3.5.2 começar com "Os ganhos são as derivadas da pressão no ponto de operação nominal, como na linearização da seção 2.6.1".
- A 3.5.4 deixa de repetir a ideia.

✅ **C3 (resolvido em 09/11, na revisão da Tabela 3: desvios no tempo com Δα e frase sobre Laplace antes da Eq. 3.21).** ~~"Letras maiúsculas = transformada de Laplace" × Tabela 3.~~ A 3.5.4 diz que $\Delta P(s)$, $\Delta A(s)$… são transformadas de Laplace (l. 845 e seguintes). A Tabela 3, logo abaixo, usa $\Delta A$ e $d\Delta A/dt$ **no tempo**.
- Sugestão: na Tabela 3 e na conta da soma, deixar claro que são desvios no tempo, por exemplo com "(no tempo)" na legenda, ou usar $\Delta\alpha$ para a abertura no tempo, como na 2.6.1, que usa $\Delta x$.
- Na Eq. 3.21, dizer em uma frase que a passagem para Laplace não muda os coeficientes, porque a relação é estática (linearidade da transformada, Castrucci seção 2.3.2).

🟡 **C4. Ação derivativa justificada duas vezes.** Está na 2.6 (l. 348–353: ruído, saltos e dois polos) e de novo na 3.5.6 ("Por que não há ação derivativa"). Ficar só com a 2.6 e tirar o parágrafo da 3.5.6.

🟡 **C5. Remissão desatualizada na 2.6, l. 330:** "($K_g$ é **medido** na seção 3.5.2…)". Desde a v20, Kg é **calculado**. Trocar para "calculado".

🟡 **C6. Por que comparar P, PI e PI+FF não está dito.** A 2.6 (l. 342–346) lista os três e o papel de cada um, mas a metodologia não explica a lógica da escada: um elemento novo por vez, com os mesmos ganhos. Só a 3.5.6 fala disso, e apenas para P × PI. A proposta de parágrafo para o início da 3.5.3 foi feita antes e não foi aplicada.

🟢 **C7. "Ponto de operação" ainda sem o "nominal" na 3.5.4,** l. 843: "Ponto de operação. É o da seção 3.5.2…". Trocar por "É o ponto de operação nominal da seção 3.5.2".

🟢 **C8. A Figura 17, citada na 3.3.4, está no Cap. 4.** A remissão adiante é aceitável, mas quem lê em ordem ainda não viu a figura. Alternativa: dizer só "o cruzamento da curva da fonte com a curva de carga da barra" e deixar a figura para a 4.1.

---

## 4. Terminologia (mesma coisa com nomes diferentes)

| Termo | Uso hoje | Sugestão |
|---|---|---|
| "ganho **da** malha" × "ganho **de** malha" | 1 × 13 | Uniformizar para **ganho de malha**. |
| "distúrbio" × "perturbação" | 13 × 27 | Escolher um. O Castrucci usa **perturbação**, e a 3.5.5 já se chama "bicos como perturbação". Manter "ganho do distúrbio" para $K_n$ cria dois nomes para a mesma coisa. Sugestão: dizer uma vez na 2.6 que "perturbação, ou distúrbio" são a mesma coisa, ou renomear $K_n$ para "ganho da perturbação". |
| "abertura **antecipada**" × "abertura **de equilíbrio**" para $\alpha_{ff}$ | 2 × 8 | Usar **abertura de equilíbrio** também na 3.5.3 (l. 841) e no Quadro 2 (l. 1139, `alpha_ff`). |
| "compensação antecipativa" × *feedforward* × "alimentação avante" (Castrucci) | 13 × muitos × 0 | Na 2.7.1, dizer os três nomes uma vez, porque o Castrucci, agora citado, usa "alimentação avante". Depois manter *feedforward*. |
| "referência" × "valor desejado" × *setpoint* | 37 × 6 × 1 | Está bem: "valor desejado" explica "referência", e *setpoint* aparece só na definição. Nenhuma mudança. |

---

## 5. Redação

🟡 **R1. Repetições que continuam desde o relatório de cortes da v17.** O autor não escolheu cortá-las, mas pesam na leitura:
- a bancada e a HV são apresentadas de novo na 3.2 (lista, legendas das Figuras 6–8 e caminho da Figura 9);
- o balanço no nó está na 3.2 (l. 526), na 3.3 (lista da Figura 11) e na 3.3.4;
- o laço da simulação aparece três vezes: na lista da 3.6.2, na Figura 15 e no Quadro 4;
- os números da Tabela 10 são relidos na 4.5, na 4.6 e na Conclusão.

Sugestão mínima: transformar as listas da 3.3 (Figura 11) e da 3.6.2 em frases que remetem à figura.

🟡 **R2. Densidade de remissões.** Muitas frases têm duas ou três remissões entre parênteses ("(seção 3.5.3)", "(Equação 2.9)", "(seções 3.5.1–3.5.2)"), sobretudo na abertura nova da 3.5.2 e na 3.5.5. Manter só a remissão que o leitor precisa seguir para entender a frase.

🟢 **R3. Parágrafos de leitura de figura.** "Na Figura X, …" aparece após quase todas as figuras e às vezes repete a legenda (Figuras 5–8, 16, 17, 19–21). Manter só o que a figura não mostra sozinha.

🟢 **R4. 2.6.1, parágrafo do Ogata p. 93.** É o único da subseção que não é usado depois, porque o texto não usa resistência linearizada. Pode virar uma frase dentro do parágrafo anterior, ou sair.

🟢 **R5. Frases longas com várias ideias:**
- a abertura nova da 3.5.2 (l. 776) tem 5 ideias numa frase;
- "Quando os blocos têm dinâmica…" (l. 340) tem 4.

Dividir em duas frases cada.

---

## 6. Ordem sugerida

| Prioridade | Itens | Muda numeração? | Esforço |
|---|---|---|---|
| 1 | C5, C7, terminologia (seção 4) | Não | Baixo |
| 2 | **C1** + C2 + C3 (Tabela 3 vira a dedução de Kg e Kn; sai a derivada implícita) | Sim (Cap. 3) | Médio |
| 3 | **N1–N4** (Laplace, FT, 1ª ordem, estabilidade, blocos no Cap. 2) | Sim (Cap. 2, se as equações forem numeradas) | Médio |
| 4 | N6–N11 (métodos numéricos e avaliação do modelo no Cap. 2) | Não, se as equações ficarem sem número | Médio |
| 5 | N12–N18, C4, C6, R1–R5 | Não | Baixo a médio |

**Observação:** os itens 3 e 4 mexem no Cap. 2, que na v20 o autor pediu para tocar "só no necessário". Pelo critério deste relatório (nada novo na metodologia), eles são o que falta para cumprir a regra. A decisão é do autor.
