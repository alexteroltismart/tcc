# 2026-10-07 — Pipeline de log Weedit: suporte a Jacto 3030/4530 e processamento de 31/08

Scripts: `tcc/scripts/` (cópia de `claude_working/context_files/20260908/`).
Máquina analisada: WQR20250023 (Jacto, `machineModel` 7, 144 bicos, bitola 3900 mm),
Fazenda Santa Terezinha. Dados em `dados/Fazenda Santa Terezinha Máquina (WQR20250023)/`
(fora do git).

## 1. Identificação das máquinas Jacto

- `machineModel` 6, 7, 18, 22 = "Jacto 3030/4530" (`section-controller/src/canMap.cpp`).
- No bucket S3 local: WQR20240009 e WQB20200001 (7), WQR20250010 (18); WQR20250023 nos dados do TCC.

## 2. O que mudou nos scripts (commit `36bc775` no tcc)

| Script | Mudança |
|---|---|
| `parse_log_manual.py` | `read_txts`: zip com pastas e vários `.txt`, ou `.txt` solto; `--members GLOB`; `profiles` gravado como string `"{}"` não quebra mais; bitola lida de `# Bitola:`; 7 IDs CAN Jacto; contexto em `df.attrs`; `--selftest` (JD + Jacto) |
| `plot_log.py` | painéis Jacto (vazão/PWM da bomba, rpm), legenda numa linha, `--members`, título com a máquina |
| `export_dataset.py` | unidades Jacto; metadata com `machine_model`, `files`, `flow_measured` (null na Jacto) |
| `validate_plant_model.py` | `--flow auto|coluna`; recusa a H2 quando não há vazão medida na barra |
| `*_explicado.md`, `weedit_log.md` §12 | atualizados para a versão nova |

IDs CAN Jacto (de `Update_Secrets.py`): `1AFFFFF9` (pressão ×6,89476 psi→kPa, velocidade),
`1AFFFFED` (pump_rpm), `1AFFFFFC` (pump_flow), `1AFFFFFF` (engine_rpm), `1888888ADE`,
`1888888A77`, `18888888AA` (flow_lmin).

Regressão JD garantida: `dataset.csv` do WQR20230004 com md5 `7c2e66416a93429619a5006ddea6598f`
e `metrics.json` idênticos antes e depois.

## 3. Achados sobre a Jacto

- **Não há vazão medida na barra.** `flow_lmin` (`18888888AA`) = `predicted_flow` (corr 0,999,
  sem atraso; cai para ~1,4 L/min quando os bicos fecham). `pump_flow`/`sent_machine_flow` são a
  vazão total da bomba, com o retorno (corr 0,07 com N·√P). `Flowmeter` dos detalhes vem zerado.
  → a validação do modelo de orifício (H2) é circular na Jacto.
- **Pressão confiável:** `can_pressure` bate com o sensor Weedit (corr 0,985).
- Unidades de `can_speed` e `pump_rpm` não documentadas.

## 4. Processamento de 31/08/2026 (36 logs, 303 MB)

Saída em `dados/.../saida_20260831/`.

- Os logs cobrem ~210 min numa janela de 13,5 h: intervalos sem mensagens WDT de 34 min (03:01),
  5,4 h (05:48) e 4,7 h (11:35). O logger continua no mesmo arquivo depois da parada, e o último
  arquivo tem ~6.500 linhas com hora 02:59 (relógio não sincronizado).
- **O `export_dataset.py` repete o último valor (ZOH) sem limite pelos intervalos** — o dataset do
  dia inteiro ficou ~75 % artificial e foi apagado. Processado por bloco com o driver
  `saida_20260831/blocos_20260831.py` (usa as funções dos scripts sem alterá-los):

| Bloco | Duração | Pulverizando | H1 pressão vs alvo 460 kPa | Vazão 1 s (estimada, só referência) |
|---|---|---|---|---|
| b1 03:35–05:48 | 133 min | 65 % | +7,6 %, RMSE 102 kPa, 421 amostras > 1000 kPa | R² 0,52 |
| b2 11:13–11:35 | 24 min | 0 % | — | — |
| b3 16:19–17:08 | 49 min | 29 % | −2,0 %, RMSE 34 kPa | R² 0,85 |

- Em 31/08 só houve alvo de 460 kPa pulverizando: o teste de troca de alvo continua sem dado.
  A única troca do pacote (490→450→410) é em 03/09 03:22–03:49, com a máquina quase sem bicos
  abertos — alvo e carga confundidos.

## 5. `nozzles.png`: pressão e vazão + eixo de tempo real (não commitado)

- Os heatmaps espalhavam as amostras igualmente pelo eixo X (`imshow` com `extent` do 1º ao último
  instante), o que escondia os intervalos sem log. Novo `on_grid` põe todas as camadas numa grade de
  tempo real comum; intervalo sem log fica em branco.
- Dois painéis de linha no fim: Pressão (kPa) e Vazão (L/min), mesmas séries do `overview.png`,
  alinhados com os heatmaps; passo mínimo de 0,5 s.
- `layout="constrained"` com coluna própria para as colorbars (larguras iguais).
- Artefato conhecido, não corrigido: o `get_details` do parser preenche os intervalos sem mensagem
  (`ffill/bfill` + `nearest`), por isso a pressão do sensor Weedit aparece em 0 kPa de 06:00 a 14:00.

## Pendências

- [ ] Commit da mudança do `plot_log.py`/`plot_log_explicado.md` (item 5) no tcc.
- [ ] Copiar o `plot_log.py` novo para `context_files/20260908/`.
- [ ] `export_dataset.py`: limitar o ZOH (ex.: `--max-hold 5s`) ou recorte por horário no `convert`.
- [ ] `get_details`: não preencher além de um limite de tempo.
- [ ] Confirmar a origem do `flow_lmin` com quem conhece a placa STM / Jacto.
- [ ] Achar log Jacto com troca de pressão alvo sob carga.
- [ ] Push do tcc: bloqueado pela permissão do Claude Code — rodar `git push` manualmente.
- [ ] Imagem de satélite de fundo no `gps.png`: plano feito, implementação descartada por ora.
