# Roteiro da apresentação: 20 minutos

Este roteiro acompanha a apresentação `Apresentacao_Banca_TCC_v25.pptx` (28 slides), que corresponde à versão 25 do TCC (`docs/25.pdf`). As figuras, tabelas e equações dos slides têm a mesma numeração do trabalho. O roteiro anterior, de 15 minutos e da v20, está em `Roteiro_Apresentacao_15min_v20.md`.

## Como usar

Cada slide tem três partes:
- **Mostre:** o que apontar na tela enquanto fala.
- **Ideia:** a frase que a banca precisa guardar daquele slide. Se esquecer o resto, diga pelo menos ela.
- **Fala:** um texto de apoio, em frases curtas. Não é para decorar; diga com suas palavras.

**Tempo:**
- A fala prevista soma **19 min 25 s**, com 35 s de folga.
- O ritmo de referência é de cerca de 130 palavras por minuto.
- Se atrasar, encurte os slides marcados com ⏩ (cada um tem uma versão de uma frase).
- Não corte os slides 16 e 17 (malha fechada e polos): eles são o centro da parte de controle.

**A apresentação tem quatro blocos:**

| Bloco | Slides | Pergunta que o bloco responde |
|---|---|---|
| Contexto | 1 a 6 | Qual é o problema e o que o trabalho quer mostrar? |
| Modelo | 7 a 11 | Como a pressão depende dos bicos e da válvula? |
| Controle | 12 a 19 | Como o controlador foi projetado e conferido? |
| Resultados | 20 a 28 | Funcionou? Onde ainda falha? |

Ao mudar de bloco, diga uma frase de transição. Elas estão marcadas com ➜ nas falas.

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
| 19 | Simulação em Python | 0:45 | 14:30 |
| 20 | Cenários e métricas ⏩ | 0:20 | 14:50 |
| 21 | Resultados | 0:35 | 15:25 |
| 22 | Cenário C1 | 0:25 | 15:50 |
| 23 | Cenário C2 | 0:35 | 16:25 |
| 24 | Cenário C3 | 0:25 | 16:50 |
| 25 | Feedforward antecipado | 0:45 | 17:35 |
| 26 | Velocidade da válvula | 0:30 | 18:05 |
| 27 | Conclusões | 0:50 | 18:55 |
| 28 | Trabalhos futuros e agradecimento | 0:30 | 19:25 |

**Pontos de controle do relógio** (quando o slide aparece):

| Slide | Horário |
|---|---|
| 8 | 3:45 |
| 14 | 8:00 |
| 20 | 14:30 |
| 27 | 18:05 |

Se estiver mais de 30 s atrasado num deles, use os ⏩.

---

## Bloco 1: contexto

### Slide 1: Capa (0:15)
**Fala:**
> Boa tarde a todos. Agradeço a presença da banca e do meu orientador.

### Slide 2: Título (0:30)
**Ideia:** controlar a pressão de uma barra bico a bico com uma válvula de alívio, tudo em simulação.

**Fala:**
> Meu nome é Alex de Jesus Terolti. O meu trabalho é "Modelagem de sistema de controle para pulverização agrícola de precisão", com orientação do professor Rogério Bastos Quirino. Em uma frase: eu controlei, em simulação, a pressão de uma barra de pulverização bico a bico, usando uma válvula de alívio e controladores simples.

### Slide 3: Pulverização agrícola (0:45)
**Mostre:** a Figura 1 (o pulverizador) e depois a Figura 2 (seções e bico a bico).

**Ideia:** no bico a bico, cada troca de bico muda a vazão da barra, e é a pressão que define quanto sai de cada bico.

**Fala:**
> Primeiro, o contexto. O pulverizador de barras leva a calda do tanque até os bicos, passando pela bomba e pelas mangueiras. Os bicos quebram o líquido em gotas.
>
> Na aplicação convencional, a dose é a mesma na área toda. Mas as plantas daninhas e as pragas aparecem em manchas. Por isso existe a pulverização localizada, que aplica só onde precisa.
>
> Na Figura 2, em cima, o controle por seções desliga grupos de bicos. Embaixo, o controle bico a bico liga só os bicos que estão sobre as plantas. É o mais preciso.
>
> O detalhe é que, no bico a bico em série, uma única mangueira alimenta todos os bicos. Então, cada vez que um bico abre ou fecha, a vazão que a barra pede muda. E é a pressão que define quanto sai de cada bico e o tamanho da gota.

### Slide 4: Problema (0:40)
**Mostre:** a Figura 10, o primeiro par de manômetros (4,0 → 5,8) e depois o último (de volta a 4,0).

**Ideia:** fechar bicos faz a pressão subir muito, e abrir a válvula de alívio traz a pressão de volta.

**Fala:**
> Quando bicos fecham, sobra líquido na linha e a pressão sobe. Quando abrem, ela cai.
>
> Na bancada de Rosa, Terra e Drews Junior, indo de sete para um bico, a pressão sobe 56 por cento. A Figura 10 é um ensaio deles: fechando três bicos, a pressão vai de 4,0 para 5,8. Abrindo a válvula de alívio à mão, ela volta para 4,0.
>
> Como a vazão do bico depende da raiz da pressão, isso muda a dose. O problema deste trabalho é fazer essa correção de forma automática.

### Slide 5: Objetivo e hipótese (0:40)
**Mostre:** a hipótese em negrito e a linha da tolerância, no fim.

**Ideia:** um modelo simples deve bastar para projetar um controlador que segure a pressão em ±10%.

**Fala:**
> A hipótese é esta: um modelo de resistências fluídicas, mais a dinâmica da válvula, basta para projetar um controlador simples que segure a pressão em mais ou menos 10 por cento.
>
> Esses 10 por cento são a tolerância da norma de inspeção ISO 16122-2. Na vazão de cada bico, isso dá cerca de 5 por cento.
>
> Os objetivos foram: modelar a barra, acrescentar a dinâmica da válvula, sintonizar os controladores e comparar tudo em simulação.

### Slide 6: Etapas ⏩ (0:15)
**Mostre:** a Figura 4, de cima para baixo, rapidamente.

**Fala:**
> O trabalho seguiu sete etapas. Cada etapa usa o resultado da anterior, e a apresentação segue essa mesma ordem.

---

## Bloco 2: modelo

### Slide 7: Bancada de referência (0:40)
**Mostre:** a foto (Figura 5), depois a Tabela 1, da primeira linha (7 bicos) até a última (1 bico).

**Ideia:** os sete pontos da Tabela 1 são os dados reais usados para ajustar o modelo.

**Fala:**
> ➜ Agora, o modelo. Ele foi ajustado a uma bancada real.
>
> A bancada tem uma barra de cinco metros com sete bicos, uma bomba de pistão e uma válvula agulha com servomotor. Essa válvula é o atuador do controle.
>
> A Tabela 1 traz os dados medidos com a válvula de alívio fechada. Fechando bicos, a pressão sobe e a vazão cai. São esses sete pontos que usei para ajustar o modelo.

### Slide 8: Modelo estático (0:50)
**Mostre:** a Figura 11 (o nó no meio), as três equações da direita e, por último, a frase "a pressão só depende de C".

**Ideia:** a pressão depende só da capacidade de saída C, que soma bicos e válvula.

**Fala:**
> O modelo estático responde a uma pergunta: com n bicos abertos e a válvula numa certa abertura, qual é a pressão?
>
> Na Figura 11, três caminhos se encontram num nó. A fonte empurra o líquido; os bicos e a válvula deixam sair. Cada bico segue a lei de orifício: a vazão é K vezes raiz de P. A fonte é uma curva de segundo grau. E a válvula é linear na abertura.
>
> Em regime, o que entra no nó é igual ao que sai. Juntando bicos e válvula numa só grandeza, a capacidade de saída C, a pressão sai de forma explícita.
>
> Guardem esta ideia: a pressão só depende de C. Ela vai voltar no controle.

### Slide 9: Resistência R₁/n² ⏩ (0:35)
**Mostre:** as duas fórmulas da esquerda e o ponto n = 7 na Figura 17.

**Ideia:** um único parâmetro físico descreve a barra melhor que a fórmula empírica de quatro coeficientes.

**Fala:**
> Com bicos iguais em paralelo, a resistência da barra é a de um bico dividida por n ao quadrado. Rosa e colaboradores usaram uma fórmula empírica, com duas exponenciais e quatro coeficientes. O meu modelo usa um parâmetro só, com significado físico. O erro máximo foi 5,9 por cento, contra 18,5 da fórmula empírica.

*Versão curta: "A resistência da barra segue R₁ sobre n ao quadrado, com um parâmetro só e erro máximo de 5,9 por cento."*

### Slide 10: Validação ⏩ (0:25)
**Mostre:** os pontos laranja sobre a curva preta da Figura 18 e a linha verde do Pref.

**Ideia:** o modelo acerta os dados, e a referência tem de ficar abaixo de 3,56.

**Fala:**
> O modelo reproduziu os sete pontos medidos com erro de até 0,7 por cento na pressão e 2,3 na vazão. Ele também mostrou uma regra: a válvula de alívio só baixa a pressão. Então a referência tem de ficar abaixo do que a fonte sustenta com sete bicos, que é 3,56. Adotei 3,5.

*Versão curta: "O modelo errou menos de 1 por cento na pressão, e a referência adotada foi 3,5."*

### Slide 11: Modelo dinâmico (0:40)
**Mostre:** a equação de cima (pressão), depois a de baixo (válvula) e a foto da válvula (Figura 7).

**Ideia:** a pressão responde na hora; quem demora é a válvula.

**Fala:**
> A dinâmica tem duas partes.
>
> A primeira é a pressão. Ela só demora a mudar por causa do termo V sobre beta, que depende do volume da mangueira. Como a mangueira é curta e está cheia, considerei a pressão instantânea.
>
> A segunda é a válvula. Ela é de primeira ordem, com constante de tempo de 0,2 segundo, e o motor não passa de 0,5 por segundo. Esses dois valores são estimados, porque a bancada não informa.
>
> A simulação avança de milissegundo em milissegundo pelo método de Euler.

---

## Bloco 3: controle

### Slide 12: Estratégia de controle (0:50)
**Mostre:** na Figura 12, o caminho da malha (Pref → controlador → válvula → planta → sensor) e depois o bloco do *feedforward*, em cima. Por último, a Equação 3.19.

**Ideia:** os três controladores saem da mesma equação: base, mais proporcional, mais integral.

**Fala:**
> ➜ Com o modelo pronto, vem o controle.
>
> A variável controlada é a pressão. A manipulada é a abertura da válvula. E o número de bicos é a perturbação, porque o controlador não escolhe.
>
> O erro é a pressão menos a referência. É ao contrário do usual, porque pressão alta pede abrir a válvula.
>
> Os três controladores saem da Equação 3.19, que tem três parcelas: uma base, uma correção proporcional ao erro e uma correção proporcional ao erro acumulado. O P usa a base fixa e o proporcional. O PI acrescenta a integral. O PI com *feedforward* troca a base fixa por uma base que acompanha o número de bicos, 0,2 segundo antes da troca.
>
> A seta tracejada é o anti-windup: a integral para de somar quando o comando bate no limite.

### Slide 13: Abertura de equilíbrio (0:55)
**Mostre:** as três equações da esquerda, de cima para baixo; depois os valores de αff à direita.

**Ideia:** cada bico que fecha pede 0,121 a mais de abertura na válvula.

**Fala:**
> A base do *feedforward* sai do próprio modelo estático.
>
> Com a pressão na referência, toda a vazão da fonte tem de sair pelos bicos e pela válvula. Essa é a primeira equação. Isolando a abertura, sai a Equação 3.14.
>
> Ela é uma reta. Cada bico que fecha pede 0,121 a mais de abertura, ou seja, 0,121 de abertura deixa passar o mesmo que um bico. Com sete bicos, a válvula fica quase fechada; com um bico, fica três quartos aberta.
>
> E por que antecipar 0,2 segundo? Porque a válvula leva uns 0,24 segundo para andar esses 0,121. Quem comanda os bicos já sabe da troca antes, pelo mapa e pela posição da máquina.

### Slide 14: Linearização (1:10)
**Mostre:** primeiro a Figura 12 pequena, no bloco "Planta hidráulica". Depois a Tabela 3, linha por linha. Depois a soma no nó e, por fim, Kg e Kn.

**Ideia:** linearizando o nó, a planta vira só dois números: Kg = −2,66 e Kn = −0,323.

**Fala:**
> Para usar a teoria de controle linear, preciso trocar o bloco da planta hidráulica, este aqui na Figura 12, por algo linear.
>
> A linearização foi feita no ponto nominal: sete bicos e pressão na referência. Na Tabela 3, cada vazão do nó vira a sua reta tangente. Os números são as derivadas parciais naquele ponto.
>
> Somando as retas no nó e isolando delta P, sai esta equação: delta P é menos 2,66 vezes delta alfa, menos 0,323 vezes delta N.
>
> O primeiro número é o ganho da planta, Kg: quanto a pressão cai quando a válvula abre. O segundo é o ganho do distúrbio, Kn: quanto a pressão cai quando um bico abre.
>
> E um resultado importante: com quatro bicos, ou com qualquer número, a soma no denominador continua a mesma. Então Kg e Kn não dependem de n, e uma única sintonia serve para todos os casos.

### Slide 15: Domínio de Laplace (0:55)
**Mostre:** na Figura 13, os dois caminhos de ΔN (para o bloco Distúrbio e para o *feedforward*). Depois as quatro equações da direita.

**Ideia:** cada bloco da malha virou uma função de transferência simples.

**Fala:**
> Com a planta linear, cada bloco vira uma função de transferência.
>
> A planta só tem ganhos, porque a pressão é instantânea. A válvula vira 1 sobre tau a s mais 1. O PI é Kc vezes 1 mais 1 sobre Ti s. E o *feedforward* é menos Kn sobre Kg vezes delta N, ou seja, 0,121 por bico fechado.
>
> Na Figura 13, o número de bicos entra por dois caminhos: direto na pressão, pelo bloco do distúrbio, e no comando da válvula, pelo *feedforward*.
>
> A referência é fixa, então a única entrada é o número de bicos. A saturação e o limite de velocidade não são lineares, e por isso ficam só no simulador.

### Slide 16: Malha fechada (1:25)
**Mostre:** a Figura 14(a) e o bloco L(s); depois a Figura 14(b); depois as equações da direita; por fim, os denominadores das três funções embaixo.

**Ideia:** o efeito de um bico na pressão fica dividido por 1 + L(s).

**Fala:**
> Agora fecho a malha.
>
> Substituindo a válvula e o controlador na planta, delta P aparece dos dois lados da equação. O produto dos blocos ao longo da volta, controlador vezes válvula vezes planta, é o ganho de malha, L de s. Na Figura 14(a), ele está num bloco só.
>
> Passando tudo para o mesmo lado, a resposta aos bicos fica Tn igual a Kn sobre 1 mais L. Na Figura 14(b), a malha inteira vira esse bloco. Em palavras: o efeito de um bico na pressão fica dividido por 1 mais o ganho de malha. Quanto maior o ganho, menor o efeito que sobra.
>
> Tirando as frações, saem as três funções embaixo: P, PI e PI com *feedforward*. Reparem que o PI e o PI com *feedforward* têm o mesmo denominador. Então o *feedforward* não muda a estabilidade.
>
> A antecipação usa um valor do futuro, o número de bicos daqui a 0,2 segundo. Isso não cabe numa função de transferência comum, então ela foi avaliada só no simulador.

### Slide 17: Alocação de polos (1:20)
**Mostre:** as equações de cima para baixo, na ordem 1-2-3; no fim, os dois polos laranja no canto da região sombreada da Figura 19.

**Ideia:** escolhi como a malha deve responder e calculei Kc e Ti para isso: 0,827 e 0,084 s.

**Fala:**
> A sintonia foi feita de trás para frente: primeiro escolhi a resposta, depois calculei o controlador.
>
> Pedi amortecimento 0,7 e acomodação em meio segundo. Pela fórmula do Ogata, isso dá uma frequência natural de 11,43.
>
> Depois, comparei o denominador da malha, termo a termo, com a forma padrão de segunda ordem. O termo em s dá Kc igual a 0,827. O termo independente dá Ti igual a 0,084 segundo. Com esses valores, os polos ficam em menos 8 mais ou menos j 8,2.
>
> Na Figura 19, a região sombreada é onde a especificação é atendida. Os polos do PI ficam exatamente no canto dela.
>
> O P usa o mesmo Kc. Assim, a comparação entre P e PI mostra só o efeito da integral.

*Versão curta da figura: "os polos ficam exatamente no canto da região pedida".*

### Slide 18: Forma discreta e conferência (0:55)
**Mostre:** as duas equações de cima, o exemplo numérico, depois a Figura 20 (curvas sem limite, depois com limite) e a conta 1,34 s⁻¹ embaixo.

**Ideia:** o modelo linear acerta os polos, mas quem define o tempo real é a velocidade da válvula.

**Fala:**
> No programa, a integral vira uma soma a cada milissegundo. Um exemplo: com a pressão em 3,6, o erro é 0,1, e a válvula recebe ordem de abrir de 2,3 para 10,7 por cento.
>
> Para conferir o projeto, a Figura 20 mostra um bico fechando no simulador completo. Sem o limite de velocidade da válvula, o PI acomoda em 0,44 segundo, dentro do que pedi, e a curva fica em cima da função de transferência.
>
> Com o limite real, a acomodação vai para 0,63 segundo. A conta embaixo explica: o controlador pede 1,34 por segundo, e a válvula só anda 0,5.

### Slide 19: Simulação em Python (0:45)
**Mostre:** a Figura 16 de cima para baixo, seguindo os passos 1 a 5 da lista.

**Ideia:** a simulação é um laço de cinco passos, repetido a cada milissegundo.

**Fala:**
> Tudo isso foi programado num único arquivo em Python, só com numpy e matplotlib. Não usei biblioteca de controle, para cada passo ficar visível no código.
>
> A simulação é este laço, repetido a cada milissegundo. Um: se chegou a hora, troca o número de bicos. Dois: o controlador calcula o comando. Três: a válvula se move, pelo método de Euler, respeitando os limites. Quatro: a pressão nova é calculada pela bissecção. Cinco: os valores são guardados.
>
> No fim, as séries no tempo dão as métricas e os gráficos. O código completo está no Apêndice A.

---

## Bloco 4: resultados

### Slide 20: Cenários e métricas ⏩ (0:20)
**Fala:**
> ➜ Agora, os resultados. Simulei três cenários: C1, um bico de cada vez; C2, degraus de três bicos, como no ensaio; e C3, trocas aleatórias rápidas. A métrica principal é o tempo com a pressão fora da faixa de 10 por cento.

### Slide 21: Resultados (0:35)
**Mostre:** na Tabela 9, as linhas de malha aberta, depois P, PI e PI+FF de cada cenário.

**Ideia:** o PI zera o erro, e o PI com *feedforward* antecipado é o melhor nos três cenários.

**Fala:**
> Na Tabela 9, sem controle, a pressão fica de 69 a 91 por cento do tempo fora da faixa. O P reduz para 38 a 50 por cento, mas deixa erro permanente. O PI zera o erro. E o PI com *feedforward* antecipado é o melhor nos três cenários: no C3, o tempo fora cai quase pela metade, de 8,3 para 4,4 por cento.

### Slide 22: Cenário C1 (0:25)
**Mostre:** primeiro explique os três gráficos da Figura 21 (pressão, abertura, bicos); depois a curva verde (P) saindo da faixa.

**Fala:**
> Os gráficos dos cenários têm a pressão em cima, com a faixa em verde; a abertura da válvula no meio; e o número de bicos embaixo. No C1, cada troca dá um salto de 9,5 por cento, ainda dentro da faixa. O P sai da faixa a partir do quarto bico fechado. O PI e o PI com *feedforward* ficam o tempo todo na faixa.

### Slide 23: Cenário C2 (0:35)
**Mostre:** na Figura 22, a curva verde parada acima de 3,5; depois os picos em t = 2 s e t = 8 s.

**Fala:**
> O C2 repete o ensaio da bancada: três bicos fecham em 2 segundos e mais três em 8. O P para em 3,81 e 4,12, praticamente o valor que a conta previa. O PI fica 6,8 por cento do tempo fora, e o *feedforward* antecipado, 5,1. O pico não some, porque a pressão salta antes de a válvula andar. Com a antecipação, ele baixa de 4,54 para 4,36.

### Slide 24: Cenário C3 (0:25)
**Mostre:** na Figura 23, um trecho em que várias trocas no mesmo sentido vêm seguidas.

**Fala:**
> O C3 imita a aplicação localizada: 66 trocas em 20 segundos. O PI fica 8,3 por cento fora da faixa, principalmente quando várias trocas no mesmo sentido chegam seguidas. O *feedforward* antecipado fica com 4,4. Sem antecipação, o mesmo *feedforward* era pior que o PI: 9,5.

### Slide 25: Feedforward antecipado (0:45)
**Mostre:** na Figura 24, a linha "o bico fecha" em 0,5 s; a curva azul começando a se mexer antes, em 0,3 s; e a tracejada passando do ponto.

**Ideia:** antecipar 0,2 s faz a válvula começar a andar antes da troca, e isso reduz o erro.

**Fala:**
> A Figura 24 mostra por que a antecipação faz diferença. Um bico fecha em meio segundo.
>
> Sem antecipar, na linha tracejada, o *feedforward* não ajuda. O PI já manda abrir no mesmo instante, e as duas correções somadas passam do ponto.
>
> Antecipando 0,2 segundo, na curva azul, a válvula começa a abrir antes. A pressão cai um pouco, para 3,44, ainda dentro da faixa. Quando o bico fecha, o salto é menor. O erro dessa troca foi 0,064, contra 0,071 do PI. No C3, esse ganho se repete em cada troca.

### Slide 26: Velocidade da válvula (0:30)
**Mostre:** a primeira linha da tabela (válvula estimada) e depois a segunda (2× mais rápida).

**Ideia:** o que mais limita o resultado é a velocidade da válvula.

**Fala:**
> O que mais pesa no resultado é a velocidade da válvula. Para três bicos, ela precisa andar 0,36, o que leva cerca de 0,7 segundo. Com uma válvula duas vezes mais rápida, o C3 cai para 0,4 por cento com o PI e 0,1 com o *feedforward* antecipado.

### Slide 27: Conclusões (0:50)
**Ideia:** hipótese confirmada em parte e só em simulação.

**Fala:**
> Para concluir.
>
> Um modelo com uma constante de bico e uma curva de fonte reproduziu a bancada.
>
> Como o ganho da planta não depende do número de bicos, uma única sintonia por alocação de polos serve para todos os casos.
>
> O PI zera o erro, e o *feedforward* antecipado em 0,2 segundo foi o melhor dos três.
>
> Mas, quando três bicos fecham juntos, a pressão ainda sai da faixa por cerca de meio segundo, porque a válvula é lenta.
>
> Por isso, a hipótese foi confirmada em parte e só em simulação. Os parâmetros da válvula foram estimados, e falta medir a pressão no tempo, na bancada.

### Slide 28: Trabalhos futuros e agradecimento (0:30)
**Fala:**
> Como próximos passos, o mais importante é medir a velocidade e a curva da válvula na bancada. Depois: medir a resposta da malha, testar uma válvula mais rápida com antecipação ajustada ao tamanho da troca e estender o anti-windup ao limite de velocidade.
>
> Agradeço a atenção e fico à disposição para as perguntas.

---

## Perguntas prováveis da banca (respostas curtas)

| Pergunta | Resposta em uma frase | Onde no TCC |
|---|---|---|
| Por que não validou com medições no tempo? | O artigo de referência só publica pontos em regime; a parte dinâmica é estudo de projeto, e medir em bancada é o primeiro trabalho futuro. | 3.8, Conclusão |
| De onde vêm τ_a e ω_max? | São estimativas, porque a bancada não informa a velocidade da válvula; por isso repeti os resultados com válvulas 2× e 4× mais rápidas. | 3.4.2, 4.6 |
| Por que linearizar, se a planta é não linear? | Para usar função de transferência e alocação de polos; na Figura 20, para um bico, o simulador fica a menos de 0,01 da FT. | 2.6.1, 3.5.2, 4.2 |
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

- Ensaie com cronômetro duas vezes. Aos 5 minutos você deve estar no slide 9; aos 10 minutos, no slide 15; aos 15 minutos, no slide 21.
- Nos slides de equação (13 a 18), aponte cada equação enquanto fala e diga o número dela.
- Nos slides com gráfico, diga primeiro o que cada eixo mostra e depois o resultado.
- Quando não lembrar a fala, diga a **Ideia** do slide e passe para o próximo.
- Se uma pergunta for sobre algo que não foi feito, diga isso diretamente e cite a limitação ou o trabalho futuro correspondente.
