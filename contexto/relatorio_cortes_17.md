# Relatório de cortes — versão 17

Data: 05/11/2026. Base: `contexto/17.md`, corpo com cerca de 20.100 palavras.
Três leitores independentes revisaram o texto, cada um com um bloco de capítulos. Nenhuma alteração foi feita no texto.

## Resumo

| Bloco | Palavras hoje | Corte estimado | % |
|---|---|---|---|
| Cap. 1 e 2 | 4.750 | ~880 | 18% |
| Cap. 3 | 9.050 | ~1.475 | 16% |
| Resumo, Cap. 4 e 5 | 4.220 | ~775 | 18% |
| **Total** (sem as sobreposições) | **~20.100** | **~2.950** | **~15%** |

Nenhuma proposta corta equação numerada, então a numeração (2.x, 3.x) não muda. Mudam só as remissões a "Quadro 4/5" e a "seção 3.6.2", se os itens correspondentes forem aplicados.

**Padrão principal:** a mesma ideia explicada duas ou três vezes, uma na teoria (Cap. 2), outra no método (Cap. 3) e outra nos resultados (Cap. 4). Os casos mais repetidos são:
- a descrição da bancada de Rosa (bomba, PCV, bicos e válvula de alívio aparecem 4 a 5 vezes);
- o balanço de vazões no nó (5 vezes);
- a ligação pressão → dose → gota (5 vezes no Cap. 1–2);
- o laço da simulação (lista na 3.6.2, Figura 14 e Quadro 4);
- os números da Tabela 10, relidos na 4.5/4.6, na Conclusão e no Resumo.

**Erro encontrado (já corrigido):** a Conclusão dizia "0,6 ponto percentual" na conferência da H6, um resto da v16. O valor da v17 é 0,4. O md e o PDF foram corrigidos.

---

## A. Cortes de risco baixo, por ganho

Podem ser aplicados direto. As linhas são as de `17.md` em 05/11.

### Cap. 3 (maior ganho)
1. **3.6.2 (l. 963–973), laço de 5 passos:** condensar para uma frase que remete à Figura 14 (~90 palavras).
2. **Balanço no nó** (l. 523, 587–599, 674): ficar com 594–597 e com a primeira frase de 674, e reduzir a lista da Figura 11 a uma frase (~110).
3. **Exemplo numérico do PI** (l. 798–806): cortar, porque só aplica as Eqs. 3.17–3.18 (~110).
4. **Bancada e válvula de alívio** (l. 462–468, 486, 494, 502, 519): a HV é apresentada 4 vezes. Tirar as repetições das legendas e virar a lista em frase (~90).
5. **Contraste R₁/n² × fórmula (2.5)** (l. 619–624): juntar em uma frase, porque o assunto volta na 4.1 (~70).
6. **Diferença centrada** (l. 756–762): cortar a fórmula geral sem número e ir direto à (3.15) (~60).
7. **3.7.3, conferências** (l. 1147–1155): de 6 itens para uma frase (~60).
8. **Abertura da 3.4 e passo de Euler** (l. 680–688, 708): tirar a capacitância explicada duas vezes e a justificativa do passo, que volta na 4.2 (~60).
9. **Limite da amostragem** (l. 927, 931): o fato "a FT contínua não mostra o limite" está em 894 e de novo em 931. Ficar com um (~60).
10. **Exemplos da faixa e do IAE** (l. 1001, 1009, 1014–1015): cortar (~50).
11. **Ação derivativa** dividida entre a 2.6 (l. 357–359) e a 3.5.5 (l. 933): ficar só na 2.6 (~45, contando o Cap. 2).
12. **Abertura da 3.7** (l. 1024–1034): repete o apêndice (~45).
13. **Contas antes da (3.14)** (l. 738–746): tirar as duas linhas que só isolam α (~45).
14. **Bissecção passo a passo** (l. 676): uma frase (~40).
15. **Leitura da Figura 12** (l. 734): ficar só com o que o diagrama não mostra (~40).
16. **Menores** (~120 no total): l. 452 (leitura da Figura 4), l. 822 ($K_n/K_g$ repetido), l. 898 (abertura da 3.5.5) e l. 977–993 (três parágrafos de cenários viram um).

### Cap. 1 e 2
17. **Organização do trabalho** (l. 181): repete o Quadro 1; uma frase basta (~80).
18. **Atuador e bancada na introdução** (l. 170–177): três parágrafos repetem a 3.2 e os trabalhos futuros (~165).
19. **Bancada no Cap. 2** (l. 218, 230, 290, 292): bomba, FanTip, PCV e perda na tubulação voltam na 3.2/H2. Os 0,92 L/min de catálogo não são usados em lugar nenhum (~170).
20. **Pressão → dose → gota** (l. 161, 189, 201, 296): ficar com uma ocorrência (~130).
21. **Controle** (l. 311–317, 337, 349–353, 398, 410–412, 422): listas que viram frases e repetições do sinal do erro, dos três controladores e do anti-windup (~210).
22. **Ruído na 2.6** (l. 357): o mesmo número está na 3.8 (~30).
23. **2.6.1, só a forma** (l. 363, 367, 388–392): tirar o metatexto e virar a lista de 3 passos em frase. O conteúdo fica (~40).

### Resumo, Cap. 4 e 5
24. **Conclusão relendo a Tabela 10** (l. 1407–1423): cortar os números entre parênteses que já estão no Cap. 4 e juntar as frases do pico triplo (~150).
25. **4.5 e 4.6 relendo a Tabela 10** (l. 1380–1397): a lista de 3 itens vira uma frase, e os fechamentos sobre o *feedforward* aparecem uma vez só (~120).
26. **Legendas em prosa** (l. 1206, 1238, 1345–1348): mantendo as cores, que a 4.4–4.6 citam (~75).
27. **"Ressalva" sobre 6,10 kgf/cm²** (l. 1258): já tratada na l. 541; vira um parêntese ali (~45).
28. **Trabalhos futuros** (l. 1426–1429): juntar os dois itens de medição e tirar o 4,8%, que já está na 4.5 (~30).
29. **Resumo e Abstract** (397 e 400 palavras, abaixo do limite de 500): encurtar três frases em cada (~50).
30. **Menores** (~100): l. 1170, 1240, 1262, 1302, 1318, 1362, 1368/1374, 1386 (antecipar a válvula aparece também nos trabalhos futuros).

## B. Cortes que dependem de decisão do autor

| # | Trecho | Ganho | Por que perguntar |
|---|---|---|---|
| B1 | **Quadros 3 e 5** (código de `p_regime` e `metricas`, l. 1063–1143) | ~200 | Copiam o Apêndice A. O autor pediu o script explicado no texto, mas a 3.7 continuaria com o Quadro 4 (laço principal) e a Figura 14. |
| B2 | **Passo a passo das funções de transferência** (l. 830–862) | ~80 | Foi pedido pelo autor na v15. A proposta tira só as contas intermediárias sem número; as Eqs. 3.22–3.25 ficam. |
| B3 | **Polos do PI refeitos na 4.2** (l. 1292–1300) | ~80 | É a mesma conta da Tabela 9 de trás para frente. A proposta deixa uma frase com os números e tira as duas equações exibidas. |
| B4 | **ISO 16122-2, item 4.8.8** (l. 301–303) | ~55 | Nada depois o usa, mas a nota A15 o manteve de propósito "como comparação". |
| B5 | **Erro do P na 4.2** (l. 1288–1290) | ~15 | A 4.4 refaz a conta. Trocar a equação exibida por uma frase com o 0,101. |

## Ordem sugerida

1. Aplicar o bloco A inteiro, cerca de 2.500 palavras (~12%), numa v18. Os números, equações e figuras não mudam.
2. Decidir B1–B5, até cerca de 430 palavras a mais.
3. Regerar o PDF e conferir as remissões a Quadros e à seção 3.6.2.
