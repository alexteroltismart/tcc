# Roteiro da apresentação: 15 minutos

Este roteiro acompanha a apresentação `Apresentacao_Banca_TCC_v19.pptx` (20 slides), que corresponde à versão 19 do TCC (`docs/19.pdf`). Todas as figuras e tabelas dos slides são do próprio TCC.

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
| 9 | Validação ⏩ | 0:35 | 5:55 |
| 10 | Modelo dinâmico | 0:50 | 6:45 |
| 11 | Estratégia de controle | 0:45 | 7:30 |
| 12 | Feedforward, ganho da planta e do distúrbio | 0:45 | 8:15 |
| 13 | Malha em Laplace: referência e bicos somados | 1:00 | 9:15 |
| 14 | Sintonia por alocação de polos | 0:50 | 10:05 |
| 15 | Cenários e métricas ⏩ | 0:20 | 10:25 |
| 16 | Resultados: Tabela 10 | 0:55 | 11:20 |
| 17 | Respostas nos três cenários | 0:50 | 12:10 |
| 18 | Gargalo: velocidade da válvula | 0:45 | 12:55 |
| 19 | Conclusões | 0:50 | 13:45 |
| 20 | Trabalhos futuros e agradecimento | 0:35 | 14:20 |

**Pontos de controle do relógio:**
- no slide 7 você deve estar perto de **3:35**;
- no slide 13, perto de **8:15**;
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
> A hipótese é que um modelo de resistências fluídicas, com a bomba, os bicos e a válvula de alívio, junto com a dinâmica da válvula, basta para projetar um controlador simples que segure a pressão dentro de mais ou menos 10 por cento. Essa é a tolerância da norma de inspeção de pulverizadores, a ISO 16122-2, e corresponde a cerca de 5 por cento na vazão de cada bico. Os objetivos foram modelar, acrescentar a dinâmica, sintonizar os controladores por alocação de polos e compará-los em simulação.

### Slide 5: Roteiro ⏩ (0:20)
> O trabalho seguiu sete etapas, em que cada uma entrega a entrada da seguinte. A base é o modelo estático, reaproveitado no simulador e no controle. Vou seguir essa ordem.

*Se atrasado: "O trabalho seguiu sete etapas, na ordem que vou apresentar."*

### Slide 6: Bancada de referência e Tabela 1 (0:45)
> A bancada de referência tem uma barra de cinco metros com sete bicos e solenoides, uma bomba de pistão com uma válvula de mola que devolve o excesso ao tanque, e uma válvula agulha com servomotor, que é o atuador. A tabela traz os dados medidos com a válvula de alívio fechada: fechando bicos, a pressão sobe, a vazão cai e a resistência P sobre Q ao quadrado cresce muito depressa. São esses sete pontos que usei para ajustar o modelo.

### Slide 7: Modelo estático (1:00)
> O modelo responde: com n bicos abertos e a válvula numa certa abertura, qual é a pressão? Três caminhos se encontram num único nó: a fonte empurra líquido, e os bicos e a válvula deixam sair. Cada bico segue a lei de orifício, q igual a K raiz de P. A fonte é uma curva de segundo grau ajustada por mínimos quadrados, e a válvula é linear na abertura. Em regime, o que entra é igual ao que sai. Juntando bicos e válvula na capacidade de saída C, isso vira uma equação de segundo grau, e a pressão sai de forma explícita, pela Equação 3.11. A pressão só depende de C: quando bicos fecham, basta a válvula abrir até C voltar ao valor de antes.

### Slide 8: Modelo R₁/n² (0:45)
> Com os bicos em paralelo, a resistência equivalente da barra é a resistência de um bico dividida por n ao quadrado: dobrando os bicos abertos, ela cai para um quarto. Embaixo está o modelo de Rosa, Terra e Drews Junior: uma soma de duas exponenciais, com quatro coeficientes ajustados aos dados. O meu modelo usa um único parâmetro físico, a constante do bico. O erro relativo máximo foi de 5,9 por cento, contra 18,5 da fórmula empírica.

### Slide 9: Validação ⏩ (0:35)
> O modelo reproduziu os sete pontos medidos com erro de até 0,7 por cento na pressão e 2,3 na vazão. Prevendo cada ponto sem usá-lo no ajuste, 0,9 e 2,7. E ele mostrou uma regra de projeto: a válvula de alívio só baixa a pressão, então a referência tem de ficar abaixo do que a fonte sustenta com todos os bicos. Por isso foi adotado 3,5.

*Se atrasado: "O modelo reproduziu os dados com menos de 1 por cento de erro na pressão, e a referência adotada foi 3,5."*

### Slide 10: Modelo dinâmico (0:50)
> A dinâmica tem duas partes. Primeiro, a pressão: ela só demora para mudar por causa do termo V sobre beta, a capacitância da linha. Como a mangueira é curta e cheia, esse termo é pequeno, e a pressão foi tratada como instantânea. Conferi com um modelo que inclui a mangueira, e a diferença foi de no máximo 0,4 ponto percentual. Segundo, a válvula: ela é um sistema de primeira ordem, com constante de tempo de 0,2 segundo, mas o motor não passa de 0,5 por segundo. Esses dois valores são estimados. A simulação avança de milissegundo em milissegundo, pelo método de Euler, e o controlador lê a pressão em todo passo, em tempo real.

### Slide 11: Estratégia de controle (0:45)
> A pressão é a variável controlada, a abertura da válvula é a manipulada e o número de bicos é a perturbação. O erro é definido ao contrário do usual, porque abrir a válvula baixa a pressão. Comparei três controladores, cada um acrescentando algo: o P, o PI e o PI com *feedforward*, em que a abertura é antecipada pelo número de bicos. O sensor e o controlador leem a pressão em tempo real, e há anti-windup no limite de posição. A ação derivativa ficou de fora, porque amplifica o ruído e os saltos de pressão.

### Slide 12: Feedforward, ganho da planta e do distúrbio (0:45)
> O próprio modelo estático dá duas coisas. Invertendo-o, sai a abertura de equilíbrio para cada número de bicos: uma reta, 0,121 por bico, que é o *feedforward*. Derivando-o, saem os ganhos. Como a pressão só depende de C, basta saber quanto ela muda com C: menos 0,760. A válvula entra em C com peso K v max e o bico com peso K, então o ganho da planta é menos 2,66 e o do distúrbio é menos 0,323 por bico. Eles são iguais para qualquer número de bicos, e por isso uma única sintonia serve para todos os casos.

### Slide 13: Malha em Laplace (1:00)
> Para projetar, linearizei a malha em torno de sete bicos e a escrevi no domínio de Laplace. Ela tem duas entradas: a referência e o número de bicos. Como o modelo linearizado é linear, vale a superposição: calculo o efeito de cada entrada com a outra zerada e somo no fim. A resposta à referência é T r, L sobre 1 mais L; a resposta aos bicos é T n, K n sobre 1 mais L. As duas têm o mesmo denominador, então têm os mesmos polos: uma única sintonia serve para seguir a referência e para rejeitar os bicos. Daí sai também que o P só segue 69 por cento de uma mudança de referência e deixa 0,1 de erro por bico, enquanto o PI zera o erro nas duas.

### Slide 14: Sintonia por alocação de polos (0:50)
> A sintonia foi feita de trás para frente, por alocação de polos, como no Ogata. Escolhi amortecimento de 0,7 e acomodação em meio segundo. Igualando a equação característica do PI à forma padrão de segunda ordem, saem Kc de 0,827 e Ti de 0,084 segundo, com polos em menos 8 mais ou menos j 8,2. O P usa o mesmo Kc. Como o controlador lê em tempo real, a malha é estável para qualquer ganho positivo. A figura confirma: sem o limite de velocidade, o simulador fica em cima da função de transferência; com o limite, a válvula anda em rampa e a correção demora mais.

*Se atrasado: "A alocação de polos deu Kc 0,827 e Ti 0,084, e a função de transferência bate com o simulador."*

### Slide 15: Cenários e métricas ⏩ (0:20)
> Simulei três cenários: C1, um bico de cada vez; C2, degraus de três bicos; e C3, trocas aleatórias rápidas. O critério principal é o tempo com a pressão fora da faixa de mais ou menos 10 por cento.

### Slide 16: Resultados: Tabela 10 (0:55)
> Esta é a Tabela 10 do trabalho, e o negrito marca o melhor de cada cenário. Sem controle, a pressão fica de 69 a 91 por cento do tempo fora da faixa. O P reduz bastante, mas deixa erro permanente e não acomoda nos degraus. O PI elimina o erro: 100 por cento do tempo na faixa no C1, acomodando em 0,44 segundo, e 8,3 por cento fora no C3. O *feedforward* não supera o PI: empata no C2 e piora um pouco no C3, para 9,5 por cento. O motivo é que o PI, lendo em tempo real, já reage no instante da troca.

### Slide 17: Respostas nos três cenários (0:50)
> Os três gráficos mostram, de cima para baixo, a pressão com a faixa em verde, a abertura da válvula e o número de bicos. No C1, o PI e o PI com *feedforward* ficam sempre na faixa, e o P para acima de 3,5 a cada degrau. No C2, o P para em 3,81 e 4,12, exatamente o que a conta do erro previa; o PI volta à referência em cerca de um segundo; e o pico de cerca de 30 por cento não some, porque a pressão salta antes de a válvula se mover. No C3, o PI fica 92 por cento do tempo na faixa.

### Slide 18: Gargalo: velocidade da válvula (0:45)
> O que mais pesa no resultado é a velocidade da válvula. No C3 ela passa 75 por cento do tempo na velocidade máxima. Como o PI já reage na troca, a válvula anda em rampa com ou sem *feedforward*, e no C2 os dois empatam em todas as velocidades. A tabela mostra o efeito de uma válvula mais rápida: duas vezes mais rápida, o PI no C3 cai de 8,3 para 0,4 por cento.

### Slide 19: Conclusões (0:50)
> Concluindo: um modelo simples, com uma constante de bico e uma curva de fonte, reproduziu a bancada. Como o ganho da planta não depende do número de bicos, e a referência e os bicos têm os mesmos polos, uma única sintonia por alocação de polos serve para tudo. O PI atende a tolerância na maior parte do tempo, e o *feedforward* não trouxe ganho sobre ele. As trocas simultâneas de vários bicos ainda tiram a pressão da faixa, porque a válvula não é rápida o bastante. Por isso a hipótese foi confirmada em parte e só em simulação: os parâmetros da válvula foram estimados.

### Slide 20: Trabalhos futuros e agradecimento (0:35)
> Como próximos passos: medir a velocidade e a curva da válvula na bancada, medir a resposta da malha e ajustar a especificação considerando o ruído do sensor, e testar uma válvula mais rápida ou antecipar o comando antes das solenoides. Agradeço a atenção e fico à disposição para as perguntas.

---

## Perguntas prováveis da banca (respostas curtas)

| Pergunta | Resposta em uma frase | Onde no TCC |
|---|---|---|
| Por que não validou com medições no tempo? | O artigo de referência só publica pontos em regime; por isso a parte dinâmica é estudo de projeto, e a validação é o primeiro trabalho futuro. | 3.8, Conclusão |
| De onde vêm τ_a e ω_max? | São estimativas, porque a bancada não informa a velocidade da válvula; por isso repeti os resultados com válvulas 2× e 4× mais rápidas. | 3.4.2, 4.6 |
| Por que alocação de polos? | Com o modelo pronto, a malha do PI tem dois polos, e dá para escolher ζ e t_s e calcular K_c e T_i direto da função de transferência. | 2.6.1, 3.5.6 |
| De onde saem K_g e K_n? | Da derivada implícita do equilíbrio do nó: P depende só de C, dP/dC = −0,760, e a válvula e o bico entram em C com pesos K_v,max e K. | 3.5.4 |
| Por que o *feedforward* é −K_n/K_g? | Para cancelar o efeito de um bico na pressão, K_n·ΔN, a válvula precisa dar o efeito oposto, K_g·ΔA = −K_n·ΔN; logo ΔA = −(K_n/K_g)·ΔN = +0,121 por bico fechado. | 3.5.5 |
| Por que a resposta à referência tem sobressinal de 10,7% e não 4,6%? | O PI tem um zero em −1/T_i, perto dos polos, que soma a derivada da resposta; a sintonia foi feita para os polos, e nos cenários a referência é fixa. | 3.5.5, 4.2 |
| Um controlador real não é amostrado? | É; aqui a leitura foi considerada em tempo real (a cada 1 ms). Intervalos grandes em relação a τ_a trariam atraso e um ganho máximo, o que está nas limitações. | 3.8 |
| Por que não usou a ação derivativa? | Ela amplifica o ruído e os saltos de pressão das trocas de bico, e o PI já coloca os dois polos onde se quer. | 2.6, 3.5.6 |
| Por que o *feedforward* não ajudou? | O PI, lendo em tempo real, já manda abrir a válvula no instante da troca; a válvula anda em rampa nos dois casos, e nas trocas rápidas o FF persegue alvos que mudam. | 4.6 |
| Por que o anti-windup só no limite de posição? | É a técnica descrita na literatura (Fernandes; Goldemberg, 2001); estendê-lo ao limite de velocidade baixou o C3 de 8,3% para 3,2% num teste e ficou como trabalho futuro. | 3.5.3, 4.5 |
| A hipótese de pressão instantânea vale? | Para a bancada, sim: com a mangueira modelada, a diferença foi de no máximo 0,4 ponto percentual; em barras longas precisa ser revista. | 3.4.1, 4.2 |
| Por que P_ref = 3,5 e não 4,0 kgf/cm²? | A válvula de alívio só baixa a pressão, e com sete bicos a fonte sustenta 3,56; 4,0 não seria atingível. | 4.1 |
| O modelo vale para barras comerciais? | A lei R₁/n² vale para bicos iguais, desde que a perda ao longo da barra seja desprezível; em barras longas é preciso incluir essa perda. | 3.3.1, 3.8 |

## Dicas para o dia

- Ensaie com cronômetro duas vezes e anote em que slide você está aos 5 e aos 10 minutos (deve ser o 8 e o 14).
- Nos slides com tabela (6, 16 e 18), aponte só a linha de que está falando; não leia a tabela inteira.
- Fale para a banca, não para a tela; aponte só o número ou a curva de que está falando.
- Nos slides com gráfico (8, 9, 14 e 17), diga primeiro o que o eixo mostra e depois o resultado.
- No slide 13, aponte no diagrama onde entra cada entrada: a referência no primeiro somador, os bicos no distúrbio e no *feedforward*.
- Se uma pergunta for sobre algo que não foi feito, diga isso diretamente e cite a limitação ou o trabalho futuro correspondente.
