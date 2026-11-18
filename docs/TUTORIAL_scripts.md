# Tutorial: como rodar os scripts do TCC

Este guia mostra, passo a passo, como gerar todos os resultados do TCC a partir dos arquivos-fonte: a simulação, as figuras, o Word e o PDF. Os comandos estão em ordem: se você seguir de cima para baixo, termina com `docs/08.docx` e `docs/08.pdf` atualizados.

Pasta do projeto: `D:\tech\tcc`. Todos os caminhos abaixo partem dela.

---

## 1. O que precisa estar instalado

| Programa | Para quê | Como conferir |
|---|---|---|
| Python 3.12 (comando `py -3`) | simulação, conversor Markdown → Word, Figura 7 | `py -3 --version` |
| numpy e matplotlib | contas e gráficos da simulação | `py -3 -c "import numpy, matplotlib"` |
| Microsoft Word 16 | equações, sumário, listas e PDF | abrir o Word normalmente |
| Graphviz (comando `dot`) | Figuras 6 e 8 | `dot -V` |
| pdftoppm (vem com o MiKTeX) | opcional: transformar páginas do PDF em imagem para conferir | `pdftoppm -v` |

Se faltar numpy ou matplotlib:

```
py -3 -m pip install --user numpy matplotlib
```

**Dica do Windows.** Se aparecer erro de acento ou de letra grega (α, τ) no terminal, rode antes:

- PowerShell: `$env:PYTHONIOENCODING = "utf-8"`
- Git Bash: `export PYTHONIOENCODING=utf-8`

---

## 2. Visão geral: o que gera o quê

```
simulacao/modelo_barra.py ──► simulacao/resultados.json
                          └─► simulacao/figuras/*.png   (Figuras 9 a 14)

build/fig/fig06.dot ──(dot)──► build/fig/fig06.png      (Figura 6)
build/fig/fig07.py  ─────────► build/fig/fig07.png      (Figura 7)
build/fig/figA1.dot ──(dot)──► build/fig/figA1.png      (Figura 8)

img/*.png  (fotos e figuras do artigo de referência)    (Figuras 1 a 5)

contexto/08.md + todas as figuras
    └─ build/md2docx.py 08 ──► build/08_raw.docx
         └─ build/post.ps1 ──► docs/08.docx + docs/08.pdf
```

O texto do TCC é escrito em `contexto/08.md`. O Word e o PDF **nunca** são editados à mão: eles são sempre gerados de novo a partir do `.md`.

---

## 3. Passo 1: rodar a simulação

Na pasta `D:\tech\tcc`:

```
py -3 simulacao/modelo_barra.py
```

Demora cerca de 1 a 2 minutos. O programa:

1. ajusta o modelo estático aos dados da Tabela 1 (K e curva da fonte);
2. faz a validação cruzada "deixa um de fora";
3. mede o ganho K_g e calcula a sintonia do PI (K_c, T_i) e as margens;
4. simula os cenários C1, C2, C3 e C4 (erro de modelo) e a varredura de velocidade da válvula;
5. grava os resultados e as figuras.

**Saídas:**

| Arquivo | Conteúdo | Onde aparece no TCC |
|---|---|---|
| `simulacao/resultados.json` | todos os números | Capítulo 4 |
| `simulacao/figuras/a_resistencia_n.png` | resistência × número de bicos | Figura 9 |
| `simulacao/figuras/b_fonte_carga.png` | curva da fonte e curvas de carga | Figura 10 |
| `simulacao/figuras/c_C1.png` | cenário C1 | Figura 11 |
| `simulacao/figuras/c_C2.png` | cenário C2 | Figura 12 |
| `simulacao/figuras/d_C3.png` | cenário C3 | Figura 13 |
| `simulacao/figuras/e_C4_erro_modelo.png` | cenário C4 | Figura 14 |

**Como saber se deu certo.** O programa imprime um resumo na tela. As primeiras linhas devem ser:

```
K = 0.4251  fonte: a2=-0.0355 a1=-0.2018 a0=5.815  erro max P=0.73% Q=2.27%
LOO: erro max P=0.92% Q=2.66%
```

e mais abaixo:

```
PI: λ=0.2  Kc=0.3342 /(kgf/cm²)  Ti=0.200 s  ...  MF=83.6°  MG=23.0 dB
```

O programa tem conferências automáticas. Se algum dado ou fórmula for alterado e quebrar o modelo, ele **para com uma mensagem de erro** (`AssertionError`) em vez de gerar figuras erradas. As conferências são:
- K precisa dar 0,425, com erros abaixo de 0,75% na pressão e 2,3% na vazão;
- a pressão de referência precisa ser atingível com 7 bicos;
- K_g não pode variar mais de 2% entre os números de bicos;
- T_i não pode ser menor que o período de amostragem.

**Para mudar um parâmetro** (por exemplo, a velocidade da válvula), edite o bloco 2 do `modelo_barra.py`:

```python
P_REF = 3.5          # pressão de referência [kgf/cm²]
KV_MAX = 3.5         # constante da válvula toda aberta
BASE = {"tau_a": 0.2, "w_max": 0.5}   # atraso e velocidade máxima da válvula
TS = 0.05            # período do controlador [s]
DT = 1e-3            # passo da simulação [s] (não aumentar: 10 ms distorce o C3)
LAMBDA = 0.2         # constante de tempo desejada para a malha fechada [s]
```

Depois rode o programa de novo e siga os passos 3 e 4 para atualizar o Word. **Atenção:** os números do texto (`contexto/08.md`) não mudam sozinhos. Se os resultados mudarem, é preciso atualizar as tabelas e os parágrafos do Capítulo 4 à mão.

---

## 4. Passo 2: gerar as figuras de diagrama (só se elas forem alteradas)

Estas figuras só precisam ser geradas de novo se você editar os arquivos delas. Os PNGs já estão prontos em `build/fig/`.

Na pasta `D:\tech\tcc\build`:

```
dot -Tpng fig/fig06.dot -o fig/fig06.png
dot -Tpng fig/figA1.dot -o fig/figA1.png
py -3 fig/fig07.py
```

| Arquivo-fonte | Figura | Observação |
|---|---|---|
| `fig/fig06.dot` | Figura 6: circuito hidráulico equivalente | Graphviz; use `<SUB>` para índices, porque a fonte Arial não tem os caracteres de subscrito |
| `fig/fig07.py` | Figura 7: diagrama de blocos do controle | matplotlib; **precisa ser rodado de dentro de `build/`**, porque salva em `fig/fig07.png` |
| `fig/figA1.dot` | Figura 8: fluxo do programa | Graphviz |

No `.md`, essas figuras aparecem como blocos ```` ```mermaid ````. O conversor ignora o código mermaid e coloca no lugar o PNG correspondente, escolhido pelo número da figura.

As Figuras 1 a 5 são imagens prontas em `img/` (`sprayer.png`, `fig02_secoes_bicos.png`, `fig03_diagrama_resistencias.png`, `fig04_fluxograma.png`, `fig05_ensaio.png`). Para trocar uma delas, basta substituir o arquivo. Use nomes **sem espaço e sem acento**.

---

## 5. Passo 3: converter o texto para Word

Na pasta `D:\tech\tcc\build`:

```
py -3 md2docx.py 08
```

O número é a versão: ele lê `contexto/08.md` e grava `build/08_raw.docx`. A saída esperada é algo como:

```
D:\tech\tcc\build\08_raw.docx: 14 imagens, 32 equações
```

O conversor:
- copia do modelo `build/Modelo_TCC_II.docx` os estilos, a capa, a folha de rosto, a folha de aprovação e a ficha;
- transforma títulos, parágrafos, listas, tabelas, legendas e imagens;
- converte as equações em LaTeX (`$$ ... \tag{3.9}$$`) para o formato de equação do Word;
- ignora o bloco `# NOTAS DE REVISÃO` do final.

Esse `_raw.docx` ainda **não** é o arquivo final: as equações estão em forma "linear" e o sumário está vazio.

---

## 6. Passo 4: finalizar no Word e gerar o PDF

Ainda na pasta `D:\tech\tcc\build`:

```
powershell -NoProfile -ExecutionPolicy Bypass -File post.ps1 -Versao 08
```

O script abre o Word em segundo plano (sem mostrar a janela) e:
1. monta as equações (`BuildUp`);
2. atualiza os campos: numeração de figuras, tabelas e quadros, sumário e listas;
3. salva `docs/08.docx` e exporta `docs/08.pdf`.

A saída esperada:

```
equacoes: 32
paginas: 68
```

**Se der erro:**
- feche o `08.docx` ou o `08.pdf` se estiverem abertos no Word ou num leitor de PDF, porque o arquivo fica bloqueado;
- se o Word ficou "preso" de uma execução anterior, feche o processo `WINWORD.EXE` no Gerenciador de Tarefas e rode de novo.

---

## 7. Passo 5 (opcional): conferir o PDF

Para ver as páginas como imagem, por exemplo das páginas 38 a 44:

```
pdftoppm -jpeg -r 70 -f 38 -l 44 ../docs/08.pdf pg/p
```

As imagens saem em `build/pg/`.

Um erro comum do conversor é uma equação "engolir" o começo do parágrafo seguinte. Para procurar esse problema no Word gerado (pasta `D:\tech\tcc`):

```
py -3 -c "import zipfile,re; x=zipfile.ZipFile(r'docs\08.docx').read('word/document.xml').decode('utf8'); print('grudadas:', len(re.findall(r'</m:oMathPara>(?:(?!</w:p>).)*?<w:r[ >]', x)))"
```

O resultado deve ser `grudadas: 0`.

---

## 8. Resumo: tudo de uma vez

PowerShell, a partir de `D:\tech\tcc`:

```
$env:PYTHONIOENCODING = "utf-8"
py -3 simulacao/modelo_barra.py
cd build
py -3 md2docx.py 08
powershell -NoProfile -ExecutionPolicy Bypass -File post.ps1 -Versao 08
cd ..
```

Resultado: `docs/08.docx` e `docs/08.pdf`.

---

## 9. Versões anteriores

**Versão 07** (com capacitância na linha e linearização). O script, os resultados e as figuras dela estão guardados em `simulacao/v07/`. Para rodar a simulação da 07 sem mexer na 08:

```
cd simulacao/v07
py -3 modelo_barra.py
```

Esse script grava em `simulacao/v07/resultados.json` e `simulacao/v07/figuras/`.

Para gerar o Word da 07 com as figuras certas, o conversor precisa achar as figuras da 07 nos lugares padrão:
1. copie `simulacao/v07/figuras/*.png` para `simulacao/figuras/`;
2. copie `simulacao/v07/fig06_v07.png`, `fig07_v07.png` e `figA1_v07.png` para `build/fig/`, renomeando para `fig06.png`, `fig07.png` e `figA1.png`;
3. rode `md2docx.py 07` e `post.ps1 -Versao 07`;
4. depois, rode o passo 1 (simulação da 08) e o passo 2 (figuras de diagrama) de novo para voltar às figuras da 08.

Os arquivos `docs/07.docx` e `docs/07.pdf` já prontos não precisam disso.

---

## 10. Scripts dos dados de campo (fora do TCC, por enquanto)

A pasta também tem scripts para os logs de pulverizadores em campo (Weedit/Jacto). Eles **não** são usados no TCC atual e precisam de bibliotecas extras (pandas, pyarrow, geopandas, rasterio, rasterstats). Os caminhos padrão dentro deles são de outro computador (`/home/shared/...`), então sempre passe o arquivo de log na linha de comando.

| Script | O que faz | Exemplo |
|---|---|---|
| `check.py` | Teste rápido dos dados de drone em `dados/` (GeoPackage + GeoTIFF) | `py -3 check.py` |
| `scripts/parse_log_manual.py` | Lê um log `.zip` e transforma em tabelas | `py -3 scripts/parse_log_manual.py LOG.zip` |
| `scripts/plot_log.py` | Gera 4 gráficos gerais do log (operação, contadores, bicos, GPS) | `py -3 scripts/plot_log.py LOG.zip --out plots` |
| `scripts/export_dataset.py` | Exporta o log numa grade regular de tempo (CSV, parquet, npz, mat) | `py -3 scripts/export_dataset.py LOG.zip --dt 100ms --out dataset` |
| `scripts/validate_plant_model.py` | Testa o modelo de bicos contra o dataset exportado | `py -3 scripts/validate_plant_model.py --data dataset/dataset.parquet` |
| `guides/fig_malha_jacto.py` | Figura da malha de bomba da Jacto a partir do log | `py -3 guides/fig_malha_jacto.py LOG.zip --members "20260831-040413*"` |
| `scripts/wip_control_stage.py` | Etapa de controle parada; **não roda** sozinho (não tem `main`) | — |

Ordem típica: `export_dataset.py` → `validate_plant_model.py`. Os outros são independentes.
