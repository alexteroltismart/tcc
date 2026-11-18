# Roteiro da apresentação: 15 minutos

Este roteiro acompanha a apresentação `Apresentacao_Banca_TCC_v15.pptx` (20 slides). Todas as figuras e tabelas dos slides são do próprio TCC.

**Tempo:**
- O tempo previsto de fala é de **14 min 20 s**. Sobram 40 s de folga para imprevistos.
- O ritmo de referência é de cerca de 130 palavras por minuto. Cada fala abaixo foi escrita para caber no tempo do slide.
- Não é preciso decorar o texto: use as falas como guia e diga com suas palavras.

**Onde ganhar tempo:**
- Se estiver atrasado, encurte os slides marcados com ⏩. Eles podem ser ditos em uma frase.
- Nunca corte os slides 16, 17, 18 e 19 (resultados, três cenários, gargalo e conclusões).

---

## Mapa de tempo

| Slide | Assunto | Tempo | Acumulado |
|---|---|---|---|
| 1 | Capa | 0:15 | 0:15 |
| 2 | Título | 0:30 | 0:45 |
| 3 | O problema | 1:00 | 1:45 |
| 4 | Objetivo e hipótese | 0:45 | 2:30 |
| 5 | Roteiro ⏩ | 0:20 | 2:50 |
| 6 | Bancada de referência e Tabela 1 | 0:45 | 3:35 |
| 7 | Modelo estático | 1:00 | 4:35 |
| 8 | Modelo R₁/n² | 0:45 | 5:20 |
| 9 | Validação ⏩ | 0:40 | 6:00 |
| 10 | Modelo dinâmico | 0:55 | 6:55 |
| 11 | Estratégia de controle | 0:55 | 7:50 |
| 12 | Feedforward e ganho da planta | 0:40 | 8:30 |
| 13 | Sintonia de Ziegler-Nichols | 0:55 | 9:25 |
| 14 | Função de transferência ⏩ | 0:35 | 10:00 |
| 15 | Cenários e métricas ⏩ | 0:20 | 10:20 |
| 16 | Resultados: Tabela 10 | 0:55 | 11:15 |
| 17 | Respostas nos três cenários | 0:55 | 12:10 |
| 18 | Gargalo: velocidade da válvula | 0:45 | 12:55 |
| 19 | Conclusões | 0:50 | 13:45 |
| 20 | Trabalhos futuros e agradecimento | 0:35 | 14:20 |

**Pontos de controle do relógio:**
- no slide 7 você deve estar perto de **3:35**;
- no slide 13, perto de **8:30**;
- no slide 19, perto de **12:55**.

Se estiver mais de 30 s atrasado num desses pontos, use os ⏩.

---

## Falas

### Slide 1: Capa (0:15)
> Boa tarde a todos. Agradeço a presença da banca e do meu orientador.

### Slide 2: Título (0:30)
> Meu nome é Alex de Jesus Terolti, e o meu trabalho é "Modelagem de sistema de controle para pulverização agrícola de precisão", com orientação do professor Rogério Bastos Quirino. Em resumo: controlar a pressão de uma barra de pulverização bico a bico usando uma válvula de alívio, com um modelo simples e controladores clássicos, tudo em simulação.

### Slide 3: O problema (1:00)
> Na pulverização localizada, cada bico abre e fecha sozinho, o que economiza produto. Só que, quando os bicos são alimentados por uma mesma mangueira, em série, cada troca muda a pressão dos outros. A figura é o ensaio da bancada de Rosa, Terra e Drews Junior, de 2019: fechando três bicos, a pressão sobe de 4,0 para 5,8; abrindo a válvula de alívio à mão, ela volta. Com a válvula fechada, indo de sete para um bico, a pressão sobe 56 por cento. Como a vazão do bico varia com a raiz da pressão, isso muda a dose aplicada e o tamanho das gotas.

### Slide 4: Objetivo e hipótese (0:45)
> A hipótese é que um modelo de resistências fluídicas, com a bomba, os bicos e a válvula de alívio, junto com a dinâmica da válvula, basta para projetar um controlador simples que segure a pressão dentro de mais ou menos 10 por cento. Essa é a tolerância da norma de inspeção de pulverizadores, a ISO 16122-2, e corresponde a cerca de 5 por cento na vazão de cada bico. Os objetivos foram modelar, acrescentar a dinâmica, sintonizar os controladores e compará-los em simulação.

### Slide 5: Roteiro ⏩ (0:20)
> O trabalho seguiu sete etapas, em que cada uma entrega a entrada da seguinte. A base é o modelo estático, reaproveitado no simulador e no controle. Vou seguir essa ordem.

*Se atrasado: "O trabalho seguiu sete etapas, na ordem que vou apresentar."*

### Slide 6: Bancada de referência e Tabela 1 (0:45)
> A bancada de referência tem uma barra de cinco metros com sete bicos e solenoides, uma bomba de pistão com uma válvula de mola que devolve o excesso ao tanque, e uma válvula agulha com servomotor, que é o atuador. A tabela traz os dados medidos com a válvula de alívio fechada: fechando bicos, a pressão sobe, a vazão cai e a resistência P sobre Q ao quadrado cresce muito depressa. São esses sete pontos que usei para ajustar o modelo.

### Slide 7: Modelo estático (1:00)
> O modelo responde: com n bicos abertos e a válvula numa certa abertura, qual é a pressão? Três caminhos se encontram num único nó: a fonte empurra líquido, e os bicos e a válvula deixam sair. Cada bico segue a lei de orifício, q igual a K raiz de P. A fonte é uma curva de segundo grau ajustada por mínimos quadrados, e a válvula é linear na abertura. Em regime, o que entra é igual ao que sai. Juntando bicos e válvula na capacidade de saída C, isso vira uma equação de segundo grau, e a pressão sai de forma explícita, pela Equação 3.11. Repare que P só depende de C: quando bicos fecham, basta a válvula abrir até C voltar ao valor de antes.

### Slide 8: Modelo R₁/n² (0:45)
> Com os bicos em paralelo, a resistência equivalente da barra é a resistência de um bico dividida por n ao quadrado: dobrando os bicos abertos, ela cai para um quarto. Embaixo está o modelo de Rosa, Terra e Drews Junior: uma soma de duas exponenciais, com quatro coeficientes ajustados aos dados. O meu modelo usa um único parâmetro físico, a constante do bico. O erro relativo máximo foi de 5,9 por cento, contra 18,5 da fórmula empírica.

### Slide 9: Validação ⏩ (0:40)
> O modelo reproduziu os sete pontos medidos com erro de até 0,7 por cento na pressão e 2,3 na vazão. Prevendo cada ponto sem usá-lo no ajuste, 0,9 e 2,7. E ele mostrou uma regra de projeto: a válvula de alívio só baixa a pressão, então a referência tem de ficar abaixo do que a fonte sustenta com todos os bicos. Por isso foi adotado 3,5.

*Se atrasado: "O modelo reproduziu os dados com menos de 1 por cento de erro na pressão, e a referência adotada foi 3,5."*

### Slide 10: Modelo dinâmico (0:55)
> A dinâmica tem duas partes. Primeiro, a pressão: pela continuidade com compressibilidade, ela só demora para mudar por causa do termo V sobre beta, a capacitância da linha. Como a mangueira é curta e cheia, esse termo é pequeno, e a pressão foi tratada como instantânea. Conferi com um modelo que inclui a mangueira, e a diferença foi de no máximo 0,6 ponto percentual. Segundo, a válvula, que é esta agulha com servomotor: ela é um sistema de primeira ordem, com constante de tempo de 0,2 segundo, mas o motor não passa de 0,5 por segundo. Quando três bicos fecham, ela anda meio segundo em rampa e depois se aproxima do comando. Esses dois valores são estimados. A simulação avança de milissegundo em milissegundo, pelo método de Euler.

### Slide 11: Estratégia de controle (0:55)
> A pressão é a variável controlada, a abertura da válvula é a manipulada e o número de bicos é a perturbação. O erro é definido ao contrário do usual, porque abrir a válvula baixa a pressão. Comparei três controladores, cada um acrescentando algo: o P, o PI e o PI com *feedforward*, em que a abertura é antecipada pelo número de bicos. Todos são amostrados a cada 50 milissegundos, com anti-windup. A ação derivativa ficou de fora, porque amplifica o ruído e os saltos de pressão.

### Slide 12: Feedforward e ganho da planta (0:40)
> O próprio modelo estático dá duas coisas. Invertendo-o, sai a abertura de equilíbrio para cada número de bicos: uma reta, 0,121 por bico, que é o *feedforward*. Derivando-o, sai o ganho da planta, menos 2,66, e ele é igual para qualquer número de bicos. Isso quer dizer que uma única sintonia serve para todos os casos.

### Slide 13: Sintonia de Ziegler-Nichols (0:55)
> Para sintonizar, usei o segundo método de Ziegler-Nichols, feito no próprio simulador: só a ação proporcional, um bico fecha e o ganho é aumentado até a pressão oscilar sem parar. A bissecção deu ganho crítico de 2,93, com período de 0,1 segundo, que é igual a duas leituras do controlador. Ou seja, quem limita o ganho é a amostragem. As regras deram os ganhos da tabela: 1,46 para o P e 1,32 com tempo integral de 0,083 segundo para o PI.

*Se houver tempo, mostrar a página interativa do ensaio.*

### Slide 14: Função de transferência ⏩ (0:35)
> Linearizando a malha e escrevendo as funções de transferência, seguindo o Ogata, aparecem três coisas: o P deixa um erro de 0,066, igual ao simulador; o s no numerador do PI faz o erro final ser zero; e o *feedforward* muda só o numerador, então não altera a estabilidade. A figura confirma: sem o limite de velocidade, o simulador segue a função de transferência.

*Se atrasado: "A função de transferência confirma o erro do P e mostra que o PI zera o erro."*

### Slide 15: Cenários e métricas ⏩ (0:20)
> Simulei três cenários: C1, um bico de cada vez; C2, degraus de três bicos; e C3, trocas aleatórias rápidas. O critério principal é o tempo com a pressão fora da faixa de mais ou menos 10 por cento.

### Slide 16: Resultados: Tabela 10 (0:55)
> Esta é a Tabela 10 do trabalho, e o negrito marca o melhor de cada cenário. Sem controle, a pressão fica de 69 a 91 por cento do tempo fora da faixa. O P reduz bastante, mas deixa erro permanente e não acomoda nos degraus. O PI elimina o erro: 100 por cento do tempo na faixa no C1, acomodando em 0,46 segundo, e cerca de 91 por cento no C3. O *feedforward* melhora o C1 e o C2, com IAE e acomodação menores, mas piora um pouco o C3.

### Slide 17: Respostas nos três cenários (0:55)
> Os três gráficos mostram, de cima para baixo, a pressão com a faixa em verde, a abertura da válvula e o número de bicos. No C1, o PI e o PI com *feedforward* ficam sempre na faixa, e o P para acima de 3,5 a cada degrau. No C2, o P para em 3,70 e 3,90, exatamente o que a conta do erro previa; o PI volta à referência em cerca de um segundo; e o pico de cerca de 30 por cento não some, porque a pressão salta antes de a válvula se mover. No C3, com trocas rápidas, o PI fica 91 por cento do tempo na faixa.

### Slide 18: Gargalo: velocidade da válvula (0:45)
> O que mais pesa no resultado é a velocidade da válvula. No C3 ela passa 77 por cento do tempo na velocidade máxima, e o *feedforward* manda a válvula para um alvo que muda antes de ela chegar. A tabela mostra os resultados com a válvula mais rápida: duas vezes mais rápida, o PI no C3 cai de 8,9 para 2,7 por cento; quatro vezes, o *feedforward* volta a ser o melhor nos dois cenários.

### Slide 19: Conclusões (0:50)
> Concluindo: um modelo simples, com uma constante de bico e uma curva de fonte, reproduziu a bancada. Como o ganho da planta não depende do número de bicos, uma sintonia de Ziegler-Nichols serve para todos os casos. O PI atende a tolerância na maior parte do tempo, mas as trocas simultâneas de vários bicos ainda tiram a pressão da faixa, porque a válvula não é rápida o bastante. Por isso a hipótese foi confirmada em parte e só em simulação: os parâmetros da válvula foram estimados.

### Slide 20: Trabalhos futuros e agradecimento (0:35)
> Como próximos passos: medir a velocidade e a curva da válvula na bancada, refazer a sintonia no equipamento real considerando o ruído do sensor, e testar uma válvula mais rápida ou antecipar o comando antes das solenoides. Agradeço a atenção e fico à disposição para as perguntas.

---

## Perguntas prováveis da banca (respostas curtas)

| Pergunta | Resposta em uma frase | Onde no TCC |
|---|---|---|
| Por que não validou com medições no tempo? | O artigo de referência só publica pontos em regime; por isso a parte dinâmica é estudo de projeto, e a validação é o primeiro trabalho futuro. | 3.8, Conclusão |
| De onde vêm τ_a e ω_max? | São estimativas, porque a bancada não informa a velocidade da válvula; por isso repeti os resultados com válvulas 2× e 4× mais rápidas. | 3.4.2, 4.6 |
| Por que Ziegler-Nichols e não outro método? | É simples, não exige modelo da planta e pode ser feito no simulador; os ganhos foram usados sem ajuste fino, e isso está nas limitações. | 2.6.1, 3.8 |
| Por que a oscilação crítica tem período 2·T_s? | Com ganho alto, o controlador corrige demais numa leitura e demais para o outro lado na seguinte; a teoria discreta dá K_cr = 3,02, perto dos 2,93 do ensaio. | 3.5.4, 4.2 |
| Por que não usou a ação derivativa? | Ela amplifica o ruído e os saltos de pressão das trocas de bico, e o T_d de Ziegler-Nichols seria de 12,5 ms, menor que o período de amostragem de 50 ms. | 2.6 |
| Por que o *feedforward* piora o C3? | A válvula está na velocidade máxima 77% do tempo e não chega ao alvo antes da próxima troca; com válvula 4× mais rápida ele volta a ajudar. | 4.6 |
| Por que o anti-windup só no limite de posição? | É a técnica descrita na literatura (Fernandes; Goldemberg, 2001); estendê-lo ao limite de velocidade baixou o C3 de 8,9% para 5,0% num teste e ficou como trabalho futuro. | 3.5.3, 4.5 |
| A hipótese de pressão instantânea vale? | Para a bancada, sim: com a mangueira modelada, a diferença foi de no máximo 0,6 ponto percentual; em barras longas precisa ser revista. | 3.4.1, 4.2 |
| Por que P_ref = 3,5 e não 4,0 kgf/cm²? | A válvula de alívio só baixa a pressão, e com sete bicos a fonte sustenta 3,56; 4,0 não seria atingível. | 4.1 |
| O modelo vale para barras comerciais? | A lei R₁/n² vale para bicos iguais, desde que a perda ao longo da barra seja desprezível; em barras longas é preciso incluir essa perda. | 3.3.1, 3.8 |

## Dicas para o dia

- Ensaie com cronômetro duas vezes e anote em que slide você está aos 5 e aos 10 minutos (deve ser o 8 e o 15).
- Nos slides com tabela (6, 16 e 18), aponte só a linha de que está falando; não leia a tabela inteira.
- Fale para a banca, não para a tela; aponte só o número ou a curva de que está falando.
- Nos slides com gráfico (8, 9, 13, 14 e 17), diga primeiro o que o eixo mostra e depois o resultado.
- Se uma pergunta for sobre algo que não foi feito, diga isso diretamente e cite a limitação ou o trabalho futuro correspondente.
