# Roteiro da apresentação: 15 minutos

Este roteiro acompanha a apresentação `Apresentacao_Banca_TCC_v20.pptx` (22 slides), que corresponde à versão 20 do TCC (`docs/20.pdf`). Todas as figuras e tabelas dos slides são do próprio TCC.

**Tempo:**
- O tempo previsto de fala é de **14 min 25 s**. Sobram 35 s de folga para imprevistos.
- O ritmo de referência é de cerca de 130 palavras por minuto. Cada fala abaixo foi escrita para caber no tempo do slide.
- Não é preciso decorar o texto: use as falas como guia e diga com suas palavras.

**Onde ganhar tempo:**
- Se estiver atrasado, encurte os slides marcados com ⏩. Eles podem ser ditos em uma frase.
- Nunca corte os slides 16 a 21 (resultados, os três cenários, gargalo e conclusões).

---

## Mapa de tempo

| Slide | Assunto | Tempo | Acumulado |
|---|---|---|---|
| 1 | Capa | 0:15 | 0:15 |
| 2 | Título | 0:30 | 0:45 |
| 3 | O problema | 0:50 | 1:35 |
| 4 | Objetivo e hipótese | 0:45 | 2:20 |
| 5 | Roteiro ⏩ | 0:20 | 2:40 |
| 6 | Bancada de referência e Tabela 1 | 0:45 | 3:25 |
| 7 | Modelo estático | 0:55 | 4:20 |
| 8 | Modelo R₁/n² | 0:45 | 5:05 |
| 9 | Validação ⏩ | 0:35 | 5:40 |
| 10 | Modelo dinâmico | 0:45 | 6:25 |
| 11 | Estratégia de controle | 0:45 | 7:10 |
| 12 | Feedforward, ganho da planta e do distúrbio | 0:50 | 8:00 |
| 13 | Malha em Laplace: os bicos como perturbação | 1:00 | 9:00 |
| 14 | Sintonia por alocação de polos | 0:45 | 9:45 |
| 15 | Cenários e métricas ⏩ | 0:20 | 10:05 |
| 16 | Resultados: Tabela 10 | 0:40 | 10:45 |
| 17 | Cenário C1: um bico por vez | 0:35 | 11:20 |
| 18 | Cenário C2: degraus de três bicos | 0:40 | 12:00 |
| 19 | Cenário C3: trocas aleatórias rápidas | 0:25 | 12:25 |
| 20 | Gargalo: velocidade da válvula | 0:40 | 13:05 |
| 21 | Conclusões | 0:50 | 13:55 |
| 22 | Trabalhos futuros e agradecimento | 0:30 | 14:25 |

**Pontos de controle do relógio:**
- no slide 7 você deve estar perto de **3:25**;
- no slide 13, perto de **8:00**;
- no slide 20, perto de **12:25**.

Se estiver mais de 30 s atrasado num desses pontos, use os ⏩.

---

## Falas

### Slide 1: Capa (0:15)
> Boa tarde a todos. Agradeço a presença da banca e do meu orientador.

### Slide 2: Título (0:30)
> Meu nome é Alex de Jesus Terolti, e o meu trabalho é "Modelagem de sistema de controle para pulverização agrícola de precisão", com orientação do professor Rogério Bastos Quirino. Em resumo: controlar a pressão de uma barra de pulverização bico a bico usando uma válvula de alívio, com um modelo simples e controladores clássicos, tudo em simulação.

### Slide 3: O problema (0:50)
> Na pulverização localizada, cada bico abre e fecha sozinho. Só que, quando os bicos são alimentados por uma mesma mangueira, em série, cada troca muda a pressão dos outros. A figura é o ensaio da bancada de Rosa, Terra e Drews Junior, de 2019: fechando três bicos, a pressão sobe de 4,0 para 5,8. Com a válvula fechada, indo de sete para um bico, a pressão sobe 56 por cento. Como a vazão do bico varia com a raiz da pressão, isso muda a dose aplicada e o tamanho das gotas.

### Slide 4: Objetivo e hipótese (0:45)
> A hipótese é que um modelo de resistências fluídicas, com a bomba, os bicos e a válvula de alívio, junto com a dinâmica da válvula, basta para projetar um controlador simples que segure a pressão dentro de mais ou menos 10 por cento. Essa é a tolerância da norma de inspeção de pulverizadores, a ISO 16122-2, e corresponde a cerca de 5 por cento na vazão de cada bico. Os objetivos foram modelar, acrescentar a dinâmica, sintonizar os controladores por alocação de polos e compará-los em simulação.

### Slide 5: Roteiro ⏩ (0:20)
> O trabalho seguiu sete etapas, em que cada uma entrega a entrada da seguinte. A base é o modelo estático, reaproveitado no simulador e no controle. Vou seguir essa ordem.

*Se atrasado: "O trabalho seguiu sete etapas, na ordem que vou apresentar."*

### Slide 6: Bancada de referência e Tabela 1 (0:45)
> A bancada de referência tem uma barra de cinco metros com sete bicos e solenoides, uma bomba de pistão com uma válvula de mola que devolve o excesso ao tanque, e uma válvula agulha com servomotor, que é o atuador. A tabela traz os dados medidos com a válvula de alívio fechada: fechando bicos, a pressão sobe, a vazão cai e a resistência P sobre Q ao quadrado cresce muito depressa. São esses sete pontos que usei para ajustar o modelo.

### Slide 7: Modelo estático (0:55)
> O modelo responde: com n bicos abertos e a válvula numa certa abertura, qual é a pressão? Três caminhos se encontram num único nó: a fonte empurra líquido, e os bicos e a válvula deixam sair. Cada bico segue a lei de orifício, q igual a K raiz de P. A fonte é uma curva de segundo grau, e a válvula é linear na abertura. Em regime, o que entra é igual ao que sai. Juntando bicos e válvula na capacidade de saída C, isso vira uma equação de segundo grau, e a pressão sai de forma explícita, pela Equação 3.11. A pressão só depende de C: quando bicos fecham, basta a válvula abrir até C voltar ao valor de antes.

### Slide 8: Modelo R₁/n² (0:45)
> Com os bicos em paralelo, a resistência equivalente da barra é a resistência de um bico dividida por n ao quadrado: dobrando os bicos abertos, ela cai para um quarto. Embaixo está o modelo de Rosa, Terra e Drews Junior: uma soma de duas exponenciais, com quatro coeficientes ajustados aos dados. O meu modelo usa um único parâmetro físico, a constante do bico. O erro relativo máximo foi de 5,9 por cento, contra 18,5 da fórmula empírica.

### Slide 9: Validação ⏩ (0:35)
> O modelo reproduziu os sete pontos medidos com erro de até 0,7 por cento na pressão e 2,3 na vazão. Prevendo cada ponto sem usá-lo no ajuste, 0,9 e 2,7. E ele mostrou uma regra de projeto: a válvula de alívio só baixa a pressão, então a referência tem de ficar abaixo do que a fonte sustenta com todos os bicos. Por isso foi adotado 3,5.

*Se atrasado: "O modelo reproduziu os dados com menos de 1 por cento de erro na pressão, e a referência adotada foi 3,5."*

### Slide 10: Modelo dinâmico (0:45)
> A dinâmica tem duas partes. Primeiro, a pressão: ela só demora para mudar por causa do termo V sobre beta, a capacitância da linha. Como a mangueira é curta e cheia, esse termo é pequeno, e a pressão foi tratada como instantânea. Conferi com um modelo que inclui a mangueira, e a diferença foi de no máximo 0,4 ponto percentual. Segundo, a válvula: ela é um sistema de primeira ordem, com constante de tempo de 0,2 segundo, mas o motor não passa de 0,5 por segundo. Esses dois valores são estimados. A simulação avança de milissegundo em milissegundo, e o controlador lê a pressão em todo passo.

### Slide 11: Estratégia de controle (0:45)
> A pressão é a variável controlada, a abertura da válvula é a manipulada e o número de bicos é a perturbação. O erro é definido ao contrário do usual, porque abrir a válvula baixa a pressão. Comparei três controladores, cada um acrescentando algo: o P, o PI e o PI com *feedforward*, em que a abertura é antecipada pelo número de bicos. O sensor e o controlador leem a pressão em tempo real, e há anti-windup no limite de posição. A ação derivativa ficou de fora, porque amplifica o ruído e os saltos de pressão.

### Slide 12: Feedforward, ganho da planta e do distúrbio (0:50)
> O próprio modelo estático dá duas coisas. Invertendo-o, sai a abertura de equilíbrio para cada número de bicos: uma reta, 0,121 por bico, que é o *feedforward*. Derivando-o no ponto de operação nominal, com sete bicos e a pressão na referência, saem os ganhos. Como a pressão só depende de C, basta saber quanto ela muda com C, pela derivada implícita da Equação 3.15: menos 0,760. A válvula entra em C com peso K v max e o bico com peso K, então o ganho da planta é menos 2,66 e o do distúrbio é menos 0,323 por bico. Eles são iguais para qualquer número de bicos, e por isso uma única sintonia serve para todos os casos.

### Slide 13: Malha em Laplace (1:00)
> Para projetar, linearizei o modelo no ponto nominal. Cada vazão vira a sua reta tangente, e, juntando as peças no nó, como na Tabela 3, sai a planta linear: menos 2,66 por unidade de abertura e menos 0,323 por bico, os mesmos ganhos de antes. A referência fica fixa, então a única entrada da malha é o número de bicos, uma perturbação em degrau. O ganho de malha L é o produto dos blocos na volta: controlador, válvula e planta. A resposta aos bicos é T n, igual a K n sobre 1 mais L. Pelo teorema do valor final, o P deixa 0,101 de erro por bico, e o PI zera o erro. Com *feedforward*, o denominador é o mesmo, então a estabilidade não muda; ele cancela o bico em regime, mas não no instante da troca.

### Slide 14: Sintonia por alocação de polos (0:45)
> A sintonia foi feita de trás para frente, por alocação de polos. Escolhi amortecimento de 0,7 e acomodação em meio segundo. Igualando a equação característica do PI à forma padrão de segunda ordem, saem Kc de 0,827 e Ti de 0,084 segundo, com polos em menos 8 mais ou menos j 8,2. O P usa o mesmo Kc, e os polos são os mesmos com e sem *feedforward*. Como o controlador lê em tempo real, a malha linear é estável para qualquer ganho positivo. Na figura, sem o limite de velocidade o simulador fica em cima da função de transferência; com o limite, a correção demora mais.

*Se atrasado: "A alocação de polos deu Kc 0,827 e Ti 0,084, e a função de transferência bate com o simulador."*

### Slide 15: Cenários e métricas ⏩ (0:20)
> Simulei três cenários: C1, um bico de cada vez; C2, degraus de três bicos; e C3, trocas aleatórias rápidas. O critério principal é o tempo com a pressão fora da faixa de mais ou menos 10 por cento.

### Slide 16: Resultados: Tabela 10 (0:40)
> Esta é a Tabela 10 do trabalho, e o negrito marca o melhor de cada cenário. Sem controle, a pressão fica de 69 a 91 por cento do tempo fora da faixa. O P reduz para 38 a 50 por cento, mas deixa erro permanente. O PI elimina o erro e é o melhor nos três cenários. O *feedforward* não supera o PI. Agora vou mostrar cada cenário.

### Slide 17: Cenário C1: um bico por vez (0:35)
> Os gráficos dos três cenários têm o mesmo formato: em cima, a pressão com a faixa em verde; no meio, a abertura da válvula; embaixo, o número de bicos. No C1, cada troca dá um salto de 9,5 por cento, dentro da faixa. O P para acima de 3,5 a cada degrau e sai da faixa a partir do quarto bico fechado. O PI fica 100 por cento do tempo na faixa e acomoda em 0,44 segundo.

### Slide 18: Cenário C2: degraus de três bicos (0:40)
> O C2 repete o ensaio da bancada: três bicos fecham em 2 segundos e mais três em 8. O P para em 3,81 e 4,12, exatamente o que a conta do erro previa. O PI e o PI com *feedforward* têm o mesmo resultado: 6,8 por cento fora da faixa e volta à referência em cerca de um segundo. O pico de 29,7 por cento não some com nenhum controlador, porque a pressão salta para 4,54 antes de a válvula se mover.

### Slide 19: Cenário C3: trocas aleatórias rápidas (0:25)
> O C3 imita a aplicação localizada: 66 trocas em 20 segundos, mais rápidas do que a malha acomoda. O PI fica 92 por cento do tempo na faixa, e o *feedforward* um pouco pior, com 9,5 por cento fora. As saídas acontecem quando várias trocas no mesmo sentido chegam seguidas e a válvula não consegue acompanhar.

### Slide 20: Gargalo: velocidade da válvula (0:40)
> O que mais pesa no resultado é a velocidade da válvula. O pico de 29,7 por cento do C2 é o mesmo da malha aberta, porque a válvula ainda está na posição antiga quando a pressão salta. Como o PI já reage na troca, a válvula anda em rampa com ou sem *feedforward*, e no C2 os dois empatam em todas as velocidades. A tabela mostra o efeito de uma válvula mais rápida: duas vezes mais rápida, o PI no C3 cai de 8,3 para 0,4 por cento.

### Slide 21: Conclusões (0:50)
> Concluindo: um modelo simples, com uma constante de bico e uma curva de fonte, reproduziu a bancada. Como o ganho da planta não depende do número de bicos, uma única sintonia por alocação de polos serve para todos os casos. O PI atende a tolerância na maior parte do tempo, e o *feedforward* não trouxe ganho sobre ele. As trocas simultâneas de vários bicos ainda tiram a pressão da faixa, porque a válvula não é rápida o bastante. Por isso a hipótese foi confirmada em parte e só em simulação: os parâmetros da válvula foram estimados.

### Slide 22: Trabalhos futuros e agradecimento (0:30)
> Como próximos passos: medir a velocidade e a curva da válvula na bancada, medir a resposta da malha e ajustar a especificação considerando o ruído do sensor, e testar uma válvula mais rápida ou antecipar o comando antes das solenoides. Agradeço a atenção e fico à disposição para as perguntas.

---

## Perguntas prováveis da banca (respostas curtas)

| Pergunta | Resposta em uma frase | Onde no TCC |
|---|---|---|
| Por que não validou com medições no tempo? | O artigo de referência só publica pontos em regime; por isso a parte dinâmica é estudo de projeto, e a validação é o primeiro trabalho futuro. | 3.8, Conclusão |
| De onde vêm τ_a e ω_max? | São estimativas, porque a bancada não informa a velocidade da válvula; por isso repeti os resultados com válvulas 2× e 4× mais rápidas. | 3.4.2, 4.6 |
| Por que alocação de polos? | Com o modelo pronto, a malha do PI tem dois polos, e dá para escolher ζ e t_s e calcular K_c e T_i direto da função de transferência. | 2.6.2, 3.5.6 |
| De onde saem K_g e K_n? | Da derivada implícita do equilíbrio do nó no ponto nominal: P depende só de C, dP/dC = −0,760, e a válvula e o bico entram em C com pesos K_v,max e K. A Tabela 3 monta os mesmos ganhos peça por peça. | 3.5.2, 3.5.4 |
| Por que a malha em Laplace só tem os bicos como entrada? | A referência fica fixa na operação; o caso é o de perturbação em degrau com referência nula (Castrucci, seção 3.11.3). | 3.5.4, 3.5.5 |
| Por que o *feedforward* é −K_n/K_g? | Para cancelar o efeito de um bico na pressão, K_n·ΔN, a válvula precisa dar o efeito oposto, K_g·ΔA = −K_n·ΔN; logo ΔA = −(K_n/K_g)·ΔN = +0,121 por bico fechado. | 3.5.5 |
| Um controlador real não é amostrado? | É; aqui a leitura foi considerada em tempo real (a cada 1 ms). Pela regra de Castrucci (seção 12.6), basta amostrar ao menos 10 vezes mais rápido que a oscilação da malha, cerca de 77 ms. | 3.8 |
| Por que não usou a ação derivativa? | Ela amplifica o ruído e os saltos de pressão das trocas de bico, e o PI já coloca os dois polos onde se quer. | 2.6, 3.5.6 |
| Por que o *feedforward* não ajudou? | O PI, lendo em tempo real, já manda abrir a válvula no instante da troca; a válvula anda em rampa nos dois casos, e nas trocas rápidas o FF persegue alvos que mudam. | 4.6 |
| Por que o anti-windup só no limite de posição? | É a técnica descrita na literatura (Fernandes; Goldemberg, 2001); estendê-lo ao limite de velocidade baixou o C3 de 8,3% para 3,2% num teste e ficou como trabalho futuro. | 3.5.3, 4.5 |
| Com o anti-windup também na velocidade, o *feedforward* continua pior? | Não: no teste, o C3 fica com 3,2% (PI) e 3,1% (PI+FF), praticamente iguais. A pequena desvantagem do FF vinha do integrador somando durante a rampa; mesmo assim ele não traz vantagem. *(Pergunta levantada na banca simulada; o texto da v20 ainda não diz isso.)* | 4.5, 4.6 |
| Por que o C1 dá 0% fora da faixa? | Fechar um bico em malha aberta sobe a pressão cerca de 9,5%, ainda dentro dos 10%; o que o PI garante é voltar à referência, sem erro permanente. *(Banca simulada.)* | 4.5 |
| A hipótese de pressão instantânea vale? | Para a bancada, sim: com a mangueira modelada, a diferença foi de no máximo 0,4 ponto percentual; em barras longas precisa ser revista. | 3.4.1, 4.2 |
| Por que P_ref = 3,5 e não 4,0 kgf/cm²? | A válvula de alívio só baixa a pressão, e com sete bicos a fonte sustenta 3,56; 4,0 não seria atingível. | 4.1 |
| O modelo vale para barras comerciais? | A lei R₁/n² vale para bicos iguais, desde que a perda ao longo da barra seja desprezível; em barras longas é preciso incluir essa perda. | 3.3.1, 3.8 |

## Dicas para o dia

- Ensaie com cronômetro duas vezes e anote em que slide você está aos 5 e aos 10 minutos (deve ser o 8 e o 15).
- Nos slides com tabela (6, 16 a 20), aponte só a linha de que está falando; não leia a tabela inteira.
- Fale para a banca, não para a tela; aponte só o número ou a curva de que está falando.
- Nos slides com gráfico (8, 9, 14 e 17 a 19), diga primeiro o que o eixo mostra e depois o resultado.
- No slide 13, aponte no diagrama os dois caminhos do número de bicos: pelo bloco do distúrbio, direto na pressão, e pelo *feedforward*, no comando da válvula.
- Se uma pergunta for sobre algo que não foi feito, diga isso diretamente e cite a limitação ou o trabalho futuro correspondente.
