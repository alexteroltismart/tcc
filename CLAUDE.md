# TCC — controle de pressão em barra de pulverização bico a bico

Eng. Elétrica, UNEMAT Sinop. Autor: Alex de Jesus Terolti. Orientador: Prof. Dr. Rogério Bastos Quirino.
Título: *Modelagem de sistema de controle para pulverização agrícola de precisão*.

Tema: manter a pressão de uma barra com alimentação em série enquanto os bicos abrem e fecham,
usando uma válvula de alívio como atuador. Modelo de resistência fluídica + simulação em Python,
com parâmetros ajustados à bancada de 7 bicos de Rosa, Terra e Drews Jr (2019). Sem dado medido
no tempo: a parte dinâmica é estudo de projeto em simulação.

## Onde está cada coisa

| caminho | conteúdo |
|---|---|
| `contexto/NN.md` | texto da monografia, uma versão por arquivo (04–25). **A maior é a atual.** Markdown com LaTeX; no fim, "NOTAS DE REVISÃO" (remover antes da entrega) |
| `contexto/relatorio_banca*.md` | revisões simuladas da banca, com prioridades 🔴🟡🟢 |
| `contexto/*_20XX_*.md` | resumos das referências principais (Rosa 2019, Steward & Humburg 2000); `Brunetti_2008_formulas.md` = fórmulas de fluidos com nº/página conferidos, mapeadas às Eqs. do TCC |
| `referencias base/Brunetti_2008_Mecanica_dos_Fluidos.md` | texto integral do livro (extração automática; equações quebradas — conferir no PDF, pág. PDF = pág. livro + 16) |
| `referencias base/` | PDFs das referências (Rosa 2019 PT; `Fabio.pdf` = Terra, Rosa e Drews, "Evaluation of the Pressure-Flow Relationship…" — outro artigo do grupo, **não** é a versão EN do Rosa; Terra 2020 IFAC = `A_Low_Cost_Prototype…`; Steward 2000; Merritt; Ogata 2010; ISO 16122-1/-2) | |
| `simulacao/modelo_barra.py` | modelo, sintonia, cenários e figuras — **todos** os números do Cap. 4 saem daqui |
| `simulacao/v07/` | script/resultados da versão 07 (com capacitância da mangueira); não usar para números novos, só para a conferência da H6 |
| `simulacao/v09/` | script/resultados da versão 09 (sintonia lambda/SIMC, faixa ±5% na vazão) |
| `simulacao/v16/` | script/resultados da versão 16 (sintonia Ziegler-Nichols pelo ganho crítico) |
| `simulacao/v18/` | script/resultados da versão 18 (controlador amostrado a 50 ms) |
| `simulacao/v19/` | script/resultados da versão 19 (referência como 2ª entrada, superposição) |
| `simulacao/v20/` | script/resultados da versão 20 (antes das figuras da v21: linearização, plano s, resposta a um bico com e sem limite) |
| `simulacao/v21/` | script/resultados da versão 21 (com validação cruzada e quatro métricas: desvio máximo e acomodação) |
| `simulacao/v24/` | script/resultados da versão 24 (PI+FF sem antecipação) |
| `simulacao/v11/` | script/resultados da versão 11 (anti-windup também no limite de velocidade; C3 PI 5,0%) |
| `img/` | figuras dos capítulos 2–3 (fluxograma e ensaio da bancada vêm do artigo) |
| `build/` | conversão para Word e modelo da UNEMAT |
| `docs/NN.docx`, `docs/NN.pdf` | versões geradas para entrega |

## Comandos

```
py -3 simulacao/modelo_barra.py            # → simulacao/resultados.json, simulacao/figuras/
py -3 build/md2docx.py 20                  # contexto/20.md → build/20_raw.docx
powershell -File build/post.ps1 -Versao 20 # Word COM: monta equações, sumário, listas → docs/NN.docx/.pdf
```

`post.ps1` abre o Word por COM — precisa do Word instalado e fechado. O script da simulação
tem conferências automáticas (K = 0,425, erros do ajuste, Kg constante, Kg/Kn analíticos = numéricos para todo n,
ζ e ωn da função de transferência iguais aos especificados); se uma falhar, ele para — não contornar, investigar. Roda em ~3 min.
Display equation com `\tag{}` sai numerada; sem `\tag` sai como conta sem número (desde a v11).
Blocos ```python saem com cores de sintaxe.
Os fluxogramas (Figura 4 e Figuras 13–14 da v16) são `build/fig/*.dot` (`dot -Tpng`); os diagramas das Figuras 11 e 12 são `build/fig/fig06.png`/`fig07.py`.
Desde a v16 o **Apêndice A** é o `simulacao/modelo_barra.py` inteiro, copiado para o .md por script: mudou o script → regerar o apêndice (blocos de código do apêndice saem sem keepNext).

## Convenções do texto

- Nova versão = copiar `contexto/NN.md` para `NN+1.md`, editar, e registrar o que mudou em
  "NOTAS DE REVISÃO" (seção A<NN>). Mudou o script → rerodar e atualizar todas as tabelas,
  o Resumo/Abstract e a Conclusão com os números novos.
- Pressão em **kgf/cm²** (como na fonte), vazão em L/min. 1 kgf/cm² = 0,9807 bar.
- Citação ABNT autor-data. Marcar pendências como `[REF. PENDENTE]` / `[A CONFERIR]`.
- Linguagem simples, cada termo explicado na primeira vez, mas **impessoal e sem gíria**
  (a banca cobrou "decorando", "repare que", aspas coloquiais).
- Cenários: C1 (um bico por vez), C2 (sequência do ensaio de Rosa), C3 (aleatório).
  O C4 (erro de modelo) foi retirado na v13 por estar fora do escopo; não reintroduzir.
- Desde a v10: artigo base único é Rosa, Terra e Drews Jr (2019); Steward e Humburg só como
  uma frase em 2.6. Controle = P → PI → PI+FF, com o feedforward antecipado em 0,2 s desde a v25 (T_ANT no script; o FF sem antecipação só como comparação e na Fig. 22). Desde a v17 a sintonia é por **alocação de polos**
  (Ogata 5-3: ζ = 0,7, t_s = 0,5 s → Kc 0,827, Ti 0,084; P com o mesmo Kc). Ziegler-Nichols foi
  retirado por erro conceitual (planta de 1ª ordem: sem curva em S e sem oscilação contínua) e
  não deve ser mencionado no texto. Desde a v19 o sensor e o controlador leem a pressão **em tempo real** (a cada passo de 1 ms, sem amostragem; não reintroduzir T_s nem K_c,lim). Desde a v20 a malha em Laplace tem só o distúrbio ΔN, com a referência fixa (a 2ª entrada e a superposição da v18 saíram; não reintroduzir); Kg e Kn vêm da derivada implícita dP/dC (3.5.2). A parte de controle se apoia em Ogata (2010) e Castrucci, Bittar e Sales (2018) (`referencias base/castrucci.epub`, texto em `Castrucci_2018_Controle_Automatico.md`; o e-book não tem página: citar por seção). Faixa = ±10% na pressão (ISO 16122-2, 4.5.4).
  Sensor sem ruído (o número do teste de ruído saiu do texto na v20).
- Desde a v11: fórmulas de fluidos citadas pelo Brunetti (2008) (mapa em `contexto/Brunetti_2008_formulas.md`);
  uma equação por número; contas encadeadas vão em linhas `$$…$$` sem número, não no texto corrido.
- Desde a v12: anti-windup = integração condicional só no limite de posição (FERNANDES; GOLDEMBERG, 2001,
  `referencias base/Técnicas Anti-Windup (2001).pdf`).
- Testes avulsos citados no texto (H6 com mangueira, passo de 2/10 ms) ficam fora do script;
  mudou o controlador → refazê-los (`py -3 simulacao/testes_avulsos.py`, ~5 min; último: v19; anti-windup em `simulacao/teste_antiwindup.py`).
- Parâmetros **estimados** (τa, ωmax, curva da válvula) devem aparecer como estimados; não
  apresentar resultado dinâmico como validado.

## Fora da monografia (mesmo repositório)

- `scripts/`, `guides/`, `dev_logs/`: pipeline de logs de máquinas Weedit (John Deere e
  Jacto 3030/4530). Cada script tem um `*_explicado.md`. Não entra no texto do TCC atual
  (seria a "validação com registros de campo" dos trabalhos futuros).
- `dados/` (fora do git) + `check.py`: voos de pulverização (QField `.gpkg` + GeoTIFF COG,
  EPSG:32721). Armadilhas já resolvidas: o DN do raster é o valor físico (paletado, 0 =
  nodata; `speed_kmh` e `pressure_dbar` guardam ×10); a calibração por balanço de massa
  precisa somar **todos** os ids de voo da data; `taxa (L/ha)` do vetor é o setpoint, não o
  aplicado; a camada `app` é categórica e o significado das classes não foi confirmado.
  `check.py` é o smoke test desses dados.

## Ferramentas

Python 3 via `py -3` (Windows). Simulação usa só `numpy` e `matplotlib` — manter assim
(o texto diz que não há biblioteca de controle). Para os dados geoespaciais: `geopandas`,
`rasterio`, `rasterstats`; instalar com `pip install --user`.
