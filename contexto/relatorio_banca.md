# Relatório de melhorias — leitura pela ótica da banca

Base: `contexto/06.md` e `simulacao/modelo_barra.py` (versão de 26/10/2026).
Os números marcados com **[teste]** vieram de rodadas rápidas do script feitas para este relatório e ainda não estão no 06.md.

Prioridade:
- 🔴 a banca quase certamente vai perguntar ou criticar;
- 🟡 fortalece bastante o trabalho;
- 🟢 acabamento.

---

## 1. Pontos críticos (🔴)

### 1.1 Os parâmetros dinâmicos são assumidos, e o valor de $C_h$ pode estar alto demais

**Críticas prováveis da banca:**
- "Seus resultados dinâmicos dependem de quatro números que você escolheu."
- "De onde veio 8 mL/(kgf/cm²)?"

**Problema.** $C_h$ foi escolhido para dar $\tau_p$ ≈ 0,2 s, sem justificativa física.

**Estimativa de ordem de grandeza.** A capacitância vale $C_h = V/\beta_{ef}$.
- Faixas usadas:
  - mangueira de 5 m com diâmetro interno de 10 a 13 mm, o que dá V ≈ 0,4 a 0,7 L;
  - módulo volumétrico efetivo de mangueira com água de 100 a 1000 MPa (faixa a confirmar em literatura de hidráulica).
- Resultado: $C_h$ ≈ 0,04 a 0,7 mL/(kgf/cm²), de **10 a 200 vezes menor** que o valor adotado.
- Bolhas de ar ou acumulador aumentam $C_h$, mas isso também precisa ser justificado.

**Efeito do $C_h$ menor [teste].** Com sintonia recalculada para cada $C_h$:

| $C_h$ [mL/(kgf/cm²)] | Configuração | C1: desvio máximo | C2: desvio máximo | C3: tempo fora da faixa |
|---|---|---|---|---|
| 8 (base) | PI+FF | 3,6% | 16,9% | 3,0% |
| 2 | PI+FF | 6,0% | 24,0% | 6,8% |
| 0,5 | PI+FF | 8,0% | 27,6% | 8,6% |
| 0,5 | PI | 9,6% | 29,5% | 35,5% |

**O que muda e o que se mantém:**
- A ordem entre as configurações se mantém: PI+FF é melhor que PI, que é melhor que malha aberta.
- O número de 97% do Resumo cairia para cerca de 91%.
- Com $C_h$ = 0,5, a sintonia SIMC dá $T_i$ = 12 ms, menor que $T_s$ = 50 ms. Um PI discreto com $T_i < T_s$ é tecnicamente questionável, e a banca de Engenharia Elétrica pode notar.

**Melhorias:**
1. Incluir no texto (3.4 ou 3.6) a estimativa física de $C_h$, com uma referência de hidráulica consultada diretamente, como Merritt (1967) ou Garcia (2005).
2. Estender a análise de sensibilidade C4 para baixo, até 0,5 mL/(kgf/cm²). Rodá-la em **C2 e C3**, não só em C1: hoje a sensibilidade usa só o cenário mais fácil.
3. Adotar como caso base um valor fisicamente justificado. Se a linha for muito rígida, a conclusão passa a ser: "o desempenho é limitado pelo atuador, não pela linha". Esse resultado é até mais interessante.
4. Justificar $\tau_a$ e $\omega_{max}$:
   - a válvula agulha de Rosa é acionada por servomotor;
   - a velocidade típica de servo é da ordem de 0,1 a 0,2 s/60°;
   - uma válvula agulha precisa de várias voltas de curso.

   Desses três fatos sai um $\omega_{max}$ defensável, ou o argumento de que a válvula agulha é lenta demais e outra válvula seria necessária.
5. Justificar $T_s$ = 50 ms pelo ATmega2560 da bancada e pela taxa do transmissor de pressão.

### 1.2 O modelo estático foi identificado e validado com os mesmos 7 pontos

**Crítica provável:** "Você ajustou 4 parâmetros ($K$, $a_2$, $a_1$, $a_0$) em 7 pontos e mediu o erro nesses mesmos pontos."

O texto já reconhece isso na seção 4.1 (Ressalvas), mas não oferece nenhuma mitigação.

**Melhoria.** Fazer **validação cruzada leave-one-out**: ajustar com 6 pontos e prever o sétimo, repetindo 7 vezes.
- É barato: cerca de 15 linhas no script.
- Rende uma tabela de erro de predição, que tem muito mais peso que o erro de ajuste.
- Se o erro continuar abaixo de 1–3%, o argumento fica sólido.

### 1.3 A curva da fonte não tem explicação física

**Crítica provável:** "Bomba de pistão tem vazão constante. Por que a vazão caiu de 5,6 para 1,0 L/min?"

A seção 3.3 diz "provavelmente alguma regulação interna... que o artigo não descreve". É honesto, mas fraco diante de uma banca.

**Melhorias:**
- Levantar e discutir as hipóteses concretas. Um parágrafo bem argumentado já basta.
  - Válvula de alívio interna ou by-pass da própria bomba. É comum em bombas de pistão de pulverizador, e o comportamento "pressão quase máxima com vazão baixa" (5,58 kgf/cm² com 1 L/min) é a assinatura de um alívio por mola.
  - Vazamento interno.
  - Escorregamento do motor ou do inversor.
- Contatar os autores (FURG) por e-mail para perguntar. Se responderem, o ponto se resolve.
- Observar no texto que a curva ajustada, com $a_0$ = 5,82 e queda suave, **é compatível com uma válvula de alívio por mola**. Isso transforma o "mistério" em interpretação.

### 1.4 O feedforward não foi testado contra erro de modelo

**Crítica provável:** "Seu feedforward inverte o próprio modelo da planta. Na simulação, planta e compensador são idênticos. Isso não é otimista demais?"

**Problema.** Em todos os cenários o FF usa exatamente $K$, $K_{v,max}$ e a curva da fonte da planta simulada. Esse é o ponto metodologicamente mais vulnerável da Tabela 6.

**Melhoria.** Criar um cenário **C5 — descasamento de modelo**. A planta simulada usa:
- $K$ com ±10%;
- curva da fonte deslocada (por exemplo, $a_0$ com ±5%, representando outra rotação);
- válvula **não linear** (por exemplo, de igual porcentagem ou quadrática), enquanto o FF continua supondo a válvula linear (H7).

Implementação: no script, separar os parâmetros da planta dos parâmetros do controlador. Hoje ambos leem as mesmas globais `K` e `KV_MAX`.

Resultado esperado: o PI corrige o erro de regime, e o FF perde parte do ganho no transitório. Mostrar isso **reforça** a justificativa do PI na seção 3.5 ("elimina o erro em regime causado por incertezas do modelo"), que hoje é afirmada, mas não demonstrada.

### 1.5 A conclusão afirma mais do que os resultados sustentam

- Seção 5: "A hipótese foi, portanto, confirmada".
  - A hipótese (1.1) fala em "manter dentro de ±10%... durante sequências de abertura e fechamento".
  - Em C2, o PI+FF fica **7,6% do tempo fora** da faixa e tem pico de 17%.
  - Melhor formulação: "**parcialmente confirmada em simulação**: atendida para comutações de um bico e para a comutação aleatória; não atendida para degraus simultâneos de três bicos, limitados pela velocidade do atuador".
- A faixa 0,9025–1,1025 não é exatamente "±10%" (é −9,75%/+10,25%). Escrever "aproximadamente ±10%", ou citar só a Equação 3.11.

### 1.6 Mudanças em relação ao projeto (TCC I / 04.docx)

**Pergunta provável:** "No projeto você propôs X; por que mudou?"

A banca costuma comparar com a proposta do TCC I. Há três mudanças:
- **Atuador:** rotação da bomba no 04, válvula de alívio no 06.
- **Validação com dados de campo do Mato Grosso:** prevista e não feita.
- **Base experimental:** passou a ser a bancada de Rosa.

**Melhoria.** Escrever um parágrafo explícito na Metodologia, em 3.1 ou 3.2, justificando cada mudança. Por exemplo:
- a válvula de alívio é o atuador para o qual há dados publicados;
- a rotação da bomba exigiria o modelo do motor e do inversor, sem dados disponíveis.

Isso também resolve a dúvida E.2 das notas.

---

## 2. Fortalecimento técnico (🟡)

### 2.1 Mostrar a dedução de que a planta não depende de $n$

O achado "$K_g$ e $\tau_p$ não dependem de $n$" é elegante e a banca vai gostar, mas hoje está só em palavras (3.4). Escrever as derivadas parciais da Eq. 3.6 no ponto de operação:

$$\frac{\partial f}{\partial P} = \frac{1}{60C_h}\left[Q_s'(P_{ref}) - \frac{nK+K_v}{2\sqrt{P_{ref}}}\right], \qquad nK + K_v = \frac{Q_s(P_{ref})}{\sqrt{P_{ref}}}$$

A segunda igualdade elimina $n$. São três linhas de equação.

### 2.2 Implementação digital: o ponto forte esperado de uma banca de Engenharia Elétrica

Hoje o controle aparece só em tempo contínuo (Eq. 3.9) com "ZOH". Acrescentar:
- a **equação de diferenças** do PI que o script realmente executa (Euler para trás, integração condicional);
- a **resolução do ADC** (10 bits no ATmega2560) e do transmissor de pressão, com a resolução resultante em kgf/cm². Comparar com a faixa de ±5%;
- **ruído de medição**, com um cenário simples somando ruído gaussiano à pressão medida, e eventualmente um filtro de 1ª ordem no sensor;
- a **resolução do comando do servo** (passo mínimo de α) e a **zona morta/folga** da válvula agulha.

Isso pode virar uma seção 3.9 curta: "Considerações de implementação embarcada". É o tipo de conteúdo que diferencia o trabalho de Engenharia Elétrica de um trabalho de Engenharia Agrícola.

### 2.3 Baseline realista: o regulador mecânico de pressão

**Pergunta provável:** "Pulverizadores comerciais já têm válvula reguladora de pressão por mola. Por que comparar com malha aberta de válvula fixa?"

**Melhoria.** Acrescentar uma configuração "**regulador mecânico**": válvula de alívio proporcional, $K_v$ aumentando linearmente com $(P - P_{ab})$, sem integrador. Ela representa o que a máquina já faz sem eletrônica, e é mais justo mostrar o ganho do PI+FF contra **isso** do que contra válvula fixa.

### 2.4 Traduzir as métricas para o campo

"% do tempo fora da faixa" é abstrato para quem é da área agrícola. Converter em **distância percorrida com dose errada** usando a velocidade de trabalho; a 15 km/h, 1 s ≈ 4,2 m. Exemplo: no C2, o tempo total do PI+FF fora da faixa (≈7,6% × 14 s ≈ 1 s) corresponde a cerca de 4 m de barra com dose fora de ±5%.

Também é possível relacionar o desvio de pressão com a variação de tamanho de gota, ao menos qualitativamente, para fechar o ciclo com a seção 2.5.

### 2.5 Antecipar o comando da válvula: fazer agora

Está em "trabalhos futuros", mas é barato: aplicar $\alpha_{ff}(n_{futuro})$ alguns décimos de segundo **antes** de comutar as solenoides. Na aplicação localizada, o sensor ou mapa conhece a comutação com antecedência, pela distância entre câmera e barra.

O cenário C2 é justamente onde o PI+FF falha (pico de 17%). Mostrar que a antecipação resolve vira um resultado próprio do trabalho, e não só sugestão.

### 2.6 Justificar λ e explorar o compromisso

λ = 0,5 s aparece como "escolha de projeto". Com margem de ganho de 29 dB, a banca pode perguntar: "Por que não um controlador mais agressivo?"

Fazer uma varredura de λ (por exemplo, 0,1 a 1 s) com o desvio máximo em C3 e a margem de fase. Isso mostra que a escolha foi pensada e evidencia o limite imposto pelo atuador.

### 2.7 Comprovar a convergência numérica

**Pergunta provável:** "Euler com 1 ms é suficiente?"

Testes rápidos com dt = 0,5 ms reproduziram a Tabela 6 (C3 PI+FF: 3,1% contra 3,0%) **[teste]**. Isso vale uma frase na seção 3.6. Se o caso base passar a usar $C_h$ pequeno ($\tau_p$ ≈ 10 ms), refazer o teste.

### 2.8 Revisão bibliográfica

O trabalho se apoia em duas fontes técnicas (Rosa 2019, Steward 2000), e várias citações são *apud*. A banca tende a apontar isso.

**Melhorias:**
- Buscar trabalhos mais recentes sobre:
  - controle de pressão e vazão em pulverizadores;
  - pulverização por PWM nos bicos, uma alternativa ao controle de pressão que a banca pode citar, então convém mencioná-la e explicar por que não foi o foco;
  - *spot spraying* e *see & spray*.

  Fontes: Google Scholar, Computers and Electronics in Agriculture, Biosystems Engineering, Transactions of the ASABE.
- Resolver as pendências da seção C das notas (ZHANG & PIERCE, SHIRATSUCHI 2013, SCHLOSSER, OGATA, SKOGESTAD).
- Trocar as citações *apud* das equações centrais (lei de orifício, Reynolds) por um livro de mecânica dos fluidos lido diretamente (Fox & McDonald, White ou similar).

### 2.9 A diferença de 7% para o catálogo do bico

O modelo prevê 0,86 L/min a 4 bar contra 0,92 L/min do fabricante. A banca pode perguntar o porquê. Possíveis explicações:
- perda na solenoide e na válvula antigotejo, entre o transmissor de pressão e a ponta;
- desgaste ou tolerância de fabricação da ponta;
- posição do manômetro.

Uma frase com essas hipóteses fecha a questão.

---

## 3. Acabamento e normas (🟢)

- **Listas ABNT:** incluir a Lista de Ilustrações e a Lista de Tabelas, que são obrigatórias quando há figuras e tabelas.
- **Unidades:** kgf/cm² não é SI. Manter por coerência com a fonte, mas dar a equivalência em kPa nas tabelas principais ou em nota. Uma banca de Engenharia Elétrica pode cobrar o SI.
- **Diagramas Mermaid:** exportar para imagem (mermaid.live → PNG/SVG) com fonte legível e estilo uniforme com os gráficos do matplotlib.
- **Figuras do script:**
  - conferir legibilidade em tamanho de página A4;
  - rótulos de eixos em português com unidade;
  - decimal com vírgula, que se configura no matplotlib com `axes.formatter.use_locale`.
- **Título:** "Modelagem de sistema de controle para pulverização agrícola de precisão" é genérico. Sugestão: "*Modelagem e controle da pressão em barra de pulverização com acionamento bico a bico*".
- **Resumo:** atualizar se os números mudarem (itens 1.1 e 1.4). Ele hoje cita 97% e 100%, os números mais sensíveis às hipóteses.
- **Reprodutibilidade:**
  - colocar o script num repositório público (GitHub) com o link no Apêndice A;
  - registrar as versões de Python, numpy e matplotlib e a semente do C3.
- **Remover:** o bloco "NOTAS DE REVISÃO" e as marcações [REF. PENDENTE] / [A CONFERIR] antes da entrega.
- **Hipóteses fora de ordem:** H1–H4 estão em 3.3, H5–H6 em 3.4, e H7 aparece no meio de 3.3. Renumerar em ordem de aparição ou reunir todas numa tabela.

---

## 4. Perguntas prováveis da banca e respostas a preparar

| Pergunta | Onde está a resposta / o que falta |
|---|---|
| De onde vieram $C_h$, $\tau_a$, $\omega_{max}$? | Falta justificativa física (item 1.1) |
| Por que a vazão da bomba de pistão cai com a pressão? | Hipótese do alívio por mola (item 1.3) |
| O feedforward funciona se o modelo estiver errado? | Falta o cenário C5 (item 1.4) |
| Por que não controlar pela rotação da bomba, como no projeto? | Parágrafo de justificativa (item 1.6) |
| Por que PI e não PID? Por que esse λ? | Está em 3.5; falta a varredura de λ (item 2.6) |
| Como isso seria implementado num microcontrolador? | Seção de implementação (item 2.2) |
| E numa barra comercial de 36 m com 70 bicos? | H2 e 3.8; argumentar que a planta independe de $n$, mas a perda distribuída e o atraso de transporte entram |
| Qual o ganho real em produto economizado ou dose correta? | Conversão para metros de campo (item 2.4) |
| Por que não usar PWM nos bicos? | Revisão bibliográfica (item 2.8) |
| Os resultados valem fora da simulação? | Seção 3.8 e conclusão; validação dinâmica pendente |

---

## 5. Plano sugerido, por custo × impacto

| # | Ação | Esforço | Impacto |
|---|---|---|---|
| 1 | Estimativa física de $C_h$ e sensibilidade estendida a C2/C3 | baixo (script pronto) | 🔴 alto |
| 2 | Validação cruzada leave-one-out | baixo | 🔴 alto |
| 3 | Cenário C5 de descasamento de modelo | médio (separar parâmetros planta/controlador) | 🔴 alto |
| 4 | Reescrever a conclusão ("parcialmente confirmada") e justificar as mudanças em relação ao projeto | baixo | 🔴 alto |
| 5 | Dedução da independência de $n$ | baixo | 🟡 |
| 6 | Seção de implementação embarcada (equação de diferenças, ADC, ruído) | médio | 🟡 alto para banca de Engenharia Elétrica |
| 7 | Baseline com regulador mecânico | médio | 🟡 |
| 8 | Antecipação do comando da válvula | médio | 🟡 |
| 9 | Revisão bibliográfica e referências pendentes | médio–alto | 🟡 |
| 10 | Acabamento ABNT e figuras | baixo | 🟢 |

Os itens 1 a 4 são feitos no script e no texto, sem dados novos, e cobrem as críticas mais prováveis.

O único ponto que só se resolve com dado externo é a validação dinâmica, que pode vir de um ensaio de degrau simples em bancada ou de uma série temporal de campo. Até lá, o trabalho deve se posicionar explicitamente como **estudo de modelagem e projeto em simulação**.
