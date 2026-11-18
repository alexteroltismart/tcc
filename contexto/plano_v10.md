# Plano da versão 10

Decidido em conversa em 02/11/2026. Base: `09.md`.

**Executado em 02/11/2026.** O resultado está em `10.md` e em `docs/10.docx` e `docs/10.pdf` (83 páginas). O que foi feito está registrado na seção A10 das notas de revisão. Valem as revisões abaixo: ZN pelo ganho crítico e faixa da ISO 4.5.4.

## Diretrizes

1. **Artigo base único:** Rosa, Terra e Drews Jr (2019). Todo o modelo (bancada, Tabela 1, fluxograma, PCV, curva da fonte) se justifica por ele.
2. **Steward e Humburg (2000) só de passagem:** uma frase na fundamentação (2.6), como exemplo de modelagem de um controlador comercial (Raven SCS-700). Nada da metodologia depende dele.
3. **Modelo físico:** o mesmo da v09 (K, curva da fonte ajustada a Rosa, validação "deixa um de fora", válvula de 1ª ordem com limite de velocidade, H6). Só reescrever de forma mais clara.
4. **Foco: o controle, simples e claro**, em três passos que se apoiam um no outro:
   - **P**, que corrige, mas deixa erro permanente;
   - **PI**, cuja integral zera esse erro;
   - **PI + *feedforward***, que antecipa a troca de bicos.
5. **Sintonia:** Ziegler-Nichols pela **curva de reação**, aplicado direto, sem ajuste posterior. Sai o método lambda/SIMC.
6. **Cenários:** os quatro continuam (C1, C2, C3 e C4).
7. **Sensor sem ruído.** O efeito do ruído vai só para as limitações.
8. **Tolerância:** a faixa vem de uma norma agrícola, e se a norma indicar outro valor, a faixa muda para ele.
9. **Texto:** claro e objetivo, sem meta de tamanho, impessoal e sem gíria.

## O que muda em cada capítulo

### Cap. 1 Introdução
- 1.3 Justificativa: tirar o argumento "como o Raven SCS-700". O atuador se justifica pela bancada de Rosa (PCV e retorno ao tanque) e pela simplicidade.
- 1.2 Objetivos específicos: reescrever na ordem modelo → P → PI → PI+FF → robustez (C4).

### Cap. 2 Fundamentação (enxugar)
- 2.1 e 2.2 (pulverizadores, agricultura de precisão): reduzir ao necessário para entender a barra em série e o controle bico a bico.
- 2.4.2 lei de orifício: manter a ideia ($Q \propto \sqrt{\Delta P}$) e o coeficiente embutido em $K$, com uma dedução mais curta.
- 2.4.4: tirar a equação de malha de Steward (Eq. 2.9) e o parágrafo da tubulação do Raven. Ficam série → paralelo → fonte ligada à barra, tudo com a notação de Rosa.
- 2.6 Controle: reorganizar como P → PI → PID, explicando o que cada ação faz e o **erro permanente** do P (com uma conta simples). Entra a frase sobre Steward e Humburg.
- **Nova 2.6.x Ziegler-Nichols, curva de reação:**
  - o que é a curva de reação (ganho, atraso, constante de tempo);
  - a tabela P/PI do método, com fonte no livro (Ogata);
  - a faixa de θ/τ em que o método vale.
- 2.7 *Feedforward* e anti-windup: manter, mais direto.
- Tolerância: citar a norma (ver Pendências).

### Cap. 3 Metodologia
- H4: a curva da fonte se justifica só pelos dados de Rosa e pela PCV do fluxograma.
- 3.4.2 atuador: $\tau_a$ e $\omega_{max}$ apresentados apenas como **estimados**, sem citar Steward.
- 3.5 Estratégia de controle:
  - 3.5.1: $K_g$ medido no modelo estático (como na v09);
  - 3.5.2: planta $K_g e^{-\theta s}/(\tau_a s+1)$ lida como "curva de reação": $K = |K_g|$, $\tau = \tau_a$, $\theta = T_s/2$, com $\theta/\tau = 0{,}125$, dentro da faixa do método;
  - 3.5.3: ganhos pelo ZN, com a conta passo a passo para o P e para o PI;
  - 3.5.4: forma discreta do PI e *feedforward* (remetendo à 2.7).
- 3.6.4 Métricas: faixa de tolerância pela norma; as demais métricas continuam.
- 3.7 Implementação: manter a estrutura da v09 (equações + fluxograma + código), atualizando o trecho da sintonia e o modo P.
- 3.8 Limitações: incluir o ruído do sensor. O ZN dá ganho cerca de 8 vezes maior que a sintonia antiga, e com ruído a válvula se movimentaria de 3 a 4 vezes mais. Isso foi testado e não entra nos resultados.

### Cap. 4 Resultados (organizado por controlador)
- 4.1 Modelo estático: igual à v09, com o texto mais claro.
- 4.2 Sintonia: valores de $K_g$, $\tau$, $\theta$ e dos ganhos ZN; conferências automáticas.
- 4.3 Controlador P: C1, C2 e C3, mostrando o erro permanente (no teste, 7 de 12 degraus do C1 não acomodam).
- 4.4 Controlador PI: o que melhora em relação ao P.
- 4.5 PI + *feedforward*: o que melhora em relação ao PI, incluindo a explicação do pico do C2 (o salto acontece antes de a válvula poder reagir).
- 4.6 Erro de modelo (C4), com PI e PI+FF.
- **Saem:** a Tabela 9 (com/sem mangueira) e a Tabela 11 (varredura de $\omega_{max}$), cada uma vira no máximo uma frase.

### Cap. 5 Conclusão, Resumo e Abstract
- Reescrever com os números novos, organizados pelos objetivos específicos.

### Referências
- Steward e Humburg continuam, por causa da frase em 2.6.
- Entram Ziegler e Nichols (1942) e a norma da tolerância.
- Sai Skogestad (2003), se nada mais o citar.

## Mudanças no script (`simulacao/modelo_barra.py`)
- `sintonia()`: substituir SIMC por ZN curva de reação, com $K_c$ e $T_i$ para P e para PI. Sai `LAMBDA`.
- `simular()`: novo modo `"P"` (sem integral, com *bias* fixo na abertura de equilíbrio de 7 bicos).
- Cenários C1 a C3 com P, PI e PI+FF; C4 com PI e PI+FF.
- `FAIXA` com o valor da norma.
- Figuras de resultado com a curva do P (cor nova em `COR`).
- Conferências automáticas: manter, acrescentando $\theta/\tau$ dentro da faixa do ZN e $T_i \geq T_s$.
- Retirar o que não for mais usado no texto (comparação com mangueira, varredura de $\omega_{max}$, `margens`).

**Números esperados (do teste de 02/11, sem ruído, faixa de 5%):**

| controlador | $K_c$ | $T_i$ | C1 fora | C2 fora | C3 fora |
|---|---|---|---|---|---|
| ZN P | 3,01 | – | 2,5% | 8,1% | 14,5% |
| ZN PI | 2,71 | 0,083 s | 0,1% | 7,5% | 4,5% |
| PI+FF | | | | | |

A linha do PI+FF fica para depois, e todos os números mudam se a faixa mudar.

## Revisão de 02/11/2026: ZN pelo **segundo método** (ganho crítico)

Esta revisão substitui a diretriz 5 e os itens do ZN abaixo.

- **Por que a curva de reação saiu:** o simulador mostrou que o ganho crítico real é **Kcr = 2,93** (o valor teórico do controlador discreto é $(1+a)/((1-a)|K_g|)$ com $a = e^{-T_s/\tau_a}$, o que dá 3,02). Os ganhos da curva de reação (P com 3,01; PI com 2,71) ficavam **acima ou perto do crítico**: a pressão oscilava sem parar a 10 Hz, limitada só pela velocidade da válvula. Os números "4,5% no C3" da tabela anterior eram de uma malha oscilando. Também deixa de existir a questão de onde vem $L = T_s/2$.
- **Método (Ogata, Tabela 8.2):** no simulador, só com P, aumentar $K_c$ até a pressão oscilar sem parar → $K_{cr}$ = 2,93 e $P_{cr}$ = 0,1 s (duas amostras). P: $K_c = 0{,}5K_{cr}$; PI: $K_c = 0{,}45K_{cr}$, $T_i = P_{cr}/1{,}2$. A tabela 8.2 já usa o ganho medido, então **não existe a armadilha do K**.
- Texto: uma figura com a oscilação sustentada no ganho crítico (Figura 8.5 do Ogata, versão da barra). A explicação é que o controlador só lê a pressão a cada 50 ms; com ganho alto demais, ele passa do ponto, corrige para o outro lado e oscila com período de duas leituras.

**Resultados (sem ruído, faixa ±10% na pressão, ISO 4.5.4), todos sem oscilação no fim:**

| | $K_c$ | $T_i$ | C1 fora | C2 fora | C3 fora | C3 desvio máx. |
|---|---|---|---|---|---|---|
| P | 1,46 | – | 10,2% | 46,6% | 26,9% | 19,9% |
| PI | 1,32 | 0,083 s | 0,0% | 7,5% | 5,0% | 16,8% |
| PI+FF | 1,32 | 0,083 s | 0,0% | 6,8% | 5,9% | 16,2% |

- **P:** erro permanente de +0,066 kgf/cm² com 6 bicos. No C2, fica 47% do tempo fora da faixa. Mostra bem por que a integral é necessária.
- **PI:** zera o erro e melhora muito.
- **FF (fica no trabalho, decisão do autor):** melhora um pouco o C2 e piora o C3 (5,0% → 5,9%). A conclusão precisa dizer isso. Investigar a causa antes de escrever (hipótese: o salto de comando do FF satura a velocidade da válvula).

## Conferido nas fontes (02/11/2026)

### ISO 16122-2:2015 (BS EN ISO 16122-2:2015, inspeção de pulverizadores de barra em uso)
- **4.5.4, dispositivos de ajuste de pressão:** devem manter a pressão constante com tolerância de **±10%** na mesma regulagem, e voltar a ±10% em até 10 s depois de desligar e religar. **É a cláusula usada para a faixa: ±10% direto na pressão.**
- 4.8.8, retornos compensatórios: 10 s depois de fechar uma seção, a pressão não pode variar mais de 10%. É o caso mais parecido com fechar bicos; pode ser citada junto.
- 4.9.3.3.2, vazão de cada bico: ±10% da nominal para bicos de 1 L/min ou mais. Ficou de fora, porque convertida para pressão daria uma faixa larga demais (0,81 a 1,21).
- 4.5.3: medidores de vazão e velocidade com erro de até ±5%. É daqui que parece vir o "5%" usado por Steward.
- Com ±10% na pressão, os resultados quase não mudam em relação à faixa antiga: ±5% na vazão dá 0,9025 a 1,1025 na pressão, praticamente a mesma faixa.

### Ogata (2010), 5ª ed., seção 8.2, Tabela 8.1 (primeiro método, resposta ao degrau)
- **P:** $K_p = T/L$; **PI:** $K_p = 0{,}9\,T/L$, $T_i = L/0{,}3$; **PID:** $K_p = 1{,}2\,T/L$, $T_i = 2L$, $T_d = 0{,}5L$. O modelo é $Ke^{-Ls}/(Ts+1)$.
- **Atenção:** a tabela do Ogata **não divide pelo ganho $K$** da planta. Na fórmula original de Ziegler e Nichols o ganho entra como $K_p = 0{,}9\,T/(K L)$. Com $|K_g| = 2{,}66$, esquecer a divisão daria $K_c$ = 7,2 em vez de 2,7. O texto deve usar a forma com $K$ e explicar o motivo, citando ZIEGLER; NICHOLS (1942), *ASME Trans.* 64, p. 759–768 (referência que o próprio Ogata lista).
- O Ogata diz que o método vale para plantas sem integradores com resposta em S, e que a curva pode vir **de simulação**.
- O Ogata também avisa que o ZN dá **um ponto de partida** e que pode ser preciso fazer **sintonia fina**. Como a decisão foi aplicar o ZN sem ajuste, o texto deve reconhecer esse aviso.
- **Ponto fraco para a banca:** na nossa planta, o atraso $L = T_s/2$ não aparece numa curva de reação simulada. Ele vem da amostragem do controlador (segurador de ordem zero). O texto precisa explicar de onde sai $L$, senão a pergunta "onde está a curva em S?" fica sem resposta.

### Resultado com faixa de ±10% na pressão (sem ruído)

| | C1 fora | C2 fora | C3 fora | C3 desvio máx. |
|---|---|---|---|---|
| ZN P | 2,7% | 8,2% | 15,5% | 17,5% |
| ZN PI | 0,1% | 7,6% | 4,6% | 16,6% |
| ZN PI+FF | 0,0% | 7,0% | 4,9% | 17,5% |

**Achado:** com os ganhos do ZN, o *feedforward* quase não ajuda e piora o C3 (4,6% → 4,9%). O PI rápido já faz quase tudo, e isso muda a conclusão da v09 sobre o FF.

## Ordem de trabalho
1. Script → rodar → conferir números e figuras.
2. Copiar `09.md` para `10.md` e reescrever na ordem Cap. 3 → 4 → 2 → 1 → 5 → Resumo/Abstract.
3. Registrar tudo em "NOTAS DE REVISÃO", seção A10.
4. Corrigir as sobras da v09: "decorando", "como manda", aspas coloquiais e o `\varphi` da nota A09.
5. Gerar o docx e o pdf (`md2docx.py 10` + `post.ps1 -Versao 10`).
6. Atualizar o `CLAUDE.md` (versões 04–10, comandos, ZN no lugar de lambda, ruído fora).
