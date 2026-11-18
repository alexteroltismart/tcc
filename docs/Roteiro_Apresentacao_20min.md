# Roteiro da apresentação: 20 minutos

Este roteiro acompanha a apresentação `Apresentacao_Banca_TCC_v25.pptx` (27 slides, visual simples), que corresponde à versão 25 do TCC (`docs/25.pdf`). Todas as figuras, tabelas e equações dos slides são do próprio TCC. O roteiro anterior, de 15 minutos e da v20, está em `Roteiro_Apresentacao_15min_v20.md`.

**O que mudou em relação ao roteiro de 15 min:**
- A parte de controle passou de 4 para 7 slides (12 a 18), com a matemática passo a passo: abertura de equilíbrio, linearização, Laplace, malha fechada, alocação de polos e a forma discreta.
- Os números são os da v25: *feedforward* antecipado em 0,2 s, que agora é o melhor controlador (C3: 4,4% contra 8,3% do PI).
- Há um slide introdutório sobre pulverização agrícola (3) e um sobre a antecipação (24, Figura 24).
- A tabela de resultados é a Tabela 9, só com tempo fora da faixa e IAE.

**Tempo:**
- O tempo previsto de fala é de **18 min 40 s**. Sobra 1 min 20 s de folga.
- O ritmo de referência é de cerca de 130 palavras por minuto.
- Não é preciso decorar: use as falas como guia e diga com suas palavras. Nas contas, aponte a equação no slide enquanto fala.

**Onde ganhar tempo:**
- Se estiver atrasado, encurte os slides marcados com ⏩.
- Não corte os slides 16 e 17 (malha fechada e polos): eles são o centro da parte matemática.

---

## Mapa de tempo

| Slide | Assunto | Tempo | Acumulado |
|---|---|---|---|
| 1 | Capa | 0:15 | 0:15 |
| 2 | Título | 0:30 | 0:45 |
| 3 | Pulverização agrícola | 0:45 | 1:30 |
| 4 | Problema | 0:40 | 2:10 |
| 5 | Objetivo e hipótese | 0:40 | 2:50 |
| 6 | Etapas ⏩ | 0:15 | 3:05 |
| 7 | Bancada de referência | 0:40 | 3:45 |
| 8 | Modelo estático | 0:50 | 4:35 |
| 9 | Resistência R₁/n² ⏩ | 0:35 | 5:10 |
| 10 | Validação ⏩ | 0:25 | 5:35 |
| 11 | Modelo dinâmico | 0:40 | 6:15 |
| 12 | Estratégia de controle | 0:50 | 7:05 |
| 13 | Abertura de equilíbrio (*feedforward*) | 0:55 | 8:00 |
| 14 | Linearização | 1:10 | 9:10 |
| 15 | Domínio de Laplace | 0:55 | 10:05 |
| 16 | Malha fechada | 1:25 | 11:30 |
| 17 | Alocação de polos | 1:20 | 12:50 |
| 18 | Forma discreta e conferência | 0:55 | 13:45 |
| 19 | Cenários e métricas ⏩ | 0:20 | 14:05 |
| 20 | Resultados | 0:35 | 14:40 |
| 21 | Cenário C1 | 0:25 | 15:05 |
| 22 | Cenário C2 | 0:35 | 15:40 |
| 23 | Cenário C3 | 0:25 | 16:05 |
| 24 | Feedforward antecipado | 0:45 | 16:50 |
| 25 | Velocidade da válvula | 0:30 | 17:20 |
| 26 | Conclusões | 0:50 | 18:10 |
| 27 | Trabalhos futuros e agradecimento | 0:30 | 18:40 |

**Pontos de controle do relógio:**
- no slide 8, perto de **3:45**;
- no slide 14, perto de **8:00**;
- no slide 19, perto de **13:45**;
- no slide 26, perto de **17:20**.

Se estiver mais de 30 s atrasado num desses pontos, use os ⏩.

---

## Falas

### Slide 1: Capa (0:15)
> Boa tarde a todos. Agradeço a presença da banca e do meu orientador.

### Slide 2: Título (0:30)
> Meu nome é Alex de Jesus Terolti, e o meu trabalho é "Modelagem de sistema de controle para pulverização agrícola de precisão", com orientação do professor Rogério Bastos Quirino. Em resumo: controlar a pressão de uma barra de pulverização bico a bico usando uma válvula de alívio, com um modelo simples e controladores clássicos, tudo em simulação.

### Slide 3: Pulverização agrícola (0:45)
> Para começar, um pouco de contexto. O pulverizador de barras leva a calda do tanque, pela bomba e pelas mangueiras, até os bicos, que quebram o líquido em gotas. Na aplicação convencional, a dose é a mesma na área toda, mas as plantas daninhas e as pragas aparecem em manchas. A pulverização localizada aplica só onde precisa: desliga seções inteiras ou, no caso mais preciso, cada bico sozinho. Só que, no bico a bico em série, uma mangueira alimenta todos os bicos, e cada troca muda a vazão que a barra pede. E é a pressão que define quanto sai de cada bico e o tamanho da gota.

### Slide 4: O problema (0:40)
> Quando bicos fecham, sobra líquido na linha e a pressão sobe; quando abrem, ela cai. Na bancada de Rosa, Terra e Drews Junior, de sete para um bico a pressão sobe 56 por cento. A figura é o ensaio deles: fechando três bicos, a pressão vai de 4,0 para 5,8, e abrindo a válvula de alívio à mão ela volta. Como a vazão do bico varia com a raiz da pressão, isso muda a dose. O problema deste trabalho é fazer essa correção de forma automática.

### Slide 5: Objetivo e hipótese (0:40)
> A hipótese é que um modelo de resistências fluídicas, mais a dinâmica da válvula, basta para projetar um controlador simples que segure a pressão dentro de mais ou menos 10 por cento, a tolerância da ISO 16122-2. Isso dá cerca de 5 por cento na vazão de cada bico. Os objetivos foram modelar, acrescentar a dinâmica, sintonizar os controladores por alocação de polos, acrescentar o *feedforward* e comparar tudo em simulação.

### Slide 6: Roteiro ⏩ (0:15)
> O trabalho seguiu sete etapas, e cada uma entrega a entrada da seguinte. Vou seguir essa ordem.

### Slide 7: Bancada de referência (0:40)
> A bancada tem uma barra de cinco metros com sete bicos e solenoides, uma bomba de pistão com válvula de mola e uma válvula agulha com servomotor, que é o atuador. A tabela traz os dados com a válvula de alívio fechada: fechando bicos, a pressão sobe, a vazão cai e a resistência P sobre Q ao quadrado cresce muito depressa. Esses sete pontos ajustam o modelo.

### Slide 8: Modelo estático (0:50)
> O modelo responde: com n bicos abertos e a válvula numa abertura alfa, qual é a pressão? Três caminhos se encontram num único nó. Cada bico segue a lei de orifício, q igual a K raiz de P. A fonte é uma curva de segundo grau, e a válvula é linear na abertura. Em regime, o que entra é igual ao que sai. Juntando bicos e válvula na capacidade de saída C, a pressão sai de forma explícita, pela Equação 3.11. Guardem essa ideia: a pressão só depende de C. Ela vai voltar no controle.

### Slide 9: Modelo R₁/n² ⏩ (0:35)
> Com bicos iguais em paralelo, a resistência da barra é a de um bico dividida por n ao quadrado. A fórmula empírica de Rosa e colaboradores usa duas exponenciais com quatro coeficientes; o meu modelo usa um único parâmetro físico. O erro relativo máximo foi 5,9 por cento, contra 18,5 da fórmula empírica.

*Se atrasado: "A resistência da barra segue R₁ sobre n ao quadrado, com um parâmetro só e erro máximo de 5,9 por cento."*

### Slide 10: Validação ⏩ (0:25)
> O modelo reproduziu os sete pontos medidos com erro de até 0,7 por cento na pressão e 2,3 na vazão. E deu uma regra de projeto: a válvula de alívio só baixa a pressão, então a referência tem de ficar abaixo do que a fonte sustenta com sete bicos, 3,56. Foi adotado 3,5.

### Slide 11: Modelo dinâmico (0:40)
> A dinâmica tem duas partes. A pressão só demora a mudar por causa do termo V sobre beta; como a mangueira é curta e cheia, ela foi tratada como instantânea. A válvula é de primeira ordem, com tau a de 0,2 segundo, mas o motor não passa de 0,5 por segundo. Esses dois valores são estimados. A simulação avança de milissegundo em milissegundo pelo método de Euler.

### Slide 12: Estratégia de controle (0:50)
> Agora a parte de controle. A variável controlada é a pressão, a manipulada é a abertura da válvula, e o número de bicos é a perturbação. O erro é P menos P ref, ao contrário do usual, porque pressão alta pede abrir a válvula. Os três controladores saem de uma só equação, a 3.19: uma base, uma parcela proporcional ao erro e uma parcela proporcional ao erro acumulado. O P usa só a base fixa e o proporcional. O PI acrescenta a integral. No PI com *feedforward*, a base passa a acompanhar o número de bicos, olhando 0,2 segundo à frente. A seta tracejada é o anti-windup: a integral para de somar quando o comando bate no limite.

### Slide 13: Abertura de equilíbrio (0:55)
> A base do *feedforward* sai do modelo estático. No nó, com a pressão na referência, toda a vazão da fonte tem de sair pelos bicos e pela válvula. Dividindo por raiz de P ref e isolando alfa, sai a Equação 3.14. Ela é uma reta em n, com inclinação K sobre K v max: cada bico que fecha pede 0,121 a mais de abertura. Com sete bicos a válvula fica quase fechada, 0,023; com um bico, 0,752. E por que antecipar 0,2 segundo? Porque a válvula leva cerca de 0,24 segundo para andar esses 0,121. Quem comanda os bicos já sabe da troca antes, pelo mapa e pela posição da máquina. A 15 quilômetros por hora, 0,2 segundo são uns 80 centímetros.

### Slide 14: Linearização (1:10)
> Para usar a teoria de controle linear, o modelo foi linearizado no ponto nominal: sete bicos e pressão na referência. Cada vazão do nó vira a sua reta tangente, e os coeficientes são as derivadas parciais, como no Ogata. Por exemplo, a derivada da vazão dos bicos em relação a n é K raiz de P, 0,795. Somando as retas no nó, a variação da fonte é igual à soma das variações dos bicos e da válvula. Passando os termos em delta P para um lado, aparece o denominador D, 2,462. Ele junta dois efeitos que seguram a pressão quando ela sobe: as saídas deixam passar mais, e a fonte entrega menos. O resultado é delta P igual a menos 2,66 delta alfa menos 0,323 delta N. K g é o ganho da planta, K n o ganho do distúrbio. Um ponto importante: com quatro bicos, a parcela dos bicos cai e a da válvula sobe, mas a soma continua 0,817. Então D, K g e K n não dependem de n, e uma única sintonia serve para qualquer número de bicos.

### Slide 15: Domínio de Laplace (0:55)
> Com as retas, a malha vai para Laplace. A planta é estática pela hipótese de pressão instantânea, então a transformada só carrega os ganhos. A válvula sem o limite de velocidade é de primeira ordem: tau a alfa ponto mais alfa igual ao comando vira 1 sobre tau a s mais 1, um polo em menos 5. O PI é K c vezes 1 mais 1 sobre T i s. O *feedforward* é menos K n sobre K g vezes delta N, mais 0,121 por bico fechado, que é o compensador menos G2 sobre Gp do Castrucci. No diagrama, o número de bicos entra por dois caminhos: direto na pressão e pelo *feedforward*. A referência é fixa, então a única entrada é delta N. A saturação e o limite de velocidade ficam só no simulador.

### Slide 16: Malha fechada (1:25)
> Substituindo a válvula e o controlador na planta, delta P aparece dos dois lados. O produto dos blocos ao longo da volta, controlador vezes válvula vezes planta, é o ganho de malha L de s. Como K g é negativo, ele entra com sinal de menos: a realimentação é negativa. Passando para o lado esquerdo, fica delta P vezes 1 mais L igual ao efeito do bico. Então a resposta aos bicos é T n igual a K n sobre 1 mais L, que é a parte b da figura: o efeito de um bico fica dividido por 1 mais o ganho de malha. Tirando as frações, saem as três funções embaixo. Reparem no denominador do PI e do PI com *feedforward*: é o mesmo, então o *feedforward* não muda a estabilidade. E a antecipação usa um valor do futuro, então ela não cabe numa função de transferência comum: foi avaliada só no simulador.

### Slide 17: Alocação de polos (1:20)
> A sintonia é feita de trás para frente. Primeiro escolhi a resposta: amortecimento 0,7, perto do que acomoda mais depressa, e acomodação em 0,5 segundo. Pela fórmula do Ogata, t s igual a 4 sobre zeta omega n, a frequência natural fica 11,43. Depois, o denominador comum, dividido por tau a T i, é comparado termo a termo com a forma padrão s ao quadrado mais 2 zeta omega n s mais omega n ao quadrado. O termo em s dá K c igual a 0,827, e o termo independente dá T i igual a 0,084 segundo. A equação fica s ao quadrado mais 16 s mais 130,6, com polos em menos 8 mais ou menos j 8,2. Na figura, a região sombreada é onde a especificação é atendida: à esquerda de menos 8 e dentro do ângulo de 45,6 graus. Os polos ficam no canto. O polo do P está em menos 16 e o da válvula sozinha em menos 5. Os círculos são os zeros, que não mexem nos polos mas mudam a forma da curva. O P usa o mesmo K c, para a comparação mostrar só o efeito da integral.

*Se atrasado: corte a leitura da figura e diga só "os polos ficam exatamente no canto da região pedida".*

### Slide 18: Forma discreta e conferência (0:55)
> No programa, a integral vira uma soma de retângulos a cada milissegundo, e o comando é a Equação 3.21. Um exemplo com números: pressão em 3,6, erro de 0,1; a válvula recebe ordem de abrir de 2,3 para 10,7 por cento. Para conferir o projeto, a Figura 20 mostra um bico fechando no simulador completo. Sem o limite de velocidade, o PI acomoda em 0,44 segundo, dentro dos 0,5 pedidos, e fica a menos de 0,01 da função de transferência. Com o limite real, a conta embaixo mostra o problema: o controlador pede 1,34 por segundo, quase três vezes o que a válvula dá. Ela anda em rampa e a acomodação vai para 0,63. O modelo linear acerta os polos, mas quem define o tempo real é a válvula.

### Slide 19: Cenários e métricas ⏩ (0:20)
> Simulei três cenários: C1, um bico de cada vez; C2, degraus de três bicos, como no ensaio; e C3, trocas aleatórias rápidas. As métricas são o tempo fora da faixa de 10 por cento e o IAE, a área do erro.

### Slide 20: Resultados (0:35)
> Esta é a Tabela 9. Sem controle, a pressão fica de 69 a 91 por cento do tempo fora da faixa. O P reduz para 38 a 50, mas deixa erro permanente. O PI zera o erro. E o PI com *feedforward* antecipado é o melhor nos três cenários; no C3, cai quase pela metade, de 8,3 para 4,4 por cento.

### Slide 21: Cenário C1 (0:25)
> Os gráficos têm a pressão em cima, com a faixa em verde, a abertura no meio e o número de bicos embaixo. Cada troca dá um salto de 9,5 por cento, dentro da faixa. O P sai da faixa a partir do quarto bico fechado. O PI e o PI com *feedforward* ficam 100 por cento na faixa.

### Slide 22: Cenário C2 (0:35)
> O C2 repete o ensaio: três bicos fecham em 2 segundos e mais três em 8. O P para em 3,81 e 4,12, praticamente o que a conta d sobre 1 mais K c K g previa. O PI fica 6,8 por cento fora, e o *feedforward* antecipado 5,1. O pico não some: a pressão salta para 4,54 antes de a válvula se mover. Com a antecipação, o pico baixa para 4,36.

### Slide 23: Cenário C3 (0:25)
> O C3 imita a aplicação localizada: 66 trocas em 20 segundos. O PI fica 8,3 por cento fora, quando várias trocas no mesmo sentido chegam seguidas. O *feedforward* antecipado fica com 4,4. Sem antecipação, o mesmo *feedforward* ficava pior que o PI, 9,5.

### Slide 24: Feedforward antecipado (0:45)
> Este gráfico mostra por quê. Um bico fecha em meio segundo. Sem antecipar, o *feedforward* não ajuda: o PI, lendo em tempo real, já manda abrir no mesmo instante, e as duas correções somadas passam do ponto. É o s ao quadrado no numerador da Equação 3.28. Antecipando 0,2 segundo, a válvula começa a abrir antes; a pressão cai um pouco, para 3,44, ainda dentro da faixa, e o salto vai a 3,79 em vez de 3,83. O IAE dessa troca foi 0,064, contra 0,071 do PI. No C3, esse ganho se repete em cada troca.

### Slide 25: Velocidade da válvula (0:30)
> O que mais pesa ainda é a velocidade da válvula. O salto acontece com qualquer controlador, e a volta depende da rampa: para três bicos são 0,36 de abertura, cerca de 0,7 segundo. Com a válvula duas vezes mais rápida, o C3 cai para 0,4 por cento com o PI e 0,1 com o *feedforward* antecipado.

### Slide 26: Conclusões (0:50)
> Concluindo: um modelo com uma constante de bico e uma curva de fonte reproduziu a bancada. Como o ganho da planta não depende do número de bicos, uma única sintonia por alocação de polos serve para todos os casos. O PI zera o erro, e o *feedforward* antecipado em 0,2 segundo foi o melhor dos três. Mas três bicos fechando juntos ainda tiram a pressão da faixa por cerca de meio segundo. A hipótese foi confirmada em parte e só em simulação: os parâmetros da válvula foram estimados, e falta medir a pressão no tempo em bancada.

### Slide 27: Trabalhos futuros e agradecimento (0:30)
> Como próximos passos: medir a velocidade e a curva da válvula, medir a resposta da malha, testar uma válvula mais rápida com antecipação ajustada ao tamanho da troca, congelar a integral durante a antecipação e estender o anti-windup ao limite de velocidade. Agradeço a atenção e fico à disposição para as perguntas.

---

## Perguntas prováveis da banca (respostas curtas)

| Pergunta | Resposta em uma frase | Onde no TCC |
|---|---|---|
| Por que não validou com medições no tempo? | O artigo de referência só publica pontos em regime; a parte dinâmica é estudo de projeto, e medir em bancada é o primeiro trabalho futuro. | 3.8, Conclusão |
| De onde vêm τ_a e ω_max? | São estimativas, porque a bancada não informa a velocidade da válvula; por isso repeti os resultados com válvulas 2× e 4× mais rápidas. | 3.4.2, 4.6 |
| Por que linearizar, se a planta é não linear? | Para usar função de transferência e alocação de polos; a conferência na Figura 20 mostra que, para um bico, o simulador fica a menos de 0,01 da FT. | 2.6.1, 3.5.2, 4.2 |
| De onde vem o denominador 2,462? | Da soma das retas no nó: as saídas deixam passar mais (0,817 = C/2√P) e a fonte entrega menos (1,645). | 3.5.2 |
| Por que K_g e K_n não dependem de n? | Com P regulada, C é sempre 3,057; quando um bico fecha, a parcela dos bicos cai e a da válvula sobe na mesma quantidade, e a soma 0,817 não muda (vale se a válvula for linear, H5). | 3.5.2 |
| Por que o FF é −K_n/K_g? | Para anular o bico, K_g·ΔA = −K_n·ΔN, logo ΔA = −(K_n/K_g)·ΔN = +0,121 por bico fechado; é o F = −G₂/G_p do Castrucci com ganhos estáticos. | 3.5.4 |
| Por que o salto não é sobressinal? | Pelo teorema do valor inicial, ΔP(0⁺) = K_n·ΔN com qualquer controlador: a correção ainda não passou pela válvula. | 3.5.4, 4.2 |
| Com ζ = 0,7, o sobressinal não seria 4,6%? | Na forma padrão, sim; aqui a resposta aos bicos tem zeros (0 e −5), então a forma muda: a pressão passa 10% do salto abaixo da referência. | 2.6.2, 4.2 |
| Por que t_s = 0,5 s, se a válvula sozinha leva 0,8 s? | A realimentação deixa a malha mais rápida que a válvula livre (polo do P em −16 contra −5 da válvula); com o limite de velocidade, o tempo real foi medido no simulador: 0,63 s. | 3.5.5, 4.2 |
| A antecipação entra na função de transferência? | Não: ela usa n(t + T_ant), um valor do futuro, que uma FT comum não representa; por isso foi avaliada só no simulador. | 3.5.4, 4.6 |
| Por que o FF sem antecipação não ajudou? | Não há atraso puro para aproveitar (diferente do Ex. 7.4 do Castrucci), e o PI e o FF corrigem a mesma coisa ao mesmo tempo: a soma passa do ponto (s² no numerador da Eq. 3.28). | 4.6 |
| Por que 0,2 s de antecipação? | É perto do tempo que a válvula leva para compensar um bico (0,121/0,5 ≈ 0,24 s); para três bicos seria preciso cerca de 0,7 s, que ficou como trabalho futuro. | 3.5.1, 4.6 |
| Um controlador real não é amostrado? | É; aqui a leitura foi considerada a cada 1 ms. Pela regra de Castrucci (seção 12.6), basta amostrar ao menos 10 vezes mais rápido que a oscilação da malha. | 3.8 |
| Por que não usou a ação derivativa? | O salto de um bico (0,33 em 1 ms) daria um comando de cerca de 2,7 de abertura mesmo com T_d = 0,01 s; e a derivativa não acrescenta polo, os dois já estão no lugar. | 3.5.6 |
| Por que o anti-windup só no limite de posição? | É a técnica descrita por Fernandes e Goldemberg (2001); estendê-lo ao limite de velocidade baixou o C3 do PI de 8,3% para 3,2% num teste e ficou como trabalho futuro. | 3.5.3, 4.5 |
| Por que P_ref = 3,5 e não 4,0 kgf/cm²? | A válvula de alívio só baixa a pressão, e com sete bicos a fonte sustenta 3,56; 4,0 não seria atingível. | 4.1 |
| A hipótese de pressão instantânea vale? | Para a bancada, sim: com a mangueira modelada, a diferença foi de no máximo 0,4 ponto percentual; em barras longas precisa ser revista. | 3.4.1, 4.2 |

**Atenção:** os valores da mangueira (0,4 ponto) e do passo de integração foram calculados com o *feedforward* antigo, sem antecipação, e `testes_avulsos.py` ainda não foi rodado de novo. Se perguntarem, diga que esses testes foram feitos com o PI e que a conclusão não depende do *feedforward*.

## Dicas para o dia

- Ensaie com cronômetro duas vezes. Aos 5 minutos você deve estar no slide 10; aos 10 minutos, no slide 15 ou 16; aos 15 minutos, no slide 21.
- Nos slides 13 a 18, aponte cada equação enquanto fala e diga o número dela; a banca acompanha melhor.
- No slide 15, aponte no diagrama os dois caminhos do número de bicos: pelo bloco do distúrbio, direto na pressão, e pelo *feedforward*, no comando da válvula.
- Nos slides com gráfico, diga primeiro o que o eixo mostra e depois o resultado.
- Se uma pergunta for sobre algo que não foi feito, diga isso diretamente e cite a limitação ou o trabalho futuro correspondente.
