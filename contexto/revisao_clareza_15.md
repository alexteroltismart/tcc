# Revisão da v15: clareza, gordura e pendências

Data: 04/11/2026. Base: `contexto/15.md`, com 1803 linhas; o corpo vai até a L1559.

Três leitores independentes revisaram o texto, um por bloco:
- pré-textuais e Cap. 1–2;
- Cap. 3;
- Cap. 4–5, Referências, Resumo e Abstract.

As afirmações principais foram conferidas no arquivo. Os números de linha são os da versão atual.

**Status: APLICADO na v16 (04/11/2026), ver A16 no 16.md.** Tabela 3, Figura 4 e a conta do erro do P em 4.4 foram mantidas. Cada item tem uma prioridade:
- 🔴 corrigir antes da entrega;
- 🟡 melhora clara;
- 🟢 opcional.

---

## 1. Visão geral

| Bloco | Principais problemas | Corte possível sem perder conteúdo |
|---|---|---|
| Pré-textuais | Listas de siglas e símbolos incompletas ou com sobras; Resumo com números em "tempo dentro" | ~5% |
| Cap. 1–2 | Teoria nunca usada depois (Re, $R_{F,D}$/$R_{F,T}$, $Q_{ref}$); ideia do FF repetida 4×; argumento da ISO que não fecha | 16–20% |
| Cap. 3 | Símbolo $C$ com dois significados; laço da simulação descrito 4×; bissecção explicada 3×; figuras e quadros que repetem equações | 15–20% |
| Cap. 4–5 | Prosa que só transcreve a Tabela 10; mesmas conclusões em 4.6 e no Cap. 5; frases imprecisas | 15–20% |
| Referências | Ordem, autoria (BRASIL), anos faltando, entradas incompletas | — |

Todas as referências citadas estão listadas, e todas as listadas são citadas. As contas do Cap. 4 foram conferidas e estão certas.

---

## 2. Correções obrigatórias (🔴)

| # | Onde | Problema | Correção |
|---|---|---|---|
| 1 | L1468 | Sobrou "[Versão parcial — revisar após validação com dados adicionais.]" | Remover |
| 2 | 3.5.5 (L873 em diante) | $C(s)$ (controlador) colide com $C(n,\alpha)$ (capacidade de saída, Eq. 3.11), introduzido agora | Chamar o controlador de $G_c(s)$ nas Eqs. 3.21–3.24, no texto e na Lista de Símbolos |
| 3 | L865 | "Linearizando a Equação (3.10)": a forma $P(n,\alpha)$ que se deriva agora é a (3.11) | Trocar por (3.11). Acrescentar uma frase: $K_g = K_{v,max}\,dP/dC$ e $K_n = K\,dP/dC$, logo $K_n/K_g = K/K_{v,max}$ = 0,121. Isso demonstra o que o Passo 4 só afirma |
| 4 | L911 | O sinal de "cada bico pede $-K_n/K_g$" é −0,121 por bico **aberto**, mas o texto diz "o mesmo 0,121" | "−0,121 por bico aberto, ou seja, +0,121 por bico fechado (Eq. 3.14)" |
| 5 | Resumo L37, Abstract L43, L1486 | "leva alguns décimos de segundo para voltar". A Tabela 10 dá 0,90–0,95 s | "cerca de 0,9 s" |
| 6 | Resumo e Abstract | "31% e 10%" são % de tempo **dentro** da faixa. O Cap. 4 só usa tempo **fora** | Escrever em tempo fora: "8,9% contra 91% sem controle" |
| 7 | L386 × L1206 | O mesmo teste de ruído aparece como "2,5 a 3,4 vezes" e "2,6 a 3,4 vezes" | Unificar em 2,5–3,4 (valor das notas A) |
| 8 | L1069 (Quadro 2) | `simular` cita "(3.10)–(3.13)", mas o programa usa (3.10) com bissecção, não a (3.11) | "(2.18), (3.10), (3.12), (3.13), (3.17), (3.18)" |
| 9 | Referências | Ver seção 6 (ordem, autoria, anos, entradas incompletas) | — |

---

## 3. Pouco claro ou obscuro (🟡)

### Cap. 1–2

- **L168 × L218:** a L168 diz "duas formas comuns de ajustar a pressão (seção 2.3)", mas a 2.3 lista três. Ajustar para "as mais comuns".
- **L317:** "A norma admite queda de até 10%… por isso a perda pode ser desprezada" não se sustenta: a norma tolerar 10% não prova que a perda é pequena. A ISO também é citada antes de ser apresentada (2.5). Trocar pelo argumento da bancada (PT-01 ≈ PT-02, vazão pequena, H2).
- **L297:** a Eq. (2.9) está sem unidade de $R_F(n)$. Indicar a unidade.
- **L338:** "Um sensor de vazão fecha a malha" usa "fechar a malha" antes da definição (L340), e quem corrige é o controlador. Mover ou cortar.
- **L370–374:** $|K_g|$ aparece antes de $K_g$ ser definido (3.5.2) e sem explicar o módulo. Acrescentar "(em módulo, porque abrir a válvula reduz a pressão)".
- **L386:** "a válvula se move 2,5 a 3,4 vezes mais": mais do que o quê? Completar com "…do que sem ruído (seção 3.8)".
- **L386–389:** os motivos para não usar a ação D citam resultados ($P_{cr}$, seção 4.2) dentro da Fundamentação. Deixar só "ruído" e "saltos" em 2.6.
- **L404:** "a malha deixa de se acalmar sozinha", "dá o ritmo da malha" são expressões vagas. Trocar por "limite de estabilidade" e "escala de tempo da malha".
- **L56:** HV = "*hand valve*" (válvula manual), mas a HV tem servomotor. Explicar que a sigla é o rótulo do fluxograma de Rosa et al.
- **L270:** "$K$ medido a partir dos dados" → "calculado" (Eq. 3.2).

### Cap. 3

- **L771:** na conta de $\alpha_{ff}$, o 3,5 é $K_{v,max}$, mas o leitor lê $P_{ref}$ (também 3,5). Apresentar $K_{v,max}$ = 3,5 e o motivo antes da conta.
- **$P_{ref}$ = 3,5:** é usado em todo o Cap. 3, mas só é justificado em 4.1. Pôr uma frase de justificativa em 3.5.1 ou 3.6.1.
- **L809:** "A soma das constantes é sempre a mesma…" é confuso. Reescrever pela Eq. (3.11): $P$ depende só de $C$, e $\partial C/\partial\alpha = K_{v,max}$ não depende de $n$, logo $K_g$ é constante.
- **L599–600 e Quadro 1:** H2, H4 e H6 são citadas antes da lista de hipóteses (L611). Subir as hipóteses para logo depois da Figura 11, ou trocar "(H6)" por "pressão instantânea" no Quadro 1.
- **L641:** ficam dois valores de $R_1$ (5,54 e 5,58) sem explicação no Cap. 3. Dizer em uma frase que 4.1 usa 5,58 (medido com um bico) para testar só a forma $1/n^2$, ou cortar e deixar para 4.1.
- **L693:** agora que existe a forma explícita, falta uma frase dizendo por que o programa usa a bissecção. Exemplo: "o programa já usava a bissecção; as duas são equivalentes".
- **L717:** não diz de onde vem "os últimos 0,1 desacelerando" ($\tau_a\,\omega_{max}$) e usa 0,12 antes da dedução (L773). Mover o exemplo para depois de 3.5.1 ou cortá-lo; o mesmo cálculo reaparece em 4.3.
- **L851:** "14 divisões" → "14 repetições". Dizer também qual critério define que a malha "ainda oscila".
- **L1194:** "valor teórico… (3,02)" surge do nada no método. Citar a fórmula ou cortar.
- **L1031:** LOO sem expansão nem citação: escrever "validação cruzada *leave-one-out* (LOO)".

### Cap. 4–5

- **L1251:** "valores grandes de n = 1 e 2": o grande é R, não n.
- **L1323:** "As duas coisas têm causas diferentes" não diz quais são as duas coisas. Nomear: o período vem da amostragem; o dente de serra, do limite de velocidade.
- **L1337:** "a soma de retângulos acompanha de forma grosseira" não diz a consequência. Dizer o efeito ou cortar.
- **L1419:** "passa de 69% a 91%" parece uma evolução no tempo. Escrever "fica fora de 69% (C1) a 91% (C3) do tempo".
- **L1431:** "com o dobro do ganho, oscilaria sem parar": 2 × 1,46 ≈ $K_{cr}$. Escrever "chegaria ao limite de estabilidade ($K_{cr}$ = 2,93)".
- **L1453:** "para cada novo alvo inteiro" é uma frase truncada.
- **L1460:** "0,95 s fora da faixa" se confunde com os 0,95 s de acomodação. Escrever "quase 1 s (6,8% de 14 s)".
- **L1476:** "a amostragem limita o ganho" → "a amostragem, junto com o atraso da válvula, limita o ganho".
- **L1484:** "o FF **voltou** a ajudar nos dois cenários": no C3 ele nunca tinha ajudado. Escrever "passou a ajudar também nas trocas rápidas".

---

## 4. Gordura: o que cortar

### Cap. 1–2

- **Teoria não usada depois (decisão do autor, ver nota):**
  - **2.4.1 (Re, Eq. 2.1):** o regime da bancada nunca é calculado. Reduzir a uma frase: a lei de orifício vale para escoamento turbulento, típico de pontas e válvulas.
  - **Eqs. 2.6–2.8 ($R_{F,D}$, $R_{F,T}$, $P_S$ em kg/m⁷):** o Cap. 3 só usa $R_1/n^2$ em (kgf/cm²)/(L/min)². As áreas e unidades também ficam desencontradas da Eq. 2.4.
  - **Eq. 2.11 ($Q_{ref}$, fator 600):** não é usada em lugar nenhum.
  - **Nota:** as Eqs. 2.6–2.9 descrevem o modelo de Rosa et al., que o autor quis mostrar (slide 8 e seção 3.3.1). **Recomendação:** cortar a 2.11 e reduzir a 2.4.1. Manter a 2.9, que é a fórmula comparada no trabalho. As 2.6–2.8 podem virar uma frase ("o artigo separa resistências localizadas e distribuídas"). Cortar equações obriga a renumerar 2.x no texto todo.
- **L183:** anúncio do capítulo que repete a 1.4. Cortar.
- **L189:** tratorizados, autopropelidos e TDP não são usados depois. Reduzir a uma frase.
- **L220:** "grande perda de carga… linhas de até 2\"": cortar.
- **L266:** "mesma forma da equação do tubo Venturi": cortar.
- **L301:** "o efeito conjunto depende só de como…": cortar.
- **L321:** frase solta sobre a deriva (Costa et al.): cortar.
- **L395:** o 1º método de ZN, que não é usado, é descrito. Reduzir a meia frase.
- **L414–424:** a ideia "o FF só acerta se o modelo for exato, por isso há realimentação" aparece 4 vezes. Deixar uma.
- **L433:** técnica de anti-windup não usada (realimentação do integrador). Cortar o item.
- **L439:** "e a correção termina sem passar do ponto": promete demais. Cortar.
- **Siglas sem uso:** AP (só definida), ZN e ISA (nunca aparecem). Tirar da lista.

### Cap. 3

- **Laço da simulação descrito 4 vezes:** 3.4.3, 3.6.2, Figura 16/L1130–1138 e Quadro 5. Manter a 3.6.2 como descrição única e remeter a ela. Cortar "É o coração do programa" (L1130, gíria).
- **Bissecção explicada 3 vezes:** 3.3.4, Figura 15 com o parágrafo (L1098–1104) e Quadro 4. Cortar a Figura 15 e o parágrafo.
- **Figura 14 + Quadro 3 (L1079–1096):** uma função de duas linhas que é a própria Eq. (3.14). Cortar.
- **Figura 17 (L1168–1174):** fluxograma para cinco linhas que repetem as Eqs. 3.26–3.28. Cortar.
- **Tabela 3:** três linhas idênticas. Virar uma frase: "para n = 7, 4 e 1, $K_g$ = −2,66". Também a lista de 3 passos (L781–783) e o exemplo com sete bicos (L803–805) repetem a fórmula de Chapra e a (3.15).
- **L469:** o roteiro aparece em parágrafo, Quadro 1 e Figura 4: três vezes. Reduzir o parágrafo a uma frase.
- **Exemplos triviais:** α = 0,2005 (L727–729), "26 000 passos… 520" (L981). Cortar.
- **Anúncios:** L735 (segunda frase), L855 (última frase), L945. Cortar.
- **L723:** aspas coloquiais "distância = velocidade × tempo". Cortar.
- **L645:** "o formato dos dados é o esperado para esse tipo de válvula" não tem fonte. Cortar.
- **L495:** "O manômetro na ponta direita é o PG-02". Cortar.
- **L719 × L1005:** ω_max 2× e 4× aparece duas vezes. Manter a L1005.
- **L1001–1003:** redefine P, PI e PI+FF. Remeter à 3.5.3.

### Cap. 4–5

- **L1423, L1438, L1449–1451:** só transcrevem a Tabela 10. Condensar em uma frase com interpretação.
- **L1462:** repete L1435 e L1458. Cortar.
- **L1474 e L1478:** método repetido na conclusão. Manter só o resultado.
- **L1301:** ressalva que repete a 3.2. Reduzir a um parêntese.
- **L1303:** frase de transição. Cortar.
- **L1347–1349 × L1427–1431:** o erro do P é calculado duas vezes. Em 4.4, só citar o valor de 4.2.
- **Repetições entre 4.x, Cap. 5 e Resumo:**
  - "a velocidade da válvula define a resposta": 7 lugares;
  - "o FF piora o C3": 6 lugares;
  - "o pico do C2 é instantâneo": 4 lugares.

  Deixar cada uma em 4.6 e na conclusão.

---

## 5. Consistência de termos e listas (🟡)

- **"Correção antecipada"** (Resumo) × **"compensação antecipativa"** (resto do texto): unificar.
- **Bar fora da convenção:** L228 ("4,0 bar") e L1217 ("4,0 bar = 4,079 kgf/cm²"). Deixar claro que é o valor do catálogo, com o equivalente em kgf/cm².
- **Lista de Símbolos.**
  - Faltam: $u$, $\rho$, $v$, $\mu$, $d_i$, $A_1$/$A_2$, $Q_{barra}$, $q$, $V$, $\beta$, $G_d$/$G_p$, $e_k$ (e $P_S$, $Q_{ref}$, se ficarem). Com o item 2 da seção 2, falta também $G_c(s)$.
  - Colisões a indicar: $P$ e $P_{cr}$; $T_s$ e $t_s$; $C$, $C(s)$ e $C_D$; $s$ e $s_k$.
  - $a_2$, $a_1$, $a_0$ aparecem com unidade "—", mas têm unidade.
- **L112 × L439:** a lista diz $s_k$ = 0 "no limite de posição"; o texto diz "quando está saturado". Usar "limite de posição" nos dois.
- **Tabela 10, C1:** o negrito do empate está incoerente. O tempo fora (0,0%) está em negrito para PI e PI+FF, mas o desvio igual (9,5%) só para o PI+FF.
- **Tabela 10:** citar as Eqs. 3.27 e 3.28 no cabeçalho, porque o Cap. 4 não as cita.

---

## 6. Referências (🔴)

- **Ordem:** BRASIL deve vir antes de BRUNETTI.
- **BRASIL (2025):** a autoria é do Movimento Nacional ODS, não do governo. Corrigir a entrada e a citação na L127. A entrada não tem ano.
- **AGRIQ e KUHN:** citados como 2025, mas as entradas não têm data. Usar "[2025]".
- **ISO:** a entrada começa por "INTERNATIONAL ORGANIZATION…", mas a citação é "(ISO, 2015)". Fazer entrada e citação baterem.
- **LIU et al. (2018):** faltam volume e páginas, e "[s. l.]" não se usa em periódico. A versão impressa parece ser *J. Intell. Manuf.*, v. 30, 2019; conferir.
- **Entradas incompletas:**
  - FELIZARDO: páginas, marcado [A CONFERIR];
  - HOLTERMAN: ano e veículo, marcado [A CONFERIR] (1997?);
  - MILHORANCE: data, URL e acesso;
  - MERCALDI: número de folhas;
  - MANTOVANI: página final;
  - COSTA, RIBEIRO e ZIEGLER: número da revista.

---

## 7. Pendências (NOTAS DE REVISÃO, seções B–E, e marcadores no corpo)

### Ainda no corpo do texto (precisam sair antes da entrega)

| Marcador | Linha | Situação |
|---|---|---|
| `[ANO DA DEFESA]` (capa e folha de rosto) | 9, 25 | Aberto: depende da data da defesa |
| `[FICHA CATALOGRÁFICA — gerar em biblioteca.unemat.br/gfc]` | ~30 | Aberto: gerar no site da biblioteca |
| `[FOLHA DE APROVAÇÃO …]` | ~31 | Aberto: imprimir, assinar na defesa e digitalizar |
| `[Versão parcial — revisar…]` | 1468 | **Remover** (item 1 da seção 2) |
| `[A CONFERIR — páginas]` FELIZARDO | 1514 | Aberto |
| `[A CONFERIR — …1997…]` HOLTERMAN | 1522 | Aberto |

### Notas B–E: o que está resolvido e o que continua aberto

| Item | Situação | Ação na nota |
|---|---|---|
| B1 – τa e ωmax estimados | **Aberto.** É limitação declarada no texto (3.8 e trabalhos futuros) | Manter |
| B2 – conferência da H6 | **Desatualizado.** A nota diz "diferença de 1,7 p.p."; o texto atual (L1369) diz 0,6 p.p. (testes da v13) | Atualizar para 0,6 p.p. |
| B3 – curva da válvula / C4 | **Obsoleto.** O C4 saiu na v13 | Apagar |
| B4 – ZN sem ajuste fino | Aberto. Pergunta provável da banca; a resposta está no roteiro | Manter |
| B5 – Kcr depende de Ts | Aberto, mas já explicado no texto | Manter |
| B6 – PCV na bancada | Aberto (pressão de ajuste desconhecida). A nota cita "Figura 8"; hoje é a **Figura 9** | Corrigir o número |
| B7 – validação dinâmica | Aberto (trabalho futuro) | Manter |
| B8 – justificativa da seção 1.3 | Aberto: confirmar com o orientador | Manter |
| C – "2.7 sem referência" | **Resolvido.** Liu et al. (2018) e Fernandes e Goldemberg (2001) | Apagar |
| C – ISO 16122-2 adotada pela ABNT? | Aberto | Manter |
| C – Ziegler e Nichols (1942) original não lido | Aberto | Manter |
| C – "ler originais" | Parcial. **Hughes e Bega não são mais citados** | Tirar os dois da lista |
| C – DOI de Steward e Humburg (2000) | Aberto | Manter |
| C – autoria BRASIL (2025) | Aberto (ver seção 6) | Manter até corrigir |
| D1–D2 – parâmetros da válvula e validação dinâmica | Aberto (trabalhos futuros) | Manter |
| D3 – referências pendentes | Parcial (ver seção 6) | Manter |
| D4 – ficha, folha de aprovação, ano | Aberto | Manter |
| E1 – ano da defesa | Aberto | — |
| E2 – tom simples | Resolvido na prática (v14–v15) | Pode apagar |
| E3 – P_ref = 3,5 ou 4 bar | Decisão tomada (3,5); falta justificar no Cap. 3 (seção 3) | Apagar após justificar |
| E4 – "FF piora o C3 e todo o C4" | **Desatualizado** (o C4 saiu). Resta confirmar com o orientador se a seção 4.6 basta | Reescrever sem o C4 |

---

## 8. Ordem sugerida de aplicação

1. **🔴 itens 1–8 da seção 2.** São correções pontuais, sem renumeração.
2. **Referências (seção 6).**
3. **Cortes que não mexem na numeração:**
   - repetições do Cap. 4–5;
   - anúncios;
   - exemplos triviais;
   - Figuras 14, 15 e 17 e o Quadro 3. As figuras e quadros seguintes são renumerados; as equações, não.
4. **Esclarecimentos da seção 3.**
5. **Cortes no Cap. 2 (decisão do autor):** 2.4.1, Eqs. 2.6–2.8 e 2.11. Isso exige renumerar as equações do Cap. 2.
6. **Atualizar as notas B–E** conforme a seção 7.
7. **Gerar a v16:** `py -3 build/md2docx.py 16` e `post.ps1 -Versao 16`.

Corte total estimado: 15–18% do texto, sem perder nenhum resultado.
