# Roteiro para explicar o TCC (versão 17)

Este roteiro serve para estudar e explicar o trabalho em detalhe, para o orientador, para a banca ou nas perguntas depois da apresentação. Ele segue a ordem do texto (`docs/17.pdf`). Para cada parte, mostra:
- o que foi feito;
- por que foi feito assim;
- a equação ou o número que importa;
- como explicar em palavras simples.

No fim há uma lista de perguntas prováveis da banca e uma cola com os números principais.

---

## 1. A história em um minuto

Na pulverização bico a bico, cada bico abre e fecha sozinho para aplicar produto só onde precisa. Como todos os bicos são alimentados pela mesma mangueira, cada vez que um bico fecha, sobra líquido para os outros e a pressão sobe. Com a pressão muda a vazão de cada bico, e com ela a dose e o tamanho das gotas.

O trabalho monta um modelo matemático simples da barra, ajustado aos dados da bancada de Rosa, Terra e Drews Jr (2019). Com esse modelo, testa em simulação três controladores que mexem numa válvula de alívio para segurar a pressão: P, PI e PI com *feedforward*. Os ganhos foram calculados por alocação de polos.

Resultado: o PI segura a pressão dentro de ±10% quando os bicos trocam um de cada vez. Nas trocas aleatórias, a pressão fica fora da faixa 11,5% do tempo. Quando vários bicos fecham juntos, a pressão escapa por cerca de 1 s, porque a válvula não é rápida o bastante. A hipótese foi **confirmada em parte, só em simulação**.

---

## 2. O mapa do trabalho (Quadro 1 e Figura 4)

O trabalho tem sete etapas, e cada uma entrega o que a seguinte usa:

| Etapa | O que faz | O que entrega |
|---|---|---|
| 1. Dados da bancada | Lê as Tabelas 1 e 2 de Rosa et al. (2019) | Pontos de pressão e vazão para 1 a 7 bicos |
| 2. Modelo estático | Lei de orifício nos bicos e na válvula, mais uma curva para a fonte | $P(n, \alpha)$ em regime, Eq. (3.11) |
| 3. Modelo dinâmico | Válvula com atraso e limite de velocidade; pressão instantânea | Simulador no tempo |
| 4. Ganho da planta e *feedforward* | Quanto a pressão muda por abertura, e a abertura de equilíbrio por $n$ | $K_g$ = −2,66 e $\alpha_{ff}(n)$ |
| 5. Controle | P, PI e PI+FF; função de transferência; alocação de polos | $K_c$ = 0,827 e $T_i$ = 0,084 s |
| 6. Simulação | Cenários C1, C2 e C3; métricas | Tabela 10 |
| 7. Programa | Python, só numpy e matplotlib, com conferências automáticas | Todos os números do Cap. 4 |

**Como explicar:** "Primeiro eu fiz um modelo que acerta a bancada parada. Depois dei tempo a ele. Depois projetei o controle em cima desse modelo e, por fim, testei tudo em simulação."

---

## 3. Parte por parte

### 3.1 O problema (Cap. 1)

- **O que dizer:** com a válvula de alívio fechada, indo de sete para um bico, a pressão sobe de 3,57 para 5,58 kgf/cm², cerca de 56% (Tabela 1).
- **Por que isso importa:** a vazão do bico varia com a raiz quadrada da pressão, $Q = K\sqrt{P}$ (Eq. 2.3). Se a pressão sobe 56%, a vazão de cada bico aberto sobe cerca de 25%, e a dose sai errada.
- **Por que controlar a pressão e não a vazão:** a pressão é a mesma para todos os bicos (H2). Segurando a pressão, segura-se a vazão de cada bico ao mesmo tempo.
- **Por que a válvula de alívio como atuador:** é o atuador da bancada de referência, e os autores mediram o efeito dela num ensaio (Tabela 2). Usar a rotação da bomba exigiria modelar o motor e o inversor, e não há dados publicados para conferir esse modelo.

### 3.2 A fundamentação (Cap. 2), só o que é usado depois

1. **Lei de orifício** (Eq. 2.3): $Q = K\sqrt{P}$. É a base de todo o modelo. Vale para os bicos e para a válvula.
2. **Resistência fluídica** (Eq. 2.4): a queda de pressão é proporcional ao quadrado da vazão, $\Delta P = R_F Q^2$. Bicos abertos ficam em paralelo.
3. **Norma ISO 16122-2, item 4.5.4:** tolerância de ±10% na pressão. É a faixa usada em todas as métricas.
4. **Ações P, I e D** (Eqs. 2.7 e 2.8):
   - a **P** corrige proporcionalmente ao erro de agora, mas deixa erro em regime, $e_{reg} = d/(1 + K_c|K_g|)$ (Eq. 2.9);
   - a **I** acumula o erro e só para quando ele zera;
   - a **D** ficou de fora por causa do ruído e dos saltos de pressão.
5. **Alocação de polos** (2.6.1): a forma padrão de segunda ordem (Eq. 2.10), com sobressinal $M_p$ e tempo de acomodação $t_s = 4/(\zeta\omega_n)$ (Eq. 2.11).
6. ***Feedforward* e anti-windup** (2.7):
   - o *feedforward* antecipa a correção pelo número de bicos, que o sistema já conhece;
   - o anti-windup para de integrar quando a válvula está no limite de posição (FERNANDES; GOLDEMBERG, 2001).

### 3.3 Modelo estático (3.2 e 3.3)

**A ideia em uma frase:** tudo o que a fonte manda precisa sair pelos bicos ou pela válvula.

$$Q_s(P) = \left[nK + K_v(\alpha)\right]\sqrt{P} \quad \text{(Eq. 3.10)}$$

As peças do modelo:
- **Bico:** $K$ = 0,425 (L/min)/√(kgf/cm²), média dos sete pontos da Tabela 1 (Eq. 3.2).
- **Barra:** com $n$ bicos em paralelo, a resistência equivalente é $R_1/n^2$ (Eq. 3.4). Isso substitui a fórmula empírica de quatro coeficientes de Rosa et al. (Eq. 2.5) por um único parâmetro físico.
- **Fonte (bomba + regulação interna):** uma parábola ajustada aos dados, com $a_2$ = −0,0355, $a_1$ = −0,2018 e $a_0$ = 5,815 (H4).
- **Válvula:** linear (H5), $K_v = K_{v,max}\,\alpha$, com $K_{v,max}$ = 3,5.

O modelo tem forma explícita: como tudo depende de $C = nK + K_{v,max}\alpha$, a Bhaskara dá a pressão direto (Eq. 3.11). O programa resolve por bissecção e confere com a fórmula; a diferença é menor que $10^{-14}$.

**Quanto ele acerta:** erro máximo de 0,73% na pressão e 2,27% na vazão. Na validação cruzada, tirando um ponto de cada vez do ajuste, o erro fica em 0,92% e 2,66%.

**Como explicar:** "Com só dois ingredientes, a constante do bico e a curva da bomba, o modelo reproduz os sete pontos medidos com menos de 1% de erro na pressão."

### 3.4 Hipóteses (H1 a H6)

Vale saber dizer cada uma e por que é aceitável:

| Hipótese | O que supõe | Por que é aceitável |
|---|---|---|
| H1 | Escoamento permanente, incompressível, barra horizontal | Padrão para líquido em mangueira curta (Brunetti) |
| H2 | Mesma pressão em todos os bicos | PT-01 e PT-02 quase iguais na bancada, com vazão pequena |
| H3 | Bicos iguais, lei de orifício | Mesmo modelo de ponta nos sete bicos |
| H4 | Fonte como curva de 2º grau | Ajuste bate com os dados |
| H5 | Válvula linear | A curva real não está nas fontes; é **estimativa** |
| H6 | Pressão instantânea | Conferido: com a mangueira no modelo, a diferença máxima foi de 0,4 p.p. |

### 3.5 Modelo dinâmico (3.4)

- **A pressão não tem dinâmica** (H6). Ela é recalculada a cada passo pela Eq. (3.10).
- **Só a válvula demora.** Ela segue o comando como primeira ordem, com velocidade limitada:

$$\frac{d\alpha}{dt} = \frac{\alpha_c - \alpha}{\tau_a}, \qquad \left|\frac{d\alpha}{dt}\right| \le \omega_{max} \quad \text{(Eq. 3.12)}$$

  Os valores são $\tau_a$ = 0,2 s e $\omega_{max}$ = 0,5 s⁻¹ (curso total em 2 s). **Os dois são estimados**, e isso precisa ser dito com clareza.
- **Integração:** Euler com $\Delta t$ = 1 ms (Eq. 3.13). Com 2 ms, os resultados mudam no máximo 0,2 p.p.
- **Controlador:** lê a pressão e atualiza o comando a cada $T_s$ = 50 ms, segurando o comando entre as leituras.

**Como explicar:** "A pressão responde na hora; quem demora é o motor da válvula. Por isso o modelo dinâmico é só a válvula."

### 3.6 Ganho da planta e *feedforward* (3.5.1 e 3.5.2)

- **$K_g$ = −2,66 kgf/cm² por unidade de abertura**, medido no modelo estático por diferença centrada (Eq. 3.15). É negativo porque abrir a válvula baixa a pressão.
- **O ganho não muda com o número de bicos.** Com a pressão em $P_{ref}$, $C$ tem sempre o mesmo valor (3,057), e abrir a válvula aumenta $C$ sempre na mesma proporção. Consequência: uma única sintonia serve para qualquer $n$. Esse é um resultado bonito para mostrar.
- **Feedforward** (Eq. 3.14): é a abertura que mantém $P_{ref}$ com $n$ bicos:

$$\alpha_{ff}(n) = \frac{1}{K_{v,max}}\left[\frac{Q_s(P_{ref})}{\sqrt{P_{ref}}} - nK\right]$$

  A válvula abre 0,121 a cada bico que fecha. Com sete bicos, a abertura é $\alpha_0$ = 0,023. É tão pequena porque $P_{ref}$ = 3,5 está logo abaixo do máximo de 3,56 que a fonte sustenta com sete bicos e a válvula fechada.

### 3.7 Os controladores (3.5.3)

- **Erro:** $e = P - P_{ref}$, ao contrário do usual, porque pressão alta pede **abrir** a válvula.
- **Comando** (Eq. 3.16):

$$\alpha_c = \alpha_{ff}(n) + K_c\left[e + \frac{1}{T_i}\int e\,dt\right]$$

- **As três configurações:**
  - **P:** sem a integral, com a base fixa $\alpha_0$;
  - **PI:** com a integral, base fixa $\alpha_0$;
  - **PI+FF:** a equação completa.
- **Forma discreta:** a integral vira soma de retângulos a cada 50 ms (Eqs. 3.17 e 3.18).
- **Anti-windup:** o integrador para quando o comando está em 0 ou 1 e o erro pede para ir além.

### 3.8 Função de transferência (3.5.4)

É a ponte entre o simulador e a teoria do Ogata. Linearizando em torno de sete bicos e $P = P_{ref}$, sem o limite de velocidade e sem amostragem:
- válvula: $1/(\tau_a s + 1)$ (Eq. 3.19);
- planta: $\Delta P = K_g\,\Delta A + K_n\,\Delta N$ (Eq. 3.20), com $K_n$ = −0,323 por bico;
- PI: $K_c(1 + 1/(T_i s))$ (Eq. 3.21).

O que ela mostra:
1. **O P deixa erro:** pelo teorema do valor final, um bico fechando deixa 0,101 kgf/cm² de erro.
2. **O PI zera o erro:** o $s$ no numerador da Eq. (3.24) zera o valor final.
3. **O *feedforward* não muda a estabilidade:** as Eqs. (3.24) e (3.25) têm o mesmo denominador.
4. **A equação característica do PI tem a forma de segunda ordem:**

$$s^2 + \frac{1 + K_c|K_g|}{\tau_a}\,s + \frac{K_c|K_g|}{\tau_a T_i} = 0$$

**Como explicar:** "A função de transferência explica, com conta, o que o simulador mostra. E é dela que saem os ganhos."

### 3.9 Sintonia por alocação de polos (3.5.5)

**A ideia:** primeiro se escolhe como a malha deve responder; depois se calculam os ganhos que dão essa resposta.

**Especificação:**
- **$\zeta$ = 0,7:** sobressinal de cerca de 4,6%, perto do amortecimento que acomoda mais rápido (Ogata, p. 157).
- **$t_s$ = 0,5 s:** um pouco mais rápido que a válvula livre, que leva $4\tau_a$ = 0,8 s.

**Conta** (comparando a equação característica com $s^2 + 2\zeta\omega_n s + \omega_n^2$):

$$\omega_n = \frac{4}{\zeta t_s} = 11{,}43 \text{ rad/s} \quad (3.26)$$

$$K_c = \frac{2\zeta\omega_n\tau_a - 1}{|K_g|} = 0{,}827 \quad (3.27)$$

$$T_i = \frac{K_c|K_g|}{\tau_a\omega_n^2} = 0{,}084\ \text{s} \quad (3.28)$$

O P usa o mesmo $K_c$, para que a comparação P × PI mostre só o efeito da integral.

**Limite da amostragem** (Eq. 3.29): a função de transferência contínua diz que qualquer ganho é estável, mas o controlador só olha a pressão a cada 50 ms.
- Entre duas leituras, o erro é multiplicado por $a - (1-a)K_c|K_g|$, com $a = e^{-T_s/\tau_a}$ = 0,779.
- Se esse número ficar abaixo de −1, o controlador corrige demais para um lado e depois para o outro, cada vez mais.
- Daí vem o limite $K_{c,lim} = (1+a)/((1-a)|K_g|)$ = 3,02. O ganho adotado é 27% dele.

**Como explicar o limite:** "É como dirigir abrindo os olhos só a cada meio segundo. O carro não é instável, mas quem dirige corrige tarde e corrige demais. Por isso existe um ganho máximo, e ele vem da amostragem, não da planta."

### 3.10 Cenários e métricas (3.6)

**Cenários:**
- **C1:** fecha um bico a cada 2 s, de 7 até 1, e reabre um a um (26 s).
- **C2:** a sequência do ensaio de Rosa: 7 → 4 bicos em 2 s e 4 → 1 em 8 s (14 s). São fechamentos triplos.
- **C3:** trocas aleatórias a cada 0,1 a 0,5 s, durante 20 s, com semente fixa.

**Métricas:**
- **tempo fora da faixa** de ±10% (Eq. 3.30), a principal;
- **IAE**, a área do erro (Eq. 3.32);
- **desvio máximo**;
- **acomodação** em ±2%.

### 3.11 Programa (3.7)

- `simulacao/modelo_barra.py`, inteiro no Apêndice A. Roda em cerca de 3 min.
- Usa só numpy e matplotlib, sem biblioteca de controle. Isso mostra que as contas foram feitas à mão.
- **Conferências automáticas:** o programa para se algo sair do esperado:
  - $K$ = 0,425 e erros do ajuste;
  - $K_g$ igual para todo $n$;
  - $K_c < K_{c,lim}$ e $T_i \ge T_s$;
  - $\zeta$ e $\omega_n$ da função de transferência iguais aos especificados.

---

## 4. Resultados (Cap. 4): como ler a Tabela 10

| Tempo fora da faixa | Malha aberta | P | PI | PI+FF |
|---|---|---|---|---|
| C1 | 69,2% | 38,5% | **0,0%** | **0,0%** |
| C2 | 85,7% | 46,6% | 7,5% | **6,8%** |
| C3 | 90,5% | 50,0% | **11,5%** | 12,4% |

Três mensagens, nesta ordem:

1. **O P não basta.** Ele deixa a pressão parada acima da referência, exatamente no valor da Eq. (2.9): 3,81 kgf/cm² com quatro bicos e 4,12 com um. A partir do quarto bico fechado, sai da faixa.
2. **O PI resolve o erro permanente.** Ele dá 0% fora da faixa no C1. O que sobra no C2 é o **salto instantâneo**: quando três bicos fecham, a pressão pula para 4,54 kgf/cm² (29,7%) no mesmo instante, porque a válvula ainda está na posição antiga. O controle define quanto tempo leva para voltar, cerca de 1 s.
3. **O gargalo é a velocidade da válvula.**
   - No C3, a válvula passa 75% do tempo na velocidade máxima.
   - O *feedforward* ajuda nas trocas espaçadas (C1 e C2), mas piora as rápidas (C3), porque manda a válvula para um alvo que muda antes de ela chegar.
   - Dobrar $\omega_{max}$ corta o tempo fora da faixa do PI quase pela metade no C2 e para cerca de um terço no C3.

**Conferências que dão confiança:**
- a função de transferência acerta o valor final do simulador (Figura 17);
- a hipótese H6, conferida com a mangueira no modelo, muda no máximo 0,4 p.p.;
- o passo de integração de 1 ms é suficiente;
- com ruído de 1% a 2% no sensor, a pressão continua na faixa, mas a válvula anda 2,1 a 2,5 vezes mais.

---

## 5. Conclusão e limitações (dizer com honestidade)

- **Confirmada em parte, só em simulação.** O PI atende a tolerância nas trocas de um bico e na maior parte da troca aleatória, mas não nas trocas simultâneas de vários bicos.
- **Limitações principais:**
  - $\tau_a$, $\omega_{max}$ e a curva da válvula foram **estimados**;
  - não há dado medido no tempo para validar a dinâmica;
  - o sensor foi considerado perfeito.
- **Trabalhos futuros:**
  - medir a válvula na bancada;
  - testar uma válvula mais rápida ou antecipar o comando da válvula ao das solenoides;
  - estender o anti-windup ao limite de velocidade, que no teste à parte levou o C3 de 11,5% para 4,8%;
  - validar com registros de campo.

---

## 6. Perguntas prováveis da banca

**1. Por que alocação de polos e não Ziegler-Nichols?**
A planta vista pelo controlador é de primeira ordem. As regras de Ziegler-Nichols pedem uma resposta ao degrau em forma de S, o primeiro método, ou uma oscilação sustentada com ganho proporcional, o segundo (Ogata, p. 523–524). A planta não tem nenhuma das duas. Como existe um modelo, é mais direto calcular os ganhos pela especificação.
*O texto não menciona Ziegler-Nichols. Esta resposta é só para o caso de a pergunta vir.*

**2. Por que ζ = 0,7 e $t_s$ = 0,5 s?**
- **ζ = 0,7:** sobressinal pequeno (4,6%) e acomodação quase mínima.
- **$t_s$ = 0,5 s:** um pouco mais rápido que a válvula sozinha (0,8 s), sem chegar perto do limite de 3,02.
- **Para ir mais rápido:** um $t_s$ menor aumentaria $K_c$, com mais desgaste do motor e mais sensibilidade a ruído.

**3. Se a função de transferência diz que qualquer ganho é estável, de onde vem o limite?**
Da amostragem. O controlador segura o comando por 50 ms sem ver a pressão. Com ganho alto, corrige demais entre duas leituras e o erro troca de sinal crescendo (Eq. 3.29).

**4. Por que o P usa o mesmo $K_c$ do PI?**
A malha do P tem um polo só, então não há ζ para escolher. Com o mesmo ganho, a diferença entre P e PI é só a ação integral.

**5. Por que não usar a ação derivativa?**
- A derivada amplifica o ruído do sensor.
- Os saltos de pressão nas trocas de bicos dariam picos no comando.
- Com o PI, a malha tem dois polos, e $K_c$ e $T_i$ já bastam para colocá-los onde se quer.

**6. Por que a pressão pode ser considerada instantânea?**
Porque foi conferido: com o armazenamento de líquido na mangueira incluído, o tempo fora da faixa mudou no máximo 0,4 p.p.

**7. De onde vêm $\tau_a$ e $\omega_{max}$?**
São estimados, e isso está dito no texto. São os parâmetros que mais pesam no resultado, e medi-los é o primeiro trabalho futuro.

**8. Por que $P_{ref}$ = 3,5 kgf/cm²?**
A válvula de alívio só baixa a pressão. Com sete bicos e a válvula fechada, a fonte chega a 3,56. A referência precisa ficar abaixo disso.

**9. Por que $\alpha_0$ = 0,023?**
É a abertura de equilíbrio com sete bicos em $P_{ref}$ (Eq. 3.14). É pequena porque 3,5 está muito perto do máximo de 3,56.

**10. Por que o ganho da planta não depende do número de bicos?**
A pressão depende de $n$ e $\alpha$ só através de $C = nK + K_{v,max}\alpha$. Em $P_{ref}$, $C$ é sempre 3,057, e abrir a válvula muda $C$ sempre na mesma proporção.

**11. Por que o *feedforward* piora o C3?**
A válvula não chega à posição calculada antes da próxima troca. O *feedforward* persegue alvos que mudam, enquanto o PI só corrige o erro que de fato aparece.

**12. Por que o pico do C2 não some com nenhum controlador?**
A pressão salta no mesmo instante em que os bicos fecham, antes de a válvula se mover. Para reduzir o pico, seria preciso mover a válvula **antes** das solenoides.

**13. Por que ±10% e não ±5%?**
É o valor da norma ISO 16122-2, item 4.5.4, para a pressão.

**14. Esse modelo vale para uma barra comercial?**
Não diretamente. A bancada tem vazão pequena e perda desprezível na barra (H2). Para barras longas, seria preciso incluir a perda ao longo da barra.

**15. O que garante que o programa está certo?**
- As conferências automáticas: o programa para se algo sair do esperado.
- A comparação da função de transferência com o simulador (Figura 17).
- A validação cruzada do modelo estático.

**16. Como isso seria implementado de verdade?**
Fora do escopo do trabalho. O controlador discreto a 50 ms, com a soma de retângulos e o anti-windup (Eqs. 3.17 e 3.18), é o que um microcontrolador executaria.

---

## 7. Cola: números para lembrar

| Grandeza | Valor |
|---|---|
| Constante do bico $K$ | 0,425 (L/min)/√(kgf/cm²) |
| Erro do modelo estático (ajuste / validação cruzada) | 0,73% e 2,27% / 0,92% e 2,66% |
| Pressão com válvula fechada, 7 → 1 bico | 3,57 → 5,58 kgf/cm² |
| $P_{ref}$; máximo com 7 bicos | 3,5; 3,56 kgf/cm² |
| $K_{v,max}$; $\alpha_0$; abertura por bico | 3,5; 0,023; 0,121 |
| $\tau_a$; $\omega_{max}$ (estimados) | 0,2 s; 0,5 s⁻¹ |
| $T_s$; $\Delta t$ | 50 ms; 1 ms |
| $K_g$; $K_n$ | −2,66 kgf/cm²; −0,323 por bico |
| ζ; $t_s$; $\omega_n$ | 0,7; 0,5 s; 11,43 rad/s |
| $K_c$; $T_i$ | 0,827; 0,084 s |
| Polos do PI | −8,0 ± j8,2 |
| $K_{c,lim}$ | 3,02 (o ganho usado é 27% dele) |
| Faixa | ±10% na pressão (ISO 16122-2, 4.5.4) |
| PI fora da faixa: C1 / C2 / C3 | 0% / 7,5% / 11,5% |
| Pico do fechamento triplo (C2) | 29,7%, volta em ~1 s |
| Válvula na velocidade máxima (C3) | 75% do tempo |
