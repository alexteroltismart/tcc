# Contexto — Rosa, Terra & Drews (2019): modelagem pressão × vazão em barra de pulverização

Dois PDFs com **o mesmo trabalho**, um em cada idioma:

| arquivo | versão | publicação |
|---|---|---|
| `Pulverizador_Agricola_em_Barras_com_Apli.pdf` | **PT**: "Pulverizador Agrícola em Barras com Aplicação a Taxa Variada: Modelagem Física" | **XIV SBAI 2019** (Simpósio Brasileiro de Automação Inteligente, Ouro Preto, 27–30/out/2019), p. 2286–2291, **DOI 10.17648/sbai-2019-111478**. Primeira autora: Gabrielle R. A. Rosa |
| `Fabio.pdf` | **EN**: "Evaluation of the Pressure-Flow Relationship in a Boom of an Autonomous Robotic Agricultural Sprayer" | Formato de conferência **IEEE** (2 colunas, tamanho carta, referências numeradas). O evento **não aparece no PDF**, que foi gerado em jan/2020. Primeiro autor: **Fabio P. Terra** |

- **Autores:** Gabrielle R. A. da Rosa, Fabio P. Terra e Paulo L. J. Drews Jr, do NAUTEC/C3 da FURG (Rio Grande, RS). Terra também é do IFSul (Pelotas).
- **Financiamento:** FAPERGS, proc. 17/2551-0000896-0, dentro do projeto **AutoCERES**, que busca uma solução de baixo custo para a agricultura familiar.
- **Relação com o meu TCC:** é a **referência mais próxima do meu problema**: pressão e vazão numa barra com controle bico a bico e alimentação em série. Ela já aparece no `04.docx` como "DA ROSA, 2019" (Figura 2) e está nas referências como ROSA; TERRA; DREWS-JR.

---

## 1. Ideia do artigo
O controle por seções não resolve trechos menores que uma seção nem falhas na linha de plantio. Por isso o artigo trata do **controle bico a bico**, que pode ser **em paralelo** (cada bico com sua própria mangueira até o tanque) ou **em série** (uma linha-tronco, o *header*, alimenta todos os bicos; é o caso do Jacto Omni 700). Quando os bicos abrem e fecham, a vazão consumida muda, a pressão na barra varia e o **tamanho de gota** se altera (Holterman, 2016). Os autores:
1. modelam a barra como um conjunto de **resistências fluídicas quadráticas**;
2. caracterizam em bancada uma barra de 7 bicos;
3. mostram que uma **válvula de alívio/agulha** consegue trazer a pressão de volta ao setpoint.

Eles apontam que Mercaldi et al. (2017) supõem pressão uniforme na barra, sem perda de carga, e contestam essa hipótese citando Delmée (2003). A ironia é que o próprio experimento deles acabou mostrando pressão praticamente uniforme (ver §3).

## 2. Modelo matemático (seção 2 PT / II EN)
Regime de escoamento pelo **número de Reynolds**: `Re = ρ·dᵢ·v/μ`. Escoamento laminar para Re < 1100 e turbulento para Re > 3500, segundo Garcia (2005); entre esses valores, transitório. O escoamento foi assumido **estacionário**, com Bernoulli e continuidade e com h₁ = h₂ (barra na horizontal).

| eq. | expressão | significado |
|---|---|---|
| (2)–(3) | `P₁ + ½ρv₁² = P₂ + ½ρv₂²` | Bernoulli sem diferença de altura |
| (5) | `A₁v₁ = A₂v₂` | continuidade (fluido incompressível) |
| (7) | `Q = A₁·√(2ΔP / (ρ[(A₁/A₂)² − 1]))` | vazão teórica numa restrição |
| (8) | `C_D = Q_real / Q_teórica` | coeficiente de descarga, obtido experimentalmente (vena contracta) |
| (9) | `Q = C_D·A₁·√(…)` | vazão real |
| **(10)** | **`ΔP = R_F·Q²`** | **resistência fluídica** [kPa/(L/min)²]; 1 m³/s = 60 000 L/min |
| (11) | `R_F,D = ρ / (2·C_D²·Aᵢ²)` | elementos "deprimogênios": **bicos e válvulas** (Felizardo et al., 2016) [kg/m⁷] |
| (12) | `R_F,T = f_a·L·ρ / (2·dᵢ·Aᵢ²)` | trecho de tubo; `f_a` vem do **diagrama de Moody** (depende de Re) |
| **(13)** | **`P_S = (R_F,D + R_F,T)·Q²`** | pressão do sistema, com base no conceito de Steward & Humburg (2000) |
| (14) | `R_F(n) = 42,59·e^(−2,335n) + 2,307·e^(−0,4591n)` | **ajuste empírico** da resistência equivalente em função do número de bicos abertos *n* |

O diagrama de blocos (Fig. 4 PT / Fig. 5 EN) mostra Q, R_F,D e R_F,T entrando, com Q elevado ao quadrado, os R somados e o produto resultando em P_S. É um modelo **estático**, sem dinâmica: não tem capacitância, inércia nem atraso de válvula.

## 3. Bancada experimental (FURG/C3)
- Reservatório de 100 L e **bomba de pistão** (deslocamento positivo) de 14 L/min, acionada por **motor elétrico com inversor de frequência**, que simula a TDP do trator.
- **Barra de 5 m com 7 bicos em série.** Bicos leque Hypro **FanTip 0,2 / 110°**, que segundo o fabricante dão ≈0,92 L/min a 4 bar.
- **Instrumentação com tags ISA 5.1:**
  - transmissores de pressão PT-01 e PT-02, piezorresistivos **HK1100C**;
  - medidores de vazão FT **YF-S201** (turbina/efeito Hall, de baixo custo);
  - manômetro PG;
  - válvula reguladora **agulha 1/4" acionada por servomotor**, chamada de PV no texto em português e de HV no texto em inglês;
  - **7 solenoides on/off** (XV), uma por bico, com anti-gotejo.
- Aquisição e comandos feitos com **ATmega2560 (Arduino Mega)**.

**Tabela 1: válvula de recirculação fechada, n bicos abertos**

| n | ΔP [kgf/cm²] | Q [L/min] | R_F eq = ΔP/Q² |
|---|---|---|---|
| 7 | 3,57 | 5,60 | 0,114 |
| 6 | 3,88 | 5,07 | 0,151 |
| 5 | 4,24 | 4,40 | 0,219 |
| 4 | 4,64 | 3,60 | 0,358 |
| 3 | 4,96 | 2,80 | 0,633 |
| 2 | 5,27 | 2,00 | 1,318 |
| 1 | 5,58 | 1,00 | 5,580 |

- PT-01 e PT-02 marcaram valores **muito próximos**, ou seja, a perda de carga **ao longo** da barra é desprezível nessas condições.
- O **Re** cresce de forma quase linear, de ~1700 com 1 bico a ~9400 com 7 bicos (Fig. 11 PT / Fig. 12 EN). O regime passa de transitório/laminar para turbulento.
- **Ensaio dinâmico com a válvula reguladora (Fig. 12 PT / Fig. 13 EN):**
  1. Partindo de 4,00 kgf/cm² com a válvula fechada, fechar os bicos 1, 4 e 7 leva a pressão a **5,80**.
  2. Abrir a válvula **11%** traz a pressão para **4,40**.
  3. Fechar também os bicos 2, 3 e 5 leva a pressão a **6,10**.
  4. Abrir a válvula **33%** traz a pressão de volta a **≈4,00**.
  - Conclusão dos autores: **regular a abertura de uma válvula de alívio do excedente da bomba controla a pressão na barra.** Nesse ensaio a válvula foi ajustada **manualmente, em malha aberta**.

## 4. Conclusões e trabalhos futuros (dos autores)
- Sensores de baixo custo deram medições confiáveis.
- A variação de pressão com o número de bicos abertos é evidente, e a válvula reguladora é uma solução viável.
- **Futuro:** colocar a **válvula de controle no modelo (eq. 13)** e aplicar **controle em malha fechada**; levantar curvas de outros bicos (leque, cone vazio, cone cheio) e de barras com mais bicos.
- Em outras palavras, **o artigo para exatamente onde o meu TCC começa** (modelo com atuador, controlador e validação).

## 5. Diferenças entre PT e EN
- **EN acrescenta:**
  - definição de deriva (Dexter, 1995);
  - fatores de aplicação (vento, UR, temperatura, escolha de ponta) com citação de Jacto e Cruvinel (2016);
  - uma figura do método convencional;
  - Evenson & Gollin (2003) e Wheeler (2002) sobre a Revolução Verde;
  - a motivação "robótica autônoma + **visão de máquina** comandando os bicos";
  - multas por sobreaplicação;
  - a menção à TDP;
  - os tipos de bico como trabalhos futuros.
- **PT tem a mais:** o custo "> R$ 800 mil" (Araújo, 2016), substituído no EN por "several thousands of dollars"; agradecimento ao Prof. André Oldoni (IFSul).
- **Nome da válvula reguladora:** PV (PT) × HV (EN). O EN também identifica as solenoides como XV.
- **Erro de digitação no EN:** na Tabela I, a linha n = 2 traz Q = 1,00 L/min. O PT, que é o correto, traz **2,00** (confirmado pelo cálculo 5,27/2² = 1,318).
- **Unidades:** o EN registra que 4,0 bar = 4,079 kgf/cm². Cuidado, porque os dois textos chamam a coluna de pressão de ΔP e de P indistintamente; são **pressões manométricas**.
- **Citação:** o PT usa autor-data (estilo SBAI) e o EN usa numeração [n] (IEEE).

---

## 6. Observações minhas (úteis para o TCC)

**a) Modelo físico melhor que a eq. (14).** Dividindo a vazão pelo número de bicos e por √P, obtém-se uma constante: `q_bico = K·√P`, com **K ≈ 0,425 (L/min)/√(kgf/cm²)** em todos os 7 casos (0,418–0,436). Isso é a lei de orifício de cada bico. Como os n bicos estão **em paralelo** do ponto de vista hidráulico:

```
R_eq(n) = 1/(n·K)² = R₁/n²     (R₁ = 5,58)
```

Esse modelo **reproduz a tabela tão bem quanto a dupla exponencial (14) ou melhor**: para n = 7 dá 0,114 (medido 0,114), enquanto a eq. (14) dá 0,093. Além disso, ele tem **um único parâmetro com significado físico** (o K da ponta, que vem do catálogo). A eq. (13) soma R_F,D + R_F,T **em série** e não deixa explícito que os bicos ficam em **paralelo**. Esse é um ponto que posso explorar no meu modelo.

**b) Coerência com o catálogo:** com P ≈ 4 kgf/cm², a vazão sai a ~0,85–0,9 L/min por bico, perto dos 0,92 L/min do fabricante a 4 bar.

**c) Pergunta em aberto:** a bomba de pistão é de 14 L/min, mas com a recirculação fechada passam só 1–5,6 L/min. Deve haver um **alívio/regulador interno no conjunto da bomba**. O artigo não explica isso, e é algo a considerar se eu for modelar a bomba.

**d) O que o artigo NÃO tem e o meu TCC deve ter:**
- dinâmica: transitório de pressão e tempo de resposta da solenoide e da válvula;
- modelo do atuador (válvula/rotação da bomba);
- controlador (PID) e sintonia;
- simulação em malha fechada;
- validação com **dados de campo de máquina real** (logs) e não só de bancada;
- barra comercial com dezenas de bicos, onde a perda de carga ao longo do header pode deixar de ser desprezível.

**e) Alerta de originalidade:** vários trechos do `04.docx` estão **praticamente iguais** ao texto deste artigo:
- o parágrafo das restrições hidráulicas e resistências fluídicas (Garcia, 2005);
- o parágrafo pressão-vazão-gota (Holterman, 2016);
- o dado do INCA de 5 L/hab/ano (Milhorance, 2015).

Preciso **reescrever com palavras próprias** e citar *Rosa, Terra e Drews Jr (2019)* como fonte direta, já que as citações de Garcia e Holterman foram herdadas daqui. Também convém **ler as fontes originais** antes de citá-las diretamente.

**f) Referências daqui que valem buscar:**
- **Garcia (2005)**, o livro-base de resistência fluídica;
- **Felizardo et al. (2016, ASABE)**;
- **Mercaldi et al. (2017, IFAC)**: regulação de vazão e pressão com solenoides;
- **Steward & Humburg (2000)**: modelagem de pulverizador com injeção;
- Hughes (2002);
- Bega et al. (2006): instrumentação e diagrama de Moody;
- **ISA 5.1** para os tags do fluxograma.

## Como citar (ABNT)
ROSA, G. R. A. da; TERRA, F. P.; DREWS JR, P. L. J. Pulverizador agrícola em barras com aplicação a taxa variada: modelagem física. In: SIMPÓSIO BRASILEIRO DE AUTOMAÇÃO INTELIGENTE, 14., 2019, Ouro Preto. **Anais** [...]. Campinas: Galoá, 2019. p. 2286-2291. DOI: 10.17648/sbai-2019-111478.

Para a versão EN, falta o nome do evento. Antes de citar, preciso buscá-lo (Google Scholar/IEEE Xplore, pelo título).
