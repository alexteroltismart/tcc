# Chapra e Canale — trechos citáveis no TCC

**Referência (ABNT):** CHAPRA, S. C.; CANALE, R. P. **Métodos numéricos para engenharia**. 5. ed. Porto Alegre: AMGH, 2011. Recurso eletrônico. ISBN 978-85-8055-011-5.

Dados tirados da ficha catalográfica (PDF p. 3). Também foi publicado como livro impresso em 2008, pela McGraw-Hill, com ISBN 978-85-86804-87-8.

**Arquivos e páginas:**
- O PDF original tem acentos no nome que as ferramentas não abrem. A cópia de trabalho é `referencias base/Chapra_2011_Metodos_Numericos.pdf`.
- Página do livro = página do PDF − 17.
- Todas as equações abaixo foram conferidas no texto do PDF em 04/11/2026.
- Citação: (CHAPRA; CANALE, 2011, p. X).

| O que | Fórmula / ideia (como no livro) | Nº | Seção / página | Uso no TCC (v14) |
|---|---|---|---|---|
| **Método da bissecção** | se $f(x_l)f(x_u) < 0$ há raiz no intervalo; testa-se o ponto médio $x_r = (x_l + x_u)/2$ e fica-se com a metade em que o sinal troca | (5.1); algoritmo na Fig. 5.5 | 5.2, p. 101–102 | 3.3.4 (Eq. 3.10 resolvida por bissecção); Quadro 3; busca do $K_{cr}$ (3.5.4) |
| **Diferença dividida centrada** | $f'(x_i) \approx \dfrac{f(x_{i+1}) - f(x_{i-1})}{2h}$, com erro $O(h^2)$; mais precisa que a progressiva e a regressiva | **(4.22)** | 4.1, p. 75–76 | 3.5.1: $K_g$ pela Eq. 3.13 (±0,005 em torno de $\alpha_{ff}$) |
| **Regressão polinomial por mínimos quadrados** | soma dos quadrados dos resíduos $S_r = \sum (y_i - a_0 - a_1x_i - a_2x_i^2)^2$; derivadas iguais a zero dão as equações normais, um sistema linear | **(17.18)**, (17.19) | 17.2, p. 393 | 3.3.2: curva da fonte (Eq. 3.5, `numpy.polyfit`) |
| **Coeficiente de determinação** | $r^2 = (S_t - S_r)/S_t$; $r^2 = 1$ é ajuste perfeito. Também vale para a regressão polinomial (p. 394) | (17.10) | 17.1, p. 384–385 | 4.1: R² = 0,9999 da curva da fonte |
| **Método de Euler** | $y_{i+1} = y_i + f(x_i, y_i)\,h$ | **(25.2)** | 25.1, p. 588 | 3.4.3, Eq. 3.12 |
| **Erro do método de Euler** | erro local proporcional a $h^2$; erro global $O(h)$, ou seja, proporcional ao passo: "o erro pode ser reduzido diminuindo-se o tamanho do passo" | (25.9) e texto | 25.1.1, p. 590–592 | 3.4.3 e 4.2: escolha de $\Delta t$ = 1 ms e teste com 2 e 10 ms |
| **Integração por retângulos** | contar retângulos sob a curva dá uma "estimativa grosseira da área", refinada com reticulado mais fino | texto | introdução da Parte 6 (PT6), p. 493 | 3.5.3 e 4.2: soma de retângulos do PI (Eq. 3.16), "acompanha a integral de forma grosseira" |

## Observações

- **Regressão.** O TCC ajusta P em função de Q ($y = P$, $x = Q_s$) com um polinômio de 2º grau. É exatamente o caso da Eq. 17.18, com os coeficientes renomeados ($a_0, a_1, a_2$ do livro correspondem a $a_0, a_1, a_2$ do TCC).
- **Bissecção no TCC.** O teste de sinal é feito em $Q_s(P) - k_{total}\sqrt P$. Ficar com a metade em que a diferença troca de sinal é o passo 3 da Fig. 5.5.
- **Euler no TCC.** É aplicado a $d\alpha/dt$ (Eq. 3.11). O erro global ser $O(h)$ justifica o teste do passo: com 2 ms o resultado quase não muda.
- **Não está no Chapra:** a forma discreta do PI e o efeito da amostragem. Isso é assunto de controle digital (Ogata, *Discrete-time control systems*, ou Åström e Wittenmark).
