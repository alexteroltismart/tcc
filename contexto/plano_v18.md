# Plano v18: malha de controle no domínio de Laplace com superposição (referência + bicos)

## Decisões do autor (2026-11-09)

- D1: **só Laplace** (s). Sem Bode: o Passo 9 sai do plano.
- D2: **sem FF de referência**. O FF continua só dos bicos, e $P_{ref}$ entra só pelo erro. A derivada $1/K_g$ pode virar uma frase, no máximo.
- D3: conferência **só no modelo linear** (`resposta_linear` + figura da soma). Os números do Cap. 4 não mudam.
- D4: o desenvolvimento vai **direto na v18** (17.md → 18.md).

## Objetivo

Hoje, na seção 3.5.4, só aparece $\Delta P(s)/\Delta N(s)$, e a referência entra como constante. Na v18 a planta e o controlador são escritos com **duas entradas**: a variação da pressão de referência $\Delta P_{ref}(s)$ e a variação do número de bicos $\Delta N(s)$. Cada efeito é calculado **sozinho**, com a outra entrada zerada, e os dois são **somados** no fim (princípio da superposição, que vale porque o modelo foi linearizado).

**Não muda:**
- modelo estático;
- hipóteses H1–H6;
- especificação ζ = 0,7 e t_s = 0,5 s;
- $K_c$ = 0,827 e $T_i$ = 0,084 s;
- controlador amostrado a 50 ms;
- cenários C1–C3 e números do Cap. 4;
- nenhuma menção a Ziegler-Nichols.

## Ponto de operação (base de tudo)

$\bar n$ = 7, $\bar P = P_{ref}$ = 3,5 kgf/cm², $\bar\alpha = \alpha_{ff}(7)$ = 0,023, $\bar C = nK + K_{v,max}\alpha$ = 3,057, $\bar Q_s$ = 5,72 L/min.
Os desvios são definidos como $\Delta P = P - \bar P$, $\Delta\alpha = \alpha - \bar\alpha$, $\Delta n = n - \bar n$ e $\Delta P_{ref} = P_{ref} - \bar P$. As maiúsculas $\Delta P(s)$, $\Delta A(s)$, $\Delta N(s)$ e $\Delta P_{ref}(s)$ são as suas transformadas.

---

## Desenvolvimento passo a passo

### Passo 1: planta linearizada de forma analítica

Este passo substitui a diferença centrada como cálculo principal; a Tabela 3 fica como conferência.

O equilíbrio do nó (Eq. 3.10) é escrito como uma função que vale zero:
$$F(P, C) = Q_s(P) - C\sqrt{P} = 0$$
Pela derivada implícita (regra da cadeia), $dP/dC = -(\partial F/\partial C)/(\partial F/\partial P)$:
$$\frac{dP}{dC} = \frac{-\sqrt{\bar P}}{\dfrac{\bar C}{2\sqrt{\bar P}} - \dfrac{dQ_s}{dP}}, \qquad \frac{dQ_s}{dP} = \frac{1}{2a_2\bar Q_s + a_1}$$
- **Leitura física:** o denominador soma o quanto as saídas (bicos + válvula) aumentam a vazão quando a pressão sobe, $\bar C/(2\sqrt{\bar P})$, com o quanto a fonte reduz a sua vazão, $-dQ_s/dP$. Quanto mais "dura" a fonte, menor o efeito de cada abertura.
- **Números:** $dQ_s/dP$ = −1,645 e $dP/dC$ = −0,760, o que dá:
$$K_g = K_{v,max}\,\frac{dP}{dC} = -2{,}66 \qquad K_n = K\,\frac{dP}{dC} = -0{,}323$$
  Os valores batem com a Tabela 3 e com o script.
- **Por que $K_g$ não depende de $n$:** $\bar C$ e $\bar P$ são os mesmos para qualquer $n$ (já está no texto; agora fica explícito na fórmula).
- **Equação da planta:**
$$\Delta P(s) = K_g\,\Delta A(s) + K_n\,\Delta N(s)$$

### Passo 2: atuador

$$\Delta A(s) = \frac{1}{\tau_a s + 1}\,\Delta A_c(s)$$
É a Eq. 3.19 atual, sem mudança.

### Passo 3: controlador com as duas entradas

O erro é $E(s) = \Delta P(s) - \Delta P_{ref}(s)$; agora a referência aparece de forma explícita. O comando é a soma de duas parcelas:
$$\Delta A_c(s) = G_c(s)\,E(s) + \Delta A_{ff}(s)$$
- **Realimentação:** $G_c(s) = K_c\,(1 + 1/(T_i s))$; no controlador P, $T_i \to \infty$.
- **FF dos bicos:** $\Delta A_{ff} = -(K_n/K_g)\,\Delta N$, a derivada da Eq. 3.14 em relação a $n$.
- *(opcional, decisão D2)* **FF da referência:** a Eq. 3.14 também depende de $P_{ref}$, e a sua derivada é $\partial\alpha_{ff}/\partial P_{ref} = 1/K_g$ = −0,376. Isso dá a parcela $\Delta A_{ff,r} = (1/K_g)\,\Delta P_{ref}$, já conferida numericamente.

### Passo 4: juntar tudo em uma equação

Substituindo os Passos 2 e 3 no Passo 1, com $K_g = -|K_g|$ e o **ganho de malha** $L(s) = G_c(s)\,|K_g|/(\tau_a s + 1)$:
$$\Delta P\,[1 + L(s)] = L(s)\,\Delta P_{ref} + K_n\,\Delta N + \frac{K_g}{\tau_a s + 1}\,\Delta A_{ff}$$
Os mesmos blocos aparecem nas duas entradas, e o fator $1 + L(s)$ é comum às duas.

### Passo 5: efeito isolado da referência ($\Delta N = 0$)

$$T_r(s) = \frac{\Delta P(s)}{\Delta P_{ref}(s)} = \frac{L(s)}{1 + L(s)}$$

- **P:**
$$T_r(s) = \frac{K_c|K_g|}{\tau_a s + 1 + K_c|K_g|}$$
  O valor final é $T_r(0) = K_c|K_g|/(1+K_c|K_g|)$ = 0,688: o P só leva a pressão a **69%** da mudança pedida.
- **PI:**
$$T_r(s) = \frac{K_c|K_g|\,(T_i s + 1)}{\tau_a T_i s^2 + T_i(1 + K_c|K_g|)\,s + K_c|K_g|}$$
  O valor final é 1, então o erro em regime é zero.
- **Novidade:** o numerador tem um **zero** em $s = -1/T_i$ = −11,9, perto dos polos −8 ± j8,2. Por isso o degrau de referência tem sobressinal de **10,6%**, e não os 4,6% que ζ = 0,7 daria, com acomodação em 0,45 s (valores conferidos numericamente). Ogata trata o efeito de zeros na resposta de 2ª ordem [A CONFERIR página].
- **PI + FF de referência** (só se D2 = sim): o numerador ganha o termo do FF. Será desenvolvido se for escolhido.

### Passo 6: efeito isolado dos bicos ($\Delta P_{ref} = 0$)

$$T_n(s) = \frac{\Delta P(s)}{\Delta N(s)} = \frac{K_n\,[1 + \text{termo do FF}]}{1 + L(s)}$$

É o desenvolvimento atual (Eqs. 3.22–3.25), reorganizado para mostrar o mesmo $1 + L(s)$ do Passo 5:
- **P:** igual à Eq. 3.23;
- **PI:** igual à Eq. 3.24;
- **PI+FF:** o FF multiplica $K_n$ por $\tau_a s/(\tau_a s+1)$, o que dá a Eq. 3.25.

### Passo 7: superposição (soma dos efeitos)

$$\Delta P(s) = T_r(s)\,\Delta P_{ref}(s) + T_n(s)\,\Delta N(s)$$

- **Justificativa:** o sistema é linear e vale a superposição. Citar Ogata (cap. 2, sistemas lineares) [A CONFERIR página].
- **Erro:**
$$E(s) = -S(s)\,\Delta P_{ref}(s) + T_n(s)\,\Delta N(s), \qquad S(s) = \frac{1}{1 + L(s)}$$
- **Consequência:** as duas funções têm o **mesmo denominador**, portanto os mesmos polos e a mesma equação característica. Uma única sintonia serve para seguir a referência e para rejeitar os bicos, e o FF não muda a estabilidade em nenhum dos casos.

### Passo 8: valores finais (teorema do valor final) para cada entrada e cada controlador

As entradas são um degrau $\Delta P_{ref} = +0{,}1/s$ e um bico fechando, $\Delta N = -1/s$:

| Controlador | Erro final, referência | Erro final, bico | Erro final, os dois juntos |
|---|---|---|---|
| P | $-0{,}1/(1+K_c\vert K_g\vert)$ = −0,031 | $-K_n/(1+K_c\vert K_g\vert)$ = +0,101 | soma = +0,070 |
| PI | 0 | 0 | 0 |
| PI+FF | 0 | 0 | 0 |

A última coluna mostra a superposição em número.

### Passo 9: domínio da frequência propriamente dito ($s = j\omega$), decisão D1

Este passo traça $|T_r(j\omega)|$ e $|T_n(j\omega)|$ (Bode só de módulo) para P, PI e PI+FF, e mostra:
- a faixa de frequência em que a pressão segue a referência (banda passante);
- que o PI rejeita trocas lentas de bicos ($|T_n| \to 0$ quando $\omega \to 0$);
- que o FF baixa $|T_n|$ nas frequências baixas e médias, mas não nas altas, onde quem limita é a válvula.

Para isso entra uma figura nova, gerada no script com numpy puro, sem biblioteca de controle.

### Passo 10: sintonia

As Eqs. 3.26–3.28 continuam as mesmas, porque a equação característica não mudou. Entram duas notas:
- o sobressinal maior para a referência, causado pelo zero do PI;
- $K_{c,lim}$ (Eq. 3.29), que vale para as duas entradas, porque depende só da malha.

### Passo 11: conferência numérica (decisão D3)

- **Script:** `resposta_linear` passa a aceitar $\Delta P_{ref}$. Uma figura nova mostra três respostas: só referência, só bico, e os dois ao mesmo tempo. A terceira deve ser **igual à soma** das duas primeiras, o que é a prova visual da superposição.
- *(opcional)* **Simulador completo:** degrau de $P_{ref}$ (ex.: 3,5 → 3,0) no simulador não linear, comparado com $T_r$. O limite de velocidade e a amostragem aparecem como diferença.
- **Conferência automática nova:** os polos de $T_r$ e de $T_n$ devem ser iguais.

---

## Onde entra no texto

- **3.5.4** é reescrita e dividida, por exemplo:
  - 3.5.4 *Planta linearizada* (Passos 1–2);
  - 3.5.5 *Malha fechada: efeito da referência e dos bicos* (Passos 3–8);
  - 3.5.6 *Resposta em frequência* (Passo 9, se escolhido);
  - 3.5.7 *Sintonia* (a atual 3.5.5).
- **Figura 13** (diagrama em $s$): ganha a entrada $\Delta P_{ref}$ no somador; o arquivo é `build/fig/fig12_freq.py`.
- **2.6 ou 2.6.1:** um parágrafo curto sobre superposição e sobre o efeito de um zero, com referência.
- **Lista de Símbolos:** $T_r$, $T_n$, $L$, $S$, $\Delta P_{ref}$.
- **4.2:** os números novos, ou seja, a tabela do Passo 8, o sobressinal de 10,6% e a figura da superposição.
- **Motivação para a referência mudar:** na pulverização em taxa variável, a dose pode ser ajustada mudando a pressão (seção 2.5). Por isso faz sentido analisar $\Delta P_{ref}$, mesmo com os cenários C1–C3 usando $P_{ref}$ fixa.
- **Depois:** Resumo/Conclusão (uma frase), notas A18, roteiro de estudo e apresentação.

## Riscos

- As equações do Cap. 3 serão renumeradas, e as referências cruzadas e a apresentação precisam ser atualizadas.
- O texto cresce. Para compensar, a derivação atual do $\Delta P/\Delta N$ vira um caso particular (com $\Delta P_{ref} = 0$), em vez de ficar repetida.
- O sobressinal de 10,6% é **maior** que o especificado. Ele precisa ser apresentado como consequência conhecida do PI, sem mudar a sintonia; mudar a sintonia seria fora do escopo.
