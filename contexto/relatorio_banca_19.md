# Relatório de banca — versão 19

Data: 09/11/2026. Base: `contexto/19.md` (PDF de 101 p.). As linhas citadas são as do 19.md nesta data.
Nenhuma alteração foi feita no texto.

Tamanho do corpo, contando só a prosa (sem equações exibidas e sem blocos de código):

| Parte | Palavras |
|---|---|
| Cap. 1 | 1.240 |
| Cap. 2 | 3.500 |
| 3.1–3.4 (bancada, modelos) | 3.620 |
| 3.5 (controle, Laplace, sintonia) | 3.570 |
| 3.6–3.8 (simulação, programa, limitações) | 2.110 |
| Cap. 4 | 3.770 |
| Cap. 5 | 900 |
| **Corpo** | **~18.700** |

A v18 acrescentou a análise em Laplace com duas entradas: a seção 3.5.5 sozinha tem 1.375 palavras e cerca de 20 equações exibidas. Ela é hoje a maior seção do trabalho. Quase nada do relatório de cortes da v17 foi aplicado, e os itens que ainda valem foram trazidos para cá.

---

## 1. Parecer geral

O trabalho está coerente com a decisão da v19: o controlador lê a pressão a cada 1 ms, e a explicação de por que o *feedforward* perdeu a vantagem (4.6) é clara e honesta. A conclusão "confirmada em parte, só em simulação" está bem sustentada.

A banca deve concentrar as perguntas em três pontos:
1. **O veredito sobre o *feedforward* depende da idealização do sensor.** Com leitura em tempo real e pressão instantânea (H6), o PI reage no mesmo milissegundo da troca, e o *feedforward* não tem o que adiantar. Na v18, com leitura a cada 50 ms, o *feedforward* ganhava no C2. O texto precisa deixar claro que o resultado vale para um controlador rápido em relação à válvula (ver R3).
2. **A especificação $t_s$ = 0,5 s não considera o limite de velocidade da válvula.** O texto mostra que esse limite define o tempo de resposta (4.2), mas não diz para quais trocas os 0,5 s são possíveis. Uma conta de uma linha explica por que o C1 acomoda em 0,44 s e o C2 em 1,02 s (ver R5).
3. **O C3 continua com uma única semente.** A diferença entre o PI e o PI+FF (8,3% × 9,5%) é de 1,2 ponto. Na revisão da v10, com 10 sementes, a variação entre sementes era muito maior que isso. Esse item continua pendente desde a v10.

---

## 2. Erros e inconsistências (corrigir antes da entrega)

🔴 **E1. Sobra do $K_{c,lim}$ na 3.8 (l. 1287).** "Os resultados dinâmicos, os ganhos e o **ganho-limite** dependem deles." O ganho-limite saiu na v19. Trocar por "Os resultados dinâmicos e os ganhos dependem deles."

🔴 **E2. Ruído comparado com um controlador que não existe no texto (l. 360 e l. 1289).** "a válvula se moveu de 2,0 a 2,2 vezes mais do que com um PI de ganho 2,5 vezes menor ($K_c$ = 0,33)". O $K_c$ = 0,33 é a sintonia antiga da v09, e o `testes_avulsos.py` ainda compara com ela (`("Kc 0,33", 0.334, 0.2)`). Um leitor não tem como saber de onde vem esse controlador. Duas saídas:
- **(a) recomendada:** refazer o teste comparando o PI com ruído com o mesmo PI sem ruído, e escrever "a válvula se moveu X vezes mais do que sem ruído". Isso exige rodar de novo o `testes_avulsos.py` (cerca de 5 min);
- **(b)** manter a comparação, mas dizer que o segundo controlador é um PI com $t_s$ maior, calculado pela Equação (3.37). Hoje ele não é, porque $T_i$ = 0,2 não sai da (3.38) com o mesmo $\zeta$.

🔴 **E3. Parágrafo colado à lista na 2.6 (l. 361–362).** Falta uma linha em branco antes de "Além disso", e o parágrafo vira parte do último item da lista no PDF. A frase também termina com "o outro motivo depende da sintonia e está na seção 3.5.6", que não diz qual é o motivo. Sugestão:
> Além disso, a malha com o PI tem só dois polos, e $K_c$ e $T_i$ bastam para colocá-los onde se quer (seção 3.5.6).

A afirmação "a pressão não tem inércia própria, que é o que a ação derivativa ajuda a amortecer (OGATA, 2010, p. 201–202)" precisa ser conferida no livro. Se a página não disser isso, a frase sai.

🟡 **E4. "A malha simulada não tem outro limite de estabilidade" (l. 1029).** O simulador também é discreto (Euler, passo de 1 ms), então a afirmação vale para a malha **linear**, não para a simulada. Trocar "a malha simulada" por "a malha linear".

🟡 **E5. "O controlador já é contínuo" (l. 824).** Ele atualiza a cada 1 ms. Sugestão: "O controlador pode ser tratado como contínuo, porque atualiza o comando a cada 1 ms, um tempo duzentas vezes menor que $\tau_a$."

🟡 **E6. Cores da Figura 19 em conflito com as Figuras 18 e 20–22.** Nas outras figuras, verde é o P e laranja é o PI. Na Figura 19, verde é "só o bico" e laranja é "só a referência" (`fig_superposicao`, `color=COR["P"]` e `COR["PI"]`). A frase "o PI+FF passa mais da referência que o PI (curva verde do gráfico de baixo)" (l. 1462) parece falar do controlador P. Melhor trocar as cores da Figura 19 (por exemplo, roxo e marrom) e escrever "curva da resposta ao bico".

🟢 **E7. Detalhes de forma:**
- l. 1054: "Os ganhos da Equação (3.37) e (3.38)" → "das Equações (3.37) e (3.38)";
- l. 1060: "*Etapa 6.*" está sozinha numa linha. Juntar a uma frase, como nas outras seções ("*Etapa 6.* Esta seção descreve…");
- l. 1551, "No campo": usa o PI+FF como exemplo, mas o controlador que o trabalho recomenda é o PI. Os dois dão 6,8% no C2, então basta escrever "do PI";
- Resumo e Abstract: "empatou com o PI nas trocas espaçadas". No C1 o PI+FF acomodou mais devagar (0,48 × 0,44 s). Escrever "empatou no tempo fora da faixa".

🟢 **E8. Marcas de rascunho que ainda estão no texto:** [ANO DA DEFESA] (2×), ficha catalográfica, folha de aprovação, Holterman "[A CONFERIR …1997…]" nas Referências, e o volume e as páginas de Liu et al. Ainda não há marca `[REF. PENDENTE]` no corpo.

---

## 3. Reescritas recomendadas (clareza e argumento)

**R1. Conclusão, segundo objetivo (l. 1561).** O parágrafo só fala da H6 e não diz o que se aprendeu sobre a válvula, que é o principal resultado dinâmico. Sugestão:
> O segundo objetivo era acrescentar a dinâmica da válvula. A pressão pôde ser tratada como instantânea: com o armazenamento de líquido na mangueira, o tempo fora da faixa mudou no máximo 0,4 ponto percentual. A dinâmica que importa é a da válvula, e o limite de velocidade dela é o que define o tempo de correção em todos os controladores. Como $\tau_a$ e $\omega_{max}$ foram estimados, esse é o resultado que mais depende de medição.

**R2. "Sem limite de ganho" dito seis vezes.** Aparece na l. 824, l. 916, l. 1029, l. 1054 (parágrafo inteiro), l. 1288, l. 1430 e na Conclusão (l. 1563). Ficar com a l. 1029 (com a correção de E4) e com a 3.8. Nas outras, cortar ou reduzir a uma oração.

**R3. A 3.8 deve ligar a leitura em tempo real ao teste de 10 ms que já existe.** Hoje a limitação diz só que "intervalos grandes trariam atraso". A 4.2 (l. 1466) já tem um dado sobre isso: com o controlador lendo a cada 10 ms, o PI mudou 0,8 ponto. Sugestão para a l. 1288:
> Um controlador digital real lê o sensor a intervalos fixos. Num teste com leitura a cada 10 ms (seção 4.2), o tempo fora da faixa do PI mudou 0,8 ponto percentual; intervalos maiores, perto de $\tau_a$, trariam atraso e um ganho máximo de estabilidade. Com o PI reagindo mais tarde, o *feedforward* poderia recuperar parte da vantagem que não teve aqui (seção 4.6).

A última frase responde à primeira pergunta da banca sem reintroduzir a amostragem na simulação. Fica a critério do autor.

**R4. Por que $t_s$ = 0,5 s (3.5.6, l. 1038).** A justificativa atual fala da válvula livre (0,8 s), mas não do limite de velocidade. Basta uma conta com números que o texto já tem:
> Com $\omega_{max}$ = 0,5 s⁻¹, a válvula leva 0,121/0,5 ≈ 0,24 s para compensar um bico, dentro dos 0,5 s; para três bicos de uma vez, a mudança é de 0,36, e só a rampa leva 0,73 s. Por isso a especificação pode ser cumprida nas trocas de um bico, mas não nos fechamentos triplos (seção 4.5).

Isso liga a sintonia aos resultados do C1 (0,44 s) e do C2 (1,02 s).

**R5. 2.6, ruído.** Depois de corrigir E2, a frase da l. 360 fica melhor com um número só e a remissão: "um ruído de 1% a 2% na leitura já faz a válvula se mover cerca de X vezes mais (seção 3.8)".

**R6. Resumo e Abstract (416 e 421 palavras, abaixo do limite de 500).** A frase dos ganhos por superposição ("…escrita com a referência e o número de bicos como entradas separadas, somadas por superposição") é a mais difícil do Resumo e não traz resultado. Sugestão: "…os ganhos saíram da função de transferência da malha." (−20 palavras). A frase do *feedforward* pode ficar com a causa: "A compensação antecipativa não trouxe ganho, porque o PI já reage no instante da troca e a válvula, limitada em velocidade, é a mesma nos dois casos."

---

## 4. Cortes

### A. Risco baixo (podem ser aplicados direto)

Nenhum corte retira equação numerada, então a numeração não muda.

**Cap. 3, controle (novo na v18/v19, maior ganho)**
1. **$\zeta$ e $\omega_n$ identificados duas vezes** (l. 1015–1027, no fim da 3.5.5, e l. 1044–1050, na 3.5.6). Deixar a comparação com a forma padrão só na 3.5.6. Na 3.5.5, a equação característica fica, e o texto remete à 3.5.6 (~90 palavras e 3 equações sem número).
2. **Polos do PI refeitos na 4.2** (l. 1412–1420): é a conta da Tabela 9 de trás para frente, e o próprio texto diz isso. Uma frase com os polos −8,0 ± j8,2 basta (~110).
3. **"$K_g$ não depende de $n$" explicado três vezes**: na 3.5.2 (l. 779), na 3.5.4 (l. 884) e na 4.2 (l. 1388). Manter a explicação física na 3.5.4, que é a que tem a conta, e deixar uma frase na 3.5.2 (~120).
4. **Diferença centrada genérica** (l. 759–763): ir direto à Equação (3.15) sem a fórmula geral com $O(h^2)$ (~60).
5. **"Sem limite de ganho"**: ver R2 (~120).

**Cap. 3, bancada, modelo e programa (itens da v17 que continuam valendo)**

6. **Bancada e HV apresentadas quatro vezes** (l. 465–471, legendas das Figuras 6–8 em l. 489, 497 e 505, l. 522). Virar a lista da l. 465 em frase e tirar a repetição das legendas (~150).
7. **Balanço no nó** (l. 526, 590–600, 657): ficar com a l. 597 e com a abertura da 3.3.4, e reduzir a lista da Figura 11 a uma frase (~110).
8. **Laço da simulação em três lugares**: lista da 3.6.2 (l. 1087–1093), Figura 15 e Quadro 4. Trocar a lista por uma frase que remete à Figura 15 (~90).
9. **3.7.3** (l. 1270–1278): de 8 itens para um parágrafo curto, porque cada conferência já é citada onde o número aparece (~80).
10. **Bissecção** (l. 679): reduzir a uma frase (~50).
11. **"Ressalva" dos 6,10 kgf/cm²** (l. 1384): o assunto já está na l. 544. Virar um parêntese ali (~45).

**Cap. 1 e 2**

12. **1.3, últimos parágrafos** (l. 171–178): repetem a 3.2 e os trabalhos futuros (~165).
13. **1.4** (l. 182): repete o Quadro 1. Uma frase basta (~80).
14. **Bancada no Cap. 2** (l. 219, 221, 291, 293): bomba, PCV, HV e perda na tubulação voltam na 3.2 e na H2. Manter os 0,92 L/min, que agora são usados na 4.1 (~120).
15. **Pressão → dose → gota** (l. 134, 162–167, 190, 297): a ligação aparece quatro vezes. Ficar com a da 1.3 e a da 2.5 (~100).
16. **Listas da 2.6** (l. 312–318, 352–356): viram frases (~120).

**Cap. 4 e 5**

17. **4.5 e Conclusão relendo a Tabela 10** (l. 1531–1534 e l. 1569–1571): tirar da Conclusão os números entre parênteses que já estão no Cap. 4 (~150).
18. **Legendas em prosa** (l. 1332, l. 1364, l. 1497–1500): manter só as cores, que o texto cita (~60).
19. **Trabalhos futuros** (l. 1578–1579): juntar os dois itens de medição (~25).

**Total do bloco A: cerca de 1.850 palavras (~10% do corpo).**

### B. Dependem de decisão do autor

| # | Trecho | Ganho | Por que perguntar |
|---|---|---|---|
| B1 | **Passo a passo das funções de transferência** (3.5.5, l. 942–980): cada controlador repete "multiplicando o numerador e o denominador por…" | ~250 | O autor pediu o passo a passo (v15 e v18). A proposta faz a conta uma vez para o PI e dá o P como caso $T_i \to \infty$. As Eqs. 3.27–3.33 ficam. |
| B2 | **$K_g$ calculado de dois jeitos**: Tabela 3, por diferença centrada (3.5.2), e Eq. (3.20), por derivada implícita (3.5.4) | ~200 | Um dos dois pode virar só conferência ("o programa confere pelos dois métodos"). A Tabela 3 é citada no deck e no roteiro. |
| B3 | **Exemplo numérico do PI** (l. 801–809) | ~100 | Foi refeito na v19 para explicar $T_i$. A proposta mantém a última frase ("depois de $T_i$, a parcela integral iguala a proporcional") e tira as três contas. |
| B4 | **Quadros 3 e 5** (código de `p_regime` e `metricas`) | ~200 | Copiam o Apêndice A. A 3.7 continuaria com o Quadro 4 e a Figura 15. |
| B5 | **ISO 16122-2, item 4.8.8** (l. 302–304) | ~55 | Nada depois o usa, mas a nota A15 o manteve como comparação. |
| B6 | **Leitura dos valores finais da Figura 19** (l. 1455–1460) | ~100 | Confirma o teorema do valor final com números, o que já foi feito para o P na l. 1410. Pode virar uma frase. |

**Total do bloco B: até ~900 palavras.**

---

## 5. Ordem sugerida

1. **v20, correções:** E1–E8, R1–R6 e o bloco A. Os números do Cap. 4 não mudam, a não ser em E2, que pede rodar de novo o `testes_avulsos.py` com a comparação "com ruído × sem ruído".
2. Decidir B1–B6.
3. Pendências antigas, se houver tempo: C3 com várias sementes (desde a v10) e as referências (Holterman, Liu).
4. Depois da v20: atualizar o roteiro de estudo (`docs/Roteiro_Explicacao_TCC_v17.md`, ainda com ZN e amostragem) e conferir se o deck cita a Tabela 3 ou o "ruído 2×".
