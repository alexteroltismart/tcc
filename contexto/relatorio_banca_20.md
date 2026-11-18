# Relatório de banca simulada — versão 20

Data: 11/11/2026. Base: `contexto/20.md` (PDF de 98 p.). As linhas citadas são as do 20.md nesta data. Nenhuma alteração foi feita no texto.

A banca teve três avaliadores independentes, que leram o trabalho sem ver o parecer uns dos outros:

| Avaliador | Foco |
|---|---|
| A | Controle e modelagem dinâmica |
| B | Máquinas agrícolas, tecnologia de aplicação e hidráulica |
| C | Forma, redação, estrutura e ABNT. Não repetiu o `relatorio_redacao_coerencia_20.md`. |

As afirmações mais graves foram conferidas depois por mim. A marca **[conferido]** indica uma conta, um script ou um livro checado. A marca **[suspeita]** indica um ponto que depende de interpretação.

---

## 1. Notas

| Critério | A (controle) | B (hidráulica) | C (forma) |
|---|---|---|---|
| Fundamentação / estrutura | 8,0 | 8,5 | 7,5 |
| Metodologia e rigor / redação | 6,5 | 7,5 | 8,0 |
| Resultados e análise / ABNT | 6,0 | 8,0 | 6,5 |
| Conclusões / referências | 6,5 | 7,5 | 6,0 |
| **Nota do avaliador** | **7,0** | **8,0** | **7,3** |

**Nota da banca: 7,4.** O trabalho está aprovado, e as notas convergem. Os três avaliadores dizem que, com as correções 🔴 aplicadas, a nota passaria a ficar entre 8,5 e 9.

O que a banca elogiou:
- As contas estão certas. Os avaliadores refizeram Kg, Kn, Kc, Ti, os polos, o erro do P, os saltos em malha aberta, K, Qs, α_ff, as rampas e a conversão de 15 km/h, e tudo bate com o texto e com o script.
- Os números estão coerentes entre o Resumo, o Cap. 4 e a Conclusão.
- As 24 citações batem com as 24 referências da lista, sem sobras nem faltas.
- O texto é didático, com voz de aluno adequada.
- A conclusão "confirmada em parte, só em simulação" é honesta.

---

## 2. Parecer geral

O modelo e as contas estão sólidos. Os problemas estão na **interpretação** dos resultados de controle e na **ponte com o campo**. A banca deve concentrar a arguição em quatro pontos:

1. **A explicação do *feedforward* está errada.** O texto atribui a piora do FF no C3 à velocidade da válvula, mas ela vem do anti-windup só por posição. Com o anti-windup também na velocidade, os dois controladores empatam (A-P1). O Exemplo 7.4 de Castrucci também é usado ao contrário (A-P2).
2. **O projeto linear não vale nem para um bico.** A parcela P do controlador já pede mais velocidade do que a válvula tem (A-P3). Além disso, a métrica de acomodação não é a mesma da especificação de 0,5 s (A-P4).
3. **A válvula não foi identificada.** Kv,max = 3,5 aparece como "escolha de projeto", e a Tabela 2 de Rosa sugere uma válvula com bem mais autoridade. A frase "uma única sintonia serve" depende da H5 (B-P1, A-P6).
4. **Hipótese e conclusão.** A hipótese não tem critério de aceitação (C-F2). A ISO 4.5.4 foi citada pela metade (B-P2). A métrica de área fora da faixa está errada (B-P3).

---

## 3. Erros e inconsistências (corrigir antes da entrega)

🔴 **E1. A causa da piora do FF é o anti-windup, não a velocidade da válvula (l. 1469–1474, 1496 e Resumo).** **[conferido]** Rodei `simulacao/teste_antiwindup.py`:

| Anti-windup | C2 PI | C2 PI+FF | C3 PI | C3 PI+FF |
|---|---|---|---|---|
| só posição (texto) | 6,8% / 1,02 s | 6,8% / 1,02 s | 8,3% | 9,5% |
| posição + velocidade | 6,8% / 0,68 s | 6,8% / 0,68 s | **3,2%** | **3,1%** |
| nenhum | 17,8% | 19,3% | 29,1% | 32,7% |

A seção 4.5 (l. 1461) já cita o 3,2% do PI. Só que a 4.6 e a Conclusão continuam dizendo "a causa é a velocidade da válvula", e nenhuma delas diz que, com o anti-windup estendido, o PI+FF empata com o PI no C3. O FF passa mais tempo na velocidade máxima (cerca de 75% contra 68%, segundo o avaliador A) e por isso acumula mais *windup*.

O Castrucci (6.3.4) trata o *windup* para a saturação de qualquer elemento do atuador, o que inclui a velocidade. Portanto, restringir o anti-windup à posição foi uma escolha do trabalho, e não uma limitação das referências.

Saídas:
- **(a) recomendada:** reescrever a 4.6 e o item da Conclusão. A piora do FF no C3 vem do *windup* durante a rampa. Com o anti-windup também na velocidade, os dois ficam iguais (3,2% e 3,1%), e o FF continua sem vantagem.
- **(b)** adotar o anti-windup posição + velocidade como caso principal. Isso muda a Tabela 10, as Figuras 19–21, o Resumo e a Conclusão.

🔴 **E2. O Exemplo 7.4 de Castrucci é usado ao contrário, e a explicação ignora o modelo linear (l. 929, 1469).**
- **Exemplo 7.4.** O livro diz que, **sem** atraso puro, o FF traz "apreciável melhora". O texto usa a ausência de atraso como argumento contra o FF. Isso foi conferido pelo avaliador A no livro e precisa ser revisto por você no epub.
- **Modelo linear.** O avaliador A calculou com as Eqs. 3.28 e 3.29, sem limite de velocidade, para um bico fechando:
  - IAE: 0,0260 no PI e 0,0272 no PI+FF;
  - subsinal: −0,034 no PI e −0,068 no PI+FF (o dobro).

  Ou seja, o FF já não ajuda no modelo linear. Pela H6, o salto é instantâneo, e a parcela P sozinha já pede Kc·|Kn| ≈ 0,27 de abertura, mais que os 0,121 necessários. Somar o FF faz o comando passar do ponto.
- **"Compensador ideal" (l. 929).** O FF estático não é o ideal de 7.8.1. O ideal seria −(Kn/Kg)(τa·s + 1), que é impróprio. O texto deve dizer "a versão estática (ganho) do compensador ideal".

🔴 **E3. "Todos os números do Capítulo 4 vêm dessa execução" é falso (l. 1120, l. 1261).** **[conferido]** Vários números vêm de testes à parte, fora do Apêndice A:
- o teste da H6 com mangueira (0,4 p.p.);
- os passos de 2 e 10 ms;
- o anti-windup estendido (3,2%, 0,68 s, 29%).

O teste da H6 também não tem método escrito: faltam V, β, C_h e τ_h (C-F1, B-P9). Pelas notas da v07, C_h = 0,5 mL/(kgf/cm²) e τ_h ≈ 12 ms.

Correção:
- acrescentar em 3.6.3 um parágrafo "Testes complementares", com parâmetros e nomes dos scripts;
- trocar a l. 1261 por "…exceto os testes complementares da seção 3.6.3".

🔴 **E4. A hipótese não tem critério de aceitação (l. 144, 1500).** A hipótese diz que o modelo "é suficiente para projetar", mas o controlador é avaliado no mesmo modelo. Também não diz quanto tempo fora da faixa confirma ou refuta, e por isso o "confirmada em parte" fica arbitrário.

O avaliador C propõe uma reescrita que torna a resposta objetiva (confirmada no C1, não confirmada no C2 e no C3):

> **Hipótese:** em simulação, um controlador PI sintonizado por alocação de polos sobre um modelo de resistências fluídicas da barra (bicos em paralelo, curva da fonte e válvula de alívio com curso e velocidade limitados) mantém a pressão dentro de ±10% da referência (ISO 16122-2, item 4.5.4) durante a abertura e o fechamento de bicos. Considera-se a hipótese confirmada em um cenário quando o tempo fora da faixa é nulo.

Ver também E8: o C1 dá 0% até com controle fraco.

🔴 **E5. ISO 16122-2, item 4.5.4, citado pela metade (l. 289).** **[conferido no texto; a íntegra foi lida pelo avaliador B na BS EN em `referencias base/`]** O item também diz "…and shall return within 10 s to the original working pressure ±10% after the sprayer has been switched off and on again". Esse ponto foi levantado na banca da v10 e adiado.

Correção:
- citar o item inteiro;
- dizer que "cada instante fora da faixa" é um critério do autor, **mais severo** que o da norma;
- acrescentar uma frase dizendo que, pelo critério da norma, o PI e o PI+FF atendem todos os cenários, e o P reprova a partir de 3 bicos.

Opcional: citar o 4.8.9 (queda de pressão ≤ 10% ao longo da barra), que dá base normativa à H2.

🔴 **E6. Pré-texto e referências com marca de rascunho (C-F3, F4).**
- Restam [ANO DA DEFESA] (l. 10 e 25), a ficha catalográfica com "[SEMESTRE] de [ANO]" e "OBS: Gerar Ficha…", e a folha de aprovação em modelo.
- No PDF, a folha de aprovação vem **antes** da ficha. Pela NBR 14724, a ficha vem no verso da folha de rosto.
- HOLTERMAN [A CONFERIR] (2016 ou 1997?) sustenta a frase sobre deriva.
- CASTRUCCI [A CONFERIR] precisa registrar que é um e-book sem paginação. A NBR 10520:2023 aceita a seção como localizador.

---

## 4. Problemas médios (recomendados)

🟡 **E7. O projeto linear é violado já em um bico (l. 1004, 1387).** No salto de um bico, a parcela P pede Kc·|Kn|/τa ≈ 0,27/0,2 = 1,34 s⁻¹, mais que o dobro de ω_max = 0,5. Os polos especificados nunca aparecem no modelo completo.

A frase "a especificação pode ser cumprida nas trocas de um bico" está certa só no sentido de que o C1 acomoda em 0,44 s pela métrica da Tabela 10 (ver E9).

Saídas:
- declarar a violação em 3.5.6; **ou**
- incluir a restrição Kc·|Kn|/τa ≤ ω_max no projeto, o que dá Kc ≲ 0,31 e um t_s maior.

A primeira é mais barata e coerente com o escopo.

🟡 **E8. O C1 com 0% fora da faixa não diferencia os controladores (l. 1403, 1457, Resumo).** **[conferido]** Em malha aberta, um bico a menos leva a pressão a cerca de 3,83 kgf/cm² (+9,5%), dentro do limite de 3,85. Qualquer controlador com integrador dá 0% no C1. O 0% vem da ausência de erro estacionário, não de mérito do PI. A folga é de 0,5 ponto percentual e depende de K, P_ref e da fonte. Basta dizer isso em 4.5.

🟡 **E9. A métrica de acomodação não é a mesma da especificação (l. 1106, 1377, 1403).**
- **Especificação:** t_s = 0,5 s pelo critério de 2% **da amplitude do salto**.
- **Tabela 10:** usa ±2% **de P_ref** (±0,07 kgf/cm²), o que equivale a cerca de 21% do salto de um bico.

Por isso aparecem ao mesmo tempo "0,44 s" na tabela e "demora mais que 0,50 s" na Figura 18. Renomear a métrica (por exemplo, "tempo até ±2% de P_ref") ou medir pelo critério da especificação.

🟡 **E10. Kv,max não foi identificado, e a válvula do modelo parece fraca (l. 603, 766, 833, 1041, 1488).**
- **A dependência.** |Kg| ∝ Kv,max, então a sintonia inteira depende desse valor. Ele aparece como "escolha de projeto", mas a agulha de 1/4" da bancada tem um Kv,max próprio.
- **Avaliador B [suspeita]:** pelos pontos da Tabela 2 de Rosa (11% → 4,40; 33% → 4,00), Kv,max ≈ 7,4–7,7, cerca do dobro de 3,5. O resultado depende de como se interpreta o "%" do artigo.
- **Avaliador A [suspeita]:** abrir 11% derrubou a pressão em 24% no ensaio e em só 7% no modelo.
- **Consequência:** "uma única sintonia serve" (l. 833) só vale sob a H5 (Kv linear em α). Uma agulha real em α ≈ 0,023, quase na sede, é não linear e tem folga.

Correção mínima:
- escrever "sob a H5" na l. 833;
- em 3.8, acrescentar a não linearidade e a folga da válvula e a incerteza de Kv,max.

Correção completa: estimar Kv,max pela Tabela 2 e mostrar a sensibilidade para 3,5 e 7.

🟡 **E11. Tempo fora da faixa não é área fora da tolerância (l. 1095, 1476).** Bicos fechados não aplicam nada, e os picos acontecem justamente quando há poucos bicos abertos. A fração de área é o tempo ponderado por n/7. Os "4 m fora da tolerância" valem só para os bicos ainda abertos. Corrigir a frase da 3.6.4 e a da 4.6, ou trocar por volume aplicado fora da tolerância.

🟡 **E12. O "Por que o FF não ajuda" deve partir do valor inicial (A-P8).** Pelo teorema do valor inicial, o salto inicial é Kn·ΔN com **qualquer** controlador, porque a válvula tem inércia. Isso explica por que o desvio máximo do C2 é igual nos três controladores, e cabe em uma frase. O zero de Tn,PI em −1/τa = −5, mais lento que os polos (−8), também merece uma frase.

🟡 **E13. "O que limita o ganho é a velocidade da válvula" (l. 995, 1488).** A velocidade limita o **desempenho**, não a estabilidade. O ganho, na prática, é limitado por dinâmicas não modeladas: capacitância da linha, amostragem e filtro do sensor.

🟡 **E14. A fonte domina os ganhos (B-P5, B-P6).**
- O termo da fonte (1,645) é 67% do denominador de Kg. Isso depende da rotação da tomada de força e do ajuste da PCV, e deve entrar em 3.8.
- P_ref = 3,5 deixa só 1,7% de margem sobre os 3,56 da fonte. Uma queda pequena da bomba torna a referência inatingível com 7 bicos. Discutir a margem de vazão na regra de projeto da l. 1347.

🟡 **E15. 3.8 sem limitações de campo (B-P7, B-P8).** Faltam:
- velocidade variável: com controle de taxa, P_ref ∝ v²;
- escala para barra comercial: com 72 bicos, cada bico pesa cerca de 1,4%, mas o fechamento de seções pesa mais;
- golpe de aríete nas solenoides;
- propriedades da calda.

Também falta a ordem de grandeza da relação pressão–gota. Exemplo: o pico de 29,7% do C2 dá cerca de +14% de vazão e gotas cerca de 7% mais finas, com DMV ∝ P^(−0,3) [a conferir em fonte].

🟡 **E16. Hipótese do 99,9% (l. 132).** A afirmação clássica é que menos de 0,1% do produto atinge o alvo, o que é diferente de dizer que 99,9% chega às águas. Conferir em Ribeiro et al. (2007) e reescrever:

> estima-se que menos de 0,1% do produto atinja o organismo-alvo, e o restante se dispersa no ambiente, inclusive nas águas (RIBEIRO et al., 2007).

🟡 **E17. Objetivo 3 e Resumo × 3.5.6 (C-F10).** O texto diz "sintonizar, por alocação de polos, um P e um PI", mas o P só reaproveita o Kc do PI. Sugestão: "Sintonizar um PI por alocação de polos e usar o mesmo Kc num controlador P, para isolar o efeito da ação integral."

O Resumo diz que o P "reduziu muito". Trocar por "reduziu esse tempo para 38% a 50%".

🟡 **E18. Referências.** Sobre a atualidade (C-F5):
- só 4 itens com revisão por pares são posteriores a 2015;
- cerca de 25% da lista é literatura cinzenta: Jacto, AgriQ, Kuhn, O Globo, ODS regional;
- falta uma seção "Trabalhos relacionados". Os trabalhos seguintes do grupo de Rosa (Terra 2020, IFAC; Terra, Rosa e Drews) estão em `referencias base/` e não são citados. Terra 2020 é pendência da v10.

Fontes usadas e não referenciadas (C-F8): ANSI/ISA-5.1-2009 (l. 54–68, 522) e o catálogo do FanTip (l. 219).

Entradas incompletas (C-F7):
- MILHORANCE: falta data e URL;
- LIU: falta v. 30, p. 2819-2833, 2019 [a conferir]. É preciso fixar a versão, porque as páginas "p. 1–4, 12" citadas no texto são da versão *online first*;
- MANTOVANI: falta o intervalo de páginas;
- MERCALDI: faltam folhas e área;
- ISO: a entrada usa outro nome que a citação. Como o documento consultado foi a BS EN, a referência deve ser a dele;
- intervalos de página: usar hífen.

🟡 **E19. Símbolos com mais de um significado (C-F11).**

| Símbolo | Significados | Sugestão |
|---|---|---|
| K | constante do bico, derivada genérica (l. 365), ganho de malha (l. 988) | K_L para o ganho de malha |
| C | capacidade de saída, C(s) da Eq. 2.10 | Y(s)/R(s) na Eq. 2.10 |
| N | número de amostras, ΔN | N_a para as amostras |
| G_2 / F | repetem G_d / G_f da 2.7.1 | notação G_d / G_f também na l. 929 |

Também: G(s), H(s) e Δα não estão na lista de símbolos, e a lista de siglas está fora da ordem alfabética (PCV e PG aparecem depois de PID).

🟡 **E20. A metodologia usa números do Cap. 4 (C-F12).** Os coeficientes da fonte "da seção 4.1" entram nas contas da 3.5. Basta um aviso, uma única vez, de onde vêm os valores usados a partir dali. Considerar renomear o Cap. 4 para "RESULTADOS E DISCUSSÃO".

---

## 5. Problemas menores

🟢 Itens de forma:
- **Citação misturada com remissão interna** (l. 346, 353): "(CASTRUCCI; BITTAR; SALES, 2018, seção 7.8; seção 2.7)" → "(…, seção 7.8), como detalhado na seção 2.7".
- **Chamadas faltando:** Quadro 3 (l. 1159) e Figura 15 (l. 1185) não são chamados antes de aparecer.
- **Página do Ogata:** t_s a 2% é citado com p. 157 (l. 400) e p. 155 (l. 1106). Uniformizar.
- **Fontes:** os 15 km/h (l. 1476) não têm fonte. INCA: o nome oficial é "Instituto Nacional **de** Câncer" (l. 57).
- **Bico:** "FanTip 0,2" → 110-02.
- **K 7% abaixo do catálogo** (l. 1265): está dentro dos ±15% da ISO 4.9.3.3.2 para bicos abaixo de 1 L/min. Vale citar.
- **l. 1058:** "pressão do passo anterior" não é exatamente o retangular para trás. O efeito é desprezível, mas a descrição deve ser exata.

🟢 Abstract: "second-order pump curve" → "quadratic pump curve"; "it tied with" → "it performed the same as".

🟢 Informalidades que ainda estão no texto:

| Onde | Hoje | Sugestão |
|---|---|---|
| Resumo | "monta" | "desenvolve" |
| Resumo | "tirados de" | "obtidos de" |
| Resumo | "já tira a pressão da faixa" | "leva a pressão para fora da faixa" |
| l. 706, 909 | "na hora" | "instantaneamente" |
| l. 708 | "pula direto para o novo valor" | "passa diretamente ao novo valor de equilíbrio" |
| l. 1467, 1496, Resumo | "empatou/empataram" | "teve o mesmo desempenho" |
| l. 1469 | "não tem o que adiantar" | "não consegue antecipar a correção" |
| l. 1476 | "uns 4 m" | "cerca de 4 m" |
| l. 178 | "grudam menos" | "aderem menos" |
| l. 1482 | "tentou responder" | "investigou, em simulação, se…" |

---

## 6. Perguntas prováveis na arguição

| # | Pergunta | Resposta esperada |
|---|---|---|
| 1 | Com anti-windup também na velocidade, o FF continua pior? | Não. O C3 fica com PI 3,2% e FF 3,1%. A diferença vinha do *windup* durante a rampa. O FF continua sem vantagem porque a parcela P já pede mais abertura que o necessário. |
| 2 | Em quais trocas a válvula opera na região linear? | Em nenhuma. Kc·\|Kn\|/τa = 1,34 s⁻¹ > ω_max = 0,5. O modelo linear dá os valores finais e a forma da resposta, mas não o tempo. |
| 3 | Por que o salto inicial é igual nos três controladores? | Pela H6 e pelo teorema do valor inicial: o salto é Kn·ΔN, e o controlador só age através da válvula, que tem inércia. |
| 4 | Qual seria o FF ideal e por que não foi usado? | −(Kn/Kg)(τa·s + 1), que é impróprio. Uma versão realizável seria um avanço-atraso, ou um *preview* (abrir a válvula antes de fechar as solenoides). |
| 5 | Por que o C1 dá 0% com qualquer controlador com integrador? | O salto de um bico é de 9,5%, menor que a faixa de 10%. |
| 6 | Pelo texto integral do 4.5.4, quais controladores atendem a norma? | O PI e o PI+FF, em todos os cenários. O P reprova a partir de 3 bicos. O critério do trabalho é mais severo que a norma. |
| 7 | Kg continua independente de n com uma válvula não linear? | Não. Kg = (dKv/dα)·dP/dC varia com α(n), e seria preciso escalonar o ganho. |
| 8 | Como estimaria Kv,max e τa? | Kv,max pelos pontos da Tabela 2 de Rosa. τa com um ensaio de degrau no servo. |
| 9 | A H6 vale numa barra de 36 m? | Na bancada, τ_h ≈ 12 ms. Numa barra longa, com mangueira de borracha e ar retido, τ_h pode chegar a centenas de ms, comparável a τa. |
| 10 | Por que tempo fora não é área fora? | Bicos fechados não aplicam nada. É preciso ponderar por n. |
| 11 | Qual critério separa "confirmada" de "refutada"? | Tempo fora da faixa nulo por cenário: confirmada no C1, não confirmada no C2 e no C3, só em simulação. |
| 12 | Por que quase não há literatura recente de controle por bico, nem do próprio grupo de Rosa? | Citar Terra 2020 e os trabalhos seguintes do grupo, e dizer o que o TCC acrescenta. |
| 13 | Por que kgf/cm²? | Para comparar direto com a Tabela 1 de Rosa. 1 kgf/cm² = 98,0665 kPa. |

---

## 7. Ordem sugerida

1. **Texto, sem rodar nada:**
   - E1(a), E2, E3, E4, E5: reescrever 4.6, Conclusão, hipótese, 2.5, 3.6.3 e l. 1261;
   - E7, E8, E9: declarar a violação e o C1, e renomear a métrica;
   - E11, E12, E13.
2. **Ampliar a 3.8:** E10 (mínimo), E14, E15.
3. **Forma:** E6, E16–E20 e os 🟢. Isso pode entrar junto com o relatório de redação e coerência (N1–N11, C1).
4. **Decisões do autor, porque mudam números ou escopo:**
   - E1(b): anti-windup posição + velocidade como caso principal;
   - E10 completo: Kv,max estimado pela Tabela 2 e sensibilidade;
   - E18: seção "Trabalhos relacionados".
