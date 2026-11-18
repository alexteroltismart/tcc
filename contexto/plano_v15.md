# Plano — versão 15 (clareza e roteiro da metodologia)

## Objetivo

Deixar o texto "redondo". A metodologia deve mostrar o passo a passo do trabalho, e os trechos confusos ou sem clareza apontados na revisão (`contexto/revisao_clareza_14.md`) devem ser corrigidos.

**Fica de fora desta versão:**
- mudanças nos números ou no escopo;
- alterações no script da simulação;
- novos cenários.

Também ficam para depois:
- a referência do *feedforward* na seção 2.7.1, que espera o livro (Campos e Teixeira, Seborg ou Åström e Hägglund);
- os itens adiados da banca da v10.

Base: `contexto/14.md` → `contexto/15.md`.

---

## Passos

### 1. Roteiro da metodologia (seção 3.1)

- Reescrever a seção 3.1 como **roteiro do trabalho em 7 etapas**, com uma **tabela-mapa**. Colunas: etapa, entrada, o que é feito, saída, seção do método, seção do resultado.
  1. Dados de referência
  2. Modelo estático
  3. Modelo dinâmico
  4. Ganho da planta e *feedforward*
  5. Controladores, sintonia e função de transferência
  6. Simulação e avaliação
  7. Implementação e conferências
- **Figura nova "Etapas do trabalho"**: um fluxograma em Graphviz, `build/fig/fig_etapas.dot`, no mesmo estilo das Figuras 13–17. Ele mostra a saída de cada etapa alimentando a seguinte.
  - A figura entra em 3.1, antes das figuras da bancada, como **Figura 5**. As figuras 5–24 passam a 6–25.
  - Atualizar no `md2docx.py` o mapa dos diagramas mermaid para v ≥ 15 (Figuras 12 e 13).
- Manter, numa frase, a classificação da pesquisa como aplicada e quantitativa.

### 2. Frases de abertura com a etapa

Cada seção do Cap. 3 começa dizendo a etapa e o objetivo. Por exemplo, para a 3.3: "Etapa 2. Com os dados da bancada, o objetivo é obter uma equação que dê a pressão para qualquer número de bicos e abertura da válvula."

A seção 3.7 passa a dizer que o programa executa o mesmo roteiro da seção 3.1. A Figura 13 (fluxo do programa) é mantida.

### 3. Reorganização e simplificação no Cap. 3

- **Trocar 3.5.1 e 3.5.2 de ordem.** Primeiro a abertura de equilíbrio α_ff(n) (Eq. 3.13), depois K_g (Eq. 3.14). Renumerar as duas equações, as referências e os rótulos das figuras (Fig. 13/programa: K_g; Fig. 14/alpha_ff; `fig07.py`: α_ff).
- **Simplificar a seção 3.4.2**, que fica sem "saturação" e sem a notação sat±ω_max:
  - a Eq. 3.11 passa a ser dα/dt = (α_c − α)/τ_a;
  - o limite de velocidade é dito em palavras: "a abertura não muda mais que 0,5 por segundo; quando a conta pede mais, a válvula anda nessa velocidade";
  - mantém-se o exemplo do C2, com a conta 3 × 0,12 = 0,36 e a remissão à seção 3.5.
- **Seção 3.5.5 (função de transferência):**
  - frase-motivo no início (item 7 da revisão);
  - explicação do sinal da realimentação seguindo a malha (item 9);
  - origem do termo do *feedforward*, 0,121 por bico = K/K_v,max, e de onde sai a Eq. 3.24 (item 10);
  - ponto de cálculo de K_n e K_n na Tabela 4 (item 11);
  - P e PI estáveis com qualquer ganho na forma contínua, com remissão à Tabela 9 (item 13);
  - **as contas numéricas (0,066, polos, ζ, t_s) vão para a seção 4.2**, junto da Figura 21 (item 8). Em 3.5.5 ficam as equações e as conclusões qualitativas.
- **Modelo R₁/n²** (itens 1–3):
  - deixar claro que as Eqs. 3.3 e 3.4 são o mesmo modelo;
  - o simulador usa K = 0,425 (R₁ = 5,54), e a seção 4.1 usa R₁ = 5,58 só para testar a forma 1/n²;
  - "vale para qualquer número de bicos, desde que H2".
- **Seção 3.3:** trocar "parte da Equação (2.8)" (item 4) e escrever em palavras a capacidade total de saída, sem nK + K_v antes da definição (item 32).
- **Um nome para a válvula atuadora**, "válvula de alívio (HV)", com os sinônimos explicados uma vez em 3.2. Na 3.3.2, a PCV não pode ser chamada de "válvula de alívio" (item 5).
- **Um nome para a abertura fixa:** α₀ = α_ff(7) = 0,023, com `bias  # α0` no Quadro 4 (item 21).
- **Seção 3.2:** avisar que a Tabela 2 parte de 4,00 kgf/cm², outra rotação da bomba, e por isso só serve como comparação qualitativa (item 6).
- **Tabela 5:** acrescentar a duração do C2 (14 s) e dizer de qual cenário é o exemplo das 946 amostras (item 22).
- **Seção 3.5.3:** "o efeito de não congelar o integrador no limite de velocidade é medido na 4.5" (item 18).
- **Seção 3.7.3:** escrever "até 2,3%" (item 23).

### 4. Cap. 2

- **Seção 2.5:** a faixa de ±10% vem do item 4.5.4 da ISO. O item 4.8.8 só mostra que a norma trata o fechamento de seção; o critério do trabalho é mais exigente (item 14).
- **Seção 2.6:** reordenar o parágrafo da Eq. 2.11 e ligá-lo à pressão como variável controlada (item 15).
- **Seção 2.4.4:** corrigir a lógica de "sustenta a H2" (item 28).
- **Seção 2.3:** a PCV "provavelmente" explica a queda de vazão (item 29).
- **Seção 2.6.1:** a remissão passa a ser só "seção 3.8" (item 30).
- **Início do Cap. 2:** frase com a ordem dos assuntos.

### 5. Cap. 4 e Conclusão

- **Seção 4.1:**
  - abrir explicando o R₁ = 5,58 (item 1);
  - mostrar a Tabela 7 com Q previsto em três casas, tiradas de `resultados.json` (item 23);
  - transição para a 4.2.
- **Seção 4.2:**
  - receber as contas da função de transferência;
  - distinguir as causas da oscilação: a amostragem define o período e a velocidade, a forma em dente de serra (item 33);
  - fórmula ou origem do 3,02 (item 24);
  - "conclusão que volta a aparecer nas seções 4.5 e 4.6" (item 34).
- **Seção 4.3:**
  - dizer qual figura olhar e explicar "não acomoda (11 de 12)" (item 35);
  - transição para a 4.4.
- **Seção 4.5:**
  - distinguir os 0,7 s da válvula dos 0,95 s de acomodação (item 26);
  - justificar o anti-windup só por posição como a forma da literatura, e estendê-lo ao limite de velocidade como melhoria indicada (item 17).
- **Seção 4.6:**
  - "0,95 s" explicado como 6,8% de 14 s (item 25);
  - por que o PI acompanha melhor as trocas rápidas (item 27).
- **Conclusão:**
  - cada objetivo no seu parágrafo: K_g no do 3º objetivo e um parágrafo próprio para o 4º, o *feedforward* (item 16);
  - trabalhos futuros: medir a velocidade da válvula e estender o anti-windup ao limite de velocidade.

### 6. Repetições, transições e listas

- Cortar as repetições listadas na revisão:
  - motivos da bancada;
  - a válvula como trabalho futuro de Rosa;
  - a justificativa da H2 (completa só em 3.3);
  - as três formas de ajuste;
  - "K_g não depende de n";
  - o erro do P (dedução em 2.6, números só no Cap. 4);
  - o 3,02;
  - o teste de 10 ms.
- Transições:
  - fim da 1.4: o roteiro passa a citar o modelo R₁/n² e a função de transferência;
  - início da 3.3;
  - início da 3.6;
  - da 4.1 para a 4.2;
  - da 4.3 para a 4.4.
- **Lista de símbolos:** acrescentar P_ref, α₀, C(s), G(s), E(s), os desvios Δ, t_s, d e e_reg (item 37).
- Inserir a linha em branco que falta antes da 3.4.2 (item 36).
- **Resumo e Abstract:** só ajuste de forma, se algo mudar de nome. Os números ficam.

### 7. Registro e geração

- Escrever a seção A15 nas NOTAS DE REVISÃO, com a lista do que foi aplicado e a renumeração de equações e figuras.
- Regenerar as figuras com rótulos alterados (`fig_etapas`, `fig12_programa`, `fig13_alpha_ff`, `fig07.py`).
- Rodar `py -3 build/md2docx.py 15` e `powershell -File build/post.ps1 -Versao 15`.
- Atualizar o `CLAUDE.md` e a memória. Marcar no `revisao_clareza_14.md` os itens aplicados.

---

## Verificação

- **Números iguais aos da v14.** Comparar por grep todas as tabelas (5–10), o Resumo e a Conclusão. O script não é rodado de novo.
- **Equações e figuras em sequência:**
  - `\tag` sequencial nos Caps. 2, 3 e 4;
  - toda "Equação (x)" e toda "Figura N" apontam para o lugar certo;
  - o mapa dos diagramas mermaid no conversor corresponde às figuras certas, conferido no PDF.
- **Tamanho:** o corpo pode crescer um pouco, por causa do roteiro e das transições, e encolher pelas repetições cortadas. A meta é ficar entre −5% e +5% em relação à v14.
- **Itens da revisão:** os 37 itens e as listas são conferidos um a um. Os não aplicados ficam registrados na A15 com o motivo.
- **PDF:** sem restos de LaTeX, e conferência visual da 3.1 (tabela-mapa e figura), da 3.4.2, da 3.5.5 e da 4.2.
- **Releitura opcional:** uma nova leitura independente (agente revisor) da v15, para confirmar que os pontos confusos foram resolvidos.
