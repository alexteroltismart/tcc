# Relatório para a banca — versão 07

Base: `contexto/07.md`, `docs/07.pdf` e `simulacao/modelo_barra.py` (27/10/2026).

Os números marcados **[teste]** vieram de rodadas extras do script feitas para este relatório. Eles não estão no 07.

Prioridade:
- 🔴 a banca quase certamente vai cobrar;
- 🟡 fortalece o trabalho;
- 🟢 acabamento.

---

## Visão geral

**Pontos fortes que a banca deve reconhecer:**
- **Modelo estático bem validado:** erro de ajuste de 0,7%/2,3% e erro de previsão na validação cruzada de 0,9%/2,7%.
- **Resultado analítico próprio:** a planta linearizada não depende de $n$ nem de $C_h$ no ganho, demonstrado nas Eqs. 3.13–3.16.
- **Achado de projeto concreto:** a válvula de alívio só baixa a pressão, então a bomba precisa ter folga de vazão. O C5 reforça isso, porque bicos gastos tornam a referência inatingível.
- **Honestidade nos resultados:** o feedforward piora com erro de modelo, e a hipótese foi confirmada só em parte.
- **Reprodutibilidade:** o script tem conferências automáticas e está explicado no corpo do texto.

**Principal fragilidade:** os resultados dinâmicos dependem de três números estimados, $C_h$, $\tau_a$ e $\omega_{max}$. Um deles ($\omega_{max}$) decide sozinho a conclusão. Ver item 1.1.

---

## 1. Pontos críticos (🔴)

### 1.1 A conclusão depende de $\omega_{max}$, que foi estimado

O texto diz que a velocidade da válvula é o gargalo e usa $\omega_{max}$ = 0,5 s⁻¹ "estimado". Variando só esse valor, com os mesmos ganhos **[teste]**:

| $\omega_{max}$ [s⁻¹] | C3, PI: tempo fora | C3, PI+FF: tempo fora | C2, PI: tempo fora | C2: pico de pressão |
|---|---|---|---|---|
| 0,25 | 18,1% | 17,7% | 14,2% | 29% |
| **0,5 (adotado)** | **4,7%** | **4,8%** | **7,5%** | **29%** |
| 1,0 | 0,4% | 0,5% | 4,1% | 29% |
| 2,0 | 0,2% | 0,8% | 2,6% | 25–29% |

**Leitura dos números:**
- O "cerca de 95% do tempo dentro da faixa" do Resumo pode virar 82% ou 99,6%, dependendo de um número que não foi medido.
- O pico do C2 (~29%) **não muda** com a velocidade da válvula. Ele acontece nos primeiros milissegundos, antes do primeiro período de amostragem (50 ms): a pressão salta em 12 ms e o controlador só reage depois.

**Pergunta provável:** "Se a válvula fosse mais rápida, o problema do C2 sumiria?" A resposta correta é "não": só antecipar o comando da válvula resolve o pico.

**O que fazer:**
1. Justificar $\omega_{max}$ com um dado concreto: a velocidade do servomotor (tipicamente 0,1–0,2 s/60°) e o número de voltas da válvula agulha de 1/4". Ou citar o tempo de curso de válvulas comerciais de pulverizador.
2. Incluir **uma frase e a tabela acima** em 4.2.2. A seção de sensibilidade foi retirada, mas uma tabela curta sobre o parâmetro que manda no resultado é diferente de uma análise de sensibilidade completa, e protege contra a crítica.
3. Corrigir a explicação do C2 no texto. Hoje ela atribui o pico à velocidade da válvula, mas o pico vem do salto instantâneo da pressão. O que a velocidade da válvula define é **quanto tempo** a pressão fica fora da faixa.

### 1.2 Não existe validação dinâmica

A validação "qualitativa" do C2 contra a Tabela 2 fica fraca, porque o próprio texto (4.1, Ressalva) diz que o ensaio da Tabela 2 foi feito em outra condição de bomba. Na prática, a parte dinâmica não tem nenhuma comparação com dado real.

**Pergunta provável:** "Como você sabe que a pressão responde em 12 ms e não em 200 ms?"

**O que fazer:**
- Assumir isso de forma explícita no objetivo e na conclusão: a parte dinâmica é um **estudo de projeto em simulação**.
- Comparar ao menos a ordem de grandeza com a literatura. Steward e Humburg (2000) dão tempos de subida e a taxa de 0,2 s do medidor.
- Se houver acesso à bancada ou a uma máquina, um único ensaio de degrau (fechar 3 bicos e registrar a pressão a 100 Hz) já valida $C_h$ e $\omega_{max}$.

### 1.3 A sintonia escolhida é agressiva e não considera ruído de medição

$\lambda$ = 0,05 s dá $K_c$ = 0,863, seis vezes maior que o do 06. A regra de escolha foi "o menor $\lambda$ com margem de fase ≥ 60°", mas a lista começava em 0,05, então o critério nunca foi ativo: **todos** os valores testados passaram. Com ruído no sensor de pressão **[teste]**, no C1 com PI+FF:

| $\lambda$ | Ruído do sensor (desvio-padrão) | Tempo fora | IAE | Curso total da válvula |
|---|---|---|---|---|
| 0,05 | 0 | 0% | 0,61 | 1,8 |
| 0,05 | 0,05 kgf/cm² | 0% | 0,98 | **5,8** |
| 0,2 | 0 | 0% | 0,69 | 1,7 |
| 0,2 | 0,05 kgf/cm² | 0% | 0,79 | **3,0** |

Com $\lambda$ = 0,05, o ruído faz a válvula andar **três vezes mais**, o que significa desgaste do atuador, sem melhora no resultado.

**O que fazer:**
- Rever o critério de escolha: por exemplo, "menor $\lambda$ com margem de fase ≥ 60° **e** margem de ganho ≥ 6 dB, partindo de $\lambda \ge \tau_a$". Ou simplesmente adotar $\lambda$ = 0,2 s, com $K_c$ 0,317 e margem de fase de 81°.
- Citar o ruído como limitação ou incluir o teste acima.

### 1.4 Numeração dos cenários: "C5" sem "C4"

A Tabela 4 lista C1, C2, C3 e C5, e a seção 4.2.3 fala em "cenário C5". A banca vai perguntar onde está o C4. **Renomear C5 → C4** no texto, no script (`casos_c5`, a figura `e_C5_erro_modelo.png`) e nas legendas.

### 1.5 Revisão bibliográfica fraca para um TCC II

São 14 referências, das quais:
- 3 são sites (AGRIQ, JACTO, KUHN);
- 1 entrada (BRASIL) tem autoria errada;
- 3 estão citadas no texto mas faltam na lista (ZHANG & PIERCE, SHIRATSUCHI 2013, SCHLOSSER);
- 2 ainda estão marcadas "a conferir" (OGATA, SKOGESTAD);
- 7 citações são *apud*, inclusive as das equações centrais (Reynolds, lei de orifício, perda distribuída).

Não há nada sobre controle de pulverização publicado depois de 2012. A banca de TCC II costuma esperar de 25 a 40 referências, com parte recente.

**O que fazer:**
- Trocar os *apud* das equações por um livro de mecânica dos fluidos lido diretamente (Fox & McDonald, White, Çengel), e o de controle por Ogata ou Nise.
- Usar Merritt (1967) ou um livro de hidráulica para a capacitância e o módulo volumétrico (Eq. 3.9). Hoje a faixa de $\beta$ de 100 a 1000 MPa está sem fonte, e é justamente ela que sustenta o $C_h$ adotado.
- Acrescentar de 5 a 10 artigos recentes (2015–2025) sobre controle de pressão e vazão em pulverizadores, *spot spraying* e pulverização por PWM.
- Resolver as marcações em amarelo.

### 1.6 Tom: simples, mas às vezes informal demais

A simplificação ajudou muito na leitura, mas alguns trechos soam coloquiais para um trabalho acadêmico. Exemplos:
- "quem 'manda' na resposta";
- "o modelo não está só 'decorando'";
- "Repare que";
- "planta mais 'fácil'";
- "como se ninguém mexesse nela";
- "ele 'segura' a pressão".

**O que fazer:** manter as explicações, mas trocar as gírias e as aspas por termos neutros. Por exemplo, "é a constante de tempo dominante", "o modelo generaliza para pontos fora do ajuste", "Observa-se que". Também convém manter a impessoalidade, sem imperativos dirigidos ao leitor.

---

## 2. Fortalecimento (🟡)

### 2.1 Explicar por que o feedforward quase não ajuda

O texto mostra que o PI+FF fica igual ao PI no C3, mas a explicação é curta. A explicação física tem três partes:
1. a pressão responde em 12 ms;
2. o controlador só atualiza a cada 50 ms;
3. a válvula leva de 0,2 a 0,7 s para chegar à nova posição.

O feedforward não chega antes da perturbação, porque é aplicado no mesmo instante da troca dos bicos, e a válvula é o gargalo nos dois casos. Dizer isso deixa claro que a próxima melhoria natural é **antecipar o comando**, que já aparece em trabalhos futuros. Simular esse cenário (comando da válvula 0,3–0,5 s antes das solenoides) seria o resultado mais forte que ainda falta. É barato: basta deslocar os eventos de $n$ usados pelo feedforward.

### 2.2 Baseline realista

A "malha aberta" com a válvula parada é um limite inferior. Muitas máquinas comerciais têm regulador de pressão por mola, que é uma válvula de alívio proporcional. Comparar o PI com esse regulador responde à pergunta "o que se ganha com a eletrônica?".

### 2.3 Rigor nas margens de estabilidade

As margens (Eq. 3.22) consideram a válvula linear, mas no resultado ela fica quase sempre **saturada em velocidade**. Uma frase dizendo que as margens valem para pequenas variações, e que nas trocas grandes quem domina é a saturação (efeito não linear), evita a crítica "a análise linear não explica o que você simulou".

### 2.4 Significado dos números no campo

O texto já traz "4 m de barra fora da faixa no C2". Seria bom fazer o mesmo para o C3 e para a malha aberta, e relacionar a variação de pressão com o tamanho de gota (seção 2.5), mesmo que só de forma qualitativa. A banca de Engenharia Elétrica pode não ser da área agrícola, e esse elo mostra a relevância.

### 2.5 Justificar $P_{ref}$ e $K_{v,max}$ do ponto de vista prático

$P_{ref}$ = 3,5 kgf/cm² ficou abaixo dos 4 bar do catálogo do bico. Vale explicar qual seria a consequência agronômica: vazão cerca de 7% menor que a nominal, e a velocidade de trabalho precisaria ser ajustada. Também convém dizer que $K_{v,max}$ = 3,5 é uma escolha que corresponde a uma válvula real de tamanho X.

---

## 3. Acabamento (🟢)

- **Resumo:** tem 385 palavras, dentro do limite de 500. Revisar após mudar os números dos itens 1.1 e 1.3.
- **Título** genérico. Sugestão: *"Modelagem e controle da pressão em barra de pulverização com acionamento bico a bico"*.
- **Unidades:** kgf/cm² não é SI. Manter por coerência com a fonte, mas dar o valor em kPa ou bar nas tabelas principais.
- **Tabela 10:** a coluna "Caso" quebra em várias linhas; usar nomes curtos ou nota de rodapé.
- **Figuras 1–5:** ainda são caixas de descrição; inserir as imagens.
- **Página 57:** só tem uma referência. Ajustar a paginação no final.
- **Quadros 2–4 (código):** fonte pequena. Conferir a legibilidade na impressão.
- **Pré-textuais:** ano da defesa e ficha catalográfica ainda em amarelo.
- **NOTAS DE REVISÃO** e marcações [REF. PENDENTE] / [A CONFERIR]: remover antes da entrega.

---

## 4. Perguntas prováveis da banca

| Pergunta | Resposta hoje | O que falta |
|---|---|---|
| De onde vieram $\tau_a$ e $\omega_{max}$? | "Estimados" | Dado do servo e da válvula (item 1.1) |
| Se a válvula fosse 2× mais rápida, o C2 passaria? | Não está no texto | Não: o pico ocorre antes do controlador agir (item 1.1) |
| Como sabe que a pressão responde em 12 ms? | Estimativa por V/β | Fonte para β, ou ensaio (itens 1.2 e 1.5) |
| Por que λ = 0,05? | Menor da lista com margem de fase ≥ 60° | Critério que considere ruído (item 1.3) |
| Cadê o cenário C4? | — | Renumerar (item 1.4) |
| Para que serve o feedforward, se não ajuda? | Ajuda pouco e piora com erro | Antecipação do comando (item 2.1) |
| O que a eletrônica ganha de um regulador por mola? | — | Baseline mecânico (item 2.2) |
| A análise de margens vale com a válvula saturada? | — | Frase sobre pequenos sinais × saturação (item 2.3) |
| Por que não controlar pela rotação da bomba, como no projeto? | Seção 1.4 | Confirmar a redação com o orientador |
| Quais trabalhos recentes fazem algo parecido? | Nenhum citado após 2012 | Revisão bibliográfica (item 1.5) |

---

## 5. Plano sugerido

| # | Ação | Esforço | Impacto |
|---|---|---|---|
| 1 | Renumerar C5 → C4 | muito baixo | 🔴 |
| 2 | Corrigir a explicação do pico do C2 e incluir a tabela de $\omega_{max}$ | baixo | 🔴 |
| 3 | Rever a escolha de $\lambda$ (provavelmente 0,2) e citar o ruído | baixo (rerodar o script) | 🔴 |
| 4 | Justificar $\omega_{max}$ e $\beta$ com fontes | médio (pesquisa) | 🔴 |
| 5 | Ajustar o tom informal | baixo | 🔴 |
| 6 | Ampliar as referências (livros-texto e artigos recentes) | médio–alto | 🔴 |
| 7 | Cenário de antecipação do comando | médio | 🟡 alto |
| 8 | Baseline com regulador por mola | médio | 🟡 |
| 9 | Frase sobre margens × saturação; significado no campo | baixo | 🟡 |
| 10 | Acabamento ABNT, figuras e pré-textuais | baixo | 🟢 |

Os itens 1, 2, 3 e 5 se resolvem em uma rodada de edição do texto e do script, sem dados novos. O item 4 é o que mais protege o trabalho, porque é dele que depende a credibilidade dos números do Capítulo 4.
