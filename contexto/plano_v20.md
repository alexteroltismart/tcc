# Plano da versão 20 — simplificação moderada

Data: 09/11/2026. Base: `contexto/19.md`. Itens escolhidos pelo autor: **1, 3, 4 e 9** da conversa de simplificação, mais as correções do `relatorio_banca_19.md`.

## Como cada item foi entendido (confirmar)

| Item | O que entra | O que **não** muda |
|---|---|---|
| 1. Só o distúrbio na malha | Sai a referência como segunda entrada: $T_r(s)$, o zero do PI, os 10,7%, a soma das respostas e a Figura 19 | Funções de transferência dos bicos ($T_n$) para P, PI e PI+FF; sintonia; números do Cap. 4 |
| 3. $K_g$ de um jeito só | Fica a derivada implícita ($dP/dC$ → $K_g$ e $K_n$). Saem a diferença centrada e a Tabela 3; o método numérico vira uma frase de conferência | Valores −2,66 e −0,323; a explicação de por que não dependem de $n$ |
| 4. Introdução mais curta | Só o **Cap. 1**: Revolução Verde, INCA e ODS num parágrafo; lista de super e subdosagem em frase; 1.3 e 1.4 sem repetir a 3.2 e o Quadro 1 | **Cap. 2 inteiro**: texto, dedução da lei de orifício, válvula agulha e Figuras 1–3 |
| 9. Menos métricas | Sai o IAE (Eq. 3.41, coluna da Tabela 10, sigla, linha do Quadro 5). A acomodação fica só no C1 e no C2, como hoje | Tempo fora da faixa, desvio máximo e acomodação |

**Não escolhidos, ficam como estão:**
- o *feedforward* (item 2), que fica inteiro como terceira configuração;
- as fotos da bancada (item 5);
- a seção 3.7 do programa (item 6);
- a validação com a Tabela 6, a Figura 16 e a validação cruzada (item 7);
- os testes à parte (item 8).

Ganho estimado: **~2.000 a 2.300 palavras (~11–12% do corpo)**, 7 equações, 1 tabela e 1 figura. Isso é menos que os ~6.000 da versão "forte", porque os itens 2, 5, 6, 7 e 8 ficam.

---

## Base bibliográfica da reescrita: Ogata e Castrucci

O autor pediu que a reescrita da parte de controle se apoie em **Ogata (2010)** e em **Castrucci, Bittar e Sales (2018)**, e cite os dois.

- **Arquivo:** `referencias base/castrucci.epub`. O texto foi extraído para `referencias base/Castrucci_2018_Controle_Automatico.md`, para busca.
- **Referência:** CASTRUCCI, P. L.; BITTAR, A.; SALES, R. M. **Controle automático**. 2. ed. Rio de Janeiro: LTC, 2018. *E-book*. Conferir a cidade na página de créditos.
- **Sem páginas:** o epub não tem marcação de página. A citação vai por seção, por exemplo "(CASTRUCCI; BITTAR; SALES, 2018, seção 3.11.3)". Se o autor tiver o livro impresso, troca-se depois pela página.
- **Equações em imagem:** antes de citar uma fórmula, abrir a imagem no epub e conferir.
- **Regra:** só citar uma afirmação depois de ler o trecho no livro. Nenhuma citação "de memória".

| Trecho do TCC | Ogata (2010) | Castrucci et al. (2018) |
|---|---|---|
| 2.6: malha fechada, PID, P/I/D | p. 2–3, 21 (já citado) | seções 1.2 e 6.2 |
| Eq. 2.9, erro do P com perturbação | p. 198 (valor final) | **seção 3.11.3**, perturbação em degrau e referência nula (Tabela 3.4) |
| 2.6.1: 2ª ordem, $M_p$, $t_s$ | p. 151–157 (já citado) | seções 3.5 e 3.6 |
| 3.5.6: alocação de polos | p. 522, 658 | **seção 8.2**, imposição arbitrária de polos |
| 2.7.1: *feedforward* | — | **seções 7.8 e 7.8.1**. Pode substituir Liu et al. (2018), cuja referência ainda está incompleta. Decidir. |
| 2.7.2: *windup* | — | seção 6.3.4. Explica o *windup* e usa outra técnica, a realimentação externa. A integração condicional continua com Fernandes e Goldemberg (2001). |
| 3.4.2: válvula de 1ª ordem | p. 147 | seção 3.4 |
| 3.5.4: linearização; limite de velocidade | — | seções 9.10.1 e 9.10.2 |
| 3.5.5: diagrama de blocos; valor final | p. 22, 198 | seções 2.6 e 2.3.4 |
| 3.8: leitura discreta real | — | seções 12.2.1 (retangular) e 12.6 (período de amostragem) |

A 3.11.3 do Castrucci justifica o item 1 do plano: o livro analisa o erro estacionário "com perturbação em degrau e referência nula", que é o caso deste trabalho.

## Etapa 1 — Script (`simulacao/modelo_barra.py`)

1. Guardar o script e os resultados da v19 em `simulacao/v19/`.
2. **Item 1:**
   - tirar `superposicao`, `fig_superposicao`, as constantes `D_REF`/`T_REF` e a chave `superposicao` do JSON;
   - em `modelo_linear`/`resposta_linear`, tirar o ramo da referência (`d_ref`, $T_r$);
   - a conferência do denominador fica só para $T_n$;
   - sai a conferência "soma = resposta conjunta".
3. **Item 3:** `ganho_kg` (diferença centrada) continua no programa, mas só como conferência de `derivada_dp_dc` (diferença < 0,1%). Não sai mais tabela dela.
4. **Item 9:** `metricas` pode continuar gravando o IAE no JSON, porque não atrapalha. No texto ele some.
5. Rodar e conferir que `cenarios` e `varredura_w_max` são **idênticos** aos da v19. Nenhum número do Cap. 4 deve mudar.
6. Regerar a Figura 13 (`build/fig/fig12_freq.py`) sem a entrada $\Delta P_{ref}$: só o distúrbio $\Delta N$, o *feedforward* e a realimentação direta.

## Etapa 2 — Texto (`contexto/20.md`)

**Item 1, referência como entrada:**
- 2.6: sai o parágrafo "Duas entradas ao mesmo tempo" (l. 320) e a citação de Ogata sobre superposição.
- 2.6.1: sai o último parágrafo sobre o zero (l. 397). Fica uma frase: "a válvula tem limite de velocidade, então o resultado precisa ser conferido numericamente (seção 4.2)".
- 3.5.4: sai "a malha passa a ter duas entradas" (l. 834) e $\Delta P_{ref}$ da lista de desvios.
- 3.5.5:
  - novo título, "Malha fechada com os bicos como distúrbio";
  - a Eq. (3.25) fica sem $\Delta P_{ref}$;
  - saem $T_r$, $T_{r,P}$ e $T_{r,PI}$ (atuais 3.27–3.29), a soma (3.34) e o erro (3.35);
  - em "O que as funções de transferência mostram" saem o item do zero e o valor final da referência;
  - ficam os polos comuns, o erro do P, o PI zerando o erro e a equação característica. A identificação de $\zeta$ e $\omega_n$ passa a ser feita só na 3.5.6, junto com o item A1 do relatório.
- 3.5.6: sai a frase "os polos valem para as duas entradas; o que muda são os zeros" (l. 1033).
- 4.2:
  - sai a parte "Referência e bicos, separados e somados" (l. 1432–1462) e a Figura 19;
  - os polos refeitos (l. 1412–1420) ficam numa frase (item A2 do relatório).
- Resumo e Abstract: sai a oração da superposição (R6).
- Conclusão: saem as frases das duas entradas, dos 69% e dos 10,7% (l. 1563).
- Lista de Símbolos: saem $T_r$ e $\Delta P_{ref}$. $T_n$ fica, com a descrição "resposta da pressão ao número de bicos".

**Item 3, $K_g$ pela derivada implícita:**
- A dedução de $dP/dC$, $K_g$ e $K_n$ (hoje na 3.5.4, l. 836–884) **sobe para a 3.5.2**, que passa a se chamar "Ganho da planta e ganho do distúrbio". A 3.5.4 fica só com o ponto de operação, a planta linear (3.22) e a válvula (3.23).
- Saem a fórmula geral da diferença centrada, a Eq. (3.15) e a Tabela 3. Fica uma frase: "O programa confere o valor por diferença centrada, abrindo e fechando a válvula 0,005 no modelo estático (diferença menor que 0,1%)."
- "Não depende de $n$" fica explicado uma vez só, na 3.5.2. Na 4.2, l. 1388, sobra uma remissão.
- Ajustar o Quadro 1 (etapa 4: "derivada implícita"), a Tabela 4 (origem de $K_g$) e o Quadro 2 (`ganho_kg` → conferência).

**Item 4, Cap. 1:**
- l. 132: Revolução Verde, INCA, deriva e ODS num parágrafo de 2–3 frases.
- l. 162–167: a lista de super e subdosagem vira uma frase.
- l. 171–178: os três parágrafos sobre a bancada e o atuador viram um, porque o detalhe está na 3.2 e na 2.3.
- l. 182 (1.4): uma frase que remete ao Quadro 1.

**Item 9, métricas:**
- 3.6.4: sai o item do IAE e a Eq. (3.41).
- Tabela 10: sai a coluna IAE.
- 4.6: sai "IAE 10% maior" (fica a acomodação, 0,48 × 0,44 s).
- Quadro 2 (`metricas`) e Quadro 5: sai a linha do IAE, e o título vira "Cálculo do tempo fora da faixa".
- Lista de Siglas: sai IAE.

**Correções do relatório da v19:**
- E1 ("ganho-limite"), E3 (parágrafo colado na 2.6; conferir Ogata p. 201–202), E4, E5, E7, R1 (2º objetivo na Conclusão), R2 ("sem limite de ganho" uma vez só), R3 (3.8 ligada ao teste de 10 ms) e R4 (conta da rampa para justificar $t_s$).
- **E6** (cores da Figura 19) deixa de existir, porque a figura sai.
- **E2** (ruído comparado com $K_c$ = 0,33): **decidir**. Ou se refaz o `testes_avulsos.py` comparando com o mesmo PI sem ruído (~5 min), ou o número sai e fica só "a válvula se move mais".

## Etapa 3 — Numeração

Cap. 3 passa de 41 para 34 equações:

| Antiga | Nova | | Antiga | Nova |
|---|---|---|---|---|
| 3.15 (diferença centrada) | — | | 3.30 $T_n$ | 3.26 |
| 3.16 $\alpha_c$ | 3.18 | | 3.31 $T_{n,P}$ | 3.27 |
| 3.17 $I_k$ | 3.19 | | 3.32 $T_{n,PI}$ | 3.28 |
| 3.18 $\alpha_{c,k}$ | 3.20 | | 3.33 $T_{n,PI+FF}$ | 3.29 |
| 3.19 $dP/dC$ | 3.15 | | 3.34, 3.35 | — |
| 3.20 $K_g$ | 3.16 | | 3.36 $\omega_n$ | 3.30 |
| 3.21 $K_n$ | 3.17 | | 3.37 $K_c$ | 3.31 |
| 3.22 planta | 3.21 | | 3.38 $T_i$ | 3.32 |
| 3.23 válvula | 3.22 | | 3.39 faixa | 3.33 |
| 3.24 $G_c$ | 3.23 | | 3.40 fora | 3.34 |
| 3.25 $\Delta A_c$ | 3.24 | | 3.41 IAE | — |
| 3.26 malha | 3.25 | | 3.27–3.29 $T_r$ | — |

- **Tabelas:** sai a 3. As Tabelas 4–10 viram 3–9, e a "Tabela 10" dos resultados vira **Tabela 9**.
- **Figuras:** sai a 19. As Figuras 20–22 viram 19–21.
- **Comentários do script:** os números de equação no `modelo_barra.py` também mudam (Quadros 3–5 e Apêndice A).
- **Conferência final:** `grep` de "Equação (3.", "Tabela " e "Figura " no 20.md inteiro e no script.

## Etapa 4 — Fechamento

1. Copiar o script para o Apêndice A.
2. Escrever a nota A20 nas NOTAS DE REVISÃO.
3. Atualizar o `CLAUDE.md`: a malha passa a ter uma entrada, o distúrbio, e saem a conferência de superposição e o IAE.
4. Gerar `docs/20.docx` e `docs/20.pdf` (md2docx + post.ps1), conferir o número de páginas e olhar a 3.5 no PDF.
5. **Depois, numa etapa separada:**
   - deck: o slide 13 "referência e bicos somados" vira "malha com o distúrbio", e as citações de "Tabela 10" e da Tabela 3 mudam;
   - roteiro de 15 min: sai a pergunta dos 10,7%;
   - roteiro de estudo, a partir da v20.

## Decisões pendentes

1. O item 4 é **só o Cap. 1**, com o Cap. 2 intacto. Foi assim que entendi "manter as fotos e o texto do cap 2".
2. O *feedforward* fica inteiro, porque o item 2 não foi escolhido.
3. E2 (ruído): refazer o teste ou tirar o número?
4. A acomodação fica no C1 e no C2. Sai só o IAE.
5. Na 2.7.1, trocar Liu et al. (2018) pelo Castrucci, ou citar os dois?
6. Citar o Castrucci por seção, porque o epub não tem páginas. Você tem o livro impresso?
