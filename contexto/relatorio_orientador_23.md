# Parecer do orientador sobre a v23 (11/11/2026)

**Escopo:** Capítulos 1 a 5 de `contexto/23.md`, com dois focos: clareza da redação e correção da teoria de controle.

**Como foi feito:** duas leituras independentes, uma de redação e outra de controle. Depois, conferência minha de cada ponto no texto e, quando havia número, no Python. A margem de fase e a margem de atraso foram recalculadas: 69° e 88 ms. Os números das tabelas e as referências cruzadas batem, salvo onde indicado.

---

## Veredito

O texto está **mais claro que a v20**, mas ainda **não está pronto para a banca**.

Há quatro afirmações de controle que um examinador atento derruba em dois minutos:
1. a causa atribuída ao fraco desempenho do *feedforward*;
2. uma frase da 4.2 que contradiz a hipótese H6;
3. a especificação de $t_s$ "cumprível" que os próprios resultados desmentem;
4. a regra de amostragem de 77 ms, que deixa a malha perto do limite.

Nenhuma delas exige rodar a simulação de novo. Todas exigem **reescrever o raciocínio**, e não só a frase.

O segundo problema é de ordem. O Cap. 2 fala de função de transferência, polos e equação característica antes de defini-los, e a definição só aparece no Cap. 3. Isso viola a regra que você mesmo estabeleceu: nenhum conceito pode aparecer pela primeira vez na metodologia.

Nota, se fosse hoje: **7,5**. Com os 🔴 corrigidos, passa de 8,5.

---

## 🔴 Bloqueantes: corrigir antes de qualquer outra coisa

### 1. A explicação do *feedforward* está errada (4.6 e Conclusão)

**O que o texto diz:** que o FF não ajuda "por causa da velocidade da válvula" e que "só faria diferença se a válvula fosse rápida o bastante para chegar à posição calculada antes de o PI reagir".

**Por que está errado:** o próprio trabalho mostra o contrário. Na Figura 22, **sem limite de velocidade**, o PI+FF já é pior que o PI: passa 21% do salto abaixo da referência, contra 10% do PI. A causa é estrutural:
- a planta é estática e o PI lê a pressão em tempo real, então a parcela proporcional já reage no instante da troca. Não existe um "antes de o PI reagir";
- o FF estático passa pela mesma válvula e se soma a uma correção que já está agindo. O resultado é sobrecorreção. Em $T_{n,PI+FF}$ (Eq. 3.28), o zero duplo na origem é a marca disso;
- o limite de velocidade **agrava** o efeito, mas não é a causa.

**O texto também se contradiz:** a 4.6 diz que "a correção leva o mesmo tempo", e a Tabela 8 dá 0,63 s para o PI e 0,86 s para o PI+FF.

**O que fazer:**
- Reescrever a 4.6: com realimentação contínua e planta sem atraso, o FF estático não tem o que antecipar e só soma uma correção duplicada.
- Citar os números sem limite (10% contra 21%) e o zero duplo.
- Dizer que o compensador ideal seria $-(K_n/K_g)(\tau_a s + 1)$, que não é realizável e cuja forma estática só cancela em regime.
- Manter Castrucci, Ex. 7.4: o FF ajuda quando há tempo morto, e aqui não há.
- Corrigir a Conclusão no mesmo sentido.

O teste de antecipação dos bicos (4,7% no C3) cabe como trabalho futuro, porque é justamente a forma de dar ao FF algo que ele possa antecipar.

### 2. A 4.2 contradiz a H6

**Trecho:** "quando a pressão chega à referência, a válvula já passou da posição certa".

**Por que está errado:** pela H6 a pressão é função direta de $\alpha$ e $n$. Então $P = P_{ref}$ ocorre exatamente quando $\alpha = \alpha_{ff}(n)$: nesse instante a válvula está na posição certa. Quem passou do ponto foi o **comando**, inflado pelo integrador durante a rampa.

**Reescrever:** "quando a pressão chega à referência, a válvula está na abertura certa, mas o comando, aumentado pelo integrador durante a rampa, ainda pede mais abertura; a válvula continua andando e passa do ponto."

### 3. A especificação de $t_s$ não é cumprida nem com um bico (3.5.5)

**O que o texto diz:** que pedir 0,5 s não faz "o comando passe a exigir da válvula, a toda hora, mais velocidade do que ela tem" e que "a especificação pode ser cumprida nas trocas de um bico".

**O que o próprio texto mostra depois:**
- na 3.5.6 e na 4.2, uma troca de um bico já pede 1,34 s⁻¹, 2,7 vezes o $\omega_{max}$;
- na Tabela 8, com o limite, o $t_s$ é 0,63 s.

A frase foi escrita antes de esses números existirem e ficou falsa. **Isso é meu também:** o argumento da rampa de 0,24 s ignorou o integrador.

**Reescrever:** 0,5 s é a especificação **do modelo linear**. Com $\omega_{max}$ = 0,5 s⁻¹ a válvula satura em velocidade já numa troca de um bico, e a resposta real é medida na 4.2. Pode-se acrescentar que, para não saturar, seria preciso $K_c \le \omega_{max}\tau_a/|K_n| \approx 0{,}31$. Esse é o caminho da sintonia por cancelamento, que você decidiu não seguir; basta citar como limitação.

### 4. A regra de amostragem leva a malha perto da instabilidade (3.8)

**O que o texto diz:** "basta ler a cada 77 ms ou menos".

**A conta que derruba:**
- a margem de fase do PI é 69° em $\omega_c$ = 13,7 rad/s, o que dá uma **margem de atraso de 88 ms**;
- ler a cada 77 ms acrescenta cerca de $T/2$ = 38 ms de atraso pelo segurador, mais até um período de atraso de cálculo, porque o programa usa a pressão do passo anterior;
- com isso, a fase perdida chega perto ou passa dos 69°.

A regra de "10 leituras por oscilação" foi aplicada a uma resposta quase sem oscilação ($\zeta$ = 0,7). Quem citar Castrucci 12.6 assim vai ouvir que ela se refere à banda passante.

**Reescrever:** "a malha linear tolera cerca de 88 ms de atraso (margem de fase de 69° em 13,7 rad/s); para perder poucos graus de fase, convém ler a cada 10 a 20 ms. O teste a 10 ms mudou só 0,8 ponto percentual."

A margem de fase não aparece no Cap. 2. Se entrar, precisa de duas frases de fundamentação, com Ogata. A alternativa é falar só em "atraso tolerado", explicado em uma frase.

### 5. Laplace, função de transferência e polos são usados antes de definidos (Cap. 2)

**Onde aparecem antes:**
- a 2.6 usa $G(s)H(s)$;
- a 2.6.1 diz que "a função de transferência, os polos e o teorema do valor final" serão usados;
- a 2.6.2 usa polos.

**Onde são definidos:** a função de transferência só na 3.5.2 ("A função de transferência é a relação…", Ogata p. 13). O teorema do valor final e a equação característica, só na 3.5.4. A frase "a malha com o PI tem só dois polos" (fim da 2.6) aparece antes da definição de polo.

**O que fazer:** criar no início da 2.6 um parágrafo "Transformada de Laplace e função de transferência":
- derivada vira $s$, integral vira $1/s$;
- função de transferência = saída/entrada com condições iniciais nulas;
- denominador igual a zero = **equação característica**;
- **teorema do valor final**.

Na 3.5.2 e na 3.5.4 deixar só a remissão. Na 2.6, trocar a frase dos "dois polos" por uma remissão à 3.5.6.

---

## 🟡 Erros de definição e imprecisões de controle

6. **"O produto $K_c|K_g|$, o ganho de malha em regime, vale 2,2"** (3.5.5) e **"O ganho da malha… vale 2,2"** (4.2) estão errados para o PI. Com integrador, $L(0)$ é infinito, e é isso que zera o erro. **Reescrever:** "$K_c|K_g|$ = 2,2 é o ganho de malha do P (e da parcela proporcional do PI)". Usar "ganho **de** malha" nos dois lugares.
7. **"Com um integrador na malha, o erro… passa a ser nulo"** (2.6) é impreciso. O integrador precisa estar **no controlador**, antes do ponto onde a perturbação entra. A 3.5.4 já diz certo; corrigir a 2.6.
8. **"Estável para qualquer ganho positivo; o que limita o ganho é a velocidade da válvula"** (3.5.4 e Conclusão).
   - A estabilidade incondicional vem da idealização: sem atraso, sem sensor, sem mangueira.
   - O limite de velocidade não limita o ganho por estabilidade.
   - A remissão "(seção 3.8)" aponta para uma seção que não trata disso.
   - **Reescrever:** "no modelo linear idealizado…; na prática, o ganho é limitado por atrasos e dinâmicas não modelados, ruído e saturação de velocidade". Remeter à 3.8 corrigida pelo item 4.
9. **$t_s$ "±2% do valor final"** não faz sentido numa resposta de regulação, porque o valor final do desvio é zero.
   - O programa usa ±2% **do salto** em torno do valor final, e isso precisa estar escrito na 4.2.
   - Na 2.6.2, escrever $t_s \approx 4/(\zeta\omega_n)$, porque é uma aproximação pela envoltória.
   - Na 2.6.2, trocar "o $t_s$ calculado pelos polos continua valendo" por "continua valendo aproximadamente": deu 0,445 s, não 0,5 s.
   - Na Conclusão, "volta à faixa de ±2%" confunde com a faixa da norma; usar "se acomoda (critério de 2% do salto)".
10. **Item 1 da 3.5.6: o "chute" da derivativa está exagerado.** O número 2,7 é meu e eu o defendi mal.
    - O valor 330 kgf/cm²/s depende do passo de 1 ms.
    - O efeito real é um impulso de área $K_c T_d \Delta P$ ≈ 0,003, e a válvula, limitada em velocidade, mal se mexe.
    - O exemplo de Ogata (p. 541) é sobre degrau na **referência**.
    - **Reescrever:** o salto produz um impulso na derivada; na prática exigiria filtro e não traria ganho, porque o salto já passou quando a válvula reage. Dar o peso maior aos itens 2 a 4.
11. **"A derivativa não acrescenta polo"** (3.5.6, item 3) vale só para a derivada ideal $T_d s$. A derivada filtrada, que é a usada na prática, acrescenta um polo. Acrescentar essa ressalva entre parênteses.
12. **O windup por limite de velocidade não aparece na 2.7.2.** É a saturação dominante neste sistema: está ativa em toda troca e em 68% do tempo no C3. A 4.5 já mostra o efeito (de 8,3% para 3,2%). Uma frase na 2.7.2 resolve.
13. **A Eq. (2.13) e a 3.5.3 divergem.** A 2.7.2 diz que $s_k$ = 0 "quando o comando está no limite". O código congela só se o comando está no limite **e o erro pede para ir além**. Do jeito escrito, o integrador nunca sairia da saturação. Corrigir a 2.7.2.
14. **Item "O PI+FF tem os mesmos polos" (4.2 e Figura 21).** Falta citar o **zero duplo na origem** do PI+FF, que explica o undershoot maior e sustenta a correção do item 1.
15. **"O modelo linear acerta os polos"** (4.2) é circular, porque recalcular raízes da mesma função de transferência é conferência de código. O que valida é: o simulador sem limite coincide com a função de transferência (< 0,01 kgf/cm²) e acomoda em 0,44 s, como previsto.

---

## 🟡 Redação: confunde o leitor iniciante

16. **"Corrigido em cerca de 0,44 s" no C1 (4.5)** é resto da métrica "acomodação média", que saiu na v22 (critério de ±2% de $P_{ref}$). O leitor vai associar ao $t_s$ da Tabela 8, que mede outra coisa. Retirar o número, ou dizer "volta para perto de 3,5 kgf/cm² em menos de 1 s, antes da próxima troca".
17. **Conclusão, fechamentos triplos:** "leva cerca de 1 s para voltar". Pela 4.5 e pela 4.6 são cerca de 0,5 s fora da faixa por fechamento, e a válvula leva 0,7 s para chegar. Uniformizar.
18. **Termos duplos:**
    - "abertura de equilíbrio" e "abertura antecipada", que aparecem na 3.5.3 e no Quadro 2;
    - "perturbação" e "distúrbio" ($G_d$, "ganho do distúrbio", "bloco do distúrbio");
    - "ganho da malha" e "ganho de malha".

    Escolher um termo de cada par e dizer o sinônimo uma vez, na 2.6.
19. **Notação do FF:** a 2.7.1 usa $G_f = G_d/G_p$ e a 3.5.4 usa $F = -G_2/G_p$. Unificar como $G_f = -G_d/G_p$, explicando o sinal já na 2.7.1.
20. **Símbolos reaproveitados:**
    - $K$ é a constante do bico, a inclinação da reta na 2.6.1 e o ganho de malha na 3.5.4. Na 2.6.1 usar $m$; na 3.5.4 escrever $1/(1 + K_c|K_g|)$;
    - $\Delta P$ é queda de pressão na 2.4 e desvio na 3.5. Avisar na 3.5.2.
21. **Conceitos que surgem na metodologia ou nos resultados sem fundamentação:**
    - **diferença centrada** (3.5.2): incluir como 2.8.5, já que a 2.8 diz "os métodos usados";
    - **RMSE e $R^2$** (4.1): uma frase cada na 2.8.1;
    - **"atraso puro"** (4.6): definir em uma frase.
22. **3.5.2, "o sinal é positivo porque a curva da fonte desce":** o leitor acabou de ver −1,645. **Reescrever:** "como $dQ_s/dP$ é negativo, entra no denominador com o sinal trocado, +1,645".
23. **3.3.1, de $\Delta P$ para $P$ sem explicação.** Dizer que o bico descarrega para a atmosfera e que $P$ é manométrica, então a queda no bico é a própria $P$.
24. **H1, "escoamento permanente"**, parece contradizer o modelo dinâmico. Escrever "em cada instante, tratado como permanente (quase estático)", com remissão à H6.
25. **Parágrafo do ganho de malha na 2.6** é longo demais e mistura definição, interpretação, exemplo e duas citações. Dividir em dois. "Suponha que" vira "Considere-se que".

---

## 🟢 Polimento

- **Repetições:**
  - os motivos para não usar derivativa (2.6 e 3.5.6): na 2.6 basta uma frase de remissão;
  - $R_1$ = 5,58 em vez de 5,54 (3.3.1 e duas vezes na 4.1);
  - "oitenta vezes menor que $T_i$" (duas vezes).
- **Tabela 9:** o empate de IAE no C2 (0,83 e 0,83) está em negrito só no PI+FF.
- **Palavras informais:**

  | Trocar | Por |
  |---|---|
  | uns 4 m | cerca de 4 m |
  | pula direto | passa imediatamente |
  | grudam menos | aderem menos |
  | praticamente o tempo todo | de forma quase contínua |
  | bateria no limite | atingiria o limite |
  | Python, um software gratuito | a linguagem Python, gratuita |

- **Ambiguidades:**
  - "as três dão" depois de listar quatro equações → "todas dão";
  - "ganhos de até 10" → "$K_c$ de até 10 (kgf/cm²)⁻¹";
  - "passaria a ajudar mais do que ajudou aqui": o FF não ajudou → "poderia passar a trazer vantagem";
  - "a pressão muda o efeito inteiro do bico" → "a pressão varia $K_n\,\Delta N$".
- **"P exagerado fica instável" (2.6):** dizer que isso vale em geral, mas não nesta malha de primeira ordem (3.5.4).
- **Itens soltos:**
  - $\alpha_0$ aparece antes da 3.5.1;
  - a sigla XV das solenoides não é explicada;
  - o bloco "Alvo" da Figura 13 não é explicado;
  - $a_1$ aparece como −0,202 na 3.5.2 e como −0,2018 no resto: uniformizar.

---

## Plano de trabalho que eu cobraria

1. **Primeiro, os itens 1 a 4.** São reescritas de raciocínio, sem nova simulação. O item 1 muda a conclusão sobre o *feedforward*, então o Resumo e o Abstract também mudam.
2. **Item 5 (Laplace na 2.6), junto com os itens 6, 7, 8, 9 e 13.** São todos do Cap. 2 e da 3.5.
3. **Itens 10 a 12 e 14 a 15** (3.5.6, 2.7.2, 4.2).
4. **Redação, itens 16 a 25,** numa passada única com busca de termos.
5. **Polimento.**

**O que já está bom e não deve ser mexido:**
- a sequência 3.5.1 a 3.5.6 com o roteiro de 4 passos;
- a Tabela 3 como única dedução de $K_g$ e $K_n$;
- as Figuras 4, 5, 16, 21 e 22;
- a 2.8;
- a Tabela 9 com só duas métricas.

A estrutura está madura. O que falta é rigor no raciocínio de controle e disciplina de termos.
