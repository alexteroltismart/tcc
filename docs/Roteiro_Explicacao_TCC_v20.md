# Guia de estudos do TCC (versão 20)

Este guia serve para estudar o trabalho e explicá-lo ao orientador ou à banca, inclusive nas perguntas depois da apresentação. Ele segue a ordem do texto (`docs/20.pdf`, 95 p.). Cada parte traz:
- o que foi feito e por quê;
- a equação ou o número que importa;
- **onde ler nos livros**, com a página do Ogata e a seção do Castrucci;
- uma frase pronta para explicar.

No fim há perguntas prováveis da banca e uma cola com os números.

**Livros citados neste guia:**

| Sigla | Livro | Como citar |
|---|---|---|
| **Ogata** | OGATA, K. *Engenharia de controle moderno*. 5. ed. Pearson, 2010 | por página |
| **Castrucci** | CASTRUCCI, P. L.; BITTAR, A.; SALES, R. M. *Controle automático*. 2. ed. LTC, 2018 | por **seção** (o *e-book* não tem página) |
| **Brunetti** | BRUNETTI, F. *Mecânica dos fluidos*. 2. ed. Pearson, 2008 | por página |
| **Chapra** | CHAPRA, S. C.; CANALE, R. P. *Métodos numéricos para engenharia*. 5. ed. AMGH, 2011 | por página |
| **Merritt** | MERRITT, H. E. *Hydraulic control systems*. Wiley, 1967 | por página |

As citações do Castrucci vão por seção porque o *e-book* não tem páginas. O autor vai revisar uma a uma no acesso *online*.

---

## 1. A história em um minuto

Na pulverização bico a bico, cada bico abre e fecha sozinho. Como todos são alimentados pela mesma mangueira, cada vez que um bico fecha sobra líquido para os outros, e a pressão sobe. Com a pressão mudam a vazão de cada bico, a dose e o tamanho das gotas.

O trabalho monta um modelo simples da barra, ajustado aos dados da bancada de Rosa, Terra e Drews Jr (2019). Com esse modelo, testa em simulação três controladores que mexem numa válvula de alívio para segurar a pressão: P, PI e PI com *feedforward*. Os ganhos foram calculados por alocação de polos.

**Resultado:**
- o PI mantém a pressão dentro de ±10% quando os bicos trocam um de cada vez;
- nas trocas aleatórias, a pressão fica fora da faixa 8,3% do tempo;
- quando três bicos fecham juntos, a pressão escapa por cerca de 1 s, porque a válvula não é rápida o bastante;
- o *feedforward* não trouxe ganho.

A hipótese foi **confirmada em parte, só em simulação**.

---

## 2. O mapa do trabalho (Quadro 1 e Figura 4)

| Etapa | O que faz | O que entrega |
|---|---|---|
| 1. Dados da bancada | Lê as Tabelas 1 e 2 de Rosa et al. (2019) | Pressão e vazão para 1 a 7 bicos |
| 2. Modelo estático | Lei de orifício nos bicos e na válvula, mais uma curva para a fonte | $P(n, \alpha)$ em regime, Eq. (3.11) |
| 3. Modelo dinâmico | Válvula com atraso e limite de velocidade; pressão instantânea | Simulador no tempo |
| 4. Abertura de equilíbrio e ganhos | Inversão do modelo e derivada implícita | $\alpha_{ff}(n)$, $K_g$ = −2,66 e $K_n$ = −0,323 |
| 5. Controle | P, PI e PI+FF; função de transferência; alocação de polos | $K_c$ = 0,827 e $T_i$ = 0,084 s |
| 6. Simulação | Cenários C1, C2 e C3; métricas | Tabela 9 |
| 7. Programa | Python, só numpy e matplotlib, com conferências automáticas | Todos os números do Cap. 4 |

**Como explicar:** "Primeiro fiz um modelo que acerta a bancada parada. Depois dei tempo a ele. Em cima desse modelo projetei o controle e, por fim, testei tudo em simulação."

---

## 3. Parte por parte

### 3.1 O problema (Cap. 1)

- **O que dizer:** com a válvula de alívio fechada, indo de sete para um bico, a pressão sobe de 3,57 para 5,58 kgf/cm², cerca de 56% (Tabela 1).
- **Por que isso importa:** a vazão do bico varia com a raiz da pressão, $Q = K\sqrt{P}$. Se a pressão sobe 56%, a vazão de cada bico aberto sobe cerca de 25%, e a dose sai errada.
- **Por que controlar a pressão:** a pressão é a mesma para todos os bicos (H2). Segurando a pressão, segura-se a vazão de todos ao mesmo tempo.
- **Por que a válvula de alívio:** é o atuador da bancada, e os autores mediram o efeito dela (Tabela 2). Usar a rotação da bomba exigiria modelar o motor e o inversor, sem dados para conferir.

### 3.2 Fundamentação (Cap. 2), só o que é usado depois

1. **Lei de orifício** (Eq. 2.3): $Q = K\sqrt{\Delta P}$. Sai de Bernoulli mais continuidade, com o coeficiente de descarga.
   - **Ler:** Brunetti p. 212–213 (veia contraída, orifício); Merritt p. 40–41.
2. **Resistência fluídica** (Eq. 2.4), $\Delta P = R_F Q^2$. Em paralelo, $n$ peças iguais dão $R/n^2$ (Eq. 2.6).
3. **ISO 16122-2, item 4.5.4:** ±10% na pressão, o que dá cerca de ±5% na vazão.
4. **Ações P, I e D** (Eqs. 2.7 e 2.8). O P deixa erro em regime, $e_{reg} = d/(1 + K_c|K_g|)$ (Eq. 2.9); o I zera esse erro; o D ficou de fora por causa do ruído e dos saltos de pressão.
   - **Ler:** Ogata p. 21 (PID); Castrucci seção 6.2 (PID na forma $K_c$, $T_I$, $T_D$, padrão ISA); Ogata p. 159 e p. 541 (derivada e ruído, derivada de degrau).
   - **Para a Eq. 2.9:** Castrucci seção 3.11.3 e Tabela 3.4. Sem integrador na malha, o erro a uma perturbação em degrau é $-AK_p/(1 + K)$; com um integrador, é zero.
5. **Referência e perturbação:** a malha recebe as duas, mas aqui a referência é fixa, e a análise trata só a perturbação, que é o número de bicos.
   - **Ler:** Castrucci seção 3.10 (sistema realimentado com referência e perturbação) e 3.11.3 (perturbação em degrau, referência nula).
6. **Alocação de polos** (2.6.1): forma padrão de 2ª ordem (Eq. 2.10), sobressinal $M_p$ e $t_s = 4/(\zeta\omega_n)$ (Eq. 2.11).
   - **Ler:** Ogata p. 151 (forma padrão), p. 156 ($M_p$), p. 157 ($t_s$ e o mínimo perto de $\zeta$ = 0,76), p. 522 e 658 (projeto pelo modelo, alocação); Castrucci seções 3.5–3.6 (2ª ordem, $M_p$ e $t_s$) e 8.2 (imposição de polos).
7. ***Feedforward*** (2.7.1): o comando que anula o distúrbio é a razão entre o efeito do distúrbio e o efeito do comando. Ele é somado à realimentação, que corrige o resto.
   - **Ler:** Castrucci seção 7.8: "o cancelamento não precisa ser perfeito, pois a malha de realimentação é que dá qualidades de precisão". Castrucci seção 7.8.1, Eq. 7.51: $F(s) = -G_2(s)/G_p(s)$. Liu et al. (2018).
8. **Anti-windup** (2.7.2): durante a saturação, o integrador acumula erro demais. A integração condicional para de integrar quando a válvula está no limite (Eq. 2.13).
   - **Ler:** Castrucci seção 6.3.4 (o que é o *windup*); Fernandes e Goldemberg (2001), p. 5 (integração condicional).

### 3.3 Modelo estático (3.2 e 3.3)

**A ideia em uma frase:** tudo o que a fonte manda precisa sair pelos bicos ou pela válvula (continuidade, Brunetti p. 75).

$$Q_s(P) = \left[nK + K_v(\alpha)\right]\sqrt{P} \quad \text{(Eq. 3.10)}$$

As peças do modelo:
- **Bico:** $K$ = 0,425 (L/min)/√(kgf/cm²), média dos sete pontos (Eq. 3.2).
- **Barra:** com $n$ bicos, a resistência equivalente é $R_1/n^2$ (Eq. 3.4). Isso troca a fórmula de quatro coeficientes de Rosa et al. (Eq. 2.5) por um único parâmetro físico.
- **Fonte:** a bomba mais a PCV, descritas por uma parábola ajustada por mínimos quadrados (Chapra p. 393): $a_2$ = −0,0355, $a_1$ = −0,2018, $a_0$ = 5,815. A PCV desvia a vazão que sobra (Merritt p. 321 e 337).
- **Válvula:** linear (H5), $K_v = K_{v,max}\,\alpha$, com $K_{v,max}$ = 3,5.
- **Forma explícita** (Eq. 3.11): tudo depende de $C = nK + K_{v,max}\alpha$, e a Bhaskara dá a pressão. O programa usa bissecção (Chapra p. 101–102), e a diferença entre os dois é menor que $10^{-14}$.

**Quanto ele acerta:** erro máximo de 0,7% na pressão e 2,3% na vazão (Tabela 6). Na validação cruzada, 0,9% e 2,7% (Tabela 7).

**Como explicar:** "Com dois ingredientes, a constante do bico e a curva da bomba, o modelo reproduz os sete pontos medidos com menos de 1% de erro na pressão."

### 3.4 Hipóteses (H1 a H6)

| Hipótese | O que supõe | Por que é aceitável |
|---|---|---|
| H1 | Escoamento permanente, incompressível, barra horizontal | Padrão para líquido (Brunetti p. 10 e 67) |
| H2 | Mesma pressão em todos os bicos | PT-01 ≈ PT-02 na bancada; só as restrições intencionais contam (Merritt p. 52) |
| H3 | Bicos iguais, lei de orifício | Mesmo modelo de ponta nos sete |
| H4 | Fonte como curva de 2º grau | Uma reta teria erro 12 vezes maior |
| H5 | Válvula linear | **Estimativa**: a curva real não está nas fontes |
| H6 | Pressão instantânea | Conferida: com a mangueira no modelo, diferença de 0,4 p.p. |

### 3.5 Modelo dinâmico (3.4)

- **A pressão não tem dinâmica** (H6). Ela é recalculada a cada passo pela Eq. (3.10). A capacitância da mangueira, $(V/\beta)\,dP/dt$ (Merritt p. 53), é pequena.
- **Só a válvula demora.** Ela é de primeira ordem, com velocidade limitada (Eq. 3.12): $\tau_a$ = 0,2 s e $\omega_{max}$ = 0,5 s⁻¹ (curso total em 2 s). **Os dois são estimados.**
  - **Ler:** Ogata p. 147 e Castrucci seção 3.4 (sistema de 1ª ordem: 63,2% em uma constante de tempo, 2% em quatro). Castrucci seção 9.10.2 (saturação) e Merritt p. 277 (limites como não linearidade).
- **Integração:** Euler a cada $\Delta t$ = 1 ms (Eq. 3.13; Chapra p. 588 e 592).
- **Controlador:** lê a pressão em tempo real, a cada passo de 1 ms, sem amostragem.

**Como explicar:** "A pressão responde na hora; quem demora é o motor da válvula. Por isso o modelo dinâmico é só a válvula."

### 3.6 Abertura de equilíbrio e *feedforward* (3.5.1)

A abertura que mantém $P_{ref}$ com $n$ bicos sai de isolar $\alpha$ na Eq. (3.10):

$$\alpha_{ff}(n) = \frac{1}{K_{v,max}}\left[\frac{Q_s(P_{ref})}{\sqrt{P_{ref}}} - nK\right] \quad \text{(Eq. 3.14)}$$

- Com sete bicos, $\alpha_0$ = 0,023; com um bico, 0,752.
- Cada bico que fecha pede 0,121 a mais de abertura.
- $\alpha_0$ é tão pequeno porque $P_{ref}$ = 3,5 está logo abaixo dos 3,56 que a fonte sustenta com sete bicos.

### 3.7 Ganho da planta e ganho do distúrbio (3.5.2), **mudou na v20**

A pressão depende de $n$ e $\alpha$ só através de $C$. Por isso basta a derivada $dP/dC$, tirada do equilíbrio do nó $F(P, C) = Q_s(P) - C\sqrt{P} = 0$ por **derivada implícita** (regra da cadeia):

$$\frac{dP}{dC} = \frac{-\sqrt{P}}{\dfrac{C}{2\sqrt{P}} - \dfrac{dQ_s}{dP}} = \frac{-1{,}871}{0{,}817 + 1{,}645} = -0{,}760 \quad \text{(Eq. 3.15)}$$

$$K_g = K_{v,max}\,\frac{dP}{dC} = -2{,}66 \qquad K_n = K\,\frac{dP}{dC} = -0{,}323 \quad \text{(Eqs. 3.16 e 3.17)}$$

- **Leitura física do denominador:** quando a pressão sobe, as saídas deixam passar mais (0,817) e a fonte entrega menos (1,645). Os dois termos ajudam o nó a voltar ao equilíbrio.
- **Por que não depende de $n$:** com a pressão em $P_{ref}$, $C$ vale sempre 3,057, então $dP/dC$ não muda. Uma única sintonia serve para qualquer $n$. A razão $K_n/K_g = K/K_{v,max}$ = 0,121 é a mesma do *feedforward*.
- **Conferência:** o programa calcula também por diferença centrada (Chapra p. 75), e a diferença é menor que 0,1%.

### 3.8 Os controladores (3.5.3)

- **Erro:** $e = P - P_{ref}$, ao contrário do usual, porque pressão alta pede **abrir** a válvula.
- **Comando** (Eq. 3.18): $\alpha_c = \alpha_{ff}(n) + K_c[e + \frac{1}{T_i}\int e\,dt]$.
- **As três configurações:**
  - **P:** sem a integral, base fixa $\alpha_0$;
  - **PI:** com a integral, base fixa $\alpha_0$;
  - **PI+FF:** a equação completa.
- **Forma discreta** (Eqs. 3.19 e 3.20): a integral vira uma soma de retângulos a cada 1 ms, com o erro no fim do passo.
  - **Ler:** Chapra p. 493; Castrucci seção 12.2.2 (retangular para trás).
- **Significado de $T_i$:** com erro constante, depois de $T_i$ = 0,084 s a parcela integral iguala a proporcional.
- **Anti-windup:** o integrador para quando o comando está em 0 ou 1 e o erro pede para ir além.

### 3.9 Modelo linear e função de transferência (3.5.4 e 3.5.5), **mudou na v20**

**Linearização:** cada relação é trocada pela reta tangente no ponto de operação (sete bicos, $P_{ref}$, $\alpha_0$). Também se tira o limite de velocidade da válvula.
- **Ler:** Castrucci seção 9.10.1 (linearização para pequenos sinais, série de Taylor, variáveis de desvio).

#### A linearização em palavras simples

**Por que linearizar.** Laplace, função de transferência e alocação de polos só funcionam com equações **lineares**, ou seja, retas. O modelo da barra não é linear: o bico tem uma raiz ($q = K\sqrt{P}$), a válvula também ($K_{v,max}\,\alpha\sqrt{P}$), e a bomba é uma parábola. A saída é trocar cada curva por uma reta que vale perto de um ponto escolhido.

**A ideia.** Vista de muito perto, uma estrada curva parece reta. A linearização escolhe um ponto da curva, traça a **reta tangente** nele e usa essa reta no lugar da curva. A inclinação da reta é a **derivada** no ponto. Enquanto o sistema ficar perto do ponto, o erro é pequeno; se ele se afastar muito, a reta deixa de valer.

**O ponto escolhido (ponto de operação nominal).** É a situação "normal" da máquina: 7 bicos abertos, P = 3,5 kgf/cm², válvula quase fechada (α = 0,023) e bomba dando $Q_s$ = 5,72 L/min.

**Desvios.** Em vez da pressão inteira, passa-se a falar de **quanto ela mudou** em relação ao ponto: ΔP, Δα e ΔN (Δ = "variação"). Exemplos: ΔN = −1 é "fechou um bico"; ΔP = +0,3 é "a pressão subiu 0,3 acima de 3,5". A referência é fixa, então a única coisa que chega de fora é o número de bicos, a **perturbação**.

**Cada peça vira uma reta (Tabela 3).** Os números são as derivadas no ponto:

| Peça | O que a reta diz |
|---|---|
| Bicos | cada bico a mais tira 0,795 L/min; cada 1 kgf/cm² a mais faz os bicos soltarem mais 0,795 L/min |
| Válvula | abrir 1 (de 0 a 1) desvia 6,55 L/min; a pressão quase não mexe nela (0,022), porque está quase fechada |
| Fonte | cada 1 kgf/cm² a mais faz a bomba entregar **1,645 L/min a menos** (a válvula de mola devolve mais ao tanque) |

**Juntando no nó.** "Entra = sai" vira "variação do que entra = variação do que sai":

$$-1{,}645\,\Delta P = 0{,}795\,\Delta N + 0{,}795\,\Delta P + 6{,}55\,\Delta\alpha + 0{,}022\,\Delta P$$

Juntando os termos em ΔP (1,645 + 0,795 + 0,022 = **2,462**):

$$\Delta P = -2{,}66\,\Delta\alpha - 0{,}323\,\Delta N$$

É a **planta linear**, com os mesmos ganhos da derivada implícita da 3.5.2:
- $K_g$ = −2,66 (ganho da planta): abrir a válvula baixa a pressão;
- $K_n$ = −0,323 (ganho do distúrbio): cada bico a menos sobe a pressão 0,323.

**Como ler o 2,462.** Ele diz quem segura a pressão. Quando ela sobe, os bicos soltam mais (0,795), a válvula solta um pouquinho mais (0,022) e a bomba entrega menos (1,645). Os três freiam a subida, e a bomba é cerca de 2/3 do total. Por isso a curva da fonte pesa tanto nos ganhos.

**Exemplo com números.** Um bico fecha (ΔN = −1): pela reta, a pressão sobe 0,323, de 3,5 para 3,82 kgf/cm². O modelo completo dá 3,83, quase igual. Para voltar, a válvula precisa abrir 0,323/2,66 = **0,121**, que é exatamente o *feedforward* por bico. As duas contas batem.

**A válvula.** Sem o limite de velocidade, ela já é um sistema de primeira ordem: vai até o comando aos poucos, com τa = 0,2 s. Em Laplace, vira o bloco $1/(\tau_a s + 1)$ (Eq. 3.22). Não precisa linearizar, porque já é linear.

**Resumo em uma frase:** "A 3.5.4 troca as curvas do modelo por retas em volta do ponto de operação (7 bicos, 3,5 kgf/cm²) e junta tudo no nó; daí saem a planta linear ΔP = −2,66 Δα − 0,323 ΔN e o bloco da válvula 1/(0,2s + 1), com os quais a 3.5.5 monta a malha em Laplace."

**Curiosidade que pode cair na banca:** as duas derivadas dos bicos dão o mesmo número (0,795) porque $K\sqrt{P} = nK/(2\sqrt{P})$ quando 2P = n, e aqui 2 × 3,5 = 7.

**Uma entrada só:** a referência é fixa, então $\Delta P_{ref} = 0$, e a única entrada é o número de bicos $\Delta N$. Esse é o caso "perturbação em degrau com referência nula" (Castrucci seção 3.11.3).

**Blocos** (Figura 13; diagramas de blocos em Castrucci seção 2.6):

| Bloco | Expressão | Equação |
|---|---|---|
| planta | $\Delta P = K_g\,\Delta A + K_n\,\Delta N$ | 3.21 |
| válvula | $1/(\tau_a s + 1)$ | 3.22; Ogata p. 147 |
| PI | $G_c(s) = K_c(1 + 1/(T_i s))$ | 3.23 |
| comando | $\Delta A_c = G_c\,\Delta P + \Delta A_{ff}$, com $\Delta A_{ff} = -(K_n/K_g)\,\Delta N$ no PI+FF | 3.24 |

O *feedforward* é o $F = -G_2/G_p$ do Castrucci (seção 7.8.1), com $G_2 = K_n$ e $G_p = K_g$.

**Malha:** com o ganho de malha $L(s) = G_c(s)|K_g|/(\tau_a s + 1)$, chega-se a $\Delta P[1 + L] = K_n\,\Delta N + \ldots$ (Eq. 3.25). Daí:

$$T_n(s) = \frac{K_n}{1 + L(s)} \quad \text{(Eq. 3.26; Ogata p. 22)}$$

| Controlador | $T_n(s)$ | Equação |
|---|---|---|
| P | $\dfrac{K_n(\tau_a s + 1)}{\tau_a s + 1 + K_c\lvert K_g\rvert}$ | 3.27 |
| PI | $\dfrac{K_n T_i s(\tau_a s + 1)}{\tau_a T_i s^2 + T_i(1 + K_c\lvert K_g\rvert)s + K_c\lvert K_g\rvert}$ | 3.28 |
| PI+FF | $\dfrac{K_n \tau_a T_i s^2}{\text{mesmo denominador}}$ | 3.29 |

**O que elas mostram:**
1. **O *feedforward* não muda a estabilidade:** as Eqs. (3.28) e (3.29) têm o mesmo denominador.
2. **O P deixa erro:** pelo teorema do valor final (Ogata p. 198; Castrucci seção 2.3.4), um bico fechando deixa $-K_n/(1 + K_c|K_g|)$ = 0,101 kgf/cm².
3. **O PI zera o erro:** o $s$ do numerador faz $T_n(0) = 0$. É a linha "um integrador, erro nulo" da Tabela 3.4 do Castrucci.
4. **O *feedforward* cancela em regime, mas não na hora:** o que sobra do distúrbio é $K_n\,\tau_a s/(\tau_a s + 1)$, porque o comando dele também passa pela válvula.
5. **Estabilidade:** com todos os coeficientes da equação característica positivos, P e PI são estáveis para qualquer ganho positivo. Como a leitura é em tempo real, não há ganho máximo; o limite prático é a velocidade da válvula.

**Como explicar:** "A função de transferência explica com conta o que o simulador mostra, e é dela que saem os ganhos."

### 3.10 Sintonia por alocação de polos (3.5.6)

**A ideia:** primeiro se escolhe como a malha deve responder, e depois se calcula o controlador que coloca os polos lá (Ogata p. 658; Castrucci seção 8.2).

**Especificação:**
- **$\zeta$ = 0,7:** sobressinal de 4,6%, perto do amortecimento que acomoda mais rápido (Ogata p. 157);
- **$t_s$ = 0,5 s:** um pouco mais rápido que a válvula livre ($4\tau_a$ = 0,8 s).

**Conta:** dividindo a equação característica por $\tau_a T_i$ e comparando com $s^2 + 2\zeta\omega_n s + \omega_n^2$ (Ogata p. 151):

$$\omega_n = \frac{4}{\zeta t_s} = 11{,}43 \;(3.30) \qquad K_c = \frac{2\zeta\omega_n\tau_a - 1}{|K_g|} = 0{,}827 \;(3.31) \qquad T_i = \frac{K_c|K_g|}{\tau_a\omega_n^2} = 0{,}084\ \text{s} \;(3.32)$$

- **Polos:** os do PI ficam em −8,0 ± j8,2; o do P, em −16.
- **Por que o P usa o mesmo $K_c$:** a malha do P tem um polo só, então não há $\zeta$ para escolher.
- **A conta da rampa, nova na v20:** compensar um bico pede 0,121 de abertura, e 0,121/0,5 ≈ 0,24 s de rampa, que cabe nos 0,5 s. Três bicos pedem 0,36, e só a rampa leva cerca de 0,7 s. **Por isso o C1 acomoda em 0,44 s e o C2 em 1,02 s.**

### 3.11 Cenários e métricas (3.6)

**Cenários:**
- **C1:** fecha um bico a cada 2 s, de 7 até 1, e reabre um a um (26 s).
- **C2:** a sequência do ensaio de Rosa, 7 → 4 bicos em 2 s e 4 → 1 em 8 s (14 s), com fechamentos triplos.
- **C3:** trocas aleatórias a cada 0,1 a 0,5 s, durante 20 s (66 trocas), com semente fixa.

**Métricas:**
- tempo fora da faixa de ±10% (Eqs. 3.33 e 3.34), a principal;
- IAE (Eq. 3.35);
- desvio máximo;
- acomodação em ±2% (Ogata p. 155; Castrucci seção 3.6.5).

### 3.12 Programa (3.7)

- `simulacao/modelo_barra.py`, inteiro no Apêndice A. Usa só numpy e matplotlib e roda em cerca de 3 min.
- **Conferências automáticas:** o programa para se algo sair do esperado:
  - $K$ = 0,425 e os erros do ajuste;
  - $P_{ref}$ atingível com sete bicos;
  - $K_g$ e $K_n$ analíticos iguais aos numéricos para todo $n$;
  - $\zeta$ e $\omega_n$ iguais aos especificados;
  - o denominador montado bloco a bloco igual ao da Eq. (3.28).

---

## 4. Resultados (Cap. 4): como ler a Tabela 9

| Tempo fora da faixa | Malha aberta | P | PI | PI+FF |
|---|---|---|---|---|
| C1 | 69,2% | 38,5% | **0,0%** | **0,0%** |
| C2 | 85,7% | 46,3% | **6,8%** | **6,8%** |
| C3 | 90,5% | 50,1% | **8,3%** | 9,5% |

Três mensagens, nesta ordem:
1. **O P não basta.** Ele deixa a pressão parada acima da referência, no valor da Eq. (2.9): 3,81 kgf/cm² com quatro bicos e 4,12 com um. A partir do quarto bico fechado, sai da faixa.
2. **O PI resolve o erro permanente.** No C1 dá 0% fora da faixa, com pico de 9,5% e acomodação em 0,44 s. No C2 sobra o **salto instantâneo**: quando três bicos fecham, a pressão pula para 4,54 kgf/cm² (29,7%) no mesmo instante, porque a válvula ainda está parada. O controle define só quanto tempo ela leva para voltar, 1,02 s.
3. **O gargalo é a velocidade da válvula.**
   - Dobrar $\omega_{max}$ leva o PI de 6,8% para 3,4% no C2 e de 8,3% para 0,4% no C3.
   - No C3, a válvula passa 68% do tempo na velocidade máxima com o PI e 75% com o PI+FF.

**Por que o *feedforward* não ajudou (4.6):**
- No Exemplo 7.4 do Castrucci (seção 7.8.1), a planta tem atraso puro, e o *feedforward* age antes de a realimentação perceber o erro.
- Aqui a pressão salta na hora (H6), e o PI, lendo em tempo real, já manda abrir no mesmo instante. Os dois comandos pedem mais do que a válvula dá, então ela anda em rampa nos dois casos.
- Nas trocas rápidas, o *feedforward* manda a válvula para um alvo que muda antes de ela chegar.

**Conferências que dão confiança:**
- a função de transferência acerta o valor final do simulador (Figura 18);
- H6, com a mangueira no modelo: 0,4 p.p.;
- passo de integração: com 2 ms muda 0,1 p.p.; com 10 ms muda 0,8 p.p.;
- anti-windup: estendido ao limite de velocidade, o C3 iria para 3,2%; sem anti-windup, para 29%.

---

## 5. Conclusão e limitações (dizer com honestidade)

- **Confirmada em parte, só em simulação.** O PI atende nas trocas de um bico e na maior parte da troca aleatória, mas não nas trocas simultâneas.
- **Limitações principais:**
  - $\tau_a$, $\omega_{max}$ e a curva da válvula foram **estimados**;
  - não há medição no tempo para validar a dinâmica;
  - o sensor foi tratado como perfeito, sem ruído;
  - a leitura em tempo real é uma idealização. Na prática, o período de leitura deve ser pelo menos 10 vezes menor que o período das oscilações (Castrucci seção 12.6). Com os polos em −8,0 ± j8,2, esse período é 2π/8,2 ≈ 0,77 s, então ler a cada 77 ms ou menos.
- **Trabalhos futuros:**
  - medir a válvula;
  - ajustar $\zeta$ e $t_s$ com ruído real;
  - usar uma válvula mais rápida ou antecipar o comando da válvula;
  - estender o anti-windup ao limite de velocidade;
  - barras comerciais;
  - dados de campo.

---

## 6. Perguntas prováveis da banca

**1. Por que alocação de polos?**
Existe um modelo, e a malha com PI tem dois polos e dois parâmetros, $K_c$ e $T_i$. Basta escolher onde ficam os polos e resolver (Ogata p. 658; Castrucci seção 8.2).
*O texto não menciona Ziegler-Nichols. Se perguntarem: a planta é de 1ª ordem, sem curva em S e sem oscilação sustentada com P, então as regras não se aplicam (Ogata p. 523–524).*

**2. Por que $\zeta$ = 0,7 e $t_s$ = 0,5 s?**
- $\zeta$ = 0,7 dá sobressinal pequeno (4,6%) e acomodação quase mínima (Ogata p. 157).
- $t_s$ = 0,5 s é um pouco mais rápido que a válvula livre e ainda cabe na rampa para um bico (0,24 s).
- Um $t_s$ menor daria um $K_c$ maior, mais esforço do motor e mais sensibilidade a ruído, sem ganho real, porque a rampa já limita.

**3. Por que a análise só usa o número de bicos como entrada?**
A referência é fixa em todos os cenários, e o problema é rejeitar a perturbação. É o caso "perturbação em degrau, referência nula" do Castrucci (seção 3.11.3). A mesma equação característica valeria para uma mudança de referência.

**4. Onde o modelo da fonte entra no controle?** Em cinco lugares:
1. **Nos ganhos $K_g$ e $K_n$:** o termo $-dQ_s/dP$ = 1,645 é cerca de dois terços do denominador da Eq. (3.15). Fazendo a conta com uma fonte de vazão constante ($dQ_s/dP = 0$): $dP/dC$ = −1,871/0,817 = −2,29, e $K_g$ ≈ −8,0, três vezes maior. A sintonia seria outra. *Essa conta não está no texto; é para responder na hora.*
2. **No *feedforward* e em $\alpha_0$:** a Eq. (3.14) usa $Q_s(P_{ref})$.
3. **Na escolha de $P_{ref}$:** precisa ficar abaixo dos 3,56 kgf/cm² que a fonte sustenta com sete bicos.
4. **Na escolha de $K_{v,max}$:** com folga sobre os 3,06 necessários, que é $Q_s(P_{ref})/\sqrt{P_{ref}}$.
5. **No simulador:** a cada 1 ms a pressão é recalculada pela Eq. (3.10), com a fonte. A fonte é a própria planta.

**5. Se a função de transferência diz que qualquer ganho é estável, o que limita o ganho?**
A velocidade da válvula, que não entra no modelo linear, e, num equipamento real, o ruído do sensor e o período de leitura (Castrucci seção 12.6).

**6. Por que o P usa o mesmo $K_c$ do PI?**
A malha do P tem um polo só, em −16, então não há $\zeta$ para escolher. Com o mesmo ganho, a diferença P × PI é só a ação integral.

**7. Por que não usar a ação derivativa?**
- Amplifica o ruído (Ogata p. 159).
- Os saltos de pressão dariam picos no comando (Ogata p. 541).
- Com o PI, $K_c$ e $T_i$ já colocam os dois polos onde se quer.

**8. Por que o *feedforward* não ajuda, se a teoria diz que ele antecipa?**
Ele antecipa em relação à realimentação. Aqui a realimentação já reage no mesmo milissegundo, porque não há atraso entre a troca e a leitura, e a válvula limita os dois igualmente. No exemplo do Castrucci (Exemplo 7.4), havia atraso puro na planta. Com leitura a intervalos maiores, o *feedforward* poderia recuperar parte da vantagem (seção 3.8 do texto).

**9. Por que o pico do C2 não some com nenhum controlador?**
A pressão salta no instante em que os bicos fecham, antes de a válvula se mover. Seria preciso mover a válvula **antes** das solenoides.

**10. Por que a pressão pode ser considerada instantânea?**
Foi conferido: com a capacitância da mangueira (Merritt p. 53), o tempo fora da faixa mudou no máximo 0,4 p.p., e o P continuou estável até $K_c$ = 10.

**11. De onde vêm $\tau_a$ e $\omega_{max}$?**
São estimados, e o texto diz isso. São os parâmetros que mais pesam, e medi-los é o primeiro trabalho futuro.

**12. Por que $P_{ref}$ = 3,5 kgf/cm² e $\alpha_0$ = 0,023?**
A válvula de alívio só baixa a pressão. Com sete bicos e a válvula fechada, a fonte chega a 3,56, então a referência fica logo abaixo. Por isso a abertura de equilíbrio é tão pequena.

**13. Por que o ganho não depende do número de bicos?**
A pressão depende de $n$ e $\alpha$ só através de $C$. Em $P_{ref}$, $C$ é sempre 3,057, e $dP/dC$ (Eq. 3.15) não muda.

**14. Como sabe que o anti-windup importa?**
Sem ele, o C3 do PI iria de 8,3% para 29% (Castrucci seção 6.3.4 explica o efeito).

**15. Por que ±10% e não ±5%?**
É o valor da ISO 16122-2, item 4.5.4, para a pressão, e corresponde a cerca de ±5% na vazão.

**16. Esse modelo vale para uma barra comercial?**
Não diretamente. A bancada tem vazão pequena e perda desprezível na barra (H2). Barras longas precisam da perda distribuída e talvez da capacitância.

**17. O que garante que o programa está certo?**
- As conferências automáticas;
- a função de transferência batendo com o simulador (Figura 18);
- a validação cruzada do modelo estático.

---

## 7. Cola: números para lembrar

| Grandeza | Valor |
|---|---|
| Constante do bico $K$ | 0,425 (L/min)/√(kgf/cm²) |
| Erro do modelo estático (ajuste / validação cruzada) | 0,7% e 2,3% / 0,9% e 2,7% |
| Pressão com válvula fechada, 7 → 1 bico | 3,57 → 5,58 kgf/cm² (+56%) |
| $P_{ref}$; máximo com 7 bicos | 3,5; 3,56 kgf/cm² |
| Fonte: $a_2$, $a_1$, $a_0$ | −0,0355; −0,2018; 5,815 |
| $K_{v,max}$; $\alpha_0$; abertura por bico; $\alpha_{ff}(1)$ | 3,5; 0,023; 0,121; 0,752 |
| $\tau_a$; $\omega_{max}$ (estimados) | 0,2 s; 0,5 s⁻¹ |
| $\Delta t$ (simulação e leitura) | 1 ms |
| $dQ_s/dP$; $C/(2\sqrt{P})$; $dP/dC$ | −1,645; 0,817; −0,760 |
| $K_g$; $K_n$; $K_n/K_g$ | −2,66 kgf/cm²; −0,323 por bico; 0,121 |
| $\zeta$; $t_s$; $\omega_n$ | 0,7; 0,5 s; 11,43 rad/s |
| $K_c$; $T_i$; ganho de malha $K_c\lvert K_g\rvert$ | 0,827; 0,084 s; 2,2 |
| Polos: PI; P | −8,0 ± j8,2; −16 |
| Erro do P por bico (valor final) | 0,101 kgf/cm² |
| P parado: 4 bicos / 1 bico | 3,81 / 4,12 kgf/cm² |
| Faixa | ±10% → 3,15 a 3,85 kgf/cm² (ISO 16122-2, 4.5.4) |
| PI fora da faixa: C1 / C2 / C3 | 0% / 6,8% / 8,3% |
| PI+FF fora da faixa: C1 / C2 / C3 | 0% / 6,8% / 9,5% |
| Acomodação: C1 PI / PI+FF; C2 | 0,44 / 0,48 s; 1,02 s |
| Pico do fechamento triplo (C2) | 29,7% |
| $\omega_{max}$ = 1,0 / 2,0: PI no C2 e no C3 | 3,4% e 0,4% / 1,7% e 0,2% |
| Válvula na velocidade máxima (C3): PI / PI+FF | 68% / 75% |
| Anti-windup: estendido / sem | C3 3,2% / 29% |
| Leitura máxima recomendada (Castrucci 12.6) | ≈ 77 ms |
