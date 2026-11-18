# Relatório da banca — versão 10

Base: `contexto/10.md`, `docs/10.pdf` (83 páginas) e `simulacao/modelo_barra.py` (02/11/2026).

**Banca simulada:** três avaliadores independentes leram o trabalho sem as conclusões do autor.
- **Controle:** teoria, Ziegler-Nichols, PI discreto, *feedforward* e coerência entre texto e script.
- **Máquinas agrícolas e hidráulica:** física do modelo, dados de Rosa, ISO 16122-2 e realismo dos parâmetros.
- **Forma e ABNT:** estrutura, consistência dos números, tom e referências.

**Marcação dos números:**
- **[verificado]**: o autor do relatório refez a conta ou o teste e confirmou;
- **[banca]**: o número veio de um teste do avaliador e não foi refeito.

**Prioridade:**
- 🔴 a banca quase certamente vai cobrar;
- 🟡 fortalece o trabalho;
- 🟢 acabamento.

---

## Visão geral

**Pontos fortes reconhecidos pelos três avaliadores:**
- **Texto e script batem.** Todos os números do Cap. 4 conferem com o `resultados.json`. Os números também batem entre o Resumo, o Abstract, as tabelas e a Conclusão. O Quadro 4 reproduz fielmente o laço de `simular`.
- **Modelo estático correto e bem validado.** A lei de orifício, a associação em paralelo (R/n²) e a validação "deixa um de fora" estão certas; esta última é rara num TCC. Trocar a fórmula empírica de quatro parâmetros por um único K físico é uma contribuição real.
- **Uso correto da fonte.** As Tabelas 1 e 2 conferem com o artigo de Rosa, Terra e Drews Jr (2019). A leitura do fluxograma (PCV por mola, HV, ordem das solenoides) está correta.
- **Teoria amarrada à simulação.** A Eq. 2.12 prevê 3,71 e 3,91 kgf/cm², e o simulador dá 3,70 e 3,90. A tabela de ZN confere com o Ogata (Tabela 8.2).
- **Honestidade.** A conclusão diz "confirmada em parte e só em simulação", os parâmetros estimados são declarados e as conferências automáticas estão no script.
- **Estrutura completa.** O trabalho segue a ordem do modelo da UNEMAT, e cada objetivo é retomado na Conclusão.

**Principal fragilidade:** as três novidades da v10 se apoiam em escolhas que o texto não defende. São elas:
- a sintonia de ZN, aplicada a uma oscilação causada pela amostragem (item 1.2);
- a conclusão sobre o *feedforward*, que vem de um único sorteio (item 1.1);
- a faixa de ±10%, tirada de uma norma de inspeção e usada como critério dinâmico (item 1.3).

Nenhuma dessas fragilidades derruba o trabalho, mas as três precisam ser tratadas no texto.

---

## 1. Pontos críticos (🔴)

### 1.1 A conclusão sobre o *feedforward* vem de um único sorteio e está errada na Conclusão

O C3 usa uma única sequência aleatória (semente 42). Repetindo o C3 com outras 10 sementes e os mesmos ganhos **[verificado]**:

| | PI: tempo fora | PI+FF: tempo fora | FF pior em |
|---|---|---|---|
| Semente 42 (a do texto) | 5,0% | 5,9% | — |
| Média de 10 sementes | **5,7%** (de 2,1% a 9,1%) | **8,0%** | **10 de 10** |

Leitura dos números:
- **O FF piora sempre, e mais do que o texto mostra.** A semente 42 é uma das mais favoráveis a ele: 0,9 ponto de diferença, contra 2,3 pontos na média.
- **O "95% do tempo dentro da faixa" do Resumo depende do sorteio.** Com outras sementes, o mesmo PI dá de 91% a 98%.
- **A Conclusão erra até com os números do próprio texto.** Ela diz "com uma válvula duas a quatro vezes mais rápida, o feedforward voltou a ajudar". Mas com ωmax = 1,0 s⁻¹ (duas vezes mais rápida) o C3 dá 1,2% (PI) contra 1,6% (PI+FF), e o FF ainda piora.
- **Com ωmax = 2,0, o FF também piora na média.** No sorteio do texto ele ajuda (1,0% → 0,8%), mas em 10 sementes fica pior em 8 **[banca]**.
- **A causa ("a válvula não chega à posição antes da próxima troca") não foi demonstrada.** O avaliador testou reduzir Kc à metade e a um quarto, e o PI+FF continuou pior que o PI **[banca]**. Isso descarta a "dupla correção" como explicação.

**O que fazer:**
1. Rodar o C3 com 10 sementes no script e informar média e faixa, na Tabela 10 e no Resumo.
2. Reescrever 4.6 e a Conclusão: o FF estático ajudou pouco nas trocas espaçadas (C1 e C2) e piorou as trocas rápidas em todas as velocidades testadas.
3. Apresentar a velocidade da válvula como **hipótese** para a piora, não como causa demonstrada.
4. Ligar com o item 2.2: a malha PI já é quase *deadbeat*, o que deixa pouco espaço para o FF.

### 1.2 O Ziegler-Nichols foi aplicado a uma oscilação causada pela amostragem

**O problema:**
- A planta contínua (válvula de 1ª ordem, pressão instantânea) **nunca oscila** só com controle P. A oscilação crítica vem do controlador amostrado: o polo discreto chega a z = −1. Por isso Pcr = 2·Ts sempre.
- Consequências:
  - Pcr e Ti (= 1,67·Ts) são fixados pela **escolha** de Ts = 50 ms, e não pela física.
  - Kcr depende só de Ts/τa, e τa foi estimado.
  - Com a mangueira incluída, Kcr sobe de 2,93 para cerca de 5,0 [verificado na v10]. Ou seja, os ganhos são consequência das hipóteses do modelo.
- O Ogata diz: "se a saída não exibe uma oscilação sustentada para qualquer valor que Kp pode assumir, então esse método não se aplica". A banca vai perguntar se esse é o caso.

**Três frases do texto estão erradas ou frágeis:**
- **4.2: "A pequena diferença vem do limite de velocidade da válvula"** está errada. Sem limite de velocidade, a bissecção dá Kcr = 2,921, ainda mais longe do teórico 3,02 **[verificado]**. Com o ensaio estendido para 30 s, sai 2,975 **[banca]**. A diferença vem do critério de detecção: janela de 10 s e limiar de 10⁻⁴ kgf/cm². Perto do crítico, a oscilação decai muito devagar e é tomada como sustentada.
- **2.6.1: "o período crítico diz qual é o ritmo natural da malha"** está errada neste caso, porque o ritmo é o da amostragem.
- **2.6.1: "o método não exige um modelo, só um experimento"** é frágil, porque o simulador é o modelo.

**O que fazer:**
1. Em 3.5.4, deduzir em 4 ou 5 linhas a planta discreta, G(z) = |Kg|(1−a)/(z−a) com a = e^(−Ts/τa), e o polo de malha fechada, z = a − Kc|Kg|(1−a). Com z = −1 saem Kcr = 3,02 e Pcr = 2·Ts. O script já faz essa conta (`kcr_teo`), mas o texto não mostra.
2. Dizer explicitamente que a oscilação crítica vem da amostragem, e que por isso os ganhos dependem de Ts e τa.
3. Justificar o ZN como **o procedimento que seria repetido na bancada real**; o simulador só antecipa esse ensaio.
4. Corrigir a explicação da diferença de 3% e informar o limiar do ensaio.
5. Em 4.2 e 3.8, dizer que a hipótese H6 muda pouco as métricas com os mesmos ganhos, mas muda a sintonia (Kcr ≈ 5 com a mangueira).

### 1.3 A ISO 16122-2 foi usada como critério dinâmico, e ela não é isso

**O problema:**
- A ISO 16122-2 é uma norma de **inspeção periódica de máquinas em uso**.
- O item 4.5.4 foi citado pela metade. O texto completo é: "…tolerance of ±10 % at constant setting **and shall return within 10 s** to the original working pressure ±10 %…" **[verificado]**.
- O item 4.8.8 também mede a pressão "10 s after a section has been closed". Os dois são critérios de **regime**, com 10 s para acomodar.
- O "tempo fora da faixa", medido a cada 1 ms, é uma métrica criada pelo autor e bem mais severa que a norma.
- Pelo critério real da norma:
  - o PI e o PI+FF atendem em todos os cenários, porque acomodam em menos de 1 s;
  - o P falha só com um bico aberto (3,90 > 3,85);
  - a malha aberta falha.
- A própria norma aceita manômetro com erro de ±10% e pulsação de até 10% (itens 4.5.2.3 e 4.2.2). É uma tolerância grosseira.

**A equivalência "±10% na pressão ≈ ±5% na vazão" está certa**, mas é uma conta do autor, não da norma.

**O que fazer:**
1. Citar o item 4.5.4 inteiro.
2. Separar dois critérios:
   - **o normativo:** regime, 10 s depois da troca. O PI atende com folga, e isso é um resultado positivo;
   - **o adotado neste trabalho:** tempo instantâneo fora da faixa. Justificá-lo pela resolução espacial da aplicação localizada: a 15 km/h, 10 s são cerca de 42 m.
3. Na hipótese (1.1), escrever "faixa de ±10% **baseada** na ISO 16122-2".
4. Como apoio para os ±5% na vazão, usar a recomendação de erro de aplicação ≤ 5% citada por Steward e Humburg (2000), que já estão nas referências.

### 1.4 Falta discutir Terra et al. (2020), do mesmo grupo, que mostra o regulador por mola segurando a pressão

O artigo "A Low-Cost Prototype to Automate Agricultural Sprayers" (TERRA et al., 2020, IFAC) está na pasta `referencias base/` e não é citado. Num pulverizador real de 10 bicos com válvula de alívio por mola, fechar 3 a 5 bicos mudou a pressão em apenas 3,5% a 6,8%. Os autores escrevem que a pressão ficou "close to the adjusted setpoint, varying only 0.5 bar approximately. This is due to the performance of the relief valve" **[verificado]**.

**Pergunta provável:** "O problema de 56% existe numa máquina bem regulada?"

**O que fazer:**
1. Citar e discutir o artigo.
2. Explicar que a PCV por mola é, na prática, um **controlador P mecânico**, com erro de regime. Isso liga direto com o resultado do P na seção 4.4.
3. Dizer que o ganho da válvula ativa com PI é eliminar esse erro e permitir mudar a pressão de trabalho durante a aplicação.
4. Dizer que a bancada de Rosa, com uma fonte que cai 2 kgf/cm² entre 1 e 5,6 L/min, é um caso desfavorável, e que o resultado não deve ser generalizado.
5. Num parágrafo, comparar com a solução passiva clássica, o **retorno compensatório** (válvula de três vias com orifício calibrado por bico), que a própria ISO cita no item 4.8.8.

### 1.5 Marcas de rascunho e restos de LaTeX no PDF

Aparecem no PDF **[verificado]**:
- p. 28: "√(0,9) **approx**0,95";
- p. 54: "O módulo |**ldots**| tira o sinal". O `md2docx.py` não converte `\approx` e `\ldots` no texto corrido;
- p. 32: "[REF. PENDENTE — ver notas]", em amarelo, na seção 2.7;
- p. 80: "[Versão parcial — revisar após validação…]" no início da Conclusão. Isso desqualifica o capítulo;
- p. 82: "[A CONFERIR]" em Felizardo e em Holterman.

**Sobre Holterman:** a referência certa é o artigo de **1997** (*Computers and Electronics in Agriculture*, v. 19, p. 1-22). O "2016" foi herdado de um erro do artigo de Rosa. Corrigir também as citações no texto (p. 18 e 27).

**Sobre a seção 2.7:** ela inteira (FF, *windup*, *clamping*, *back-calculation*, Eqs. 2.14 e 2.15) está sem fonte. Sugestão: Åström e Hägglund, *Advanced PID Control* ou *PID Controllers*.

**O que fazer:**
1. Trocar `\approx` por "≈" e `\ldots` por "…" no .md.
2. Antes de gerar o PDF, fazer uma busca por `\` fora de `$`.
3. Resolver as quatro marcas.

### 1.6 Revisão bibliográfica desatualizada

**Situação:** são 24 entradas, 6 delas sites ou fontes não acadêmicas. Nenhuma é posterior a 2019, num tema com muita produção recente (bico a bico, PWM, *spot spraying*). Bernoulli e a lei de orifício são citados a partir de um artigo de congresso, e a seção 3.1 não tem referência de metodologia.

**Sugestões dos avaliadores** (conferir os dados de cada uma antes de usar):
- **Medições do problema:**
  - Sharda et al. (2011, *Comput. Electron. Agric.*; 2013, *Trans. ASABE*);
  - Luck et al. (2010/2011);
  - Mercaldi et al. (2017, IFAC);
  - Terra et al. (2020, IFAC).
- **PWM:** Butts et al. (2019); Fabula et al. (2021, *Comput. Electron. Agric.*).
- **Aplicação localizada:**
  - Villette et al. (2021; 2022);
  - Gerhards et al. (2022, *Weed Research*);
  - Allmendinger et al. (2022, *Agronomy*).
- **Livros:**
  - Matthews, Bateman e Miller, *Pesticide Application Methods*;
  - Antuniassi e Baio;
  - um livro de mecânica dos fluidos (Fox, White ou Çengel);
  - um livro de metodologia.
- **Catálogo da ponta FanTip:** serve para a relação de vazão e a faixa de pressão recomendada.

**O que fazer:** acrescentar um parágrafo de estado da arte em 2.2 ou 2.6, com 5 a 8 desses trabalhos. Para cada um, dizer o que foi medido ou proposto e onde este TCC se encaixa.

**Entradas fora da NBR 6023:2018:**
- **MILHORANCE:** faltam data completa e URL, e o dado é do INCA.
- **BRASIL (ODS):** a autoria deve ser o próprio Movimento ODS.
- **AGRIQ, KUHN e BRASIL:** sem data. Usar data provável entre colchetes, por exemplo [2024?].
- **OGATA:** "Tradução: Heloísa Coimbra de Souza", com dois-pontos.
- **ZIEGLER e NICHOLS:** falta n. 8.
- **COSTA et al.:** falta o fascículo.
- **MANTOVANI:** falta o intervalo de páginas.
- **MERCALDI:** faltam as folhas e a área do mestrado.
- **ISO:** tirar o parêntese "(Adotada como BS EN…)", ou referenciar a versão BS EN, que foi a lida.

---

## 2. Fortalecimento (🟡)

### 2.1 O anti-windup na saturação de velocidade decide o resultado do PI
No C3, o integrador fica congelado em 63% das amostras com o PI. Congelando só no limite de posição, que é a forma clássica, o PI vai de 5,0% para 8,95% fora da faixa **[banca]**. O texto trata isso em uma frase.

Também há um detalhe de implementação: `sat_vel` usa o α_c da amostra anterior, então detecta a saturação com uma amostra de atraso.

**O que fazer:** justificar o congelamento na saturação de velocidade em 2.7.2 e mostrar o efeito numa linha ("sem o congelamento por velocidade, o PI ficaria X% fora da faixa").

### 2.2 Falta dizer onde estão os polos e de onde vêm os picos
Pelo modelo discreto:
- o P sintonizado tem polo em z ≈ −0,08;
- o PI tem polos em z ≈ 0,53 e 0,008 **[banca]**.

A malha linear é, portanto, bem amortecida, quase *deadbeat*. O "sobressinal grande" do ZN que o texto menciona não aparece. Os picos de 9,5% e 29,7% vêm do salto instantâneo da pressão (H6) e da saturação de velocidade, não da sintonia. A margem de ganho é 2 por construção (0,5·Kcr).

**O que fazer:** um parágrafo curto em 4.2. Na seção 4.4, trocar "com o dobro do ganho a malha já oscilaria" (que é tautológico) por "a margem de ganho é 2".

### 2.3 O modelo da conferência da H6 não está no texto
A seção 4.2 diz "o modelo da versão anterior deste trabalho, que inclui o armazenamento na mangueira". O leitor não tem esse modelo, e ele sustenta o "no máximo 1,7 ponto".

**O que fazer:**
1. Descrever esse modelo em poucas linhas: a equação dP/dt = (Q_s − Q_saída)/C_h e o valor de C_h com sua origem. Pode ficar em 4.2 ou num Apêndice A.
2. Tirar a expressão "versão anterior".

### 2.4 A Tabela 2 não bate com a Tabela 1, e a explicação do texto conflita com a PCV
**O problema:**
- O ensaio parte de 4,00 kgf/cm² com 7 bicos e a válvula fechada. A Tabela 1 dá 3,57 kgf/cm² nessa condição.
- O salto ao fechar 3 bicos foi de +45% no ensaio, contra +30% no modelo. Mesmo deslocando a fonte para dar 4,00, o modelo prevê 5,15, e não 5,80 **[banca]**.
- A explicação "outra rotação da bomba" conflita com a interpretação da PCV por mola. É a mola que define a pressão máxima (a₀), não a rotação.
- O mesmo problema aparece no C4, onde "a₀ +5%" é rotulado como "bomba girando mais rápido".
- "Ajustando a válvula à mão" é uma inferência. O artigo diz só "abriu-se 11%", e a válvula tem servomotor.

**O que fazer:**
1. Declarar a diferença com números.
2. Atribuir a₀ à regulagem da PCV, no texto e no rótulo do C4.
3. Trocar "à mão" por "em malha aberta, por comando do operador".

### 2.5 Realismo da válvula e alcance do "Kg constante"
- **A válvula trabalha quase fechada.** Com 7 bicos, α_ff = 0,023, ou seja, 2,3% de abertura. Uma válvula agulha nessa região é muito não linear, e um servo de modelismo tem zona morta da ordem de 1°. A H5 (válvula linear) é menos defensável justamente onde a malha trabalha.
- **"Kg igual para todo n" é consequência direta da H5.** O valor é exato no modelo: a Eq. 3.11 só depende de nK + K_v·α, que é constante em P_ref. Por isso a conferência de 2% é satisfeita trivialmente. Com a válvula quadrática, Kg varia com α.
- **K_v,max e ωmax andam juntos.** O que limita a correção é o produto ωmax·K_v,max, então a varredura de ωmax é também uma varredura de K_v,max.
- **K_v,max = 3,5** equivale a Cv ≈ 0,25, o que é plausível para uma válvula agulha de 1/4".
- **Os valores de τa e ωmax parecem conservadores.** Um servo de modelismo gira 60° em 0,1 a 0,2 s. Justificar com uma folha de dados do servo ou de uma válvula reguladora comercial.
- **Frase de 3.4.1:** "leva cerca de 0,2 s para reagir" sugere atraso puro, mas τa é constante de tempo.

**O que fazer:** restringir a afirmação para "no modelo, com válvula linear, Kg não depende de n", e ligá-la ao teste da válvula quadrática no C4.

### 2.6 "Tempo fora da faixa = área aplicada fora" não vale no controle bico a bico
Com n bicos abertos, só n/7 da largura está aplicando. Um instante fora da faixa com 1 bico aberto pesa um sétimo de um instante com 7 bicos.

**O que fazer:** ponderar a métrica por n(t), ou corrigir a frase de 3.6.4 e o exemplo dos "4 m" (que vale por bico aberto).

### 2.7 Escala dos cenários e transferência para o campo
- **As trocas da bancada são grandes.** Um bico da bancada é 14% da vazão; numa barra de 36 m, com cerca de 72 bicos, cada bico é cerca de 1,4%.
- **O caso típico do *spot spraying* não foi simulado.** Nele a barra fica quase toda fechada, com pulsos curtos de abertura.
- **A abertura simultânea de bicos não foi simulada.** Ela faz a pressão cair, que é o caso de subdose, e a válvula de alívio já está quase fechada.

**O que fazer:** discutir essa escala no texto. Se der tempo, acrescentar uma variante do C3 com baixa ocupação (n quase sempre entre 0 e 2).

### 2.8 P_ref = 3,5 kgf/cm² deixa só 1,7% de margem
A fonte dá 3,56 kgf/cm² com 7 bicos e a válvula fechada, e alivia só cerca de 0,15 L/min em P_ref. O próprio C4 mostra o efeito: com bicos 10% mais gastos, a referência fica inatingível.

**O que fazer:** justificar P_ref pelo catálogo da ponta e discutir o efeito de uma referência menor (por exemplo, 3,0 kgf/cm²). Mencionar que, nas máquinas reais, o retorno também serve à agitação do tanque.

### 2.9 Incerteza dos dados de origem
O artigo de Rosa usa sensores de baixo custo: medidor de vazão YF-S201 e transmissor HK1100C. O ponto com 1,00 L/min está no limite inferior do medidor. Os erros de ajuste de 0,7% e 2,3% estão abaixo dessa incerteza, e o déficit de 7% frente ao catálogo cabe nela.

**O que fazer:** um parágrafo sobre a incerteza dos dados. Chamar K de "K efetivo do conjunto solenoide + antigotejo + ponta".

### 2.10 Tom e títulos
O texto é simples, o que está certo, mas ainda há imperativos e coloquialismos.

**Trechos a reescrever:**
- 3.5.1: "Deixe n bicos…", "Abra a válvula um pouquinho", "Feche…", "Divida…" (imperativo e diminutivo);
- "como quem tira o pé do acelerador";
- "gotas grandes grudam menos";
- "andam sozinhos";
- "ninguém confere o resultado";
- "como se ninguém mexesse nela";
- "a variável que o controlador pode mexer";
- "dá para escrever" e "dá para entender";
- "pula direto";
- "vale saber qual é qual";
- "É o coração do programa";
- "Uma pergunta natural é";
- "correndo atrás do comando";
- "uns 4 m";
- "O problema é que", no Resumo.

**Títulos a trocar:**
- 3.4.3 "Avançando no tempo" → "Integração numérica (método de Euler)";
- 3.5.1 "Quanto a pressão muda quando a válvula abre" → "Ganho estático da planta";
- 3.6.2 "Como a simulação funciona, passo a passo" → "Algoritmo de simulação".

### 2.11 O que ainda pode sair
O Cap. 3 ocupa 31 das 66 páginas de texto, e só a seção 3.7 ocupa 10.
- **Na seção 3.7.2**, as equações são repetidas com o mesmo número. Basta remeter: "implementa as Equações (3.9) e (3.10)". Isso economiza cerca de 2 páginas.
- **As Figuras 13 e 16** são fluxogramas de funções de 2 a 4 linhas e podem sair. O Quadro 1 pode ir para um apêndice.
- **Itens não usados depois:**
  - Eq. 2.1, Reynolds: nunca é calculado. Calcular (Re ≈ 9.000 na mangueira da bancada, turbulento, o que apoia a lei de orifício) ou cortar;
  - Eq. 2.9, Q_ref: não é usada, e o símbolo D não está na lista;
  - o termo T_d e o parágrafo da ação derivativa: basta uma frase;
  - a Figura 3.
- **Os "Como ler" das fotos** (Figuras 4 a 7) podem ser reduzidos a uma frase cada.

### 2.12 Material que a banca não tem
- **Código e resultados.** O texto cita `simulacao/modelo_barra.py` e `resultados.json`, que são caminhos locais. Pôr o código num apêndice ou dar o link de um repositório com a versão.
- **Teste de ruído (3.8).** Os resultados aparecem sem método. Dar uma frase de método, ou deixar só a ressalva.
- **Kcr teórico de 3,02.** Aparece sem equação; o item 1.2 resolve.

---

## 3. Acabamento (🟢)

- **Resumo e Abstract:** cerca de 400 palavras cada. As palavras-chave ficam sozinhas na página seguinte (p. 6 e 8). Encurtar para cerca de 300 palavras.
- **IAE do PI no C3:** a Tabela 10 traz 3,14 e a Tabela 11 traz 3,13. O valor é 3,1345, então o certo é **3,13** **[verificado]**.
- **Ilustrações não citadas:** a Figura 16 e o Quadro 3 não são citados no texto. As Figuras 13 e 15 são citadas só depois de aparecer.
- **Tabela 7:** acrescentar colunas de erro, porque com o arredondamento a linha n = 2 parece ter 2,5% de erro, enquanto o texto diz 2,3%.
- **Tabela 10:** escrever "não acomodou em 11 dos 12 degraus".
- **Siglas:** colocar em ordem alfabética. "ZN" não é usada no texto. "PV" pode confundir com *process variable*.
- **Símbolos que faltam:** R_b, R₁, D, v, L, ρ, μ, A, f_a e d_i.
- **Eq. 2.12:** o |Kg| é uma solução improvisada para o sinal. Escrever com o ganho de malha L = Kc·|Kg| a partir de um diagrama de blocos, e dizer que é uma linearização em torno de P_ref. Também falta um espaço depois de "P:" e "PI:" na Eq. 2.13.
- **"Hipótese":** a hipótese de pesquisa e H1 a H6 usam o mesmo nome. Chamar H1 a H6 de "hipóteses simplificadoras". A p. 27 cita a H2 antes de ela ser definida.
- **Objetivo geral:** fala em "pressão e vazão", mas a métrica é só de pressão.
- **Conclusão:** diz que "o terceiro e o quarto objetivos eram sintonizar", mas o quarto é o FF.
- **Seção 3.3.4:** "fórmula de Bhaskara" é um nome que só se usa no Brasil. Preferir "fórmula resolvente da equação do 2º grau".
- **Negrito:** aparece demais no meio dos parágrafos.
- **Sumário:** os subtítulos estão recuados. Conferir se o modelo da UNEMAT exige isso.
- **Linha 176:** conferir se Casali (2012) sustenta que "muitos autopropelidos já vêm com controle individual de bicos".
- **`referencias base/Fabio.pdf` não é a versão em inglês do artigo de Rosa** **[verificado]**. É outro artigo do mesmo grupo (Terra, Rosa e Drews, "Evaluation of the Pressure-Flow Relationship…"). Corrigir as anotações internas e o `CLAUDE.md`.
- **Pré-textuais:** ano da defesa e ficha catalográfica, onde aparece a instrução do modelo "OBS: Gerar…".
- **Notas e marcações:** apagar o bloco NOTAS DE REVISÃO e as marcações antes da entrega.

---

## 4. Perguntas prováveis da banca

| Pergunta | Resposta hoje | O que falta |
|---|---|---|
| Sua planta nunca oscila com P. De onde vem a oscilação crítica, e por que Pcr = 2·Ts? O ZN se aplica? | Explicação qualitativa em 3.5.4 | Dedução em z (item 1.2) |
| Com Ts = 20 ms, o que muda em Kcr, Kc e Ti? Os ganhos refletem a planta ou a sua escolha? | — | Item 1.2 |
| Deduza o Kcr de 3,02. Por que o simulador deu 2,93? | "Limite de velocidade" (errado) | Critério de detecção (item 1.2) |
| O FF piorar o C3 vale para outros sorteios? A causa é mesmo a velocidade da válvula? | Uma semente, causa afirmada | 10 sementes, causa como hipótese (item 1.1) |
| Pelo critério de 10 s da ISO, qual controlador reprovaria? Por que um critério instantâneo? | Norma citada pela metade | Item 1.3 |
| Terra et al. (2020) mediram 3,5% a 6,8% só com a mola. O que a válvula ativa acrescenta? | — | Item 1.4 |
| Por que não usar retorno compensatório? | — | Item 1.4 |
| Onde estão os polos do PI? De onde vêm os picos de 9,5% e 29,7%? | — | Item 2.2 |
| Por que congelar o integrador na saturação de velocidade? Quanto muda sem isso? | Uma frase | Item 2.1 |
| Com 2,3% de abertura, a válvula agulha com servo se comporta como linear? O Kg continua constante? | H5 | Item 2.5 |
| A Tabela 2 parte de 4,00, e não de 3,57. Que regulagem explica isso, se a pressão máxima é da mola? | "Outra rotação" | Item 2.4 |
| Numa barra de 72 bicos em *spot spraying*, o que dos cenários continua valendo? | — | Item 2.7 |
| Qual a exatidão do YF-S201 a 1 L/min? | — | Item 2.9 |
| Que trabalhos recentes resolvem o mesmo problema (PWM com compensação de pressão)? | Nenhum depois de 2019 | Item 1.6 |

---

## 5. Plano sugerido

| # | Ação | Esforço | Impacto |
|---|---|---|---|
| 1 | Limpar o PDF: `\approx`, `\ldots`, marcas de rascunho, Holterman 1997, IAE 3,13 | muito baixo | 🔴 |
| 2 | C3 com 10 sementes no script; reescrever 4.6, Conclusão e Resumo sobre o FF | baixo (rodar o script) | 🔴 |
| 3 | Dedução em z do Kcr e do Pcr; corrigir as três frases sobre o ZN (item 1.2) | baixo | 🔴 |
| 4 | ISO: citar o 4.5.4 inteiro e separar o critério normativo do adotado | baixo | 🔴 |
| 5 | Citar e discutir Terra et al. (2020); PCV como "P mecânico"; retorno compensatório | baixo–médio | 🔴 |
| 6 | Referência para a seção 2.7 e de 5 a 8 trabalhos recentes; corrigir entradas ABNT | médio–alto (leitura) | 🔴 |
| 7 | Polos da malha, margem de ganho 2 e justificativa do anti-windup por velocidade | baixo | 🟡 |
| 8 | Descrever o modelo com mangueira (apêndice); Tabela 2 × PCV; rótulo do C4 | baixo | 🟡 |
| 9 | Tom e títulos; enxugar a 3.7.2 e os itens não usados do Cap. 2 | baixo | 🟡 |
| 10 | Métrica ponderada por n, cenário de baixa ocupação, incerteza dos sensores | médio | 🟡 |
| 11 | Acabamento ABNT, siglas, símbolos e pré-textuais | baixo | 🟢 |

Os itens 1 a 5 e 7 se resolvem numa rodada de edição e uma rodada do script, sem dados novos. O item 2 é o mais urgente, porque hoje a Conclusão afirma algo que os próprios números do texto contradizem. O item 6 é o que mais pesa na nota de uma banca de TCC II e exige leitura.
