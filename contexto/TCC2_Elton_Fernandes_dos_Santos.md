# Contexto — `docs/TCC 2 - ELTON FERNANDES DOS SANTOS.pdf`

**Para que serve:** é um **TCC II aprovado** no mesmo curso (Engenharia Elétrica, UNEMAT Sinop, em 18/06/2019) e funciona como **referência de formatação e escrita**. O assunto técnico (FPGA/VHDL) não tem relação com o meu tema. Use o arquivo para ver *como* a monografia final fica montada na prática, comparando-o com o template `Modelo_TCC_II.doc`.

- **Título:** Bloco de Atraso Digitalmente Controlado Usando Técnicas Híbridas
- **Autor:** Elton Fernandes dos Santos · **Orientador:** Prof. Dr. Vlademir de Jesus Silva Oliveira · **Coorientador:** Luciano Nogueira
- **Banca:** Eduardo Rodrigo Thiesen e Maria Helena Vieira Kelles (avaliadores); o orientador também presidiu a banca.
- **Tamanho:** 59 folhas, sendo 13 pré-textuais e ~42 de texto (Introdução na p. 14, Referências nas p. 57–58). Tem 43 figuras, 4 tabelas e 22 referências.

---

## 1. Formatação (como foi feito)

### Ferramenta e aparência geral
- Feito em **LaTeX com abnTeX2** (os metadados do PDF registram `pdfTeX`, `abntex2`). Fica claro que a UNEMAT **aceita LaTeX/abnTeX2**, não só o template em Word.
- Folha **A4**, com fonte sem serifa parecida com **Arial/Helvetica** (NimbusSans) em todo o documento e equações em Computer Modern.
- Corpo **justificado**, espaçamento entre linhas de **~1,5**, recuo de primeira linha de ~1,25 cm e espaço extra entre parágrafos (padrão do abnTeX2).
- **Cabeçalho** a partir da Introdução: o nome do capítulo em itálico à esquerda ("Capítulo 2. HARDWARE"), o número da página à direita e um filete horizontal embaixo. Nas páginas que abrem capítulo aparece **só o número**, no canto superior direito.
- As páginas pré-textuais são contadas, mas não numeradas. A numeração visível começa em **14** na Introdução.

### Pré-textuais (ordem real)
1. **Capa:** "UNIVERSIDADE DO ESTADO DE MATO GROSSO" no topo, nome do autor no meio, título em **negrito e caixa alta**, e "SINOP-MT / 2019" embaixo. Tudo centralizado e em negrito.
2. **Folha de rosto:** nome sem negrito, título em negrito e a **natureza do trabalho num bloco recuado à direita** (~metade da página, justificado, fonte menor), com o texto exato do template: *"Trabalho de Conclusão de Curso apresentado à Banca Examinadora do Curso de Engenharia Elétrica - UNEMAT, Campus Universitário de Sinop - MT, como pré-requisito para a obtenção do título de Bacharel em Engenharia Elétrica."* Logo abaixo, "Orientador: Prof. Dr. …".
3. **Ficha catalográfica** gerada pela biblioteca, com bibliotecário CRB, Cutter `S237b`, "59 f.; 30 cm", palavras-chave numeradas e CDU. *(No original, o nome do autor aparece duplicado na ficha: "Santos Santos". Conferir com cuidado antes de entregar.)*
4. **Folha de aprovação digitalizada (scan)** já assinada: brasões do governo do MT e da UNEMAT, a hierarquia "Governo do Estado / SECITEC / UNEMAT / Campus Sinop / Curso", nome, título, as quatro assinaturas (2 avaliadores, orientador, presidente) e "Aprovado em __/__/____" preenchido à mão. → **Essa página é impressa, assinada na defesa e depois escaneada para a versão final.**
5. **Agradecimentos** (curto, 2 parágrafos)
6. **Epígrafe** (citação centralizada com a fonte entre parênteses e sem título na página). *Não há dedicatória.*
7. **Resumo:** um único parágrafo de ~150 palavras e a linha "Palavras-chave:" com termos separados por vírgula. *(O template pede ponto como separador; o Elton usou vírgula.)*
8. **Abstract:** tradução literal do resumo, com Keywords.
9. **Lista de ilustrações:** "Figura N – Título . . . . pág", gerada automaticamente.
10. **Lista de tabelas**
11. **Lista de abreviaturas e siglas:** sigla à esquerda e expansão à direita. *(Aqui a ordem das colunas ficou desalinhada e as expansões não batem com as siglas. É um defeito a evitar.)*
12. **Sumário:** numeração progressiva com indicativos alinhados à esquerda. Capítulos (nível 1) e seções (nível 2) em **negrito**, subseções (nível 3) sem negrito. Pontilhado até o número da página e linha em branco entre capítulos. "REFERÊNCIAS" aparece sem número.

### Títulos e seções
- Capítulo (nível 1): **"1 INTRODUÇÃO"** em caixa alta, fonte grande, sem negrito pesado, alinhado à esquerda, **sempre começando em página nova**.
- Nível 2: "1.1 Objetivos" e nível 3: "1.1.2 Objetivos específicos", ambos com só a inicial maiúscula e fonte que diminui a cada nível.
- Não há ponto depois do número ("1.1 Objetivos", e não "1.1. Objetivos" como aparece no template Word).
- O texto do Elton tem 5 capítulos: Introdução (com Objetivos dentro) → fundamentação ("HARDWARE") → desenvolvimento ("DESENVOLVIMENTO DO BLOCO DE ATRASO") → "Resultados" → "CONCLUSÃO". **Não existe um capítulo de Metodologia separado**: o método fica embutido no desenvolvimento.
- Cada capítulo abre com uma seção **"X.1 Introdução"** que apresenta o que vem a seguir. É um bom recurso para dar fluidez.

### Figuras, tabelas, equações
- **Figura:** a legenda vai **acima**, centralizada ("Figura 8 – Corpo de uma arquitetura.", com travessão), e a **fonte vai abaixo**, centralizada e em fonte bem menor ("Fonte: Autor", "Fonte: (VAHID, 2008)", "Fonte: (AMORE, 2012) editado pelo autor"). As figuras ficam dentro de uma moldura com borda cinza clara.
- Toda figura é **citada no texto antes de aparecer** ("como na Figura 1", "Na Figura 13 mostra…").
- **Tabela:** título acima ("Tabela 1 – …"), no estilo booktabs, só com filetes horizontais e **sem linhas verticais**. *(As tabelas do Elton não indicam fonte, mas o ideal é indicar.)*
- **Equação:** centralizada e numerada **por capítulo**, à direita: "(3.1)".
- **Notas de rodapé** explicativas para termos técnicos (Verilog, push button, netlist, shell script, código termométrico). A numeração **reinicia a cada capítulo**.
- **Código-fonte** entra como figura (captura de tela), e não como listagem. *(Se o meu trabalho tiver código MATLAB/Python, o melhor é usar listagem/"Quadro" com fonte monoespaçada.)*
- Termos estrangeiros em **itálico** (*clock*, *software*, *chip*). Marcas registradas aparecem com ® (Altera®, Quartus®).

### Citações e referências
- Sistema **autor-data** (NBR 10520). Entre parênteses e em caixa alta: "(HENZLER, 2010)", "(GIORDANO et al., 2015; JIAQI et al., 2006; LIMA; OLIVEIRA, 2017)". Quando o autor faz parte da frase, vai em caixa baixa: "Lima e Oliveira (2017) define…", "Jiaqi et al. (2006)".
- Referências em **ordem alfabética**, alinhadas à esquerda, em espaço simples e com linha em branco entre elas. O título da obra vai em **negrito/itálico** conforme o abnTeX2. Para fontes online, "Disponível em: <url>. Acesso em: …". Quando falta local, usa-se "[S.l.]".
- Ele cita **TCCs anteriores do mesmo orientador** (Schmatz e Oliveira, 2017; Cajado e Oliveira, 2018) como base do trabalho. Isso é perfeitamente aceito.
- O cabeçalho das páginas de referências mostra "Referências | 58".

---

## 2. Escrita (estilo e estrutura do texto)

### Padrões que vale copiar
- **Introdução em funil:** parte do contexto amplo (digital vs. analógico), passa para a tecnologia (FPGA), depois para a aplicação (TDC/DCDL), para as técnicas existentes, para o que o trabalho faz e, por fim, para um **parágrafo-roteiro** com o que cada capítulo e seção traz ("No capítulo 2 na seção 2.2 foi apresentado…").
- **Objetivos dentro da Introdução** (1.1), com geral e específicos (lista com marcadores, cada item começando por verbo no infinitivo).
- **Conclusão retoma a hipótese em forma de pergunta** e responde a ela: "A pesquisa partiu da seguinte hipótese, é possível…? Durante o trabalho verificou-se que…".
- **Admite as limitações com franqueza** nos resultados e na conclusão (placa inadequada, osciloscópio limitado, não linearidade e metaestabilidade sem explicação), sugere caminhos (ferramenta Chip Planner) e indica a continuidade do trabalho.
- Resultados mostram **dados concretos em tabela** (palavra de controle × atraso, entrada × saída do TDC) e explicam um **exemplo numérico de ponta a ponta** (palavra de 13 bits que gera 13,000 ns: 10 ns do atraso grosso, 66 MUX medidos e 34 MUX de correção). Esse tipo de exemplo trabalhado ajuda muito a banca a entender.
- Explica o porquê das escolhas de projeto (comparação entre DLL, Vernier e TDL antes de escolher o TDL).
- Usa voz **impessoal/passiva** ("foi utilizado", "verificou-se", "optou-se por") e evita a primeira pessoa.

### Problemas do texto (evitar no meu)
- **Concordância verbal** com erros frequentes: "fatores que compromete", "Lima e Oliveira (2017) define", "os resultado foram", "esses arranjos são feitos… desprendem".
- **"mais" no lugar de "mas"** ("mais também surgiram", "comprovam a lógica mais não traz").
- **Crase** errada: "nas linhas 08 à 11" (o certo é "08 a 11").
- Erros de digitação: "quarto modo" (quatro), "estancia" (instancia), "interações" no sentido de iterações, "algorítimo", "metainstabilidade", "nem uma" (nenhuma).
- Construções do tipo "**Na Figura 3 mostra** um diagrama", que ficam sem sujeito. O correto é "A Figura 3 mostra…" ou "Na Figura 3 é mostrado…".
- **Siglas entre parênteses com a expansão em vez da sigla:** "descrito em linguagem (VHSIC Hardware Description Language -VHDL)" e "desenvolver um (Time-to-Digital Converters -TDC)". O padrão correto é "linguagem de descrição de hardware (*VHSIC Hardware Description Language* – VHDL)" ou "Nome por extenso (SIGLA)".
- O resumo começa com uma oração subordinada solta ("Tendo em vista que… assim como física de alta energia…"). O abstract é tradução literal e chega a errar termos ("thick delay" para atraso grosso, quando o usual é "coarse delay").
- O parágrafo-roteiro da introdução **não bate com a numeração real** das seções (cita 3.2/3.3 e 3.4 deslocados) e diz que o trabalho "está dividido em dois capítulos".
- Mistura de tempos verbais: "pretende-se obter" no objetivo convive com "foi apresentado" no roteiro.
- A Tabela 4 tem um valor deslocado (a coluna DEC ficou desalinhada).

---

## 3. Checklist derivado para o meu TCC II
- [ ] Decidir entre **Word (template `Modelo_TCC_II.doc`) e LaTeX/abnTeX2**. O Elton prova que abnTeX2 é aceito e o resultado sai mais limpo (sumário, listas e numeração automáticos).
- [ ] Capa e folha de rosto no mesmo layout, com o texto de natureza do trabalho copiado do template.
- [ ] Ficha catalográfica pelo site da biblioteca (biblioteca.unemat.br/gfc), conferindo o nome.
- [ ] Folha de aprovação **assinada e escaneada** na versão final.
- [ ] Resumo em parágrafo único (≤500 palavras) com objetivo, método, resultados e conclusão. Palavras-chave **separadas por ponto** (regra do template). Abstract revisado de verdade, não traduzido automaticamente.
- [ ] Lista de siglas conferida, sem desalinhamento.
- [ ] Capítulos sempre em página nova, cada um com uma seção de abertura e cabeçalho com o nome do capítulo.
- [ ] Figuras com legenda acima, fonte abaixo e citação no texto antes. Tabelas sem linhas verticais. Equações numeradas por capítulo.
- [ ] Introdução com contexto, problema, objetivos, justificativa e roteiro, e o roteiro **conferido com o sumário final**.
- [ ] Conclusão que responde à pergunta ou hipótese, assume as limitações e propõe trabalhos futuros.
- [ ] Revisão gramatical focada em concordância, mas/mais, crase e siglas.
