# BRUNETTI, F. *Mecânica dos Fluidos*. 2. ed. rev. São Paulo: Pearson Prentice Hall, 2008.

> Texto extraído automaticamente do PDF (`referencias base/Mecânica dos Fluidos ... Brunetti ...pdf`, 448 p.).
> `<!-- p. N -->` marca o início da página N do livro (página do PDF = N + 16).
> **Equações, tabelas e figuras saem quebradas na extração**: conferir sempre no PDF antes de citar.
> Resumo do que interessa ao TCC: `contexto/Brunetti_2008_mecanica_fluidos.md`.

<!-- p. pré-5 -->
São Paulo Brasil Argentina Colômbia Costa Rica Chile Espanha Guatemala México Peru Porto Rico Venezuela ASSOCIAÇÃO BRASILEIRA DE DIREITOS REPROGRÁFICOS

<!-- p. pré-6 -->
© 2008, 2005 Franco Brunetti Todos os direitos reservados. Nenhuma parte desta publicação poderá ser reproduzida ou transmitida de qualquer modo ou por qualquer outro meio, eletrônico ou mecânico, incluindo fotocópia, gravação ou qualquer outro tipo de sistema de armazenamento e transmissão de informação, sem prévia autorização, por escrito, da Pearson Education do Brasil. Diretor editorial: Roger Trimer Gerente editorial: Sabrina Cairo Supervisor de produção: Marcelo Françozo Editora: Eugênia Pessotti Revisão: Maria Luiza Favret Capa: Alexandre Mieda Composição editorial: ERJ Composição Editorial Dados Internacionais de Catalogação na Publicação (CIP) (Câmara Brasileira do Livro, SP, Brasil) Brunetti, Franco Mecânica dos fluidos / Franco Brunetti. — 2. ed. rev. — São Paulo : Pearson Prentice Hall, 2008.

ISBN 978-85-7605-182-4 1. Mecânica dos fluidos I. Título.

08-01989 CDD-620.106 Índice para catálogo sistemático:

1. Mecânica dos fluidos aplicada: Engenharia 620.106 2008 Direitos exclusivos para a língua portuguesa cedidos à Pearson Education do Brasil, uma empresa do grupo Pearson Education Av. Ermano Marchetti, 1435 CEP: 05038-001 – São Paulo – SP Fone: (11) 2178-8686 – Fax: (11) 2178-8688 e-mail: vendas@pearsoned.com

<!-- p. pré-7 -->
Capítulo 3 z z5 A minha esposa Ana Maria, a minhas filhas Claudia e Angela, a meus netos Alice, Andrey e Ariane de quem subtraí horas de convívio para este trabalho. A meus colegas professores, pelo incentivo, pelo auxílio e pelas sugestões.

A meus ex-alunos, alunos, futuros alunos e para todos os que utilizam este livro, esperando que seja útil durante o período escolar e na vida profissional.

<!-- p. pré-8 -->
<!-- p. pré-9 -->
Prefácio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . XIII Capítulo 1 Introdução, definição e propriedades dos fluidos . . . . . . . . . . . . . . . . . . . . . . . . . . . 1 1.1 Introdução . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1 1.2 Conceitos fundamentais e definição de fluido . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1 1.3 Tensão de cisalhamento — Lei de Newton da viscosidade. . . . . . . . . . . . . . . . . . . . 3 1.4 Viscosidade absoluta ou dinâmica . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4 1.5 Simplificação prática . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5 1.6 Massa específica (ρ) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8 1.7 Peso específico (γ). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8 1.8 Peso específico relativo para líquidos (γr). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9 1.9 Viscosidade cinemática (ν) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9 1.10 Fluido ideal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10 1.11 Fluido ou escoamento incompressível . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10 1.12 Equação de estado dos gases . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10 Exercícios. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11 Capítulo 2 2.1 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9 Estática dos fluidos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18 Pressão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18 Teorema de Stevin . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19 Pressão em torno de um ponto de um fluido em repouso . . . . . . . . . . . . . . . . . . . 20 Lei de Pascal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21 Carga de pressão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22 Escalas de pressão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23 Unidades de pressão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24 O barômetro . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25 Medidores de pressão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26 2.9.1 Manômetro metálico ou de Bourdon. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26 2.9.2 Coluna piezométrica ou piezômetro . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27 2.9.3 Manômetro com tubo em U . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27 2.9.4 A equação manométrica . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

<!-- p. pré-10 -->
VIII z Mecânica dos Fluidos 2.10 Força numa superfície plana submersa . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30 2.11 Centro das pressões . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32 2.12 Força em superfícies reversas, submersas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35 2.12.1 Componente horizontal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35 2.12.2 Componente vertical . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36 2.13 Empuxo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36 2.14 Flutuador — Nomenclatura . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37 2.15 Estabilidade. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38 2.16 Estabilidade vertical . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38 2.16.1 Corpo totalmente submerso em equilíbrio . . . . . . . . . . . . . . . . . . . . . . . . . . . 38 2.16.2 Corpo parcialmente submerso em equilíbrio . . . . . . . . . . . . . . . . . . . . . . . . . 38 2.17 Estabilidade à rotação . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39 2.17.1 Corpo totalmente submerso, em equilíbrio . . . . . . . . . . . . . . . . . . . . . . . . . . 39 2.17.2 Corpo parcialmente submerso, em equilíbrio . . . . . . . . . . . . . . . . . . . . . . . . 40 2.18 Equilíbrio relativo — Introdução. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43 2.19 Recipiente com movimento de translação uniformemente acelerado segundo a horizontal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43 2.20 Recipiente com movimento de translação uniformemente acelerado segundo a vertical . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46 2.21 Recipiente com movimento de translação uniformemente acelerado ao longo de um plano inclinado. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46 2.22 Recipiente com movimento de rotação de velocidade angular ω constante . . . . 48 Exercícios. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50 Capítulo 3 3.1 3.2 3.3 3.4 3.5 3.6 3.7 Cinemática dos fluidos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67 Regimes ou movimentos variado e permanente . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67 Escoamentos laminar e turbulento . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68 Trajetória e linha de corrente . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69 Escoamento unidimensional ou uniforme na seção . . . . . . . . . . . . . . . . . . . . . . . . . 71 Vazão — Velocidade média na seção . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72 Equação da continuidade para regime permanente . . . . . . . . . . . . . . . . . . . . . . . . . 74 Velocidade e aceleração nos escoamentos de fluidos. . . . . . . . . . . . . . . . . . . . . . . . 76 Exercícios. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78 Capítulo 4 Equação da energia para regime permanente . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85 4.1 Introdução . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85 4.2 Tipos de energias mecânicas associadas a um fluido . . . . . . . . . . . . . . . . . . . . . . . . 85 4.3 Equação de Bernoulli. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87 4.4 Equação da energia e presença de uma máquina . . . . . . . . . . . . . . . . . . . . . . . . . . . 90 4.5 Potência da máquina e noção de rendimento . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92 4.6 Equação da energia para fluido real . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95 4.7 Diagrama de velocidades não-uniforme na seção . . . . . . . . . . . . . . . . . . . . . . . . . . 97 4.8 Equação da energia para diversas entradas e saídas e escoamento em regime permanente de um fluido incompressível, sem trocas de calor . . . . . . . . . . . . . . . 100 4.9 Interpretação da perda de carga . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102 4.10 Equação da energia geral para regime permanente . . . . . . . . . . . . . . . . . . . . . . . . 105 Exercícios. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107

<!-- p. pré-11 -->
Capítulo 5 5.1 5.2 5.3 5.4 5.5 Equação da quantidade de movimento para regime permanente . . . . . . . . . . . . 121 Introdução . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121 Equação da quantidade de movimento . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121 Método de utilização da equação . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124 Forças em superfícies sólidas em movimento . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127 Equação da quantidade de movimento para diversas entradas e saídas em regime permanente . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130 Exercícios. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132 Capítulo 6 Análise dimensional — semelhança . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141 6.1 Introdução . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141 6.2 Grandezas fundamentais e derivadas. Equações dimensionais . . . . . . . . . . . . . . 141 6.3 Sistemas coerentes de unidades. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143 6.4 Números adimensionais . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144 6.5 Vantagem da utilização dos números adimensionais na pesquisa de uma lei física . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144 6.6 Teorema dos π . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147 6.7 Alguns números adimensionais típicos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150 6.8 Semelhança ou teoria dos modelos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151 6.9 Escalas de semelhança. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152 6.10 Relações entre escalas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152 Exercícios. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156 Capítulo 7 Escoamento permanente de fluido incompressível em condutos forçados . . . . 163 7.1 Introdução . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163 7.2 Definições . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163 7.2.1 Condutos – Classificação . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163 7.2.2 Raio e diâmetro hidráulico . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164 7.2.3 Camada limite numa placa plana. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164 7.2.4 Desenvolvimento da camada limite em condutos forçados . . . . . . . . . . . 167 7.2.5 Rugosidade . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168 7.2.6 Classificação das perdas de carga . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168 7.3 Estudo da perda de carga distribuída (hf) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169 7.4 Fórmula da perda de carga distribuída . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173 7.5 Experiência de Nikuradse. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174 7.6 Condutos industriais . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176 7.7 Problemas típicos envolvendo apenas perda de carga distribuída . . . . . . . . . . . 176 7.8 Perdas de carga singulares . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184 7.9 Instalações de recalque . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187 7.10 Linhas de energia e piezométrica . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191 Exercícios. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 196 Capítulo 8 8.1 8.2 8.3 Noções de instrumentação para medida das propriedades dos fluidos e dos escoamentos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206 Introdução . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206 Massa específica e peso específico relativo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206 Viscosidade . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207

<!-- p. pré-12 -->
X z Mecânica dos Fluidos 8.3.1 Viscosímetro de cilindros coaxiais . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207 8.3.2 Viscosímetro de esfera . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207 8.3.3 Viscosímetro Saybolt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208 8.4 Medida da velocidade com tubo de Pitot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208 8.5 Medida da vazão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 211 8.5.1 Orifício de bordo delgado ou diafragma . . . . . . . . . . . . . . . . . . . . . . . . . . . 211 8.5.2 Venturímetro ou tubo Venturi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216 8.5.3 Bocal convergente. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 217 8.5.4 Rotâmetro . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 217 8.5.5 Medidores volumétricos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218 8.5.6 Medida em canais abertos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218 Exercícios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218 Capítulo 9 9.1 9.2 9.3 9.4 9.5 9.6 Fluidodinâmica . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223 Introdução. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223 Conceitos fundamentais . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224 Força de arrasto de superfície . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 228 Força de arrasto de forma ou de pressão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232 Força de arrasto total. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 234 Força de sustentação . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 237 Exercícios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239 Capítulo 10 10.1 10.2 10.3 10.4 10.5 10.6 10.7 Generalização das equações integrais para regime variado . . . . . . . . . . . . . . . . 242 Introdução. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242 Vazão generalizada . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245 Equação da continuidade na forma integral para volume de controle . . . . . . . . 247 Relacionamento geral entre as propriedades do sistema e as equações integrais para volume de controle. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 252 Equação da energia geral para volume de controle . . . . . . . . . . . . . . . . . . . . . . . 254 Equação da quantidade de movimento para volume de controle . . . . . . . . . . . 258 10.6.1 Equação para volume de controle fixo ou móvel com velocidade constante . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 258 10.6.2 Equação para volume de controle acelerado . . . . . . . . . . . . . . . . . . . . . . 263 Equação do momento da quantidade de movimento para volume de controle . . 265 Exercícios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270 Capítulo 11 11.1 11.2 11.3 11.4 11.5 11.6 11.7 11.8 Análise diferencial . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275 Introdução. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275 Cinemática da partícula . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276 11.2.1 Sistemas de coordenadas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276 Geometria do movimento. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278 Variação das grandezas de um ponto a outro do fluido . . . . . . . . . . . . . . . . . . . 280 Análise dos movimentos de uma partícula fluida . . . . . . . . . . . . . . . . . . . . . . . . 284 Dilatação volumétrica . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 286 Equação da continuidade na forma diferencial. . . . . . . . . . . . . . . . . . . . . . . . . . . 287 Equação fundamental do movimento de uma partícula de fluido ideal (equação de Euler) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 289

<!-- p. pré-13 -->
11.8.1 Fluido incompreensível em repouso, campo da gravidade. . . . . . . . . . 290 11.8.2 Equilíbrio relativo para fluido incompressível . . . . . . . . . . . . . . . . . . . . 291 11.8.3 Escoamento em que a massa específica do fluido não depende da temperatura (ρ = f (p)). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 294 11.9 Escoamento bidimensional de fluido ideal, incompressível . . . . . . . . . . . . . . . . 298 11.9.1 Análise de alguns tipos de escoamentos planos, irrotacionais, em regime permanente de fluido incompressível . . . . . . . . . . . . . . . . . . . . . 305 11.10 Equação de Navier-Stokes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 312 11.11 Algumas aplicações da Equação de Navier-Stokes . . . . . . . . . . . . . . . . . . . . . . . 313 Exercícios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 320 Capítulo 12 12.1 12.2 12.3 12.4 12.5 12.6 12.7 12.8 12.9 12.10 Escoamento compressível. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 327 Introdução — Hipóteses — Conceitos fundamentais . . . . . . . . . . . . . . . . . . . . . 327 Definições . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 328 12.2.1 Energia interna (I) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 328 12.2.2 Entalpia (H). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 328 12.2.3 Entropia (S) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 329 Gás perfeito. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 329 Problema geral e equações básicas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 331 12.4.1 Equação da continuidade . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 331 12.4.2 Equação da energia . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 332 12.4.3 Equação da quantidade de movimento . . . . . . . . . . . . . . . . . . . . . . . . . . 334 12.4.4 Equação de estado . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 334 12.4.5 Variação de entropia . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 334 Velocidade do som . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 334 Número de Mach (M) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 337 Estado de estagnação – Relações entre as propriedades do fluido e as propriedades do estado de estagnação. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 338 Algumas aplicações da teoria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 341 12.8.1 Medida da velocidade de um gás com tubo de Pitot em escoamento subsônico . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 341 12.8.2 Venturi em escoamento subsônico – Coeficiente de compressibilidade . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 342 12.8.3 Descarga de um gás para a atmosfera por um orifício de um reservatório de grandes dimensões. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 345 12.8.4 Propagação de uma onda de pressão num meio compressível homogêneo a partir de um ponto emissor . . . . . . . . . . . . . . . . . . . . . . . . 347 Escoamento unidimensional em regime permanente, isoentrópico de um gás perfeito, em conduto de seção variável . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 351 12.9.1 Introdução . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 351 12.9.2 Variação das propriedades do fluido ao longo do escoamento em função da variação da área da seção do conduto e do número de Mach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 351 12.9.3 Estado crítico. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 355 12.9.4 Estado de estagnação no escoamento isoentrópico. . . . . . . . . . . . . . . . . 356 Escoamento isoentrópico em conduto convergente a partir de um reservatório de grandes dimensões . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 357

<!-- p. pré-14 -->
XII z Mecânica dos Fluidos 12.11 12.12 12.13 Escoamento isoentrópico em conduto convergente/divergente a partir de um reservatório de grandes dimensões . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 361 Onda de choque normal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 363 12.12.1 Equacionamento matemático da onda de choque . . . . . . . . . . . . . . . . . 364 12.12.2 Interpretação gráfica da onda de choque . . . . . . . . . . . . . . . . . . . . . . . . . 369 12.12.3 Complementação do estudo do escoamento ao longo de um bocal convergente/divergente . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 373 Escoamento adiabático com atrito ao longo de condutos de seção constante (escoamento de Fanno) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 376 Exercícios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 382 Exercícios selecionados . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 393 Apêndice Tabelas para a solução de escoamentos de fluidos compressíveis. . . . . . . . . . . 411 Tabela 1 — Relações para o escoamento unidimensional, isoentrópico, de um gás perfeito com k = 1,4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 411 Tabela 2 — Relações para onda de choque normal. Gás perfeito com k = 1,4. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 415 Tabela 3 — Relações para o escoamento unidimensional, adiabático com atrito, em conduto com seção constante. Linha de Fanno. Gás perfeito com k = 1,4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 418 Bibliografia . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 423 Índice remissivo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 425

<!-- p. pré-15 -->
Transcorreram-se três anos desde a primeira edição deste livro. Durante esse tempo, pelo uso durante as aulas e pela contribuição dos colegas professores e dos próprios alunos, localizamos algumas falhas. Nesta nova edição foi realizada uma revisão, mas, mesmo assim, não temos a esperança de ter atingido a perfeição, continuando a aceitar sugestões e correções. Visando enriquecer ainda mais o conteúdo apresentado, foi acrescentada nesta nova edição, no final do livro, uma seção de exercícios selecionados, que ajudarão o leitor a verificar se compreendeu a teoria globalmente. Esses exercícios pertencem ao acervo das questões de provas realizadas por nossos alunos que, em geral, foram bem-sucedidos, demonstrando o real aprendizado da disciplina. O livro continua mantendo o método inovador de apresentar o conteúdo em uma seqüência que difere da maioria dos livros de Mecânica dos Fluidos. Em vez de estabelecer, desde o início, modelos abrangentes, nos capítulos iniciais estabelecem-se situações regidas por hipóteses simplificadoras para que o leitor compreenda e acostume-se mais facilmente com as principais variáveis e efeitos, para depois eliminar gradualmente as simplificações e chegar a equações mais abrangentes. Os capítulos 3 a 9 são dedicados ao regime permanente, eliminando as variações em função do tempo. Entretanto, após o tirocínio desses capítulos, no Capítulo 10 são estabelecidas as equações para o regime variado. O leitor poderá verificar que, nessa situação, chega-se a equações diferenciais de solução demorada e complexa e, muitas vezes, esta somente poderá ser obtida por métodos numéricos. O Capítulo 6 trata de análise dimensional como suporte fundamental à análise empírica. Até o Capítulo 10 estuda-se o movimento do sistema fluido, isto é, porções da substância em que as partículas têm, em média, um comportamento semelhante. Esse método pode ser denominado “análise integral”. No Capítulo 11 analisa-se o movimento individual das partículas, o que constitui a “análise diferencial”. No Capítulo 12, por sua vez, estuda-se brevemente o escoamento compressível, em que a variação da massa específica ao longo do escoamento desempenha papel muito importante na interpretação dos fenômenos e na solução dos problemas. Todos os capítulos contêm algum exercício típico resolvido para orientar o leitor ao encadeamento lógico no uso da teoria para a solução de problemas.

<!-- p. pré-16 -->
XIV z Mecânica dos Fluidos No final de cada capítulo há uma série de exercícios com respostas. O leitor deverá resolvê-los, trabalhando com as situações propostas até obter as respostas, o que exigirá a leitura da teoria tantas vezes quantas forem necessárias para atingir a compreensão de todos os conceitos. É importante lembrar o leitor de que a partir da teoria pode ser criada uma infinidade de exercícios, e que a solução de alguns modelos, sem compreender todos os conceitos teóricos, não significará o sucesso na solução de outros modelos diferentes. O Companion Website que acompanha o livro ((wwww.preeanrshoanll..ccoomm/.bbrru/nberuttni_ebtrt)i) oferece aos professores apresentações em PowerPoint e resoluções dos exercícios. Para ter acesso ao conteúdo, os professores que adotam o livro devem entrar em contato com um representante da Pearson ou enviar um e-mail para universitarios@pearson.com. Como a edição anterior já comprovou sua utilidade, acreditamos que essa edição revisada, com mais exercícios e uma nova apresentação visual, será ainda mais valiosa para estudantes e profissionais. Prof. Eng. Franco Brunetti

<!-- p. 1 -->

# Capítulo 1 — Introdução, definição e propriedades dos fluidos

## 1.1 Introdução

Mecânica dos Fluidos é a ciência que estuda o comportamento físico dos fluidos, assim como as leis que regem esse comportamento. As bases lançadas pela Mecânica dos Fluidos são fundamentais para muitos ramos de aplicação da engenharia. Dessa forma, o escoamento de fluidos em canais e condutos, a lubrificação, os esforços em barragens, os corpos flutuantes, as máquinas hidráulicas, a ventilação, a aerodinâmica e muitos outros assuntos lançam mão das leis da Mecânica dos Fluidos para obter resultados de aplicação prática. Como se pode observar, pelo exposto, poucos são os ramos da engenharia que escapam totalmente do conhecimento dessa ciência que se torna, assim, uma das de maior importância entre as que devem fazer parte dos conhecimentos básicos do engenheiro.

## 1.2 Conceitos fundamentais e definição de fluido

A definição de fluido é introduzida, normalmente, pela comparação dessa substância com um sólido. A definição mais elementar diz: Fluido é uma substância que não tem uma forma própria, assume o formato do recipiente. A Figura 1.1 ilustra o significado desse enunciado. Figura 1.1 Os fluidos são, portanto, os líquidos e os gases, sendo que estes ainda se distinguem dos primeiros por ocuparem todo o recipiente, enquanto os líquidos apresentam uma superfície livre.

<!-- p. 2 -->
Se o problema fundamental fosse apenas reconhecer os fluidos, a definição apresentada seria perfeitamente suficiente para essa finalidade. Entretanto, é possível introduzir uma outra que, apesar de ser mais complexa, permite construir uma estrutura lógica que será de grande utilidade para o desenvolvimento da Mecânica dos Fluidos. Essa definição está novamente ligada à comparação de comportamento entre um sólido e um fluido, por uma observação prática denominada “Experiência das Duas Placas”, descrita a seguir. Seja um sólido preso entre duas placas planas, uma inferior fixa e outra superior solicitada por uma força tangencial Ft (na direção do plano da placa) (Figura 1.2a). Figura 1.2 Mantida a força Ft constante, nota-se que o sólido se deforma angularmente (Figura 1.2b) até alcançar uma nova posição de equilíbrio estático. Nessa posição, as tensões internas equilibram a força externa aplicada e somente uma variação da força Ft faria com que houvesse uma modificação da nova configuração do sólido. Pode-se dizer, então, que um sólido, solicitado por uma força tangencial constante, deforma-se angularmente, mas atinge uma nova configuração de equilíbrio estático (Figura 1.2b). A mesma experiência será agora realizada colocando-se um fluido entre as placas. Suponha que seja possível, por exemplo, por meio de um corante, visualizar um certo volume ABCD do fluido (Figura 1.3a). Sendo a placa inferior fixa e a superior móvel, ao se aplicar a força tangencial Ft na placa superior, esta irá se deslocar. A primeira observação importante nessa experiência é que pontos correspondentes do fluido e da placa continuam em rcorrespondência durante o movimento; assim, se a placa superior adrquire uma velocidade v, os pontos do fluido em contato com ela terão a mesma velocidade v, e os pontos do fluido em contato com a placa fixa ficarão parados junto dela. Tal observação conduz ao chamado princípio da aderência: Os pontos de um fluido, em contato com uma superfície sólida, aderem aos pontos dela, com os quais estão em contato. Então, o que se observa é que o volume ABCD de fluido, sob a ação da força Ft, deforma-se continuamente, não alcançando uma nova posição de equilíbrio estático, supondo-se as placas de comprimento infinito. Essa experiência permite a distinção entre sólidos e fluidos, pois, enquanto aqueles se deformam limitadamente sob a ação de esforços tangenciais pequenos, estes se deformam continuamente sem alcançar uma nova posição de equilíbrio estático. Pode-se então dizer que: Fluido é uma substância que se deforma continuamente, quando submetida a uma força tangencial constante qualquer ou, em outras palavras, fluido é uma substância que, submetida a uma força tangencial constante, não atinge uma nova configuração de equilíbrio estático. Figura 1.3

<!-- p. 3 -->
## 1.3 Tensão de cisalhamento — Lei de Newton da viscosidade

Da experiência realizada para definir fluido podem-se obter outras importantes conclusões que serão descrirtas neste item. Antes de tudo, será definida a tensão de cisalhamento. Seja uma força F aplicada sobre uma superfície de área A (Figura 1.4). Essa força pode ser decomposta segundo a direção da normal à superfície e a da tangente, dando origem a uma componente normal e outra tangencial. Figura 1.4 Define-se tensão de cisalhamento média como sendo o quociente entre o módulo da componente tangencial da força e a área sobre a qual está aplicada. τ = Ft A (1.1)

Em outras palavras: tensão de cisalhamento τ é a força tangencial por unidade de área. As unidades mais utilizadas para essa grandeza serão o kgf/m2 do sistema MK*S (Técnico), o dina/cm2 (CGS) e o N/m2 (SI). A seguir será descrito outro fato notável que pode ser observado na experiência das duas placas.

A placa superior é inicialmente acelerada pela força Ft, fato facilmente observável, já que passa da velocidade nula para uma velocidade finita. Nota-se, porém, que a partir de um certo instante a placa superior adquire uma velocidade v0 constante. Isso demonstra que a força externa Ft aplicada na placa é equilibrada por forças internas ao fluido, visto que, não existindo aceleração, pela segunda lei de Newton da dinâmica, a resultante das forças deverá ser nula (equilíbrio dinâmico).

Como aparecem essas forças internas? Para responder a essa pergunta, deve-se relembrar o princípio da aderência. Segundo ele, o fluido junto à placa superior irá se deslocar com velocidade v0, enquanto aquele junto à placa inferior estará com velocidade nula. As camadas intermediárias deverão se adaptar às extremas, adquirindo velocidades que variam desde v0 até zero (Figura 1.5). Em cada seção normal às placas, como a seção AB genérica, irá se formar um diagrama de velocidades, onde cada camada do fluido desliza sobre a adjacente com uma certa velocidade relativa. Como o leitor já deve ter percebido, esse fato cria uma espécie de atrito entre as diversas camadas do fluido.

Tal deslizamento entre camadas origina tensões de cisalhamento, que, multiplicadas pela área da placa, originam uma força tangencial interna ao fluido, responsável pelo equilíbrio da força Ft externa, o que fará com que a placa superior assuma uma velocidade constante v0. A Figura 1.5b mostra o aparecimento de τ devido à velocidade relativa v1 – v2, que cria um escorregamento entre as duas camadas indicadas.

Newton descobriu que em muitos fluidos a tensão de cisalhamento é proporcional (α) ao gradiente da velocidade, isto é, à variação da velocidade com y.

<!-- p. 4 -->
Figura 1.5 Disso pode-se traduzir a lei de Newton da viscosidade:

τ α dv dy ou τ dv = cte (1.2) dy Os fluidos que obedecem a essa lei são ditos fluidos newtonianos. Os fluidos que se comportam de forma a obedecer à Equação 1.2 são a grande maioria, como água, ar, óleos etc., e os restantes, chamados não-newtonianos, não serão abordados neste estudo, pois são de pequeno interesse geral, sendo objeto apenas de estudos muito especializados.

## 1.4 Viscosidade absoluta ou dinâmica

A lei de Newton da viscosidade impõe uma proporcionalidade entre a tensão de cisalhamento e o gradiente da velocidade. Tal fato leva à introdução de um coeficiente de proporcionalidade na Equação 1.2. Tal coeficiente será indicado por μ e denomina-se viscosidade dinâmica ou absoluta. A Equação 1.2 ficará então:

τ = μ dv (1.3) dy Essa grandeza μ é uma propriedade de cada fluido e de suas condições, como, por exemplo, a pressão e, principalmente, a temperatura. A origem da viscosidade nos fluidos mereceria uma análise microscópica que não será feita neste estudo. De forma simplificada, pode-se dizer que a viscosidade dos fluidos é originada por uma coesão entre as moléculas e pelos choques entre elas. Uma forma de visualizar a existência da viscosidade é retornar à Experiência das Duas Placas. Verificou-se que, após um certo tempo de aplicação da força Ft (cte) na placa superior, esta assume uma velocidade v0 constante, pelo equilíbrio dinâmico da força externa por forças desenvolvidas internamente. A viscosidade, portanto, não é uma propriedade observável num fluido em repouso, pois, qualquer que seja a força tangencial, ele se deforma. Com o movimento do fluido, porém, ela faz sentir seu efeito, criando as condições para equilibrar a força Ft externa.

<!-- p. 5 -->
Pode-se dizer, então, que viscosidade dinâmica é a propriedade dos fluidos que permite equilibrar, dinamicamente, forças tangenciais externas quando os fluidos estão em movimento. Matematicamente, μ é a constante de proporcionalidade da lei de Newton da viscosidade. De uma forma mais prática: Viscosidade é a propriedade que indica a maior ou a menor dificuldade de o fluido escoar (escorrer). As unidades da viscosidade podem ser obtidas por análise dimensional a partir da lei de Newton da viscosidade. Adotando como grandezas fundamentais FLT: [τ] = Força F Área = L2 = FL–2 L ⎡ dv ⎤ ⎢⎣ dy ⎦⎥ = T L = T –1 mas τ = μ dv dy e μ= τ dv dy logo: [μ] = FL –2 T –1 = FL–2 T MK*S (Técnico)

⎯→ un μ = kgf ⋅ m2 s MKS Giorgi ou SI ⎯→ un μ = N⋅s m2 CGS ⎯→ un μ = dina ⋅ cm 2 s = poise Utiliza-se ainda o centipoise: 1 cpoise = 0,01 poise. Note-se que a viscosidade dinâmica possui um valor diferente para cada fluido e varia, para um mesmo fluido, principalmente em relação à temperatura. Os gases e os líquidos comportam-se de maneiras diferentes quanto a esse aspecto. Nos líquidos, a viscosidade diminui com o aumento da temperatura, enquanto nos gases a viscosidade aumenta com o aumento da temperatura. A razão desse comportamento exige uma análise microscópica que não será abordada.

## 1.5 Simplificação prática

Viu-se que a lei de Newton da viscosidade é escrita da seguinte forma: τ = μ dv dy onde dv é o gradiente da velocidade ou variação de v com y (Figura 1.6). dy Figura 1.6

<!-- p. 6 -->
Pela figura, observa-se que, a um deslocamento dy, na direção do eixo y, corresponde uma variação dv da velocidade. Quando a distância ε é pequena, pode-se considerar, sem muito erro, que a variação de v com y seja linear (Figura 1.7). Figura 1.7 A simplificação que resulta desse fato é a seguinte: o ΔABC ≈ ΔMNP. Logo: dv = v0 dy ε ou, de uma forma mais geral:

dv Δv dy = Δy ficando a lei de Newton:

τ = μ Δv = μ v0 Δy ε (1.4)

Esse fato leva a simplificações importantes nos problemas, evitando hipóteses e integrações às vezes complicadas. Um pistão de peso G = 4 N cai dentro de um cilindro com uma velocidade constante de 2 m/s. O diâmetro do cilindro é 10,1 cm e o do pistão é 10,0 cm. Determinar a viscosidade do lubrificante colocado na folga entre o pistão e o cilindro. Solução Se vr = cte ⇒ ar = 0, logo, o pistão está em equilíbrio dinâmico, isto é:

∑ r F = r ma = 0 Na direção do movimento, a força causada pelas tensões de cisalhamento Fμdeve equilibrar o peso G, na velocidade dada.

Logo, ou Fμ = G τA=G ou μ dv dy πD i L = G Sendo a distância ε = De – Di = 10,1 – 10 = 0,05 cm muito pequena, adota-se um diagrama linear de velocidades. 2 2

<!-- p. 7 -->
Nesse caso, logo, μ v ε π DiL = G μ = εG vπ DiL μ = 0,05 × 10–2 × 4 = 6,37 × 10–2 N. s m 2 2 π × 0,1× 0,05 A seguir, o problema será resolvido também para o caso em que o diagrama não é linear. Adotando-se uma coordenada polar R i ≤ r ≤ Re, para uma camada de espessura dr, a velocidade varia de v + dv para v, criando o escorregamento que gera as tensões de cisalhamento. Logo, τ = –μ dv, pois para um dr positivo o v varia de um dv negativo. dr Como cada camada se desloca com v = cte, isso significa que o peso, transmitido no contato com a primeira camada, equilibra-se com as tensões de cisalhamento um dr adiante. Assim, para uma camada genérica: τA = G ou −μ dv 2 πrL = G dr ou, separando as variáveis: 2 πLμdv = – Gdr r Integrando de Ri a Re, quando v varia de v a 0:

∫ ∫ 0 2 πLμdv = – R e G dr v Ri r –2 πLμv = –G ln Re Ri μ = G ln Re 2 πLv R i ou μ = G ln De 2 πLv Di μ= 4 ln 10,1 = 6,33 × 10–2 N. s/m2 2π × 0,05 × 2 10 Note-se que esse seria o resultado correto. Então, o erro ao considerar o diagrama linear seria: Erro = μ linear – μ real × 1 00 μ real Erro = 6,37 × 1 0–2 – 6,33 × 10 –2 × 100 = 0,63% 6,33 × 10 –2 que é um erro desprezível, comprovando que, quando a espessura do fluido é pequena, pode-se utilizar um diagrama linear.

<!-- p. 8 -->
## 1.6 Massa específica (ρ)

No estudo realizado será considerado, salvo menção contrária, que os fluidos são um meio contínuo e homogêneo, de forma que as propriedades médias definidas coincidam com as propriedades nos pontos. Tal hipótese facilita o estudo e permite introduzir definições simples para todas as propriedades dos fluidos. Massa específica é a massa de fluido por unidade de volume.

ρ=m V onde m = massa V = volume (1.5) Unidades Por análise dimensional, utilizando FLT:

lei de Newton F m= a F [m] = LT –2 = FL–1 T 2 [V] = L3 [ρ] = FL–1 T L3 2 = FL–4 T 2 Sistema MK*S ⎯→ un ρ = kgf ⋅ s 2 m4 utm = m3 Sistema MKS Giorgi ou SI ⎯→ un ρ = N⋅s2 m4 kg = m3 Sistema CGS ⎯→ un ρ = dina ⋅ s 2 cm 4 g = cm 3

## 1.7 Peso específico (γ)

Peso específico é o peso de fluido por unidade de volume.

γ = G onde G = peso (1.6) V V = volume Unidades Por análise dimensional, tem-se:

[G] = F [V] = L3 [γ ] = F L3 = FL–3 Sistema MK*S ⎯→ un γ = kgf m3 Sistema MKS Giorgi ou SI ⎯→ un γ = N m3 Sistema CGS ⎯→ un γ = dina cm 3

<!-- p. 9 -->
Pode-se deduzir uma relação simples entre peso específico e massa específica:

γ = G mas G = mg V ou γ = mg e γ = ρg (1.7) V

## 1.8 Peso específico relativo para líquidos (γr)

É a relação entre o peso específico do líquido e o peso específico da água em condições padrão. Será adotado que γ H 2O = 1.000 kgf m 3 ≅ 10.000 N/m 3 Como a massa específica e o peso específico diferem por uma constante, conclui-se que a massa específica relativa e o peso específico relativo coincidem. O peso específico relativo de uma substância é 0,8. Qual será seu peso específico? Solução γr = γ γ H2O → γ = γ rγ H2O = 0,8 × 1.000 = 800 kgf/ m 3 ≅ 8.000 N/m3

## 1.9 Viscosidade cinemática (ν)

Por comodidade e por outras razões que aqui não serão expostas, convém dar um nome ao quociente μ /ρ que, muitas vezes, aparecerá no decorrer do estudo. Viscosidade cinemática é o quociente entre a viscosidade dinâmica e a massa específica. ν = μ ρ (1.8) Unidades Por análise dimensional, utilizando FLT, teremos: [μ ] = FL–2 T [ρ] = FL–4 T 2 Logo, [ν] = FL–2 T FL–4 T 2 = L2 T –1 Sistema MK*S ⎯→ un ν = m 2 s Sistema MKS Giorgi ou SI ⎯→ un ν = m 2 s Sistema CGS ⎯→ un ν = cm 2 = stoke (St)

s Utiliza-se ainda o centistoke: 1 cSt = 0,01 St.

<!-- p. 10 -->
Das unidades, verifica-se que o nome — viscosidade cinemática — deve-se ao fato de essa grandeza não envolver força, mas somente comprimento e tempo, que são as grandezas fundamentais da Cinemática.

## 1.10 Fluido ideal

Fluido ideal é aquele cuja viscosidade é nula. Por essa definição conclui-se que é um fluido que escoa sem perdas de energia por atrito. É claro que nenhum fluido possui essa propriedade; no entanto, será visto no decorrer do estudo que algumas vezes será interessante admitir essa hipótese, ou por razões didáticas ou pelo fato de a viscosidade ser um efeito secundário do fenômeno.

## 1.11 Fluido ou escoamento incompressível

Diz-se que um fluido é incompressível se o seu volume não varia ao modificar a pressão. Isso implica o fato de que, se o fluido for incompressível, a sua massa específica não variará com a pressão. É claro que na prática não existem fluidos nessas condições. Os líquidos, porém, têm um comportamento muito próximo a esse e na prática, normalmente, são considerados como tais. Mesmo os gases em certas condições, em que não são submetidos a variações de pressão muito grandes, podem ser considerados incompressíveis. Um dos exemplos práticos é o estudo de ventilação, em que, em geral, essa hipótese é aceitável. É importante compreender que nenhum fluido deve ser julgado de antemão. Sempre que ao longo do escoamento a variação da massa específica ρ for desprezível, o estudo do fluido será efetuado pelas leis estabelecidas para fluidos incompressíveis.

## 1.12 Equação de estado dos gases

Quando o fluido não puder ser considerado incompressível e, ao mesmo tempo, houver efeitos térmicos, haverá necessidade de determinar as variações da massa específica ρ em função da pressão e da temperatura. De uma maneira geral, essas variações obedecem, para os gases, a leis do tipo ƒ(ρ, p, T) = 0 denominadas equações de estado. Para as finalidades desse desenvolvimento, sempre que for necessário, o gás envolvido será suposto como ‘gás perfeito’, obedecendo à equação de estado:

p = RT ρ ou ρ= p RT (1.9) onde:

p = pressão absoluta R = constante cujo valor depende do gás T = temperatura absoluta (lembrar que a escala absoluta é a escala Kelvin e K = °C + 273) Para o ar, por exemplo, R ≅ 287 m2/s2 K. Numa mudança do estado de um gás:

p1 ρ 2 = T1 p2 ρ1 T2 (1.10)

<!-- p. 11 -->
O processo é dito isotérmico quando na transformação não há variação de temperatura. Nesse caso: p1 = p 2 = cte ρ1 ρ2 (1.11)

O processo é dito isobárico quando na transformação não há variação de pressão. Nesse caso: ρ1 T1 = ρ2 T2 = cte (1.12)

O processo é dito isocórico ou isométrico quando na transformação não há variação de volume. Nesse caso: p1 = p 2 = cte T1 T2 (1.13)

O processo é dito adiabático quando na transformação não há troca de calor. Nesse caso: p1 ρ1k = p ρ 2 k 2 = cte (1.14)

onde k é a chamada constante adiabática cujo valor depende do gás. No caso do ar, k = 1,4. Numa tubulação escoa hidrogênio (k = 1,4, R = 4.122 m2/s2K). Numa seção (1), p1 = 3 × 105 N/m2(abs) e T1 = 30°C. Ao longo da tubulação, a temperatura mantém-se constante. Qual é a massa específica do gás numa seção (2), em que p2 = 1,5 × 105 N/m2 (abs)? Solução p1 ρ1 = RT1 Logo: ρ1 = p1 RT1 Logo:

T1 = 30 + 273 = 303K ρ1 = 3× 4122 105 × 303 = 0,24kg m3 Como: Portanto:

T1 = T2 → p1 ρ1 = p2 ρ2 ou ρ2 = ρ1 p2 p1 ρ2 = 0,24 × 1,5 × 105 3 × 105 = 0,12kg m3 1.1 A viscosidade cinemática de um óleo é 0,028 m2/s e o seu peso específico relativo é 0,85. Determinar a viscosidade dinâmica em unidades dos sistemas MK*S, CGS e SI (g = 10 m/s2). Resp.: μ MK* S =2,38kgf. s m2; μCGS = 233 dina.s/cm2; μSI = 23,3 N.s/m2.

1.2 A viscosidade dinâmica de um óleo é 5 × 10–4 kgf.s/m2 e o peso específico relativo é 0,82. Determinar a viscosidade cinemática nos sistemas MK*S, SI e CGS (g = 10 m/s2; γ H2 0 = 1.000 kgf / m 3 ). Resp.: ν = 6 × 10–6 m2/s = 6 × 10–2 St 1.3 O peso de 3 dm3 de uma substância é 23,5 N. A viscosidade cinemática é 10–5 m2/s. Se g = 10 m/s2, qual será a viscosidade dinâmica nos sistemas CGS, MK*S, SI e em N.min/km2? Resp.: 7,83 × 10–2 poise = 8 × 10–4 kgf.s/m2 = 7,83 × 10–3 N.s/m2 = 130,5 N.min/km2

<!-- p. 12 -->
12 z Mecânica dos Fluidos 1.4 São dadas duas placas planas paralelas à distância de 2 mm. A placa superior move-se com velocidade de 4 m/s, enquanto a inferior é fixa. Se o espaço entre as duas placas for preenchido com óleo (ν = 0,1St; ρ = 830 kg/m3), qual será a tensão de cisalhamento que agirá no óleo? Resp.: τ = 16,6 N/m2 1.5 Uma placa quadrada de 1,0 m de lado e 20 N de peso desliza sobre um plano inclinado de 30°, sobre uma película de óleo. A velocidade da placa é 2 m/s constante. Qual é a viscosidade dinâmica do óleo, se a espessura da película é 2 mm? Resp.: μ = 10–2 N.s/m2 1.6 O pistão da figura tem uma massa de 0,5 kg. O cilindro de comprimento ilimitado é puxado para cima com velocidade constante. O diâmetro do cilindro é 10 cm e do pistão é 9 cm e entre os dois existe um óleo de ν = 10–4 m2/s e γ = 8.000 N/m3. Com que velocidade deve subir o cilindro para que o pistão permaneça em repouso? (Supor diagrama linear e g = 10 m/s2.) Resp.: v = 22,1 m/s 1.7 Num tear, o fio é esticado passando por uma fieira e é enrolado num tambor com velocidade constante, como mostra a figura. Na fieira, o fio é lubrificado e tingido por uma substância. A máxima força que pode ser aplicada no fio é 1 N, pois, ultrapassando-a, ele rompe. Sendo o diâmetro do fio 0,5 mm e o diâmetro da fieira 0,6 mm, e sendo a rotação do tambor 30 rpm, qual é a máxima viscosidade do lubrificante e qual é o momento necessário no eixo do tambor? (Lembrar que ω = 2 π n.)

<!-- p. 13 -->
Resp.: M = 0,1 N.m; μ = 0,1 N.s/m2 1.8 O dispositivo da figura é constituído de dois pistões de mesmas dimensões geométricas que se deslocam em dois cilindros de mesmas dimensões. Entre os pistões e os cilindros existe um lubrificante de viscosidade dinâmica 10–2 N.s/m2. O peso específico do pistão (1) é 20.000 N/m3. Qual é o peso específico do pistão (2) para que o conjunto se desloque na direção indicada com uma velocidade de 2 m/s constante? Desprezar o atrito na corda e nas roldanas. Resp.: γ2 = 16.800 N/m3 1.9 O eixo da figura, ao girar, provoca a rotação do tambor. Este enrola a corda, que levanta um peso de 10 N com uma velocidade constante de 0,5 m/s. O fluido existente entre o eixo e o tambor tem μ = 0,1 N.s/m2 e apresenta um diagrama linear de velocidades. Pede-se: a) a rotação do eixo em rpm; b) o momento provocado pelo fluido contra a rotação do eixo. Dados: R1 = 10 cm; R2 = 10,1 cm; R3 = 20 cm; ω = 2 π n. Resp.: a) n = 123,5 rpm; b) Meixo = 1,96 N.m

<!-- p. 14 -->
1.10 No viscosímetro da figura, o cilindro externo gira com uma rotação de 100 rpm constante. O cilindro interno é oco, sua parede tem espessura desprezível e está preso a um fio calibrado à torção. Esse cilindro gira torcendo o fio até que nele se atinja um momento de 10 N.m. Supondo o diagrama de velocidades linear e um líquido de viscosidade cinemática v = 10−4 m2 s e ρ = 800 kg/m3, qual é a altura do líquido? Resp.: h = 3,5 cm 1.11 O turbocompressor de um motor de combustão interna tem uma rotação de 120.000 rpm (ω = 2 π n). Os mancais do eixo são flutuantes e giram com uma certa rotação. São dados: μ = 8 × 10–3 N.s/m2; D1 = 12 mm; D2 = 12,05 mm; D3 = 15,05 mm; D4 = 15,1 mm; L = 20 mm. Na condição de equilíbrio dinâmico, na rotação dada, pede-se: a) a rotação do mancal flutuante; b) o momento resistente à rotação que age no eixo do turbocompressor relativo aos mancais. Resp.: a) 40.533 rpm; b) 0,14 N.m 1.12 No sistema da figura, o corpo cilíndrico de peso G desce com velocidade constante v = 2 m/s, fazendo o eixo girar. Dados μ = 10–3 N.s/m2; L = 2/π m; De = 50,2 cm; Di = 50 cm; d = 10 cm; G = 50 N, qual é o momento aplicado por um agente externo no eixo? É motor ou resistente?

<!-- p. 15 -->
Resp.: M = 0,1 N.m (motor)

1.13 Dois discos são dispostos coaxialmente face a face, separados por um filme de óleo lubrificante de espessura ε pequena. Aplicando-se um momento no disco (1), ele inicia um movimento em torno de seu eixo e, através do fluido viscoso, estabelece-se o regime, de forma que as velocidades angulares ω1 e ω2 ficam constantes. Admitindo o regime estabelecido, determinar a função ω1 – ω2 = f(Mt, ε, D, μ). Resp.: ω1 – ω2 = 32 εMt πD4μ 1.14 Assumindo o diagrama de velocidades indicado na figura, em que a parábola tem seu vértice a 10 cm do fundo, calcular o gradiente de velocidade e a tensão de cisalhamento para y = 0; 5; 10 cm. Adotar μ = 400 centipoises. Resp.: (50 s–1; 200 dina/cm2); (25 s–1; 100 dina/cm2); (0; 0)

1.15 A placa da figura tem uma área de 4 m2 e espessura desprezível. Entre a placa e o solo existe um fluido qcauedoesfclouaid, foorém10a–n2dNo.us/mmd2iaegaravmelaodciedvaedleocmidáaxdimesaddaodoespcooramv =en2t0oyév4mmáx /(1s.–P5eyd).eA-sev:iscosidade dinâmia) o gradiente de velocidades junto ao solo; b) a força necessária para manter a placa em equilíbrio.

<!-- p. 16 -->
Resp.: a) –80 s–1; b) 3,2 N 1.16 Um fluido escoa sobre uma placa com o diagrama dado. Pede-se: a) v = f (y); b) a tensão de cisalhamento junto à placa.

Resp.: a) v = – 0,75y2 + 3y + 2; b) t = 0,03 N/m2 1.17 Na figura, uma placa de espessura desprezível e área A1 = 2 m2 desloca-se com v = 5 m/s constante, na interface de dois fluidos, tracionada por uma força F = 400 N. Na parte superior, ε = 1 mm e o diagrama de velocidades é considerado linear. Na parte inferior, o diagrama é dado por v = ay2 + by + c. Pede-se: a) a tensão de cisalhamento na parte superior da placa em movimento; b) a tensão de cisalhamento na face inferior da mesma placa; c) a expressão do diagrama de velocidades v = f (Y) no fluido superior; d) a expressão do diagrama de velocidades no fluido inferior (v = f (y)); e) a força R que mantém a placa da base em repouso.

Resp.: a) 150 N/m2; b) 50 N/m2; c) v = 5.000Y; d) v = 5y2 + 7,5y; e) 60 N 1.18 çAãroe(s2c)o, apa2o=l1o5n0g.0o0d0eNu/mma2t(uabbusl)aeçTão2 .=E2m0°uCm. Daesteeçrãmoi(n1a),rpa1v=ar2i0a0ç.ã0o00poNr/cemn2tu(aablsd)aemT1as=s5a0e°sCp.eEcmíficuamdae se(1) para (2). Resp.: 17,3%

<!-- p. 17 -->
1.19 Um gás natural tem peso específico relativo 0,6 em relação ao ar a 9,8 × 104 Pa (abs) e 15°C. Qual é o peso específico desse gás nas mesmas condições de pressão e temperatura? Qual é a constante R desse gás? (Rar = 287 m2/s2K; g = 9,8 m/s2) Resp.: γ = 7 N/m3; R = 478 m2/s2K 1.20 Calcular o peso específico do ar a 441 kPa (abs) e 38°C.

Resp.: γ = 49,4 N/m3 1.21 Um volume de 10 m3 de dióxido de carbono (k = 1,28) a 27°C e 133,3 kPa (abs) é comprimido até se obter 2 m3. Se a compressão for isotérmica, qual será a pressão final? Qual seria a pressão final se o processo fosse adiabático? Resp.: 666,5 kPa (abs); 1,046 MPa (abs)

<!-- p. 18 -->

# Capítulo 2 — Estática dos fluidos

## 2.1 Pressão

No Capítulo 1 foi visto que uma força aplicada sobre uma superfície pode ser decomposta em dois efeitos: um tangencial, que origina tensões de cisalhamento, e outro normal, que dará origem às pressões.

Se Fn representa a força normal que age numa superfície de área A, e dFn a força normal que age num infinitésimo de área dA, a pressão num ponto será: p = dFn dA (2.1)

Se a pressão for uniforme, sobre toda a área, ou se o interesse for na pressão média, então: p = Fn A (2.2)

O leitor não deve confundir pressão com força. Veja o exemplo da Figura 2.1.

Figura 2.1 Note-se que a força aplicada em ambos os recipientes é a mesma; entretanto, a pressão será diferente. De fato: Recipiente (a):

p1 = F1 A1 100 N = 10 cm 2 N = 10 cm 2

<!-- p. 19 -->
Recipiente (b):

C a p í t u l o 2 z Estática dos fluidos z 19 p2 = F2 A2 100 N = 5 cm 2 N = 20 cm 2

## 2.2 Teorema de Stevin

A diferença de pressão entre dois pontos de um fluido em repouso é igual ao produto do peso específico do fluido pela diferença de cotas dos dois pontos. Sejam um recipiente que contém um fluido e dois pontos genéricos M e N. Unindo os pontos M e N constrói-se um cilindro, cuja área da base é dA, em torno do eixo MN. Figura 2.2 Orienta-se o eixo MN de N para M, e seja α o ângulo formado com a horizontal.

Seja zN a cota do ponto N e zM a cota do ponto M, em relação a um plano horizontal qualquer, adotado como referência. Seja h a diferença de cotas dos dois pontos, isto é, h = zM – zN. Como, por hipótese, o fluido está em repouso, a resultante das forças que agem sobre o cilindro em qualquer direção deve ser nula, ou haveria um deslocamento nessa direção, contrariando a hipótese.

As forças que agem são:

dFN = pNdA no ponto N dFM = pMdA no ponto M F = ∫ pdA l na superfície lateral dG = peso do fluido contido no cilindro = volume de fluido × peso específico = l.dA.γ Todas essas forças são projetadas na direção do eixo NM. Deve-se lembrar que, como as forças devidas à pressão são normais à superfície, então as que agem na superfície lateral terão componente nula sobre o eixo. As outras forças projetadas, respeitando o sentido do eixo, resultam: pNdA – pMdA – dG sen α = 0 ou pNdA – pMdA – γldA sen α = 0 pN – pM = γl sen α mas l sen α = h = zM – zN ou pN – pM = γ h = γ (zM – zN)

(2.3)

<!-- p. 20 -->
Logo, a diferença de pressão entre dois pontos genéricos é igual ao produto do peso específico do fluido pela diferença de cotas entre os dois pontos, como se queria demonstrar. O que é importante notar ainda nesse teorema é que: a) na diferença de pressão entre dois pontos não interessa a distância entre eles, mas a diferença de cotas; b) a pressão dos pontos num mesmo plano ou nível horizontal é a mesma; c) o formato do recipiente não é importante para o cálculo da pressão em algum ponto. Na Figura 2.3, em qualquer ponto do nível A, tem-se a mesma pressão pA, e em qualquer ponto do nível B, tem-se a pressão pB, desde que o fluido seja o mesmo em todos os ramos; Figura 2.3 d) se a pressão na superfície livre de um líquido contido num recipiente for nula, a pressão num ponto à profundidade h dentro do líquido será dada por: p = γh; Figura 2.4 e) nos gases, como o peso específico é pequeno, se a diferença de cota entre dois pontos não é muito grande, pode-se desprezar a diferença de pressão entre eles. Figura 2.5

## 2.3 Pressão em torno de um ponto de um fluido em repouso

A pressão num ponto de um fluido em repouso é a mesma em qualquer direção. Existem demonstrações rebuscadas para esse enunciado; como, porém, tais demonstrações não trazem nenhum subsídio aos conhecimentos, prefere-se apelar para a intuição do leitor. Se o fluido está em repouso, todos os seus pontos também deverão estar. Se a pressão fosse diferente em alguma direção, haveria um desequilíbrio no ponto, fazendo com que este

<!-- p. 21 -->
se deslocasse nessa direção, contrariando a hipótese. Logo, se o fluido está em repouso, a pressão em torno de um ponto deve ser a mesma em qualquer direção (Figura 2.6). Figura 2.6

## 2.4 Lei de Pascal

A pressão aplicada num ponto de um fluido em repouso transmite-se integralmente a todos os pontos do fluido. A Figura 2.7 ilustra perfeitamente tal fato:

Figura 2.7 Em (a) e (b), mostra-se o mesmo recipiente cilíndrico em que foram escolhidos alguns pontos. Em (a), o fluido apresenta uma superfície livre à atmosfera e supõe-se que as pressões nos pontos indicados sejam: p1 = 1 N/cm 2; p2 = 2N/cm2; p3 = 3 N/cm 2 e p4 = 4 N/cm 2.

Ao aplicar a força de 100 N, por meio do êmbolo da Figura 2.7b, tem-se um acréscimo de F 100 N pressão de p = = A 5 = 20 cm2 . As pressões nos pontos indicados deverão, portanto, ter os seguintes valores:

p1 = 21 N/cm 2; p2 = 22 N/cm 2; p3 = 23 N/cm 2 e p 4= 24 N/cm 2.

Torna-se evidente, então, o significado da lei de Pascal. Essa lei apresenta sua maior importância em problemas de dispositivos que transmitem e ampliam uma força através da pressão aplicada num fluido.

<!-- p. 22 -->
A figura mostra, esquematicamente, uma prensa hidráulica. Os dois êmbolos têm, respectivamente, as áreas A1 = 10 cm2 e A2 = 100 cm2. Se for aplicada uma força de 200 N no êmbolo (1), qual será a força transmitida em (2)? A pressão transmitida pelo êmbolo (1) será p1 = F1 A1 .

Mas, pela lei de Pascal, essa pressão será transmitida integralmente ao êmbolo (2), portanto p2 = p1. Logo:

p2A2 = p1A2 = F2 Como: p1 = 200 10 = 20 N , então cm 2 F2 = 20 × 100 = 2.000 N Nota-se, então, que se pode, por meio desse dispositivo, não só transmitir uma força, mas também ampliá-la. É nesse princípio que, na prática, baseiam-se: prensas hidráulicas, servomecanismos, dispositivos de controle, freios etc.

## 2.5 Carga de pressão

Foi visto pelo teorema de Stevin que altura e pressão mantêm uma relação constante para um mesmo fluido. É possível expressar, então, a pressão num certo fluido em unidade de comprimento, lembrando que: p =h (2.4) γ Essa altura h, que, multiplicada pelo peso específico do fluido, reproduz a pressão num certo ponto dele, será chamada ‘carga de pressão’. Para o leitor, essa definição torna-se evidente quando existe um recipiente em que se possa falar em profundidade ou altura h (Figura 2.8). Figura 2.8 A pressão no ponto A será pA = γ hA, enquanto a carga de pressão será hA; da mesma forma, no ponto B, pB = γ hB e a carga de pressão será hB. Será que só nesses casos é que se pode falar em carga de pressão? Vejamos como seria interpretada a carga de pressão no caso de uma tubulação.

<!-- p. 23 -->
Na Figura 2.9a tem-se, por exemplo, um tubo por onde escoa um fluido de peso específico γ e à pressão p. Supondo o diâmetro do tubo pequeno, a pressão do fluido em todos os pontos da seção transversal será aproximadamente a mesma. Como, porém, há uma pequena diferença, adotem-se como referência os pontos do eixo do tubo. Note-se que nesse caso existe uma pressão p, mas não há nenhuma altura h. Será que ainda se pode falar em carga de pressão? Se possível, como deverá ser interpretada? Abrindo-se um orifício no conduto, verifica-se que, se a pressão interna for maior que a externa, um jato de líquido será lançado para cima. Figura 2.9 Se esse jato for canalizado por meio de um tubo de vidro, verifica-se que o líquido sobe até alcançar uma altura h. Essa coluna de líquido deverá, para ficar em repouso, equilibrar exatamente a pressão p do conduto. Dessa forma, novamente, γfluido × h coluna = p conduto Nota-se então que o h da coluna é exatamente a carga de pressão de p. Logo, pode-se falar em carga de pressão independentemente da existência da profundidade h. Pode-se dizer, então, que carga de pressão é a altura à qual pode ser elevada uma coluna de fluido por uma pressão p. Dessa forma, é sempre possível, dada uma coluna h de fluido, associar-lhe uma pressão p, dada por γh, assim como é possível, dada uma pressão p, associar-lhe uma altura h de fluip do, dada por , denominada carga de pressão.

γ

## 2.6 Escalas de pressão

Se a pressão é medida em relação ao vácuo ou zero absoluto, é chamada ‘pressão absoluta’; quando é medida adotando-se a pressão atmosférica como referência, é chamada ‘pressão efetiva’. A escala de pressões efetivas é importante, pois praticamente todos os aparelhos de medida de pressão (manômetros) registram zero quando abertos à atmosfera, medindo, portanto, a diferença entre a pressão do fluido e a do meio em que se encontram. Se a pressão é menor que a atmosférica, costuma ser chamada impropriamente de vácuo e mais propriamente de depressão; é claro que uma depressão na escala efetiva terá um valor negativo. Todos os valores da pressão na escala absoluta são positivos. A Figura 2.10 mostra, esquematicamente, a medida da pressão nas duas escalas, a efetiva e a absoluta. Da discussão anterior e da Figura 2.10 verifica-se que vale a seguinte relação entre as escalas: pabs = patm + pef onde pef pode ser positiva ou negativa.

(2.5)

<!-- p. 24 -->
Figura 2.10 A pressão atmosférica é também chamada pressão barométrica e varia com a altitude. Mesmo num certo local, ela varia com o tempo, dependendo das condições meteorológicas. Nos problemas que envolvem leis de estado de gases, é imprescindível o uso da escala absoluta, como foi visto no item 1.12 do Capítulo 1. Em problemas envolvendo líquidos, o uso da escala efetiva é mais cômodo, pois, nas equações, a pressão atmosférica, em geral, aparece nos dois membros, podendo ser cancelada. Sempre que for utilizada a escala absoluta, após a unidade de pressão será indicada a abreviação (abs), enquanto, ao se usar a escala efetiva, nada será indicado.

## 2.7 Unidades de pressão

As unidades de pressão podem ser divididas em três grupos: a) Unidades de pressão propriamente ditas, baseadas na definição (F/A). Entre elas, as mais utilizadas são: kgf/m2; kgf/cm2; N/m2 = Pa (pascal); daN/cm2 = bar (decanewton por centímetro quadrado); lb/pol2 = psi (pounds per square inches = libras por polegada ao quadrado). A relação entre essas unidades é facilmente obtida por uma simples transformação: 1 kgf/cm2 = 104 kgf/m2 = 9,8 × 104 Pa = 0,98 bar = 14,2 psi. b) Unidades de carga de pressão utilizadas para indicar a pressão. Essas unidades são indicadas por uma unidade de comprimento seguida da denominação do fluido que produziria a carga de pressão (ou coluna) correspondente à pressão dada. Lembrar, pelo item 2.5, que existe uma correspondência biunívoca entre p e h, através do peso específico γ do fluido. Assim, por exemplo: mmHg (milímetros de coluna de mercúrio) mca (metros de coluna de água) cmca (centímetros de coluna de água) A determinação da pressão em unidades de pressão propriamente ditas é feita lembrando que p = γh. Assim, por exemplo, 5 mca correspondem a 5 m × 10.000 N/m3 = 50.000 N/m2 (onde 10.000 N/m3 é o peso específico da água). Ainda, por exemplo, 20 mmHg correspondem a 0,02 m × 136.000 N/m3 = 2.720 N/m2 (onde 136.000 N/m3 é o peso específico do mercúrio). Vice-versa, a pressão de 2.720 N/m2 corresponde a 2.720 = 0,272 mca. 10.000 Assim, na prática, a representação da pressão em unidade de coluna de fluido é bastante cômoda, pois permite visualizar imediatamente a possibilidade que tem uma certa pressão de elevar um fluido a uma certa altura.

<!-- p. 25 -->
c) Unidades definidas. Entre elas, destaca-se a unidade atmosfera (atm), que, por definição, é a pressão que poderia elevar de 760 mm uma coluna de mercúrio. Logo, 1 atm = 760 mmHg = 101.230 Pa = 101,23 kPa = 10.330 kgf/m2 = 1,033 kgf/cm2 = 1,01 bar = 14,7 psi = 10,33 mca. Determinar o valor da pressão de 340 mmHg em psi e kgf/cm2 na escala efetiva e em Pa e atm na escala absoluta. (patm = 101,2 kPa)

1) 760 mmHg 1,033 kgf/cm2 340 x x = 1,033 × 340 = 0,461 kgf 760 cm 2 2) 760 mmHg 14,7 psi 340 y y = 340 × 14,7 = 6,6 psi 760 3) Para determinar a pressão na escala absoluta, basta lembrar que:

pabs = pef + patm 760 mmHg 101.230 Pa 340 z z = 340 × 101.230 = 45.287 Pa = 45,3 kPa 760 Logo, pabs = 45,3 + 101,2 = 146,5 kPa (abs)

4) 760 mmHg 1 atm 340 u u = 340 × 1= 0,447atm 760 Logo, pabs = 0,447 + 1 = 1,447 atm (abs)

## 2.8 O barômetro

A pressão atmosférica é medida pelo barômetro. Se um tubo cheio de líquido, fechado na extremidade inferior e aberto na superior, for virado dentro de uma vasilha do mesmo líquido, ele descerá até uma certa posição e nela permanecerá em equilíbrio (Figura 2.11). Desprezando a pressão de vapor do líquido, na parte superior obtém-se, praticamente, o vácuo perfeito ou pressão zero absoluto. Já foi visto que a pressão num mesmo nível é a mesma, logo: p0 = pA = patm. Dessa forma, a coluna h formada é devida à pressão atmosférica e tem-se patm = γh. O líquido utilizado é, geralmente, o mercúrio, já que seu peso específico é suficientemente elevado de maneira a formar um pequeno h e, portanto, pode ser usado um tubo de vidro relativamente curto. Como a pressão atmosférica padrão é muito utilizada, é interessante tê-la em mente: patm = 760 mmHg = 10.330 kgf/m2 = 101,3 kPa

<!-- p. 26 -->
Figura 2.11

## 2.9 Medidores de pressão

### 2.9.1 Manômetro metálico ou de Bourdon

Pressões ou depressões são comumente medidas pelo manômetro metálico (Figura 2.12). Esse nome provém do fato de que a pressão é medida pela deformação do tubo metálico indicado na figura. Ao ligar o manômetro pela tomada de pressão, o tubo fica internamente submetido a uma pressão p que o deforma, havendo um deslocamento de sua extremidade que, ligada ao ponteiro por um sistema de alavancas, relacionará sua deformação com a pressão do reservatório. Figura 2.12 A leitura da pressão na escala efetiva será feita diretamente no mostrador, quando a parte externa do manômetro estiver exposta à pressão atmosférica. Suponha-se, agora, o caso da Figura 2.13.

Figura 2.13 Nesse caso, a parte interna do tubo metálico está sujeita à pressão p1, e a externa, à p2. Dessa forma, o manômetro indicará não a pressão p1, mas a diferença p1 – p2. Logo, pmanômetro = ptomada de pressão – pexterna (2.6)

<!-- p. 27 -->
### 2.9.2 Coluna piezométrica ou piezômetro

Consiste num simples tubo de vidro que, ligado ao reservatório, permite medir diretamente a carga de pressão (Figura 2.14). Logo, dado o peso específico do fluido, pode-se determinar a pressão diretamente. Figura 2.14 O piezômetro apresenta três defeitos que o tornam de uso limitado: a) A altura h, para pressões elevadas e para líquidos de baixo peso específico, será muito alta. Exemplo: água com pressão de 105 N/m2 e cujo peso específico é 104N/m3 formará uma coluna p 105 h = γ = 104 = 10m Logo, não sendo viável a instalação de um tubo de vidro com mais de 10 m de altura, o piezômetro não pode, nesse caso, ser útil. Nota-se então que esse aparelho só serve para pequenas pressões. b) Não se pode medir pressão de gases, pois eles escapam sem formar a coluna h. c) Não se pode medir pressões efetivas negativas, pois nesse caso haverá entrada de ar para o reservatório, em vez de haver a formação da coluna h.

### 2.9.3 Manômetro com tubo em U

A Figura 2.15 mostra um manômetro de tubo em U. Nesse manômetro corrige-se o problema das pressões efetivas negativas. Se isso ocorrer, a coluna de fluido do lado direito ficará abaixo do nível A-A. A Figura 2.15b mostra o mesmo manômetro com a inclusão de um fluido manométrico que, em geral, é mercúrio. A presença do fluido manométrico permite a medida da pressão de gases, já que impede que estes escapem. Figura 2.15

<!-- p. 28 -->
Ao mesmo tempo, utilizando um fluido manométrico de elevado peso específico, diminui-se a altura da coluna que se formaria com um líquido qualquer. Os manômetros de tubo em U, ligados a dois reservatórios, em vez de ter um dos ramos aberto à atmosfera, chamam-se manômetros diferenciais (Figura 2.16). Figura 2.16

### 2.9.4 A equação manométrica

É a expressão que permite, por meio de um manômetro, determinar a pressão de um reservatório ou a diferença de pressão entre dois reservatórios. Seja o manômetro da Figura 2.17. Pode-se calcular a pressão no fundo dos dois ramos. Pelo Teorema de Stevin, e lembrando que, segundo Pascal, a pressão se transmite integralmente a todos os pontos do fluido, tem-se: Figura 2.17 pressão no fundo do ramo esquerdo:

pfe = pA + γA (h1 – h2) + γM h2 (1)

pressão no fundo do ramo direito:

pfd = pB + γB (h4 – h3) + γM h3 (2)

Como o fluido está em equilíbrio, então a pressão no mesmo nível deve ser a mesma. Logo, pfe = pfd Portanto, pA + γA (h1 – h 2) + γMh2 = p B + γB (h4 – h 3) + γMh3 ou pB = pA + γA (h1 – h2) – γB (h4 – h 3) – γM (h3 – h 2)

Nota-se que cada peso específico aparece multiplicado pela respectiva altura da coluna, sem necessidade de adotar como referência o fundo. Baseada nessa observação, será mostrada uma regra prática e de fácil aplicação.

<!-- p. 29 -->
Regra Começando do lado esquerdo, soma-se à pressão pA a pressão das colunas descendentes e subtrai-se aquela das colunas ascendentes. Note-se que as cotas são sempre dadas até a superfície de separação de dois fluidos do manômetro. Tem-se, portanto: pA + γ1h1 + γ2h2 – γ3h3 + γ4h4 – γ5h5 – γ6h6 = pB Dado o esquema da figura: 1) Qual é a leitura no manômetro metálico? 2) Qual é a força que age sobre o topo do reservatório? Figura 2.18 Solução 1) Determinação de pM Usando a equação manométrica, lembrando que o γ dos gases é pequeno e que, portanto, pode-se desprezar o efeito da coluna de ar em face de outros efeitos; lembrando, ainda, que ao trabalhar na escala efetiva patm = 0 tem-se: p M + γ 0h 0 + γ H2Oh H2O – γ H2O L sen 30o = 0 L sen 30o é o desnível da coluna de água no ramo direito, pois, pelo teorema de Stevin, a pressão independe da distância, dependendo somente da diferença de cotas.

<!-- p. 30 -->
Logo: p M = gH 2O(L sen 30o – h H 2O ) – g0h 0 pM = 10.000 (0,6 × 0,5 – 0,2) – 8.000 × 0,1 pM = 200 N/m2 2) Pela definição de pressão Ftopo = pM A = 200 × 10 = 2.000 N

## 2.10 Força numa superfície plana submersa

Se um fluido está em repouso, pela sua definição, não podem existir forças tangenciais agindo nele: todas as forças serão normais à superfície submersa. Se a pressão tiver uma distribuição uniforme sobre a superfície, a força será determinada multiplicando-se a pressão pela área correspondente, e o ponto de aplicação será o centro de gravidade da superfície. No caso dos gases, mesmo quando a superfície é vertical, a variação de pressão nessa direção é muito pequena, já que o seu peso específico o é; logo, qualquer que seja a posição da superfície, a força exercida será o produto da pressão pela área. No caso dos líquidos, a distribuição de pressão será uniforme somente se a superfície submersa for horizontal. Seja o traço AB do plano perpendicular ao plano da Figura 2.19. A pressão efetiva varia desde zero na superfície livre, até BC = p = γh no fim da superfície plana. A variação da pressão desde o topo até o fundo do plano deverá ser linear, pois sabe-se pelo teorema de Stevin que a pressão é diretamente proporcional à profundidade, sendo o coeficiente de proporcionalidade o peso específico do fluido. Figura 2.19 Como a pressão varia de ponto para ponto, é óbvio que nesse caso não é possível obter a força pela expressão pA. A força resultante de um lado da superfície plana será, portanto, a somatória dos produtos das áreas elementares pela pressão nelas agente. O ponto de aplicação da força resultante irá se localizar abaixo do CG, isto é, deslocado para o lado das maiores pressões. É claro que, quanto mais se afunda a superfície AB (como para a posição A' B'), mais o ponto de aplicação da força resultante aproxima-se do CG, já que as pressões vão se tornando mais uniformes. O ponto de aplicação da força resultante chama-se centro das pressões (CP). O cálculo do módulo da força resultante das pressões se baseará na Figura 2.20.

<!-- p. 31 -->
Figura 2.20 Todas as propriedades referentes ao centro de gravidade serão indicadas por um traço e todas as referentes ao centro de pressões, pelo índice CP. Seja AB o traço do plano em estudo, no plano do papel, formando um ângulo θ com a superfície livre. Deseja-se determinar nesse plano a força resultante das pressões. Seja, na figura (b), a projeção da superfície em estudo sobre um plano vertical. Seja h uma profundidade genérica e y a correspondente distância até a superfície livre no plano da superfície. Seja Ox a intersecção da superfície plana AB com a superfície livre do fluido. Seja o elemento de área dA, no qual a pressão é constante, pois é horizontal. Tem-se: dA = xdy; p = γh No elemento dA, a força será:

e h = y sen θ Integrando, tem-se:

dF = pdA = γhdA = γy sen θ dA F = γsen θ ∫ ydA Por definição do centro de gravidade, tem-se:

y = 1 A ∫ ydA Logo: ∫ ydA = yA Substituindo:

F = γsen θ y A Logo:

F = γh A = p A (2.7)

Dessa forma, verifica-se que a força resultante é obtida pelo produto da pressão, no centro de gravidade da superfície, por sua própria área. Note-se que a resultante independe do ângulo formado pela superfície, desde que o CG se mantenha fixo.

<!-- p. 32 -->
## 2.11 Centro das pressões

Centro das pressões é o ponto de aplicação da força resultante das pressões sobre uma certa área. O eixo Ox da Figura 2.20 será adotado para o cálculo do momento das forças. A força elementar na placa será dada por: pdA = γy sen θ dA = dF O momento será dado pelo produto da força pela distância ao eixo:

y dF = γ y2 sen θ dA (2.8)

Se a resultante das forças de pressão for F e a distância do ponto de aplicação ao eixo Ox for yCP, tem-se, integrando a Equação 2.8: ∫ yCP F = γ sen θ y2 dA = γ sen θ Io (2.9)

∫ onde Io = y2 dA é o chamado momento de inércia da área A em relação ao eixo Ox. Dividindo-se a Equação 2.9 pela Equação 2.7, tem-se:

y CP = γsen θI o = γsen θyA Io yA (2.10)

isto é, a distância do centro das pressões ao eixo intersecção da superfície imersa com a superfície livre do fluido é obtida dividindo-se o momento de inércia da área A, em relação ao mesmo eixo, pelo produto da distância do centro de gravidade pela área da superfície imersa. Uma das propriedades do momento de inércia é: I o = I CG + y 2A onde I CG é o momento de inércia calculado em relação a um eixo que passa pelo centro de gravidade da superfície de área A. Logo, a Equação 2.10 pode ser escrita: y CP = y+ I CG yA (2.11)

Dessa expressão, conclui-se imediatamente que o centro das pressões localiza-se abaixo do centro de gravidade e que, ao aumentar a profundidade, os dois pontos se aproximam. A posição do centro das pressões em relação a um eixo y será dada pela expressão: ∫ x CPF = xpdA Para figuras simétricas, o centro das pressões estará sempre localizado sobre o eixo da simetria, se este for perpendicular ao eixo Ox. Na placa retangular da figura, de largura 2 m, determinar a força devida à água numa de suas faces e seu ponto de aplicação (γ = 10.000 N/m3).

<!-- p. 33 -->
A pressão no centro de gravidade, devida ao líquido, será:

p = hγ = (1+ 2,5 sen 30 ° ) 10.000 = 22.500 N / m2 portanto:

F = pA = 22.500 × 5 × 2 = 225.000 N y CP − y = ICG yA l ∫ ∫ ICG = y2dA em relação a um eixo passando pelo CG. Pela figura, dA = bdy, ICG = 2 y 2bdy –l = bl3 12 2 Essa expressão, referindo-se a um eixo que passa pelo CG, é a mesma para qualquer retângulo que tenha um dos lados paralelos ao eixo Ox. bl3 yCP − y= 12 yA y = 1 sen 30o + l 2 = 2 + 2,5 = 4,5 m A = b × l = 2 × 5 = 10 m2 bl3 = 2 × 53 ≅ 20,8 m4 12 12 y CP − y = 20,8 4,5 × 10 = 0,46 m ou yCP = 0,46 + 4,5 = 4,96 m A esta altura cabe uma observação. Note-se que a força calculada é somente devida ao líquido em que a superfície está submersa. Normalmente, deveria se considerar também a pressão acima da superfície livre do líquido, que poderia ser ou não a pressão atmosférica. Nesse caso, a pressão p seria dada por: p = p 0 + γh Figura 2.21

<!-- p. 34 -->
Nos exercícios, em geral, a pressão p0 age em ambos os lados da placa, não precisando ser levada em consideração. Num caso geral, pode-se levar em conta a pressão p0, utilizando todas as mesmas expressões deduzidas, substituindo-a por um acréscimo do líquido em estudo igual à sua carga de pressão. A altura do líquido, em vez de ser h, passará a ser h'= h + p0 γ Determinar a força R que deverá ser aplicada no ponto A da comporta da figura para que permaneça em equilíbrio, sabendo-se que ela pode girar em torno do ponto O. Dados:

p01 = 100 kPa p02 = 50 kPa γ1 = 10.000 N/m3 γ2 = 8.000 N/m3 Comporta retangular com h = 5 m e b = 2 m.

Solução O problema deve ser reduzido a um outro em que a pressão efetiva, no nível dos dois líquidos, seja nula. Para tanto, substitua-se p01 e p02 por cargas de pressão correspondentes aos dois líquidos do problema. h 01 = p01 γ1 = 100 × 103 10.000 = 10 m h 02 = p02 γ2 = 50 × 103 8.000 = 6,25 m Note-se que h01 e h02 são as alturas fictícias dos líquidos que causariam, em seus níveis reais, respectivamente, as pressões p01 e p02. Pressão no CG do lado (1):

p1 = γ 1h 1 = 10.000 (10 + 1+ 2,5)= 135.000 N / m2 Força resultante do lado (1): F1 = p1A1 = 135.000 × 5 × 2 = 1.350.000 N = 1.350 kN Centro das pressões do lado (1): y CP1 – y1 = ICG y1A = bh 3 h1 × 12 bh = h2 12h 1 h CP1 − h 1 = 52 12 × 13,5 = 0,15 m

<!-- p. 35 -->
Distância do CP1 ao ponto O:

Pressão no CG do lado (2):

b1 = 2,5 + 0,15 = 2,65 m p2 = γ 2h 2 = 8.000 (6,25 + 1+ 2,5) = 78.000 N / m 2 Força resultante do lado (2):

CP do lado (2):

F2 = p2A2 = 78.000 × 5 × 2 = 780.000 N y CP2 − y2 = ICG y2A = bh 3 h2 × 12 bh = h2 12h 2 h CP2 – h 2 = 12 52 × 9,75 = 0,21 m Distância do CP2 ao ponto O:

b2 = 2,5 + 0,21 = 2,71 m Para que a comporta permaneça em equilíbrio, sem girar em torno do ponto O, é necessário que a somatória dos momentos, em relação a esse ponto, seja nula: R.h + F2b2 = F1b1 R = F1b1 – F2b2 = 1.350.000 × 2,65 – 780.000 × 2,71 h 5 R = 293.000 N

## 2.12 Força em superfícies reversas, submersas

Em qualquer superfície reversa, as forças nos diversos elementos de área são diferentes em módulo e direção, de forma que é impossível obter uma somatória delas. A Equação 2.7 é, portanto, aplicável somente a superfícies planas. No entanto, para qualquer superfície reversa, pode-se determinar a força resultante em certas direções, como a horizontal e a vertical. A resultante dessas duas componentes somente poderá ser determinada se ambas estiverem num mesmo plano.

### 2.12.1 Componente horizontal

Na Figura 2.22a, observa-se uma superfície AB qualquer, projetada sobre um plano vertical, originando a superfície plana A' B'. Tem-se, então, entre a superfície AB e sua projeção A' B', um volume em equilíbrio estático. Figura 2.22

<!-- p. 36 -->
As únicas forças horizontais que agem nesse volume são F' e Fx.

Fx = F' Logo, a componente horizontal que age em qualquer superfície é igual à força horizontal que age numa superfície plana, projeção daquela sobre um plano vertical. Por razões de equilíbrio, a direção deve ser a mesma. Como já se aprendeu a determinar módulo e ponto de aplicação em superfícies planas, a solução em relação a A' B' resolve o problema da superfície genérica AB.

### 2.12.2 Componente vertical

A componente vertical pode ser obtida considerando o volume contido entre uma superfície qualquer AB e sua projeção no plano da superfície livre do líquido (Figura 2.22b). Esse volume está em equilíbrio estático. Se a pressão na superfície for atmosférica, as únicas forças verticais serão o peso G do volume e Fy devido à pressão na superfície AB. Logo: Fy = G Como essas são as únicas forças verticais agentes, por razões de equilíbrio Fy e G devem ter a mesma direção. Como o peso tem de passar pelo CG do volume, então Fy será vertical e sua direção passará por aquele ponto. A força vertical exercida por um gás é igual ao produto da pressão pela projeção dessa superfície sobre uma superfície horizontal. No caso de a superfície não conter líquido acima dela, a noção não se altera. A força vertical será igual ao peso do volume de líquido imaginário contido entre a superfície e o nível da superfície livre.

## 2.13 Empuxo

Tudo o que for dito neste item poderia ter sido concluído no item 2.12. No entanto, optou-se por apresentá-lo em um novo item para dar maior destaque ao estudo do empuxo, que é de grande utilidade. No item 2.12.2, verificou-se que a componente vertical que age numa superfície submersa é igual ao peso do volume de fluido, real ou fictício, contido acima da superfície. Considere-se, então, o corpo ABCD da Figura 2.23.

Figura 2.23 Esse corpo pode ser imaginado como formado por duas superfícies: uma superfície ABC, em que todas as forças de pressão possuem uma componente vertical de sentido para cima, e outra superfície ADC, em que todas as forças de pressão possuem uma componente vertical de sentido para baixo. A resultante das componentes na superfície ABC, pelo que foi dito anteriormente, será dada por: Na superfície ADC, tem-se:

Fy = γVUABCV F'y = γVUADCV

<!-- p. 37 -->
O saldo Fy – F' y será uma força vertical para cima, indicada por E e chamada empuxo. ( ) E = Fy – F'y = γ VUABCV – VUADCV ou E = γVABCD = γV (2.12)

onde: E = empuxo V = volume de fluido deslocado pelo corpo γ = peso específico do fluido A Equação 2.12 pode ser expressa em palavras pelo princípio de Arquimedes: “Num corpo total ou parcialmente imerso num fluido, age uma força vertical de baixo para cima, chamada empuxo, cuja intensidade é igual ao peso do volume de fluido deslocado”. Pela noção de empuxo, é fácil estabelecer a condição de flutuação de um corpo (Figura 2.24). Figura 2.24 Suponha-se um corpo totalmente submerso. Ele flutuará se seu peso G for menor que o empuxo. E ≥G No caso da igualdade, o corpo estará em equilíbrio em qualquer posição. Imaginando o corpo totalmente submerso: Logo:

Vcorpo = Vdeslocado O corpo flutuará se:

γ fluido Vdeslocado ≥ γ corpo Vcorpo γ fluido ≥ γ corpo (2.13)

## 2.14 Flutuador — Nomenclatura

Corpo flutuante ou flutuador é qualquer corpo que permanece em equilíbrio quando está parcial ou totalmente imerso num líquido. Plano de flutuação é o plano horizontal da superfície livre do fluido. Linha de flutuação é a intersecção do plano de flutuação com a superfície do flutuador. Seção de flutuação é a seção plana cujo contorno é a linha de flutuação. Volume de carena é o volume de fluido deslocado pela parte imersa do flutuador. Note-se que o peso do volume de carena é igual à intensidade do empuxo. Centro de carena é o ponto de aplicação do empuxo. Se o fluido for homogêneo, o centro de carena coincidirá com o centro de gravidade do volume de carena (Figura 2.25).

<!-- p. 38 -->
Figura 2.25

## 2.15 Estabilidade

As forças que agem num corpo total ou parcialmente submerso em repouso são o seu peso (G), cujo ponto de aplicação é o centro de gravidade do corpo, e o empuxo (E), cujo ponto de aplicação é o centro de carena. Torna-se evidente que, para que um flutuador esteja em equilíbrio, é necessário que essas duas forças tenham a mesma intensidade, a mesma direção e sentidos opostos. Resta analisar a estabilidade desse equilíbrio. Suponha-se um corpo em equilíbrio. Aplique-se uma força pequena nesse corpo. É evidente que, se ele estava em equilíbrio, a aplicação dessa força isolada fará com que se desloque em relação à posição inicial. Retirando essa força, aplicada durante um intervalo de tempo muito pequeno, podem acontecer três coisas: a) o corpo retorna à posição de equilíbrio inicial: diz-se que o equilíbrio é estável; b) o corpo, mesmo retirando a força, afasta-se cada vez mais da posição inicial: diz-se que o equilíbrio é instável; c) o corpo permanece na nova posição, sem retornar, mas sem se afastar mais da posição inicial: diz-se que o equilíbrio é indiferente. A análise da estabilidade no caso de flutuadores reduz-se à estabilidade vertical e de rotação, já que para deslocamentos horizontais o equilíbrio é indiferente.

## 2.16 Estabilidade vertical

### 2.16.1 Corpo totalmente submerso em equilíbrio

Se o corpo estiver totalmente submerso em equilíbrio, o volume deslocado será sempre o mesmo. Qualquer que seja o deslocamento, sempre existirá o equilíbrio, de forma que é um caso de equilíbrio indiferente.

### 2.16.2 Corpo parcialmente submerso em equilíbrio

Nesse caso, ao deslocar o corpo para baixo, o volume de carena e o empuxo aumentam, ficando numa situação em que E > G. Ao retirar a força que causou o deslocamento, o flutuador sobe até que haja uma diminuição no volume de carena para que novamente E = G. Se o corpo for deslocado para cima, o volume de carena diminuirá, de forma que E < G. Ao retirar a força aplicada, o corpo desce até que E = G novamente, e isso acontece na posição inicial. Note-se que, em relação a deslocamentos verticais, os flutuadores têm um equilíbrio estável.

<!-- p. 39 -->
## 2.17 Estabilidade à rotação

Suponha-se um flutuador obrigado a abandonar a sua posição de equilíbrio, por uma pequena força que o faça girar de um pequeno ângulo em torno de um eixo de rotação. Nessa situação, devem ser examinados dois casos para os quais o comportamento é diferente.

### 2.17.1 Corpo totalmente submerso em equilíbrio

Suponha-se um corpo totalmente submerso em equilíbrio, cujo centro de gravidade esteja abaixo do centro de carena (Figura 2.26). Figura 2.26 Se o corpo girar de um pequeno ângulo, o CG e o CC permanecerão fixos em relação a ele, de forma que o empuxo e o peso, de módulos constantes e sempre verticais, vão se encontrar na posição indicada em (b). Dessa forma, fica criado um conjugado que tende a girar o corpo no sentido contrário ao da rotação. É evidente que o corpo tenderá novamente à posição (a), que será, portanto, de equilíbrio estável. Se o CG estiver acima do CC (Figura 2.27), o conjugado criado pelo empuxo e pelo peso tenderá a girar mais o corpo, de forma que ele se afastará ainda mais da posição de equilíbrio inicial. Nesse caso, a posição (a) da Figura 2.27 será de equilíbrio instável. Figura 2.27 Observa-se que num corpo totalmente submerso em equilíbrio, para que haja estabilidade à rotação, o centro de gravidade deverá estar abaixo do centro de carena. Num corpo homogêneo em equilíbrio totalmente submerso num fluido homogêneo, o centro de gravidade do corpo coincide com o centro de gravidade do volume de carena; logo, coincide com o centro de carena. Dessa forma, o CC e o CG coincidem e o corpo estará sempre numa situação de equilíbrio indiferente.

<!-- p. 40 -->
### 2.17.2 Corpo parcialmente submerso em equilíbrio

Nesse caso, o estudo não é tão simples como no caso dos corpos totalmente submersos. É óbvio que o centro de gravidade abaixo do centro de carena é uma garantia para que o equilíbrio seja estável; entretanto, essa condição não é necessária. Às vezes, a rotação do corpo causa uma variação no formato do volume de carena (o que não acontecia com o corpo totalmente submerso), o que cria um deslocamento no centro de carena, em relação ao corpo, tal que o equilíbrio pode ser estável mesmo que este esteja abaixo do centro de gravidade. Pela Figura 2.28, nota-se que se o corpo estivesse totalmente submerso, o volume deslocado seria constante, de forma que o CC acompanharia o movimento do corpo, mantendo-se fixo em relação a ele. Isso, como já foi visto, causaria o aparecimento de um conjugado a favor da rotação, que provocaria o afastamento indefinido da posição de equilíbrio. Figura 2.28 Estando o corpo parcialmente submerso, com a rotação em torno do eixo O, o volume de carena, que era ABCD, passa a ser LICB, com conseqüente deslocamento do centro de carena para a esquerda em CC'. Fica assim mostrado, intuitivamente, que o flutuador terá condições de retornar à posição inicial, estando, portanto, em equilíbrio estável desde que o empuxo esteja à esquerda do peso, como na Figura 2.28. Note-se que o sentido do conjugado pode ser analisado pela posição do ponto M, chamado metacentro, que é a intersecção do eixo de simetria do flutuador com a direção do empuxo. Se o ponto M estiver acima do CG, o conjugado será contrário à rotação e o equilíbrio, estável. Se o ponto M estiver abaixo do CG, o conjugado será a favor da rotação e o equilíbrio, instável. Se o ponto M estiver em CG, o equilíbrio será indiferente. Note-se que quanto mais acima estiver o metacentro em relação ao CG, maior será o conjugado que contraria a rotação e, portanto, mais estável o equilíbrio. Por essa observação, conclui-se que é importante conhecer a distância do metacentro ao centro de gravidade. Tal distância, chamada altura metacêntrica, será indicada por r (Figura 2.29). Figura 2.29

<!-- p. 41 -->
Para efeito da determinação de r, considere-se o perfil da Figura 2.29a, tendo girado de um ângulo θ pequeno em torno do eixo de rotação O. Note-se que o volume de carena alterou-se de V123 para V425, fazendo com que o CC se desloque para CC'. No entanto, E = E', já que o volume, apesar de mudar de forma, é o mesmo. O momento de E' em relação ao ponto CC deverá ser igual ao momento dos elementos de volume de V425 em relação ao mesmo ponto. Entretanto, nota-se que V402 é simétrico ao V302, de forma que o momento em relação a CC será nulo.

Então:

Eδ = Momento do V305 Eδ = ∫ xdf Mas df = dVγ = dAx tg θγ onde dA é um elemento de área horizontal, da seção de flutuação.

Eδ = ∫ γx 2 tgθdA = γ tgθ∫ x 2dA ∫ Mas x 2dA = I y é o momento de inércia da área da seção de flutuação em relação ao eixo y (Figura 2.30). Logo:

Note-se que:

Eδ = γ tg θI y E = γV e tg θ = δ ( r + l) cos θ Logo: γVδ = γ (r + δ l) cos θ Iy ou r+l = Iy V cos θ Se o ângulo θ for pequeno, como se admitiu, r = Iy – l V (2.14)

Como no caso do equilíbrio G = E = γV então G V= γ Logo:

r = γI y – l G (2.15) Figura 2.30 Como já foi visto, deve-se ter r > 0 e, quanto maior, maior será a estabilidade. Logo, a estabilidade do flutuador será aumentada diminuindo l e, portanto, abaixando o centro de gravidade ou aumentando γIy/G, isto é, aumentando o momento de inércia da seção de flutuação.

<!-- p. 42 -->
1. Um navio desloca 9,45 × 106 N e tem uma seção de flutuação como a indicada na figura. O centro de carena está a 1,8 m abaixo da superfície de flutuação e o centro de gravidade, a 0,3 m. Determinar a altura metacêntrica em relação a uma inclinação em torno do eixo y. Solução Pela Equação 2.15, Tem-se r = γIy – l G l = 1,8 – 0,3 = 1,5 m Iy1 = bh 3 12 = 24 × 93 12 = 1.458 m 4 Iy2 = bh 3 48 = 12 × 93 48 = 182 m 4 Iy = 1.458 + 182 = 1.640 m 4 Logo: r = 10.000 × 1.640 – 1,5 9,45 × 106 r = 0,24 m > 0 2. Uma balsa tem o formato de um paralelepípedo com 9 m de largura, 24 m de comprimento e 2,4 m de altura. A balsa pesa 4,72 × 106 N quando carregada e o seu centro de gravidade está a 3 m acima do fundo. Determinar a altura metacêntrica. Solução É preciso determinar a distância l entre o centro de gravidade e o centro de carena. Para isso, deve-se determinar a altura z, pois l = 3 – z/2. Sabe-se que: E = γV = G V = G γ = 4,72 × 104 106 = 472 m3

<!-- p. 43 -->
Logo: Tem-se:

Portanto:

C a p í t u l o 2 z Estática dos fluidos z 43 z = 472 = 2,18 m 24 × 9 l = 3 1,09 ≅ 1,9 m r = γIy – l = Iy – l G V Iy = 1 12 bh 3 = 24 × 93 12 = 1.458 m4 r = 1.458 – 1,9 = 1,2 m 472

## 2.18 Equilíbrio relativo — Introdução

Suponha-se um fluido contido num recipiente que se move com translação uniformemente variada (acelerada ou retardada) (Figura 2.31). Figura 2.31 Em relação ao sistema de referência fixo O' XYZ, o fluido estará em movimento. No entanto, adotando-se o sistema Oxyz fixo ao recipiente, nota-se que o fluido, após um certo deslocamento inicial, permanecerá em equilíbrio com uma configuração que será estável, desde que a aceleração seja mantida constante. Como as partículas do fluido não terão movimento em relação ao recipiente, fica excluída a presença de tensões de cisalhamento, podendo esse caso ser tratado como um caso de equilíbrio e ser estudado pela estática dos fluidos. Como o fluido só estará em repouso em relação ao sistema de eixos Oxyz que se movem em relação a O' XYZ, esse estudo será chamado equilíbrio relativo. Note-se que, para que isso aconteça, é suficiente que a aceleração seja constante, incluindo-se nesse estudo também o movimento circular e uniforme, em que a aceleração tangencial é nula e a centrípeta mantém-se constante.

## 2.19 Recipiente com movimento de translação uniformemente acelerado segundo a horizontal

Sejam o recipiente da Figura 2.32 e o fluido nele contido em equilíbrio em relação ao sistema de referência fixo no recipiente.

<!-- p. 44 -->
Figura 2.32 Opera-se da mesma forma que no item 2.2 (teorema de Stevin), lembrando apenas que agora haverá uma variação de pressão dependente da distância entre os dois pontos, e não somente da diferença de cotas. Adotemos os pontos genéricos (1), (2), (3): Na vertical:

p2A – p1A – γA (z1 – z2) = 0 (Equilíbrio) Logo:

p2 – p1 = γ (z1 – z2)

ou p2 – p1 = γΔz1,2 (2.16)

Logo, na vertical continua válido o teorema de Stevin. Na horizontal, pelo princípio de D’Alambert, no sistema relativo, por causa do equilíbrio, prode-se substituir o efeito da aceleração pelo efeito de uma força fictícia de inércia dada por (–ma). Pela condição de equilíbrio: p2A – p3A – max = 0 ou p2A – p3A – ρA (x3 – x2) ax = 0 Logo:

p2 – p3 = ρΔx3,2 ax (2.17)

A variação de pressão entre dois pontos quaisquer será dada pela soma de uma variação segundo a vertical e uma segundo a horizontal. Pelas equações 2.16 e 2.17, a variação de pressão entre os pontos (1) e (3) será: p3 – p1 = –ρΔx3,2 ax + γΔz1,2 mas z2 = z3 e x1 = x2 Logo:

p3 – p1 = –ρΔx3,1 ax + γΔz1,3 ou Δp3,1 = –ρΔx3,1 ax – γΔz3,1 (2.18)

Essa equação permite, dadas as coordenadas de dois pontos quaisquer, determinar a diferença de pressão entre eles. É interessante, nesse estudo, determinar a inclinação das superfícies em que a pressão se mantém constante (isobáricas). Lembre o leitor que, num fluido não acelerado, tais superfícies eram horizontais. Se os pontos (3) e (1) da Equação 2.18 pertencem a uma superfície de pressão constante, tem-se: Δp = 0 e –ρΔx3,1 ax + γΔz3,1 = 0 ou Δz 1,3 Δx 3,1 = ρa x γ

<!-- p. 45 -->
Δz 1,3 Δx 3,1 = ρa x g Note-se que a superfície livre é de pressão constante e que Δz/Δx = tg θ (Figura 2.33); logo, as superfícies de pressão constante serão paralelas a ela e formarão um ângulo θ com a horizontal. Figura 2.33 Logo: tgθ = a x g (2.19)

Se o recipiente for fechado, não existirá superfície livre, mas as superfícies de pressão constante continuarão a obedecer à Equação 2.19. Um tanque hermeticamente fechado possui uma aceleração de 6 m/s2 para a direita. Qual é a pressão nos manômetros A e B indicados na figura? (γ = 10.000 N/m3, g = 10 m/s2) Qual é a inclinação das superfícies de pressão constante? Solução Pela Equação 2.18, tem-se γ pA – pC = –ρax (xA – xC) – (zA – zC)

Como zA = zC , obtém-se ou pA – pC = –ρax (xC – xA) pA = ρax (xC – xA) + pC = 1.000 × 6 × 1,2 + 105 pA = 107,2 kPa Note-se que A e B estão na mesma vertical; logo, xA = xB γ pA – pB = – (zA – zB)

ou pB = pA + γ (zA – zB) = 107.200 + 10.000 × 0,6 pB = 113,2 kPa

<!-- p. 46 -->
A inclinação das linhas de pressão constante será dada por tg θ = ax/g = 6/10 = 0,6 θ ≅ 31°

## 2.20 Recipiente com movimento de translação uniformemente acelerado segundo a vertical

Nesse caso, as superfícies a pressão constante mantêm-se horizontais, havendo apenas uma variação na diferença de pressão entre dois pontos, em relação ao caso de repouso. Quando a aceleração é para cima, o efeito da força de inércia irá se somar ao efeito da gravidade; caso contrário, será subtraído. Tem-se:

p2A – p1A – γA Δz1,2 m ρA Δz1,2 a y = 0 onde o sinal negativo corresponde à Figura 2.34a.

p 2 – p1 = γΔz 1,2 m ρa yΔz 1,2 ou p2 – p1 = γΔz 1,2 ⎛ ⎜⎝ 1 ± ay g ⎞ ⎠⎟ Δp 2,1 = – γΔz 2,1 ⎛ ⎜1± ⎝ ay g ⎞ ⎟ ⎠ Figura 2.34 (2.20) (2.21)

## 2.21 Recipiente com movimento de translação uniformemente acelerado ao longo de um plano inclinado

Figura 2.35

<!-- p. 47 -->
Paralelo a z:

p 2A – p1A – γV cos α = 0 p 2A – p1A = γAΔz1,2 cos α p 2 – p1 = γΔz1,2 cos α (2.22)

Paralelo a x, adotando-se um A' tal que, qualquer que seja x3, o peso do segundo cilindro seja igual ao do primeiro: p2 A' – p3 A' – ma x – γV sen α = 0 p2 A' – p3 A' = ρA' Δx3,2 a x + γA' Δx3,2 sen α p 2 – p 3 = ρΔx 3,2 a x + γΔx 3,2 sen α Diferença de pressão entre dois pontos quaisquer Pelas equações 2.22 e 2.23, tem-se:

(2.23)

p 3 – p1 = γΔz1,2 cosα – ρΔx 3,2 a x – γΔx 3,2 senα mas z 2 = z 3 e x1 = x2 Logo:

p 3 – p1 = – γΔz 3,1 cosα – ρΔx 3,1a x – γΔx 3,1 senα Planos de pressão constante Nos pontos desses planos Δp = 0, logo:

– γΔz 3,1 cosα – ρΔx 3,1a x – γΔx 3,1 senα = 0 (2.24) Da Figura 2.36, nota-se que tgθ = Δz Δx Logo:

tgθ = ρa x + γ sen a γ cos a ou tgθ = a x + tg α g cos α Figura 2.36 (2.25)

<!-- p. 48 -->
## 2.22 Recipiente com movimento de rotação de velocidade angular ω constante

Figura 2.37 Seja um sistema de coordenadas cilíndricas, isto é, um eixo z coincidente com o de rotação e um eixo r, normal a z e com origem em qualquer ponto desse eixo. A coordenada r determina qualquer ponto de uma circunferência de raio r. Note-se que, nesse caso, haverá variações da pressão ao longo da vertical e ao longo do raio r, já que a aceleração centrípeta é função deste. Pela Figura 2.37, teremos na vertical:

p 2 – p1 = γΔz 1,2 Ao longo de um raio r qualquer p 2A – p3A – ma c = 0 Note-se que:

m = ρ(r2 – r3 )A (2.26)

e que a aceleração centrípeta média no cilindro horizontal indicado será dada por: ac = ω2 (r3 + r2 ) 2 Logo: ou ou p2 A – p3A = ρ( r2 – r3 )A ω 2 ( r3 + r2 ) 2 p2 – p3 = r (r22 – r32 2 )ω 2 p2 – p3 = ρ ω2 2 Δr22,3 A variação da pressão entre dois pontos quaisquer será dada por:

p3 – p1 = –r ω2 2 Δr12,3 + γΔz 1,3 ou p3 – p1 = r ω2 2 Δr32,1 – γΔz 3,1 (2.27) (2.28)

<!-- p. 49 -->
As superfícies de pressão constante são tais que Δp = 0.

Logo:

γΔz = ρ ω 2 Δr 2 2 ou Δz ω2 = Δr 2 2g (2.29)

A Equação 2.29 é a equação de um parabolóide de revolução; logo, este será também o formato da superfície livre, se existir. Um tanque de base circular possui um tubo vertical cujo eixo está a uma distância R do eixo do tanque. Inicialmente encontra-se parado e cheio de água até o nível da tampa. Em seguida, passa a girar em torno de seu eixo com uma rotação n = 120 rpm, e o nível da água no tubo vertical sobe até uma altura h acima do nível, no centro aberto à atmosfera. Calcular h no ponto médio do tubo vertical. Dados: R = 0,5 m; ρ = 1.000 kg/m3, π g = 10 m/s2 Solução Sejam os pontos (1), que é o vértice da parábola na situação de equilíbrio, e (2), que é o ponto mais alto do eixo do tubo vertical. Esses pontos estarão à mesma pressão (patm). Sendo z1 = 0 e r1 = 0, tem-se como conseqüência que z2 = h e r2 = R. Logo: p2 – p1 = ρω2 2 Δr22,1 – γΔz 2,1 ou z2 – z1 = ω2 2g ( r22 – r12 ) ou h = ω2R2 2g Como ω = 2πn, então h = 4π2n 2R2 = 2 π2n 2R2 2g g Logo:

h = 2 π2(120 60 )2( 0,5 π )2 = 0,2 m 10

<!-- p. 50 -->
2.1 No sistema da figura, desprezando-se o desnível entre os cilindros, determinar o peso G, que pode ser suportado pelo 2,5 cm2; AIII = 5 pistão V. Desprezar os cm2; AIV = 20 cm2; AV = atritos. 10 cm2; Dados: h = 2m; p1 = 500 kPa; γHg = 136.000 NA/I =m31.0 cm2; AHI = 2 cm2; AII = Resp.: G = 135 N 2.2 Aplica-se uma força de 200 N na alavanca AB, como é mostrado na figura. Qual é a força F que deve ser exercida sobre a haste do cilindro para que o sistema permaneça em equilíbrio? Resp.: F = 10 kN 2.3 Qual é a de uma altura da coluna de mercúrio (γHg coluna de água de 5 m de altura? = 136.000 N/m3) que irá ( γ H2 O = 10.000 N/ m 3 )

produzir na base a mesma pressão Resp.: hHg = 368 mm 2.4 Determinar a pressão de 3,5 atm nas outras unidades de pressão na escala efetiva e, sendo a pressão atmosférica local 740 mmHg, determinar a pressão absoluta em todas as unidades de pressão. Resp.: pef = 3,5 atm = 0,362 MPa = 3,61kgf cm2 = 36.200 kgf m 2 = 36,2 mca = 2.660 mmHg pabs = 4,47 atm = 0,47 MPa = 4,62 kgf cm2 = 46.200 kgf m2 = 46,2 mca = 3.397 mmHg

## 2.5 No γ Hg

manômetro da figura, o fluido A é água = 136.000 N / m3 ; γ H 2O = 10.000 N / m3. e o fluido B, mercúrio. Qual é a pressão p1? Dados:

<!-- p. 51 -->
Resp.: p1 = 13,35 kPa 2.6 No manômetro diferencial da figura, o fluido A é água, B é óleo e o fluido manométrico é mercúrio. Sendo γH2 h1 = 25 cm, O = 10.000 N hm2 =3 ; 100 γ Hg cm, h3 = 80 = 136.000 N cm m3 e ;γ h4 óleo = = 10 cm, qual 8.000 N m3.

é a diferença de pressão pA– pB? Dados:

Resp.: pA – pB = –132,1 kPa 2.7 Calcular a leitura do manômetro A da figura. γ Hg = 136.000 N m3 Resp.: pA = 79,6 kPa 2.8 Determinar as pressões efetivas e absolutas:

1) do ar; 2) no ponto M, na configuração a seguir. Dados: leitura barométrica 740 mmHg; γóleo = 8.500 N/m3; γ Hg = 136.000 N m3

<!-- p. 52 -->
Resp.: 1) par = 34 kPa; par abs = 134 kPa (abs)

2) pM = 36,55 kPa; pM abs = 136,55 kPa (abs)

2.9 No dispositivo da figura, a leitura do manômetro é 30 kPa e a relação de áreas dos pistões é A2 / A1 = 2. A pressão atmosférica no local é 700 mmHg. Estando escala absoluta em mca. Dados: γ = 27.000 N/m3; γ H 2O = 10.000 N m3 ; A1 / AH = 2; α = 30°. o a sistema = 100 em equilíbrio, pede-se cm; b = 80 cm; γ Hg a = pressão 136.000 pB N na m3 Resp.: pB = 17,12 mca (abs)

2.10 D1.0e0te0rkmgi/nmar3;ρpAa,tmp0= e p0 100 abs na kPa; g configuração = 10 m/s2.

do desenho, sendo dados: hB = 0,1 m; hA = 0,2 m; ρB = Resp.: ρA = 500 kg/m3; p0 = –1.000 Pa; p0 abs = 99 kPa (abs). 2.11 No sistema da figura, na situação inicial a esfera está vazia. Introduz-se óleo pelo funil até preencher totalmente o recipiente esférico e y passa a valer y'= 1 m. Dados: γ óleo = 8.000 N m3 ; γ H 2O = 10.000 N m3.

<!-- p. 53 -->
a) Qual é o valor de y na situação inicial? b) Qual é o diâmetro da esfera? c) Qual é o volume de óleo introduzido para estabelecer a situação final? Resp.: y = 0,4 m; b) D = 0,45 m; c) V = 47.833 cm3 2.12 No sistema da figura, se a escala fornece escala? Dados: D = 4,5 d; α = 11,5o; γ H 2O px = 1e0m.00m0 mNH/m2O3,.

qual é o valor real, em mm, de uma divisão da Resp.: 5 mm 2.13 Na figura a seguir, o sistema está em equilíbrio estático. Pede-se:

a) par1 em mmHg (abs); b) par2 em mca. Dados: D = 71,4 mm; d = 35,7 mm; h = 400 mm; patm = 684 mmHg; γHg = 136.000 N/m3; para F = 0 ⇒ h = 0. Resp.: a) par1 = 831 mmHg (abs); b) par2 = 3,7 mca

<!-- p. 54 -->
2.14 A figura mostra o ar contido num recipiente, inicialmente a 100°C. O ar é esfriado e a água do manômetro sobe 0,5 cm para dentro do recipiente. Dados: patm = 100 kPa; γ H 2O = 10.000 N m3 ; γ Hg = 136.000 N m3. a) Qual é a leitura inicial do manômetro? (Pa) b) Qual é a leitura final do manômetro? (Pa) c) Qual é a temperatura final do ar? (°C) Resp.: a) 25.200 Pa; b) 12.050 Pa; c) 44°C. 2.15 No manômetro da figura, são indicados os níveis dos fluidos manométricos antes e depois de ele ser ligado ao reservatório A. Pede-se: a) a leitura do manômetro em mca; b) a densidade do ar do reservatório A em kg/m3 se a temperatura dele é 20°C e R = 287 m2/s2K. Dados: γ1 = 10.000 N/m3; γ2 = 8.000 N/m3; γHg = 136.000 N/m3. Resp.: pmA = 0,0624 mca; ρA = 1,12 kg/ m 3. 2.16 Para a configuração a seguir, responder: a) Qual é a pressão do gás em valor absoluto? b) Qual é o valor da cota z? c) Aquece-se o gás de 20°C para 60°C e o desnível z varia para 1 m. Qual será o novo volume do gás, se o inicial era 2 m3? Dados: patm = 662 mmHg; γHg = 136.000 N/m3; γ H 2O = 10.000 N/m3

<!-- p. 55 -->
Resp.: a) 95 kPa (abs); b) 0,5 m; c) 2,16 m3 2.17 No esquema dado, qual é a pressão em (1) se o sistema está em equilíbrio estático? (Leitura do manômetro pm = 10 kPa.)

Resp.: p1 = 43,5 kPa 2.18 O cilindro movimenta-se dentro da tubulação circular da figura com velocidade constante. A folga entre o cilindro e a tubulação contém óleo de viscosidade dinâmica μ = 10–2 Ns/m2. a) O peso sobe ou desce? Justificar.

b) Qual é o comprimento do cilindro? c) Qual é a massa específica do material do cilindro em kg/m3? Dados: peso v = 2 m/s; g do cilindro: G = 3.950 N; diâmetro do = 10 m/s2; p1 = 50 kPa; p2 = 40 kPa.

cilindro: Dc = 0,5 m; diâmetro do tubo: Dt = 0,501 m; Resp.: a) desce; b) 0,183 m; c) 10.993 kg/m3 2.19 No manômetro da figura, sabe-se que, quando a força F é 55,6 kN, a leitura na régua é 100 cm. Determinar o valor da nova leitura, caso a força F dobre de valor.

<!-- p. 56 -->
Resp.: 128 cm 2.20 O pistão da figura desce com velocidade constante de 5 m/s. Dados: espessura da camada lubrificante 0,001 m; ν = 10–3 m2/s; patm = 100 kPa; g = 10 γm=/8s.20;0d0eNsp/rmez3;ap-sae=o1p0eksPoad; Go = 100 N; D1 = 16 pistão. Pede-se:

cm; D2 = 8 cm; AH = 20 cm2; l = 5 cm; a) a força resistente oferecida pelo lubrificante (Fμ); b) a pressão absoluta pb (cte); c) a leitura do manômetro M.

Resp.: a) 150 N; b) 60 kPa (abs); c) –50 kPa.

2.21 Calcular a pressão na câmara (1) sabendo que o pistão se desloca com uma velocidade constante de 1,2 0m,9/9s8ema;iγnódleioc=aç8ã.o00d0oNm/amn3ô;mge=tr1o0mme/tásl2i.cOo bés1e0rvkaPçaã.oD: caodnossi:dDer=ar1omn;ívLel=d0o,2ómle;oνcóolenos=ta1n0t–e3.m2/s; Dp = Resp.: p1 = –25,23 kPa

<!-- p. 57 -->
C a p í t u l o 2 z Estática dos fluidos z 57 2.22 Determinar as componentes horizontal e vertical da força devido à água que age na parte em forma de cilindro AB do tanque da figura, cuja largura é 0,3 m. Dado: γ H2O = 10.000 N/m3. Resp.: Fx = 2.160 N; Fy = 3.393 N.

2.23 Na instalação da figura, a comporta quadrada AB, que pode girar em torno de A, está em equilíbrio devido à ação da força horizontal F. Sabendo que γm = 80.000 N/m3 e γ = 30.000 N/m3, determinar o valor da força F. Resp. F = 8.640 N 2.24 Um tanque retangular, como o da figura, tem 4,5 m de comprimento, 1,2 m de largura e 1,5 m de altura. Contém 0,6 m de água e 0,6 m de óleo. Calcular a força devida aos líquidos nas paredes laterais e no fundo. Dados: γ1 = 8.500 N/m3; γ2 = 10.000 N/m3. Resp.: FA = 28.755 N; FB = 7.668 N; Ffundo = 59.948 N 2.25 A comporta AB da figura tem 1,5 m de largura e pode girar em torno de A. O tanque à esquerda contém água (γ = 10.000 N/m3) e o da direita, óleo (γ = 7.500 N/m3). Qual é a força necessária em B para manter a comporta vertical?

<!-- p. 58 -->
Resp.: FB = 50.000 N 2.26 Determinar o módulo e o ponto de aplicação das componentes horizontal e vertical da força exercida pela água sobre a comporta AB da figura, sabendo que sua largura é 0,3 m, o raio é 1,8 m e a comporta está articulada em C. Resp.: Fy = 7.634 N; Fx = 4.860 N; ycp = 1,2 m; xcp = 0,736 m 2.27 Determinar a força, devida à pressão da água, na comporta retangular da figura, sendo o peso específico do fluido 10.000 N/m3.

Resp.: F = 99,4 kN 2.28 O bujão cilíndrico da figura tem 0,6 m de diâmetro e 0,6 m de altura. Com água de um lado e óleo do outro, determinar o peso específico do material do bujão para mantê-lo em equilíbrio. Desprezar o atrito nas guias. Resp.: γb = 35.000 N/m3

<!-- p. 59 -->
2.29 A comporta da figura, em forma de ¼ de cilindro, tem peso desprezível. Determinar a relação γ1/γ2 entre os pesos específicos dos líquidos, para que a comporta não gire em torno do ponto O. Dado: x CG = 4 3 R π Resp.: γ1/γ2 = 1/3 2.30 O reservatório da figura possui uma parede móvel AB, articulada em A. Sua largura é 1,5 m e está em equilíbrio nas condições indicadas. Calcular:

a) a força que age na face direita da comporta devido à água; b) a força que deve ser aplicada em B para que seja mantido o equilíbrio.

Resp.: a) 15.000 N; b) 465 N. 2.31 A figura mostra um tanque cilíndrico. Qual é a força no fundo? Qual é a força na superfície anular MM? O tanque é aberto à atmosfera. Dado: γ = 10.000 N/m3.

Resp.: FF = 1.700 N; FM = 636 N 2.32 No esquema da figura, determinar a altura h e a mínima força F para que a comporta ABC permaneça em equilíbrio. Dados: largura = 1,5 m; γHg = 136.000 N/m3; γ H 2O = 10.000 N/m3.

<!-- p. 60 -->
Resp.: h = 3 m; F = 76.230 N 2.33 Determinar o mínimo valor de z para o qual a comporta da figura girará em torno de ponto O, se a comporta é retangular e tem largura 2 m.

Resp.: z = 6,27 m 2.34 A comporta ABC da figura é rígida e pode girar em torno de B. Sabendo que está em equilíbrio, determinar o comprimento BC.

Resp.: BC = 1 m 2.35 Sabendo que γ1 = 6 γ2, calcular a relação x/h para que a comporta permaneça em equilíbrio na posição indicada na figura. Desprezar o peso próprio da comporta.

Resp.: x/h = 1/2 2.36 A comporta ABCDEF da figura, articulada no extremo A, mantém-se na condição de equilíbrio pela ação da força H aplicada em F. Sendo γ = 10.000 N/m3 e a largura da comporta igual a 1 m, determinar o valor de H e o da força vertical que solicita a articulação em A.

<!-- p. 61 -->
Resp.: H = 204 kN; V = 120 kN 2.37 Um cilindro de ferro fundido, de 30 cm de diâmetro e 30 cm de altura, é imerso em água do mar (γ = 10.300 N/m3). Qual é o empuxo que a água exerce no cilindro? Qual seria o empuxo se o cilindro fosse de madeira (γ = 7.500 N/m3)? Nesse caso, qual seria a altura submersa do cilindro? Resp.: E = 218 N; E = 159 N; hsub = 0,218 m 2.38 Um cilindro que pesa 500 N e cujo diâmetro é 1 m flutua na água (γ = 10.000 N/m3), com seu eixo na vertical, como mostra a figura. A âncora consiste de 0,23 m3 de concreto de peso específico 25.000 N/m3. Qual é a elevação da maré necessária para elevar a âncora do fundo? (Desprezar o peso da barra.) Resp.: h = 0,3 m 2.39 O corpo maciço de seção triangular e largura 1 m deve flutuar na posição indicada pela figura. Calcular a força a ser aplicada no plano da superfície AB e a sua distância ao ponto A. Dados: peso específico do corpo γc = 2.000 N/m3; AB = 1,8 m; BC = 0,6 m; γ H2O = 10.000 N/m3. Resp.: xF = 2,7 m; F = 270 N

<!-- p. 62 -->
2.40 Um sistema de bóia é utilizado para abrir um reservatório de água quando o nível deste atinge o plano diametral da esfera. Calcular a área do disco de fechamento do reservatório, sabendo que a área da seção transversal m; R = 0,3 m; γ =da10h4asNte/émA3.o = 0,02 m2 e o peso do conjunto (esfera, haste e disco) é 55 N. Dados: h = 3 Resp.: Ad = 336 cm2 2.41 Um corpo pesa 800 N no ar e, quando imerso em água (γ = 10.000 N/m3), tem um peso aparente de 500 N. Determinar o volume do corpo e seu peso específico. Observação: peso aparente é o peso do corpo menos o empuxo. Resp.: V = 0,03 m3; γ = 26.670 N/m3 2.42 Um densímetro pesa 2,2 × 10–2 N. A sua parte superior é constituída de uma haste cilíndrica de 5 mm de diâmetro. Qual será a diferença de altura de flutuação quando o densímetro estiver mergulhado em dois líquidos de peso específico 7.800 N/m3 e 8.200 N/m3, respectivamente? Resp.: h = 7,2 mm 2.43 Determinar a altura de óleo (γo = 6.000 N/m3) para que o corpo (γc = 8.000 N/m3) passe da posição (1) para a posição (2).

Resp.: ho = 0,8 m 2.44 A comporta de perfil AB, articulada em A e de largura 1 m, possui uma bóia esférica de diâmetro D = 2 m e peso G = 6.000 N. Sabendo que a comporta se abre quando o nível da água atinge o ponto A, conforme mostra a figura, calcular a distância x do centro da bóia até a articulação A. Observação: considerar o peso da comporta AB desprezível. Dados: γ =104 N/m3.

<!-- p. 63 -->
Resp.: x = 6 m 2.45 Um cilindro, de peso especifico γc = 5.000 N/m3, flutua num líquido, conforme mostra a figura (1). Sob a ação de uma força F = 10.000 N, o cilindro permanece na posição indicada na figura (2). Determinar os pesos específicos dos líquidos A e B. Dado: área da base do cilindro = 1 m2. Resp.: γA = 15.000 N/m3; γB = 25.000 N/m3 2.46 Um balão esférico de 12 m de diâmetro está cheio de hidrogênio. Se a leitura do barômetro é 700 mmHg e a temperatura é 20º C, qual o peso do conjunto balão e lastro para que seja mantido estacionário? Dados: Rar = 287 m2/s2K; RH2 = 41.400 m2/s2K. Resp.: 10.171 N 2.47 Um cubo de peso específico γc flutua num líquido de peso específico γl. Determinar a relação γc/γl para que o cubo flutue com as arestas na vertical. Resp.: 0 < γ c < 0,21 ; 0,79 < γ c < 1 γl γl 2.48 Um objeto de madeira é mostrado na figura. O seu peso é 2,5 N e o centro de gravidade está a 5 cm da superfície superior. O equilíbrio é estável em relação ao eixo y?

<!-- p. 64 -->
Resp.: É estável (r = 0,037 m).

2.49 Qual a máxima altura H de um cilindro de seção circular de raio R, para que possa flutuar em equilíbrio estável com seu eixo na vertical em qualquer líquido? Dados: cilindro (γ); líquido (γl). Resp.: H < R 1 2γ γl ⎜⎛1 – ⎝ γ γl ⎞ ⎟ ⎠ 2.50 Determinar a diferença de pressão entre dois pontos genéricos de um tanque cheio de água acelerado verticalmente para cima com uma aceleração ay = 5 g. Resp.: Δp = 6γΔz 2.51 Um tubo em U contendo água é montado num carro de corrida. O carro parte com aceleração constante e 5 s após a partida a água no tubo em U apresenta a configuração indicada. Sendo g = 9,8 m/s2: a) Qual é a aceleração? b) Qual é a velocidade do carro nesse instante? Resp.: a = 3,57 m/s2; v = 64,2 km/h 2.52 Um tanque cúbico de 0,6 m de lado, com óleo até a metade, é acelerado ao longo de um plano inclinado de 30o com a horizontal. Determinar a inclinação da superfície livre em relação ao plano inclinado.

<!-- p. 65 -->
Resp.: θ = 41o 2.53 Um acelerômetro é constituído de um tanque e de um manômetro metálico, como indica a figura. Adiciona-se mercúrio 10 m/s2. Pede-se:

no tubo até que a leitura no manômetro seja 175 kPa. Dados: γHg = 136.000 N/m3; g = a) Qual é a leitura do mercúrio no piezômetro? b) Qual é a aceleração horizontal que provoca uma leitura de 140 kPa no manômetro, supondo inalterado o nível do mercúrio? Resp.: h = 1,29 m; a = 1,72 m/s2 2.54 Um tanque fechado, com a forma indicada na figura, com 0,6 m de lado, gira em torno de um eixo com rotação n = 100 rpm e a uma distância radial de 1,5 m. Qual é a pressão nos pontos A, B e C? (ρ = 1.000 kg/m3; patm = 100 kPa) Resp.: pA = 120 kPa (abs); pB = 126 kPa (abs); pC = 106 kPa (abs) 2.55 Um veículo move-se com velocidade constante de 100 km/h para a direita, carregando um recipiente retangular aberto que contém água. O veículo é freado em 10 s até parar com desaceleração constante. Dados: ρ = 1.000 kg/m3; g = 10 m/s2; não há transbordamento. Determinar: a) a inclinação da superfície livre em relação à horizontal, durante a frenagem; b) a pressão nos pontos A e B durante a frenagem.

<!-- p. 66 -->
Resp.: θ = 15o30’; pB = 6.400 Pa; pA = 3.600 Pa 2.56 Um recipiente aberto à atmosfera está situado sobre um veículo que se movimenta com uma aceleração a0 constante. A superfície livre da água do recipiente forma um ângulo de 30o com a horizontal. Os manômetros situados nas paredes do recipiente indicam 100 kPa e 110 kPa. Calcular o comprimento L do recipiente e a aceleração a0. Dados: ρ = 1.000 kg/m3; g = 10 m/s2. Resp.: L = 1,73 m; a0 = 5,8 m/s2 2.57 Um veículo carrega um recipiente que contém água, movimentando-se com uma velocidade constante de 72 km/h. Calcular o tempo mínimo de frenagem com desaceleração constante para que a água não transborde. Dados: g = 10 m/s2; ρ = 1.000 kg/m3. Resp.: t = 5 s 2.58 Um tanque, cheio de água e totalmente fechado, cai verticalmente sob a ação da gravidade e de uma força de FH. gD.oDisetmeramnôinmaertaroinstseintusiaddaodseaduamfoarçdaisFtâ. Dncaidaovse:rgti=ca1l0hm=/1sm2; γiHngd=ic1a3m6.0p010=N2/0mcm3; de Hg massa e p2 = 10 cm do conjunto = 1.000 kg.

Resp.: F = 13,6 kN

<!-- p. 67 -->

# Capítulo 3 — Cinemática dos fluidos

## 3.1 Regimes ou movimentos variado e permanente

Regime permanente é aquele em que as propriedades do fluido são invariáveis em cada ponto com o passar do tempo. Note-se que as propriedades do fluido podem variar de ponto para ponto, desde que não haja variações com o tempo. Isso significa que, apesar de um certo fluido estar em movimento, a configuração de suas propriedades em qualquer instante permanece a mesma. Um exemplo prático disso será o escoamento pela tubulação do tanque da Figura 3.1, desde que o nível dele seja mantido constante. (1) NC NC = Nível Constante (2) Figura 3.1 Nesse tanque, a quantidade de água que entra em (1) é idêntica à quantidade de água que sai por (2); nessas condições, a configuração de todas as propriedades do fluido, como velocidade, massa específica, pressão etc., será, em cada ponto, a mesma em qualquer instante. Note-se que em cada ponto a velocidade, por exemplo, é diferente, assim como a pressão o será, pela lei de Stevin. Regime variado é aquele em que as condições do fluido em alguns pontos ou regiões de pontos variam com o passar do tempo. Se no exemplo da Figura 3.1 não houver fornecimento de água por (1), o regime será variado em todos os pontos. Denomina-se reservatório de grandes dimensões um reservatório do qual se extrai ou no qual se admite fluido, mas, devido à sua dimensão transversal muito extensa, o nível não varia sensivelmente com o passar do tempo. Em um reservatório de grandes dimensões, o nível mantém-se aproximadamente constante com o passar do tempo, de forma que o regime pode ser considerado aproximadamente permanente. A Figura 3.2a mostra um reservatório de grandes dimensões, em que, apesar de haver uma descarga do fluido, o nível não varia sensivelmente com o passar do tempo, e o regime pode ser considerado permanente.

<!-- p. 68 -->
A Figura 3.2b mostra um reservatório em que a seção transversal é relativamente pequena em face da descarga do fluido. Isso faz com que o nível dele varie sensivelmente com o passar do tempo, havendo uma variação sensível da configuração do sistema, caracterizando um regime variado. Figura 3.2

## 3.2 Escoamentos laminar e turbulento

Para definir esses dois tipos de escoamentos, recorre-se à experiência de Reynolds (1883), que demonstrou a sua existência. Seja, por exemplo, um reservatório que contém água. Um tubo transparente é ligado ao reservatório e, no fim deste, uma válvula permite a variação da velocidade de descarga da água. No eixo do tubo é injetado um líquido corante do qual se deseja observar o comportamento (Figura 3.3). Nota-se que ao abrir pouco a válvula, portanto para pequenas velocidades de descarga, forma-se um filete reto e contínuo de fluido colorido no eixo do tubo (3). Ao abrir mais a válvula (5), o filete começa a apresentar ondulações e finalmente desaparece a uma pequena distância do ponto de injeção. Nesse último caso, como o nível (2) continua descendo, conclui-se que o fluido colorido é injetado, mas, devido a movimentos transversais do escoamento, é totalmente diluído na água do tubo (3). Esses fatos denotam a existência de dois tipos de escoamentos separados por um escoamento de transição. Figura 3.3 No primeiro caso, em que é observável o filete colorido reto e contínuo, conclui-se que as partículas viajam sem agitações transversais, mantendo-se em lâminas concêntricas, entre as quais não há troca macroscópica de partículas. No segundo caso, as partículas apresentam velocidades transversais importantes, já que o filete desaparece pela diluição de suas partículas no volume de água.

<!-- p. 69 -->
Escoamento laminar é aquele em que as partículas se deslocam em lâminas individualizadas, sem trocas de massa entre elas. Escoamento turbulento é aquele em que as partículas apresentam um movimento aleatório macroscópico, isto é, a velocidade apresenta componentes transversais ao movimento geral do conjunto do fluido. O escoamento laminar é o menos comum na prática, mas pode ser visualizado num filete de água de uma torneira pouco aberta ou no início da trajetória seguida pela fumaça de um cigarro, já que a uma certa distância dele notam-se movimentos transversais. Reynolds verificou que o fato de o movimento ser laminar ou turbulento depende do valor do número adimensional dado por: Re = ρvD μ = vD υ (3.1)

Essa expressão se chama número de Reynolds e mostra que o tipo de escoamento depende do conjunto de grandezas v, D e ν, e não somente de cada uma delas. Esse aspecto será mais bem discutido no capítulo de análise dimensional. Reynolds verificou que, no caso de tubos, seriam observados os seguintes valores: Re < 2.000 Escoamento laminar 2.000 <Re < 2.400 Escoamento de transição Re > 2.400 Escoamento turbulento Note-se que o movimento turbulento é variado por natureza, devido às flutuações da velocidade em cada ponto. Pode-se, no entanto, muitas vezes, considerá-lo permanente, adotando em cada ponto a média das velocidades em relação ao tempo. Esse fato é comprovado na prática, já que somente aparelhos muito sensíveis conseguem indicar as flutuações dos valores das propriedades em cada ponto. A maioria dos aparelhos, devido ao fato de apresentarem uma certa inércia na medição, indicará um valor permanente em cada ponto que corresponderá exatamente à média citada anteriormente (Figura 3.4). Figura 3.4 Assim, mesmo que o escoamento seja turbulento, poderá, em geral, ser admitido como permanente em média nas aplicações.

## 3.3 Trajetória e linha de corrente

Trajetória é o lugar geométrico dos pontos ocupados por uma partícula em instantes sucessivos. Note-se que a equação de uma trajetória será função do ponto inicial, que individualiza a partícula, e do tempo. Uma visualização da trajetória será obtida por meio de uma fotografia, com tempo longo de exposição, de um flutuante colorido colocado num fluido em movimento (Figura 3.5).

<!-- p. 70 -->
Figura 3.5 Linha de corrente é a linha tangente aos vetores da velocidade de diferentes partículas no mesmo instante. Note-se que, na equação de uma linha de corrente, o tempo não é uma variável, já que a noção se refere a um certo instante. A visualização pode ser feita lançando, por exemplo, serragem em diversos pontos do escoamento e tirando em seguida uma fotografia instantânea. A serragem irá, num pequeno intervalo de tempo, apresentar um curto espaço percorrido que representará o vetor velocidade no ponto. A linha de corrente será obtida traçando-se na fotografia a linha tangente aos traços de serragem (Figura 3.6). Figura 3.6 As linhas de corrente e as trajetórias coincidem geometricamente no regime permanente. Tubo de corrente é a superfície de forma tubular formada pelas linhas de corrente que se apóiam numa linha geométrica fechada qualquer (Figura 3.7). Figura 3.7 Propriedades dos tubos de corrente a) Os tubos de corrente são fixos quando o regime é permanente. b) Os tubos de corrente são impermeáveis à passagem de massa, isto é, não existe passagem de partículas de fluido através do tubo de corrente.

A propriedade (a) é óbvia, já que, quando o regime é permanente, não há variação da configuração do fluido e de suas propriedades. A propriedade (b) pode ser verificada por absurdo, supondo que uma partícula cruze o tubo de corrente. Para que isso ocorresse, seria necessário que o vetor da velocidade fosse oblíquo em relação ao tubo de corrente, o que não pode acontecer, pois ele é formado de linhas de corrente que, por definição, são tangentes aos vetores da velocidade. Essa propriedade é muito importante, pois em regime permanente garante que as partículas de fluido que entram de um lado do tubo de corrente deverão sair do outro, não havendo adição nem subtração de partículas através do tubo. A sua utilidade será vista nas equações básicas de mecânica dos fluidos.

<!-- p. 71 -->
## 3.4 Escoamento unidimensional ou uniforme na seção

O escoamento é dito unidimensional quando uma única coordenada é suficiente para descrever as propriedades do fluido. Para que isso aconteça, é necessário que as propriedades sejam constantes em cada seção (Figura 3.8). Figura 3.8 Na figura, pode-se observar que em cada seção a velocidade é a mesma, em qualquer ponto, sendo suficiente fornecer o seu valor em função da coordenada x para obter sua variação ao longo do escoamento. Diz-se, nesse caso, que o escoamento é uniforme nas seções. Na Figura 3.9 observa-se um escoamento bidimensional, em que a variação da velocidade é função das duas coordenadas x e y. Nesse escoamento, o diagrama de velocidades repete-se identicamente em planos paralelos ao plano x,y. O escoamento no espaço pode ser tridimensional (Figura 3.10).

Figura 3.9 Figura 3.10 Note-se que, com o aumento do número de dimensões, as equações se complicam e é conveniente, sempre que possível, descrever o escoamento de forma unidimensional conforme um critério que será apresentado posteriormente.

<!-- p. 72 -->
## 3.5 Vazão — Velocidade média na seção

A vazão em volume pode ser definida facilmente pelo exemplo da Figura 3.11.

Figura 3.11 Suponha-se que, estando a torneira aberta, seja empurrado o recipiente da Figura 3.11 embaixo dela e simultaneamente seja disparado o cronômetro. Admita-se que o recipiente encha em 10 s.

Pode-se então dizer que a torneira enche 20 L em 10 s ou que a vazão em volume da tor20 L neira é = 2 L s. 10 s Define-se vazão em volume Q como o volume de fluido que atravessa uma certa seção do escoamento por unidade de tempo.

V Q= (3.2) t As unidades correspondem à definição: m3/s, L/s, m3/h, L/min, ou qualquer outra unidade de volume ou capacidade por unidade de tempo.

Existe uma relação importante entre a vazão em volume e a velocidade do fluido (Figura 3.12). Figura 3.12 Suponha-se o fluido em movimento da Figura 3.12.

No intervalo de tempo t, o fluido se desloca através da seção de área A a uma distância s. O volume de fluido que atravessa a seção de área A no intervalo de tempo t é V = sA. Logo, a vazão será V sA s Q = = , mas =v tt t Logo: Q = vA (3.3)

<!-- p. 73 -->
É claro que essa expressão só seria verdadeira se a velocidade fosse uniforme na seção. Na maioria dos casos práticos, o escoamento não é unidimensional; no entanto, é possível obter uma expressão do tipo da Equação 3.3 definindo a velocidade média na seção. Figura 3.13 Obviamente, para o cálculo da vazão, não se pode utilizar a Equação 3.3, pois v é diferente em cada ponto da seção. Adotando um dA qualquer no entorno de um ponto em que a velocidade genérica é v, como na Figura 3.13, tem-se: dQ = v dA Logo, a vazão na seção de área A será:

Q = ∫Av dA (3.4)

Define-se velocidade média na seção como uma velocidade uniforme que, substituída no lugar da velocidade real, reproduziria a mesma vazão na seção. Logo:

∫ Q = A v dA = vm A (3.5)

Dessa igualdade, surge a expressão para o cálculo da velocidade média na seção:

∫1 vm = A v dA A (3.6) Figura 3.14 Determinar a velocidade média correspondente ao diagrama de velocidades a seguir. Supor que não haja variação da velocidade segundo a direção normal ao plano da figura (escoamento bidimensional).

<!-- p. 74 -->
Sendo o diagrama linear, tem-se v = C1y + C2, com C1 e C2 a serem determinados pelas condições de contorno. Para y = 0 Para y = h v = 0, v = v0, logo: C2 = 0 logo: v0 = C1h e C1 = v0 h ou, finalmente, v = v0 y h A velocidade média será dada por:

∫ ∫ Vm = 1 v dA = 1 AA bh h v0 0 y h bdy = v0 h2 y2 2 h 0 vm = v0 2 No diagrama a seguir está representado o resultado.

Assim como se define a vazão em volume, podem ser analogamente definidas as vazões em massa (Qm) e em peso (QG ). Qm = m t onde m = massa de fluido (3.7) QG = G t onde G = peso de fluido (3.8)

Pela Equação 3.5, Q = vmA, mas Qm = m t = ρV t Logo: e Qm = ρQ = ρvm A QG = G t = γV t (3.9) ou QG = γQ = γ vmA (3.10)

Por outro lado, QG = γQ = ρgQ e QG = gQm (3.11)

As unidades de vazão em massa serão kg/s, utm/s, kg/h e qualquer outra que indique massa por unidade de tempo. As unidades de vazão em peso serão kgf/s, N/s, kgf/h e qualquer outra que indique peso por unidade de tempo.

## 3.6 Equação da continuidade para regime permanente

Seja o escoamento de um fluido por um tubo de corrente (Figura 3.15). Num tubo de corrente não pode haver fluxo lateral de massa. Seja a vazão em massa na seção de entrada Qm1 e na saída Qm2. Para que o regime seja permanente, é necessário que não haja variação de propriedades, em nenhum ponto do fluido, com o tempo.

<!-- p. 75 -->
Figura 3.15 Se, por absurdo, Qm1 ≠ Qm2, então em algum ponto interno ao tubo de corrente haveria ou redução ou acúmulo de massa. Dessa forma, a massa específica nesse ponto variaria com o tempo, o que contrariaria a hipótese de regime permanente. Logo:

Qm1 = Qm2 ou ρ1Q1 = ρ2Q2 ou ρ1v1A1 = ρ2v2A2 (3.12)

Essa é a equação da continuidade para um fluido qualquer em regime permanente.

Um gás escoa em regime = 4 kg/m3 e v1 = 30 m/s.

permanente no trecho de Na seção (2), A2 = 10 cm2 tubulação da figura. e ρ2 = 12 kg/m3.

Na seção (1), tem-se A1 = 20 cm2, ρ1 Qual é a velocidade na seção (2)? Solução Qm1 = Qm2 ou portanto, Logo: ρ1v1A1 = ρ2v2A2 v2 = v1 ρ1 ρ2 A1 A2 v 2 = 30 4 12 20 10 = 20 m / s Se o fluido for incompressível, então a massa específica na entrada e na saída do volume V deverá ser a mesma. Dessa forma, a Equação 3.12 ficará ρ Q1= ρ Q2 ou Q1 = Q2 ou v1A1 = v2A2 (3.13)

Logo, a vazão em volume de um fluido incompressível é a mesma em qualquer seção do escoamento. A Equação 3.13 é a equação da continuidade para um fluido incompressível. Fica subentendido que v1 e v2 são as velocidades médias nas seções (1) e (2). A Equação 3.13 mostra que, ao longo do escoamento, velocidades médias e áreas são inversamente proporcionais, isto é, à diminuição da área correspondem aumentos da velocidade média na seção e vice-versa.

<!-- p. 76 -->
76 z Mecânica dos Fluidos O Venturi é um tubo convergente/divergente, como é mostrado na figura. Determinar a velocidade na seção mínima (garganta) de área 5 cm2, se na seção de entrada de área 20 cm2 a velocidade é 2 m/s. O fluido é incompressível. Solução Pela equação da continuidade:

veAe = vGAG vG = ve Ae AG = 2 20 5 = 8 m /s Para o caso de diversas entradas e saídas de fluido, a Equação 3.12 pode ser generalizada por uma somatória de vazões em massa na entrada (e) e outra na saída (s), isto é, ∑Qm =∑Qm (3.14) e s Se o fluido for incompressível e for o mesmo em todas as seções, isto é, se for homogêneo, a Equação 3.13 poderá ser generalizada por ∑Q =∑Q (3.15) e s Apesar de a Equação 3.14 só poder chegar à Equação 3.15 quando se tratar de um único fluido, pode-se verificar que é válida também para diversos fluidos, desde que sejam todos incompressíveis (vide o Exercício 3.7).

## 3.7 Velocidade e aceleração nos escoamentos de fluidos

Antes de mostrar a determinação das grandezas cinemáticas do item 3.7, convém ressaltar alguma coisa sobre sistemas de referência. Note-se que os sistemas que podem ser utilizados são inerciais ou em movimento, dependendo da conveniência do problema estudado. O que realmente interessa é o movimento relativo entre o fluido e o objeto. Assim, no movimento de um barco dentro da água, é interessante fixar o sistema ao barco e pensar no fluido em movimento em torno dele. Esse é o ponto de vista utilizado quando se testa um modelo de navio num tanque de provas. Note-se que a noção de regime permanente e variado é função do observador ou do sistema de referência. Assim, um problema de regime variado poderá ser reduzido a um em regime permanente por uma escolha conveniente do sistema de referência. Seja, por exemplo, o movimento de um barco em água parada. Para um observador fixado à margem do lago, por exemplo, o movimento é variado, pois pontos da água que num certo instante estavam parados irão adquirir um certo movimento quando o barco passar num instante sucessivo. Se, porém, o observador for fixado ao barco, a configuração do movimento do fluido em torno do barco será sempre a mesma, sendo o regime permanente.

<!-- p. 77 -->
A simples observação desse fato permitirá simplificar muitos problemas às vezes complicados para um sistema de referência inercial.

Vejamos como determinar a aceleração das partículas de um fluido no caso de regime permanenrte e nro caso rde regirme variado. Seja v = vx e x + vy e y + vz e z a velocidade num sistema cartesiano. Se o regime for permanente, nem a velocidade nem suas componentes serão função do tempo, sendo somente funções do ponto.

Logo:

vx = vx( x, y, z)

vy = vy( x, y, z)

r r v z = v z (x, y, z) dv Mas a = , que, como função de função, permite escrever:

dt r ∂vr dx ∂rv dy ∂rv dz a= + + ∂x dt ∂y dt ∂z dt (3.16) mas Logo: mas dx dy dz vx = dt ; vy = dt ; vz = dt r ∂rv ∂vr ∂vr a = vx ∂x + vy ∂y + vz ∂z ∂rv ∂x = ∂v x ∂x r ex + ∂v y ∂x r ey + ∂v z ∂x r ez ∂rv ∂y = ∂v x ∂y r ex + ∂v y ∂y r ey + ∂v z ∂z r ez ∂rv ∂z = ∂v x ∂z r ex + ∂v y ∂z r ey + ∂v z ∂z r ez As equações em coordenadas cartesianas ficarão, segundo suas componentes:

rr a × ex =ax = vx ∂v x ∂x + vy ∂v x ∂y + vz ∂v x ∂z rr a × ey =ay = vx ∂v y ∂x + vy ∂v y ∂y + vz ∂v y ∂z rr a × ez =az = vx ∂v z ∂x + vy ∂v z ∂y + vz ∂v z ∂z (3.17) No caso de fluido em regime variado, deve-se considerar, em relação às equações 3.17, também a variação com o tempo, ficando as equações: ax ⎛ = ⎝⎜ vx ∂v x ∂x + vy ∂v x ∂y + vz ∂v x ∂z ⎞ ⎟⎠ + ∂vx ∂t ay ⎛ = ⎜ ⎝ v x ∂v y ∂x + vy ∂v y ∂y + vz ∂v y ⎞ ⎟ ∂z ⎠ + ∂vy ∂t (3.18) az ⎛ = ⎝⎜ vx ∂v z ∂x + vy ∂v z ∂y + vz ∂v z ∂z ⎞ ⎟⎠ + ∂vz ∂t

<!-- p. 78 -->
As equações 3.17 representam a aceleração de transporte, pois indicam a variação da velocidade somente com a mudança de posição. Nas equações 3.18, as parcelas ∂vx , ∂vy e ∂vz representam a aceleração local, pois indi∂t ∂t ∂t cam a variação da velocidade num certo ponto, somente com o tempo. As equações 3.18 mostram que as partículas do fluido podem apresentar aceleração mesmo quando a velocidade é constante em cada ponto com o tempo, pois pode-se ter variações de ponto para ponto, conforme pode ser constatado pelas equações 3.17. Somente se a velocidade for a mesma em todos os pontos, em qualquer instante, a aceleração será nula. Esse fato é muito importante no desenvolvimento da equação da quantidade de movimento, que veremos no Capítulo 5. Num escoamento no plano Oxy, o campo de velocidades é dado por vx = 2xt e vy = y2t. Determinar a aceleração na origem e no ponto P ≡ (1,2) no instante t = 5 s (medidas em cm). Solução O movimento é variado, pois vx e vy são funções do tempo.

ax = ∂vx ∂t + vx ∂vx ∂x + vy ∂vx ∂y + vz ∂vx ∂z ax = 2x + 2xt (2t) + y2 t(0) = 2x + 4xt2 ay = ∂vy ∂t + vx ∂vy ∂x + vy ∂vy ∂y + vz ∂vy ∂z ay= y2 + 2xt(0) + y2t(2yt) = y2 + 2y3t2 No instante t = 5 s ax = 2x + 4x (25) = 102x ay= y2 + 2y3 (25) = y2 + 50y3 No ponto P ≡ (1,2) Logo:

ax = 102 × 1 = 102 ay= (2)2 + 50 (2)3 = 4 + 400 = 404 r r r a (P, t) = 102e x + 404e y |ar|= (102 )2 + (404)2 = 416 cm s 2 3.1 No escoamento laminar de um fluido em condutos circulares, o diagrama de velocidades é representado pela equação v = ⎡ vmax ⎢1 ⎢⎣ – ⎝⎜⎛ r R ⎠⎞⎟ 2⎤ ⎥ ⎥⎦ , onde vmax é a velocidade no eixo do conduto, R é o raio do conduto e r é um raio genérico para o qual a velocidade v é genérica. Verificar que vm/vmax = 0,5, onde vm = velocidade média na seção. 3.2 No escoamento turbulento de um fluido em condutos circulares, o diagrama de velocidades é dado pela equação v = vmax ⎛⎝⎜1 – r R ⎞⎠⎟ 1 /7 , onde todas as grandezas têm o mesmo significado do Exercício 3.1. Verificar que vm/vmax = 49/60.

<!-- p. 79 -->
C a p í t u l o 3 z Cinemática dos fluidos z 79 3.3 Um gás (γ = 5 N/m3) escoa em regime permanente com uma vazão de 5 kg/s pela seção A de um conduto retangular de seção constante de 0,5 m por 1 m. Em uma seção B, o peso específico do gás é 10 N/m3. Qual será a velocidade média do escoamento nas seções A e B? (g = 10 m/s2) Resp.: vA = 20 m/s; vB = 10 m/s 3.4 Uma torneira enche de água um tanque, cuja capacidade é 6.000 L, em 1 h e 40 min. Determinar a vazão em volume, em massa e em peso em unidade do SI se ρH2O = 1.000 kg/ m 3 e g = 10 m/s2. Resp.: Q = 10–3 m3/s; Qm = 1 kg/s; QG = 10 N/s 3.5 No tubo da figura, determinar a vazão em volume, em massa, em peso e a velocidade média na seção (2), sabendo que o fluido é água e que A1 = 10 cm2 e A2 = 5 cm2. (ρH2O = 1.000 kg/ m 3, g = 10 m/s2) Resp.: Q = 1 L/s; Qm = 1 kg/s; QG = 10 N/s; v2 = 2 m/s. 3.6 O ar escoa num tubo convergente. A área da maior seção do tubo é 20 cm2 e a da menor é 10 cm2. A massa específica do ar na seção (1) é 1,2 kg/m3, enquanto na seção (2) é 0,9 kg/m3. Sendo a velocidade na seção (1) 10 m/s, determinar as vazões em massa, volume, em peso e a velocidade média na seção (2). Resp.: v2 = 26,7 m/s; Qm = 2,4 × 10–2 kg/s; Q1 = 0,02 m3/s; Q2 = 0,0267 m3/s; QG = 0,24 N/s 3.7 Um tubo admite água (ρ = 1.000 kg/m3) num reservatório com uma vazão de 20 L/s. No mesmo reservatório é trazido óleo (ρ = 800 kg/m3) por outro tubo com uma vazão de 10 L/s. A mistura homogênea formada é descarregada por um tubo cuja seção tem uma área de 30 cm2. Determinar a massa específica da mistura no tubo de descarga e sua velocidade. Resp.: ρ3 = 933 kg/m3; v3 = 10 m/s 3.8 Água é descarregada de um tanque cúbico de 5 m de aresta por um tubo de 5 cm de diâmetro. A vazão no tubo é 10 L/s. Determinar a velocidade de descida da superfície livre da água do tanque e, supondo desprezível a variação da vazão, determinar quanto tempo o nível da água levará para descer 20 cm. Resp. v = 4 × 10–4 m/s; t = 500 s

<!-- p. 80 -->
3.9 Os reservatórios da figura são cúbicos. São enchidos pelos tubos, respectivamente, em 100 s e 500 s. Determinar a velocidade da água na seção (A), sabendo que o diâmetro do conduto nessa seção é 1 m. Resp.: vA = 4,14 m/s 3.10 A água escoa por um conduto que possui dois ramais em derivação. O diâmetro do conduto principal é 15 cm e os das derivações são 2,5 cm e 5 cm, respectivamente. O perfil das velocidades no conduto principal é dado por: v= v max 1 ⎡ ⎢1 – ⎣⎢ ⎜⎛ r ⎟⎞ 2 ⎤ ⎥ e ⎝ R1 ⎠ ⎦⎥ nas derivações por: v= v max 2,3 ⎛⎜1 – ⎝ 1 /7 r ⎞⎟ R2,3 ⎠ Sraeiovmdaxa1 = 0,02 m seção Ai)

/ s e v max2 = 0,13 m /s, determinar a velocidade média no tubo de 5 cm de diâmetro. (Ri = Resp.: v3 = 0,064 m/s 3.11 O filtro de admissão de combustível de uma certa máquina é formado por um elemento poroso com forma de tronco de cone. O combustível líquido penetra no filtro com uma vazão de 10 L/s. A distribuição de velocidades na face superior é linear com vmax = 0,3 m/s. Qual é a vazão de combustível que será filtrada pela parede porosa? Resp.: 8,8 L/s

<!-- p. 81 -->
3.12 O tanque maior da figura abaixo permanece em nível constante. O escoamento na calha tem uma seção transversal quadrada e é bidimensional, obedecendo à equação v = 3y2. Sabendo que o tanque (B) tem 1 m3 e é totalmente preenchido em 5 segundos e que o conduto circular tem 30 cm de diâmetro, determinar: a) a velocidade média na calha quadrada; b) a vazão no conduto circular de 30 cm de diâmetro; c) a velocidade máxima na seção do conduto circular de 30 cm de diâmetro. Resp.: a) 1 m/s; b) 0,8 m3/s; c) 13,86 m/s 3.13 O insuflador de ar da figura a seguir gera 16.200 m3/h na seção (0) com uma velocidade média de 9,23 eem(t/22 s)=.dF9e7ovoraaCms.eArm1de0md5 ieidtsianasdbaeosnctdeoommqpoueiermadtpuiâormsaisçenãtroaosdDsoe2çp=õreo8s0je(ct0om),d,(1oν)asrei=s(t28e)×m, sae1n0qd–u5oem, or2e/snsúpemeqceutirevoaadmpeerRensetseyã,not0ot=ledm1s7nvoaaCsr;isate1çç=ãõo4ed7soe(1sC-) prezível no sistema, determinar: a) o diâmetro da seção (1); b) as vazões em volume em (1) e (2); c) as vazões em massa em (1) e (2).

Resp. 3.14 a) 0,099 m; b) Q1 = 0,624 m3/s; Q2 = 5,021 m3/s; c) Qm1 = 0,68 kg/s; Qm2 = 4,73 kg/s O esquema a seguir corresponde à seção longitudinal de um canal de 25 cm de largura. Admitindo escoamento bidimensional e sendo o diagrama de velocidades dado por v = 30y – y2 (y em cm; v em cm/s), bem como o fluido de peso específico: 0,9 N/L e viscosidade cinemática: 70 cSt e g = 10 m/s2, determinar: a) o gradiente de velocidade para y = 2 cm; b) a máxima tensão de cisalhamento na seção (N/m2); c) a velocidade média na seção em cm/s; d) a vazão em massa na seção.

<!-- p. 82 -->
Resp.: a) 26 s–2; b) 0,189 N/m2; c) 66,7 cm/s; d) 0,75 kg/s 3.15 No sistema da figura, tem-se um único fluido incompressível de ν = 10–4 m2/s e ρ = 1.000 kg/m3. a) Qual é o número de Re nas seções (1) e (4)? b) Qual é a velocidade média na seção (2) (m/s)? c) Qual é a vazão em volume nas seções (1) e (4) (L/s)? d) Qual é a vazão em volume na derivação e qual o sentido do escoamento? (Indicar no desenho.) e) Qual é a vazão em peso na seção (0)? f) Qual é a velocidade a 1 cm de distância da parede do tubo (4)? g) Qual é a tensão de cisalhamento na parede do conduto da seção (2)? Resp.: a) e) Re1 QG 0 = = 3.430; Re4 199 N/s; f)

= v 2.000; = 5,12 b) vm2 = m/s; g)

τ5=m6/6s,;7cN) Q/m1 =2 18,9 L/s; Q4 = 7,8 L/s; d) Qder = 38,8 L/s; 3.16 A placa da figura tem uma área de 2 m2 e espessura desprezível. Entre a placa e o solo existe um fluido que escoa formando sidade dinâmica do um diagrama de velocidades bidimensional dado por fluido é 10–2 N.s/m2 e a velocidade máxima é 2 m/s. v = 20y vmax (1 – 5y). A viscoa) Qual é o gradiente de velocidade junto ao solo? b) Qual é a força necessária para manter a placa em equilíbrio estático? c) Qual é a velocidade média? d) Fora do contato da placa, o diagrama de velocidades é considerado linear bidimensional. Qual é a velocidade máxima?

<!-- p. 83 -->
Resp.: a) –40 s–1; b) 0,8 N; c) 1,33 m/s; d) 2,66 m/s 3.17 Um propulsor a jato queima 1 kg/s de combustível quando o avião voa à velocidade de 200 m/s. Sendo dados ρar = 1,2 kg/m3, ρg = 0,5 kg/m3 (na seção 2), A1 = 0,3 m2 e A2 = 0,2 m2, determinar a velocidade dos gases (vg ) na seção de saída. Resp.: 730 m/s 3.18 No sistema da figura, A3 = 0,5 m2, ρ3 = 0,4 kg/m3 e os fluidos são gases. Dados: Seção (1): v = 4[1 – (r/R)2]; Q1 = 2 m3/s; ρ1 = 0,6 kg/m3 Seção (2): v = 9(1 – r/0,4); ρ2 = 1,2 kg/m3 Determinar:

a) a velocidade do pistão; b) o raio da seção (1); c) a mínima viscosidade dinâmica do fluido na seção (1).

Resp.: a) 15 m/s; b) 0,564 m; c) 6,77 × 10–4 N.s/m2 3.19 No sistema da figura, o óleo fornecido pela bomba mantém o pistão parado. O óleo escoa através da folga entre o pistão e o cilindro com uma distribuição linear de velocidades, tendo a máxima velocidade na linha de centro da seção de escoamento. Calcular a vazão de óleo que deve ser fornecida pela bomba adotando a área da coroa circular igual a π D ε.

<!-- p. 84 -->
Dados: Pressão na base do pistão = 50 kPa L = 2 m; D = 20 cm; peso do pistão = 520π N μ = 5 × 10–3 N.s /m2; ε = 1 mm Resp.: Q = 1,57 L/s 3.20 O campo de velocidades de um escoamento é dado por vx = 3y e vy = 2. a) O movimento é variado ou permanente? b) Determinar o campo das acelerações.

c) Determinar os módulos da velocidade e aceleração no ponto de coordenadas (3;4). Resp.: b) ax = 6; ay = 0 c) v = 12,2; a = 6 3.21 Exercício anterior com vx = 0, vy = 3xy e ponto de coordenadas (2;2).

Resp.: b) ax = 0; a y = 9x2y c) v = 12; a = 72 3.22 Exercício anterior com vx = –2y, vy = 3x e ponto de coordenadas (2;3).

Resp.: a x = –6x; a y = –6y c) v = 8,5; a = 21,6 3.23 Um escoamento é definido pelo campo de velocidades vx = 2(1 + t), vy = 3(1+ t), vz = 4(1 + t). Qual é o módulo da velocidade no ponto (3;1;4) no instante t = 2 s? Qual é o módulo da aceleração no mesmo ponto e instante? Resp.: v = 16,1; a = 5,4 3.24 O campo de velocidades de um escoamento bidimensional é dado por vx = 3 + 2xy + 4t2, vy = xy2 + 3t. Determinar os módulos da velocidade e aceleração no ponto (2;1) no instante t = 5 s. Resp.: v = 108; a = 368

<!-- p. 85 -->

# Capítulo 4 — Equação da energia para regime permanente

## 4.1 Introdução

No Capítulo 3 foi introduzida a equação da continuidade. Essa equação conclui que, para que a hipótese de regime permanente seja verdadeira, a massa de fluido que flui por uma seção de um tubo de corrente deve ser idêntica àquela que o abandona por outra seção qualquer. Pode-se, então, fazer um balanço das massas ou vazões em massa entre seções de entrada ou saída de um certo escoamento. Com base no fato de que a energia não pode ser criada nem destruída, mas apenas transformada, é possível construir uma equação que permitirá fazer o balanço das energias, da mesma forma como foi feito para as massas, por meio da equação da continuidade. A equação que permite tal balanço chama-se equação da energia e nos permitirá, associada à equação da continuidade, resolver inúmeros problemas práticos como, por exemplo: determinação da potência de máquinas hidráulicas, determinação de perdas em escoamento, transformação de energia etc. Essa equação envolve, em geral, uma série de conceitos novos, e os estudantes de Mecânica dos Fluidos costumam ter certa dificuldade para sua assimilação. Por causa disso, neste capítulo será realizada uma inversão que poderá parecer conceitualmente estranha para o conhecedor do assunto, mas que é didaticamente válida. Tal inversão constará da apresentação inicial de um caso particularíssimo que será estendido, aos poucos, para o caso geral em regime permanente. Essa operação visa a uma familiarização dos leitores com alguns dos termos que ficarão posteriormente diluídos e, portanto, de difícil compreensão dentro da equação geral.

## 4.2 Tipos de energias mecânicas associadas a um fluido

a) Energia potencial (E p ) É o estado de energia do sistema devido à sua posição no campo da gravidade em relação a um plano horizontal de referência (PHR). Essa energia é medida pelo potencial de realização de trabalho do sistema. Seja, por exemplo, um sistema de peso G = mg, cujo centro de gravidade está a uma cota z em relação a um PHR (Figura 4.1).

<!-- p. 86 -->
Figura 4.1 Como: Trabalho = Força × Deslocamento Então: W = Gz = mgz Mas, pelo que foi dito anteriormente, E p = W; logo: E p = mgz (4.1)

Note-se que, na equação, que será introduzida posteriormente, interessará somente a diferença das energias potenciais de um ponto a outro do fluido, de forma que a posição do PHR não alterará a solução dos problemas. Isto é, o PHR é adotado arbitrariamente, conforme a conveniência da solução do problema. b) Energia cinética (E c ) É o estado de energia determinado pelo movimento do fluido. Seja um sistema de massa m e velocidade v; a energia cinética será dada por: mv 2 Ec = 2 (4.2) Figura 4.2 c) Energia de pressão (E pr ) Essa energia corresponde ao trabalho potencial das forças de pressão que atuam no escoamento do fluido. Seja, por exemplo, o tubo de corrente da Figura 4.3. Admitindo que a pressão seja uniforme na seção, então a força aplicada pelo fluido externo no fluido do tubo de corrente, na interface de área A, será F = pA. No intervalo de tempo dt, o fluido irá se deslocar de um ds, sob a ação da força F, produzindo um trabalho: dW = Fds = pAds = pdV Por definição: e portanto:

dW = dE pr dE pr = pdV Figura 4.3 (4.3)

<!-- p. 87 -->
ou ∫ E pr = pdV V d) Energia mecânica total do fluido (E) Excluindo-se energias térmicas e levando em conta apenas efeitos mecânicos, a energia total de um sistema de fluido será: E = E p + E c + E pr ou ∫ mv 2 E = mgz + + pdV 2V (4.4) (4.5)

## 4.3 Equação de Bernoulli

Conforme foi citado na introdução, a equação da energia geral será construída aos poucos, partindo-se de uma equação mais simples, válida somente para uma série de hipóteses simplificadoras. É óbvio que cada hipótese admitida cria um afastamento entre os resultados obtidos pela equação e os observados na prática. A equação de Bernoulli, devido ao grande número de hipóteses simplificadoras, dificilmente poderá produzir resultados compatíveis com a realidade. No entanto, é de importância fundamental, seja conceitualmente, seja como alicerce da equação geral, que será construída pela eliminação gradual das hipóteses da equação de Bernoulli e pela introdução dos termos necessários, para que a equação represente com exatidão os fenômenos naturais. As hipóteses simplificadoras são:

a) regime permanente; b) sem máquina no trecho de escoamento em estudo. Entenda-se por máquina qualquer dispositivo mecânico que forneça ou retire energia do fluido, na forma de trabalho. As que fornecem energia ao fluido serão denominadas ‘bombas’ e as que extraem energia do fluido, ‘turbinas’; c) sem perdas por atrito no escoamento do fluido ou fluido ideal; d) propriedades uniformes nas seções; e) fluido incompressível; f) sem trocas de calor. Pelas hipóteses (b), (c) e (f) exclui-se que no trecho de escoamento em estudo seja fornecida ou retirada energia do fluido. Seja o tubo de corrente da Figura 4.4, entre as seções (1) e (2).

Figura 4.4 Deixando passar um intervalo de tempo dt, uma massa infinitesimal dm1 de fluido a montante da seção (1) atravessa-a e penetra no trecho (1)-(2) acrescentando-lhe a energia:

<!-- p. 88 -->
dE 1 = dm1 gz 1 + dm1 v 2 1 2 + p 1 dV1 Na seção (2), uma massa dm2 do fluido que pertencia ao trecho (1)-(2) escoa para fora, levando a sua energia: dE 2 = dm2 gz 2 + dm 2 v 2 2 2 + p 2dV2 Como pelas hipóteses (b), (c) e (f) não se fornece nem se retira energia do fluido, para que o regime seja permanente é necessário que no trecho (1)-(2) não haja variação de energia, o que implica obrigatoriamente que: dE1 = dE 2 ou dm 1 gz1 + dm 1 v12 2 + p1 dV1 = dm 2 gz 2 + dm 2 v 2 2 2 + p 2 dV2 Como ρ = dm dV e portanto dV = dm ρ, tem-se: dm 1 gz1 + dm 1 v12 2 + p1 ρ1 dm 1 = dm 2 gz 2 + dm 2 v 2 2 2 + p2 ρ2 dm 2 Como o fluido é incompressível, ρ1 = ρ2 e, como o regime é permanente, dm1 = dm2, portanto: gz 1 + v12 2 + p1 ρ = gz 2 + v 2 2 2 + p2 ρ Dividindo a equação por g e lembrando que γ = ρg, tem-se:

z1 + v12 2g + p1 γ = z2 + v 2 2 2g + p2 γ (4.6)

A Equação 4.6 é a equação de Bernoulli, que permite relacionar cotas, velocidades e pressões entre duas seções do escoamento do fluido. A seguir, será indicado o significado dos termos dessa equação. z = mgz = E p = energia potencial por unidade de peso ou energia potencial de uma mg G partícula de peso unitário v 2 = mv 2 = mv 2 = E c = energia cinética por unidade de peso ou energia cinética de 2g 2gm 2G G uma partícula de peso unitário p γ = pV γV = pV G = E pr G = energia de pressão por unidade de peso ou energia de pressão da partícula de peso unitário Note-se, então, que a Equação 4.6 expressa que ao penetrar por (1) uma partícula de peso unitário, à qual estão associadas as energias z1, v 2 1 /2g e p1/γ , deverá sair por (2) uma partícula de peso unitário à qual estejam associadas as energias z2, v 2 2 /2g e p2/γ, de forma que a soma delas seja idêntica à soma em (1) para manter a energia constante no volume entre (1) e (2).

<!-- p. 89 -->
Uma observação importante é que, sendo z uma cota, então será medida em unidade de comprimento (por exemplo, em metros); logo, tanto v2/2g como p/γ também serão medidos dessa forma. Não deve o leitor esquecer que, apesar disso, cada uma das parcelas da Equação 4.6 tem o significado de energia por unidade de peso. Note-se ainda que no item 2.5 do Capítulo 2 a carga de pressão foi definida como sendo h = p/γ. Logo, a energia de pressão por unidade de peso é a própria carga de pressão. Por analogia, serão denominadas: z = carga potencial v2 = carga da velocidade ou carga cinética 2g Observe-se que a palavra ‘carga’ substitui a expressão ‘energia por unidade de peso’. Fazendo: p v2 H= + +z γ 2g onde: H = energia total por unidade de peso numa seção ou carga total na seção. Com a noção de carga total, a Equação 4.6 poderá ser escrita simbolicamente: H1 = H2 (4.7)

Essa equação poderá ser enunciada da seguinte forma: Se, entre duas seções do escoamento, o fluido for incompressível, sem atritos, e o regime permanente, se não houver máquina nem trocas de calor, então as cargas totais se manterão constantes em qualquer seção, não havendo nem ganhos nem perdas de carga. Água escoa em regime permanente no Venturi da figura. No trecho considerado, supõem-se as perdas por atrito desprezíveis e as propriedades uniformes nas seções. A área (1) é 20 cm2, enquanto a da garganta (2) é 10 cm2. Um manômetro cujo fluido manométrico é mercúrio (γ Hg = 136.000 N/m 3) é ligado entre as seções (1) e (2) e indica o desnível mostrado na figura. Pede-se a vazão da água que escoa pelo Venturi. (γ H2O = 10.000 N/m 3) Solução Note-se que as hipóteses impostas pelo problema o enquadram perfeitamente no uso da equação de Bernoulli. Logo: p1 γ + v 2 1 2g + z1 = p2 γ + v 2 2 2g + z2

<!-- p. 90 -->
Os centros geométricos das seções (1) e (2) têm a mesma cota z, qualquer que seja o PHR adotado. Dessa forma, pode-se escrever: v 2 2 – v 21 = p1 – p2 2g γ O segundo membro dessa expressão pode ser determinado pelo manômetro diferencial instalado, mas antes disso é interessante notar que, pela equação da continuidade, sendo A2 < A1, tem-se v2 > v1, e como a energia cinética aumenta de (1) para (2), a energia de pressão deverá diminuir para que a soma seja constante. Essa observação explica o porquê de o manômetro estar desnivelado da esquerda para a direita, já que p1 > p2. Partindo do centro geométrico da seção (1) e desprezando os trechos comuns aos dois ramos do manômetro, a equação manométrica ficará: Logo: ou p1 + γ H2Oh – γ Hg h = p2 p1 – p2 = ( γ Hg – γ H2O )h p1 – p2 = (136.000 – 10.000) × 0,1 = 12.600 N/m 2 v22 – v21 = 12.600 = 12.600 = 1,26 m 2g γ 10.000 Ou, adotando g = 10 m/s2, v22 – v12 = 25,20 m 2/s2 Como a equação da energia conduz a uma equação com duas incógnitas, haverá necessidade de outra equação que relacione as velocidades, que é a equação da continuidade. Pela equação da continuidade: ou Logo:

Q1 = Q2 v1A1 = v2A2 ∴ v1 = v2 A2 A1 = v2 2 v22 – v22 4 = 25,20 ou Logo: ou v2 = 4 × 25,20 = 5,8 m/s 3 Q = v2A2 = 5,8 × 10 × 10–4 = 5,8 × 10–3 m3/s Q = 5,8 L/s Note-se que o problema foi resolvido com o auxílio da equação da energia (Bernoulli) e da equação da continuidade. Tal fato acontecerá em quase todos os problemas, devendo, portanto, o leitor estar bastante familiarizado com os capítulos 3 e 4 para que não tenha dificuldades na seqüência do estudo.

## 4.4 Equação da energia e presença de uma máquina

Como foi explicado na Introdução (item 4.1), a equação do item 4.3 será completada gradualmente, eliminando as hipóteses impostas para se chegar à equação geral. Em outras palavras, neste item e nos próximos, serão retiradas aos poucos as hipóteses impostas no item 4.3 que restringem o uso da equação. Neste item 4.4 serão mantidas todas as hipóteses do item 4.3, mas raciocina-se com a presença de uma máquina atuando entre as seções (1) e (2) do tubo de corrente. Máquina, para efeito deste estudo, será qualquer dispositivo introduzido no escoamento, o qual forneça ou retire energia dele, na forma de trabalho. A maneira de funcionamento da máquina não interessará por enquanto, importando somente como sua presença afeta as equações 4.6 ou 4.7.

<!-- p. 91 -->
Como, por enquanto, subsiste a hipótese de fluido incompressível, para facilidade de linguagem, será denominada ‘bomba’ qualquer máquina que forneça energia ao fluido e ‘turbina’, qualquer máquina que retire energia dele. Vejamos a alteração na equação do item 4.3 ao introduzir uma máquina entre as seções (1) e (2) (Figura 4.5). Figura 4.5 Se não houvesse máquina, sabe-se que, válidas as hipóteses do item 4.3, valeria a Equação 4.7 H1 = H 2 isto é, a energia por unidade de peso do fluido em (1) é igual à energia por unidade de peso em (2) ou a carga total em (1) é igual à carga total em (2). Se a máquina for uma bomba, o fluido receberá um acréscimo de energia tal que H2 > H1. Para restabelecer a igualdade, deverá ser somada ao primeiro membro a energia recebida pela unidade de peso do fluido na máquina. Logo: H1 + HB = H2 (4.8)

A parcela HB é chamada ‘carga ou altura manométrica da bomba’ e representa a energia fornecida à unidade de peso do fluido que passa pela bomba. Se a máquina for uma turbina, H1 > H2, pois, por definição, a turbina retira energia do fluido. Para restabelecer a igualdade, tem-se: H1 – HT = H2 (4.9)

onde HT = ‘carga ou altura manométrica da turbina’ ou energia retirada da unidade de peso do fluido pela turbina. Como se deseja estabelecer uma equação geral, a carga manométrica da máquina será indicada por HM e as equações 4.8 e 4.9 poderão ser escritas de forma única como: H1 + HM = H2 (4.10)

sendo: HM = HB se a máquina for uma bomba; HM = –HT se a máquina for uma turbina.

A Equação 4.10 é a que considera a presença de uma máquina no escoamento entre as seções (1) e (2) em estudo. Lembrando os significados de H1 e H2, essa equação é escrita assim: p1 γ + z1 + v12 2g +HM = p2 γ +z2 + v 2 2 2g (4.11) ou HM = p2 – p1 γ + (z 2 – z1 ) + v 2 2 – v12 2g (4.12) A Equação 4.12 mostra que a presença de uma máquina pode acarretar variações da carga de pressão, da carga potencial e da carga cinética.

<!-- p. 92 -->
## 4.5 Potência da máquina e noção de rendimento

Antes de definir a potência da máquina, será definida a ‘potência do fluido’.

Note-se que potência, por definição, é o trabalho por unidade de tempo.

Como o trabalho é uma energia mecânica, podemos generalizar definindo potência como sendo qualquer energia mecânica por unidade de tempo e, daqui para a frente, será representado pelo símbolo N.

Dessa forma:

N = energia mecânica tempo ou equivalentemente:

N = energia mecânica × peso peso tempo A energia por unidade de peso já foi definida anteriormente e foi denominada ‘carga’, e o peso por unidade de tempo é a vazão em peso.

Dessa forma: Pela Equação 3.10:

N = carga × QG N = γ Q × carga Pela Equação 4.13, observa-se que, para calcular a potência referente ao fluido, deve-se multiplicar o peso específico dele pela vazão em volume e pela sua energia por unidade de peso ou carga. Logo: N=γQH (4.13)

Calcular a potência do jato de um fluido descarregado no ambiente por um bocal. Dados: vj = velocidade do jato; Aj = área do jato; γ = peso específico do fluido. Solução A carga ou a energia do jato por unidade de peso é dada por:

H j = pj γ + v 2 j 2g + z j Passando o PHR no centro do bocal, zj = 0. Como o jato é descarregado à pressão atmosférica, sua pressão efetiva será nula, isto é, pj = 0. Logo: H j = v 2 j 2g o que significa que o jato só tem carga cinética.

Pela Equação 4.13: ou Nj = γ Qj Hj N j = γv jA j v 2 j 2g Logo: N j = γA jv 3 j 2g ou N j = ρA jv 2 3 j

<!-- p. 93 -->
No caso da presença de uma máquina, verificou-se que a energia fornecida ou retirada do fluido, por unidade de peso, é indicada por HM (carga manométrica). Logo, nesse caso, a potência referente ao fluido será dada por: N = γ QHM ou, no caso de uma bomba:

N = γ QHB (4.14)

e no caso de uma turbina:

N = γ QHT (4.15)

Note-se que, no caso da transmissão de potência, sempre existem perdas e, portanto, a potência recebida ou cedida pelo fluido não coincide com a potência da máquina, que é definida como sendo a potência no seu eixo.

A potência de uma bomba será indicada por NB e é ilustrada esquematicamente na Figura 4.6. A potência NB, no caso do desenho, coincidiria com a potência do motor, mas nem sempre o motor é ligado diretamente ao eixo, podendo existir algum elemento de transmissão que provoque perdas.

Figura 4.6 Pelo que foi dito anteriormente, N < NB devido às perdas na transmissão da potência ao fluido, que se devem principalmente a atritos, mas que aqui não serão analisadas. Define-se rendimento de uma bomba (ηB) como a relação entre a potência recebida pelo fluido e a fornecida pelo eixo. Logo: ηB = N NB NB = N ηB = γ Q HB ηB (4.16) (4.17)

O caso da turbina é ilustrado pela Figura 4.7.

Figura 4.7 Observe-se que, nesse caso, o fluxo de energia é do fluido para a turbina e, portanto, NT < N.

<!-- p. 94 -->
Define-se rendimento de uma turbina (ηT) como a relação entre a potência da turbina e a potência cedida pelo fluido:

ηT = NT N Logo:

N T = Nη T = γ Q H T η T (4.18)

As unidades de potência são dadas por unidade de trabalho por unidade de tempo.

SI:

N.m/s = J/s = W (watt)

1 kgm/s = 9,8 W MK*S: kgf.m/s = kgm/s Outras unidades são o CV (cavalo-vapor) e o HP (horse power).

1 CV = 75 kgm/s = 735 W 1 HP = 1,014 CV O reservatório de grandes dimensões da figura fornece água para o tanque indicado com uma vazão de 10 L/s. Verificar se a máquina instalada é bomba ou turbina e determinar sua potência, se o rendimento é 75%. Supor fluido ideal. Dados: γ H2O = 104 N/m 3; Atubos = 10 cm2; g = 10 m/s2. Solução Como o fluido é considerado ideal, pode-se aplicar a equação de Bernoulli entre as seções (1) e (2), lembrando que entre as duas existe a máquina M. Mesmo que o reservatório da esquerda não seja a nível constante, será adotada a hipótese de regime permanente com a seguinte consideração: o reservatório, sendo de grandes dimensões, levará muito tempo para que seu nível seja alterado sensivelmente pela água descarregada por (2). Logo, dentro de um certo intervalo de tempo, pode-se considerar que o seu nível é constante, mantendo dessa forma a hipótese de regime permanente. Lembre o leitor que, todas as vezes que se mencionar ‘reservatório de grandes dimensões’, essa hipótese é válida e, mais que isso, pode-se considerar a velocidade do fluido no nível do reservatório praticamente nula (vide Exercício 3.8 do Capítulo 3). Com essas considerações, pode-se escrever: H1 + HM = H2 H1 = p1 γ + v 2 1 2g + z1 H2 = p2 γ + v 2 2 2g + z2 Adotando o PHR na base do reservatório (1), tem-se:

z1 = 20 m e z2 = 5 m A pressão, tanto na seção (1) como na (2), é igual à pressão atmosférica; logo, p1 = 0 e p2 = 0 na escala efetiva.

<!-- p. 95 -->
A velocidade na seção (1) é nula pelas considerações feitas ou v1 = 0.

Resta determinar v2.

Mas v2 = Q A2 = 10 × 10 × 10–3 10–4 = 10 m s H1 = 0 + 0 + 20 = 20 m H 2 = 0 + 2 10 × 2 10 + 5 = 10 m Logo:

HM = H2 – H1 = 10 – 20 = –10 m Como no sentido do escoamento HM é negativo, conclui-se que a máquina é uma turbina, e como HM = –HT , então HT = 10 m. Potência fornecida pelo fluido à turbina:

N = γQHT = 104 × 10 × 10–3 × 10 × 1 = 1 kW 1.000 Potência da turbina com a noção de rendimento:

ηT = NT N logo: NT = NηT = 1× 0,75 = 0,75 kW Observe que, pela equação de Bernoulli, calcula-se a potência posta em jogo pelo fluido. A potência realmente aproveitada pela turbina é menor, como se pode verificar pelo resultado.

## 4.6 Equação da energia para fluido real

Neste item será retirada a hipótese de fluido ideal; logo, serão considerados os atritos internos no escoamento do fluido. São mantidas as hipóteses de regime permanente, fluido incompressível, propriedades uniformes na seção e sem trocas de calor induzidas. Esta última significa que não existe uma troca de calor provocada propositalmente; no entanto, ao se considerar os atritos no escoamento do fluido, deve-se imaginar que haverá uma perda de calor do fluido para o ambiente causada pelos próprios atritos. Como será visto a seguir, a construção da equação da energia pode ser realizada sem se falar, explicitamente, dessa perda de calor. Da equação de Bernoulli sabe-se que, se o fluido fosse perfeito, H1 = H2 (Figura 4.8). Figura 4.8 Se, no entanto, houver atritos no transporte do fluido, entre as seções (1) e (2) haverá uma dissipação da energia, de forma que H1 > H2. Querendo restabelecer a igualdade, será necessário somar no segundo membro a energia dissipada no transporte.

H1 = H2 + H p1,2 H p1,2 = energia perdida entre (1) e (2) por unidade de peso do fluido (4.19)

<!-- p. 96 -->
Como Hp1,2 = H1 – H2 e como H1 e H2 são chamados cargas totais, Hp1,2 é denominado ‘perda de carga’. Se for considerada também a presença de uma máquina entre (1) e (2), a equação da energia ficará:

H1 + H M = H 2 + H p1,2 (4.20) ou v 2 1 2g + p1 γ +z1 +HM = v 2 2 2g + p2 γ +z2 + H p1,2 (4.21)

Da Equação 4.19 deve-se notar que, no escoamento de um fluido real entre duas seções onde não existe máquina, a energia é sempre decrescente no sentido do escoamento, isto é, a carga total a montante é sempre maior que a de jusante, desde que não haja máquina entre as duas. A potência dissipada pelos atritos é facilmente calculável raciocinando da mesma maneira que para o cálculo da potência do fluido. A potência dissipada ou perdida por atrito poderá ser calculada por: N diss = γ QH p1,2 1) Na instalação da figura, verificar se a máquina é uma bomba ou uma turbina e determinar sua potência, sabendo que seu rendimento é 75%. Sabe-se que a pressão indicada por um manômetro instalado na seção (2) é 0,16 MPa, a vazão é 10 L/s, a área da seção dos tubos é 10 cm2 e a perda de carga entre as seções (1) e (4) é 2 m. Não é dado o sentido do escoamento. γ H2O = 104 N / m3; g = 10 m/s2.

Solução Deve ser notado, inicialmente, que a seção (4) é o nível do reservatório inferior sem incluir a parte interna do tubo, já que nesta não se conhece a pressão. Sabe-se que o escoamento acontecerá no sentido das cargas decrescentes, num trecho onde não existe máquina. Para verificar o sentido, serão calculadas as cargas nas seções (1) e (2). H1 = p1 γ + v 2 1 2g + z1 = 0 + 0+ 24 = 24 m H2 = p2 γ + v 2 2 2g + z2 v2 = Q A2 = 10 × 10 × 10–3 10–4 = 10 m s H2 = 0,16 × 106 104 + 102 2 × 10 + 4 = 25 m

<!-- p. 97 -->
Como H2 > H1, conclui-se que o escoamento terá o sentido de (2) para (1) ou de baixo para cima, sendo a máquina, obviamente, uma bomba. Aplique-se agora a equação da energia entre as seções (4) e (1), que compreendem a bomba. Lembrar que a equação deve ser escrita no sentido do escoamento. H4 + HB = H1 + Hp4,1 H4 = p4 γ + v 2 4 2g + z4 = 0 H1 = 24 m (já calculado)

Hp1,4 = 2 m Logo:

HB = H1 – H4 + Hp1,4 = 24 – 0 + 2 = 26 m > 0 Confirma-se que a máquina é uma bomba, já que a carga manométrica resultou positiva. NB = γ QHB ηB = 104 × 10 × 10–3 × 0,75 26 × 1 = 3,47 kW 1.000 2) Na instalação da figura, a máquina é uma bomba e o fluido é água. A bomba tem uma potência de 5 kW e seu rendimento é 80%. A água é descarregada à atmosfera com uma velocidade de 5 m/s pelo tubo cuja área da seção é 10 cm2. Determinar a perda de carga do fluido entre (1) e (2) e a potência dissipada ao longo da tubulação. γ = 104 N/m3; g = 10 m/s2. Solução Temos Com H1 + HB = H2 + Hp1,2 H1 = v 2 1 2g + p1 γ + z1 = 0 + 0+5 = 5 m H2 = v 2 2 2g + p2 γ + z2 = 2 52 × 10 + 0 + 0 = 1,25 m NB = γQHB ηB → HB = ηBNB γQ = ηBNB γvA HB = 104 0,8 × × 5× 5× 10 103 × 10–4 = 80 m Hp1,2 = H1 – H2 + HB = 5 – 1,25 + 80 Hp1,2 = 83,75 m Ndiss 1,2 = γQHp1,2 = 104 × 5× 10 × 10–4 × 83,75 × 1 = 4,19 kW 1.000

## 4.7 Diagrama de velocidades não-uniforme na seção

Até agora, uma das hipóteses impostas foi referente a escoamento uniforme; entretanto, devido ao princípio da aderência, o diagrama de velocidades não será uniforme na seção.

<!-- p. 98 -->
v2 Será verificado que esse fato causa uma alteração no termo da equação da energia, 2g que foi obtido com a hipótese de escoamento uniforme na seção.

Obviamente, se o diagrama de velocidades não for uniforme, existirá uma velocidade distinta em cada ponto da seção (Figura 4.9). O termo v 2 2g não terá mais significado, já que na seção em estudo existem infinitas velocidades diferentes. Figura 4.9 É possível utilizar a idéia de velocidade média na seção definida no Capítulo 3. Porém, será verificado a seguir que o termo da energia cinética, escrito com a velocidade média, necessitará de um coeficiente de correção. Para isso, ‘fluxo da energia cinética’ (C) será definido como sendo a energia cinética que atravessa uma seção do escoamento por unidade de tempo. Na Figura 4.9 será calculada a energia cinética que, no intervalo de tempo dt, atravessa um dA da seção de área A. dE c = dmv 2 2 Logo, o fluxo da energia cinética através do dA será: dmv 2 dC = 2dt Mas dm/dt é a vazão em massa através do dA. Logo:

e, portanto, ou dm dt = dQ m = ρdQ = ρvdA dC = ρvdA v 2 2 ρv 3 dC = dA 2 (4.22)

Para obter o fluxo da energia através de toda a área A, deve-se integrar a Equação 4.22: C = ∫ ρv 2 3 dA Adotando a velocidade média na seção e supondo ρ = cte em seus pontos, pode ser verificado que: ∫ C = ρv 3 dA ≠ ρv 3 m A 2 2

<!-- p. 99 -->
É necessário, portanto, que se introduza um coeficiente de correção para provocar a igualdade das expressões. Logo: ∫ C = ρv 3 dA = α ρv 3 m A 2 2 (4.23)

onde α, denominado ‘coeficiente da energia cinética’, é o fator que provoca a igualdade das duas expressões e pode ser determinado pela Equação 4.23: ∫ α = 2 ρv 3 m A ρv 3 dA 2 ou ∫ α = 1 A ⎛ v ⎞3 ⎝⎜ vm ⎟⎠ dA (4.24)

Tendo a definição de α, o fluxo da energia cinética pode ser escrito:

C = α ρv 3 m A 2 (4.25)

energia cinética Mas C = e o termo da equação da energia corresponde à energia cinética tempo por unidade de peso. Logo:

energia cinética energia cinética = energia cinética × tempo = peso peso tempo tempo peso tempo Lembrando que Peso Tempo = QG ou vazão em peso, obtém-se: energia cinética = C α ρv 3 m A =2 =α v 2 m peso QG ρgvm A 2g Logo, a Equação 4.21 deverá ser escrita:

α1 v 2 m 1 2g + p1 γ + z1 +HM =α2 v 2 m 2 2g + p2 γ +z2 + H p1,2 (4.26)

ou simplesmente:

α1 v12 2g + p1 γ + z1 +HM =α2 v 2 2 2g + p2 γ +z2 + H p1,2 (4.27)

lembrando que a presença de α implica que v1 e v2 são as velocidades médias nas seções (1) e (2) do escoamento. O coeficiente α é função somente do diagrama de velocidades e será tanto maior que a unidade quanto mais este último se afastar do diagrama uniforme.

<!-- p. 100 -->
Em tubos de seção circular, sendo o escoamento laminar, vale o diagrama v = v max ⎡ ⎢1– ⎣ ⎜⎛⎝ r R ⎠⎟⎞ 2 ⎤ ⎥ ⎦ e, nesse caso, α = 2, e se o escoamento for turbulento, v = v max ⎛⎝⎜1– r R ⎞⎟⎠ 1/ 7 , sendo a @ 1. Nessas condições, sempre que Re > 2.400, em tubos, pode-se adotar a equação da energia na forma apresentada na Equação 4.21, em vez da apresentada na Equação 4.27, já que α ≅ 1. Note-se que este é o caso mais comum na prática da engenharia. (Vide exercícios 4.23 e 4.24, associados aos exercícios 3.1 e 3.2, respectivamente.)

A Equação 4.27 é a equação válida, sem nenhuma restrição, quando o regime é permanente, o fluido é incompressível e sem trocas de calor ou fenômenos térmicos.

Trata-se, portanto, da equação de uso mais freqüente nas aplicações que envolvem fluidos incompressíveis, isto é, líquidos ou até gases, desde que a variação da massa específica ao longo do escoamento seja desprezível.

4.8 Equação da energia para diversas entradas e saídas e escoamento em regime permanente de um fluido incompressível, sem trocas de calor Ao longo de todo o capítulo, raciocinou-se com apenas uma entrada e uma saída ou tubo de corrente. Com a base dada, o próprio leitor poderia verificar as alterações na equação para um caso em que o número de entradas e saídas fosse maior. No entanto, será aqui determinada essa equação, de grande utilidade em muitos problemas. Mantidas as hipóteses da equação de Bernoulli (item 4.3), na Figura 4.10, a energia que penetra no sistema pelas entradas deve coincidir com a que o abandona pelas saídas no mesmo intervalo de tempo t, para que o regime seja permanente. E1e (1e) E1s (1s) (2e) E2e (2s) E2s Ene (ne) (ns) Ens Figura 4.10 Logo: onde: e = entradas ∑eE = ∑s E (4.28) s = saídas Dividindo a Equação 4.28 pelo intervalo de tempo em que as energias que entraram e saíram foram computadas, obtém-se ∑eE / t = ∑s E / t e lembrando que a energia do fluido por unidade de tempo representa a potência do fluido, teremos: ∑e N = ∑s N ou ∑e γQH = ∑s γQH (4.29)

<!-- p. 101 -->
onde H = αv 2 2g + p γ +z em cada seção.

No caso da presença de máquina e de perdas por atrito, teremos, pela Figura 4.11: N1e (1e) Ndiss (1s) N1s (2e) N2e M (2s) N2s Nne (ne) N (ns) Nns Figura 4.11 ∑ ∑ γQH + N = e s γQH + N diss (4.30)

onde N será positivo ou negativo, dependendo de a máquina ser bomba ou turbina, e N = γQHM, conforme foi visto anteriormente.

∑ N diss = γQH p (4.31)

onde, na somatória, Q e Hp referem-se a cada trecho do escoamento.

No sistema da figura, os reservatórios são de grandes dimensões. O reservatório X alimenta o sistema com 20 L/s e o reservatório Y é alimentado pelo sistema com 7,5 L/s. A potência da bomba é 2 kW e o seu rendimento, 80%. Todas as tubulações têm 62 mm de diâmetro Hp1,3 = 4 m. O fluido é água (γ = 104 N/m3). Pede-se: e as perdas de carga são: H p0,1 = 2 m; H p1,2 =1 m e a) a potência dissipada na instalação; b) a cota da seção (3) em relação ao centro da bomba.

Solução a) Pela equação da continuidade: ∑eQ = ∑s Q Logo:

Q0,1 = Q1,2 = Q1,3 20 = Q1,2 + 7,5 Q1,2 = 12,5 L / s Ndiss = γQ0,1Hp0,1 + γQ1,2Hp1,2 + γQ1,3Hp1,3 Hp1,3 N diss = 104 × (20 × 10–3 × 2 + 12,5 × 10–3 × 1+ 7,5 × 10–3 × 4)

1 103 = 0,825 kW

<!-- p. 102 -->
∑ ∑ b) γQH + N = e s γQH + Ndiss γQ0,1H0 + N = γQ1,2H2 + γQ1,3H3 + N diss H0 = α 0v20 2g + p0 γ + z0 onde: v0 = 0 p0 = 0 z0 = 2 m, adotando-se o PHR no nível da bomba.

Logo, H0 = 2 m.

H2 = α 2v22 2g + p2 γ + z2 onde z2 = 0, p2 = 0 v2 = 4Q2 πD2 = 4 × 12,5 × 10–3 π × 0,062 2 = 4,14 m/s e, supondo α2 = 1, H2 = 4,142 20 = 0,86 m H3 = α 3v23 2g + p3 γ + z3 onde: v3 = 0, p3 = 0, z3 = h N = NBηB = 2 × 0,8 = 1,6 kW Portanto, na equação da energia: 104 × 20 × 10–3 × 2 + 1,6 × 103 = 104 × 12,5 × 10–3 × 0,86 + 104 × 7,5 × 10–3 × h + 0,825 × 103 e finalmente h = 14,7 m

## 4.9 Interpretação da perda de carga

A existência de atrito no escoamento do fluido provoca uma dissipação de energia que, por unidade de peso, é computada matematicamente na Equação 4.27 pela perda de carga H p . 1,2 Note-se que a idéia de perda de carga é introduzida para balancear a equação, sem o objetivo de procurar explicar o paradeiro da energia que vai sendo perdida pelo fluido ao longo do seu escoamento.

Observe-se também que, a essa altura, ainda são vigentes as hipóteses de fluido incompressível (ρ = cte) e da ausência de trocas induzidas de calor. Conclui-se, portanto, que a idéia de perda de carga está ligada a essas hipóteses e que, se elas falharem, esse termo da equação da energia deverá ser introduzido e interpretado de outra maneira.

É evidente que, entrando em detalhes, a perda de carga, provocada pelo efeito mecânico do atrito no escoamento do fluido, acabará recaindo em efeitos térmicos, que deverão ser levados em consideração na sua interpretação.

Para facilitar a compreensão, vamos observar dois casos isolados que na prática acontecem simultaneamente. Vamos supor, em primeiro lugar, que o escoamento fosse isotérmico (Figura 4.12).

<!-- p. 103 -->
Figura 4.12 Nesse caso, o atrito provoca uma tendência de aquecimento do fluido; mas, diante da hipótese, como T = cte ao longo do escoamento, deve-se supor que haverá uma troca de calor entre o fluido e o meio. Como o calor é uma energia que flui, o sentido do seu fluxo será indicado por um sinal. Considera-se o calor positivo quando é fornecido ao sistema e negativo em caso contrário. Indicando por q o calor trocado por unidade de peso, tem-se:

q > 0 quando fornecido ao fluido; q < 0 quando retirado do fluido.

É óbvio que o calor gerado pelos atritos é sempre perdido pelo fluido e, portanto, pela nossa convenção, será sempre negativo. Logo, como a perda de carga é um termo positivo, tem-se nesse caso:

Hp1,2 = – q (4.32)

Vamos supor agora que o escoamento fosse adiabático, isto é, sem trocas de calor. Nesse caso, como não é trocado calor entre as seções (1) e (2), haveria ao longo do escoamento um aquecimento provocado pelo atrito (Figura 4.13). Figura 4.13 O aumento da temperatura do fluido denota um aumento de sua energia térmica ou interna. Indicaremos essa energia por unidade de peso por i e, na ausência de outros fenômenos, i será proporcional a T. Logo: i = ce T g (4.33)

onde ce = calor específico do fluido = calor necessário para que a unidade de massa do fluido sofra uma variação de temperatura de um grau. A aceleração da gravidade g aparece pelo fato de ce ser definido por unidade de massa e i por unidade de peso. Como, devido ao atrito, T2 > T1, então i2 > i1, denotando o aumento de energia térmica do fluido.

<!-- p. 104 -->
Pelo princípio da conservação da energia, o aumento de energia térmica do fluido deverá ser acompanhado por uma diminuição da energia mecânica, cujo total é representado pela carga H; logo, se i2 > i1 ⇒ H2 < H1 Na realidade, deve ser lembrado que: αv2 p H= + +z 2g γ Assim, z2 – z1 é Por outro lado, função apenas das v1 = Q1 A1 e v2 = Q2 A2 cotas das seções (1) , pois, por se tratar e (2). de um fluido incompressível, Q1 = Q2, e, portanto, v1 e v2 são funções geométricas das áreas das seções. Conclui-se, assim, que o aumento da energia térmica só pode ser realizado à custa de uma diminuição correspondente da energia de pressão.

Logo, nesse caso, a perda de carga deverá ser interpretada pelo aumento da energia térmica ou por uma perda de energia de pressão, reduzindo-se, portanto, o conteúdo de energia mecânica do fluido. Nesse caso:

H p1,2 = i2 – i1 = ce g (T 2 – T1 ) (4.34)

Logo, quando se interpretam apenas os fenômenos mecânicos do escoamento de um fluido incompressível, o aumento da energia térmica, provocado pelos atritos, é incluído nas perdas mecânicas, interpretadas globalmente pela ‘perda de carga’. Em regime permanente, o escoamento não será nem adiabático nem isotérmico e haverá uma simultaneidade de trocas de calor e variação de temperatura entre uma seção e outra, devido aos atritos, de forma que: H p1,2 = (i 2 – i1 ) – q (4.35)

Apesar da coerência da Equação 4.35, não será possível obter a perda de carga numericamente, pela medida de seus efeitos térmicos, devido ao fato de que estes, sendo muito pequenos, são difíceis de avaliar. Logo, a Equação 4.35 deve ser interpretada apenas conceitualmente, sem o objetivo de uso para o cálculo da perda de carga, que será mostrado por outros meios no Capítulo 7.

Água escoa numa tubulação horizontal de 5 cm de diâmetro com uma vazão de 5 L/s. A perda de carga num trecho de 10 m é 2 m. a) Supondo o escoamento adiabático, qual seria a variação de temperatura entre as duas seções? b) Supondo o escoamento isotérmico, qual seria o fluxo de calor para o ambiente? c) Qual é a queda de pressão entre as duas seções? Dados: γ = 104 N/m3; g = 10 m/s2; ce = 4,186 kJ/kg.°C; Solução a) H p1,2 = ce g ( T2 – T1 ) T2 – T1 = gH p1,2 ce T2 – T1 = 10 × 2 4,186 × 103 m / s2 × m = m2 / s2 = °C J / kg. °C N. m / kg. °C já que N/kg = m/s2.

<!-- p. 105 -->
Logo: T2 – T1 = 0,0048°C Esse resultado mostra que seria impossível detectar a perda de carga pela medida da variação da temperatura do fluido. b) Hp1,2 = –q q = –2 m O sinal negativo é conseqüência do fato de que o calor é perdido pelo fluido. Fluxo de calor é o calor trocado por unidade de tempo. Mas q = calor/peso Logo:

Fluxo de calor = calor = calor × peso tempo peso tempo ou Fluxo de calor = q × QG = qγQ portanto: Fluxo de calor = –2 × 104 × 5× 10–3 ⎛⎜ m × ⎝ N× m3 m3 ⎟⎞ = J = W s⎠ s Fluxo de calor = –100 W c) H p 1,2 = H2 – H1 = ⎛ ⎜ α 2v 2 2 ⎝ 2g + p2 γ + z2 ⎞ ⎟ ⎠ – ⎛ ⎜ α 1v 2 1 ⎝ 2g + p1 γ + z1 ⎞ ⎟ ⎠ Como o tubo é horizontal, z2 – z1 = 0. Como tem seção constante, α2v22 – α1v21 = 0 2g 2g Logo: H p 1,2 = p2 – γ p1 p2 – p1 = γHp1,2 ou p2 – p1 = 104 × 2 = 20 kPa

## 4.10 Equação da energia geral para regime permanente

A Equação 4.27 só é válida se o fluido for incompressível e sem trocas induzidas de calor. Note-se que a troca de calor devida aos atritos é considerada natural e não induzida, pelo que foi exposto no item 4.9.

A Equação 4.27 é, portanto, válida para líquidos, mas pode ser válida também para gases, desde que no seu escoamento as variações da densidade sejam desprezíveis (ρ ≅ cte). Não será aqui justificado, mas pode-se verificar que a hipótese de fluido incompressível pode ser mantida, desde que o número de Mach do fluido seja menor que 0,2.

Define-se número de Mach (M) como sendo a relação entre a velocidade do fluido (v) e a velocidade do som (c) numa certa seção do escoamento. Logo:

M = v . c Dessa forma, sempre que v < 0,2, é possível utilizar as equações válidas para fluidos inc compressíveis, como, por exemplo, as equações 4.27 e 3.13.

Quando o fluido for compressível e houver trocas induzidas de calor, não será mais possível ignorar as energias térmicas, que passam a desempenhar um papel importante na interpretação dos fenômenos. Por outro lado, a existência de troca de calor induzida e a variação da energia térmica causada por essa troca fazem com que não seja mais possível observar a perda de carga, já que no global é causadora também de variação de energia interna e de troca de calor. Em outras palavras, nessas condições:

H p1,2 ≠ (i 2 – i1 )– q

<!-- p. 106 -->
Por causa disso, na equação da energia, válida para fluidos compressíveis e com efeitos térmicos, o balanço das energias deve ser feito considerando a variação da energia térmica e o calor, sem destacar a perda de carga que, de certa forma, torna-se irreconhecível ou, em outras palavras, fica englobada nos efeitos térmicos. Figura 4.14 Logo:

H1 + i1 +Hm + q = H2 + i2 (4.36)

Note-se que Hm e q podem ser positivos ou negativos, dependendo de serem fornecidos ou retirados do fluido. Escrita por extenso, a Equação 4.36 fica:

α 1 v12 2g + z1 + p1 γ1 + i1 +Hm + q = α 2 v 2 2 2g +z2 + p2 γ2 + i2 (4.37) ou α 1 v12 2g + z1 + p1 γ1 +Hm = α 2 v 2 2 2g +z2 + p2 γ2 + i2 – i1 –q (4.38) Como já foi dito anteriormente, no caso de fluidos compressíveis, com troca de calor: i 2 – i1 – q ≠ H p1,2 e no caso de fluidos incompressíveis, sem troca de calor:

i 2 – i1 – q = H p1,2 recaindo-se na Equação 4.27.

p Na Equação 4.38 pode-se ainda fazer h = γ + i onde h = entalpia por unidade de peso e se pode escrever:

α 1 v12 2g + z1 + h1 +Hm +q = α 2 v 2 2 2g +z2 +h2 (4.39)

que nada mais é do que a primeira lei da termodinâmica para sistema aberto ou volume de controle.

<!-- p. 107 -->
4.1 Determinar a velocidade do jato do líquido no orifício do tanque de grandes dimensões da figura. Considerar fluido ideal. Resp.: v = 2gh 4.2 Supondo fluido ideal, mostrar que os jatos de dois orifícios na parede de um tanque interceptam-se num mesmo ponto sobre um plano, que passa pela base do tanque, se o nível do líquido acima do orifício superior é igual à altura do orifício inferior acima da base. 4.3 A pressão no ponto S do sifão da figura não deve cair abaixo de 25 kPa (abs). Desprezando as perdas, determinar: a) a velocidade do fluido; b) a máxima altura do ponto S em relação ao ponto (A); patm = 100 kPa; γ = 104 N/m3 Resp.: a) 4,9 m/s; b) z = 6,3 m 4.4 Um tubo de Pitot é preso num barco que se desloca a 45 km/h. Qual será a altura h alcançada pela água no ramo vertical?

<!-- p. 108 -->
Resp.: h = 7,8 m 4.5 Quais são as vazões de óleo em massa e em peso no tubo convergente da figura, para elevar uma coluna de 20 cm de óleo no ponto (0)? Dados: desprezar as perdas; γóleo = 8.000 N/m3; g = 10 m/s2 Resp.: Qm = 2,1 kg/s; QG = 21 N/s 4.6 Dado o dispositivo da figura, calcular a vazão do escoamento da água no conduto. Dados: γ H2 0 = 104 N/m 3; γ m = 6 × 104 N/m 3; p2 = 20 kPa; A = 10–2 m 2; g = 10m/ s2. Desprezar as perdas e considerar o diagrama de velocidades uniforme. Resp.: Q = 40 L/s 4.7 Na extremidade de uma tubulação de diâmetro D, acha-se instalado um bocal que lança um jato de água na atmosfera com diâmetro de 2 cm. O manômetro metálico registra uma pressão de 20 kPa e a água sobe no tubo de Pitot até a altura de 2,5 m. Nessas condições, determinar: a) a vazão em peso do escoamento; b) o diâmetro D do tubo, admitindo escoamento permanente e sem atrito. γ H2 O = 10 N/ L.

<!-- p. 109 -->
Resp.: a) 22,3 N/s; b) D = 3 cm 4.8 No conduto da figura, o fluido é considerado ideal. Dados: H1 = 16 m; p1 = 52 kPa; γ = 104 N/m3; D1 = D3 = 10 cm. Determinar: a) a vazão em peso; b) a altura h1 no manômetro; c) o diâmetro da seção (2). Resp.: a) QG = 314 N/s; b) h1 = 0; c) D2 = 5,7 cm 4.9 Um dos métodos para se produzir vácuo numa câmara é descarregar água por um tubo convergentedivergente, como é mostrado na figura. Qual deve ser a vazão em massa de água pelo convergente-divergente, para produzir uma depressão de 22 cm de mercúrio na câmara da figura? Dados: desprezar as γ perdas de carga; γ H2O = 104N/m3; Hg = 1,36 × 105N/m3; g = 10 m/s2; D1 = 72 mm; D2 = 36 mm. Resp.: Qm = 8,14 kg/s

<!-- p. 110 -->
4.10 Num carburador, a velocidade do ar na garganta do Venturi é 120 m/s. O diâmetro da garganta é 25 mm. O tubo principal de admissão de gasolina tem um diâmetro de 1,15 mm e o reservatório de gasolina pode ser considerado aberto à atmosfera com seu nível constante. Supondo o ar como fluido ideal e incompressível e desprezando as perdas no tubo de gasolina, determinar a relação gasolina/ar (em massa) que será admitida no motor. Dados: ρgas = 720 kg/m3; ρar = 1 kg/m3; g = 10 m/s2. Resp.: 0,0565 4.11 Desprezando os atritos no pistão da figura, determinar:

a) a potência da bomba em kW se seu rendimento for 80%; b) a força que o pistão pode equilibrar com a haste.

Dados: A2 m; Hp5,6 = = 1 A3 m; = g A=41=0Am5/=sA2;6γ==1010cm4 N2;/AmG3=. S8ucpmo2r; Ap = 20 cm2; Ah = 10 o cilindro no plano cm2; Hp1,2 = Hp3,4 da tubulação.

= 0,5 m; Hp4,5 = 0 Resp.: a) 0,375 kW; b) 38,1 N 4.12 Um túnel aerodinâmico foi projetado para que na seção de exploração A a veia livre de seção quadrada de 0,2 m de lado tenha uma velocidade média de 30 m/s. As perdas de carga são: a) entre A e 0 → 100 m; b) entre 1 e A → 100 m. Calcular a pressão nas seções 0 e 1 e a potência do ventilador se seu rendimento é 70%. γ( ar = 12,7 N/m3)

<!-- p. 111 -->
Resp.: po = –734 Pa; p1 = 1.806 Pa; NV = 4,4 kW 4.13 Sabendo que a potência da bomba é 3 kW, seu rendimento 75% e que o escoamento é de (1) para (2), determinar: a) a vazão; b) a carga manométrica da bomba; c) a pressão do gás. Dados: Hp1,2 = Hp5,6 = 1,5 m; Hp3,4 = 0,7 m; γ Hp4,5 = 0; 3A5 = A4 = 100 cm2; = 104 N/m3.

Resp.: a) 47 L/s; b) 4,8 m; c) –49 kPa 4.14 Na instalação da figura, a carga total na seção (2) é 12 m. Nessa seção, existe um piezômetro que indica 5 m. Dados: γ H2O = 104 N/m3; γHg = 1,36× 105 N/m3; h = 1 m; D1 = 6 cm; D2 = 5 cm; ηB = 0,8. Determinar: a) a vazão; b) a pressão em (1); c) a perda de carga ao longo de toda a tubulação; d) a potência que o fluido recebe da bomba.

<!-- p. 112 -->
Resp.: a) 19,6 L/s; b) –76 kPa; c) 21,2 m; d) 3 kW 4.15 O bocal da figura descarrega 40 L/s de um fluido de ν = 10–4 m2/s e γ = 8.000 N/m3 no canal de seção retangular. Determinar:

a) a velocidade média do fluido no canal; b) o mínimo diâmetro da seção (1) para que o escoamento seja laminar; c) a perda de carga de (1) a (2) no bocal, quando o diâmetro é o do item (b), supondo p1 = 0,3 Mpa; d) a velocidade máxima no canal, se o diagrama é do tipo v = ay2 + by + c, com dv/dy = 0 na superfície do canal (vide figura). Resp.: a) 0,5 m/s; b) 0,255 m; c) 16,8 m; d) 0,75 m/s 4.16 Dados: Hp2,3 = 2 m; A3 = 20 cm2; A2 = 1 cm2; Hp0,1 = 0,8 m; ηB = 70%. Determinar: a) a vazão (L/s); b) a área da seção (1) (cm2); c) a potência fornecida pela bomba ao fluido.

Resp.: a) 0,71 L/s; b) 1,45 cm2; c) 9,4 W

<!-- p. 113 -->
4.17 Na instalação da figura, a máquina M2 fornece ao fluido uma energia por unidade de peso de 30 m e a perda de carga total do sistema é 15 m. Determinar: a) a potência da máquina M1, sendo ηm1 = 0,8; b) a pressão na seção (2) em mca; c) a perda de carga no trecho (2)-(5) da instalação. Dados: Q = 20 L/s; γ = 104 N/m3; g = 10 m/s2; A = 10 cm2 (área da seção dos tubos). Resp.: a) NT = 4 kW; b) 45 mca; c) 5 m 4.18 Na instalação da figura, a vazão de água na máquina é 16 L/s e tem-se Hp1,2 = Hp3,4 = 1 m. O manômetro na seção (2) indica 200 kPa e o da seção (3) indica 400 kPa. Determinar: a) o sentido do escoamento; b) a perda de carga no trecho (2)-(3); c) o tipo de máquina e a potência que troca com o fluido em kW; d) a pressão do ar em (4) em MPa. Resp.: a) (4) para (1); b) 17 m; c) turbina; 1,95 kW; d) 0,362 MPa 4.19 Na instalação da figura são dados: área da seção das tubulações: A = 10 cm2 (constante) piezômetro (2): h2 = 7 m piezômetro (3): h3 = 11 m piezômetro (4): h4 = 9 m perda de carga no trecho (1)-(2) = 1,8 m e no trecho (5)-(6) = 2 m γ = 10.000 N/m3 kgf/m3; ηM1 = 80%; ηM2 = 70%. Determinar:

<!-- p. 114 -->
a) o sentido do escoamento (justificar); b) a vazão (L/s); c) o tipo de máquina M1 e sua potência; d) o tipo de máquina M2 e a potência trocada com o fluido. Resp.: a) (6)-(1); b) 6 L/s; c) NT = 0,192 kW; d) NB = 0,59 kW 4.20 Na instalação da figura, os reservatórios são de pequenas dimensões, mas o nível mantém-se constante. a) Qual é a vazão na tubulação que une a parte inferior dos dois tanques? b) Para que aconteça essa vazão, qual a pressão em (3)? c) Qual é a perda de carga na tubulação inferior dos dois tanques? Dados: potência recebida pelo fluido da 100 kPa; Hp0,1 = 2 m; Hp2,3 = 4 m; γ = 104 bomba N/m3. N = 1,5 kW; D1 = 4 cm; D1 ≠ D2; p1 = 50 kPa (abs); patm = Resp.: a) 5,62 L/s; b) 0,207 MPa; c) 20,7 m 4.21 No circuito da kW; ηT = 0,75; figura instalado num plano A1 = A2 = A4 = 80 cm2; A3 = 1h0o0riczmon2;taγl,=te1m04-Nse/pm1 3=.

0,3 MPa; p2 = 0; p3 = 0,1 MPa; NT = 6 A potência que o fluido recebe da bomba é o dobro da potência da turbina. Determinar: a) a vazão; b) a perda de carga no trecho da direita; c) a leitura do manômetro (4); d) a perda de carga no trecho da esquerda.

<!-- p. 115 -->
Resp.: a) 40 L/s; b) 0,45 m; c) 0,295 MPa; d) 9,55 m 4.22 No circuito da figura, a bomba B1 é acionada pela turbina. A vazão é 30 L/s e os rendimentos da turbina e d=a10b4oNm/bma B3)1rseãcoe,breesdpaebcotimvabma eBn2tuem, 0a,7peo0tê,8n.cAiapdeerd6akWde,cdaertgearmnaintuarbauplaoçtãêonéci1a5qmue. Sabendo que o fluido cede o à fluido (γ turbina.

Resp.: N = 3,4 kW 4.23 Determinar o coeficiente α da energia cinética para o escoamento de um líquido num tubo de seção circular. O escoamento é laminar e o diagrama de velocidades é v = v max ⎡ ⎢1 ⎢⎣ – ⎝⎜⎛ r R ⎟⎠⎞ 2 ⎤ ⎥. ⎥⎦ Resp.: α = 2 4.24 Determinar o coeficiente α da energia cinética para o escoamento turbulento de um líquido num tubo de seção circular. O diagrama de velocidades é v = vmax ⎜⎝⎛1 – r R ⎟⎞⎠ 1/ 7 .

Resp.: α = 1,06 4.25 É dado um diagrama bidimensional de velocidades de um fluido ideal, num canal de largura 2 m: a) Qual é a velocidade média na seção? b) Qual é a vazão em volume? c) Qual é o coeficiente α da energia cinética? d) Qual é o fluxo da energia cinética, se ρ = 1.000 kg/m3? e) Qual é a carga cinética? Resp.: a) 3 m/s; b) 30 m3/s; c) 1,11; d) 149.850 W; e) 0,5 m

<!-- p. 116 -->
4.26 O esquema da figura corresponde à seção longitudinal de um canal de 25 cm de largura. Admite-se que a velocidade é invariável ao longo da normal ao plano do esquema, sendo variável com y através de v = 30y – y2 (y em cm e v em cm/s). Sendo o fluido de peso específico 9 N/L, viscosidade cinemática 70 cSt, g = 10 m/s2 , determinar: a) o gradiente de velocidade para y = 2 cm; b) a máxima tensão de cisalhamento na seção em N/m2; c) a velocidade média na seção em cm/s; d) a vazão em massa na seção em kg/h; e) o coeficiente da energia cinética (α) na seção.

Resp.: a) 26 s–1; b) 1,9 N/m2; c) 0,67 m/s; d) 27.135 kg/h; e) 1,73 4.27 Sabendo que a vazão proporcionada pelo tanque inferior da instalação é igual a 15 L/s e que a potência dissipada por atritos em toda a instalação é 1 kW, determinar o tipo da máquina e sua potência. Dados: γ = 104 N/m3; Hp0,2 = 4,8 m; At = 100 cm2; pm = 40 kPa; ηm = 80%. Resp.: Turbina NT = 1,31 kW 4.28 A figura está num plano vertical. Calcular a perda de carga que deve ser introduzida pela válvula V da figura para que a vazão se distribua igualmente nos dois ramais, cujos diâmetros são iguais. Dados: D = 5 cm; γ H2 O = 104 N/m3; par = 0,2 MPa; Q = 10 L/s; Hp0,1 = 2 m; Hp1,2,4 = 0; Hp2,3= 3 m; Hp4,5 = 3 m; Hp6,7 = 2 m.

<!-- p. 117 -->
Resp.: HpV = 22,4 m 4.29 No sistema da figura, a bomba deve fornecer 10 L/s ao reservatório superior e a turbina deve ter uma potência no eixo de 3 kW com um rendimento de 80%. Qual é a carga manométrica da bomba e a da turbina? Dados: Hp0,1 = 2 m; Hp2,3 = 4 m; Hp3,4 = 4 m; Hp5,6 = 4 m; Hp3,7 = 2 m; Hp3 ≅ 0; NB = 7,5 kW; γ = 104 N /m3; ηB = 0,8. Resp.: HT = 117,2 m; HB = 45,5 m 4.30 Na instalação da figura, todas as tubulações são de diâmetro muito grande em face da vazão, o que torna desprezível a carga cinética. Determinar: a) o tipo de máquina e a sua carga manométrica; b) a vazão em volume proveniente do reservatório; Dados: Q2 = Q3; Hp0,1 = 1 m; Hp1,2 = 1 m; Hp1,3 = 4 m; ηm = 80%; potência no eixo da máquina = 0,7 kW Resp.: a) bomba (HB = 2 m); b) Q0 = 56 L/s

<!-- p. 118 -->
4.31 Na instalação da figura, todas as tubulações são de mesmo diâmetro (D = 138 mm); o registro é ajustado para que a vazão pela seção (1) seja a metade da vazão pela seção (2). Para tal condição, a altura manométrica da bomba vale 8 m e as perdas de carga valem, respectivamente: H p 0,e =1 3 (v 2 e / 2g); H p s,1 = 5 (v 2 1 / 2g); H p s,2 = 1,5 (v 2 2 / 2g)

Desprezando a perda de carga no ‘T’ na saída da bomba, determinar sua potência, sendo seu rendimento 48%. (γ H2O = 104 N/m3; g = 10 m/s2). Resp.: NB = 15 kW 4.32 No trecho da instalação da figura, que está num plano horizontal, determinar: a) a leitura no manômetro (2) para que se possa considerar a perda de carga desprezível no TÊ; b) a perda de carga de (1) a (2), (5) a (6) e (3) a (4); c) a potência dissipada em todo o conjunto em kW. Dados: γ = 104 N/m3; p1 = 0,2 MPa; p3 = 0,15 MPa; p5 = 0,1 MPa; A = 10 cm2 (área da seção das tubulações). Resp.: a) p2 = 84 kPa; b) Hp1,2 = 11,6 m; Hp3,4 = 15 m; Hp5,6 = 10 m; c) 2,36 kW 4.33 Os tanques A e D são de grandes dimensões e o tanque C é de pequenas dimensões, mas o nível (4) permanece constante. A bomba B, que tem ηB = 80%, recebe 11 kW do motor elétrico e tem carga manométrica de 20 m. Determinar: a) o tipo de máquina M e a sua carga manométrica; b) a vazão no trecho (4)-(5) (Qc) (L/s); c) a vazão que passa na bomba B (L/s); d) a cota z (m). Dados: Hp0,3 = 3 m; Hp4,5 = 0 m; Hp6,7 = 2 m; Hp8,9 = 10 m.

<!-- p. 119 -->
Resp.: a) HT = 26,3 m; b) Qc = 30,4 L/s; c) QB = 44 L/s; d) z = 13,6 m 4.34 O sistema de propulsão de um barco consta de uma bomba que recolhe água na proa através de dois tubos de 5 cm de diâmetro e a lança na popa por um tubo com o mesmo diâmetro. Calcular a potência da bomba, sabendo que a vazão em cada conduto de entrada é 25 L/s, a potência dissipada pelos atritos é 0,44 kW e o rendimento é ηB = 0,75. Resp.: NB = 16,6 kW 4.35 Ar escoa isotermicamente por um tubo longo, horizontal, de diâmetro constante. Numa seção em que a pressão é de 1 MPa (abs), a velocidade é 25 m/s. Por causa do atrito no escoamento, a pressão numa seção distante da anterior é 0,2 MPa (abs). a) Qual o aumento da carga cinética? b) Qual a troca de calor em kJ/kg para que a temperatura seja mantida constante? Resp.: a) Δ v2 = 750 m; b) q = 7,5 kJ/kg 2g 4.36 NMtemoPacpoo(na(bvfsleu)r;xgpoe2nd=tee0cd,a1aloMfri)Pg,ausar(aabbeenss)dceooaρq1aur=ec1aoknvgasi/zdãmeor3ea, mddeovtgeorálmusmpineearrnfeoaitscoea.çloSãroent(r1do)océaAd1lom=e30n/,t1sreemq(21u;)Aeeo2(=2e)s0cp,o0oa5rmmuen2ni;dtpoa1dé=eis0do,2etérmico. Dizer se o calor é retirado ou fornecido. (Justificar.)

<!-- p. 120 -->
Resp.: 0,75 kW 4.37 Na máquina da figura, são dados: v1 = 4 m/s; A1 = 0,52 m2; A2 = 0,4 m2; p1 = p2 = 0,1 MPa. O escoamento é isotérmico, a potência fornecida ao fluido compressível pela máquina é 10 kW e o fluxo de calor perdido para o exterior é 0,98 kW. Qual é a vazão em massa através da máquina? Resp.: Qm = 1.634 kg/s 4.38 Uma turbina a vapor consome 4.500 kg/h de vapor e recebe dele 736 kW. As velocidades de entrada e saída do vapor são, respectivamente, 60 m/s e 275 m/s, e as entalpias, 2.760 kJ/kg e 2.090 kJ/kg. Calcular a perda de calor através da carcaça em kW. Resp.: 56 kW 4.39 A figura mostra uma máquina hidráulica por onde escoa água, isotermicamente. Desprezando as diferenças de cotas, determinar 0,25 m2; p1 = 0,2 MPa (abs); o tipo de p2 = p3 = máquina e o seu rendimento. 0,3 MPa (abs); Q1 = 2,5 m3/s; Dados: A1 = 0,5 m2; A2 = 0,2 m2; v2 = 5 m/s; calor perdido = 14,7 A3 = kW.

(Aproveitar o exercício para induzir a equação geral, para regime permanente, para diversas entradas e saídas.)

Resp.: Bomba com ηB = 0,95

<!-- p. 121 -->

# Capítulo 5 — Equação da quantidade de movimento para regime permanente

## 5.1 Introdução

Nos capítulos 3 e 4 foram realizados os balanços das massas e energias, no escoamento de um fluido, por meio das equações da continuidade e da energia, respectivamente. Em muitos problemas da engenharia, é necessário determinar as forças que agem em estruturas sólidas, fixas ou em movimento, devidas a fluidos que se movem em contato com elas. A equação que permitirá essa análise chama-se equação da quantidade de movimento. As forças determinadas serão denominadas dinâmicas, em contraposição àquelas do Capítulo 2, que poderiam ser chamadas de estáticas, já que causadas pela ação de um fluido em repouso.

## 5.2 Equação da quantidade de movimento

Essa equação nada mais é que a segunda lei de Newton da dinâmica modificada funcionalmente para o estudo da Mecânica dos Fluidos. Segundo essa lei, a aceleração de uma certa massa implica a existência de uma força resultante sobre ela que tem, em cada instante, a direção e o sentido da aceleração. Acelerar uma massa significa modificar sua velocidade em módulo e/ou direção, e por essa observação, para que a velocidade de um fluido seja modificada em módulo ou direção, será necessário aplicar uma força provocada por algum agente externo, em geral uma superfície sólida em contato com o escoamento.

Pelo princípio da ação e reação, se a superfície aplica uma força no fluido, este aplicará, sobre a superfície, uma outra de mesmo módulo e de sentido contrário. A observação desses fatos permitirá a construção da equação da quantidade de movimento, nos moldes desejados. Seja a segunda lei de Newton da dinâmica:

r F = r ma = m r dv (5.1) dt Note-se que essa equação deve ser mantida na forma vetorial, pois a velocidade pode variar em direção sem que seja alterado o seu módulo.

A Equação 5.1 é estabelecida para um sistema que tem, por definição, massa constante; logo, pode-se escrever:

r F= d r (mv) (5.2) dt

<!-- p. 122 -->
r Como mv é, por definição, a quantidade de movimento do sistema, então pode-se dizer que a força resultante, que age no sistema em estudo, é igual à variação com o tempo da quantidade de movimento do sistema.

Esse é o teorema estabelecido na Mecânica e que deverá ser aproveitado para a determinação das forças dinâmicas em estudo.

A equação da quantidade de movimento será estabelecida inicialmente para um tubo de corrente e para a hipótese de regime permanente, como já foi feito nas equações dos capítulos anteriores. No Capítulo 3 verificou-se que a aceleração r a = r dv deve ser compreendida como uma variação local com o tempo ∂vr ∂t , mais uma variação de dt transporte de um ponto a outro do fluido. Quando o regime é permanente, as propriedades não variam em cada ponto com o tempo, mas podem variar de um ponto para outro. A variação da quantidade de movimento no caso da Figura 5.1 deve então ser entendida como a variação entre as seções (1) e (2). Figura 5.1 Admitindo propriedades uniformes na seçrão, no intervalo de tempo dt, a massa de fluido que atravessa a seção (1) com velocidade v1 será dm1, provocarndo um incremento da quantidade de movimento do fluido entre as seções (1) e (2) de dm 1 v1 . No mesmo inr tervalo de tempo, através da seção (2) existe a saída de uma quantidade de movrimento drm 2 v2 . Logo, a variação da quantidade de movimento entre (1) e (2) será dm 2 v 2 – dm 1 v1 . Pelo teorema da quantidade de movimento, a força resultante que age no fluido entre as seções (1) e (2) será: ou r F = r dm 2 v 2 – r dm 1 v1 dt dt r r r F = Q m2 v 2 – Q m1 v1 Por outro lado, como o regime é permanente, então:

r Q m1 = Q m2 = Q m rr r e, portanto:

F = Qm (v2 – v1 ) = QmΔv (5.3) r rr r A Equação 5.3 mostra também que F tem a direçrão dre Δv = v2 – v1 e o ponto de aplicação pode ser encontrado na intersecção das direções de v1 e v2 (Figura 5.1).

A Equação 5.3 permite determinar a força resultante que age no fluido entre (1) e (2), o que normalmente não é o objetivo principal.

<!-- p. 123 -->
r Vamos analisar as forças componentes da resultante F (Figura 5.2).

Figura 5.2 O fluido entre (1) e (2) está sujeito a forças de contato normais (de pressão) e tangenciais (rtensões de cisalhamento) e à força de campo causada pelo campo de gravidade, que é o peso G (exclui-se a existência de outros campos).

Nas seções (1) e (2), o fluido a montante e a jusante do tubo de corrente (1)-(2) aplica pressões nessas seções contra o fluido contido entre elas.

As forças devidas às pressões nas seções (1) e (2) são, respectivamente, p1A1 e p2A2 em módulo. Para a determinação dos vetores das forças nessas duas seções, adotam-se versores normais a elas, com sentido para fora do tubo de corrente, por convençãro. Dessa forrma, as forças que agem no fluido nas seções (1) e (2) serão, respectivamente, –p1 A1 n1 e –p2 A 2 n 2 , onde os sinais negativos se devem à convenção adotada para as normais, como se observa na Figura 5.2. Na superfície lateral, o fluido está sujeito a pressões e também a tensões de cisalhamento devidas ao seu movimento em contato com o meio.

Essas pressões e tensões de cisalhamento podem variar de um ponto para outro da superfície lateral. A resultante das pressões pode ser obtida adotando-se em cada ponto uma normal dirigida para fora, conforme a convenção adotada.

A resultante em cada elemento r dAlat no entorno r de r um ponto da superfície lateral será: dF's = –p lat n lat dA lat + τdA lat Logo, a força resultante das pressões e tensões de cisalhamento na superfície lateral será: ∫ ∫ r Fs' = r – p lat n lat dA lat + τrdA lat Uma vez definida essa resultante, a Figura 5.2 pode ser reduzida à Figura 5.3.

Figura 5.3 r Pelo exposto, a força F resultante que age no fluido entre (1) e (2) será a soma das componentes representadas na Figura 5.3.

<!-- p. 124 -->
Logo: rr r rr F = F's + (–p1A1 n1 )+(–p 2A 2 n 2 )+ G Mas, pela Equação 5.3:

r r rr rr Fs' – p1A1 n1 – p 2A 2 n 2 + G = Q m (v 2 – v 1 )

(5.4)

Em geral, o interesse por essa equação corresponde aos casos em que o fluido está em contato com uma superfície sólida, na superfície lateral entre (1) e (2). Nessa condição, a força F's representaria a resultante das forças de contato da superfície sólida contra o fluido. Isolando esse termo na Equação 5.4, obtém-se:

r r r rr r F's = p1A1 n1 + p 2A 2 n 2 + Q m (v 2 – v 1 )– G Na prática, normalmente, interessa determinar a força que o frluido aplica na superfície sólida com a qual está em contato entre as seções (1) e (2). Como FS′ representa ar força resultante da superfície sólida no fluido, então, perlo prirncípio da ação e reação, a força FS que o fluido aplica na superfície sólida será:

r r Fs = –F's r rr r ou Fs = –[p1A1 n1 + p 2A 2 n 2 + Q m (v 2 – v 1 )]+ G (5.5)

r Para facilidade de cálculo nos exercícios, não será levado em consideração o peso do fluido G; entretanto, deseja-se ressaltar que nem sempre esse termo pode ser considerado desprezível e nas aplicações práticas deverá, às vezes, ser calculado.

Pelo exposto, a Equação 5.5 será daqui em diante usada na forma:

r r r rr Fs = –[p1A1 n1 + p 2A 2 n 2 + Q m (v 2 – v 1 )] (5.6)

## 5.3 Método de utilização da equação

A Equação 5.6 não é aplicada na forma vetorial. Normalmente adotam-se eixos convenientes e, para a solução do problema, os vetores da equação são projetados na direção deles. Todos os vetores da equação srerão, então, projetados na direção desses eixos, determinando-se as componentes da força Fs nessas drireções. Se o resultado final desejado for a força Fs , essas duas componentes poderão ser compostas vetorialmente para a sua obtenção. As aplicações a seguir têm o objetivo de esclarecer o método de utilização da Equação 5.6. Aplicação 1 — Conduto com redução gradual da seção

<!-- p. 125 -->
Seja o conduto da figura. Suponha-se o fluido incompressível, as propriedades uniformes nas seções e o regime permanente. Será determinado o esforço horizontal do fluido sobre o conduto. Tal força serviria, por exemplo, para dimensionar algum sistema para a sua fixação.

Para o trecho (1)-(2) pode-se escrever:

r r r rr Fs = –[p1 A 1 n 1 + p 2 A 2 n 2 + Q m (v 2 – v1 )] Projetando na direção de x:

Fsx = –[p1 A1 (–1) + p2 A 2 (+1) + Qm (v2 – v1 )] ou Fsx = p1 A 1 – p 2 A 2 + (v1 – v 2 ) ρQ Note-se que a vantagem desse método é relativa ao fato de que o estudo é realizado inteiramente nas seções de entrada e saída do conduto, sem a preocupação com a distribuição intermediária das forças. Como nenhum dos vretores da figura tem componentes na direção y, Fsy = 0 (deve-se ao fato de não se considerar G). Aplicação 2 — Redução de seção e mudança de direção Admitindo as mesmas hipóteses anteriores:

r r r rr Fs = –[p1 A 1 n 1 + p 2 A 2 n 2 + Q m (v 2 – v1 )] Projetando segundo x:

Fsx = –[p1 A1 (–1) + p2 A 2 cos θ + Qm (v2 cos θ – v1 )] ou Fsx = p1 A1 – p2 A 2 cos θ + Qm (v1 – v2 cos θ)

Projetando segundo y:

Fsy = –[0 + p2 A 2 sen θ + Qm (v2 sen θ – 0)] ou Fsyr = –pr2 A 2 sen θ – ρQv2 sen θ Note-se que compondo Fsx e Fsy pode ser obtida a força resultante do fluido sobre o conduto, isto é:

Fs = F 2 sx + F 2 sy

<!-- p. 126 -->
Aplicação 3 — Desviador de jato fixo Na figura, observa-se um desviador de jato ou pá. Esse caso tem sua aplicação, por exemplo, em pás de turbinas. O fluido lançado contra o desviador sofre uma deflexão provocada por este.

r Note-se que, pela dedução da Equação 5.6, parte da forçaFs é produzida no contato do fluido com o ar, já que entre (1) e (2) o fluido não está totalmente envolvido pela superfície rsólida. A pressão na escala efetiva é nula; no entanto, o efeito do atrito do ar existe. Logo, seFs deve ser a resultante da força que o fluido aplica no anteparo, deve-se desprezar o atrito com o ar. Então: r r r rr Fs = –[p1 A 1 n 1 + p 2 A 2 n 2 + Q m ( v 2 – v1 )] Como em (1) e (2) o jato é livre à pressão r atmosférica, rr então p1 = p2 = 0. Logo:

Fs = Qm( v1 – v2 )

Projetando segundo x:

Projetando segundo y:

Fsx = Qm ( v1 – v2 cos θ)

Fsy = Qm (0 – v2 sen θ) = –Qm v2 sen θ É normal, nesse tipo de aplicação, desprezar o atrito do fluido na superfície sólida e a diferença de cotas entre (1) e (2), resultando em v1 = v2 = v j (velocidade do jato). Logo: Fsx = ρA j v 2 j (1 – cos θ) e r Fsy = –ρArj v 2 j sen r θ A força Fs é obtida pela composição de Fsx e Fsy , e seu ponto de aplicação estará no encontro das direções dos vetores da velocidade.

<!-- p. 127 -->
Aplicação 4 — Jato incidindo numa placa plana Considere que o jato, ao atingir o anteparo, seja espalhado uniformemente, em todas as direções. A velocidade v2 não terá, portanto, componente segundo x. Como a pressão é atmosférica, obtém-se: Fsx = ρQv1

## 5.4 Forças em superfícies sólidas em movimento

Em muitos problemas, deseja-se determinar a ação de fluidos em superfícies sólidas em movimento. Neste item serão considerados somente movimentos retilíneos e uniformes das superfícies, para não haver preocupações com forças de inércia devidas às acelerações. Com essa hipótese, o problema será resolvido de forma bastante simples, pois bastará realizar o estudo em relação a um sistema de referência fixo na superfície sólida em movimento. Dessa forma, a superfície sólida será novamente observada em repouso e o fluido terá a sua velocidade alterada em relação àquela vista do sistema de referência inercial. Nesse caso, a variação da velocidade deverá ser estudada a partir do sistema de referência fixo à superfície sólida. Vejamos como se alteram as expressões antes estabelecidas, quando a superfície sólida está em movimento. Para o estudo, será adotado um caso particular para maior facilidrade de compreensão. Seja na Figura 5.4 o desviador de jato em movimento com velocidade vs constante. Figura 5.4 r rr r Sabe-se da Mecânica que vabs = u + vs , onde: rvabs = velocidade absoluta, em relação ao sistema inercial; vs = velocidade de arrastamento ou velocidade da origem do sistema de referência fixo na superfície sólida; no caso, o desviador de jato;

<!-- p. 128 -->
r u = velocidade relativa ou velocidade em relação ao sistema de referência móvel; no caso, é a velocidade do jato em relação ao desviador. A forçardo desviador contra o jato de fluido lançado pelo bocal será função da velocidade relativa u. A visualização dessa afirmação é simples, já que, se o desviador estiver com uma velocidade maior que o jato de fluido, por exemplo, a força será nula; se o desviador tiver velocidade nula, a força será maior que se ele se afastasse com uma certa velocidade do jato. No caso em que a superfície sólida esteja parada, já foi visto que vale o resultado da Aplicação 3. No caso atual, a vazão do jato lançada pelo bocal é Qm = ρA1 v1 , mas a superfície sólida, devido ao seu movimento, não é atingida por essa vazão. O que incidirá sobre a superfície sólida será uma vazão aparente dada por: Q m ap = ρA 1 (v abs1 – v s ) = ρA 1 u 1 Logo, a Equação 5.6 ficará, para o caso do movimento relativo:

r rr Fs = Q m ap ( u 1 – u 2 )

(5.7)

Pode-se verificar que, com a hipótese de movimento retilíneo e uniforme da superfície srólidr a, todras as expressões continuam válidas, desde que seja utilizada a velocidade relativa u = v abs – v s e Qmap no lugar de Qm .

Assim, de uma forma geral, r r r rr Fs = –[p1 A 1 n 1 + p 2 A 2 n 2 + Q map ( u 2 – u 1 )] (5.8)

Um desviador de jato move-se com uma velocidade de 9 m/s. Um bocal de 5 cm de diâmetro lança um jato de óleo com uma velocidade de 15 m/s, tal que o jato incide sobre o desviador, conforme indicado na figura. O ângulo de saída é 60° e o peso específico do óleo é 8.000 N/m3. Calcular a força do jato contra o desviador. Solução Pela Equação 5.7 e pela observação do item 5.4, tem-se:

Fsx = ρQap(u 1 – u 2cos θ )

e Fsy = ρQap(0 – u 2sen θ2 )

Suponha que em módulo u1 = u2 = u. Pelos motivos descritos na Aplicação 3, obtém-se: Fsx = ρA ju(u – u cos 60° )= ρA ju 2(1 – cos 60° ) Fsy = ρA ju(0 – u sen 60° )= –ρA ju 2sen 60° u = vj – vs = 15 – 9 = 6 m/s

<!-- p. 129 -->
Logo: e Portanto:

Aj = πDj2 4 = π × 52 4 × 10–4 = 1,96 × 10–3 m2 ρ = γ = 8.000 = 800 kg/m 3 g 10 Fs x = 800 × 1,96 × 10–3 × 62 × (1 – 0,5) = 28,2 N Fs y = –800 × 1,96 × 10–3 × 62 × 0,866 = –49 N Fs = 28,2 2 + 492 = 56,5N Determinar a potência transmitida por um jato de água a uma turbina de ação tipo Pelton. Determinar também o rendimento da transmissão de potência. Solução Observe que o corte AA corresponde a um desviador de jato com ângulo de saída θ. Tratando-se de uma única pá, a solução seria dada pela Equação 5.7 e, pela figura, sendo apenas a metade da pá: r Fs 2 = Qmap 2 r (u1 – r u2 ) r rr ou Fs = Qmap ( u 1 – u 2 )

Projetando na direção de x:

Fs x = Qmap ( u 1 – u 2cos θ )

Supondo u 1 = u 2 = u = vj – vs , onde vs = ωR, obtém-se: Fs x = Qmap ( vj – vs ) (1 – cos θ) No caso da turbina, tem-se um grande número de pás e uma velocidade angular ω relativamente grande. Isso faz com que se possa admitir que em cada instante se tenha uma pá na posição representada na figura. Por causa disso, pode-se admitir que toda a vazão do jato é aproveitada na transmissão de potência, de forma que é possível substituir a vazão aparente pela vazão real. Logo, a equação para a turbina fica:

<!-- p. 130 -->
ou A potência é dada por: N = Fs x vs Logo:

Fsx = Qm(v j – vs )(1 – cos θ) Fsx = ρA jv j(v j – vs )(1 – cos θ )

N = ρA jv j(v j – vs )( 1 – cos θ ) vs O rendimento da transmissão de potência do jato para a turbina é obtido pela comparação da potência da turbina com a potência do jato, que é dada por (vide Exemplo do item 4.5): Nj = ρAj v3j 2 Logo, o rendimento será: ou η = N = ρAjvj ( vj – vs )(1 – cos θ) vs Nj ρAj v3j 2 η = 2(vj – vs ) vs(1 – cosθ) v2j O máximo rendimento em função da velocidade vs pode ser obtido derivando η em relação a vs e igualando a zero: dη dvs = 2 (1 – cosθ) v2j ( vj – 2vs )= 0 ou vs = vj 2 Substituindo esse resultado na expressão do rendimento:

ηmax = 2 ⎜⎛ ⎝ vj – vj 2 ⎟⎞ vj ⎠2 v2j (1 – cos θ) = 1– cos 2 θ Observa-se que o ângulo de saída θ ideal seria 180°, mas isso não é possível, pois o jato retornaria sobre si mesmo, incidindo na pá seguinte. Na prática, o ângulo θ adotado é um pouco menor que 180°.

## 5.5 Equação da quantidade de movimento para diversas entradas e saídas em regime permanente

A Figura 5.5 mostra um sistema genérico com diversas entradas e saídas.

(1e) p1e (2e) vls p2e v2s vne pne (ne) (1s) vls pls (2s) v2s p2s pns (ns) vns Figura 5.5

<!-- p. 131 -->
Nesse caso, basta generalizar a Equação 5.6, lembrando que a vazão em massa não pode mais ser colocada em evidência, já que se tem uma vazão diferente em cada seção. Logo: ∑ ∑ ∑ r r r r Fs = – pi A i n i + Qm v – Qm v (5.9) e s onde os índices e e s representam, respectivamente, entradas e saídas.

O barco da figura tem um sistema de propulsão que consiste de uma bomba que succiona água na proa e a recalca na popa. Todos os tubos têm 5 cm de diâmetro e a vazão de saída é 50 L/s. Calcular a força de propulsão no instante da partida, isto é, com o barco em repouso. Admite-se que a pressão nas entradas e saída seja praticamente atmosférica (ρ = 1.000 kg/m3).

Solução Como existem duas entradas e uma saída, deve ser aplicada a Equação 5.9:

∑ ∑ ∑ r r r r Fs = – p iA in i + Qmv – Qmv e s Pela hipótese referente às pressões, tem-se:

r r r r Fs = Qm1 v1 + Qm2 v2 – Qm3 v3 Projetando segundo x:

Fsx = Qm1 v1cos 60° – Qm2 v2cos 60° – Qm3 v3 Pela simetria do sistema: Logo: Mas, pela equação da continuidade:

Qm1 = Qm2 e v1 = v2 Fsx = 2Qm1 v1cos 60°–Qm3 v3 Qm1 = Qm3 2 e v1 = v3 2 Logo: Fs x = 2 Qm3 2 v3 2 cos 60° –Qm3 v3 e, portanto, como cos 60°= 1: 2 Fs x =– 3 4 Qm3 v3 mas Qm3 = rQ3 = 1.000 × 50 × 10–3 = 50 kg/s

<!-- p. 132 -->
e v3 = 4Q3 πD23 = 4 × π 50 × 10–3 × 0,052 = 25,46 m/s Logo: FS X = – 3 50 × 25,46 = 4 –954,7 N O sinal negativo indica que a força de propulsão tem sentido contrário ao do eixo x adotado. Determinar a força de propulsão de um foguete, supondo a pressão de saída dos gases igual à do ambiente. Solução Aplicando a Equação 5.9:

∑ ∑ ∑ r r r r Fs = p i A i n i + Qmv – Qmv e s A pressão de saída dos gases, sendo igual à do ambienrte, na escrala efetiva será nula. Além disso, o sistema só possui uma saída, não tendo nenhuma entrada; logo, Fs = –Qms vs . Projetando segundo z, tem-se: Fsz = –Qms (–vs )= Qms vs ou Fs z = ρs vs2As 5.1 Calcular o esforço horizontal sobre a estrutura do ventilador da figura e a potência transmitida ao fluido pelo 12,7 ventilador. N/m3; v1 ≅ Desprezar 0. a perda de carga entre as seções (1) e (2). Dados: D2 = 0,38 m; v2 = 30 m/s; γ =

<!-- p. 133 -->
Resp.: FSX = –133 N; N = 1,94 kW 5.2 Sabendo que a perda de carga no trecho (1)-(2) é 3 m, determinar as componentes horizontal e vertical da força aplicada pelo fluido nesse trecho de tubulação. Dados: γ = 10.000 N/m3; Q = 6 L/s. Resp.: FS X = 28 N; FS Z = 126 N 5.3 O tubo (2)-(3) da figura está ligado ao tanque por meio de uma junta elástica de borracha que impede a transferência de esforços entre o tanque e o tubo. Calcular a altura h do nível de água do tanque para que a força horizontal sobre o suporte S seja nula. Dados: g = 10 m/s2; A3 = 20 cm2; θ = 60°; p2 = 50 kPa; A2 = 80 cm2. ρ = 1.000 kg/m3; Hp1,3 ≅ 0; Resp.: h = 7,5 m 5.4 O cotovelo da figura está preso por duas luvas elásticas para que não seja influenciado pelo resto da instalação. Sendo a área de sua seção 20 cm2 e a vazão 20 L/s, qual será a força causada pelo escoamento do fluido se a perda de carga é l,0 m (ρ = 1.000 kg/m3)?

<!-- p. 134 -->
Resp.: Fs = 820 N 5.5 A turbina da figura ‘extrai’ a potência de 2,9 kW da água em escoamento. Desprezando as perdas na redução, calcular as forças exercidas pela água sobre a redução e sobre a turbina, respectivamente. Dados: ρH2O = 1.000 kg/m 3; g = 10 m/s2. Resp.: Fr = 3.740 N; FT = 243 N 5.6 Na instalação esquematizada na figura, (T) é uma turbina e o fluido que escoa é água de massa específica ρ = 1.000 N/cm2 e p2 kg/m3. A vazão que escoa é = –2 N/cm2. Desprezam-se 314 L/s e as perdas.

as pressões em Determinar:

(1) e (2) são, respectivamente, p1 = 18 a) a potência consumida pela turbina; b) o esforço segundo x que atua na base da turbina. Adotar g = 10 m/s2 e A1 = 0,0314 m2 (D1 = 0,20 m). Resp.: N = 80,7 kW; Fs x = 8.792 N 5.7 No esquema que segue, podem ocorrer duas situações: 1) o registro (B) fechado e o registro (A) aberto, a água é despejada por (1); 2) o registro (A) fechado e o registro (B) aberto, a água é despejada por (2).

Em ambos os casos, a pressão indicada na figura é a mesma, bem como se tem a mesma força F = 1.090 N, necessária para o equilíbrio segundo a direção x. Determinar, para cada uma das situações citadas, qual deve ser a força para o equilíbrio, segundo a direção y. Dados: γ H 2O = 10.000 N/m3; A0 = 100 cm2; A1 = 50 cm2; A2 = 75 cm2; g = 10 m/s2 .

<!-- p. 135 -->
Resp.: 180 N; –120 N 5.8 No trecho (1)-(2) da tubulação, que está num plano horizontal, escoa água em regime permanente. A perda de carga de (1) a (2) é 10 m e a vazão, 10 L/s. Qual é a força resultante aplicada pelo fluido na tubulação? (γ = 10.000 N/m3) Resp.: 340 N 5.9 Calcular a força horizontal aplicada sobre o suporte do bocal da figura. Sabendo que a água incide na placa, plana e vertical, e se distribui igualmente em todas as direções, calcular a força que deve ser aplicada na placa para mantê-la em repouso. Dados: p1 = 150 kPa; v1 = 5 m/s; D1 = 10 cm; D2 = 5 cm; ρ = 1.000 kg/m3. Resp.: FS X = 589 N ; FS Xplaca = 785 N 5.10 A água contida no tanque (1) é descarregada através do bocal sem atrito. Seu nível h1 pode ser considerado constante. O jato incide sobre uma placa de grandes dimensões que cobre a saída do bocal do tanque (2), contendo água a uma altura h2 acima do orifício. Os bocais são iguais. Se h2 for conhecido, determinar h1 tal que a força do jato seja suficiente para anular a resultante das forças horizontais que agem sobre a placa.

<!-- p. 136 -->
Resp.: h1 = h2/2 5.11 Calcular as componentes horizontal e vertical da força que o jato de água da figura exerce sobre o desviador. Dados: ρ = 1.000 kg/m3; Q = 20 L/s; Dj = 10 cm. Desprezar a variação da seção do jato e seu peso. Resp.: Fsx = 14,9 N; Fsy = –36 N 5.12 A água que sai de um reservatório de grandes dimensões penetra num conduto de 15 cm de diâmetro e incide sobre uma pá defletora fixa que desvia o jato de 90°, conforme a figura. Sabendo que o empuxo horizontal desenvolvido sobre a pá é 1.000 N, determinar a potência da turbina. Dados: ρ = 1.000 kg/m3; a perda de carga da tubulação é desprezível; ηT = 70%. Resp.: NT = 25,3 kW 5.13 Dado o esquema da figura, sabendo que a seção do jato tem uma área de 520 cm2 e que a área do pistão é 20 cm2, determinar a vazão ma está em equilíbrio.

no bocal. Dados: γ H 2 O = 104 N/m 3; γ Hg = 1,36 × 105 N/m 3. Observação: o siste-

<!-- p. 137 -->
Resp.: 0,233 m3/s 5.14 O bocal da esquerda tem uma área de 30 cm2 e lança um jato com velocidade de 10 m/s contra a pá. O sistema está em equilíbrio. Qual é a vazão do segundo bocal e qual é a velocidade do jato se a área do bocal é 10 cm2? (O fluido é água com γ = 104 N/m3.) Resp.: v = 10 m/s; Q = 10 L/s 5.15 Um jato atinge uma pá que se localiza num plano inclinado. O peso do conjunto é 40 N e a área do jato é 50 cm2. Qual deverá ser a velocidade do jato para que o sistema permaneça em equilíbrio? (γ = 104 N/m3) Resp: v = 2 m/s

<!-- p. 138 -->
5.16 Dados D1 = 10 cm; ρ = 1.000 kg/m3; H p0,1 = 2,8 m; D2 = 8 cm; H p0,e = 1,5 m; H ps,2 = 2,4 m; ηB = 0,70. Calcular: a) a potência no eixo da bomba para que o corpo apoiado nas rodas sem atrito permaneça parado; b) a força que o corpo exerce sobre o solo, sendo o seu peso G = 250 N. (Desprezar o peso do trecho (1)-(3) do jato.) Resp.: a) 0,26 kW; b) 376 N 5.17 O jato de água (ρ = 1.000 kg/m3) de área Aj = 10–4 m2 incide com velocidade vj na pá solidária ao carro, que se move sem atrito num plano horizontal. O carro, ao se mover, por ação do jato, reboca um bloco de peso G = 20 N sobre um plano inclinado. Se entre a base do bloco, de área 10–2 m2, e o plano inclinado existe uma camada lubrificante de óleo (μ = 0,1 N.s/m2) de espessura ε = 10–4 m, pergunta-se: qual deve ser a velocidade vj do jato em m/s para que o bloco se movimente no plano inclinado com velocidade constante v = 1 m/s? Resp.: vj = 21 m/s 5.18 O desviador de jato da figura move-se sobre o plano inclinado com velocidade de 1,0 m/s. Sabendo que seu peso é 200 N, que sua base é 1,0 m2 e que entre o desviador e o plano inclinado existe uma camada de óleo com espessura de 0,5 mm e μ = 3 × 10–2 N.s/m2, calcular a vazão de água do jato. Dados: ρ = 1.000 kg/m3; g = 10 m/s2.

<!-- p. 139 -->
Resp.: Q = 19,9 L/s 5.19 Para uma turbina de ação do tipo Pelton, tem-se os seguintes dados: raio da turbina: R = 1,5 m; rotação: 450 rpm; ângulo de saída das pás: 170°; velocidade do jato: 100 m/s; área da seção do jato: 0,1 m2. Determinar a potência da turbina. Resp.: N = 41.115 kW 5.20 Um propulsor a jato queima 1 kg/s de combustível. Calcular a força de propulsão, quando o avião voa à velocidade constante de 200 m/s. Dados: ρar= 1,2 kg/m3; ρgases = 0,5 kg/m3; A1 = 0,3 m2; A2 = 0,2 m2. Resp.: Fs x = –38.890 N 5.21 Sabendo que o sistema da figura encontra-se em equilíbrio, desprezando as perdas, determinar a altura h0. (γ H 2O = 104 N/m3; γ = 2 × 104 N/m3; Ap = 8 × 10–3 m2; h1 = 78,5 cm; Q = 15,7 L/s) Resp.: h0 = 3,2 m 5.22 Um fabricante de brinquedos constrói um carrinho impulsionado pelo ar de uma bexiga. No instante inicial em que é liberado o ar, determinar:

a) a força de propulsão; b) a pressão do ar da bexiga, desprezando a perda de carga e supondo o ar incompressível. (patm = 100 kPa)

<!-- p. 140 -->
Resp.: a) 0,35 N; b) 2.160 Pa 5.23 No tanque da figura, determinar a força Fsx que deve ser aplicada para que ele permaneça parado. Qual é o diâmetro do bocal que deverá ser instalado na parede oposta ao bocal mostrado na figura, para que a força provocada por esse novo jato venha a substituir o efeito da força Fsx? Esse novo bocal será instalado a 1 m de profundidade e admite-se que a sua perda de carga seja igual à do bocal da figura. Desprezar o atrito nas rodas. Dados: p0 = 130 kPa; ρ = 1.000 kg/m3; D2 = 10 cm; Hp0,2 = 5,5 m; g = 10 m/s2. Resp.: Fsx = 1.649 N; D = 11,1 cm

<!-- p. 141 -->

# Capítulo 6 — Análise dimensional — semelhança

## 6.1 Introdução

A solução de muitos problemas da Mecânica dos Fluidos por métodos puramente analíticos é, em geral, difícil e trabalhosa, e às vezes impossível, devido ao grande número de variáveis envolvidas. Por causa disso, desenvolvem-se métodos experimentais que permitem, nesses problemas, produzir modelos matemáticos condizentes com a realidade. A análise dimensional, como será visto, é uma teoria matemática que, aplicada à Física, e especificamente à Mecânica dos Fluidos, permite tirar maiores proveitos dos resultados experimentais, assim como racionalizar a pesquisa e, portanto, diminuir-lhe o custo e as perdas de tempo. A teoria da semelhança, ou teoria dos modelos, é baseada em princípios abordados pela análise dimensional e resolve certos problemas através da análise de modelos convenientes do fenômeno em estudo. Assim como nos outros capítulos, o objetivo não é desenvolver a teoria de forma matematicamente precisa. O que o leitor deve aproveitar são as idéias desenvolvidas, de forma a adquirir técnicas para a utilização prática da matéria.

## 6.2 Grandezas fundamentais e derivadas. Equações dimensionais

Para descrever um certo fenômeno físico, devem-se construir funções que interliguem grandezas como espaço, tempo, velocidade, aceleração, força, massa, energia cinética, trabalho etc. Após examinar esse conjunto, verifica-se que as grandezas não são independentes, isto é, grande parte delas está interligada pelas equações que descrevem as leis físicas e as definições. Assim, por exemplo, se um sistema percorre, com movimento retilíneo uniforme, 100 m em 20 s, não se pode dizer que a sua velocidade média é 10 m/s, já que, pela definição, ela deveria ser 5 m/s. Da mesma forma, se a massa de um corpo for 20 kg e a sua aceleração, 10 m/s2, a força resultante que age nele será 200 N e não outro valor qualquer, já que, pela segunda lei de Newton da dinâmica, F = ma. Uma pesquisa no conjunto de grandezas da Mecânica mostra a existência de somente três grandezas independentes, a partir das quais podem ser relacionadas todas as demais. A escolha dessas grandezas é feita de forma conveniente e o conjunto delas é chamado base completa da Mecânica. A escolha, em geral, recai no terno FLT (força, comprimento e tempo) ou MLT (massa, comprimento e tempo). Ao longo destas anotações, será preferida a base FLT.

<!-- p. 142 -->
Todas as outras grandezas que não fazem parte da base completa são ditas grandezas derivadas e podem ser relacionadas com as grandezas fundamentais por meio das equações da Mecânica. A equação monômia que relaciona uma grandeza derivada com a base completa é chamada equação dimensional. Escrever a equação dimensional da viscosidade cinemática na base FLT.

Solução Pelo Capítulo 1, a viscosidade cinemática é dada por: ν = μ ρ Por definição:

ρ= m V Na base FLT, a massa é uma grandeza derivada e deve ser relacionada com as grandezas fundamentais. A equação que permite tal relacionamento é a lei de Newton: F = ma ou m = F. a A força é uma grandeza fundamental; logo: [F] = F.

Pela Cinemática, sabe-se que a aceleração é um comprimento dividido por um tempo ao quadrado. Logo: [a] = L = LT –2 T2 Pela Geometria, sabe-se que o volume é um comprimento ao cubo: [V] = L3 Logo:

ρ= m = F V aV [ρ] = F LT –2L3 = F L4 T –2 [ρ] = FL–4 T 2 (6.1)

A viscosidade dinâmica μ pode ser obtida por:τ = μ dv dy ou μ= τ dv dy Mas τ = Ft e, portanto: [τ] = F/L2 ou [τ] = FL–2 A O gradiente da velocidade é:

⎡ dv ⎤ ⎢⎣ dy ⎦⎥ = LT –1 L = T –1 Portanto:

[μ ] = FL–2 T –1 ou [μ ] = FL–2T Nesse caso:

ν = FL–2T = F0L2T –1 FL–4 T 2 (6.2)

<!-- p. 143 -->
Esse exercício, além de mostrar a técnica de obtenção das equações dimensionais numa certa base, visou também a estabelecer as equações das grandezas ρ e μ, que serão freqüentes no estudo a seguir e nos exercícios do fim do capítulo. Até aqui, o raciocínio foi desenvolvido considerando a existência de três grandezas fundamentais, o que é verdadeiro no caso mais geral da Mecânica. Porém existem fenômenos particulares em que as grandezas fundamentais envolvidas são apenas duas. Em todos os fenômenos da Cinemática, que é a parte da Mecânica que não se preocupa com forças, serão suficientes as grandezas fundamentais L e T para relacionar todas as grandezas derivadas. Em outros campos da Física, o número poderá ser maior que três, como, por exemplo, na Termodinâmica ou no Eletromagnetismo, em que deverão ser introduzidas grandezas fundamentais que relacionem as grandezas que descrevem fenômenos térmicos ou elétricos. Fica estabelecido desde já que, no caso em estudo, o número de grandezas fundamentais será menor ou igual a três, pois todos os fenômenos serão referentes à Mecânica.

## 6.3 Sistemas coerentes de unidades

Dada a equação dimensional de uma grandeza, é fácil escrever sua unidade, desde que seja escolhido um certo sistema. Denomina-se Sistema Coerente de Unidades aquele que define somente as unidades das grandezas fundamentais. Por exemplo, um sistema que define as unidades das grandezas FLT é o MKS Técnico ou MK*S, em que: M = metro ou unidade de L K* = quilograma-força ou unidade de F S = segundo ou unidade de T Qualquer outra unidade nesse sistema será produto de potência dessas três. Por exemplo, no caso da massa específica, pela Equação 6.1, tem-se: unρ MK*S = kgf. m–4s 2 = kgf.s 2 m4 Note-se que, às vezes, para simplificar a notação, são dados nomes às unidades das grandezas derivadas de um certo sistema. Por exemplo, a unidade de massa do MK*S costuma ser chamada utm (unidade técnica de massa). Com essa notação, tem-se: unρ MK*S = utm / m3 Note-se que utm = kgf.s2 / m é apenas uma forma de simplificar a expressão das unidades, quando na definição da grandeza comparece a massa. Para efeito de transformações de unidades ou outras operações, é imprescindível lembrar a relação entre utm e as unidades das grandezas fundamentais. Aliás, tal relação é deduzida facilmente a qualquer momento pela lei da dinâmica de Newton. Outros sistemas coerentes de unidades são o Sistema Internacional (SI) e o CGS, que adotam como grandezas fundamentais o terno MLT. Para esses sistemas, a força é uma grandeza derivada. No SI, as unidades fundamentais são: metro ou unidade de L quilograma ou unidade de M segundo ou unidade de T A unidade de força é denominada Newton (N) e deve ser considerada como: m N = kg s2

<!-- p. 144 -->
No CGS, as unidades fundamentais são: C = centímetro ou unidade de L G = grama ou unidade de M S = segundo ou unidade de T A unidade de força é chamada normalmente de dina e deve ser considerada como:

dina = g ⋅ cm s2 Como esse assunto já é conhecido da Física, não se farão outras considerações sobre ele. Note-se, porém, que tal assunto deve ser de pleno conhecimento do leitor, já que as transformações de unidades dele dependem.

## 6.4 Números adimensionais

Um número é adimensional quando independe de todas as grandezas fundamentais, isto é, sua equação dimensional apresenta expoente zero em todas as grandezas fundamentais (F 0L0 T 0 ). No Capítulo 3, foi apresentado um número adimensional: o número de Reynolds. Lembre o leitor que:

vD Re = ν onde:

[v] = L = LT –1 T [D] = L Pelo exemplo resolvido anteriormente: [v] = L2 T –1 ou LT –1L [Re] = L2 T –1 = F 0L0T 0 Nota-se, então, que Re independe das grandezas fundamentais, sendo, por definição, um número adimensional. Os números adimensionais costumam ser indicados pela letra grega π e, pelo exposto, qualquer π resultará em: π = F 0L0T 0 = M 0L0T 0 Alguns deles, devido à sua importância, como, por exemplo, o número de Reynolds, receberão nomes especiais e serão apresentados por símbolos especiais (por exemplo, o número de Reynolds será indicado por Re).

## 6.5 Vantagem da utilização dos números adimensionais na pesquisa de

uma lei física A seguir será mostrada, por meio de exemplo, a vantagem do uso dos números adimensionais, no que diz respeito à economia de tempo e recursos na pesquisa de um certo fenômeno físico. O exemplo será abordado de forma qualitativa, não sendo apresentado nenhum resultado numérico. Suponhamos que se deseja determinar a força F de resistência ao avanço de uma esfera lisa mergulhada num fluido. Tal força costuma ser chamada de força de arrasto ou arraste.

<!-- p. 145 -->
O pesquisador verificou, em laboratório, que essa força depende, qualitativamente, do diâmetro (D) e da velocidade (v) da esfera, da massa específica (ρ) do fluido e de sua viscosidade dinâmica (μ) dele (Figura 6.l). Figura 6.1 Note-se que tal determinação será feita em laboratório, num túnel aerodinâmico ou num canal de provas, dependendo de o fluido ser um gás ou um líquido, respectivamente. A medida da força será efetuada por meio de um dinamômetro, ao qual serão fixadas esferas de diferentes diâmetros. As velocidades do líquido ou gás são variadas, de forma a se obter o efeito do movimento relativo entre o fluido e a esfera. A pesquisa visa a determinar F = f (D, v, μ, ρ) seja analítica ou graficamente.

Inicialmente serão fixados μ e ρ construindo F em função de D utilizando a velocidade como parâmetro. Posteriormente, deverão ser verificadas as variações da força com a viscosidade e com a massa específica. Essa determinação implica a construção de inúmeros diagramas, desde que se queira uma idéia precisa dessa variação. Em cada caso, deverá ser fixada uma massa específica e será variada a viscosidade, e vice-versa. A Figura 6.2 mostra claramente o grande número de diagramas que deverão ser construídos na pesquisa. O tempo gasto nessa construção seria enorme, além dos problemas de ordem prática provocados pela necessidade de obtenção de fluidos de massa específica fixa e viscosidade variável, e vice-versa. Figura 6.2 Diante das dificuldades dessa operação, vejamos como ela poderia ser simplificada em termos de tempo e recursos. Suponha-se a existência dos seguintes números adimensionais: π1 = F ρv 2 D 2 ρvD e π 2 = μ (número de Reynolds)

Note-se que, por enquanto, não se sabe como foram obtidos, nem se a pesquisa que faremos é válida. O que se quer é motivar o leitor para o próximo item deste capítulo, que irá garantir o processo que aqui será descrito.

<!-- p. 146 -->
O leitor já deve ter observado que, em conjunto, os dois adimensionais, π 1 e π 2 , contêm todas as variáveis da função em estudo. Vejamos agora como o uso dos adimensionais facilitaria o trabalho.

Seja uma única esfera de diâmetro D e um único fluido de massa específica ρ e viscosidade μ. Varia-se v e medem-se as variações de F no dinamômetro. Obtida uma tabela de F em função de v, pode-se tabelar π 1 e π 2 , sendo que os dois adimensionais estão interligados pela existência da velocidade em ambas as expressões. Logo, para cada π 1 existe um π 2 e será possível construir o diagrama π 1 = φ (π 2 ) (Figura 6.3). Note-se que, sendo π 1 e π 2 números adimensionais, as coordenadas de cada ponto da curva independem dos valores individuais de ρ, v, D, μ e F; dependem da combinação de todos esses valores. Assim, o fato de se ter utilizado uma única esfera e um único fluido não influirá na generalidade da pesquisa. Dessa forma, por exemplo, o ponto indicado na Figura 6.3 cujas coordenadas são π 2 = 100 ρvD e π 1 = 0,4 pode corresponder a qualquer conjunto de valores ρ, v, D e μ, desde que =100, e a qualquer combinação de F, ρ, v, D, desde que μ F ρv2 D2 = 0,4.

Cada ponto da curva da figura envolve as infinitas combinações de valores das variáveis do fenômeno. O problema da determinação da força de arrasto sobre a esfera fica assim resolvido. Vejamos um exemplo numérico baseado no ponto indicado na Figura 6.3. Figura 6.3 Determinar a força de arrasto numa esfera de diâmetro = 1 cm que se desloca em água (ρ = 1.000 kg/m3 e μ = 10–3 N.s/m2) com uma velocidade de 1 cm/s. Solução π1 = ρvD μ = 1.000 × 10–2 10–3 × 10–2 = 100 Do diagrama, para π2 = 100, tem-se: π1 = 0,4 Logo:

F = π1ρv2D2 = 0,4 × 1.000 × (10–2 )2 × (10–2 )2 F = 4 × 10–6 N O diagrama da Figura 6.3, válido para o estudo geral da força de arrasto, que age sobre uma esfera e é construído por meio de números adimensionais, chama-se diagrama universal do fenômeno. A essa altura, o leitor deve ter percebido a grande vantagem de, numa pesquisa de um certo fenômeno, trabalhar com números adimensionais que englobem as variáveis, em vez de trabalhar com elas próprias. O item seguinte, como já foi dito anteriormente, apresentará o teorema que garante a existência dos números adimensionais, ao mesmo tempo que garante o seu uso para o estudo de um certo fenômeno.

<!-- p. 147 -->
## 6.6 Teorema dos π

Será aqui apresentado o enunciado do teorema anteriormente mencionado. Não será feita a sua demonstração, se bem que ela seria útil para a construção dos números adimensionais a serem utilizados num certo fenômeno. Tal construção será indicada posteriormente por meio de regras práticas e de um exemplo. O enunciado do teorema será um pouco modificado em relação ao tradicional, já que não interessa a sua demonstração, mas somente as conclusões construtivas que dele podem ser obtidas. Teorema Seja um fenômeno físico em que intervêm n variáveis x1, x2, x3,..., xn, interligadas por uma função: f (x1, x2,..., xn) = 0. Demonstra-se que existe outra função, φ (π 1 , π 2 , ..., π m ) = 0, rigorosamente equivalente à anterior para o estudo do fenômeno indicado, onde: a) os π i são números adimensionais independentes, construídos por combinações adequadas das n variáveis ou grandezas que intervêm no fenômeno; b) a quantidade de números adimensionais é m = n – r, onde n = número de grandezas envolvidas no fenômeno e r = número de grandezas fundamentais contidas nas grandezas do fenômeno (para o nosso caso, sabe-se que r ≤ 3); c) os adimensionais são obtidos por expressões do tipo:

π1 = x α 1 1 . x α 2 2 . .. x α r r . x r +1 π1 = x β 1 1 . x β 2 2 .. . x β r r . x r +1 ………………………… πm = x δ 1 1 . x δ 2 2 . . . x δ r r . xn Note-se que, em todos os adimensionais de um certo fenômeno, os primeiros r fatores são os mesmos, com exceção do expoente. Esse conjunto de r fatores será denominado ‘base’ das grandezas envolvidas no fenômeno. As grandezas da base devem ser independentes. Para sua escolha, escreve-se a equação dimensional de todas as grandezas e seleciona-se um número r delas, de forma que cada uma difira da anterior por pelo menos uma grandeza fundamental. (Note-se que tal critério não é obrigatório, mas, se não é adotado, pode-se incorrer em erros, a menos que se faça o estudo da chamada matriz dimensional, que não será apresentada aqui.) Por exemplo, num fenômeno em que existem as três grandezas fundamentais FLT, a base pode ser constituída por: [ρ] = FL– 4 T 2 [v] = LT –1 (independe de F que comparece em ρ)

[v] = L (independe de T que comparece em v)

Nessa trinca, L é um comprimento característico do fenômeno, podendo ser um diâmetro, um raio, uma altura ou qualquer grandeza cuja equação dimensional seja L. Quando essa trinca estiver presente entre as grandezas do fenômeno, deverá ser preferida, já que a maioria dos adimensionais conhecidos tem origem nela. O último fator de cada adimensional será constituído de cada uma das grandezas não incluídas na base. A determinação dos adimensionais será mais bem esclarecida pelos dois exemplos que veremos a seguir.

<!-- p. 148 -->
1) Verificou-se em laboratório que a força de arrasto, que age numa esfera lisa que se movimenta num fluido, é dada por uma função do tipo F = f (v, D, ρ, μ). Determinar a função de números adimensionais, equivalente à função indicada. Solução O problema será resolvido em etapas que deverão ser seguidas sempre que ele for deste tipo. a) Função das grandezas que intervêm no fenômeno:

F = f (v, D, ρ, μ ) ou f1 ( F, v, D, ρ, μ ) = 0 b) Equação dimensional das grandezas que intervêm no fenômeno [F] = F [v] = LT – 1 [D] = L [ρ] = FL–4 T 2 [μ ] = FL–2T c) Número de adimensionais independentes onde: Logo:

m=n–r n = 5 (número de grandezas envolvidas no fenômeno) e r = 3 (FLT) (número de grandezas fundamentais do fenômeno) m=5–3=2 d) Escolha da base Pelo que foi indicado anteriormente, a base deve ser formada de r = 3 elementos e, pelo critério descrito, o conjunto escolhido poderia ser: F,v,D; ρ,v,D; μ,v,D etc. Somente não podem ser escolhidas trincas que contenham simultaneamente ρ e μ, que não diferem por pelo menos uma grandeza fundamental. Será escolhida a segunda trinca, como é tradicional. (Sempre que houver ρ, v e um comprimento característico, o leitor deverá dar preferência a esse conjunto como base, como foi dito anteriormente.) e) Construção de adimensionais π1 = ρα 1 vα 2 Dα 3 F π2 = ρβ 1 vβ 2 Dβ 3 μ Agora devem ser determinados os expoentes α i e β i. e-1) Determinação dos α i π1 = ρα 1 vα 2 Dα 3 F Substitui-se cada grandeza pela equação dimensional correspondente: π1 = (FL–4 T 2 )α 1 ( LT –1 )α 2 ( L )α 3 ( F )

Mas π1, pelo teorema, deverá ser um número adimensional; logo:

F0L0T 0 = Fα 1 L–4 α 1 T 2α 1 Lα 2 T – α 2 Lα 3 F ou F 0L0T 0 = F α 1 L + 1 –4 α 1 +α 2 +α 3 T 2α 1 – α 2 Igualando os expoentes de mesma base:

α1 +1= 0 –4α1 + α2 + α3 = 0 2α1 – α2 = 0 Obtém-se dessa forma um sistema de três equações a três incógnitas que resolvido resultará em: Logo:

α1 = –1; α2 = –2; α3 = –2 π1 = ρ–1v–2D–2F ou π1 = F ρv2D2 e-2) Determinação dos β i π2 = ρβ 1 vβ 2 Dβ 3 μ

<!-- p. 149 -->
Substituindo cada grandeza pela equação dimensional correspondente:

π2 = (FL–4 T 2 )β 1 ( LT –1 )β 2 Lβ 3 FL–2T Mas π2 , pelo teorema, deverá ser um número adimensional, logo: F0L0T 0 = Fβ 1 + 1L–4 β 1 + β 2 + β 3 – 2T 2β 1 – β 2 + 1 Igualando os expoentes de mesma base:

β1+1= 0 – 4β 1 + β 2 + β 3 – 2 = 0 2β 1 – β 2 + 1 = 0 Esse sistema resolvido resultará em: Logo:

β 1 = –1; β 2 = –1; β 3 = –1 π2 = ρ–1v–1D–1μ ou π2 = μ ρvD Logo, a função equivalente será:

φ ⎜⎛ ⎝ F ρv2D2 ; μ ⎟⎞ ρvD⎠ = 0 Note-se que no item servação seguinte.

6.5 foi utilizado π 2 = ρvD, μ que é o inverso de π2 aqui determinado. Cabe então a obPelo teorema, basta que a função equivalente seja construída por números adimensionais independentes formados com as grandezas envolvidas no fenômeno. Devido a esse fato, qualquer operação que for efetuada sobre os adimensionais determinados será válida desde que eles continuem adimensionais. No caso do item 6.5, foi utilizado o inverso do adimensional determinado, que continua adimensional, com a vantagem de ser o conhecido número de Reynolds. 2) A velocidade de um corpo em queda livre é função somente da aceleração da gravidade g e da altura de queda h. Determinar a função de números adimensionais referente ao fenômeno. Solução a) Função das grandezas que intervêm no fenômeno v = f (g, h) ou f1 (v, g, h) = 0 b) Equação dimensional das grandezas que intervêm no fenômeno [v] = LT –1 ; [g] = LT –2 ; [h ] = L c) Número de adimensionais independentes m=n–r com n = 3 e r = 2 (LT); então: m = 3 – 2 = 1 d) Escolha da base v, h ou g, h. Escolhe-se v, h. (A base não deve conter g, v, que não diferem por pelo menos uma grandeza fundamental.) e) Construção do adimensional π = vα 1 h α 2 g L0T 0 = (LT –1 )α 1 ( L )α 2 LT –2 L0T 0 = Lα 1 + α 2 + 1T – α 1 – 2 α1 +α2 +1= 0 –α1 – 2 = 0 Resolvendo: α1 = –2; α2 = 1 ou π = v–2hg e, portanto: π = gh v2 Note-se que, havendo um só adimensional envolvido, ele deverá ser uma constante, pois: ϕ( π) = 0, o que significa π = cte = K

<!-- p. 150 -->
v = gh K A análise dimensional não é suficiente para a determinação de K, que deverá ser determinado experimental ou analiticamente. Sabe-se nesse caso que K = 1/2. Logo: v = 2gh

## 6.7 Alguns números adimensionais típicos

Entre as grandezas que mais freqüentemente comparecem nos fenômenos da Mecânica dos Fluidos, tem-se: massa específica (ρ), velocidade característica (v), comprimento característico (L), viscosidade dinâmica (μ), variação de pressão (Δp), aceleração da gravidade (g) e velocidade do som (c). A combinação dessas grandezas, ao se adotar ρ,v,L como base, dá origem a quatro adimensionais que, devido à sua freqüente presença no estudo da Mecânica dos Fluidos, possuem nomes próprios. Verifica-se que cada um desses quatro adimensionais representa uma relação entre forças de origens diferentes, que agem no escoamento de um fluido. a) Número de Reynolds (Re)

ρvD Já foi visto que Re = μ O número de Reynolds, de uma forma mais geral, é escrito: ρvL vL Re = = μν onde L é um comprimento característico do escoamento, sem ser necessariamente um diâmetro. Chamando de Fi = ma as forças de inércia do escoamento e de Fμ = τA as forças viscosas, verifica-se a seguir o resultado da relação entre essas duas forças: Fi = ma α ρV v T Fμ τA μ v A L Com VαL3 e AαL2, tem-se:

Logo: Fi ρL3 v αT ρv 2 L2 = ρvL = Fμ μ v L2 μ v L2 μ L L Re = ρvL α Fi μ Fμ ou: O número de Reynolds é proporcional ao quociente das forças de inércia e viscosas do escoamento. Já foi visto no Capítulo 3 que o movimento em tubos é laminar quando Re < 2.000 e é turbulento quando Re > 2.400. Isso significa que as turbulências denotam um predomínio das forças de inércia sobre as viscosas, enquanto no laminar a predominância das forças viscosas não permite agitações e, portanto, acelerações das partículas.

<!-- p. 151 -->
Daqui se conclui que, quanto maior for o Re, menor será o efeito das forças viscosas no conjunto de forças que agem no fluido. Nessas condições, o número de Reynolds caracterizará, nos fenômenos, o efeito da viscosidade comparativamente com outros efeitos. Conclui-se que valores muito elevados do número de Reynolds representam um efeito desprezível da viscosidade no fenômeno em estudo. b) Número de Euler (Eu) O número de Euler é dado por: Δp Eu = ρv2 = ΔpA ρv2 A α F ρv2 L 2 (6.3)

O número de Euler ou coeficiente de pressão indica a relação entre as forças de pressão (Fp ) e as forças de inércia no escoamento de um fluido. O Eu comparece no estudo de escoamentos em torno de perfis, em tubos, em máquinas hidráulicas etc. No estudo do escoamento em volta de objetos imersos, em movimento relativo com o fluido, costuma-se usar o adimensional: Ca = Fa 1 ρv2 A 2 (6.4)

que é proporcional ao número de Euler, já que L2 representa uma área.

Esse adimensional é chamado ‘coeficiente de arrasto’ e Fa será a força de arrasto ou força de resistência ao avanço de uma superfície sólida que se desloca num fluido. c) Número de Froude (Fr)

v2 Fr = Lg (6.5)

Representa a relação entre as forças de inércia e as forças devidas à aceleração da gravidade. É importante em escoamentos onde há superfícies livres com possibilidade de formação de ondas. São casos desse tipo: ação das ondas em flutuantes, escoamento em canais, escoamento em vertedores, em orifícios etc. d) Número de Mach (M) M= v (6.6) c onde c é a velocidade do som no fluido em escoamento.

Esse adimensional comparece quando os efeitos de compressibilidade do fluido são importantes. O M permite classificar os escoamentos em subsônicos (M < 1), sônicos (M = 1) e supersônicos (M > 1) de características diferentes qualitativa e quantitativamente. (Ver Capítulo 12.)

## 6.8 Semelhança ou teoria dos modelos

Devido ao grande número de variáveis envolvidas, é normalmente impossível a determinação de todos os resultados numéricos referentes a um certo fenômeno da Mecânica dos Fluidos, por via puramente analítica. Uma das formas de simplificar as pesquisas é a construção de um modelo em escala que simula as condições do fenômeno em escala real, que será chamado protótipo.

<!-- p. 152 -->
Para que os resultados das grandezas medidas no modelo tenham valor prático em relação ao protótipo, certas condições deverão ser cumpridas. Tais condições são: a) entre modelo e protótipo deve existir semelhança geométrica, isto é, o modelo e o protótipo poderão ter dimensões diferentes, mas devem ter o mesmo formato. As suas dimensões correspondentes deverão ser proporcionais; b) entre modelo e protótipo deve existir semelhança cinemática, isto é, as velocidades das partículas de fluido homólogas deverão manter uma relação constante (Figura 6.4); Figura 6.4 Note-se que, daqui em diante, o índice m denotará modelo e o índice p, protótipo. c) entre modelo e protótipo deve existir semelhança dinâmica, isto é, as forças que agem em pontos homólogos deverão manter relações constantes. Para que todas essas condições sejam obtidas, verifica-se que os adimensionais referentes ao protótipo devem ser iguais aos respectivos adimensionais referentes ao modelo. Se, por construção, essa igualdade é conseguida, diz-se que o fenômeno referente ao protótipo e o referente ao modelo mantêm uma semelhança completa. Note-se que nem sempre isso é possível e depende da experiência do pesquisador de associar ao protótipo os resultados obtidos no modelo.

## 6.9 Escalas de semelhança

Chama-se escala de semelhança a relação entre uma grandeza referente ao modelo e a mesma grandeza referente ao protótipo. As escalas de semelhança serão indicadas pelo símbolo K.

Por exemplo: KL =Lm Lp escala geométrica Kv = vm vp escala das velocidades Kμ = μm μp escala das viscosidades ou, genericamente:

Kx = xm xp onde x representa uma grandeza física qualquer referente ao fenômeno.

## 6.10 Relações entre escalas

Foi visto que, para que modelo e protótipo mantenham semelhança completa, é necessária a igualdade dos respectivos números adimensionais. Tal igualdade conduz a relações entre escalas que deverão ser observadas para que os resultados referentes ao modelo te-

<!-- p. 153 -->
nham significado para o protótipo. A seguir serão determinadas essas relações quando Re, Eu e Fr forem adimensionais característicos do fenômeno. a) Re m = Re p ρ m v m L m = ρ p v pL p ou μ m = ρ m v mL m μm μp μ p ρpvpL p Logo: b) Eu m = Eu p K μ = K ρK vK L Fm ρ m v 2 m L 2 m = ρ Fp p v 2 p L 2 p ou Fm Fp = ρ m v 2 m L 2 m ρ p v 2 p L 2 p (6.7) Logo: c) Frm = Frp KF = K ρK 2 v K 2 L v 2 m = v 2 p Lmgm L pgp ou v 2 m v 2 p = Lmgm L pg p (6.8) Logo: K 2 v =KLKg (6.9)

Note-se que, em geral, K g = 1 para fenômenos realizados na Terra, pois a aceleração da gravidade varia muito pouco de um local para outro. 1) Quer-se determinar a força de arrasto que age no ‘sonar’ de um submarino por meio de testes efetuados com um modelo na escala l:5. Os testes são realizados em água a 20°C, a uma velocidade de 60 km/h, e a força de arrasto medida é 30 N. Sabendo que o protótipo será utilizado em água a 4,0°C, calcular a velocidade do submarino em condições de semelhança completa e, nessas condições, determinar a força de arrasto correspondente. Solução Como o escoamento realiza-se sobre um corpo totalmente submerso, o número de Froude não influirá no fenômeno, conforme já foi dito anteriormente; logo, sendo desprezíveis os efeitos da gravidade mediante as forças viscosas e de arrasto, a função representativa do fenômeno será: que leva a f (ρ, v, L,μ , Fa )= 0 φ ( Re, Eu) = 0 Note-se que poderia ter sido usado o coeficiente de arrasto em vez do número de Euler. A função de números adimensionais nos levará às equações 6.7 e 6.8. De uma tabela, devem ser determinadas as propriedades da água a 20°C e 4°C.

ρH2O(20o C ) = ρm = 1.000 kg/ m 3 ≅ ρH2O( 4o C )

μ H2 O(20o C ) = 10–3 N. s m2 μ H2 O( 4o C )= 1,58 × 10–3 N. s m2 Pela Equação 6.7:

Kμ = Kρ KvKL

<!-- p. 154 -->
Logo: ou 10–3 1,58 × 10–3 = 1× Kv × 1 5 ou Kv = 5 1,58 = 3,16 vm = 3,16; vp logo: vp = 60 3,16 ≅ 19 km /h Logo, em condições de semelhança completa, o sonar, fixo ao submarino, deverá se deslocar com uma velocidade de aproximadamente 19 km/h ou 5,28 m/s. Pela Equação 6.8: Portanto:

KF = Kρ K2vK2L KF = 1× (3,16)2 × ⎜⎛⎝ 1 5 ⎟⎠⎞ 2 = 0,4 Mas KF = Fm Fp = 0,4 ou Fp = 30 0,4 = 75 N A força de arrasto no sonar real será de 75 N.

2) Um modelo de navio, na escala 1:100, é testado em laboratório. O protótipo tem 100 m de comprimento. Para uma velocidade que corresponde a 10 m/s no protótipo, a força de arrasto medida no modelo é 10 N. Supor que, no teste do modelo, a água é igual àquela em que navegará o protótipo. Qual é a velocidade de teste do modelo e a força de arrasto no protótipo? Solução Diferentemente do exemplo anterior, como o navio se desloca na superfície livre, os efeitos da força de gravidade não são desprezíveis. Logo, para o estudo do fenômeno, deve-se considerar a seguinte função: f (ρ, v, L, μ, g, F) = 0 que originará a seguinte função de números adimensionais: φ (Re, Fr, Eu) = 0 A igualdade dos adimensionais referentes a modelo e protótipo levará ao uso das equações 6.7, 6.8 e 6.9. Pela Equação 6.7: e como então ou Pela Equação 6.9: ou Kμ = Kρ KvKL μ m = μ p; ρm = ρp 1 = 1× Kv × KL Kv = 1 KL = 100 Kv2 = KL Kg Kv = 1 =1 100 10 (mesmo fluido) (1)

(2)

Note-se que (1) e (2) são incompatíveis.

Uma das formas de corrigir esse fato seria trabalhar no modelo com um fluido diferente do fluido do protótipo. Isto é, adotando (2) como verdadeira, a (1) fica: Kμ = Kρ × 1 10 × 1 100 Kμ = 1 ou μ m × ρp = 1 Kρ 1.000 μ p ρm 1.000 Nem sempre é possível obter na prática um fluido que obedeça a tal relação e, quando possível, o processo pode ser impraticável. O que se costuma fazer é abandonar uma das duas condições, (1) ou (2), não sendo possível manter a semelhança completa.

<!-- p. 155 -->
Comumente abandona-se a condição imposta pelo número de Reynolds ou, em outras palavras, não se considera o efeito da viscosidade. Note-se que se o Re for muito grande, tanto no modelo como no protótipo, o erro introduzido será desprezível, já que se verificou que esse fato implica forças viscosas pequenas, comparativamente com outras forças do escoamento. O abandono de uma das condições de semelhança completa introduz o chamado efeito de escala, isto é, os resultados obtidos para o protótipo, através das medidas no modelo, não são de semelhança completa, trazendo um desvio em relação à realidade. Em geral, ou esse desvio é desprezível ou o pesquisador deverá utilizar processos apropriados para cada experiência, que minimizem o efeito de escala. Através do exemplo, será verificado que ao abandonar a condição (1), que corresponde a desprezar o efeito das forças viscosas, o erro é pequeno, pois o efeito da viscosidade é realmente desprezível em face de outros efeitos. Pela (2): Kv = 1; 10 logo, vm = 1 ou vp 10 vm = 10 10 Portanto: vm = l m /s Pela Equação 6.8:

KF = Kρ K2vKL2 ou KF = 1× ⎜⎛⎝ 1 10 ⎟⎠⎞ 2 × ⎝⎛⎜ 1 100 ⎞⎠⎟ 2 de onde KF = 1 106 ou Fm = 1 Fp 106 Logo:

Fp = 10 × 10–6 = 107 N De posse dos resultados finais, serão calculados os números de Reynolds do modelo e do protótipo e será verificado se o efeito de escala afetará tais resultados.

Re m = ρmvmLm μm = 1.000 × 1× 10–3 1 = 106 (turbulento) Re p = ρpvpLp μp = 1.000 × 10 × 10–3 100 = 109 (turbulento)

Pelos valores calculados e lembrando o significado de Re, conclui-se que, para o modelo nas condições do ensaio e para o protótipo nas condições de utilização, o efeito da viscosidade é desprezível. Tal não aconteceria se, por exemplo, Rem = 1.000 (laminar); então as forças viscosas no modelo não seriam desprezíveis e o erro nos resultados obtidos seria grande. Nesse caso, seria possível, por exemplo, aumentar o tamanho do modelo para reduzir o efeito de escala. 3) Uma bomba centrífuga é acionada por um motor que gira a 1.800 rpm e fornece 3 L/s quando a carga manométrica é 18 m. Determinar suas características quando o motor gira a 1.500 rpm. Solução Numa bomba centrífuga, as grandezas características interligam-se na função:

f (ρ, n, D,μ ,Q, γHB )= 0 onde n = rotação da bomba D = diâmetro do rotor da bomba Q = vazão em volume HB = carga manométrica γHB = variação total de pressão entre a entrada e a saída da bomba. Adotando-se como base [ρ] = FL–4 T 2; [n ] = T –1; [D] = L e aplicando-se o teorema dos π, obtêm-se os seguintes números adimensionais:

Re = nD2 (número de Reynolds) ν

<!-- p. 156 -->
φ= Q nD3 (coeficiente de vazão)

Ψ = gHB (coeficiente manométrico) n 2D2 Note-se que o Re está ligeiramente modificado, mas deve ser lembrado que até agora a base adotada sempre foi ρ,v,L, enquanto neste problema é ρ,n,L (onde L = D). Nas bombas centrífugas, geralmente, o efeito da viscosidade é pequeno e o número de Reynolds pode ser abandonado, ficando-se com: Ψ = f (φ)

Pela condição de semelhança:

Ψm = Ψp Kg KH = Kn2KD2 φm = φp KQ = KnK3D Note-se que no problema a bomba é a mesma; logo, KD = l. Tem-se, então: 1× KH = K2n × 1 KQ = Kn × 1 mas Kn = 1.800 1.500 = 1,2 Logo: KQ = Qm Qp = 1,2 e Qp = 3 1,2 = 2,5 L/ s Assim, a vazão da bomba na nova rotação será 2,5 L/s.

e ainda KH = H Bm H Bp = (1,2)2 e H Bp = 18 1,44 = 12,5 m A nova carga manométrica será de 12,5 m.

6.1 Determinar nas bases FLT e MLT as equações dimensionais das seguintes grandezas: área, volume, aceleração, massa, força, massa específica, peso específico, pressão, tensão de cisalhamento, vazão em volume, vazão em peso, vazão em massa, viscosidade dinâmica, viscosidade cinemática, momento, trabalho e potência. 6.2 A carga manométrica de uma bomba centrífuga depende da vazão Q, da massa específica ρ e da viscosidade dinâmica μ do fluido, do diâmetro D do rotor e da rotação n. Determinar os adimensionais característicos da bomba. Função representativa: f (ρ, n, D,μ ,Q, γΗ B ) = 0.

Resp.: Re = nD2 ; ν φ = Q nD3 ; Ψ = gH B n 2D2 6.3 A pressão efetiva p, num ponto genérico de um líquido em repouso, é função da massa específica ρ, da aceleração da gravidade g e da profundidade do ponto h em relação à superfície livre do líquido. Determinar a equação das pressões. Resp.: p = Cρgh 6.4 Determinar uma expressão para o período de oscilação de um pêndulo simples, de comprimento l, que oscila com amplitude reduzida devido unicamente à ação da gravidade. Resp.: T = C l g

<!-- p. 157 -->
6.5 A vazão Q de um líquido ideal que escoa para a atmosfera através de um orifício de bordo delgado, praticado na parede lateral de um reservatório, é função do diâmetro D do orifício, da massa específica ρ do fluido e da diferença de pressão entre a superfície livre e o centro do orifício. Determinar a expressão para a vazão. Resp.: Q = CD2 p ρ 6.6 A velocidade v com que o fluido atravessa o vertedor triangular da figura é uma função da aceleração da gravidade g e da altura h da superfície livre do líquido em relação ao vértice do triângulo. Determinar a expressão para a vazão. Resp.: Q = Cg1 /2 h 5 /2 6.7 A potência fornecida a um líquido por uma bomba centrífuga é função do peso específico γ do líquido, da vazão em volume Q e da altura manométrica HB da bomba. Determinar a equação da potência NB. Resp.: NB = C γ Q HB 6.8 Em muitos fenômenos estudados pela Mecânica dos Fluidos comparecem as seguintes grandezas características: ρ, v, L, μ, F, g, c. Determinar os números adimensionais que podem ser formados com essas grandezas. (L = comprimento característico; c = velocidade do som.) Resp.: Re, Fr, Eu, M (vide item 6.7).

6.9 Sabe-se que o empuxo F devido à hélice de um avião é função de sua velocidade v em relação ao ar, da velocidade angular ω da hélice, do diâmetro D da hélice, da massa específica ρ, da viscosidade dinâmica μ do ar e da velocidade c do som. Determinar a função de adimensionais equivalente à função representativa do fenômeno físico. Resp.: φ ⎛ ⎜ ⎝ F ρv2D2 , ρvD μ , v c , v⎞ ωD ⎟⎠ =0 6.10 A força resultante F, exercida por um fluido sobre um perfil de asa de comprimento característico L, depende da massa específica ρ e da viscosidade dinâmica μ do fluido, da velocidade v do perfil em relação ao fluido e do ângulo de ataque α. Determinar a função de adimensionais equivalente.

<!-- p. 158 -->
Resp.: φ ⎛F ⎜ ⎝ ρv2 L2 , ρvL μ ,α ⎟⎞ ⎠ =0 6.11 Um modelo de avião é construído na escala 1:10. O modelo decola à velocidade de 50 km/h. Desprezando o efeito da viscosidade dinâmica, calcular a velocidade de decolagem do protótipo e a escala de resistência oposta ao movimento. Dado: f (F, v, L, ρ, μ, g) = 0. Resp.: vp = 158 km / h; KF = 1 1.000 6.12 Água à temperatura de 20°C escoa por um conduto horizontal, cilíndrico, de seção circular (D = 75 mm), com uma velocidade média de 3,2 m/s. Entre duas seções distantes uma da outra 20 m, a perda de pressão é 20 kPa. Com que velocidade deve escoar benzeno, à mesma temperatura, através do mesmo conduto, para que a perda de pressão, entre as mesmas seções, seja a mesma? Dados: μ meno: f ( ΔHp2 O, (20o C) = ρ, v, D, 9,8 × μ) = 10 0. –4 N. s/m 2 ; μ ben(20o C) = 6,4 × 10–4 N. s/m 2. Função representativa do fenôResp.: vp = 4,9 m / s 6.13 Uma hélice de 6 m de diâmetro desloca um barco com a velocidade de 7,5 m/s, quando gira a 120 rpm. Constrói-se um modelo geometricamente semelhante do casco e da hélice na escala 1:10 para a determinação da força de tração axial. Determinar a velocidade do modelo, a rotação da hélice do modelo e a escala das forças. Dado: f (ρ, v, D, n, g, F) = 0. Resp.:

vm = 2,37 m /s; n m = 379 rpm; KF =1 1.000 6.14 É necessária a força de 15 N para rebocar uma placa de 1,5 m de comprimento por 15 cm de largura, totalmente submersa em um tanque de água, à velocidade de 6 m/s. Que dimensões deverá ter uma placa semelhante para que, rebocada no ar à velocidade de 30 m/s, se verifique semelhança completa? Nessas condições, que força é necessária para manter a placa em movimento? Dados: ρH2O = 1.000 kg/ m 3; νH2O = 10–6 m 2/ s; ρar = 1,2 kg/ m 3; νar = 10–5 m 2/ s. Função representativa do fenômeno: f (F, v, L, ρ, μ) = 0. Resp.: 3 m × 30 cm; F = 1,8 N 6.15 As duas bombas da figura são geometricamente semelhantes e apresentam o mesmo regime dinâmico de escoamento. Sabe-se que a bomba B1 tem vazão Q = 5 L/s, carga manométrica HB = 25 m, rotação n = 1.200 rpm e diâmetro do rotor D = 20 cm. Determinar a rotação da bomba B2 e sua carga manométrica, sabendo que o seu diâmetro é D = 15 cm. Resp.: nB2 = 2.844 rpm; H m B2 = 79 m.

<!-- p. 159 -->
6.16 Dado o diagrama Eu = φ (Re), que caracteriza a queda de pressão no escoamento de um fluido ao longo de um trecho de um conduto cilíndrico de diâmetro D = 5 cm, calcular a viscosidade cinemática de um fluido de peso específico γ = 8.000 N/m3 que sofre uma queda de pressão de 49,2 kPa quando se desloca no mesmo conduto, com velocidade de 2,4 m/s. Re 100 500 1.000 1.500 2.000 Eu 128 25,6 12,8 8,5 6,4 Resp.: ν = 9,6 × 10–5 m2 / s 6.17 Uma esfera totalmente submersa em um líquido movimenta-se em um plano horizontal com uma velocidade v1, sendo necessária uma força F1. Essa força foi medida para diversas velocidades, obtendo-se os dados da tabela a seguir. Se outra esfera totalmente submersa, de diâmetro D2 = 50 cm, movimenta-se no mesmo fluido com kg/m3; μ = 10–3 N. s / m velocidade v2 = 3 m/s, qual será a 2. Função representativa: f (F, ρ, v, força D, μ)

necessária? = 0.

Dados: D1 = 20 cm; ρ = 1.000 V1 (m/s) 2 4 6 8 10 F1 (N) 40 100 180 300 450 Resp.: 270 N 6.18 No teste de um modelo num tanque de provas, verificou-se que as grandezas que intervêm no fenômeno são: v, g, L, ν. O protótipo vai trabalhar em água a 20°C, de viscosidade cinemática ν = 10–6 m 2/s. Sabe-se que a escala de semelhança geométrica é: KL = Lm Lp = 1. 2 Escolher entre os fluidos a seguir aquele em que deve ser feito o teste para se obter semelhança completa:

Fluido água a 20°C água a 50°C água a 90°C mercúrio gasolina querosene ν( m 2/s) 10–6 7 × 10–7 3,54 × 10–7 1,25 × 10–7 5,12 × 10–7 3,1× 10–6 Resp.: Água a 90°C.

6.19 Num certo fenômeno, a função representativa é: f (N, g, ρ, v, L) = 0, onde N = potência, g = aceleração da gravidade e L = comprimento característico. Ao determinar os adimensionais pelo teorema dos π e efetuando uma série de experiências em laboratório, chegou-se ao gráfico indicado a seguir. Se numa certa experiência obtém-se ρ = 1.000 kg/m3, v = 2 m/s, L = 0,5 m e g = 10 m/s2, qual será a potência em kW? Adotar como base ρ,v,L. Resp.: N = 2,5 kW

<!-- p. 160 -->
6.20 Num certo fenômeno físico, as forças viscosas e da gravidade são dominantes. O protótipo funciona com um fluido de viscosidade cinemática ν = 4,8 × 10–5 m2/s. Se a escala geométrica é 1:4, qual deve ser a viscosidade do fluido utilizado no teste do modelo para que haja semelhança completa? Justificar tudo o que for adotado. Resp.: ν = 6 × 10–6 m2/s 6.21 A figura mostra o esboço de uma bomba centrífuga vista em corte. Numa bomba centrífuga, a carga manométrica aumenta ao dificultar a passagem do fluido, isto é, a vazão. Isso significa que a mesma bomba, em diferentes instalações hidráulicas, pode fornecer vazões e cargas manométricas diferentes, dependendo da dificuldade criada ao escoamento do fluido. A figura mostra a curva característica HB = f (Q) de uma bomba centrífuga, cujo diâmetro do rotor brando que os adimensionais característicos de uma bomba é 15 são cm φ= e cuja rotação é Q e Ψ = gH 3.500 rpm. LemB , já que, em genD3 n 2D2 ral, o efeito da viscosidade é desprezível e, portanto, não há necessidade levar em conta Re, determinar: a) a curva universal para todas as bombas semelhantes à bomba dada; b) a curva característica HB = f (Q) de uma bomba semelhante à dada, que tenha o dobro do diâmetro e a metade da rotação. 6.22 Dois barcos geometricamente semelhantes são arrastados por dois rebocadores. O barco A é arrastado a uma velocidade de 9 m/s e oferece uma resistência ao arrasto de 105 N. Sendo o segundo barco três vezes menor, qual deverá ser a sua velocidade para que haja semelhança completa e qual resistência ele irá oferecer ao arrasto? (Observação: desenvolver os adimensionais, dada a função que caracteriza o fenômeno: f (F, ρ, v, L, g) = 0.) Resp.: vB = 5,2 m/s; FB = 3.700 N 6.23 No sistema da figura estão instaladas duas bombas semelhantes. Numa situação, a bomba B1 está ligada, a válvula V1, aberta, e a válvula V2, fechada, sendo as perdas de carga Hp1,8= 3 m; Hp9,5= 3 m; H p5,7 = 4 m. Em outra situação, a bomba B2 está ligada, a válvula V2, aberta, e a válvula V1, fechada, sendo as perdas de carga H p1,3 = 1 m; H p4,5 = 3 m , e a perda de carga de 5 a 7 é a mesma que a da situação anterior. Sendo a rotação da bomba B1 = 3.450 rpm, qual será a rotação da bomba B2? Dados : Ψ = gH B ; φ = Q n 2D2 nD3 Resp.: 3.158 rpm

<!-- p. 161 -->
6.24 Uma indústria necessita, para o recalque de óleo (γ = 8.500 N/m3), de uma bomba que forneça uma carga manométrica de 100 m quando funciona com uma rotação de 1.750 rpm. Para análise dessa bomba, dispõe-se da curva característica de uma bomba geometricamente semelhante, três vezes menor que a anterior, que foi ensaiada com água na mesma rotação. Sendo o diâmetro do rotor da segunda bomba 100 mm, determinar: a) a vazão de óleo que poderá ser recalcada pela primeira bomba na condição estabelecida; b) o rendimento da primeira bomba, se a potência dissipada nela é 23,5 kW.

Resp.: a) 91,8 L/s; b) 0,768 6.25 Num canal de provas são realizados ensaios de determinação da força de resistência ao avanço, numa esfera de 20 cm de diâmetro, utilizando água. Após vários ensaios, foi construído o diagrama Eu = f (Re) dado a seguir. Se uma esfera de diâmetro = 5 cm cai livremente em ar (νar = 10–5 m2/s; γar = 10 N/m3), qual é a força de resistência ao avanço na condição em que o efeito das forças viscosas começa a se tornar desprezível? Dado: função representativa do fenômeno: f (F, ρ, v, D, μ) = 0.

Resp.: 0,75 N 6.26 Um recipiente, contendo um gás (ρ = 1,2 kg/m3), tem um orifício por onde ele é descarregado para o ambiente. O gás pode ser considerado incompressível. Após algumas observações, conclui-se que a vazão em volume (Q) é função da diferença de pressão com o ambiente( Δp ), da viscosidade cinemática (ν), da massa específica (ρ) e do diâmetro do orifício (D). a) Determinar π1 e π2 , sendo π1 = f (base) × Q e π2 = f (base) × Δp. b) Verificou-se que, para Q = 0,2 × 10–3 m3/s, obtem-se Δp = 100 kPa, e que diâmetro do orifício em milímetros.

π1 = 2 × 10–2. Determinar o π2 Resp.: 5,9 mm

<!-- p. 162 -->
6.27 Num fenômeno, a função representativa é dada por f (QG, g, γ, v, L, μ) = 0 (QG = vazão em peso; L = comprimento característico). Ao determinar os adimensionais pelo teorema dos π, usando a base γ,v,L, sendo π1 = f (QG), π2 = f (g) e π′3 = 1/π3 = f (μ), obteve-se o gráfico a seguir. a) Determinar as equações dimensionais de todas as grandezas. b) Determinar os números adimensionais. c) Numa certa experiência, γ = 104 N/m3, v = 10 m/s, L = 5 m, g = 10 m/s2, μ = 10–3 N.s/m2 . Qual é a vazão em peso em N/s? d) Pode-se afirmar que o efeito da viscosidade é desprezível? Em que condições? e) Se os dados do item (c) correspondem a um modelo, qual é a escala das vazões em peso com um protótipo que é ensaiado com o mesmo fluido e que tem escala geométrica 1/16? Resp.: c) 1.500 N/s; e) 1/1.024 6.28 A potência (N), necessária para o acionamento de um barco, é função de ρ,v,g,L = comprimento da linha d’água e Afr = área frontal submersa. O barco deve se deslocar com uma velocidade de 36 km/h. a) Determinar os adimensionais necessários ao estudo da semelhança com um modelo na escala 1/100. b) Qual deve ser a velocidade de ensaio do modelo em água, para conseguir semelhança completa? c) Qual é a potência necessária em kW para deslocar o barco na velocidade dada, se no laboratório mediu-se uma força no modelo de 0,75 N? Resp.: b) 3,6 km/h; c) 7.500 kW

<!-- p. 163 -->

# Capítulo 7 — Escoamento permanente de fluido incompressível em condutos forçados

z Escoamento permanente de fluido incompressível em condutos forçados z 163

## 7.1 Introdução

No Capítulo 4 foi visto que a equação da energia, dentro de hipóteses convenientes, reduz-se a: H1 + H M = H 2 + H p1,2 (7.1)

em que o significado das parcelas foi amplamente explicado naquele capítulo.

Muitos dos problemas referentes a instalações hidráulicas recaem nas hipóteses de validade da Equação 7.1 e visam à determinação de uma de suas parcelas, devendo, portanto, ser conhecidas as outras três.

Não se deseja que o leitor faça disso uma regra, pois outros casos acontecem, mas muitas vezes a incógnita nos problemas é o termo HM (carga manométrica da máquina) que, como apresentado, é utilizado no cálculo de sua própria potência. Nesse caso, normalmente, H1 e H2 são conhecidos pelo projetista, pela própria configuração da instalação e pelas condições que lhe são impostas, como, por exemplo, a vazão disponível ou necessária para uma certa aplicação.

Restaria, nesse caso, conhecer o termo Hp1,2 (perda de carga), para que, por meio da Equação 7.1, fosse possível determinar HM. O objetivo deste capítulo é exatamente estabelecer métodos para a determinação da perda de carga e com isso resolver a Equação 7.1, qualquer que seja a incógnita prefixada pelo projeto. O estudo do Capítulo 7 implica, mais do que qualquer outro, a necessidade de conhecimento de todos os outros já estudados, devendo o leitor reportar-se a eles sempre que necessário.

## 7.2 Definições

Neste item serão introduzidas definições e conceitos utilizados ao longo do capítulo. Prefere-se apresentá-los inicialmente para não interromper a seqüência nos itens posteriores, onde forem necessários.

### 7.2.1 Condutos – Classificação

Conduto é qualquer estrutura sólida, destinada ao transporte de fluidos. Os condutos são classificados, quanto ao comportamento dos fluidos em seu interior, em forçados e livres.

<!-- p. 164 -->
O conduto é dito forçado quando o fluido que nele escoa o preenche totalmente, estando em contato com toda a sua parede interna, não apresentando nenhuma superfície livre (Figura 7.1a). O conduto é dito livre quando o fluido em movimento apresenta uma superfície livre (Figura 7.1b).

### 7.2.2 Raio e diâmetro hidráulico

Raio hidráulico (RH) é definido como: A RH = σ onde:

A = área transversal do escoamento do fluido; σ = perímetro ‘molhado’ ou trecho do perímetro, da seção de área A, em que o fluido está em contato com a parede do conduto. Diâmetro hidráulico (DH) é definido por: DH = 4RH A tabela a seguir apresenta alguns exemplos:

Figura 7.1 (7.2) (7.3)

### 7.2.3 Camada limite numa placa plana

A noção de ‘camada limite’ será muito útil ao longo deste capítulo, como será visto durante o seu desenvolvimento.

<!-- p. 165 -->
Esse conceito é mais facilmente introduzido no escoamento de fluidos sobre placas planas do que no escoamento em condutos. Por causa disso, neste item será feito o estudo da camada limite sobre placas planas e essa noção será aproveitada no próximo item para o estudo do mesmo fenômeno no escoamento em condutos. Figura 7.2 Seja uma placa plana de espessura muito pequena, introduzida paralelamente a um escoamento uniforme e em regime permanente de um fluido. Seja a velocidade do fluido, ao longe da placa, uniforme de valor v0. Os acontecimentos serão explicados para um dos lados da placa, sendo que do outro o aspecto será simétrico. Suponha-se que, por meio de um medidor, sejam detectadas as velocidades nos pontos ao longo de uma seção vertical (1) (Figura 7.2). Ao fazer isso, verifica-se que junto à placa, devido ao princípio da aderência, a velocidade é nula. Quando se percorre a vertical (1), a velocidade é crescente até que, num ponto A, a velocidade coincida com v0 e assim se mantenha para todos os pontos acima dele. É óbvio que o fluido até o ponto A sofreu a influência da presença da placa, influência esta que é denotada pela existência de um gradiente da velocidade ao longo da vertical. Acima do ponto A, o fluido comporta-se como se a placa não existisse, isto é, escoa com a mesma velocidade v0 uniforme que ele possuía ao longe. Se a mesma experiência for efetuada ao longo de verticais mais afastadas do bordo de ataque, como a (2) e a (3), verifica-se uma repetição daquilo que aconteceu na (1), com a única diferença de que os pontos (B) e (C), que denotam o fim da variação da velocidade, estarão mais afastados da placa. Se isso for realizado em diversas verticais, verifica-se que os pontos do tipo A, B e C pertencem a uma linha que será o lugar geométrico dos pontos a partir dos quais a velocidade passa a ter valor v0 constante ao longo de cada vertical (Figura 7.3). Figura 7.3 O fluido fica dividido, por essa linha, em duas regiões distintas. Uma em que as velocidades são menores que v0 devido à presença da placa e outra em que a velocidade é v0, não sendo influenciado o escoamento nessa região pela presença da superfície sólida.

<!-- p. 166 -->
A região entre a placa e a linha construída chama-se ‘camada limite’, enquanto a região acima dela chama-se ‘fluido livre’. Note-se que a espessura l da camada limite é crescente ao longo da placa e pode-se verificar que é função do parâmetro adimensional: Re x = ρv0 x μ = v0x ν que nada mais é que uma forma do número de Reynolds, como foi visto no Capítulo 6. Logo: l = f (Rex). Verifica-se que, para Re x < 5 × 105, as forças viscosas na camada limite são consideráveis, comparativamente com as de inércia, sendo o escoamento, dentro da camada limite, do tipo laminar.

Quando o Rex ultrapassa esse valor, o escoamento na camada limite passa para turbulento. Para um dado fluido, com uma certa velocidade v0, a passagem para escoamento turbulento acontecerá numa abscissa chamada crítica, correspondente ao valor do número de Reynolds de 5 × 105, também chamado crítico. Re cr = ρv 0 x cr μ = 5 ×105 Pela expressão acima, pode-se determinar a abscissa da placa, em que acontece a passagem do movimento laminar para turbulento dentro da camada limite, pois: 5 ×105 μ x cr = ρv 0 Isso acontecerá sempre que o comprimento da placa for maior que xcr. A passagem de camada limite laminar para camada limite turbulenta é facilmente observável pelo crescimento repentino de sua espessura, como se observa na Figura 7.4. Tal crescimento se deve ao próprio conceito de movimento turbulento, em que, sendo pequeno o efeito das forças viscosas, o efeito da presença da placa transmite-se a uma maior distância dentro do escoamento do fluido. Apesar de o movimento, para uma abscissa x > xcr, ser turbulento no interior da camada limite, numa camada de espessura δ muito pequena, junto à placa, devido às baixas velocidades, subsiste um movimento do tipo laminar. Essa região denomina-se ‘subcamada limite laminar’. Figura 7.4 O conceito de camada limite laminar e turbulenta e o de subcamada limite laminar serão de grande utilidade na explicação de fenômenos que serão apresentados nos itens seguintes.

<!-- p. 167 -->
### 7.2.4 Desenvolvimento da camada limite em condutos forçados

Seja o conduto de descarga de um tanque (Figura 7.5). Antes de o fluido penetrar no conduto, sendo o tanque de grandes dimensões, terá uma velocidade uniforme. Ao penetrar no tubo, pelo princípio da aderência, haverá a formação da camada limite que, como já observado, é crescente. O diagrama de velocidades vai se ajustando ao longo do tubo, apresentando um gradiente na camada limite e um valor constante no fluido livre. A camada limite cresce até preencher o conduto na abscissa x = x. A partir desse ponto, o diagrama tem uma configuração constante em qualquer seção do conduto e o regime de escoamento é denominado ‘dinamicamente estabelecido’. Figura 7.5 Como foi visto, a camada limite pode apresentar uma parte laminar e uma turbulenta. Se o preenchimento do conduto pela camada limite acontecer enquanto esta é laminar, então, daí para a frente, o escoamento será laminar, e o diagrama de velocidades, em condutos de seção circular, será dado por v = v max ⎡ ⎢1 ⎣ – ⎝⎛⎜ r R ⎞⎠⎟ 2 ⎤ ⎥ ⎦ , conforme apresentado no Capítulo 3. Esse ρvD caso acontecerá se Re = μ < 2.000.

É mais freqüente esse preenchimento da camada limite acontecer quando ela já está com movimento turbulento. Nesse caso, o regime dinamicamente estabelecido apresentará diagramas idênticos em todas as seções, dados pela expressão v = v max ⎜⎛⎝1 – r R ⎞⎟⎠ 1/7 , conforme foi visto no Capítulo 3 (Figura 7.6).

Figura 7.6 O escoamento, nessa situação, será turbulento no conduto, a não ser junto às paredes, ρvD onde aparecerá o filme laminar, cuja espessura δ será função de Re = será maior que 2.400. μ , que, nesse caso,

<!-- p. 168 -->
A presença do filme laminar, no escoamento em tubos, permitirá explicar o comportamento de uma grandeza importante num item posterior. Em resumo, em condutos o escoamento pode se estabelecer laminar, se Re < 2.000, ou turbulento, se Re > 2.400, e, nesse caso, o escoamento apresentará subcamada limite laminar.

### 7.2.5 Rugosidade

Os condutos apresentam asperezas nas paredes internas que influem na perda de carga dos fluidos em escoamento. Em geral, tais asperezas não são uniformes, mas apresentam uma distribuição aleatória tanto em altura como em disposição. No entanto, para efeito de estudo, supõe-se inicialmente (tal hipótese será retirada posteriormente) que as asperezas tenham altura e distribuição uniformes. A altura uniforme das asperezas será indicada por ε e denominada ‘rugosidade uniforme’ (Figura 7.7). Figura 7.7 Para efeito do estudo das perdas no escoamento de fluidos, é fácil compreender que elas não dependem diretamente de ε, mas do quociente DH/ε, que será chamado ‘rugosidade relativa’.

### 7.2.6 Classificação das perdas de carga

Se for examinado o comportamento do escoamento de fluidos em condutos, será possível distinguir dois tipos de perda de carga (não esqueça o leitor que perda de carga é a energia perdida pela unidade de peso do fluido quando este escoa). O primeiro tipo é chamado ‘perda de carga distribuída’, que será indicada por hf. Tal perda, como o próprio nome diz, é a que acontece ao longo de tubos retos, de seção constante, devido ao atrito das próprias partículas do fluido entre si. Note-se que nessa situação a perda só será considerável se houver trechos relativamente longos de condutos, pois o atrito acontecerá de forma distribuída ao longo deles. O segundo tipo corresponde às chamadas ‘perdas de carga locais ou singulares’, que serão indicadas por hs. Elas acontecem em locais das instalações em que o fluido sofre perturbações bruscas no seu escoamento. Essas perdas podem, diferentemente das anteriores, ser grandes em trechos relativamente curtos da instalação, como, por exemplo, em válvulas, mudanças de direção, alargamentos bruscos, obstruções parciais etc. Esses locais, nas instalações, costumam ser chamados de ‘singularidades’, provindo daí o nome ‘perdas de carga singulares’. A Figura 7.8 mostra uma instalação em que são indicados os tipos de perdas que irão acontecer. Figura 7.8

<!-- p. 169 -->
Entre (1 e 2), (2 e 3), (3 e 4), (4 e 5) e (5 e 6) existem perdas distribuídas. Em (1) estreitamento brusco, (2) e (3) cotovelos, (4) estreitamento, (5) válvula, existem perdas singulares. Mais adiante será observado que o cálculo de umas e outras perdas será efetuado de formas diferentes, como era de esperar, já que as primeiras dependem do comprimento do conduto, enquanto as outras não dependem. Numa instalação completa, o termo Hp1,2 da Equação 7.1 será dado por: ∑ ∑ Hp1,2 = h f + h s (7.4)

## 7.3 Estudo da perda de carga distribuída (hf)

As hipóteses a seguir estabelecem as condições de validade do estudo. a) Regime permanente, fluido incompressível, para a validade da Equação 7.1. Note-se que gases que escoam com pequenas variações de pressão podem ser considerados incompressíveis. b) Condutos longos, para que no trecho considerado possa alcançado o regime dinamicamente estabelecido. c) Condutos cilíndricos, isto é, de seção transversal constante, mas qualquer. Se na instalação a área da seção variar de local a local, será necessário calcular a perda de carga em cada trecho e posteriormente somá-las para obter o total. d) Regime dinamicamente estabelecido, para que o diagrama de velocidades seja o mesmo em cada seção. e) Rugosidade uniforme (esta hipótese será retirada posteriormente). f) Trecho considerado sem máquinas. Dentro dessas hipóteses, serão aplicadas entre as seções (1) e (2) de um conduto as equações estudadas nos capítulos 3, 4 e 5. Figura 7.9 1) Equação da continuidade Dentro da hipótese de fluido incompressível, a equação da continuidade resulta em: Q1 = Q2 ou v1 A1 = v2 A 2 Mas o conduto é cilíndrico, então:

A1 = A2 v1 = v 2 = cte (7.5)

Logo, a velocidade deve ser constante em cada trecho escolhido para o cálculo da perda de carga distribuída.

<!-- p. 170 -->
2) Equação da energia Figura 7.10 A equação da energia entre as seções (1) e (2), entre as quais não há máquina, resulta em: H1 = H 2 + H p1,2 Mas, cumpridas as hipóteses de (a) a (f), Hp1,2 = h f1,2 por definição. Logo:

h f1,2 = H1 – H 2 = ΔH (7.6)

Pode-se então concluir que a perda de carga distribuída entre duas seções de um conduto é igual à diferença entre as cargas totais das duas seções, mantidas as hipóteses de (a) a (f). αv2 p Mas H= + +z 2g γ Logo: h f 1,2 = α 1 v12 – α 2 v 2 2 2g + p1 – p2 γ + z1 – z2 Pela Equação 7.5 e rearranjando os termos tem-se:

h f1 = ⎜⎛⎝ p1 γ + z 1 ⎞⎟⎠ – ⎛⎜⎝ p2 γ ⎞ + z 2 ⎟⎠ (7.7) A soma p γ + z será chamada ‘carga piezométrica’ (CP).

Note-se que, pela Figura 7.10, a CP pode ser medida em cada seção pela instalação de um piezômetro. Adotado um PHR, a carga piezométrica será, então, a distância, em cada seção, do nível superior do líquido no piezômetro até o PHR. Observe-se que, pela Equação 7.7, a perda de carga é dada pela diferença entre as cargas piezométricas das duas seções. Isso permite estabelecer um método experimental para a determinação da perda de carga. Se entre as seções (1) e (2) forem instalados muitos piezômetros, o nível superior do líquido em cada um deles indicará a carga piezométrica na seção, isto é, o valor de p + z (Figura 7.11). γ

<!-- p. 171 -->
Figura 7.11 O lugar geométrico dos pontos p γ + z é denominado linha piezométrica, que mostra geometricamente o andamento da pressão do fluido ao longo do conduto. Será mostrado a seguir que a linha piezométrica, dentro das hipóteses de (a) a (f), é p uma linha reta, de forma que, conhecendo-se o valor de γ + z em dois pontos, ela possa ser traçada. Define-se linha da energia como sendo o lugar geométrico dos pontos: p αv 2 +z+ =H γ 2g αv 2 Essa linha é obtida ao se somar a quantidade à carga piezométrica e fornecerá o 2g andamento da energia ao longo da instalação, sendo portanto sempre decrescente no sentido do escoamento, menos entre as seções de entrada e saída de uma bomba, já que esta fornece energia para o fluido. Note-se que mantidas as hipóteses de (a) a (f), a linha da energia será uma reta paralela αv 2 à linha piezométrica, já que é constante no trecho considerado (Figura 7.12). 2g Figura 7.12 A diferença de cotas entre dois pontos quaisquer da linha da energia fornecerá o valor da perda de carga no trecho considerado, isto é, entre as seções correspondentes aos dois pontos.

<!-- p. 172 -->
3) Equação de quantidade de movimento Figura 7.13 Pela equação da quantidade de movimento entre (1) e (2) (Equação 5.6):

r r r rr r Fs' = p1 A1 n 1 + p 2 A 2 n 2 + Qm ( v 2 – v1 ) – G r lembrando que F s' é a força resultante das pressões e tensões de cisalhamento da parede sólida sobre o fluido. Tal força, nesse caso, é exercida pela parede interna do conduto entre as seções (1) e (2).

Projetem-se os vetores dessa equação segundo o eixo x do conduto, orientado conforme mostrado na Figura 7.13. Lembrando ainda que pela Equação 7.5: rr v1 = v2 Logo:

Fs' = –p1 A1 + p2 A 2 + G sen α Como as pressões agem perpendicularmente à parede lateral, a força de pressão não terá componente segundo o eixo x, de forma que a força F's será composta somente da resultante das tensões de cisalhamento que agem na parede lateral do conduto. Essa parede tem uma área dada por σΔx. Assim, supondo as tensões com distribuição uniforme, já que o regime é dinamicamente estabelecido e a rugosidade é uniforme, tem-se:

F's = –τσΔx O sinal negativo resulta do fato de que essa força se opõe ao movimento e, portanto, tem sentido contrário ao do eixo x. Logo:

–τσΔx = (p2 – p1 )A + G sen α G = γV = γΔxA ou –τσΔx = (p2 – p1 )A + γAΔx sen α Note-se que:

Δx sen α = z 2 – z1 Logo:

τσΔx = (p1 – p2 )A + γA(z1 – z 2 )

Dividindo por γA e lembrando que A σ = R H , tem-se:

τΔx γR H = ⎜⎛⎝ p1 γ + z1 ⎟⎞⎠ – ⎛⎜⎝ p2 γ + z 2 ⎟⎞⎠ Pela Equação 7.7 nota-se que:

h f 1,2 = 4τΔx γD H = ⎛⎝⎜ p1 γ + z 1 ⎠⎞⎟ – ⎛⎝⎜ p2 γ + z 2 ⎟⎞⎠ (7.8)

<!-- p. 173 -->
Dessa equação conclui-se que a linha piezométrica é uma reta, pois sendo τ, γ, RH p constantes, pode-se escrever γ + z = kx, que é a equação de uma reta.

Pode-se concluir, ainda, que a perda de carga distribuída é diretamente proporcional ao comprimento Δx = L do conduto e inversamente proporcional ao diâmetro hidráulico. Se o cálculo da tensão de cisalhamento na parede do conduto não fosse de difícil determinação, a expressão 4τL h f1,2 = γD H (7.9)

serviria para o cálculo da perda de carga distribuída. Devido àquela dificuldade, será determinada outra expressão de maior utilidade prática.

## 7.4 Fórmula da perda de carga distribuída

A dedução será realizada por análise dimensional.

No fenômeno da perda de carga a função representativa é: γh f = f (ρ, v, DH , μ, L, ε) Existem sete grandezas e, portanto, quatro adimensionais. Escolhendo a base ρ,v,DH, obtém-se: π1 = gh f v2 , que por conveniência será utilizado na forma π1 = v h 2 f 2g . π2 = ρvDH μ = Re; π 3 = L DH ; π 4 = DH ε Logo, a função equivalente será:

hf v2 = φ⎛⎜Re, L , DH ⎞⎟ ⎝ DH ε ⎠ 2g ou hf = v2 φ⎛⎜Re, L 2g ⎝ DH , DH ε ⎟⎞⎠ Pela Equação 7.9, verificou-se que: h f αL DH , logo: h f L = DH v2 2g φ1 ⎝⎛⎜Re, DH ε ⎞⎠⎟. Seja o valor de φ1 ⎛⎜⎝Re, DH ε ⎠⎞⎟ = f = coeficiente da perda de carga distribuída; então: L v2 hf =f DH 2g (7.10) Note-se que, com essa equação, dados L, DH e a vazão (ou velocidade), pode-se determinar hf conhecendo o valor de f que é função do número de Reynolds e da rugosidade relativa. A obtenção do valor do coeficiente f em função dos valores de Re e DH será realizada experimentalmente, pela construção de um diagrama universal, já que f, ε Re e D H são adimensionais.

ε

<!-- p. 174 -->
## 7.5 Experiência de Nikuradse

Nikuradse realizou uma experiência em que procurou determinar a função f = f ⎛⎝⎜Re, DH ε ⎞⎟⎠ para condutos com rugosidade uniforme. Para tanto, colou na parte interna de diversos condutos areia de granulosidade uniforme. Fixou então os valores de ε, L, DH, ρ e μ no dispositivo da Figura 7.14. Para diversas aberturas da válvula e, portanto, para diversas velocidades do fluido, obteve os valores de p1 e p2 nos manômetros indicados.

Pela equação da energia:

hf = ( p1 − p2 ) γ Figura 7.14 Logo, fixado o DH ε , obteve uma tabela de f em função de Re = ρvD μ H , já que calculou a velocidade em cada caso e ρ, DH e μ eram conhecidos.

Efetuando essa experiência para diversos DH ε , construiu um gráfico de f = f ⎝⎛⎜Re, DH ε ⎟⎞⎠ (Figura 7.15).

A seguir serão descritas as diversas regiões desse gráfico.

Figura 7.15 (I) Corresponde a Re < 2.000. Nesse trecho, o diagrama é uma reta e nota-se que f só é função do Re, havendo uma única reta para todos os ⎜⎝⎛ DH ε ⎠⎟⎞ testados. Sabe-se que, nesse caso, as forças viscosas são grandes, deslocando as partículas segundo trajetórias retas paralelas, não afetadas pelas asperezas da parede do conduto. Pode-se verificar que:

<!-- p. 175 -->
log f = log 64 – log Re ou 64 f= Re (7.11)

de modo que, para Re < 2.000, não haveria necessidade do diagrama, já que, dado o Re, o f fica determinado. (II) Corresponde a 2.000 < Re < 2.400, sendo, portanto, relativo à transição entre laminar e turbulento. Acima de Re = 2.400 o regime será turbulento no conduto, mas junto à parede subsiste a subcamada limite, em que o movimento é do tipo laminar. Sabe-se que a espessura δ da subcamada é função do número de Reynolds. Dada a rugosidade ε do conduto, podem acontecer duas coisas: se δ > ε, a subcamada cobre as asperezas e, sendo o movimento laminar no seu interior, as asperezas não participam das perdas; se δ < ε, as asperezas emergem da subcamada e penetram no núcleo do escoamento, que é turbulento, tendo então influência nas perdas.

(III) Note-se que todas as curvas para as quais DH ε é grande ⎜⎝⎛ ⎛⎜⎝ DH ε ⎟⎞⎠ é crescente para baixo⎞⎟⎠ têm o trecho inicial coincidente com a curva (III) inferior. Isso se deve ao fato de que, quanto menor o número de Reynolds, mais espessa é a subcamada que pode cobrir as asperezas. Quando isso acontece, as perdas e, portanto, o coeficiente f só dependem do número de Reynolds, não dependendo do DH ε . Por causa disso, as curvas de DH ε mantêm-se coincidentes com a curva (III) até um certo número de Reynolds, a partir do qual as asperezas ficam descobertas. Vejam-se, por exemplo, as curvas (1) e (2) na Figura 7.15.

De A até B, as curvas coincidem, pois até o valor de Re do ponto B o δ é maior que a rugosidade de ambas as curvas. A partir do ponto B, a curva (1) se separa, mas a (2) não, pois a rugosidade da curva (1) é maior que a da (2) e, portanto, já emerge da subcamada. Aumentando o Re até C, a curva (2) também se separa, pois, a partir desse ponto, δ é menor que a rugosidade correspondente a essa curva. A curva (III) corresponde ao chamado ‘regime hidraulicamente liso’, porque o filme laminar, cobrindo as asperezas, faz com que o núcleo do escoamento, que é turbulento, deslize sobre uma parede lisa, formada pela subcamada limite laminar. (IV) Essa região é a compreendida entre a curva (III) e a reta xy. Nessa região, todas as curvas de DH emergem da subcamada e o coeficiente f depende de Re e DH . Essa região é de ε ε transição entre a curva (III) do hidraulicamente liso e a região (V) do hidraulicamente rugoso. (V) Na região (V), as curvas de DH ficam paralelas ao eixo dos números de Reynolds. Isso ε mostra que, dada uma curva DH ε , a partir do ponto de intersecção com a reta xy, f independe de Reynolds, isto é, variações no Re não afetam as perdas. Isso era de esperar, pois no Capítulo 6 foi verificado que números de Reynolds elevados implicam o fato de que as forças viscosas não mais influem no fenômeno. Nessa região, as variações do coeficiente f são devidas somente ao D H e, portanto, à rugosidade. Diz-se, então, que o regime é ‘hidraulicamente rugoso’.

ε

<!-- p. 176 -->
## 7.6 Condutos industriais

A experiência de Nikuradse, como foi visto, baseou-se no fato de que a rugosidade dos condutos era uniforme. Ele conseguiu isso artificialmente, colando areia de granulação calibrada no interior dos condutos utilizados na pesquisa. Na prática, essa condição não se verifica, pois os condutos industriais apresentam uma distribuição aleatória de rugosidades. Colebrook, ao repetir as mesmas experiências de Nikuradse para condutos industriais, verificou que o comportamento experimental é análogo.

Superpondo os seus resultados aos de Nikuradse, Colebrook criou o conceito de ‘rugosidade equivalente k’, isto é, o valor correspondente a ε do tubo artificial para o qual as experiências de Colebrook, com tubos industriais, superpõem-se àquelas de Nikuradse na região hidraulicamente rugosa. Em termos mais simples, a rugosidade equivalente k é uma rugosidade fictícia, uniforme, que substituída no lugar da rugosidade real de um tubo industrial causa o mesmo efeito.

Moody e, posteriormente, Rouse construíram, para tubos reais, o diagrama conhecido como diagrama de Moody-Rouse (Figura 7.16). Do lado esquerdo do diagrama, observa-se o valor das rugosidades equivalentes para diversos materiais.

Note-se que ao utilizar o diâmetro hidráulico nas expressões Re = ρvDH = vDH μ ν (7.12) DH ε L v2 hf =f DH 2g (7.13) (7.14)

elas valem para condutos de qualquer seção, circular ou não.

## 7.7 Problemas típicos envolvendo apenas perda de carga distribuída

Em muitas instalações, a perda de carga singular é desprezível, em relação à distribuída. É o caso, por exemplo, de instalações longas com poucas singularidades. O caso contrário também acontece. Nas instalações residenciais, por exemplo, devido ao grande número de singularidades, as perdas distribuídas são desprezíveis comparativamente às singulares. Serão aqui estudadas as soluções de três problemas típicos ligados ao primeiro caso, isto é, as perdas singulares, se existirem, serão desprezíveis.

Sejam os problemas em que são envolvidas as variáveis L, DH, Q, ν, k e hf. Podem-se observar três casos importantes:

1ο 2ο 3ο caso: caso: caso:

dados: dados: dados:

L, L, L, DH, Q, ν, k, procura-se hf ; DH, hf, ν, k, procura-se Q; Q, hf, ν, k, procura-se DH. Volta-se a ressaltar o fato de que o estudo feito a seguir para esses três casos só será válido se H P1,2 = h f1,2 , isto é, hs ≅ 0.

O estudo dos três casos será feito por exemplos numéricos, que poderão servir como modelo sempre que um problema se enquadrar num deles.

1o caso Determinar a perda de carga por km de comprimento de uma tubulação de aço de seção circular de diâmetro 45 cm. O fluido é óleo (ν = l,06 ×10–5 m 2/s) e a vazão é 190 L/s.

<!-- p. 177 -->
Capítulo 7 z Escoamento permanente de fluido incompressível em condutos forçados z 177 Figura 7.16

<!-- p. 178 -->
Solução Pelo fato de a tubulação ser de aço, no canto esquerdo da Figura 7.16 encontra-se k = 0,000046 m ou k = 4,6 × 10–5 m. Sendo de seção circular, D = DH = 0,45 m. Note-se que:

hf = f L DH v2 2g Seja g = 10 m/s2; são conhecidos L e DH; não se tem nem v nem f. O f é função da velocidade, pois depende do Re. Deve-se, então, calcular v. v = Q = 4Q = 4 × 190 × 10–3 = 1,19 m /s A πD2 π × 0,452 Determinação de f f = f ⎜⎝⎛ Re, DH k ⎠⎞⎟ Re = vDH = 1,19 × 0,45 ≅ 5 × 104 ν 1,06 × 10–5 DH k = 0,45 4,6 × 10–5 ≅ 104 = 10.000 A função f deverá então ser calculada no ponto f = f (5 × 104 ;10.000)

No diagrama de Moody-Rouse (Figura 7.16) deve-se fazer a determinação do f, conforme a ilustração a seguir. (Note-se que as linhas de chamada, para os Re, são curvas.) Logo, pelo esquema, f = 0,021.

hf = f L DH v2 2g = 0,021 1.000 × 0,45 1,192 2 × 10 = 3,3 m A perda de carga, a cada 1.000 m = 1 km de tubulação, será de 3,3 m.

<!-- p. 179 -->
2o caso Calcular a vazão de água num conduto de ferro fundido, sendo dados D = 10 cm, ν = 0,7 × 10–6 m 2/s e sabendo-se que dois manômetros instalados a uma distância de 10 m indicam, respectivamente, 0,15 MPa e 0,145 MPa ( γ H2O = 104 N/m 3 ). Solução Equação da energia H 1 + H M = H 2 + H p1,2 No trecho (1)–(2) só existe perda distribuída; logo:

h f1,2 = H1 – H2 = α 1v21 – α 2v22 2g + p1 – γ p2 + z1 – z2 Mas: Logo:

vl = v2; α1 = α2 e z1 = z2 h f1,2 = p1 – γ p2 = (0,15 – 0,145) × 104 106 = 0,5 m Tem-se: D = 0,1 m; ν = 0,7 × 10–6 m 2/s; L = 10 m; hf = 0,5 m e, da tabela à esquerda da Figura 7.16, obtém-se: k (ferro fundido) = 0,000259 m = 2,59 × 10–4 m Procura-se a vazão. Nota-se, então, que é tipicamente o segundo caso citado anteriormente. Sabe-se que: Q = vA e hf = f L DH v2 2g ou v = 2gh f DH fL Note-se que para determinar a velocidade é necessário determinar o valor de f, que, no entanto, é função da velocidade através do número de Reynolds. Entretanto, o produto Re f , existente em abscissas, na parte inferior do diagrama de Moody-Rouse (Figura 7.16), resultará em: Re f = vDH 2gh f DH = DH 2gh f DH ν v2L ν L (7.15)

e nota-se que independe da velocidade; logo, pode ser calculado. Opera-se, então, da seguinte forma: f = f ⎜⎛ ⎝ Re f ; DH k ⎞⎟ ⎠ Re f = Dh 2gh f Dh = 0,1 2 × 10 × 0,5 × 0,1 ≅ 4,5 × 104 ν L 0,7 × 10–6 10

<!-- p. 180 -->
DH = 0,1 = 385 k 2,59 × 10–4 No diagrama, procura-se f = f (4,5 × 104; 385).

Logo:

f = 0,027 e v = 2gh f DH = 2 × 10 × 0,5 × 0,1 = 1,92 m/s fL 0,027 × 10 Note-se que, em vez de obter f no diagrama, poderia ter-se optado pela obtenção de Re, e teríamos Re = 2,8 × 105. Mas: Re = vDH ν e v = νRe = 0,7 × 10–6 × 2,8 × 105 = 1,96 m/s DH 0,1 O primeiro resultado (v = 1,92 m/s) é de maior confiabilidade, pois a leitura de f, pelas escalas utilizadas no diagrama, é mais precisa. O leitor deverá, portanto, optar sempre pelo primeiro método, isto é, pela leitura do valor de f no diagrama. Logo:

Q = vA = v πD2 = 1,92 × π × 0,12 = 15,1× 10–3 m3 / s 4 4 ou Q = 15,1 L/s 3o caso Calcular o diâmetro de um tubo de aço que deverá transportar uma vazão de 19 L/s de querosene ( ν = 3 × 10–6 m 2/s) a uma distância de 600 m, com uma perda de carga de 3 m. Solução Esse caso só pode ser resolvido por tentativas. O método será o seguinte:

a) Como hf = f L v2 D 2g = f L D Q2 A 22g = f L D ⎛⎜ Q2 πD2 ⎞⎟ 2 2g ⎝ 4⎠

<!-- p. 181 -->
ou hf = fL 8Q2 π 2D5g portanto D = 5 8fLQ2 (1) h f π2g b) Na expressão (1) não se tem o valor de f nem é possível calculá-lo, pois não se conhece v e D. Será feita uma primeira tentativa com f = f1.

c) Calculado o diâmetro, pela expressão (1), pode-se calcular a velocidade e, com ela, o Re. Com Re e DH do diagrama de Moody-Rouse, obtém-se f2.

k Se f2 for igual ao f1 adotado, então o diâmetro obtido pela expressão (1) será a solução; senão, adota-se f = f2 e faz-se uma segunda tentativa, repetindo todo o processo anterior. No caso do exemplo, tem-se: tubo de aço com k = 4,6 × 10–5 m.

1a tentativa Adota-se fl = 0,02.

Logo: D1 = 5 8f1LQ2 h f π2g =5 8 × 0,02 × 600 × (19 × 3 × π2× 10 10–3 )2 = 0,164 m v1 = 4Q πD12 = 4 × 19 × 10–3 π × (0,164)2 = 0,9 m/ s Re 1 = v1D1 ν = 0,9 × 0,164 3 × 10–6 = 4,92 × 104 D1 = 0,164 = 3.560 k 4,6 × 10–5 2a tentativa Adota-se f2 = 0,023.

Logo: D2 = 5 8× 0,023 × 600 × 3× π2 × (19 × 10 10–3 )2 = 0,165 m É óbvio que com essa variação no diâmetro não haverá alterações no Re nem no D/k; logo: f3 = f2 = 0,023 Conclui-se, então, que o diâmetro do conduto deverá ser D = 0,165 m.

<!-- p. 182 -->
1) Na instalação da figura, a bomba B recalca água do reservatório R1 para o reservatório R2, ambos em nível constante. Desprezando as perdas de carga singulares, determinar: a) a vazão na tubulação; b) a potência da bomba em kW se o rendimento é 73%.

Dados: D = 10 cm; L = 50 m (comprimento g = 10 m/s2; ν = 10–6 m2/s; γ = 104 N/m3. total da tubulação); tubos de ferro fundido (k = 2,5 × 104 m); hf = 4 m; Solução a) Como as perdas singulares são desprezíveis, conclui-se que o problema se refere ao segundo caso. hf = f L DH v2 → 2g v= 2gDHh f fL Tem-se:

Re f = DH 2gDHh f ν L ou Re f = 10 × 10–2 2 × 10 × 10 × 10–2 × 4 = 4 × 104 10–6 50 DH = 10 × 10–2 = 400 k 2,5 × 10–4 Pelo diagrama de Moody-Rouse, obtém-se f = 0,025; logo:

v = 2gDHh f = 2 × 10 × 10 × 10–2 × 4 = 2,55 m /s fL 0,025 × 50 A vazão será:

Q = vA = v πD2 = 2,55 × π (10 × 10–2 )2 4 4 ou Q = 20 × 10–3 m3/s = 20 L/s b) Equação da energia entre (1) e (2)

ou mas H 1 + H B = H 2 + H p1,2 H B = H 2 – H 1 + H p1,2 H2 – H1 = α 2v22 – α 1v21 2g + p2 – γ p1 + z2 – z1 Como os tanques são de grandes dimensões e abertos à atmosfera, tem-se:

H2 – H1 = z2 – z1

<!-- p. 183 -->
Ainda: Logo: e Hp1,2 = h f1,2 HB = (z2 – z1 )+ h f1,2 = 10 + 4 = 14 m NB = γQHB hB = 104 × 20 × 10–3 × 0,73 14 1 = 3,8 kW 1.000 2) Dada a tubulação da figura, cuja seção (2) está aberta à atmosfera, calcular: a) a perda de carga entre (1) e (2); b) a vazão em volume.

Sabe-se que o escoamento é laminar. Dados: γ = 9.000 N/m3; ν = 0,5 × 10–3 m2/s; L1,2 = 30 m; D = 15 cm; p1 = 32,8 kPa. Solução a) Aplicando a equação da energia entre (1) e (2), tem-se:

H 1 + H B = H 2 = H p1,2 ou H p1,2 = H1 – H2 = α 1v21 – α 2v 2 2 2g + p1 – γ p2 + z1 – z2 Pela equação da continuidade, v1 = v2.

Se o regime é dinamicamente estabelecido, α1 = α2.

Se (2) está aberto à pressão atmosférica, p2 = 0.

Tem-se ainda z1 = z2.

Logo: H p1,2 = h f1,2 = p1 γ = 32,8 × 103 9.000 = 3,64 m h f1, ,2 = 3,64 m b) hf =f L DH v2 2g (1)

Não se conhece v; logo, não se conhece f. Como, porém, o escoamento é laminar, sabe-se que: f = 64 = 64 ν (2) Re vDH Substituindo (2) em (1), tem-se:

hf = 64 ν vDH L DH v2 2g ou v = 2gD2Hh f = 20 × 0,152 × 3,64 = 1,71 m /s 64 νL 64 × 0,5 × 10–3 × 30 Logo:

Q = vA = v πD2 = 1,71× π × 0,152 = 30,1× 10–3 4 4 Q = 30,1× 10–3 m 3/s = 30,1 L/ s

<!-- p. 184 -->
## 7.8 Perdas de carga singulares

Já foi visto que a perda de carga é singular quando é produzida por uma perturbação brusca no escoamento do fluido. Viu-se também que tais perturbações são produzidas nas singularidades, como válvulas, registros, alargamentos bruscos etc. As perdas de carga singulares também são calculadas por uma expressão obtida pela análise dimensional, como se segue. No fenômeno da perda de carga singular, a função característica é: γhs = f (v, ν, ρ, grandezas geométricas da singularidade), onde v é uma velocidade de referência e as grandezas geométricas são características para cada singularidade. Por exemplo, num alargamento brusco (Figura 7.17), são grandezas geométricas características as áreas A1 e A2. Figura 7.17 Conclui-se então que:

hs v2 = φ (Re, coeficientes adimensionais de forma)

2g O valor numérico da função φ, para um certo valor do número de Reynolds e para certos valores dos coeficientes de forma, será indicado por ks e será chamado ‘coeficiente da perda de carga singular’. Portanto: hs = ks v2 2g (7.16)

onde: ks = φ (Re, coeficiente adimensional de forma) No caso do alargamento brusco: ks = φ ⎛⎜ Re, ⎝ A1 A2 ⎟⎞ ⎠ Para números de Reynolds elevados, como se sabe, o fenômeno passa a independer das forças viscosas; logo, nesse caso: k s = φ (coeficiente de forma)

Exemplos de valores de ks são fornecidos na tabela a seguir. Os valores na tabela servem apenas como exemplo. Para maiores informações, o leitor deverá recorrer a manuais de hidráulica ou a catálogos de fabricantes.

<!-- p. 185 -->
Singularidade Alargamento Esquema ks (1 - A1/A2) (no caso, v = v1)

Caso limite 1 Estreitamento φ (A1/A2) Caso limite 0,5 Cotovelo a 90° 0,9 Válvula de gaveta Válvula tipo globo Totalmente aberta 0,2 Totalmente aberta 10 Válvula de retenção 0,5 Outro método para a determinação das perdas singulares é o dos ‘comprimentos equivalentes’. Comprimento equivalente de uma singularidade é o comprimento fictício de uma tubulação de seção constante de mesmo diâmetro, que produziria uma perda distribuída igual à perda singular da singularidade. Sua determinação pode ser feita da seguinte forma:

Singularidade:

v2 h s = k s 2g Tubo fictício:

h f eq = f L eq DH v2 2g

<!-- p. 186 -->
Igualando as duas expressões (pela definição de comprimento equivalente (Leq), obtém-se: f L eq DH v2 2g v2 = k s 2g ou L eq = k sDH f (7.17)

Na prática, os comprimentos equivalentes são tabelados, de forma que numa instalação todas as singularidades possam ser reduzidas a comprimentos imaginários de condutos, e o cálculo da perda total é dado por: ∑ ∑ Hp = h f + h s Hp = f L real DH v 2 + f L eq 2g DH v2 2g Hp = f (L real + L eq DH ) v2 2g (7.18)

Como a maioria dos exercícios que serão resolvidos ou propostos neste capítulo irá se referir ao cálculo das perdas singulares, por meio do coeficiente ks, será aqui apresentado um exemplo para a utilização do comprimento equivalente. No trecho (1)-(5) de uma instalação existem: uma válvula de gaveta (2), uma válvula tipo globo (3) e um cotovelo (4). Sendo a tubulação de aço de diâmetro = 2"(5 cm), determinar a perda de carga entre (1) e (5), sabendo que a vazão é 2 L/s e que o comprimento da tubulação entre (1) e (5) é 30 cm. (ν = 10–6 m2/s) Solução O comprimento das singularidades é desprezado e supõe-se que a perda de carga distribuída seja devida a 30 m de tubulação. Note-se que esse fato será observado em todos os problemas deste capítulo. H p1,5 = h f1,5 + h s 2 + h s 3 + h s 4 Da tabela de um fabricante tem-se:

Válvula de gaveta (2") → Leq2 = 0,335 m Válvula tipo globo (2") → Leq3 = 17,61 m Cotovelo (2")

→ Leq4 = 3,01 m Tudo se passa, então, como se a tubulação tivesse um comprimento de L = L real + L eq(2) + L eq(3) + L eq(4)

para efeito de cálculo da perda de carga.

<!-- p. 187 -->
L = 30 + 0,335 + 17,61 + 3,01 ≅ 51 m hf = f L DH v2 2g A velocidade será:

v = Q = 4Q = 4 × 2 × 10–3 ≅ 1 m /s A πD2 π × ( 5 × 10–2 )2 Logo: Para aço: Logo:

Re = vDH = 1× 5 × 10–2 = 5 × 104 ν 10–6 k = 4,6 × 10–5m DH = 5 × 10–2 = 1.090 k 4,6 × 10–5 Com Re = 5 × 104 e DH = 1.090, do diagrama de Moody-Rouse tem-se f = 0,025. k Logo: h f1,5 = 0,025 × 51 × 5 × 10–2 12 = 1,28 m 2 × 10 ou HP1,2 = 1,28 m

## 7.9 Instalações de recalque

É o conjunto de equipamentos que permite o transporte e controle da vazão de um fluido. Compreende, em geral, um reservatório, tubos, singularidades, máquina e um reservatório de descarga. A tubulação, que vai desde o reservatório de tomada até a máquina, chama-se ‘tubulação de sucção’ e, geralmente, contém uma válvula de pé com crivo na entrada, que nada mais é que uma válvula de retenção com filtro. Esta tem o objetivo de não permitir a entrada de detritos na máquina e a válvula de retenção não permite o retorno do fluido ao se desligar a bomba (Figura 7.18). Figura 7.18 A tubulação que liga a bomba com o reservatório de descarga chama-se ‘tubulação de recalque’ e contém, em geral, uma válvula de retenção e um registro para o controle da vazão (Figura 7.18).

<!-- p. 188 -->
Geralmente, o objetivo nas instalações é a seleção e a determinação da potência da máquina hidráulica instalada. Posteriormente, serão vistos alguns exemplos de cálculo, mas antes será discutido o fenômeno da cavitação. Ao aplicar a equação da energia entre as seções (1) e (e) de entrada da bomba:

H1 = H e + H p1, e Adotando o PHR por (1) e sendo o reservatório de grandes dimensões e aberto à atmosfera, conclui-se que H1 = 0.

Como: He = α e v 2 e 2g + pe γ +ze e Então: ou H p1, e = h f + h s 0= αev 2g 2 e + pe γ +z e+h f +h s pe γ =– ⎜⎛ α e v 2 e ⎝ 2g +z e +h f +h s ⎞⎟ ⎠ Note-se que todos os termos entre parênteses são positivos; logo: pe <0 γ Em termos de escala absoluta:

p eabs =p e+p atm p eabs = p atm –γ ⎛⎜ α e v 2 e ⎝ 2g +z e+h f +h s ⎞⎟ ⎠ (7.19)

Se pv é a pressão de vapor do líquido à temperatura do escoamento, pode acontecer que: p e abs ≤ p v Nesse caso, haveria formação de vapor na tubulação de sucção nos pontos onde vigora a condição anteriormente citada. O fenômeno de formação de vapor, em tubulação ou máquinas hidráulicas, devido à baixa pressão, chama-se cavitação. A cavitação é prejudicial, pois as bolhas de vapor, alcançando pontos de maior pressão, condensam bruscamente e implodem com grande liberação de energia, podendo causar vibrações e uma erosão particular devido à agitação e choques das partículas do líquido sobre as paredes sólidas. Além disso, o fenômeno da cavitação faz com que o rendimento das máquinas alcance valores muito baixos. Todos já perceberam que, para evitar tal fenômeno, a condição necessária é:

p e abs > p v A tabela apresentada a seguir fornece a variação de pv com a temperatura, para o caso da água. t (°C) pv (kPa)

0 0,617 10 1,225 20 2,313 30 4,204 50 12,25 100 101,2

<!-- p. 189 -->
A condição peabs > pv nem sempre é suficiente para evitar a cavitação. Mesmo que o fluido entre na máquina, obedecendo àquela condição, é possível que devido às suas condições internas haja formação de bolhas de vapor em seu interior. Tal fato pode ser notado quando, ao desmontar a máquina, percebe-se, principalmente no rotor, formação de cavidades causadas pela erosão. Na prática, fixam-se índices mais seguros para que não haja cavitação na máquina. Tais índices são determinados experimentalmente. Tem-se, como exemplo, o chamado NPSH (Net Positive Suction Head). Para maiores informações, o leitor deverá reportar-se à literatura especializada em máquinas hidráulicas. A condição que será imposta para nosso estudo e na solução de problemas é a seguinte: p e abs > p v O leitor deve notar que pela Equação 7.19 as condições que ajudam a manutenção dessa desigualdade são: a) Menor velocidade no tubo de sucção. Fixada a vazão, esse resultado só pode ser obtido com tubos de maior diâmetro. b) Menor cota ze. Às vezes, a máquina deverá trabalhar ‘afogada’, isto é, com ze negativo, ou, em outras palavras, a máquina deverá ser colocada abaixo do nível do reservatório. c) Menores perdas distribuídas e singulares na tubulação de sucção.

Sendo a pressão pressão p8 mantida igual a 532 kPa constante, determinar a potência da bomba na entrada dela se a vazão for 40 L/s. Dados: tubos de ferro galvanizado de (k rendimento 0,7 e a = 0,15 × 10–3 m); k s 1 = 15; k s 2 = k s 6 = 0,9; k s 3 = k s 5 = 10; patm = 101 kPa.

k s 7 = 1; k s 4 = 0,5; pv H 2O = 1,96 kPa (abs); γ = 104 N/m 3; υ = 10–6 m 2/s; Indica-se com índice S o que se refere à sucção e com R o que se refere ao recalque. Dados: DS = 15 cm; DR = 10 cm.

<!-- p. 190 -->
Solução Note-se que os diâmetros na sucção e no recalque são diferentes; logo, o cálculo das perdas deverá ser feito separadamente. Se os diâmetros fossem os mesmos, poderíamos efetuar um cálculo diretamente entre as seções (0) e (8). Equação da energia de (0) a (8)

H 0 + H B = H 8 + H p0,8 Assumindo o PHR no nível (0), tem-se H0 = 0.

H8 = α 8v28 2g + p8 γ + z8 = 0+ 532 × 103 104 + 7,5 = 60,7 m Cálculo das perdas Sucção Perda distribuída ∑ ∑ Hp0,8 = h f S + h f R + h s S + h s R vS = 4Q πD2S = 4 × 40 × 10–3 π × 0,152 = 2,26 m/s Re S = vDH ν = 2,26 × 0,15 10–6 = 3,4 × 105 ⎝⎛⎜ DH k ⎟⎞⎠ S = 0,15 0,15 × 10–3 = 1.000 Do diagrama de Moody-Rouse, fS = 0,021 Logo: hfS = fS LS DH S v2S 2g = 0,021 × 12 × 2,262 = 0,43 m 0,15 2 × 10 Perda singular h fS = ks1 v 2 S 2g +k s 2 v 2 S 2g +k s 3 v 2 S 2g = (ks 1 +ks 2 +ks 3 ) v 2 S 2g hs S = (15 + 0,9 + 10) 2,262 2 × 10 = 6,61 m Logo:

h p0, e = h f S + h s S = 0,43 + 6,6 m = 7,03 m ≅ 7,0 m Recalque pela equação da continuidade vR = v S ⎜⎛ ⎝ DS DR 2 ⎞⎟ ⎠ = 2,26 ⎜⎛ 15 ⎞⎟ 2 ⎝ 10 ⎠ = 5,1 m /s Perda distribuída Re R = vDH ν = 5,1× 0,1 = 5,1× 10–6 105 ⎜⎛ DH ⎟⎞ ⎝ k ⎠R = 0,1 1,5 × 10–4 = 666 Do diagrama de Moody-Rouse, fR = 0,023. Logo:

hfR = fR LR DH R vR2 2g = 0,023 × 36 × 0,1 5,12 = 10,8 m 2 × 10

<!-- p. 191 -->
Perda singular hsR = ks4 v R2 2g + ks5 v 2R 2g + ks6 v 2 R 2g + ks7 v 2 R 2g hsR = (ks 4 + ks 5 + ks6 + ks7 )

vR2 = (0,5 + 10 + 0,9 + 1) 2g 5,12 = 16,1 m 2 × 10 Logo:

Hp S,8 = h f R + h s R = 10,8 + 16,1 = 26,9 m A perda total na instalação será:

Hp0,8 = Hp0, e + Hp S,8 = 7,0 + 26,9 = 33,9 m Logo, voltando à equação da energia: HB = H8 – H0 + Hp0,8 = 60,7 – 0 + 33,9 = 94,6 m A potência da bomba será dada por: NB = γQH B ηB = 104 × 40 × 10–3 × 0,7 94,6 1 1.000 ≅ 54 kW Pressão na entrada Aplicando a equação da energia entre (0) e (e), tem-se:

Como H0 = 0 e HM = 0, então:

H 0 + H M = H e + H p0, e Mas:

H e + H p0, e = 0 He = α ev2e 2g + pe γ + ze Logo: pe = –γ ⎛⎝⎜ α ev2e 2g + ze + H p0, e ⎞⎠⎟ pe = –104 ⎜⎛ 2,262 + ⎝ 2 × 10 0,5 + 7,0⎟⎠⎞ × 1 1.000 = –77,5 kPa Na escala absoluta:

peabs = pe + patm = –77,5 + 101 = 23,5 kPa (abs) peabs = 23,5 kPa (abs) > pv = 1,96 kPa (abs) Logo, a tubulação de sucção está bem dimensionada.

## 7.10 Linhas de energia e piezométrica

No item 7.3 foi vista a definição das linhas de energia e piezométrica. αv2 p Viu-se que a linha de energia (LE) é o lugar geométrico dos pontos 2g + γ + z de uma p instalação e a linha piezométrica (LP), o lugar geométrico dos valores de γ + z. Foi visto, ainda, que essas duas linhas, num trecho de conduto reto de seção constante, são retas paralelas decrescentes no sentido do escoamento e que, nesse caso, a diferença entre a cota de dois de seus pontos corresponde à perda de carga no trecho entre as duas seções correspondentes do conduto.

<!-- p. 192 -->
No caso da existência de perdas singulares, as LE e LP não têm andamento definido, sendo representadas por uma linha sinuosa (Figura 7.19). Figura 7.19 No caso de uma máquina, as duas linhas serão crescentes, se esta for uma bomba, e decrescentes, se for uma turbina. Figura 7.20 Nos exemplos que serão resolvidos a seguir, o leitor deverá procurar interpretar o aspecto das duas linhas, de forma a não ter dúvidas no traçado em qualquer outro caso. 1) Esboçar as LP e LE, qualitativamente, para as instalações das figuras (a), (b) e (c). a)

<!-- p. 193 -->
Capítulo 7 z Escoamento permanente de fluido incompressível em condutos forçados z 193 b) c)

2) Dada a instalação da figura, determinar qual é o trecho que está com pressão negativa e qual o valor da cota z0. Dados: Q ks1 = 0,5; = k 3,94 L/s; D s2 = 0,2; ks3 = 5 cm (constante); L = 100 = 19; ks4 = 1; k = 25 × 10–5 m; m; l γ = = 25 10 m; z5 = 20 4 N /m 3.

m; ν = 10–6 m2/s; NB = 1,91 kW; ηB = 0,75; Solução Determina-se, em primeiro lugar, a cota z0. Aplicando a equação da energia entre (0) e (5), tem-se: H 0 + H B = H 5 + H p0,5 Note-se que os dois tanques são de grandes dimensões (v ≅ 0) e abertos à atmosfera (p = 0).

<!-- p. 194 -->
Logo: H0 = z0 H5 = z5 = 20 m Pelo valor da potência da bomba pode-se determinar a carga manométrica: NB = γQH B ηB HB = ηBNB γQ = 0,75 × 1,91× 103 104 × 3,94 × 10–3 = 36,3 m Cálculo das perdas H p0,5 = h f0,5 + h s 1 + h s 2 + h s 3 + h s 4 H p0,5 =f L D v2 2g + k s 1 v2 2g + k s 2 v2 2g + k s 3 v2 2g + k s 4 v2 2g H p0,5 = ⎜⎝⎛ f L D + k s 1 + ks2 + ks3 + k s 4 ⎟⎞⎠ v2 2g v = Q = 4Q = 4 × 3,94 × 10–3 = 2 m/s A πD2 π × ( 5 × 10–2 )2 v2 = 2 2 = 0,2 m 2g 2 × 10 Re = vDH = 2 × 5 × 10–2 = 105 ν 10–6 DH = 5 × 10–2 = 200 k 25 × 10–5 Pelo diagrama de Moody-Rouse, f = 0,031. Logo:

H p0,5 = ⎛⎜ 0,031 125 + ⎝ 0,05 0,5 + 0,2 + 19 + 1⎞⎟ ⎠ 0,2 = 19,64 m Levando todos os resultados à equação da energia, tem-se:

z0 + 36,3 = 20 + 19,64 m ou z0 = 3,34 m Note-se que esse resultado tem um significado físico muito ilustrativo. O fato de z0 dever ser 3,34 m significa que a carga manométrica de 36,3 m da bomba não é suficiente para vencer as perdas e os 20 m do tanque de descarga. O fluido precisará de uma energia potencial inicial correspondente aos 3,34 m calculados. Na segunda parte do problema, deve-se determinar o trecho da instalação que está com pressão negativa, isto é, pressão menor que a atmosférica. É óbvio que, se existir tal condição, ela será necessariamente encontrada no conduto de sucção. Calcula-se a pressão no ponto A antes da válvula (2).

Equação da energia entre (0) e (A)

H 0 = H A + H p0, A Note-se que os resultados obtidos na pesquisa de z0 podem ser aqui utilizados. H0 = 3,34 m HA = pA γ + vA2 2g + zA A velocidade é a mesma em toda a instalação, pois o diâmetro é constante; logo:

<!-- p. 195 -->
v2A = 0,2 m 2g HA = pA γ + 0,2 + 0 H p0, A = h f0, A + hs1 =f L D v2 2g + k s 1 v2 2g = ⎛⎜⎝ f L D + k s 1 ⎠⎞⎟ v2 2g H p0, A = ⎛⎜ 0,031× ⎝ 12,5 + 0,5⎟⎞ × 0,05 ⎠ 0,2 = 1,65 m 3,34 = pA + 0,2 + 1,65 γ pA = 1,49 m γ Logo, a pressão antes da válvula é positiva.

O trecho negativo poderia ser obtido por tentativas. No entanto, sabe-se que a LP num trecho reto de seção constante é uma reta. Calcula-se, então, a pressão no ponto B a jusante da válvula (2) e a pressão no ponto (e) de entrada da bomba. Tais pressões (como zB = ze = 0), marcadas em escala num desenho, serão dois pontos da LP que, portanto, poderá ser traçada. Pressão no ponto B Aplicando a equação da energia entre A e B, tem-se:

H A = H B + H pA, B v2A 2g + pA γ + zA = v2B 2g + pB γ + zB + H pA, B Pela equação da continuidade: vA = vB.

H pA, B = hs2 = ks2 v2 2g pB γ = pA γ – ks2 v2 2g pB = 1,49 – 0,2 × 0,2 = 1,45 m γ Pressão no ponto (e) Equação da energia entre B e (e)

H B = H e + H p B, e pB γ + vB2 2g + zB = pe γ + ve2 2g + ze + hf B, e pe = pB – f L v2 γ γ D 2g pe = 1,45 – 0,03112,5 × 0,2 = – 0,1 m γ 0,05 Vamos desenhar a LP entre B e (e).

<!-- p. 196 -->
Pela semelhança dos dois triângulos:

1,45 = 12,5 – x; logo: x = 0,8 m 0,1 x O trecho com pressão negativa começa a 0,8 m antes da bomba.

7.1 Uma galeria de seção quadrada (0,6 m × 0,6 m) esgota ar de uma mina, onde a pressão é de 0,2 mca, para a atmosfera. Calcular a vazão de ar. Desprezar as perdas singulares. Sabe-se que νar = 10–5 m 2/s; γ ar = 12,7 N/m 3; k = 10–3 m. Resp.: Q = 4,5 m3/s 7.2 Na instalação da figura, deseja-se conhecer o desnível Δh entre os dois reservatórios de água. Dados: potência fornecida k s 4 =k s 5 =1,2; k s 6 ao fluido N = 0,75 kW; diâmetro D = 3 cm; = 1,6; ν = 10–6 m 2/s ; f = 0,02; γ = 104 N/m 3. Q = 3 L/s; L1,2 = 2 m; L3,6 = 10 m; k s 1 =1; Determinar também a rugosidade do conduto e a altura h0 para que a pressão efetiva na entrada da bomba seja nula. Resp.: Δh = 13,3 m; k = 1,5 × 10–5 m; h0 = 3 m

<!-- p. 197 -->
7.3 No sistema esquematizado, conhece-se Q = 16 L/s e sabe-se que o sentido de escoamento é de (0) para (8). Com os dados da figura, determinar: a) a energia por unidade de peso trocada entre a máquina e o fluido e o tipo de máquina; b) o coeficiente de perda de carga distribuída.

Dados: γ H ks 2 = 3,5.

2 O = 104 N / m3; γ Hg = 1,36 × 105 N / m3 ; D = 10 cm; ks 1 =k s =10; 7 ks6 = 2; ks 3 = ks4 =k s 5 = 1,5; Resp.: a) 25,2 m; b) 0,04 7.4 Dada a instalação da figura, determinar:

a) a velocidade e a vazão na tubulação; b) a pressão no ponto A, ponto médio do trecho (3)-(4). Dados: k s 1 = 0,5 ; k s 2 = k s 3 = k s 4 = k s 5 = 1; k s 6 = 10; k s 7 = 1; D = 6 cm; k = 0,15 cm; g = 10 m/s2; ν = 10–6 m 2/s ; γ = 104 N /m 3. Resp.: a) v = 1,45 m/s; Q = 4,1 L/s; b) pA = 15,5 kPa 7.5 Um motor elétrico fornece 3 kW à bomba da instalação da figura, que tem um rendimento de 80%. Sendo dados: a) as tubulações são de mesma seção, cujo diâmetro é de 5 cm e de mesmo material; b) c) k a sv1a=zã1o0;emk s 2v=olkusm8 e=n1a; kinss3 t=alkaçsã5 o= ékds 6e=10k sL7/=s;k s 9 = 0,5; d) o comprimento (real) de (1) a (3) é de 10 m e, de (5) a (9), de 100 m.

<!-- p. 198 -->
198 z Mecânica dos Fluidos Determinar: a) a perda de carga entre (0) e (4) (total); b) o coeficiente de perda de carga distribuída; c) a perda de carga entre (4) e (10) (total); d) a potência da turbina, sabendo que seu rendimento é de 90%; e) o comprimento equivalente das singularidades da instalação. Resp.: a) 17,6 m; b) 0,01; c) 29,9 m; d) 5,1 kW; e) 72,5 m 7.6 Numa certa região, há três reservatórios naturais, A, B e C, e um conjunto TB formado por uma turbina acoplada diretamente a uma bomba. As perdas de carga nas tubulações são: entre a e b, H pa, b = 0,5 m entre c e d, H pc, d = 0,4 m entre f e g, H pf, g = 0,6 m entre i e j, H pi, j = 0,4 m e o rendimento do conjunto TB, ηTB = ηT × ηB = 0,6. Sendo T = turbina e B = bomba, determinar a relação entre as vazões QT e QB na turbina e na bomba, respectivamente. Fluido: água de γ = 104 N/m3. Resp.: QT/QB = 9,15

<!-- p. 199 -->
7.7 Entre A e C do circuito hidráulico da figura está um conjunto de elementos combustíveis usado em reatores H pC, A nucleares. Desprezam-se as perdas no resto do circuito = 135 m; D = 10 cm; ν = 10–7 m2/s; LCA = 24 m; d = 1,5 cm; e γ =sã1o04dNad/oms:3.NB = 18 kW; ηB = 0,75; Calcular a rugosidade equivalente k dos materiais de que são feitos os tubos externos e internos. Resp.: k = 2,8 × 10–4 m 7.8 Calcular a vazão na tubulação da figura para H = 10 m. Calcular em seguida o novo valor de H para que a vazão seja 50 L/s. Dados: D = 150 mm; ν = 1,05 × 10–6 m2/s; γ = 104 N/m3; k = 25,9 × 10–5 m; k s 1 = 0,5; k s 2 = k s 3 = 0,9; k s 4 = 10 Resp.: Q = 47 L/s; h = 11,1 m 7.9 Um pequeno reservatório é alimentado por um poço artesiano, conforme mostra a figura. O manômetro metálico acusa 50 kPa. Sabe-se que a tubulação é de ferro fundido de 10 cm de diâmetro. Calcular a vazão de alimentação do reservatório. (ν = 10–6 m2/s) Resp.: Q = 40 L/s 7.10 Dois reservatórios cujos níveis estão nas cotas 500 m e 480 m estão interligados por uma tubulação de concreto (k = 10–3 m) de 8 km de extensão e 1 m de diâmetro. Determinar a vazão que pode ser transportada. (Desprezar as perdas singulares.)

<!-- p. 200 -->
Resp.: Q = 1,27 m3/s 7.11 Pretende-se esgotar a atmosfera poluída de uma instalação subterrânea através de um poço de seção circular, por meio de um 10–5 m2/s; k = 10–3 m; ventilador. Dados: D = 3 m; h = 50 m; Q = patm = 100 kPa. Determinar a potência do 71 m3/s; ηV ventilador.

= 0,75; γ = 13 N/m3; ν = 1,5 × Resp.: NV = 50,4 kW 7.12 Na instalação da figura, a água deve ser lançada por meio de um bocal no tanque da direita. Determinar a mínima potência da bomba para que isso aconteça. Dados: D = 10 cm; material: ferro fundido; diâmetro de saída Ds = 7,5 cm; ν = 10–6 m2/s; γ = 104 N/m3; k s 1 = 0,5; ηB = 0,75. Desprezar a perda singular no bocal. Resp.: NB = 18,1 kW 7.13 A instalação da figura será utilizada para o transporte de 12 L/s de água do reservatório A para o reservatório C, ambos mantidos em nível constante. A bomba será adquirida do fabricante X, que produz bombas de potência nominal: 0,5 CV; 1 CV; 1,5 CV; 2 CV; 3 CV; 4 CV; 5 CV, todas com rendimento de 82%. Dados: D k s 6 = 1; L2,3 = 4 = 10 cm; m; L3,6 = d=8 15 m; cm; g= k = 5 × 10–5 m; γ = 104 N/m3; ν = 10 m/s2. Desprezam-se as perdas 10–6 m2/s; k s 3 = 0,1; k s 4 = k s 5 = 0,5; entre as seções (0) e (1). Selecionar a bomba apropriada.

<!-- p. 201 -->
7.14 Na instalação da figura, um líquido de alta viscosidade cinemática (ν = 10–4 m2/s), escoando laminarmente, é recalcado do reservatório A para C. O comprimento da tubulação, desde a saída da bomba B até a entrada do cotovelo, é 60 m, medidos ao longo do eixo do tubo. O raio R é muito grande e a distância entre a saída do cotovelo e a entrada do tanque C pode ser desprezada. Determinar: a) a carga manométrica que a bomba deverá prover para obter-se uma vazão de 8 L/s; b) a potência da bomba, cujo rendimento é de 70%. Dados: ks (saída de A) = 0,78; γ = 8.000 N/m3; ks (cotovelo) = 0,6; ks (entrada de C) = 0,5. Resp.: a) HB = 12,3 m; b) NB = 1,1 kW 7.15 Dada a instalação da figura, determinar a pressão p0 para que a vazão seja 6 L/s. Em seguida, traçar a linha piezométrica e a linha de energia sobre a instalação, marcando o valor das respectivas alturas nas seções A, B, C, ν = 10–6 m2/s; D, E, NB = F e G. Dados: D = 5 cm; L = 0,75 kW; γ = 104 N/m3; ηB 50 m; f = = 100%.

0,02; k s B = 0,5; k s CD = 0,5; h = 2 m; pE = -50 kPa; Resp.: p0 = 127 kPa

<!-- p. 202 -->
7.16 Um conduto de ferro fundido de 1.000 m de comprimento e 10 cm de diâmetro liga dois reservatórios em níveis constantes, e foi projetado para uma vazão de 20 L/s de água. Colocada em funcionamento a instalação, verificou-se que a vazão que circulava era igual à metade da prevista, em virtude de uma obstrução do escoamento por material esquecido no interior da tubulação. Qual é a perda de carga singular introduzida pela obstrução? Dados: γágua = 104 N/m3; μágua = 10–3 N.s/m2. Resp.: hS = 62,6 m 7.17 Considere um tubo de ferro galvanizado, horizontal, de 5 cm de diâmetro. Qual deve ser a mínima queda de pressão da água, num trecho de 30 m de comprimento, para que o escoamento seja turbulento e hidraulicamente rugoso? Dados: γágua = 104 N/m3; μágua = 10–3 N.s/m2. Resp.: Δp = 500 kPa 7.18 Na instalação da figura, determinar a potência da bomba necessária para produzir uma vazão de 10 L/s, supondo seu rendimento de 70%. Dados:

= 104 N/m3; Leq = 1 20 m ; Leq 2 =2 m ; Leq 6 = Leq 7 Drec = =1 m 2,5" ; ks (6,25 = 10 5 cm); Dsuc ; k s = 8 1 . = 4" (10 cm); aço; ν = 10–6 m2/s; γ Resp.: 7,1 kW

## 7.19 Na Leq

figura, =2 m.

3 H1 = 56 m, H4 Determinar:

= 38 m e os comprimentos equivalentes das singularidades são Leq2 = 18 m e a) o coeficiente de perda de carga distribuída f; b) o comprimento da instalação entre (1) e (4); c) a perda de carga singular devida à válvula (3).

Resp.: a) f = 0,02; b) L = 60 m; c) hs = 0,45 m 7.20 No esquema da figura, qual deve ser a máxima cota z para que não haja cavitação com água a 20°C? Dados: Q = 10 L/s; D = 10 cm; patm = 92,4 kPa; pv = 2,36 kPa (abs); tubo de aço. (ν = 10-6 m2/s, γ = 104 N/m3)

<!-- p. 203 -->
Resp.: z = 7,6 m 7.21 Na instalação da figura, o sistema que interliga os reservatórios A e B é constituído por uma tubulação de diâmetro constante (D = 0,1 m), comprimento total L = 100 m e pela máquina M. Admitindo-se desprezíveis as perdas de carga singulares na tubulação e sendo conhecidos os trechos da LP e LE, como é indicado na seção C, determinar: a) o tipo de máquina M; b) a potência da máquina, cujo rendimento é de 75%; c) a cota z da LP na seção indicada na figura. Dados: ν = 10–6 m2/s; g = 10 m/s2; γ = 104 N/m3; tubo de ferro fundido. Resp.: a) Turbina (HM = –8,8 m); b) NT = 1,04 kW; c) z = 13,76 m 7.22 Na instalação da figura, a bomba B recalca uma vazão Q e a LE para tal vazão tem a configuração indicada. A tubulação tem diâmetro constante D = 25 mm e o coeficiente de perda de carga f = 0,025. Sabendo que o manômetro diferencial conectado na válvula V da forma indicada acusa um desnível h = 1 m e que g = 10 m/s2, γ H2O = 104 N/m 3; γ Hg = 1,3 × 105 N/m 3, determinar: a) a vazão Q; b) a potência no eixo da bomba, supondo um rendimento de 59%. Resp.: a) Q = 2,2 × 10–3 m3/s; b) NB = 1,26 kW

<!-- p. 204 -->
204 z Mecânica dos Fluidos 7.23 Água escoa em regime laminar num conduto cilíndrico horizontal de diâmetro D. A linha de energia forma com a horizontal um ângulo α. Determinar a vazão. Dados: ν = 10–6 m2/s; D = 1 cm; tg α = 0,0032; g = 10 m/s2. Resp.: Q = 7,9 × 10–6 m3/s 7.24 O escoamento no trecho do tubo da figura é laminar. Com a válvula totalmente aberta, a linha piezométrica é praticamente uma reta (ks ≅ 0) e indica as medidas do desenho. Ao fechar a válvula de 3/4, a vazão cai à metade da anterior. Determinar o coeficiente de perda de carga singular nesse caso, sabendo que na segunda situação o desnível marcado pelos manômetros extremos é o mesmo da primeira situação. Dados: ν = 10–5 m2/s; γ = 104 N/m3; DT = 2 cm.

Resp.: kS = 1.280 7.25 Na instalação são dados: reservatório de grandes dimensões; f = 0,01; k s 2=2; γ = 104 N/m3; g = 10 m/s2. Determinar: a) a vazão em volume; b) a perda de carga na instalação; c) o valor de x; d) substituindo o cotovelo (2) por uma turbina e mantidas as demais condições, determinar sua potência, sabendo que ηT = 90%. Resp.: a) 47,1 L/s; b) 12,8 m; c) 14,6 m; d) 1,5 kW

<!-- p. 205 -->
7.26 Na instalação da figura, determinar:

a) a altura h; b) o tipo de máquina; c) a potência da máquina se ηM Dados: Q = 31,4 L/s; tg β = 0,2; γ = 70%. = 8.000 N/m3; ν = 10–4 m2/s; k s 1 = 16; Leq4 = 20 m; p5 = 32 kPa; D = 20 cm; d = 10 cm.

Resp.: a) 40,8 m; b) bomba; c) 10 kW 7.27 Nbpeoanridpnosetrqadulaaesçkãdosi2sd=tar1i;bfkiugsíu3d=raa0s,,5a(;pptagortaαênf=acc0iai,l0id0taa4r;bηoosBm=cbá8alc0éu%1lo,e5sγ7).=kQ1W0u4.aDlNde/etmevr3e.mrDáinessaeerrjaao-psceroesmsuspbãrositmpit1ueeinrotaocsdopmaetrpudrbaimus lseainnçtãgoouLlaa, rsseeasracrescentado nos cálculos? Resp.: p1 = 14,6 kPa; Leq = 2.000 m 7.28 No alargamento da figura escoa água γ = 104 N/m3 com escoamento uniforme nas seções, por hipótese. Sendo indicada a linha piezométrica e sendo A1 = 10 cm2 e A2 = 45 cm2, determinar o coeficiente de perda de carga singular. Resp.: ks = 0,75

<!-- p. 206 -->

# Capítulo 8 — Noções de instrumentação para medida das propriedades dos fluidos e dos escoamentos

## 8.1 Introdução

Este capítulo tratará dos princípios de funcionamento da instrumentação para a medição de propriedades dos fluidos, como massa específica e viscosidade, e de propriedades do escoamento, como velocidade e vazão. O princípio de funcionamento dos medidores de pressão não será abordado, já que o Capítulo 2 tratou desse assunto. Este capítulo tratará apenas de noções conceituais que servirão como introdução para o estudo de uma literatura mais especializada, à qual deverá recorrer o leitor para conhecer os detalhes, se necessário para a sua vida profissional.

## 8.2 Massa específica e peso específico relativo

A medida da massa específica baseia-se, em geral, na determinação da massa de um volume conhecido do fluido em estudo. Outra forma de realizá-la é pela estática dos fluidos, tratada no Capítulo 2. Pesa-se um corpo de volume conhecido numa balança e posteriormente ele é pesado mergulhado no fluido do qual se quer medir a massa específica. Figura 8.1 Se a balança da Figura 8.1 estiver equilibrada, ao ser mergulhado o corpo de volume conhecido no líquido em estudo, ela irá se desequilibrar para a direita, por causa do empuxo. Mas o empuxo é igual ao peso do volume de líquido deslocado que, por sua vez, é igual ao peso que se deve retirar do prato direito da balança para restabelecer o equilíbrio. Logo: G = Vγ ou γ = G V

<!-- p. 207 -->
e portanto: ρ=γ g Para a determinação do peso específico relativo, realiza-se a mesma experiência com água a 15°C, considerada padrão, determinando o γ H 2O que será utilizado como referência: γ γr = γ H 2O Os densímetros são corpos graduados que colocados num líquido flutuam num certo nível, indicando o peso específico relativo do líquido. A graduação baseia-se no mesmo princípio indicado anteriormente. Outra forma para a determinação da massa específica é indicada no Exercício 2.10, desde que se possua um líquido de massa específica conhecida.

## 8.3 Viscosidade

O medidor de viscosidade costuma ser chamado de viscosímetro. Esse dispositivo pode ser idealizado de diversas formas.

### 8.3.1 Viscosímetro de cilindros coaxiais

É baseado no Exercício 1.10, em que existe uma explicação sucinta, mas clara, de seu funcionamento. A viscosidade dinâmica será dada por: μ = 2M t (De – Di πωD 3 i h ) (8.1)

onde, mantidos De, Di, h e ω, pode-se ler diretamente a viscosidade, pois μ = kM t , que, por sua vez, está relacionado à deformação do fio calibrado à torção.

### 8.3.2 Viscosímetro de esfera

É constituído de um tubo cilíndrico de altura conhecida (Figura 8.2), que contém o líquido em estudo. Deixa-se cair uma esfera no líquido e se mede o tempo que ela leva para percorrer uma distância conhecida. Na esfera agem: o peso:

G = Vγ esfera = 4 3 πR 3 γ e Figura 8.2

<!-- p. 208 -->
o empuxo: E = Vγ líquido = 4 3 πR 3 γ l a força de resistência ao avanço ou arrasto (capítulos 6 e 9):

Fa = 6πμvR Como Fa é proporcional a v, a velocidade da esfera aumentará sob a ação da gravidade, até que as três forças anteriormente indicadas fiquem em equilíbrio. A partir desse instante, a velocidade será constante e dada por: L v= t onde t pode ser medido por um cronômetro. Para essa condição, tem-se:

G = E + Fa ou 4 3 πR 3 γ e = 4 3 πR 3 γ l +6πμ L t R e portanto:

μ = D2 ( γ e – γ l )t onde D = 2R 18 L (8.2)

### 8.3.3 Viscosímetro Saybolt

A viscosidade é medida em segundos Saybolt. Esses segundos representam o tempo para que 60 cm3 do fluido escoem no tubo capilar da Figura 8.3. Figura 8.3 A viscosidade em segundos Saybolt pode ser relacionada com a viscosidade cinemática, pois o escoamento pelo capilar é função da viscosidade dinâmica e da massa específica. Por causa disso, dois fluidos de mesma viscosidade Saybolt podem ter diferentes viscosidades dinâmicas, mas deverão ter a mesma viscosidade cinemática. A relação que liga a viscosidade cinemática com os segundos Saybolt é:

ν = 0,0022t – 1,80 (8.3) t onde: ν em cm2/s e t em s.

## 8.4 Medida da velocidade com tubo de Pitot

O tubo de Pitot é fundamentalmente um tubo colocado com a sua abertura na direção das trajetórias das partículas do fluido, que é dobrado posteriormente em ângulo reto, onde é adaptado um piezômetro (Figura 8.4).

<!-- p. 209 -->
As partículas de fluido, ao incidir em (2), são paradas ao encontrar o fluido do piezômetro, de forma que a coluna h formada será devida parte à carga da pressão e parte à carga da velocidade, já que no ponto (2) também a energia cinética é transformada em efeito de pressão, o que é explicado fisicamente pelos choques contínuos das partículas que chegam em (2) em cada instante. O ponto (2) é chamado ‘ponto de parada ou de estagnação’. Figura 8.4 Adotando-se o ponto (1) muito próximo de (2), as perdas entre eles serão desprezíveis, e a aplicação da equação da energia reduz-se a: H1 = H2 ou v12 2g + p1 γ + z1 = v 2 2 2g + p2 γ +z2 mas: Logo:

z1 = z 2 e v2 = 0 (ponto de estagnação)

v12 = p 2 – p1 2g γ e v1 = 2g (p2 – p1 ) γ (8.4)

Note-se que p2 pode ser dado por γh no piezômetro instalado no tubo de Pitot, enquanto p1 pode ser obtido por um manômetro instalado nas proximidades do piezômetro. Dessa forma, a velocidade no ponto (1) pode ser calculada pela Equação 8.4. A disposição mais usual para essa medição está indicada na Figura 8.5, onde foi utilizado um manômetro em U. O ramo da esquerda, sendo tangente às trajetórias, medirá a ‘pressão estática’ do fluido, enquanto o ramo da direita medirá a mesma pressão acrescida do efeito dinâmico ou choque devido à incidência das partículas, que será chamada ‘pressão dinâmica’. Devido a essas considerações, é óbvio que p2 p1 e, portanto, o fluido manométrico irá se desnivelar conforme a Figura 8.5. A equação manométrica aplicada entre (1) e (2) resulta em:

p1 + γ m h – γh = p2

<!-- p. 210 -->
Figura 8.5 ou p2 – p1 γ = ⎛ ⎜⎝ γm γ ⎞ –1⎠⎟ h (8.5)

Substituindo a Equação 8.5 na Equação 8.4, tem-se:

v= 2g ⎛ ⎜⎝ γm γ ⎞ – 1⎠⎟ h (8.6)

A Equação 8.6 permite, conhecidos os fluidos, determinar a velocidade do ponto onde o tubo de Pitot está instalado. Com o tubo de Pitot, é possível medir a velocidade em diversos pontos da seção para construir o diagrama de velocidades (Figura 8.6). Figura 8.6 É possível então, lembrando que: Q = ∫ vdA (Capítulo 3, Equação 3.4), obter a vazão pela utilização do tubo de Pitot.

A O tubo de Pitot pode ser utilizado também para a medida da velocidade em fluidos compressíveis, não sendo, porém, as expressões e o método tão simples como foi descrito (ver Capítulo 12).

Num tubo de seção circular, o diâmetro é 10 cm e o escoamento é do tipo turbulento. Um tubo de Pitot está instalado de forma a medir a velocidade no eixo do tubo, conforme a figura. Determinar a vazão no tubo.

<!-- p. 211 -->
Solução v= 2g ⎛ ⎜⎝ γm γ ⎞ – 1⎠⎟ h = 2 ×10 ⎛1,36 ×105 ⎜ ⎝ 10 4 ⎞ – 1⎟ ⎠ × 0,05 v = 3,55 m/s Note-se que no centro o tubo de Pitot estará medindo a velocidade máxima do diagrama; logo: vmax = 3,55 m/s. No Capítulo 3, verificou-se que, quando o movimento é turbulento, a velocidade média será: v = 49 60 vmax Logo: Portanto:

v = 2,9 m/s Q = vA = 2,9 × π 0,12 = 22,8 × 10–3 m 3/s 4 Q = 22,8 L/s

## 8.5 Medida da vazão

Neste item serão examinados alguns dispositivos que podem ser utilizados para a medida da vazão em diferentes instalações. Alguns deles poderiam ser utilizados para fluidos compressíveis, sendo, porém, o equacionamento mais complexo que o apresentado, válido somente para fluidos incompressíveis.

### 8.5.1 Orifício de bordo delgado ou diafragma

Neste item será examinado o escoamento de um fluido incompressível por um orifício de bordo delgado, instalado na parede lateral de um reservatório de grandes dimensões (Figura 8.7). Figura 8.7 O orifício tem bordo delgado, ou aresta viva, para que o fluido tenha contato apenas com a aresta do orifício, reduzindo o atrito (Figura 8.7).

Suponha-se inicialmente que o fluido seja ideal, de forma que Hp na equação da energia seja nulo. Logo: ou H1 = H 2 v12 2g + p1 γ + z1 = v 2 2 2g + p2 γ +z2 Com v1 = 0, z1 – z2 = h e lembrando que o fluido foi admitido ideal, pode-se obter o valor de v2, que será indicado por v2T = velocidade teórica.

<!-- p. 212 -->
v 2T = 2g ⎛ ⎝⎜ h + p1 – γ p2 ⎞ ⎠⎟ (8.7)

Se, em particular, p1 = p2 v2T = 2gh (8.8)

que é a equação de Torricelli. A Equação 8.7, pela hipótese de fluido ideal, não corresponde à realidade, de forma que a velocidade real no orifício será menor que a calculada por causa das perdas; isto é: v2r v2T onde v2r = velocidade real no orifício. Define-se coeficiente de velocidade como: Cv = vr vT (8.9)

Logo, se for possível determinar tal coeficiente, obtida a velocidade teórica pela Equação 8.7, a velocidade real poderá ser calculada. v 2r = C v v 2T = C v 2g ⎛ ⎜⎝ h + p1 – γ p2 ⎞ ⎠⎟ (8.10)

A vazão teórica no orifício será:

Q T = v 2T A o (8.11)

onde Ao é a área do orifício. Na Equação 8.11 existem dois efeitos que fazem com que a vazão que realmente escoa pelo orifício seja diferente.

O primeiro efeito já foi discutido e é devido ao fato de que v2T não corresponde à velocidade real; o outro deve-se à contração do jato na saída (Figura 8.8). Figura 8.8 As partículas do fluido, devido à inércia do movimento, tendem a ocupar no jato uma seção menor que a do orifício. O jato contrai-se e, a uma certa distância do orifício, apresenta-se com seção constante. É a chamada ‘veia contraída’. Define-se ‘coeficiente de contração’ como sendo a relação entre a área do jato na veia contraída e a área do orifício. Cc = Ac Ao com C c < 1 (8.12)

A vazão real no orifício será:

Q = C v v 2TC c A o

<!-- p. 213 -->
ou Q = C vC c A o 2g ⎛ ⎝⎜ h + p1 – γ p2 ⎞ ⎠⎟ (8.13) ou Q = C vC cQT (8.14)

Note-se que o produto dos coeficientes de velocidade e de contração dá origem ao coeficiente que corrige a vazão. Este será denominado coeficiente de vazão ou descarga: Q CD = QT (8.15)

portanto, comparando as equações 8.14 e 8.15, conclui-se que:

C D = C vC c Logo: Q = CDAo 2g ⎛ ⎝⎜ h + p1 – γ p2 ⎞ ⎠⎟ Será estudado agora o caso em que um desses orifícios está instalado na seção de saída de um tubo de seção circular (Figura 8.9). Figura 8.9 Aplicando a equação da energia entre (1) e (2) para fluido ideal:

v12 2g + p1 γ + z1 = v 2 2 2g + p2 γ +z2 ou a velocidade teórica do jato será:

v 2T = 2g ⎛ ⎜ p1 + v12 ⎞ ⎟ ⎝ γ 2g ⎠ e a vazão: Q = CcCvAo 2g ⎛ ⎜ ⎝ p1 γ + v12 2g ⎞ ⎟ ⎠ = CDAo 2g ⎛ ⎜ ⎝ p1 γ + v12 2g ⎞ ⎟ ⎠ (8.16) A velocidade v1 é chamada ‘velocidade de aproximação do orifício’. Note-se que a Equação 8.16 não serve para o cálculo da vazão, pois esta depende de v1. A velocidade de aproximação deve então ser retirada do segundo membro da equação. Após algumas transformações algébricas, tem-se:

Q= CDAo 1– C 2 C ⎛ ⎜⎝ Do D1 ⎞ ⎠⎟ 4 2g p1 γ onde Do = diâmetro do orifício.

<!-- p. 214 -->
Designando por:

k= CD 1– C 2 C ⎛ ⎜⎝ Do D1 ⎞ ⎠⎟ 4 (8.17) obtém-se: Q = kA o 2g p1 γ (8.18)

onde k é um coeficiente adimensional que depende do número de Reynolds de aproximação, isto é, calculado com a velocidade de aproximação e da relação Do . D1 Com os conceitos estabelecidos, será possível, agora, estudar o caso mais prático do orifício instalado no interior de uma tubulação para medir a vazão (Figura 8.10). Figura 8.10 Aplicando a equação da energia entre (1) e (2) e procedendo da mesma forma que no caso anterior, verifica-se que é obtida uma equação idêntica à Equação 8.18, exceto em relação à existência de p2 ≠ 0. Logo: Q = kA o 2g ⎛ ⎝⎜ p1 – γ p2 ⎞ ⎠⎟ (8.19)

com k dado pela Equação 8.17. Tais orifícios são normalizados e a Figura 8.11 mostra o diagrama de k em função de Re e Do , obtido de literatura especializada, para orifícios do tipo daquele indicado na próD1 pria figura.

<!-- p. 215 -->
Figura 8.11 No orifício da figura, está instalado um manômetro diferencial cujo fluido manométrico, de γm = 3× 104 N/m3, indica um desnível de 5 cm. Sendo o diâmetro do tubo 10 cm e o do orifício 5 cm, determinar a vazão, sabendo que o fluido que escoa é água. (γ = 104 N/m3 ; ν = 10–6 m2/s). Solução Ao = πD2o 4 = π × 52 4 × 10–4 = 1,96 × 10–3 m2 Aplicando a equação manométrica:

p1 + γh – γ mh = p2 ou p1 – γ p2 = ⎝⎛⎜ γm γ – 1⎠⎟⎞ h portanto: p1 – γ p2 = ⎛⎜ ⎝ 3 × 104 104 – 1⎞⎟ × ⎠ 0,05 = 0,1 m O valor de k deve ser obtido da Figura 8.11. Como, porém, não se conhece a vazão, v1 não é conhecido, logo não se pode calcular Re. Note-se, porém, que o k, a partir de um certo valor de Re, torna-se constante. O valor de k será adotado e deverá ser verificado posteriormente. Com Do = 5 = 0,5, tem-se: k = 0,624 para Re 7 × 104. D1 10

<!-- p. 216 -->
Logo:

Q = 0,624 × 1,96 × 10–3 2 × 10 × 0,1 Q = 1,73 × 10–3 m3/s Agora deverá ser feita a verificação:

v1 = 4Q πD21 = 4 × 1,73 × 10–3 π × 0,12 = 0,22 m/s e Re = v1D1 = 0,22 × 0,1 = 2,2 × 104 , que é menor que o adotado (7 × 104).

ν 10–6 Portanto, deve ser feita a correção. O novo k será obtido com o valor do Re = 2,2× 104 e Do = 0,5; portanto: k = 0,63. D1 Logo:

Q = 0,63 × 1,96 × 10–3 2 × 10 × 0,1 Q = 1,75 × 10–3 m3/s Verificação: v1 = 4Q πD21 = 4 × 1,75 × 10–3 π × 0,12 = 0,223 m/s Re = v1D1 = 0,223 × 0,1 = 2,23 × 104 ν 10–6 Note-se que o Re variou muito pouco; logo, a vazão obtida na segunda tentativa pode ser adotada como verdadeira. Assim: Q = 1,75 L/s.

### 8.5.2 Venturímetro ou tubo Venturi

Como é mostrado na Figura 8.12, o tubo Venturi é constituído de um tubo convergente que atinge uma seção mínima denominada garganta, aumentando posteriormente num tubo divergente. Figura 8.12 O princípio de funcionamento é o mesmo que o do orifício. Na seção (2), devido à diminuição da área, a velocidade aumenta, causando uma queda da pressão. Tal queda, com um equacionamento semelhante ao do orifício, proporcionará uma expressão que permite o cálculo da vazão. (Notar que no orifício o aumento da velocidade acontece por causa da veia contraída (Figura 8.10).) Obtém-se:

Q = A2 v2 = CA 2 1– ⎛ ⎜⎝ D2 D1 ⎞ ⎟⎠ 4 2g ⎛ ⎝⎜ p1 – γ p2 ⎞ ⎠⎟ (8.20)

<!-- p. 217 -->
No caso dos tubos Venturi, o coeficiente C depende também do Re e de D2 ; no entanto, D1 a sua variação é pequena, podendo em geral ser dotado entre 0,95 e 0,99, sendo os valores mais altos para os maiores diâmetros e os mais baixos para os menores.

### 8.5.3 Bocal convergente

Corresponde à parte convergente do tubo Venturi (Figura 8.13).

Figura 8.13 Como no orifício, forma-se um descolamento do escoamento, dando origem a uma região de fluido sem movimento de translação, em cuja parte central escoa a veia contraída. Também nesse caso tem-se:

Q = kA 2 2g ⎛ ⎜⎝ p1 – γ p2 ⎞ ⎟⎠ (8.21) onde k é um coeficiente que é função de Re1 e D2 D1 (Figura 8.14).

Figura 8.14

### 8.5.4 Rotâmetro

É um tubo graduado no qual se localiza um elemento flutuante com ranhuras helicoidais, de forma que a rotação resultante faça com que se mantenha no centro do tubo (Figura 8.15). Dependendo da vazão, o flutuante irá se localizar numa certa posição que na escala corresponde a uma vazão predeterminada.

<!-- p. 218 -->
Figura 8.15

### 8.5.5 Medidores volumétricos

Existem muitos tipos de medidores volumétricos e seu objetivo é dar uma medida do volume total consumido durante um certo tempo. Por exemplo, são utilizados na entrada das instalações residenciais para a medida do consumo.

### 8.5.6 Medida em canais abertos

Nos canais abertos podem ser utilizados vertedores, que são obstruções no canal que obrigam o fluido a passar sobre elas. A medida da vazão é função da altura H do fluido em relação ao vertedor. A Figura 8.16 mostra um vertedor de seção retangular. Para o caso da figura, pode-se verificar que: Q = 1,84 LH3 2 onde L e H são em m e Q em m3/s.

Figura 8.16 (8.22)

8.1 Um pequeno objeto pesa 6 N no ar e 4,6 N quando mergulhado num líquido. O volume do objeto é 170 cm3. Qual é a massa específica, o peso específico e o peso específico relativo do líquido, se o peso específico da água é 104 N/m3? Resp.: ρ = 840 kg/m3; γ = 8.235 N/m3; γr = 0,823 8.2 Um densímetro é constituído de um cilindro de 0,5 cm de diâmetro e 36 cm de altura. No fundo do cilindro está presa uma esfera de 2,5 cm de diâmetro. O dispositivo pesa 0,15 N. Qual é a altura do cilindro que aflorará de um líquido de peso específico 104 N/m3? Resp.: 13 mm 8.3 Um viscosímetro de cilindros coaxiais possui líquido até uma altura de 25 cm. O diâmetro do cilindro menor é 10 cm, enquanto o do cilindro maior é 10,1 cm. O cilindro externo gira com uma rotação de 9,0 rpm quando se aplica um conjugado de 5 N.m. Determinar a viscosidade do fluido, desprezando o efeito do fundo. Resp.: μ = 13,1 N.s/m2

<!-- p. 219 -->
8.4 Uma esfera de chumbo (γ = 1,14 × 105 N/m3), de 0,5 cm de diâmetro, cai numa coluna de óleo (γ = 8.600 N/m3) com uma velocidade de 0,05 m/s. Determinar a viscosidade do óleo. Resp.: μ = 2,93 N.s/m2 8.5 Construiu-se um viscosímetro tipo Saybolt que deverá ser calibrado por intermédio da medida da viscosidade de dois líquidos de viscosidade conhecida. Um dos líquidos, de viscosidade 0,46 St, escoa um certo volume em 95 s, enquanto o outro tem 0,20 St e escoa o mesmo volume em 45 s. Determinar a equação do aparelho. Resp.: ν = 0,00496 t – 1,064/t 8.6 Sendo Cv = 0,9 e Cc = 0,6, determinar a pressão p1, sabendo Pitot. Determinar a vazão, sabendo que a área do orifício que é 50 o fluido cm2.

é água e que sobe 3 m no tubo de Resp.: p1 = -12,9 kPa; Q = 23,2 L/s 8.7 O reservatório superior descarrega a água, por um orifício cujo CD = 0,6, para um reservatório que, por sua vez, descarrega água por outro orifício. O sistema está em equilíbrio, de forma que o nível não muda em nenhum dos dois reservatórios. Qual será o coeficiente de descarga do segundo orifício? Dados: diâmetro do orifício (1): 9 cm; diâmetro do orifício (2): 10 cm. Resp.: CD = 0,81 8.8 Dado o dispositivo da figura, calcular a vazão do escoamento da água no conduto. Dados: γ H 2 O = 104 N/m3 ; γ m = 6 × 104 N/m3 ; p2 = 20 kPa; A = 10–2 m2; g = 10 m/s2. Desprezar as perdas e supor o diagrama de velocidades uniforme na seção. Resp.: Q = 40 L/s

<!-- p. 220 -->
8.9 No fundo do reservatório inferior da figura, inicialmente vazio, situa-se um cubo de madeira de 1 m de aresta. Do reservatório superior escoa água através de um orifício de aresta viva, cujo coeficiente de contração é Cc flutuar em = 0,6. Determinar o valor do coeficiente de velocidade do orifício, 20 s. Dados: γmadeira = 8.000 N/m3; Aorifício = 0,1 m2; g = 10 m/s2. para que o corpo comece a Resp.: Cv = 0,97 8.10 Qual é a diferença de pressão entre a seção maior e a garganta de um Venturi? A seção maior tem um diâmetro de 15 cm, e a garganta, de 7,5 cm. A vazão é 5 L/s de água. (γ = 104 N/m3) Dado: CD = 0,97 Resp.: Δp = 638 Pa 8.11 Um orifício de bordo delgado tem um diâmetro de 7,5 cm e descarrega uma vazão de 28 L/s. Mede-se um ponto da trajetória do jato e obtém-se x = 4,7 m para y = 1,2 m. Determinar os coeficientes de velocidade, de contração e de vazão do orifício. Resp.: Cv = 0,96; CD = 0,634; Cc = 0,66 8.12 Determinar a vazão num conduto de 15 cm de diâmetro que contém um bocal de diâmetro mínimo de 10 cm. Sabe-se que o manômetro diferencial instalado indica um desnível de 25 cm e que o fluido que escoa é água. Dados: ν = 10–6 m2/s; γ Hg = 13,6 × 104 N/m 3; γ H2O = 104 N/m 3. Resp.: Q = 66 L/s 8.13 Na Figura 8.16, L = 30 m, b = 0,5 m, H = 0,25 m. Estimar a vazão no canal. Resp.: Q = 6,9 m3/s

<!-- p. 221 -->
8.14 Após 5 min de funcionamento, o reservatório inferior, inicialmente vazio, está completamente cheio e, então, a comporta gira em torno do eixo A, devido ao momento de 6 × 104 N.m nela aplicado pela água. Determinar o coeficiente de descarga do orifício de saída do reservatório superior. Área do orifício = 0,01 m2. Resp.: CD = 0,467 8.15 Na figura, o tubo de Pitot faz a tomada da pressão dinâmica de um jato de água lançado por um orifício instalado no fundo do tanque. Se o orifício tem um diâmetro de 2,5 cm e o manômetro do Pitot indica 112 kPa, determinar o coeficiente de velocidade do orifício. Resp.: Cv = 0,93 8.16 No esquema m/s2.

a seguir, determinar a relação d2/d1. Desprezar as perdas. Dados: γ água = 104 N/m 3; g = 10 Resp.: d2 = 2 d1 8.17 Um tubo de água está fechado por um tampão na extremidade. Ao efetuar a operação de colocação de um piezômetro conforme a figura, o operador provoca um orifício no tampão (por acidente), o que provoca um vazamento. A leitura no piezômetro é 0,7 m a partir do eixo do orifício. Admitindo que a vazão de descarga pelo orifício é de 1,58 L/s, o diâmetro do orifício é 4 cm e o coeficiente de descarga, CD = 1, π determinar a velocidade de aproximação da água. Dados: g = 10 m/s2; γágua = 104 N/m3.

<!-- p. 222 -->
Resp.: 1,27 m/s 8.18 Os reservatórios do sistema não podem ser considerados de grandes dimensões; porém, deseja-se que seus níveis sejam constantes. São dados: γ = 2× 104 N/m3; p0 = p1 = p2; traçado quantitativo de LE e LP entre (s) e (o) na figura; Do = 0,8 D. Determinar: a) as pressões p0 e ps; b) a perda de carga entre (s) e (o); c) o coeficiente de descarga do orifício ‘e’.

Resp.: a) po = 24 kPa; ps = 100 kPa b) H ps, o = 3,5 m c) CD = 0,4

<!-- p. 223 -->

# Capítulo 9 — Fluidodinâmica

## 9.1 Introdução

Este capítulo tem o objetivo de estudar a interação existente entre um fluido e um corpo nele imerso, quando entre os dois existe um movimento relativo. Nessa condição, não importa se o corpo ou o fluido, ou ambos, estão em movimento. A observação do fenômeno será efetuada adotando-se o sistema de referência fixo à superfície sólida. Logo, do ponto de vista do observador o corpo sempre estará em repouso, e o fluido, em movimento. Por exemplo, se o objetivo for estudar o efeito do ar em um automóvel em movimento na estrada, o observador estará fixo no automóvel. Dessa forma, do ponto de vista do observador, tudo se passa como se o automóvel estivesse parado, e o ar, em movimento, com uma velocidade igual e em sentido contrário à do veículo. Nota-se, nesse caso, que o fluido pode ser dividido em duas regiões: uma em que o movimento do fluido é perturbado pela presença do objeto sólido, e outra em que o fluido escoa como se o objeto não estivesse presente. Uma seção, perpendicular às linhas de corrente, na região do fluido não perturbada pela presença do objeto, será denominada a partir de agora ‘seção ao longe ou no infinito’. Ao passar pelo corpo, o fluido provocará nele o aparecimento de uma força resultante. Essa força, supondo o escoamento bidimensional, poderá ser decomposta em duas componentes, que serão chamadas: a) resistência ao avanço ou força de arrasto (Fa), paralela às linhas de corrente ao longe; b) força de sustentação (Fs), que é a componente normal ou perpendicular às linhas de corrente ao longe (Figura 9.1). O objetivo fundamental deste capítulo é o estudo qualitativo e quantitativo dessas duas forças, propiciando ao leitor a possibilidade de desenvolver raciocínios que facilitem o desenvolvimento de estimativas, já que na maioria dos casos a determinação dessas forças é uma tarefa puramente empírica. Figura 9.1

<!-- p. 224 -->
As hipóteses gerais para o estudo dessas forças são: a) na seção ao longe as linhas de corrente são paralelas; b) na seção ao longe o diagrama de velocidades é uniforme; c) o regime é permanente; d) o fluido é incompressível; e) para a determinação das diferenças de pressão, desprezam-se as diferenças de cotas.

## 9.2 Conceitos fundamentais

Em cada ponto, a ação de um fluido numa superfície sólida pode-se decompor numa ação normal (pressão) e numa ação tangencial (tensão de cisalhamento) (Figura 9.2). Para facilitar a compreensão, o estudo pode ser realizado separando o efeito normal das pressões do efeito tangencial das tensões de cisalhamento. Figura 9.2 Inicia-se estudando os casos em que não existam tensões de cisalhamento por hipótese, de maneira que a força resultante se deva somente ao efeito das pressões. Em primeiro lugar, pode-se imaginar o fluido em repouso e, assim, já se sabe que a força resultante corresponde à diferença de pressões provocada pelas diferenças de cotas. Nesse caso, a resultante, denominada empuxo, já foi estudada no Capítulo 2, uma vez que é um problema de estática. Nesse capítulo, verificou-se que a direção do empuxo é vertical, com sentido para cima, e que a resultante na horizontal se anula, uma vez que a distribuição das pressões é simétrica. Num segundo caso, será estudado um fluido ideal, o que também implica a ausência de tensões de cisalhamento. Deseja-se verificar que a distribuição das pressões não é uniforme sobre o corpo, o que ocasiona o aparecimento de uma força resultante não-nula. A diferença de pressão de um ponto a outro do corpo será provocada pela diferença de velocidades do fluido. Figura 9.3 Por ser o fluido ideal, pode-se aplicar a equação de Bernoulli entre os pontos (1) e (2) de uma linha de corrente. Como o ponto (1) pertence à seção ao longe, v1 = vo. No ponto (2), o fluido incide na superfície sólida e pára. Como já foi visto, um ponto nessa condição denomina-se ponto de parada ou de estagnação; logo: v2 = 0.

<!-- p. 225 -->
A equação fica:

v12 2g + p1 γ + z1 = v 2 2 2g + p2 γ +z2 são Como p1 = p0 = pressão devidas às diferenças de ao longe, e não levando em consideração cotas, isto é, desprezando Δz:

p2 = v 2 0 + as p0 diferenças de presγ 2g γ ou multiplicando por γ e lembrando que γ = ρ g então: p2 = p0 + ρv 2 0 2 (9.1)

Se o fluido estivesse em repouso à pressão p0, o corpo mergulhado nele ficaria sujeito a essa pressão em todos os pontos e, por essa observação, a pressão que agiria em todos os pontos do corpo do fluido em repouso é denominada ‘pressão estática’.

Na Equação 9.1, o termo ρv 2 0 tem as dimensões de uma pressão e, como se deve ao efeito 2 da velocidade, é denominado ‘pressão dinâmica’.

Portanto: ρv 2 0 2 = p din e p0 = p est Em todos os pontos, o corpo fica sujeito a uma ‘pressão total’ que é a soma algébrica da pressão estática com a pressão dinâmica que, como se observou, é uma função da variação da energia cinética. Aplicando a equação de Bernoulli entre (3) e (4), tem-se:

v 2 3 2g + p3 γ +z3 = v 2 4 2g + p4 γ +z4 Como v3 = v0, p3 = p0, e não se considera z4 – z3 = Δz, então:

p4 = p0 + v 2 0 – v 2 4 γ γ 2g (9.2) Figura 9.4 No tubo de corrente mostrado na Figura 9.4, nota-se que o ponto (4) pertence a uma seção que, devido à presença do corpo, sofre um estreitamento; logo, pela equação da continuidade, v4 > v0 e, portanto:

v 2 0 – v 2 4 = Δ (v2 ) < 0

<!-- p. 226 -->
Dessa forma, multiplicando a Equação 9.2 por γ:

ρΔ (v 2 ) p4 = p0+ 2 < p0 Observam-se no corpo, então, pontos do tipo do ponto (2), em que a pressão é maior que a estática devido ao efeito da velocidade, e outros, como o ponto (4), em que a pressão é menor que a estática devido ao fato de parte da energia de pressão transformar-se em energia cinética. Esse desbalanceamento das pressões, que não existiria se o corpo estivesse em repouso, cria o aparecimento de uma força resultante não-nula que, decomposta, dá origem às forças de arrasto e sustentação citadas anteriormente (Figura 9.5). Figura 9.5 Para efeito de cálculo da força resultante, a soma não se altera subtraindo p0 de todos os pontos. Assim, a distribuição das pressões ficaria como a da Figura 9.6. Figura 9.6 Efetivamente, tudo se passa como se o corpo estivesse em alguns pontos sujeito a uma pressão positiva e, em outros, a uma pressão negativa. Ou, em termos relativos, parte da superfície do corpo é comprimida e, em outros, é succionada. Devemos lembrar que esse conceito é apenas relativo, já que na realidade a pressão é sempre um efeito contra a superfície do corpo, apenas a compressão é maior em alguns pontos do que em outros. Pode-se, agora, calcular a força resultante das pressões dinâmicas (relativas) numa direção qualquer, por exemplo, na direção de x (Figura 9.7). Figura 9.7 Como a pressão é uma entidade escalar, a força que age nurm elemento de área dA qualquer do corpo terá de ser orientada por um versor normal n, dirigido para fora, por convenção. Nesse caso:

rr dF = –pndA

<!-- p. 227 -->
rr rr Logo, na direção de x: dFx = –pdA (n × i ) = pdA (–n × i )

Pela Figura 9.8, observa-se que: dFx = pdA cos θ Figura 9.8 Verifica-se que dA cos θ é a projeção da dA na perpendicular a x, isto é, perpendicular à direção da força. Seja Por outro lado, viu-se que:

dA cos θ = dA x ρΔ (v2 )

p= 2 Logo:

ρΔ (v2 ) dFx = 2 dA x Para determinar a força resultante segundo x, deverá ser feita a integral para todos os dA. Logo: ∫ ρΔ (v2 ) Fx = 2 dA x Essa integração em geral esbarra na dificuldade de se obter matematicamente a distriρΔ (v2 )

buição de p = . É costume admitir uma expressão final que depende, por definição, de 2 um coeficiente de correção determinado empiricamente.

Logo: ∫ Fx = ρΔ (v2 ) 2 dA x =Cx ρv 2 0 A x 2 onde Cx é o coeficiente fluidodinâmico ou o coeficiente que permite que a expressão adotada venha a coincidir com o valor real de Fx. O coeficiente adimensional Cx pode ser obtido experimentalmente, pois se Fx = Cx ρv 2 0 A x 2 (9.3) então: Cx = 2Fx ρv 2 0 A x

<!-- p. 228 -->
Figura 9.9 A medida de Fx é feita por meio de um dinamômetro, como esquematizado na Figura 9.9. Logo, conhecendo ρ, vo, Ax e Fx, pode-se obter Cx. Outra coisa importante é o fato de que Ax pode ser substituído por outra área de referência qualquer, desde que o coeficiente C seja alterado, correspondentemente, de forma a satisfazer o valor da força real. Assim, de uma forma geral:

F = C ρv 2 0 A 2 (9.4)

onde F é a força fluidodinâmica na direção desejada, A é uma área de referência (na maioria das vezes projetada na perpendicular à direção de v0, mas não necessariamente) e C, o coeficiente adequado para que o segundo membro da Equação 9.4 produza o resultado correto para a força que se quer calcular. Note-se que, devido ao fato de C ser um adimensional, terá o mesmo valor para qualquer protótipo de um dado modelo. Este item teve o objetivo de mostrar a lógica de cálculo das forças fluidodinâmicas por uma expressão do tipo da Equação 9.4.

## 9.3 Força de arrasto de superfície

No item anterior, considerou-se fluido ideal, isto é, a ausência de tensões de cisalhamento. Verificou-se que, nesse caso, a força é causada pela resultante das pressões dinâmicas. No caso dos fluidos reais, a ação do atrito ou das tensões de cisalhamento irá causar um acréscimo na força resultante aplicada pelo fluido no sólido. Representa-se por Fas a força de arrasto de superfície, isto é, a força provocada pelas tensões de cisalhamento na superfície sólida (Figura 9.10). Figura 9.10 Pode-se obter Fas por:

∫ Fas = τdA τ onde Aτ = área da superfície do corpo onde agem as tensões de cisalhamento.

<!-- p. 229 -->
Na prática, é muito difícil separar a parcela da força de arrasto devido às pressões dinâmicas, denominada ‘força de arrasto de forma ou de pressão’, daquela provocada pelas tensões de cisalhamento. Entretanto, é bastante instrutivo estudá-las separadamente. Com essa finalidade, será realizado um estudo sucinto do caso limite, isto é, o caso da placa plana, muito fina, paralela ao escoamento, de forma que não aconteça nenhum efeito devido às pressões dinâmicas. Como foi visto, a força de arrasto de superfície é devida às tensões de cisalhamento que se desenvolvem na superfície, causadas pelo gradiente de velocidade ao longo das perpendiculares à placa. No Capítulo 7 foi visto que a região do fluido onde existe um gradiente de velocidade denomina-se camada limite. Sua existência é responsável pela força de arrasto de superfície. Ainda no Capítulo 7, verificou-se que a espessura da camada limite é variável (Figura 9.11). Figura 9.11 Da figura pode-se observar que o diagrama de velocidades varia ao longo da abscissa x, de forma que o gradiente dv/dy junto à placa é mais suave afastando-se do bordo de ataque. Tal fato mostra claramente que a tensão de cisalhamento é variável ao longo de x, de forma que: ∫ Fas = τdA Se a placa fosse retangular, de largura b constante, então:

∫x Fas = τbdx 0 A integração dessa equação resolveria o problema de determinação da força de arrasto de superfície, não fosse o fato de que τ é função de dv/dx, que não é conhecido. A determinação de Fas é, portanto, difícil e requer métodos matemáticos que não serão abordados. Se a camada limite for laminar, isto é, para Re < Recr ou L < xcr (ver Capítulo 7), ao fazer: ∫ F a s = L τbdx 0 = C a s ρv 2 0 bL 2 (9.5) Logo: ∫ C as 2 = ρv 2 0 L Lτdx 0 (9.6) E, ao aplicar os métodos matemáticos citados, obtém-se:

1,328 C as = Re L onde Re L = v0L ν e L é o comprimento da placa considerado.

(9.7)

Entretanto, em geral, o xcr é um valor muito pequeno e, normalmente, haverá a passagem da camada limite laminar para a turbulenta (Figura 9.12).

<!-- p. 230 -->
Figura 9.12 Os diagramas de velocidade na camada limite turbulenta são dados por uma expressão matemática diferente, e a integração da Equação 9.6 deverá ser realizada de outra maneira. Supondo que todos os diagramas fossem do tipo da camada turbulenta, desde o bordo de ataque, pode-se obter: C as = 0,074 5 Re L (9.8)

Entretanto, pelo fato de a camada limite ser laminar até xcr, o resultado da Equação 9.8 deverá ser corrigido. Note-se que, no caso da camada limite turbulenta, o gradiente de velocidade junto à placa é maior que na camada limite laminar, e a correção deverá ser subtrativa (Equação 9.9).

C as = 0,074 5 Re L k – Re L (9.9)

onde k = f(Recr) e é dado pela tabela a seguir, pois a extensão do trecho laminar depende do xcr. Recr 3 × 105 5 × 105 106 k 1.050 1.700 3.300 3 × 106 8.700 O valor de Recr será função da rugosidade da placa, da troca de calor entre ela e o fluido, das turbulências ao longe e de outros fatores que possam facilitar ou dificultar a passagem da camada limite de laminar para turbulenta. Para Re > 107, Schlichting verificou que o valor de Cas é mais bem representado por 0,455 k Cas = (log Re L )2,58 – Re L (9.10)

Os resultados das equações 9.9 e 9.10 são bastante próximos e pode-se utilizar indiscriminadamente a Equação 9.9. A Equação 9.5, associada à Equação 9.7, se o comprimento da placa for menor que xcr, ou à Equação 9.9, em caso contrário, permite calcular a força de arrasto de superfície em placas planas ou em superfícies onde o raio de curvatura seja grande. Note-se que, pela Equação 9.5, calculou-se a força de arrasto num dos lados da placa. Se esta estiver submersa, a ação será dupla e a área A = bL deverá ser multiplicada por dois. Uma placa plana retangular de 1 m de largura e 2 m de comprimento, imersa em água (ρ = 1.000 kg/m3 e ν = 1,5 × 10–6 m2/s), é arrastada horizontalmente com velocidade constante de 1,5 m/s. Calcular a força necessária, supondo os três casos seguintes:

<!-- p. 231 -->
a) a camada limite mantém-se laminar desde o bordo de ataque até o bordo de fuga; b) a camada limite é turbulenta desde o bordo de ataque; c) o número de Reynolds crítico é 5 × 105. Solução A força deverá ser igual à resistência ao avanço ou à força de arrasto. Em qualquer um dos casos: Fa s = 1 2 C a s ρv02A onde A é duas vezes a área da placa, pois as tensões de cisalhamento agem de ambos os lados. A alteração que se tem em (a), (b) e (c) será em relação ao Ca . s Logo: Fa s = 1 2 C a s 1.000 × 1,52 × 2× 2× 1= 4.500 Cas a) se a camada limite é totalmente laminar, tem-se:

Cas = 1,328 ReL ReL = v0L n = 1,5 × 2 1,5 × 10−6 = 2 × 10−6 Cas = 1,328 = 9,4 × 10–4 2 × 106 Fa s = 4.500 C a s = 4.500 × 9,4 × 10–4 Fa s = 4,23 N b) se a camada limite fosse totalmente turbulenta, o cálculo do Ca s seria dado pela Equação 9.8 sem correção, isto é: Ca s = 0,074 5 Re L = 0,074 5 2 × 106 = 4,06 × 10−3 Fa s = 4.500 Ca s = 4.500 × 4,06 × 10–3 Fa s = 18,3 N c) se Recr = 5 × 105, significa que na abscissa:

xcr = Re cr v0 ν = 5× 105 × 1,5 × 1,5 10−6 = 0,5 m haverá a passagem de laminar para turbulento.

Logo, nem o resultado do item (a) nem o do item (b) são reais; o certo será utilizar a Equação 9.9 com a correção devido à existência do trecho laminar. É óbvio que o desvio entre (c) e (b) será muito menor que o entre (c) e (a), pois o trecho laminar é muito pequeno. Ca s = 0,074 5 Re L − k Re L Da tabela, para Recr = 5 × 105, obtém-se k = 1.700. Logo:

Ca s = 4,06 × 10–3 – 1.700 2 × 106 = 3,21× 10–3 Fa s = 4.500 C a s = 4.500 × 3,21 × 10–3 Fa s = 14,4 N Nesse caso, o erro cometido ao se considerar a camada limite totalmente turbulenta será: erro = 18,3 – 14,4 × 100 = 21,3% 18,3

<!-- p. 232 -->
É claro que o erro será tanto menor quanto menor for o xcr em relação ao comprimento total da placa ou, em outras palavras, quando o comprimento do trecho da camada limite laminar for desprezível comparado com o da camada limite turbulenta.

## 9.4 Força de arrasto de forma ou de pressão

Para ilustrar a existência da força de arrasto de forma ou de pressão, será utilizada a descrição do escoamento em torno de um cilindro, já que a simetria permite uma explicação mais simples. Figura 9.13 Se o escoamento fosse perfeitamente simétrico (Figura 9.13), as pressões teriam uma distribuição também simétrica, de forma que não haveria nenhum saldo em favor devido a elas. Note-se, porém, que, no escoamento, a seção inicialmente indicada por (A) sofre uma diminuição até um mínimo em (A'), havendo, portanto, uma aceleração das partículas do fluido, que serão posteriormente desaceleradas a partir de (A'), já que a seção aumenta novamente. Não esquecer que, ao aumentar a velocidade, a pressão diminui, e vice-versa. Logo, o fluido desloca-se até (A') com uma variação negativa da pressão, que alcança um mínimo na posição de velocidade máxima, passando em seguida a crescer no sentido do escoamento. A Figura 9.14a mostra como, na realidade, apresenta-se a Figura 9.13, e a Figura 9.14b mostra a ampliação da região próxima da seção (A'), onde acontece a maior velocidade. Figura 9.14 Seja o escoamento acelerado até o ponto C. Daí para a frente, o fluido desacelera-se e a pressão aumenta. Esse fenômeno denomina-se ‘gradiente adverso de pressões’. Devido à dissipação de energia, causada pelos atritos dentro da camada limite, a velocidade não retorna ao seu valor inicial, havendo uma diminuição dela em D e uma parada logo adiante, já que junto à superfície sólida as velocidades são baixas. Daí em diante, o aumento da pressão exigiria uma ulterior desaceleração, o que é impossível, pois o fluido próximo à superfície sólida parou. Nesse caso, a camada limite descola da superfície sólida. No ponto E haveria um retorno de fluido no sentido das pressões decrescentes, que viria a encher o vazio deixado pelo descolamento da camada limite. Isso na realidade não se observa, e a jusante do ponto de descolamento o escoamento caracteriza-se por uma região de redemoinhos chamada esteira do descolamento. Tal região pode ser perfeitamente observada, por exemplo, na traseira de um barco em movimento.

<!-- p. 233 -->
A uma certa distância do sólido, os redemoinhos extinguem-se pelo efeito da viscosidade. Na esteira, o fluido não tem praticamente movimento de translação, podendo-se chamar essa região de fluido morto, como foi feito no Capítulo 8 no caso de diafragmas e bocais. Como os redemoinhos não podem retransformar a sua energia cinética em energia de pressão, a pressão na esteira permanece praticamente igual àquela da região do descolamento, que é próxima da mínima. Logo, o sólido fica na sua parte dianteira sujeito a pressões maiores que na sua parte traseira, tendo como resultante das pressões uma força no sentido do escoamento: é a força de arrasto de forma ou de pressão. A Figura 9.15 ilustra a distribuição das pressões em torno de um cilindro de eixo normal ao escoamento. Figura 9.15 Se a pressão ao longe for atmosférica e se adotar escala efetiva, na face esquerda haverá uma compressão e na direita, uma sucção, produzindo uma resultante com o sentido indicado. Note-se que o fenômeno acontece tanto com camada limite laminar como com turbulenta. Entretanto, o tipo de escoamento influi na posição do descolamento. Como no movimento laminar cada partícula desloca-se com uma trajetória individual, as que estão próximas à superfície, ao encontrar o gradiente adverso de pressões, não têm um suprimento adicional de energia para enfrentá-lo. Logo, quando a camada limite é laminar, o descolamento acontece de imediato ao encontrar o gradiente adverso. Se a camada limite for turbulenta, tal não acontece, pois a troca de energia entre as partículas, devida aos movimentos transversais ao escoamento, fornece um suprimento adicional de energia que facilita a penetração do escoamento pelo gradiente adverso. A Figura 9.16 mostra a formação da esteira no escoamento com a camada limite laminar (a) e no escoamento com a camada limite turbulenta (b). Por essa consideração, é óbvio que na passagem de laminar para turbulento há uma queda brusca da força de arrasto. Como já foi visto, a força de arrasto de forma ou de pressão será dada por:

Fap = C ap ρv 2 0 2 A Figura 9.16

<!-- p. 234 -->
## 9.5 Força de arrasto total

No caso geral, não é praticável nem interessante separar nos cálculos os dois tipos de força de arrasto. A força de arrasto total é a soma das forças de arrasto de forma e de superfície. Fa= Fas + Fap Uma nunca aparece separada da outra, apesar de, em certos casos, uma poder ser muito pequena quando comparada à outra. De qualquer forma: Fa = Ca ρv 2 0 2 A (9.11)

onde Ca será dado por C as (equações 9.7 e 9.9) no caso de placas planas paralelas ao escoamento e experimentalmente em qualquer outro caso. Note-se que v0 e A podem ser a velocidade ao longe e a área projetada num plano normal ao escoamento, mas também podem ser uma velocidade e uma área de referência. Quando esse segundo caso acontecer, deverá ser informado, pois o valor do Ca terá de ser alterado de forma a obter um resultado coerente para Fa. A seguir será estudada a variação do coeficiente de arrasto para uma esfera lisa, caso este bastante elucidativo.

A Figura 9.17 mostra a variação do coeficiente de arrasto para uma esfera lisa, em função do número de Reynolds.

Figura 9.17 I — Para Re < 1, o escoamento é dito ‘lento’, e o Ca, num diagrama dilogarítmico, varia linearmente com o número de Reynolds. Nesse caso, pode-se verificar que: 24 Ca = Re (9.12)

Nessa situação, não acontece o descolamento, e a força de arrasto é praticamente devida somente às tensões de cisalhamento (Fas). Pelas equações 9.11 e 9.12:

Figura 9.18

<!-- p. 235 -->
Fa = 24 ρ v 2 0 Re 2 A Mas: πD 2 A= (área projetada da esfera = círculo)

4 Fa = 24ν ρ v 2 0 v0D 2 πD 2 4 Fa = 3πμv0D (9.13)

Essa equação foi utilizada no Capítulo 8 para determinar a força de arrasto, para o viscosímetro de esfera.

II — Para Re > 1, a camada limite começa a descolar na traseira e o arrasto de forma começa a crescer de importância, tornando-se proporcional a v 2 0 . Ao aumentar o Re, o descolamento vai se estendendo para a parte dianteira da esfera, até que, em Re ≅ 1.000, o ponto de separação fixa-se aproximadamente a 80o do ponto de estagnação.

Figura 9.19 III — Para 103 < Re < 3,5 × 105, o ponto de descolamento mantém-se aproximadamente fixo eIVCa—sePráarcaoRnest≅an3t,e5,×v1a0le5,nndootaa-psreouxmimaaqduaemdeanbtreu0s,c4a5d. o Ca. A explicação é a passagem da camada limite de laminar para turbulenta e, conforme foi visto na Figura 9.16, há um salto do ponto de descolamento da parte dianteira para a parte traseira da esfera. O ponto de descolamento irá se localizar aproximadamente a 115o do ponto de estagnação. Figura 9.20 Note-se que esses resultados são para a esfera lisa. As turbulências podem ser induzidas artificialmente, tornando a superfície rugosa e com isso diminuindo o valor de Ca. É óbvio que isso faz aumentar o arrasto de superfície, mas nesse caso ele é secundário e é plenamente compensado pela diminuição do arrasto de forma. Exemplos desse efeito podem ser observados nas bolas de tênis ou de golfe, que não são lisas exatamente para induzir a uma camada limite turbulenta. Nesse ponto, é fácil entender por que se utilizam corpos de forma alongada, ditos aerodinâmicos, para aplicações em que a força de arrasto deve ser a menor possível. Tais corpos permitem que a camada limite e as trajetórias das partículas os contornem com facilidade, não causando acelerações muito bruscas que criariam um elevado gradiente adverso de pressões e, conseqüentemente, um grande descolamento. Dessa forma, ao alongar suavemente os corpos, a força de arrasto será relativamente baixa, pois o descolamento acontecerá na traseira, numa área pequena. O alongamento do corpo causa, porém, um acréscimo do arrasto de superfície e, portanto, a melhor forma aerodinâmica é aquela que causa a menor soma dos dois efeitos, o de forma e o de superfície.

<!-- p. 236 -->
Contrariamente aos corpos aerodinâmicos, tem-se os corpos ‘abruptos’, que oferecem grande resistência ao avanço. Como exemplo, pode-se citar uma placa plana perpendicular ao escoamento. Nesses corpos, o coeficiente de arrasto, para Re > 100, é praticamente constante (Figura 9.21) e em geral pode ser adotado aproximadamente 1,2. Figura 9.21 Os valores dos coeficientes de arrasto referentes a diversos corpos, para diferentes Re, podem ser encontrados na literatura especializada. Qual será a máxima velocidade de descida de um pára-quedista que pesa com seu equipamento 1.200 N, sendo que o pára-quedas tem um diâmetro de 6 m e um coeficiente de arrasto igual a 1,2? De que altura 1,2 kg/m3)

se deveria saltar sem pára-quedas para chegar ao solo com a mesma velocidade? (ρar = Solução Sabe-se que a força de arrasto aumenta com a velocidade; logo, o pára-quedista atingirá a máxima velocidade quando o seu peso for equilibrado pela força de arrasto. Assim: Mas: Fa = G Fa = C a ρ v20 2 A onde A = área projetada num plano perpendicular ao escoamento, isto é: A = πD2 (área do círculo do pára-quedas) 4 Ca ρ v02 2 πD2 4 = G ou vo = 8G C aρπD2 = 8 × 1.200 1,2 × 1,2π × 62 = 7,7 m/s Saltando sem pára-quedas, a resistência do ar será desprezível. Trata-se de calcular a altura de queda livre de um corpo para que alcance no solo uma velocidade de 7,7 m/s. Pode-se utilizar a expressão: v = 2gh Logo:

h = v2 = 7,72 = 2,93 m 2g 20

<!-- p. 237 -->
## 9.6 Força de sustentação

A teoria da força de sustentação envolve conceitos não abordados neste livro, como o conceito de circulação, que o leitor poderá consultar na literatura a respeito. O item será abordado de forma mais prática, sem esses conceitos. A força de sustentação pode estar presente em qualquer objeto; entretanto, o corpo destinado a provocar propositadamente essa força é o aerofólio ou perfil de asa. A explicação qualitativa mais elementar do aparecimento da força de sustentação é o fato de a velocidade do fluido ser diferente nas duas faces do aerofólio, provocando o diferencial de pressões causador de uma força resultante perpendicular à direção do movimento (Figura 9.22a). Tal fato, que pode ser deduzido pela equação de Bernoulli, é mostrado na Figura 9.22b. Figura 9.22 A diferença de pressão entre as faces do aerofólio resulta numa força para cima ou de sustentação, que, por analogia com as expressões apresentadas para a força de arrasto, poderá ser calculada por: Fs = C sρ v 2 0 2 A onde: A = área de referência e Cs = coeficiente de sustentação. A Figura 9.23 mostra a nomenclatura para o caso de um aerofólio. Figura 9.23 No caso do aerofólio, a área de referência é dada por:

A = corda × envergadura = c × e A utilização da corda externa ou interna depende das normas utilizadas.

Assim, no caso de aerofólios, as forças de arrasto e de sustentação são dadas, respectivamente, por: Fa = Ca ρv 2 0 ce 2 Fs = Cs ρv 2 0 ce 2

<!-- p. 238 -->
A linha média do aerofólio é chamada linha de camber e o ângulo formado entre a corda e a direção do escoamento é o ângulo de ataque (Figura 9.24). Figura 9.24 O ‘camber’ máximo deve ser maior para se obter sustentação em baixas velocidades; nas altas, poderá ser menor. Como o Cs é função do ângulo de ataque, experimentalmente é feita a determinação dessa variação, que é representada em gráficos (Figura 9.25). Figura 9.25 Na Figura 9.25, observa-se que mesmo para um ângulo de ataque nulo ainda há uma sustentação positiva em virtude do ‘camber’ do aerofólio. Se este fosse simétrico (camber = 0), então o gráfico passaria pela origem. Conforme o ângulo de ataque aumenta, chega-se a uma condição em que o aerofólio comporta-se como corpo abrupto, isto é, a camada limite descola totalmente, provocando um aumento sensível da força de arrasto e uma diminuição brusca da força de sustentação. Nessa situação, diz-se que o aerofólio estola (stall). Uma curva que representa bem as características de um aerofólio é o diagrama polar, em que se lança Cs = f(Ca) utilizando o ângulo de ataque como parâmetro (Figura 9.26). Figura 9.26

<!-- p. 239 -->
Os pontos notáveis do diagrama estão indicados nele próprio. Note-se que, ao traçar linhas a partir da origem (pólo) até os pontos da curva, obtêm-se, com o eixo dos Ca, ângulos θ cuja tangente corresponde a Cs/Ca. Logo, o máximo ângulo θ corresponde ao (Cs/Ca)max, e ao se traçar uma tangente da origem à curva pode-se determinar o ângulo de ataque para o melhor rendimento do perfil. Esses diagramas são obtidos por ensaios em túneis aerodinâmicos e são apresentados em normas e manuais. 9.1 Deixa-se cair livremente uma esfera de massa específica 2.040 kg/m3 num tanque que contém glicerina de massa específica 1.290 kg/m3 e viscosidade cinemática 2,7 × 10–2 m2/s. A velocidade final constante da esfera é tal que Re = 0,1. Qual é a força de arrasto na esfera e qual é a velocidade final? Resp.: Fa = 0,873 N; v = 4,4 cm/s 9.2 Uma esfera de 15 cm de diâmetro é colocada numa corrente de ar de ρ = 1,2 kg/m3. O dinamômetro indica uma força de 1,14 N. Qual é a velocidade do ar? (νar = 10–5 m2/s)

Resp.: v = 15,5 m/s 9.3 Um balão contém hélio e é lançado no ar, que no local tem massa específica 1,2 kg/m3. O balão mais os acessórios pesam 240π N. Escolher, entre os diâmetros indicados a seguir, aquele que permite uma ascensão com a velocidade mais próxima de 10 m/s. Escolhido o diâmetro, verificar qual será a velocidade real de subida, supondo o coeficiente de arrasto 0,266. Se o balão é ancorado ao solo e é atingido por um vento de 36 km/h, determinar o ângulo que o cabo de ancoragem formará com o solo. Diâmetros (m): 4,8; 5,2; 5,6; 6,0; 6,4. Resp.: D = 5,6 m; v = 9,43 m/s; α = 41,6o 9.4 Os testes com um automóvel revelaram que ele tem um coeficiente de arrasto constante igual a 0,95. A área projetada é considerada 2,52 m2. Construir o gráfico da potência necessária para vencer a resistência do ar em função da velocidade. (ρar = 1,2 kg/m3) 9.5 Num viscosímetro de esfera, uma esfera de aço de massa específica ρ = 7.800 kg/m3 e diâmetro 1 mm afunda num líquido de massa específica ρ = 800 kg/m3, com uma velocidade limite de 2 cm/s. Calcular a viscosidade cinemática do fluido. Resp.: ν = 2,43 cm2/s 9.6 No teste de um veículo, num túnel aerodinâmico, foi levantada a curva de potência gasta para vencer a força de arrasto do ar em função de sua velocidade. Sendo a vista frontal do veículo indicada na figura, determinar o seu coeficiente de arrasto. Dados: ρar = 1,2 kg/m3; Área A = 0,72 m3; Área B considerada retangular. 1,5 m A B 20 cm Pot (CV) 30 1,0 m 20 17,5 10 15 cm Resp.: Ca = 0,44 20 40 60 80 100 120 v0 (km/h)

<!-- p. 240 -->
9.7 Deseja-se impulsionar uma embarcação de 105 N de peso à velocidade de 72 km/h. A embarcação é sustentada por uma asa submarina cujos coeficientes de sustentação e arrasto são, respectivamente, 0,7 e 0,06. Determinar: a) a área da asa; b) a potência necessária para a propulsão. Resp.: A = 0,714 m2; N = 171 kW 9.8 Uma gota de chuva tem diâmetro médio de 2,5 mm. Calcular a velocidade limite da gota se o ar tem ρ = 1,2 kg/m3 e ν = 1,8 × 10–6 m2/s. Resp.: vo = 7,9 m/s 9.9 Água escoa sob uma placa plana de 10 cm de comprimento e 20 cm de largura, com uma velocidade de 0,1 m/s. Determinar a força de arrasto que age na placa. (ν = 10–6 m2/s e ρ = 1.000 kg/m3) Resp.: Fa = 133 dina 9.10 Uma barcaça de casco chato de 20 m de comprimento e 7 m de largura está imersa em profundidade de 1,5 m e deve ser empurrada com uma velocidade de 3,6 km/h. Estimar a potência necessária para efetuar o serviço se ν = 10-6 m2/s e ρ = 1.000 kg/m3. Resp.: N = 6,5 kW 9.11 A asa de um avião tem 7,5 m de envergadura e 2,1 m de corda. Estimar a força de arrasto na asa utilizando os resultados para o escoamento sobre uma placa plana e admitindo a camada limite turbulenta desde o bordo de ataque, quando o avião voa a 360 km/h. Qual seria a redução de potência necessária se fosse feito o controle da camada limite de forma a assegurar escoamento laminar até o bordo de fuga? (ν = 10–5 m2/s; ρ = 1,0 kg/m3) Resp.: Fa = 407 N; 88,3% 9.12 Determinar a relação entre a velocidade constante de subida de uma bolha de ar de diâmetro 1 mm dentro da água e a velocidade constante de descida de uma gota de água de mesmo diâmetro no ar. Dados: ρar = 1,0 kg/m3; ρH2O = 1.000 kg/m3; Ca = 0,5. Resp.: vH2O = 31,6 var 9.13 Uma placa de 0,9 m × 1,2 m move-se com 13,2 m/s em ar parado, com uma inclinação de 12° com a horizontal. Sendo Ca = 0,17; Cs = 0,72; ρ = 1,2 kg/m3; A = área de referência = área da placa, determinar: a) a força resultante exercida pelo ar sobre a placa; b) a força de atrito; c) a potência necessária para manter a placa em movimento.

Resp.: a) F = 83,5 N; b) 1,9 N; c) 0,25 kW 9.14 Um anemômetro, utilizado para medir a velocidade do vento, consiste de duas semi-esferas ocas montadas em sentidos opostos sobre dois braços iguais, que podem girar livremente quando montados sobre um eixo vertical. Qual é o momento necessário para manter o dispositivo estacionário, quando o vento tem uma velocidade de 36 km/h? (ρar = 1,0 kg/m3) Resp.: M = 0,097 N.m

<!-- p. 241 -->
9.15 Um avião pesa 18 kN e tem uma área de asa de 27 m2. Qual deverá ser o ângulo de ataque das asas a uma velocidade de 160 km/h? Supor que o coeficiente de sustentação varie linearmente de 0° a 6° desde 0,35 até 0,8. (ρ = 1,2 kg/m3) Resp.: α = 2,8° 9.16 Um papagaio pesa 1 N e tem uma área de 74,4 dm2. A tensão na linha é 30 N quando ela forma um ângulo de 45° com a direção do vento. Para um vento de 36 km/h, quais serão os coeficientes de arrasto e de sustentação, a fim de que o papagaio forme um ângulo de 30° com a horizontal? (ρar = 1,2 kg/m3. Considerar o peso aplicado no centro geométrico e adotar a área projetada como área de referência.) Resp.: Ca = 0,95; Cs = 1

<!-- p. 242 -->

# Capítulo 10 — Generalização das equações integrais para regime variado

## 10.1 Introdução

Nos capítulos 3, 4 e 5 foram apresentadas as equações da continuidade, da energia e da quantidade de movimento mantendo-se a hipótese de regime permanente. Essa abordagem permite que o leitor se familiarize com os termos dessas equações sem o envolvimento da variação com o tempo, já que essa hipótese permite que o fluido observado e suas propriedades tenham a imagem repetida em todos os instantes. Nos capítulos mencionados, em primeiro lugar, foi realizado um estudo para um tubo de corrente, para limitar o estudo do fluxo a apenas duas seções: uma de entrada e uma de saída. Posteriormente, as três equações foram generalizadas para diversas entradas e saídas. Para facilitar a generalização, neste capítulo, serão explicitados os conceitos de sistema e volume de controle, que naqueles capítulos ficaram apenas implícitos. Sistema é uma porção fixa e definida de matéria (Figura 10.1).

Figura 10.1 O estudo das propriedades do sistema baseia-se exatamente no fato de que não há troca de massa entre ele e o meio através da fronteira, sendo sempre constituído das mesmas partículas. As grandezas associadas a um sistema, como velocidade, aceleração, volume, energia, temperatura e outras, deverão ser determinadas em cada instante ao longo de sua trajetória, pelo método denominado lagrangeano.

A Figura 10.2 mostra a evolução de um sistema aro longo de sua trajetória, em que o objetivo seria, por exemplo, o de determinar a velocidade v do seu centro de gravidade em função da sua posição no espaço em cada instante.

r Logo:

v = f (x, y, z, t)

<!-- p. 243 -->
C a p í t u l o 1 0 z Generalização das equações integrais para regime variado z 243 Figura 10.2 O método lagrangeano pode ser utilizado na Mecânica dos Fluidos; entretanto, na maioria dos problemas em que se lida com conjuntos de partículas, pode ser difícil identificar o sistema ao longo do movimento ou pode não interessar a obtenção de previsões sobre suas propriedades futuras. Por exemplo, escolhendo como sistema em estudo uma porção de fluido na entrada de uma bomba, ficará difícil acompanhá-la até a saída e então identificá-la, pois a agitação provocada pelo rotor da bomba fará com que suas partículas se separem (Figura 10.3). Figura 10.3 Um outro exemplo que ilustra o que foi dito corresponde ao estudo dos gases expelidos por um foguete, cujas propriedades são importantes para a propulsão. Nesse caso, as propriedades do gás só interessam no instante da saída, não importando conhecê-las no futuro, quando já tiverem se afastado d%0o foguete e se espalhado no espaço (Figura 10.4). Figura 10.4 Pelo exposto, nota-se que o método lagrangeano é de maior importância no estudo de sólidos, que se mantêm coesos e para os quais se deseja determinar as propriedades ao longo da trajetória, com o passar do tempo. No caso do estudo dos fluidos, é mais interessante lembrar que, sendo o escoamento contínuo, o observador poderá fixar a sua atenção numa região do espaço por onde o fluido estiver passando e, nela, determinar as propriedades da porção de fluido que em cada instante estiver ocupando essa região. É claro que, se as informações obtidas na região não forem suficientes, o observador poderá voltar a sua atenção a tantas outras regiões quantas forem necessárias, ao longo do escoamento.

<!-- p. 244 -->
Essa região denomina-se volume de controle (VC) e em cada instante é ocupada por diferentes sistemas. Portanto, volume de controle (VC) é uma região do espaço em que se fixa a atenção para o estudo das propriedades do fluido que passa por ela em cada instante. A fronteira do volume de controle denomina-se superfície de controle (SC). Por exemplo, no caso da bomba da Figura 10.5, o observador não se preocuparia em acompanhar o sistema que entra por (e), uma vez que já vimos que seria difícil localizar em (s). Ele se preocupará com as propriedades nas seções (e) e (s), no mesmo instante, verificando a sua variação entre a entrada e a saída da bomba. O observador poderá, por exemplo, fazer leituras simultâneas de manômetros instalados nas duas seções. No caso do foguete, o volume de controle seria fixado na seção de saída dos gases, onde, em cada instante, suas propriedades seriam responsáveis pela propulsão. O observador não se preocuparia com a evolução das propriedades do sistema (1) que abandona o foguete, mas com as propriedades dos diversos sistemas, que em cada instante ocupam o volume de controle escolhido. Em termos reais, seria possível imaginar diversos sensores na seção de saída, que em cada instante registrariam as propriedades do gás de exaustão do foguete. Dependendo das necessidades do estudo, o volume de controle pode ser fixo em relação a um sistema de referência inercial adotado, podendo ser móvel ou deformável se toda a superfície de controle ou parte dela se mover durante a observação. Esse método denomina-se euleriano e, no caso do estudo de fluidos, mostra-se mais adequado que o lagrangeano, cujo equacionamento procura acompanhar o sistema ao longo de sua trajetória. Nos capítulos 3, 4 e 5, nas equações da continuidade, da energia e da quantidade de movimento, já se usou esse método sem explicitá-lo, em primeiro lugar adotando um volume de controle especial, isto é, um tubo de corrente, e posteriormente analisando diversas entradas e saídas. Entretanto, na ocasião, adotou-se constantemente a hipótese de regime permanente. Neste capítulo, deseja-se generalizar aquelas equações para a aplicação em regime variado e reduzir as restrições estabelecidas nos capítulos mencionados. É claro que, dentro das hipóteses estabelecidas, as equações já apresentadas são válidas para a solução dos problemas. Figura 10.5

<!-- p. 245 -->
C a p í t u l o 1 0 z Generalização das equações integrais para regime variado z 245

## 10.2 Vazão generalizada

No Capítulo 3 já foram apresentadas as definições de vazão em volume, massa e peso. Naquele capítulo apelou-se para a intuição do leitor, afirmando-se que a vazão é o volume, massa ou peso que passam através de uma certa seção, por unidade de tempo. Note-se que, ao se analisar o fluido atravessando uma seção, utiliza-se o método euleriano, fixando o observador num VC e olhando o fluido passar através da SC. Na realidade, pelo método lagrangeano não é possível estabelecer a idéia de vazão, já que, ao acompanhar o sistema ao longo da trajetória, não há como observar o fluxo através de uma seção pré-selecionada. É, portanto, no método euleriano que surge essa idéia, observando o fluido atravessar a SC de um VC adequadamente escolhido para a solução de um dado problema. Na Figura 10.6a escolheu-se um VC no interior do escoamento de um fluido e, no instante inicial tV0, observa-se o sistema fluido que coincide com aquele. Deixando passar um pequeno intervalo de tempo Δt, esse sistema desloca-se ao longo de sua trajetória, saindo parcialmente do VC e atravessando a SC. Supondo o fluido um meio contínuo, o espaço liberado pelo sistema inicial passará a ser ocupado por um novo sistema. Figura 10.6 É nessa situação que as definições de vazão em volume, massa e peso assumem o seu significado,%0 isto é, são o volume, a massa ou o peso que atravessam uma seção da SC por unidade de tempo. No Capítulo 3, quando se definiram as vazões e o seu relacionamento com a velocidade do fluido, admitiu-se implicitamente que a massa específica fosse uniforme em todos os pontos da seção e que os vetores da velocidade fossem perpendiculares a ela. Essas hipóteses, se bem que restritivas, referem-se à grande maioria dos problemas e atingem os objetivos daqueles capítulos, nos quais se desejava estabelecer conceitos simples. Entretanto, desejando-se estabelecer equações gerais, é necessário não impor nenhuma restrição. Nesse caso, seria admitida a possibilidade de qrue a massa específica fosse variável nos pontos onde o fluido atravessa a SC e que o vetor v, além de variável, possa não ser perpendicular à seção. Além disso, a superfície de controle pode ser móvel em relação a um sistema de referência adotado e, nesse caso, o que interessa é a velocidade do sistema fluido em relação à superfície de controle e não em relação ao sistema de referência, isto é, o que interessa é a velocidade relativa e não a absoluta. Lembre o leitor dessa observação, pois, para não complicar a notação, não será utilizado o índice r para indicar o uso da velocidade relativa. Para o cálculo da vazão em massa na entrada e saída do VC, serão ampliadas essas seções da Figura 10.6b.

<!-- p. 246 -->
Como a massa específica e a velocidade podem ser diferentes de um ponto a outro, será adotado um ponto na SC (Figura 10.7). Figura 10.7 únicoNrvoeeunmtorúnnoicdoovpaolnotrodéeaρd.otada uma área infinitesimal dA para garantir que existam um Lembrando que o volume de um prisma é calculado por: dV = Área da base (dA) ×Altura (dh)

então, a massa que atravessa o dA no intervalo de tempo dt será:

dm = ρdV = ρdA dh Cormo a altura está na direção perpendicular à base dA, essa direção é obtida por um versor n, como já foi feito no Capítulo 5.

r Sendo a distância percorrida pelo fluido na direção de v dada por:

ds = vdt então:

dh = ds cos θ= vdt cos θ ou dm = ρdA v cos θ dt dm e como a vazão em massa através do dA éd:Qm = dt então:

dQVm = ρv dA cos θ rr rr Note-se que: v× n = v . 1 . cos (v, n) =v r . cos r θ = vn então:

dQm = ρv × ndA = ρvn dA onde vVn é a componente da velocidade segundo o versor da normal r n, isto é, v . cos θ. Logo, a vazão em massa na seção de saída do VC será:

Qms = ∫ ρvn dA = ∫ ρv cos θ . dA = ∫ ρvr × r ndA SC Saída SC Saída SC Saída (10.1)

A Figura 10.8 mostra a situação na entrada do VC.

<!-- p. 247 -->
C a p í t u l o 1 0 z Generalização das equações integrais para regime variado z 247 Figura 10.8 Seguindo o mesmo raciocínio, obtém-se:

Qme = ∫ ρrv × r ndA = ∫ ρvn dA = ∫ ρv cos θ . dΑ SC entrada SC entrada SC entrada (10.2) Como r n é sempre dirigido para fora, no caso da entrada, o ângulo θ será maior que 90°, correspondendo a um cosseno negativo.

É claro que a vazão em si é sempre um valor positivo; entretanto, o sinal indicará se ela é de entrada ou de saída.

Diante disso, a vazão em massa na entrada ou na saída do VC será dada por:

Qm = ∫ ρrv × r ndA = ∫ ρv . cos θ . dA = ∫ ρvn dA (10.3) SC SC SC com o sinal determinado pelo cos θ.

Lembrar que a vazão em volume é a vazão em massa dividida pela massa específica ρ; logo: Q = ∫ r v × r ndA = ∫ v . cosθ . dA = ∫ vn dA (10.4) SC SC SC r Não esqueçer que, se a superfície de controle estiver em movimento, a velocidade v deverá sAelrésmubdsististou,íadaexpisetlêanvceialodceidrva×denr em relação à SC. diferente de zero, numa seção de entrada ou de saída do VC, caracterizaruma passagem de fluido através da superfície de controle que é denominada fluxo do vetor v .

## 10.3 Equação da continuidade na forma integral para volume de controle

Ao generalizar as equações, devem ser eliminadas as suas restrições. No Capítulo 1 definiu-se a massa específica ou densidade como: ρ=m v Essa definição parte do pressuposto de que a substância seja homogênea, isto é, com ρ uniforme em todo o volume; caso contrário, a massa específica, assim determinada, representaria apenas o valor médio. Se a massa específica variar de um ponto a outro, a sua definição deverá se referir a um volume infinitesimal em volta de um ponto, isto é: ρ = dm dV (10.5)

<!-- p. 248 -->
Nesse caso, para determinar a massa do sistema será necessário efetuar uma integração: ∫ m sis = ρ dV (10.6) Vsis onde o índice VVsis significa que a somatória, realizada através da integral, deverá ser estendida a todo o volume do sistema.

Seja um trecho de escoamento de fluido que se deseja estudar (Figura 10.9a).

Figura 10.9 Para esse estudo adota-se no instante tV0 um volume de controle adequado às necessidades e, nesse instante, haverá um sistema coincidindo com o volume. Estando o fluido em movimento no instante tV0 + Δt, o sistema se deslocará em relação ao volume de controle, que poderá ser fixo ou deformável (Figura 10.9b). O movimento relativo do sistema produz três regiões distintas. A região I representa a porção do sistema que desencontrou com o VC, a região II, a que ainda coincide com o VC no instante tV0 + Δt, e a região III, o novo sistema que ocupa no VC o espaço deixado pelo sistema inicial. Note-se que, ao observar a evolução do sistema ao longo de sua trajetória, usa-se o método lagrangeano, enquanto ao observar os acontecimentos no VC usa-se o método euleriano. No instante tV0:

m sis (t 0 ) = m VC (t 0 )

(10.7)

onde mVVC (tV0) significa a massa contida no VC no instante tV0, enquanto mVsis(tV0) significa a massa do sistema observada no instante tV0. No instante tV0 + Δt:

m VC (t 0 + Δt) = m II + m III Mas:

m II = m sis (t 0 + Δt) – m I Substituindo a Equação 10.9 na Equação 10.8, obtém-se:

(10.8) (10.9)

m VC (t 0 + Δt) = m sis (t 0 ) – m I + m III (10.10)

Logo, a variação da massa contida no VC, no intervalo de tempo Δt, será obtida pela diferença entre as equações 10.10 e 10.7. m VC (t 0 + Δt) – m VC (t 0 ) = m sis (t 0 + Δt) – m I + m III ou m sis (t 0 + Δt) – m sis (t 0 ) = m VC (t 0 + Δt) – m VC (t 0 ) + m I – m III (10.11)

Dividindo a expressão por Δt, para obter as características por unidade de tempo e passando-se ao limite para Δt tendendo a zero, resulta: lim m sis (t 0 + Δt) – m sis (t 0 ) = dm sis Δt→ 0 Δt dt

<!-- p. 249 -->
C a p í t u l o 1 0 z Generalização das equações integrais para regime variado z 249 Esse termo representa a variação instantânea da massa do sistema, quando evolui ao d longo de sua trajetória. Nesse caso, usa-se o símbolo da derivada total para indicar que a dt variação é função da posição (x,y,z) ocupada ao longo da trajetória pelo método lagrangeano. Por outro lado:

lim m VC (t 0 + Δt) – m VC (t 0 ) = ∂m VC Δt→ 0 Δt ∂t ∂ Nesse caso, utiliza-se o símbolo de derivada parcial ∂t por se tratar de uma variação local, com o passar do tempo, na região observada pelo método euleriano.

Os outros dois termos lim m I e lim m III representam as tendências de fluxo de massa Δt→ 0 Δt Δt→ 0 Δt através da SC, respectivamente, saindo e entrando no VC. Lembre que a massa que passa por unidade de tempo é a vazão em massa QVm.

Logo, após as operações indicadas, a Equação 10.11 fica:

dm sis dt = ∂m VC ∂t +Qms – Qme onde os índices (s) e (e) representam saída e entrada, respectivamente.

Pelas equações 10.6 e 10.3, a Equação 10.12 também pode ser escrita:

(10.12) d ρ dV = ∂ ρ dV + ρvr × r ndA (10.13)

∫ ∫ ∫ Lembrar que o termo dt ρrv r Vsis × ndA ∂t VC terá seu sinal SC fixado pelo cos θ, onde θ é o ângulo forma- ∫ r r SC do entre v e n que, nas entradas, é maior que 90°, produzindo um fluxo de sinal negativo, e nas saídas é menor que 90°, resultando num fluxo de sinal positivo.

Pode-se lembrar agora que a massa do sistema é constante, por definição, e, portanto, a ∫ variação com o tempo d ρ dV, ao longo da trajetória, será nula. dt Vsis ∫ ∂ Por outro lado, ρ dV representa a variação da massa dentro do VC que, com o pas- ∂t VC sar do tempo, poderá não ser nula. Isto é, a taxa de variação da massa dentro do VC dependerá dos diferentes sistemas que o ocuparem com o passar do tempo.

Pelas observações anteriores, a equação geral da continuidade resulta em:

∫ ∫ ∂ ρ dV + ρvr × r ndA = 0 ∂t VC SC (10.14) r Lembrar que se o VC for deformável, isto é, se a SC estiver em movimento, o vetor v corresponderá à velocidade relativa observada de um sistema de referência fixo no VC. Caso o regime seja permanente, as propriedades do fluido não variarão em cada ponto do VC com o passar do tempo e, portanto:

Conseqüentemente, a Equação ∫ ∂ ρ dV ∂t VC 10.14 ficará:

=0 ∫ r ρv × r ndA = 0 SC ou, havendo diversas entradas e saídas do VC:

∑ Qm – ∑ Qm = 0 ou ∑ Qm = ∑ Qm s e e s

<!-- p. 250 -->
No caso em que o fluido seja incompressível, para o qual ρ = cte em todos os pontos, obtém-se: ∑Q = ∑Q e s Essas últimas equações correspondem aos resultados obtidos no Capítulo 3 e são casos particulares da Equação 10.14.

Uma caldeira tem um volume interno de 3,4 m3, sendo que inicialmente 2,8 m3 são ocupados por água líquida (ρ = 1.000 kg/m3) e o restante é ocupado por vapor (ρ = 65 kg/m3).

Determinar:

a) massa inicial total de líquido e vapor na caldeira; b) a vazão em massa de água que entra e a vazão em massa que sai; c) após 10 minutos, qual a massa total (líquido e vapor) contida na caldeira? Dados: D1 = 2,5 cm; D2 = 5 cm; v1 = 3 m/s; v2 = 20 m/s. (Quando nada for indicado, supõe-se que as velocidades sejam as médias nas seções e que seus vetores sejam perpendiculares a elas.) a) m t0 = VL0 ρ1 + Vv0 ρ2 Vv0 = Vt – VL0 = 3,4 – 2,8 = 0,6 m 3 ∫ b) m t0 Qm = 3,4 × 1.000 + 0,6 × = ρrv × r ndA 65 = 2.839 kg SC ∫ Qm1 = ρL vncos θ dA = ρL v1 cos 180o A1 = –ρL v1 πD21 4 A1 No caso do cálculo avulso da vazão, pode-se adotá-la em módulo, não esquecendo o sinal na hora da aplicação na equação da continuidade.

| | Qm1 = 1.000 × 3 × π× 0,0252 4 = 1,47 kg/s ∫ Qm2 = ρv vr × nr dA = ρvv2cos 0° A2 = ρvv2 πD22 4 Qm2 = 65 × 3× π × 0,052 4 = 2,55 kg/s

<!-- p. 251 -->
C a p í t u l o 1 0 z Generalização das equações integrais para regime variado z 251 c) ∂ ∂t ∫ ρ dV+ ∫ ρrv × nrdA = 0 VC SC ∫ ∫ | | ∂ ∂t ⎡ ⎤ ⎢ ρ dV+ ρ dV⎥ ⎣⎢ V L Vv ⎦⎥ – Qm1 + Qm2 = 0 ∂ ∂t (mL + mv ) = Qm1 – Qm2 ∂ ∂t mt = Qm1 – Qm2 Como a variação da massa é local, no volume de controle, somente com o passar do tempo a derivada parcial poderá ser confundida com a total e, portanto: dm t = (Qm1 – Qm2) dt ∫ ∫ ou: mf m0 dm t = t 0(Qm1 – Qm2 )dt onde: mf = massa final no volume de controle, e as vazões em massa nas seções de entrada e saída são constantes com o passar do tempo. Logo: m f – m t 0 = (Qm1 – Qm2)t m f = m t 0 + (Qm1 – Qm2)t m f = 2.839 + (1,47 – 2,55) × 10 × 60 = 2.191 kg Um fluido (ρ = 800 kg/m3; ν = 10–5m2/s) escoa lentamente pela tubulação de descarga de um reservatório, com o diagrama de velocidades v = vmáx ⎡ ⎢1 ⎣⎢ – ⎛ ⎝⎜ r 0,05 ⎞ ⎟⎠ 2 ⎤ ⎥ ⎦⎥ . É claro que ao esvaziar o reservatório o vmáx diminui com o passar do tempo; entretanto, admite-se que, a partir do nível inicial, em que h0 = 3 m, e durante 2 min, a velocidade seja aproximadamente constante, com vmáx = 0,2 m/s. Sendo a área da seção do tanque Atan = 0,5 m2, determinar a taxa de variação do nível do tanque ⎛⎝⎜ dh dt ⎠⎞⎟ e, pela hipótese adotada, determinar o novo nível após 2 min. Solução Num instante qualquer, o VC fixo estará na seguinte situação:

A massa no VC seria:

<!-- p. 252 -->
∫ ∫ ρl dV+ ρar dV Vl Var Entretanto, comoρar << ρl, o segundo termo pode ser desprezado em relação ao primeiro e pode-se abandonar o índice l, lembrando que os dados sempre serão referidos ao líquido. Logo: ∂ ∂t ∫ ρ dV + ∫ ρrv × r ndA = 0 V SC Como ρ = cte para todos os dV (líquido), o primeiro termo fica assim:

∂ρ ∂t ∫ dV V e como ρ = cte com o passar do tempo, em cada ponto, tem-se: ρ ∂V ∂t Note-se que o volume de líquido contido no VC varia em cada instante e é, portanto, função do tempo t, não podendo ser colocado para fora da derivada. Como V só é função de t, a derivada local ou parcial pode ser confundida com a total d, dt e como num instante qualquer V = Atanh: ∫∂ ∂t ρ dV = ρA tan dh dt V O segundo termo da equação resulta em:

∫ ρrv × r ndA = ρvmcos 0o A = ρvm πD2 4 = Qm SC Sendo que D = 0,1 m, observando a expressão da velocidade, em que R = 0,05 m e vm = vmáx 2 = 0,1 m/s, conforme foi visto no Capítulo 3.

Logo: Qm = 800 × 0,1× π × 0,12 4 = 0,628 kg/s Como: ρA tan dh dt = – Qm Então:

dh = – Qm = 0,628 = –1,57 × 10–3 m/s dt ρAtan 800 × 0,5 Portanto: ∫ ∫ h dh = t (–1,57 × 10–3 )dt h0 0 ou h – h 0 = –1,57 × 10–3 t h = h 0 – 1,57 × 10–3 t Após 2 min: h = 3 − 1,57 × 10−3 × 2 × 60 = 2,812 m.

## 10.4 Relacionamento geral entre as propriedades do sistema e as

equações integrais para volume de controle As propriedades de um sistema podem ser classificadas em extensivas e intensivas. Propriedades extensivas são as que dependem da quantidade de matéria que constitui o sistema. Exemplos: m, V, EVcin etc. Propriedades intensivas são as que independem da quantidade de matéria do sistema. As intensivas naturais são a pressão e a temperatura.

<!-- p. 253 -->
C a p í t u l o 1 0 z Generalização das equações integrais para regime variado z 253 Entretanto, qualquer propriedade extensiva por unidade de massa torna-se intensiva. Essas propriedades denominam-se específicas. Supondo as propriedades homogêneas, o teste para verificar se a propriedade é extensiva ou intensiva pode ser realizado da seguinte forma: Divide-se o sistema em partes. Se em cada parte a propriedade se reduzir proporcionalmente à massa, então será extensiva; se independer da variação da massa, será intensiva (Figura 10.10). Figura 10.10 A propriedade específica de uma certa propriedade extensiva será representada pelo mesmo símbolo, mas com letra minúscula. O que se nota da Figura 10.10 é que, por exemplo, a energia é uma propriedade extensiva, mas a energia específica (e), isto é, a energia por unidade de massa, passa a ser uma propriedade intensiva. Note-se que a operação realizada na Figura 10.10c pode ser realizada indefinidamente, até se chegar a uma massa infinitesimal. Isso faz com que as propriedades intensivas possam ser atribuídas a um ponto de sistema (Figura 10.11). Figura 10.11 Logo:

dE = edm = ρedV ⇒ E = ∫ ρedV Sis Pelo exposto, pode-se concluir que qualquer propriedade específica de uma extensiva sempre pode ser associada à massa infinitesimal do fluido e a extensiva correspondente pode ser obtida pela operação de integração indicada.

<!-- p. 254 -->
Essa possibilidade permite criar um relacionamento entre qualquer propriedade extensiva do sistema e o VC, com base na Equação 10.13. Verifica-se que: A derivada em relação ao tempo de uma propriedade extensiva do sistema é igual à derivada dessa propriedade no volume de controle, mais o fluxo através da superfície de controle. (Lembrar que o fluxo pode ser positivo ou negativo, dependendo de se tratar de uma saída ou de uma entrada do VC.) Seja N uma propriedade extensiva qualquer do sistema e n a específica correspondente, isto é: n = dN ⇒ dN = ndm = nρ dV dm Então:

∫ dN sis = ∂N VC + r nρv × r ndA dt ∂t SC (10.15) ou: ∫ ∫ ∫ d nρ dV = ∂ nρ dV + nρrv × r ndA dt Sis ∂t VC SC (10.16) N Por exemplo, se N = m (massa do sistema), n = = 1, logo:

m ∫ ∫ ∫ d ρ dV = ∂ ρ dV + ρrv × r ndA dt Sis ∂t VC SC que coincide com a Equação 10.13.

r r Se, por exemplo, N = m v (quantidade de movimento do sistema), então n = v; logo: ∫ ∫ ∫ d r ρv dV = ∂ r rr r ρv dV + ρvv × ndA dt Sis ∂t VC SC Considerar que se ∫ ρ × r ndA representa o fluxo da massa através da superfície de contro- ∫ le, então r nρv × r ndA SC representará o fluxo da propriedade N, da qual n é a específica. Assim, ∫ SC rr r no exemplo acima, a parcela ρvv × ndA é o fluxo da quantidade de movimento.

SC

## 10.5 Equação da energia geral para volume de controle

A forma mais simples de introduzir essa equação é recorrer à primeira lei da Termodinâmica para o processo de um sistema. Lembrando que o sistema tem massa fixa e definida, a variação da sua energia só pode ser provocada por troca de calor e/ou trabalho com o meio, já que essas energias são as únicas que podem ser trocadas sem haver troca de massa. Em relação aos textos de Termodinâmica, modifica-se a convenção do sinal do trabalho. Neles, normalmente, o trabalho é considerado positivo quando é realizado do sistema contra o meio. Neste estudo, para manter a coerência com o Capítulo 4, no qual se adotou o trabalho da bomba positivo e o da turbina negativo, será mantida essa convenção, que é exatamente a contrária àquela. Dessa forma, para um intervalo de tempo infinitesimal: δQ + δW = dE onde: δQ = calor trocado entre o sistema e o meio, positivo quando fornecido ao sistema e negativo quando retirado (o símbolo d é utilizado em lugar de d, para lembrar que o calor e o

<!-- p. 255 -->
C a p í t u l o 1 0 z Generalização das equações integrais para regime variado z 255 trabalho não são propriedades de estado do sistema, pois dependem do processo através do qual são trocados); δW = trabalho trocado entre o meio e o sistema, com a mesma convenção do calor (lembre o leitor que o calor Q está sendo representado pelo símbolo em itálico para não confundi-lo com a vazão em volume Q). Logo, por unidade de tempo:

δQ δW dE += dt dt dt onde E é uma propriedade extensiva do sistema e, portanto:

onde:

E = ∫ ρedV Sis v2 e = u + + gz e as parcelas são, respectivamente:

2 u = energia interna específica do sistema v2 = energia cinética específica do sistema 2 gz = energia potencial específica do sistema ∫ Logo: δQ δW + = d ρ ⎛ ⎜ u + v 2 ⎞ + gz⎟ dv v2 e, nesse caso, n = u + + gz e, pela Equação 10.16, dt dt dt Sis ⎝ 2 ⎠ 2 tem-se: ∫ ∫ δQ dt δW + dt = ∂ ∂t ρ ⎛ ⎜ u + v 2 VC ⎝ 2 ⎞ + gz⎟ ⎠ dV + ρ ⎛ ⎜ u + v 2 SC ⎝ 2 ⎞ + gz⎟ ⎠ r v × r ndA O termo δQ é o fluxo de calor trocado entre o sistema e o meio. dt δW O termo é a potência trocada entre o fluido e o meio e compreende: dt a) a potência que o fluido troca com a máquina, a qual no Capítulo 4 foi indicada por N; b) a potência da força de pressão nas entradas e saídas do volume de controle. Adotando-se comorsempre a normal para fora, a força de pressão num elemento de área da SC será: –pndA. A potência será a força de pressão projetada na direção do movimento, multiplicada pela velocidade, ou:

r –pdAn × r v = r –pv × r ndA Dividindo e multiplicando esse termo por ρ, οβτ⎡μ−σε:

– p ρvr × r ndA ρ ∫ Sobre toda a SC: – ρ p r v × r ndA SC ρ c) a potência dissipada pelas tensões de cisalhamento na SC, a qual será indicada por –Nτ, por ser sempre subtraída da energia útil do sistema. Dessa forma, a equação fica: ∫ ∫ ∫ δQ dt + N − Nτ − ρ p r v × r ndA = SC ρ ∂ ∂t ρ VC ⎛ ⎝⎜ u + v2 2 + gz ⎞ ⎟⎠ dV + ρ ⎛ ⎜ u + v 2 SC ⎝ 2 ⎞ + gz⎟⎠ r v × r ndA

<!-- p. 256 -->
ou, juntando o termo da pressão do primeiro membro, com o semelhante do segundo membro: ∫ ∫ δQ dt +N–Nτ δ = δt ρ VC ⎛ v2 ⎜u + ⎝2 ⎞ + gz⎟⎠ dV + ρ SC ⎛ p v2 ⎜ ⎝ u + ρ + 2 ⎞ + gz⎟ ⎠ r v × r ndA (10.17) Para a solução de problemas em que os efeitos térmicos não sejam importantes, como já foi feito no Capítulo 4, os termos do fluxo de calor, variação de energia interna e potência das tensões de cisalhamento, serão englobados na potência dissipada, que, em relação ao fluido, será sempre subtraída dos efeitos mecânicos logo: ∫ ∫ δQ dt +N τ – ∂ ∂t ρudV VC – ρuvr × r ndA SC = –N diss Com essa modificação, a Equação 10.17 ficará:

∫ ∫ N – N diss = ∂ρ ∂t VC ⎛ v2 ⎜ ⎝2 ⎞ + gz⎠⎟ dV + ρ SC ⎛ v2 ⎜ ⎝2 + p ρ + ⎞ gz ⎟ ⎠ r v × r ndA (10.18) Se o regime for permanente, o termo da variação no VC será nulo:

∫ ∂ ∂t ρ VC ⎛ v2 ⎜ ⎝2 ⎞ + gz⎟ ⎠ dV = 0 O termo referente ao fluxo pode ser multiplicado e dividido por g, resultando em: ∫ ∫ ρ SC ⎛ v2 ⎜ ⎝2 + p ρ + ⎞ gz ⎟ ⎠ r v × r ndA = ρg SC ⎛ v2 ⎜ ⎝ 2g + p ρg + ⎞ z⎟ ⎠ r v× r ndA = ∫= γ SC ⎛ v2 ⎜ ⎝ 2g p⎞ + γ + z⎠⎟ r v × r ndA Adotando a velocidade média na seção e lembrando que p/γ + z = cte numa seção de escoamento: ∫γ SC ⎛ v2 ⎜ ⎝ 2g p⎞ + γ + z⎟ ⎠ r v × r ndA = ±γ ⎛ ⎜α ⎝ v2 2g p⎞ + γ + z⎟ ⎠ Q onde α = coeficiente da energia cinética, como foi definido no item 4.7 do Capítulo 4. O sinal da expressão depende de se tratar de uma entrada (< 0) ou uma saída (> 0). Logo, havendo diversas entradas e saídas, para regime permanente a Equação 10.18 ficará: ∑ ∑ N – N diss = γQH – γQH s e ou ∑ ∑ γQH + N = γQH + N diss e s que é a Equação 4.30 do item 4.8 do Capítulo 4, que para tubo de corrente (uma entrada e uma saída) reduz-se a:

HV1 + HVm = HV2 + HVp1,2 Conclui-se que a Equação 10.18 é a equação geral que dá origem a todas as equações do Capítulo 4.

<!-- p. 257 -->
C a p í t u l o 1 0 z Generalização das equações integrais para regime variado z 257 Supondo fluido ideal, determinar a expressão do nível do fluido num tanque em função do tempo quando ele é descarregado por um orifício. Solução ∫ ∫ N – N diss = ∂ ∂t ρ VC ⎜⎛ ⎝ v2 2 + gz ⎞⎟ ⎠ dV + ρ SC ⎛⎜ ⎝ v2 2 + p ρ + gz ⎞⎟ ⎠ r v × r ndA Não havendo máquina e sendo o fluido ideal:

∫ ∫ ∂ ρ ⎛ ⎜ v2 + gz ⎞⎟ dV + ρ ⎜⎛ v2 + p + gz ⎞⎟ r v × r ndA = 0 ∂t VC ⎝2 ⎠ SC ⎝ 2 ρ ⎠ Admitindo ρarρliq, ao se adotar uma SC fixa, pode-se desprezar a massa de ar, comparativamente com a do líquido. Sendo o líquido homogêneo e a seção do tanque constante e relativamente grande, a velocidade v nos elementos de volume internos ao VC pode ser adotada em média como sendo v1, isto é, a velocidade de descida do nível. Isso só não é verdade num pequeno volume próximo ao orifício, junto à saída. A cota z média do fluido no VC será em qualquer instante zm = h 2 . Logo: ∫ ∫ ∂ ∂t ρ VC ⎛ ⎜ ⎝ v21 2 + g h 2 ⎞ ⎟ ⎠ dV + SC ρ ⎛ ⎜ ⎝ v22 2 + p2 ρ + z 2 ⎞ ⎟ ⎠ v2dA = 0 Note-se que p2 = 0, z2 = 0 e, por se tratar de um jato livre, pode-se admitir que a velocidade seja uniforme na seção. Como na parcela referente ao VC adotaram-se valores médios no volume, as variações se devem somente ao tempo e pode-se confundir a derivada parcial com a total. Logo: d dt ⎢⎡ρ ⎣ ⎜⎛ ⎝ v21 2 + g h 2 ⎟⎞ ⎠ ⎤ Atanh ⎥ ⎦ = –ρ v23 2 Ao Em cada instante, pela equação da continuidade:

v1A tan = v2Ao ⇒ v2 = v1 A tan Ao Além disso, a velocidade v1 é exatamente a velocidade de descida do nível:

v1 = – dh dt Logo: ρA tan d dt ⎡⎛ ⎢⎣⎢⎜⎜⎝ 1 2 ⎜⎛⎝ dh dt ⎟⎠⎞ 2 + g 2 ⎞ h ⎠⎟⎟ ⎤ h⎥ ⎥⎦ = –ρ Ao 2 v31 ⎜⎛ ⎝ A tan Ao ⎞⎟ ⎠ 3

<!-- p. 258 -->
d dt ⎡ ⎢h ⎢⎣ ⎜⎛⎝ dh dt ⎟⎠⎞ 2 + gh 2 ⎤ ⎥ ⎦⎥ = ⎜⎛⎝ dh dt ⎞⎟⎠ 3 ⎜⎛ ⎝ A tan Ao ⎟⎞ ⎠ 2 dh dt ⎛⎝⎜ dh dt ⎞⎟⎠ 2 + 2h d 2h dt 2 + 2gh dh dt = ⎜⎛⎝ dh dt ⎞⎠⎟ 3 ⎛ ⎜ ⎝ 2 A tan ⎞ ⎟ Ao ⎠ d 2h dt 2 é a aceleração das partículas, que pode ser considerada pequena; logo: ⎝⎜⎛ dh dt ⎟⎠⎞ 2 + 2gh = ⎜⎛⎝ dh dt ⎠⎟⎞ 2 ⎜⎛ ⎝ A tan Ao ⎟⎞ ⎠ 2 dh = – dt 2gh 2 ⎛⎜ Atan ⎟⎞ – 1 ⎝ Ao ⎠ O sinal negativo corresponde ao esvaziamento.

∫ ∫ h dh = – t ho h 0 2g dt 2 ⎛ ⎜ A tan ⎞ ⎟ –1 ⎝ Ao ⎠ 2( h – ho)= – 2g t 2 ⎛⎜ Atan ⎞⎟ – 1 ⎝ Ao ⎠ h= ho – 2g t ⎜⎛ Atan ⎞⎟ 2 – 1 2 ⎝ Ao ⎠ h= h– 2 2g t ⎜⎛ Atan ⎟⎞ 2 – 1 2 ⎝ Ao ⎠ Note-se que: v1 = – dh dt = 2gh 2 ⎜⎛ Atan ⎞⎟ – 1 e v2 = 2gh Atan 2 ⎛⎜ Atan ⎞⎟ – 1 Ao ⎝ Ao ⎠ ⎝ Ao ⎠ Se a área do tanque for muito grande, h → h o em qualquer instante e v2 = 2gh 0 , como se verifica no Exemplo 4.1 do Capítulo 4.

## 10.6 Equação da quantidade de movimento para volume de controle

### 10.6.1 Equação para volume de controle fixo ou móvel com velocidade constante

Para um sistema, a força resultante é:

rr r r dv d (mv) F = ma = m = dt dt

<!-- p. 259 -->
C a p í t u l o 1 0 z Generalização das equações integrais para regime variado z 259 r onde mr v é a quantidade de movimento do sistema e é uma propriedade extensiva do tipo N = mv . r Nesse caso, a específica n = v, e a Equação 10.16 resulta em:

∫ ∫ ∫ r d F= ρrv dV = ∂ ρvr dV + ρvr vr × r ndA dt Sis ∂t VC SC r r Em cada instante, a força resultante F, que age no sistema, coincide com a força F que age no VC, já que em cada instante o VC coincide com o sistema nele contido. Logo, a equação da quantidade de movimento para VC será:

∫ ∫ r ∂ F= ρvr dV + ρvr vr × r ndA ∂t VC SC r (10.19) r A força F resultante que age no VC compõe-se de forças de contato ou de superfície ( FC ), causadas pela ação do meio na SC, e forças de campo ou a distância, provocadas por um campo que aje no sistema crontido no VC. Em geral, o campo considerado será o da gravidade e essa força será o peso (G) do sistema, contido no VC em cada instante. Logo:

∫ ∫ r F rr = G +Fc = ∂ ∂t ρvr VC dV + ρvr vr × r ndA SC (10.20)

Nos problemas, é muito importante selecionar a SC de forma a facilitar a solução, fazendo aparecer na Equação 10.20 forças de contato de fácil determinação e visualização. Por exemplo, no Capítulo 5, o VC foi escolhido como sendo um tubo de corrente, de forma que a força de contato resultou (Figura 10.12) em: Figura 10.12 r Fc r = –p1 A 1 n 1 – r p2 A2 n2 r + FS' ∫ ∫ r onde: FS' = r –p Lat dA Lat n Lat + r τdA Lat no Capítulo 5 foi adotado como sendo a resultante das SC SC pressões e tensões de cisalhamento na superfície lateral do fluido (tubo de corrente). Dessa forma, a Equação 10.20 resulta em:

∫ ∫ r G r – p1 A1 n1 r – p2 A2 n2 r + FS' = ∂ ∂t ρrv VC dV + ρvr vr × r ndA SC rr Supondo v1 e v2 uniformes ou adotando a velocidade média nas seções, obtém-se:

<!-- p. 260 -->
∫ r G r – p1 A1 n1 r – p2 A2 n2 r + FS' = ∂ ∂t ρvr VC dV r r + v2 Qm2 – v1Qm1 Recorde que ∫ ρrv × r ndA é a vazão em massa e que r v × r n > 0 na saída e r v × r n < 0 na entrada. SC Lembrar também que, no caso em que haja diversas entradas e saídas, as parcelas das vazões serão apresentadas como somatóriars. No Capítulo 5 admitiu-se que FS' fosse a resultante do contato de uma superfície sólida com a superfície lateral do fluido, e nesse caso:

∫ r FS' = ∂ ∂t ρvr VC dV r + p1 A1 n1 r + p2 A2 n2 r + v 2 Q m2 r – v1Q m1 r –G Querendo, então, determinar a força resultante do fluido com a parede sólida comr a qural está em contato entre (1) e (2), é necessário lembrar que pelo princípio da ação e reação FS = –FS' e, portanto: ∫ r FS = – ∂ ∂t ρvr VC r dV – p1 A1 n 1 – r p2 A2 n2 r + v1Q m1 r – v 2 Q m2 r +G (10.21)

No caso em que o regime seja permanente:

Logo: ∫ ∂ r ρv dV = ∂t VC 0 e Q m1 = Q m2 = Qm r r r rr r FS = –[p1 A1 n 1 + p 2 A 2 n 2 + Q m ( v 2 – v1 )] + G que é exatamente a equação deduzida e utilizada no Capítulo 5.

Isso significa que a Equação 10.21 é a geral, dentro das considerações admitidas no Capítulo 5, agora válida também para regime variado.

Não esquecer que, se o VC estiver em movimento com velocidade constante, as velocidades que deverão ser utilizadas são as relativas e, portanto, a Equação 10.21 será: ∫ r FS = – ∂ ∂t r r ρv r dV – p1 A 1 n 1 VC r – p2 A2 n2 r + v1r Q m ap1 – r v 2r Q m ap2 r +G (10.22)

Na Equação 10.22, Qmap é a vazão em massa aparente, conforme foi visto no Capítulo 5, isto é, a vazão calculada com a velocidade relativa. Não esqueça o leitor que, dependendo do problema, pode ser interessante que a SC não envolva somente o fluido e corte alguma superfícire sólida. Nesses casos, é interessante aplicar a Equação 10.21 geral e fazer a análise da força Fs de contato, observando em cada ponto a ação do meio na SC.

Seja um jato que atinge um desviador em regime permanente. Adota-se uma SC que corta o suporte de fixação do desviador. Determinar a força (Fd) que age na seção do suporte, cortada pela SC.

<!-- p. 261 -->
C a p í t u l o 1 0 z Generalização das equações integrais para regime variado z 261 Solução Isolando o VC r Gr = peso de todo o material contido no VC G r l = peso do líquido de (1) a (2) G r d = peso do desviador contido no VC Gar = peso do ar contido no VC (desprezível)

rr r r G = Gl + Gd + Gar r Fc = força de contato com o meio (lembrar que a pressão atmosférica compensa-se em todos os pontos, menos no trecho onde a SC corta o suporte do desviador). Logo:

rr r Fc = Fd – patmA dn Lat Pela Equação 10.22, rr G + Fc = ∂ ∂t ∫ ρvr dV + ∫ ρvrvr × r ndA com a hipótese de regime permanente: VC SC r rr rr r Gl + Gd + Fd – patmAdn Lat = v2Qm – v1Qm r rr r r r ou Fd = Qm( v2 – v1 ) – Gl – Gd + patmAdn Lat

<!-- p. 262 -->
Projetando segundo x: Fdx = Qm( v2cos θ – v1 ) Projetando segundo z: Fdz = Qm( v2sen θ – v1 )+ Gl + Gd + patmAd Seja agora um novo VC, adotando como SC o tubo de corrente constituído pelo jato em contato com o desviador, para determinar a força que o jato aplica nele. Isola-se o VC, como é mostrado na figura. Nesse caso, a única força de campo é o peso do líquido do jato entre (1) e (2). As forças de contato constituem-se das normais em cada ponto, resultantes da distribuição das pressões, e dars tangenciais, resultantes das tensões de cisalharmento, que podem ser divididas nas aplicadas pelo ar (τar) e nas aplicadas pela superfície do desviador (τd). Nesse caso, descontando a pressão atmosférica em cada ponto, pode-se trabalhar com a escala efetiva e, portanto, p1 = p2 = par = 0 e pLat = pLat (ef).

Logo, as forças de contato serão:

r r ∫ Força de atrito do ar: Fatar = τ ardAar A ar ∫ ∫ Resultante da superfície sólida em contato com o fluido: Fr'S = r τ ddAd + r –pLat ef n Lat dA d Ad Logo: ∫ ∫ r Fat ar + r FS' + r Gl = ∂ ∂t ρvr dA + ρvr vr × r ndA VC SC Sendo o regime permanente:

r Fat ar + r FS' + r Gl = r v2Qm – r v1Qm ou Fr 'S r = Qm( v2 – r v1 )– r Fat ar – r Gl Nesse caso, a força que age no desviador: r FS = –Fr 'S ou r rr r r FS = Qm( v1 – v2 )+ Fat ar + Gl Projetando na direção de x, obtém-se: FSx = Qm( v1 – cos θ)+ Fatar Projetando na direção de z, tem-se: FSz = –Qmv2 sen θ + Fatarz – Gl Note que, ao desprezar o atrito do ar e o peso do líquido, chega-se exatamente aos resultados obtidos no Capítulo 5.

<!-- p. 263 -->
C a p í t u l o 1 0 z Generalização das equações integrais para regime variado z 263

### 10.6.2 Equação para volume de controle acelerado

Seja um sistema que pertença a um sistema de referência (x,y,z) acelerado em relação a um sistema de referência inercial (X,Y,Z) (Figura 10.13). Figura 10.13 rr r Sabe-se que F = ma, onde a é a aceleração absoluta. Da Física, sabe-se que a aceleração absoluta é dada por:

r a r = a rel r +a0 rr + 2ω ∧ v rel + ωr& ∧ r r + ωr ∧(ωr ∧ r r ) r ar rel = aceleração do sistema em relação a Oxyz a 0r= arceleração de arrastamento (do sistema de referência Oxyz)

ωrr&2ω∧ ∧r v rr= rel = aceleração complementar arceleração tangencial ou de Coriolis ω ∧(ω ∧ r ) = aceleração centrípeta Obviamente, as acelerações que contêm ωr só existem se o sistema tem movimento de rotação.

Pela expressão da aceleração desenvolvida, tem-se:

r F =m r (a rel r +ao rr + 2ω ∧ v rel + ωr& ∧ r r + ωr ∧ (ωr ∧ r r ))

ou, em relação ao sistema de referência móvel:

r F – r m [ao rr + 2ω ∧ v rel + ωr& ∧ r r + ωr ∧ (ωr ∧ r r )] = r ma rel r r ∫ Como r a rel = dv rel dt , então r ma rel = dmv rel dt = d dt r ρv rel V Sis dV Como em cada instante o VC coincide com o sistema, então:

∫ ∫ ∫ r r F – ρ [a o VC rr + 2ω ∧ v rel + ωr& ∧ r r + ωr ∧(ωr ∧ r r )] ρdV = ∂ ∂t r rr ρv rel dV + ρv rel v rel VC SC × r ndA Dispara-se um foguete, partindo do repouso, ao longo de uma trajetória retilínea, a partir de uma estação espacial. O foguete queima β kg/s de combustível e tem inicialmente uma massa m0. Após o disparo, a massa varia segundo a lei: m = mV0 – βt. A velocidade de descarga dos gases em relação ao foguete é vs constante, assim como a pressão ps e a massa específica ρs. Qual é a velocidade absoluta do foguete vf em relação à Terra, considerada inercial?

<!-- p. 264 -->
Solução Como não há rotação, todos os termos que contêm r ω são nulos. r Sendo o foguete drisparado de uma estação espacial, pode-se desprezar a resistência do ar ( Rar ) e o efeito da gravidade (peso G).

Logo, não há forças de campo, e das forças de contato sobra só a de pressão na saída. rrr r r ∫ F = G + Rar + –ps n s dAs = –ps As n s As ∫ Das parcelas da aceleração sobra somente ρra odV = r ma o VC Logo: ∫ ∫ r –ps As n s – r ma o = ∂ ∂t ρrvr dV+ ρrvrrvr × nrdA VC SC ∂ ∂t ∫ ρrvr dV ≅ 0 ⇒ Esse termo refere-se ao movimento do VC em relação ao sistema de referência Oxyz fixo no foguete. A parte sólida não tem movimento relativo e a parte fluida tem velocidade relativa razoável somente no bocal de saída, e essa massa é muito pequena em cada instante.

Logo: r –ps As n s – r ma o = –ρs vs A s r vs , e projetando todos os vetores na direção do eixo do foguete: + ps As – ma o = –ρs v2s As m = mV0 βt, logo: pVsAVs – (mV0 – βt) aV0 = –ρVs vs2V AVs Como: ao = dvf dt ⇒ (m o – βt) dvf dt = ρs v2s As + ps A s ∫ ∫ vf 0 dvf = t 0(ρs v 2s A s + ps A s ) dt m0 – βt vf = (ρ S v 2 S A S + psA S ) 1 −β ln (m 0 – βt) t 0 vf = ρs v2s As + β ps A s ln m0 m 0 – βt Como β = ρs vs As , então: vf = ⎝⎛⎜ vs + ps A s β ⎟⎠⎞ ln m0 m 0 – βt

<!-- p. 265 -->
C a p í t u l o 1 0 z Generalização das equações integrais para regime variado z 265

## 10.7 Equação do momento da quantidade de movimento para volume de controle

Da Mecânica sabe-se que: A derivada em relação ao tempo do momento da quantidade de movimento de um sistema, em relação a um ponto, é igual, em cada instante, ao momento da resultante das forças externas que agem no sistema, em relação ao mesmo ponto. A Figura 10.14 mostra o esquema para a determinação do momento da força externa resultante que age no sistema em relação a um ponto qualquer. Figura 10.14 r Notar que a força resultante F compõe-se das forças de contato e do peso, já que não se consideram outros campos senão o da gravidade.

⎯⎯→ OP =Arr,pqauretirlodcaolipzroanotopoOn,toesdcoelahpidliocapçaãroadoa cálculro força F.

do momento, traça-se o vetor posição Ormromento M O em relação ao ponto O será um vetor cuja direção é perpendicular ao plano ( rF ), cujo sentido pode ser determinado pela regra da mão direita e definido por: r rr MO = r∧F (10.23)

cujo módulo é:

M O = rF sen θ rr onde θ = ângulo formado pelas direções positivas dos vetores r e F.

(10.24)

PelarFigura 10.14 observa-se que r sen θ = r0, que é a distância do ponto O à linha de ação da força F, comumente denominado braço da força F em relação ao ponto O.

r A Figura 10.15 mostra a determinação do momento da quantidade de movimento (dΓ)

de um elemento de massa do sistema em relação ao ponto O.

r dΓ = r (r ∧ r v)dm Figura 10.15

<!-- p. 266 -->
Para o sistema todo, o momento da quantidade de movimento será:

r Γ = ∫ ( r r ∧ r v)dm Sis e pode-se observar que é uma propriedade extensiva, passível da aplicação do teorema que permite a transformação para o estudo com VC.

Pelo teorema do momento da quantidade de movimento apresentado no início deste item, pode-se escrever:

∫ r MO = d dt rr ρ ( r ∧ v)

Vsis dV e portanto: ∫ ∫ r MO = ∂ ∂t ρ VC (rr ∧ rv) dV + ρ ( r r ∧ r v) ( r v × r n )dA SC (10.25)

Essa expressão, válida para um VC inercial, como já foi discutido na equação da quantidade de movimento, pode ser utilizada para um VC em movimento sem aceleração, usando a velocidade relativa. Também pode ser usada para um VC acelerado, desde que se acrescentem os termos dos momentos das acelerações, isto é:

∫ ∫ r MO – ρrr r [a o rr + 2ω ∧ v rel + ωr& ∧ r r + ωr ∧(ωr ∧ r r )] dV = ∂ ∂t rr ρ ( r ∧ v rel )

VC dV + ∫ rr r r + ρ ( r ∧ vrel ) ( vrel ∧ n )dA (10.26) SC Na grande maioria dos problemas, interessa a determinação do momento da força em relação a um eixo. Com essa finalidade, o vetor momento deverá ser projetado na direção do eixo selecionado. Seja um sistema de coordenadas cilíndricas ( r, θ, z ) orientado pelos vetores r e r , r e θ , r e z. Para simplificar, o estudo será realizado para um VC fixo.

Passa-se o eixo z pelo ponto O, adotado como origem, e faz-sre o eixo z coincidir com o eixo em relação ao qual se deseja determinar o momento da força F (Figura 10.16). rr Pela Figura 10.16 pode-se observar que dM z = dM O × e z .

∫ ∫ Logo: MZ = r MO × r e Z = ∂ ∂t ρ ( r r ∧ r v) VC dV × r e z + ρ ( r r ∧ r v)( r v × r ndA ) SC × r ez Figura 10.16

<!-- p. 267 -->
C a p í t u l o 1 0 z Generalização das equações integrais para regime variado z 267 Figura 10.17 rr Pela Figura 10.17 verifica-se que os vetores r e v envolvidos em coordenadas cilíndricas são dados por:

r r r er r ∧ v = r0 rr r r r = r r0 e r + r ze z r r v= r v r e r + vθe θ + vz e z eθ ez r r r 0 z = – vθ ze r +( vr z − r0 vz ) e θ + r0 vθ e z vr vθ vz Logo, lembrando que o produto escalar de vetores perpendiculares é nulo: rr r ( r ∧ v) × e z = r0 vθ Assim: ∫ ∫ M z = ∂ ∂t ρr0 vθ dV VC + rr ρr0 vθ( v × ndA )

(10.27) (10.28)

No caso de um sistema de referência acelerado, não esquecer as acelerações da Equação 10.26 e que a velocidade deverá ser a relativa. O irrigador da figura é alimentado com uma vazão de 4 L/s de água (ρ = 1.000 kg/m3). As seções de saída têm uma área de 20 cm2. Determinar o momento em relação ao eixo z: a) com o irrigador em repouso; b) com o irrigador girando com uma rotação de 10 rpm constante. Solução

<!-- p. 268 -->
a) Supondo regime permanente ∫ Mz = ρvθ r r0v × r ndA SC Mz = 2ρvθ r0 Q 2 = ρvθ r0Q = ρv cos 60o r0Q Mz = ρcos 60o r0Q2 2A = 1.000 × 0,5 × 0,3 × ( 4 × 10–3 )2 2 × 20 × 10–4 = 0,6 N. m Esse é o momento segundo z da força resultante que age no fluido. No irrigador, pelo princípio da ação e reação, o momento será: Mz' = –Mz = –0,6 N. m b) Fixando o VC no fluido, ele girará com velocidade angular ω em relação ao eixo z. A equação aplicável, agora, é a 10.26, com cada aceleração projetada segundo z.

∫ Mz – ρrr ∧ r [a 0 + r 2ω ∧ r vrel + ωr& ∧ r r + r ω ∧ r (ω ∧ r r )] dV × r ez = VC ∫ ∫ = ∂ ∂t ρr0vθ rel dV+ ρr0vθ rel r v rel × nrdA VC SC O regime é permanente e, portanto, o termo referente a ∂ será nulo, e como o VC não tem translação nem ace∂t leração angular, então:

r a0 = 0 e ωr& ∧ r r =0 Como r ω tem a direção de z er rr é radial, r ω ∧ r (ω ∧ r r )produz um vetor perpendicular a plano r (ω, r r ) e, portanto, não tem componente segundo ez , e a equação reduz-se a:

∫ ∫ Mz – ρrr ∧ r (2ω ∧ r vrel ) dV × r ez = ρr0vθ rel r vrel × r ndA VC SC No trecho radial da tubulação:

∫ ∫ ρrr ∧ r (2ω ∧ r vrel ) dV × r e z = r0 0 ρrre r ∧ (2ωre z ∧ vrel r e r ) Adr × r e z = VC ∫ ∫ = r0 0 ρrre r ∧ (2ωvrel r e θ ) Adr × r e z = r0 ρΑ 0 (2rωvrel ) r e z dr × r ez = ∫= r0 0 ρΑ (2rωv rel ) dr = 2ρAωvrel r02 2 = ρAωvrel r02 Nos borrifadores:

∫ ∫ ρrr ∧ r (2ω ∧ r vrel ) dV × r ez = ρrrer ∧ (2ωrez ∧ vrel r e θ ) Ard θ × r ez = VC VC ∫= ρrer r ∧ (–2ωvrel r e r )× r ez =0 VC A integral de fluxo através da SC será:

∫ ρr0vθ rel r v rel × r ndA = 2ρr0vθ rel Q 2 = ρr0vrelQ cos θ Logo:

Mz = ρr0vrelQ cos θ – ρAvrel r02 Mz = ρr0vrelQ cos θ – ρωr02Q = ρr0Q(vrelcos θ – ωr0 )

A velocidade relativa vrel é a velocidade vista pelo observador fixo no VC que gira com o irrigador, que do ponto de vista do observador é como se estivesse parado; logo:

<!-- p. 269 -->
C a p í t u l o 1 0 z Generalização das equações integrais para regime variado z 269 vrel =Q 2A = 4 × 10–3 2 × 20 × 10–4 = 1 m/s Logo: Mz = 1.000 × 0,3 × 4× 10–3 ⎛⎝⎜1× cos 60o – 2π × 30 × 60 0,3⎟⎠⎞ = 0,22 N. m e Mz' = –0,22 N. m Outra solução pode ser obtida adotando-se um VC fixo. Nesse caso:

∫ ∫ Mz = ∂ ∂t ρr0vθ dV+ ρvθ r v × r ndA VC SC A parcela da variação com o tempo no VC é nula. No termo do fluxo será necessário determinar a velocidade absoluta. r vrel = Q 2A r n ⇒ vθ rel = Q 2A cos θ r varr = ωr0er θ ⇒ vθ arr = –ωr0 vθ abs = Q 2A cos θ – ωr0 Mz = 2ρr0 Q 2 ⎝⎜⎛ Q 2A cos θ – ωr0 ⎠⎞⎟ = ρr0Q ⎜⎛⎝ Q 2A cos θ – ωr0 ⎟⎠⎞ Mz = 1.000 × 0,3 × 4 × 10–3 ⎜⎛ ⎝ 2 4× × 20 10–3 × 10–4 cos 60o – 2π× 10 × 60 0,3⎟⎞ ⎠ = 0,22 N. m Mz' = –0,22 N. m Aplicação ao rotor de uma bomba centrífuga Hipóteses:

• regime permanente; • fluido incompressível; • infinitas pás de espessura nula, para garantir que as partículas percorram exatamente o perfil das pás; • sem atrito.

<!-- p. 270 -->
Seja z um eixo perpendicular ao plano do desenho, passando por O.

∫ ∫ M z = ∂ ∂t rr ρr0 vθ dV + ρr0 vθ v × ndA VC SC Pela hipótese de regime permanente e fluido incompressível:

Mz = ρr2 vu Q 2 – ρr1 v u Q 1 = ρQ (v u 2 r2 – v u 1 r1 )

Não havendo perdas por atrito, a potência transmitida ao fluido é igual à potência no eixo do rotor, que é calculada por:

N = Mzω N = ρQ (v u 2 r2 – v u 1 r1 ) ω = ρQ (v u 2 u 2 – v u 1 u 1 )

Representando por Ht∞ a carga ou altura manométrica da bomba para infinitas pás de espessura nula e sem atrito, isto é, para as hipóteses dadas, então a potência transmitida ao fluido será: N = γQH t∞ = ρQ (v u 2 u 2 – v u 1 u 1 )

gH t∞ = v u 2 u 2 – v u 1 u 1 Essa última é a equação fundamental para o estudo das máquinas hidráulicas de fluxo. Para esse estudo o leitor deverá recorrer aos livros especializados no assunto. Todos os exercícios dos capítulos 3, 4 e 5 podem ser resolvidos com as equações gerais apresentadas neste capítulo, adotando as hipóteses convenientes para a sua simplificação. Lembrar que a hipótese básica estabelecida neles foi a de regime permanente, como consta nos títulos. Nesse ponto, em que o leitor já deverá estar familiarizado com a Mecânica dos Fluidos, será um aprendizado interessante partir de uma equação mais geral e analisar as hipóteses do problema para utilizá-la na solução. Neste conjunto de exercícios serão incluídos apenas os que podem ser resolvidos somente pela aplicação das equações gerais apresentadas neste capítulo. 10.1 Um reservatório contém um gás e tem uma válvula que controla a sua saída de forma que a pressão interna seja reduzida segundo a lei: p = p0 (1 – αt2)

Sabe-se que durante a descarga a temperatura do gás do reservatório mantém-se constante (processo isotérmico: p/ρ = cte) e que no instante t = 10 s a passagem de abertura da válvula tem uma área de 0,5 m2. Determinar para o instante t = 10 s: a) a vazão em massa do gás; b) a vazão em volume;

<!-- p. 271 -->
C a p í t u l o 1 0 z Generalização das equações integrais para regime variado z 271 c) a velocidade média na seção de saída; d) a massa do gás que resta no reservatório; e) o tempo de esvaziamento do reservatório; f) a massa do gás no reservatório após o esvaziamento; g) traçar a curva de esvaziamento do reservatório m = m(t) e verificar que a área debaixo da curva representa a massa que sai até o instante considerado.

Resp.: a) 5 kg/s; b) 2 m3/s; c) 4 m/s; d) 25 kg; e) 13,4 s; f) 5,11 kg 10.2 Água escoa de um tanque por um tubo lateral, conforme a figura. A velocidade do escoamento na seção do tubo de descarga é dada por: v = ⎡ vmáx ⎢1 – ⎢⎣ ⎛⎜⎝ r R ⎠⎞⎟ 2⎤ ⎥ ⎥⎦ Determinar: a) a taxa de variação com o tempo, no instante t0, da massa de água contida no tanque, sendo nesse instante vmáx = vmáx0 ; b) a velocidade de descida do nível da água no tanque no instante inicial. Resp.: a) –ρvmáx0 πR 2 2 ; b) vmáx0 = πR2 2A tan 10.3 A figura mostra uma seringa para injeções, com as respectivas dimensões. Se a velocidade do êmbolo é 0,25 cm/s e a velocidade do líquido na agulha é 25 cm/s, qual a porcentagem de líquido desperdiçada através da folga entre o êmbolo e o cilindro? (Desprezar o volume contido na agulha.) ve = 0,25 cm/s Dc = 0,62 cm Da = 0,61 mm va = 25 cm/s De = 0,61 cm L = 1,15 cm Resp.: 3,25% 10.4 A massa de gás no interior de um botijão varia segundo a lei: m (t) = m0 – βt, onde β = cte. Sendo ρs a massa específica do gás na seção de saída, calcular a velocidade média nessa seção, cuja área é As.

<!-- p. 272 -->
Resp.: vs =β ρs A s 10.5 Após a seção de entrada (1) de um conduto de seção quadrada de 0,3 m × 0,3 m, existem duas paredes porosas. A vazão de água na entrada é 300 L/s. Pela parede porosa superior (2) há uma vazão de entrada que varia parabolicamente, por unidade de largura, desde 0 L/s.m na seção (1) até 80 L/s.m, junto à seção (4). Na outra face porosa (3), a água sai com uma vazão que varia linearmente, por unidade de largura, desde 150 L/s.m, junto à seção (1), até 0 L/s.m, junto à seção (4). Determinar a vazão na seção (4) de saída do conduto, localizada a 50 cm da entrada (1). Resp.: Q4 = 292,8 L/s 10.6 O amortecedor hidráulico do sistema de aterrissagem de um avião suporta o peso G quando é acionado. No instante do pouso na pista, a pressão do ar é pV0, e seu volume é z0A, onde A é a área da seção transversal do cilindro. Verificar, aplicando a equação da energia para regime variado, que a velocidade do pistão é dada pela equação diferencial: dv2 dz = 2g h ⎛ ⎜⎝ – p0z 0 γz – h + G γA ⎞⎠⎟. Admitir: a) ar a temperatura constante; b) atrito desprezível.

10.7 No tubo em U da figura, de seção de área A, oscila, em torno da posição de equilíbrio, uma coluna de comprimento total L de um líquido admitido ideal. Determinar o período T da oscilação.

<!-- p. 273 -->
C a p í t u l o 1 0 z Generalização das equações integrais para regime variado z 273 Resp.: T = 2 π L 2g 10.8 Um veículo de massa m0 = 900 kg move-se com uma velocidade de 30 m/s em relação a um inercial, sob a ação de uma força constante de 4.500 N. No instante t = 0 surge um vazamento no tanque de combustível, de forma que este é perdido verticalmente com uma vazão de 4,5 kg/s. O veículo continua a se mover sob a ação da força inicial constante. Qual será a velocidade do veículo após 20 s do início do vazamento? Resp.: v = 39,5 m/s 10.9 Na instalação, a vazão de 100 L/s divide-se igualmente nos dois ramais. Qual é o momento em relação ao eixo z devido somente à ação da água? Dados: A2 = A3 = 2 × 10–3 m2; p1 = 100 Pa; γ = 104 N/m3. Resp.: 1.250 N.m 10.10 Água escoa horizontalmente para fora de um tubo, através de uma fenda de 3 mm de largura e 1,8 m de comprimento. A vazão é 28 L/s e a velocidade varia linearmente desde vmáx até zero no fim da fenda. Determinar o momento em relação ao eixo vertical, provocado pelo escoamento do fluido (ρH2O = 1.000 kg / m3 ).

<!-- p. 274 -->
Resp.: Mz = 114 N.m 10.11 Uma bomba centrífuga tem pás com ângulo de entrada de 15o e de saída de 25o. A rotação é 1.720 rpm e os diâmetros de entrada e saída são, respectivamente, de 10 cm e 25 cm. Sendo vu1 = 0 e vr1 = vr2, determinar: a) os diagramas de velocidades; b) a altura manométrica teórica para infinitas pás. Resp.: a) u1 = 9 m/s; w1 = 9,33 m/s; u2 = 22,51 m/s; vu2 = 17,34 m; w2 = 5,70 m/s; v2 = 17,51 m/s; b) Ht∞ = 39,8 m 10.12 Deseja-se uma bomba que, acoplada a um motor de 3.450 rpm, produza uma altura manométrica teórica de 80 m. O ângulo de entrada das pás deve ser de 15o e o de saída, de 30o. Sendo d1 = 10 cm, quanto deve ser d2, supondo vr1 = vr2 e vu1 = 0? Resp.: d2 = 180 mm

<!-- p. 275 -->

# Capítulo 11 — Análise diferencial

C a p í t u l o 1 1 z Análise diferencial z 275

## 11.1 Introdução

Nos capítulos anteriores, o estudo foi dedicado à análise integral e empírica. Na análise integral, procurou-se estabelecer expressões algébricas que representassem o comportamento e as propriedades de um conjunto de partículas de fluido agrupadas no sistema que, num dado instante, ocupa a região de interesse denominada volume de controle. A análise empírica permitiu relacionar as grandezas que influem num dado fenômeno através da análise dimensional, estabelecendo, a partir de modelos teóricos, os critérios para a determinação de coeficientes experimentais que corrijam esses modelos para que possam representar os resultados reais. O objetivo deste capítulo é o de estabelecer o equacionamento para o estudo do comportamento de partículas individuais do fluido, se bem que ainda com uma certa característica de conjunto. Isso significa que mesmo o escoamento turbulento, em que existe certa aleatoriedade no movimento, será estudado por um comportamento médio das partículas, sem levar em conta as suas flutuações. A esta altura, é interessante definir o conceito de partícula fluida, já que essa entidade foi citada em diversas ocasiões, sem a sua definição formal. Seja um sistema para o qual se deseja definir a massa específica num ponto P (Figura 11.1). Figura 11.1 Adota-se um volume ΔV, que contém uma massa Δm, no entorno do ponto P. A massa específica média será definida por: ρm Δm = ΔV

<!-- p. 276 -->
Para se obter a massa específica no ponto, passa-se ao limite para ΔV tendendo a zero em volta do ponto P. Entretanto, quando o volume chega a um certo valor ΔV0, nota-se que, devido à agitação molecular, a massa contida no volume adquire valores que variam de um instante para outro, havendo uma descontinuidade na função.

Partícula fluida é a de volume ΔV0 para o qual o gráfico da Figura 11.1 não sofre descontinuidade. Isto é: ρP = lim Δm ΔV→ ΔV0 ΔV Se o fluido não é um gás rarefeito, admite-se que: lim Δm ≅ lim Δm = dm ΔV→ ΔV0 ΔV ΔV→ 0 ΔV dV Nesse caso, os fluidos são confundidos com um contínuo, permitindo o estudo por análise diferencial.

## 11.2 Cinemática da partícula

### 11.2.1 Sistemas de coordenadas 11.2.1.1 Coordenadas cartesianas

Deslocamento (Figura 11.2)

Figura 11.2 Velocidade Logo:

r dP d (P – O) dx r dy r dz r r r r v= = dt dt = dt e x + dt e y + dt e z = vx e x + vy e y + vz e z dx vx = dt dy vy = dt dz vz = dt

<!-- p. 277 -->
C a p í t u l o 1 1 z Análise diferencial z 277 Aceleração r a d2P = dt 2 r = dv = dvx dt dt r ex + dvy dt r e y + dv z dt r ez d2xr d2yr = dt 2 e x + dt 2 e y d2z r + dt 2 e z = rrr axex +ayey +azez Logo: ax = dvx dt d2x = dt 2 ay = dvy dt d2y = dt 2 az = dvz dt d2z = dt 2 11.2.1.2 Coordenadas cilíndricas Deslocamento (Figura 11.3)

Velocidade r dP dr r dθ r dz r r r r v = dt = dt e r + r dt e θ + dt e z = vr e r + vθ e θ + vz e z Logo: dr vr = dt dθ vθ = r dt dz vz = dt Aceleração r r dv Sendo a = , pode-se verificar que:

dt ar = dvr dt – v 2 θ r aθ = dv θ dt + vr vθ r az = dvz dt d2z = dt 2 Figura 11.3

<!-- p. 278 -->
## 11.3 Geometria do movimento

No Capítulo 3 definiram-se trajetórias e linhas de corrente como uma forma de visualizar o movimento, mas nesse capítulo não houve a preocupação com a determinação daquelas linhas, a não ser intuitiva ou experimentalmente. Neste item podem-se complementar aqueles conhecimentos obtendo-se suas equações matemáticas. Trajetória É o lugar geométrico dos pontos ocupados por uma partícula, com o passar do tempo. A partícula selecionada é individualizada por suas coordenadas iniciais (a; b; c). A trajetória pode ser obtida pela integração das equações paramétricas do movimento que, em coordenadas cartesianas, são: dx = vx dt dy = vy dt dz = vz dt Eliminando o tempo entre essas equações, obtêm-se as equações em coordenadas cartesianas que representam a linha geométrica percorrida pela partícula. Dado o campo de velocidades de um fluido em movimento, vx = x 1+ t ; vy = 1; vz = 0; determinar a expressão da trajetória e traçar a trajetória da partícula que no instante inicial t0 = 0 está no ponto (2; 2; 0). Solução vx = dx dt = x 1+ t → dx x = dt 1+ t Integrando: lnx = ln (1+ t) + lnC1 ⇒ x = C1 (1+ t )

vy = dy dt = 1→ dy = dt Integrando: y = t + C2 vz = dz dt = 0→ dz = 0 Integrando: z = C3 Se para t = 0 a partícula ocupa as coordenadas iniciais (a; b; c), então: Se x = C1 (1 + t), para t = 0 → C1 = a → x = a (1 + t) Se y = t + C2, para t = 0 → C2 = b → y = t + b Se z = C3, para t = 0 → C3 = c → z = c Eliminando o tempo entre as duas primeiras equações:

t = y – b → x = a (1 + y – b) ou x – ay = a – ab Essa equação representa retas em planos paralelos ao Oxy, cada um com a cota z = c. A partícula, com as coordenadas iniciais indicadas no enunciado, seguirá a trajetória dada por x – 2y = –2, no plano Oxy, já que z = 0. A partícula e sua trajetória são mostradas na figura.

<!-- p. 279 -->
C a p í t u l o 1 1 z Análise diferencial z 279 Linhas de corrente Como foi visto no Capítulo 3, linha de corrente é a linha tangente aos vetores da velocidade nos seus pontos de aplicação, num certo instante. Essa característica é representada pela expressão: r dP ∧ v = 0 Tal equação em coordenadas cartesianas é dada por:

r r r dP r = dx r e x + dy r e y + dz r ez v = vxex +vyey +vzez rrr dP ∧ r v = ex dx ey dy ez dz = (vz dy – vy dz)

r ex +( v x dz – v z dx) r e y +( v y dx – v x dy) r e z vx vy vz Logo:

vz dy – vy dz = 0 → dy = vy dz vz vx dz – vz dx = 0 → dx vx = dz vz vy dx – vx dy = 0 → dx vx = dy vy Determinar as linhas de corrente para o campo de velocidades do exemplo anterior: vx = x 1+ t ; vy = 1; vz = 0.

Solução Lembrar que t = cte = t, já que as linhas de corrente são traçadas para um certo instante. dx = dy → dx = dy → (1+ t ) dx = dy vx vy x1 x 1+ t y Integrando: (1+ t) lnx = y + C → x = Ke 1 + t Como o regime é variado, pois é função de t, a configuração das linhas de corrente do escoamento varia de instante para instante. Por exemplo, no instante inicial, quando t = 0: x = Key

<!-- p. 280 -->
e, para cada K, pode ser traçada uma linha de corrente, de modo que, qualitativamente, o escoamento terá o aspecto da figura a seguir.

## 11.4 Variação das grandezas de um ponto a outro do fluido

No espaço ocupado por um fluido, em cada ponto localizado por um sistema de coordenadas, as grandezas assumem diferentes valores e poderão variar com o passar do tempo se o regime não for permanente. O objetivo deste item é estabelecer uma expressão matemática que, a partir de um ponto onde as grandezas sejam conhecidas, permita determiná-las nos outros pontos do campo. Com essa finalidade, pode-se efetuar o estudo da variação das grandezas de duas maneiras diferentes, mas equivalentes. Uma das formas é pelo método de Lagrange, já descrito na forma integral para sistemas. Por esse método, dada uma partícula de fluido, pode-se acompanhá-la ao longo de sua trajetória no espaço, verificando o valor das grandezas a ela associadas em cada ponto. Nesse caso, é importante notar que existem duas causas para a variação das grandezas da partícula. A primeira se deve ao fato de que ela mesma evolui de um ponto a outro do campo, onde as grandezas têm diferentes valores, e a segunda é que, para chegar ao novo ponto, a partícula leva um certo tempo, durante o qual as propriedades, em cada ponto, poderão variar se o regime não for permanente. Para se ter um conhecimento detalhado da variação das grandezas associadas à partícula, é necessário que estabelecer a variação para deslocamentos infinitesimais, pois, adotando um deslocamento finito, seriam desconhecidos os acontecimentos nos pontos intermediários entre os pontos de partida e de chegada. A Figura 11.4 mostra a descrição pelo método de Lagrange. Pela figura, observa-se que a escolha da partícula cuja evolução se deseja estudar, é definida pela sua posição no instante considerado inicial. Acompanha-se, então, a partícula ao longo de sua trajetória, que será percorrida até o ponto P, num certo intervalo de tempo, durante o qual as grandezas do próprio campo poderão ter variado. Figura 11.4

<!-- p. 281 -->
C a p í t u l o 1 1 z Análise diferencial z 281 Nesse caso, a variação da grandeza G, associada à partícula, de um ponto a outro da trajetória, será: ΔG = G (P2 , t 2 ) – G (P1 , t1 )

sendo P1 e P2 os pontos ocupados pela partícula, respectivamente, nos instantes t1 e t2. Dividindo pelo intervalo de tempo Δt = t2 – t1 e passando ao limite para Δt tendendo a zero, será obtida a variação da propriedade de um ponto a outro, infinitamente próximos, e, portanto, a variação de forma contínua ao longo da trajetória.

lim G (P2 , t 2 ) – G (P1 , t1 ) = dG Δt→ 0 Δt dt (11.1)

A derivada assim obtida será denominada ‘derivada total’, já que expressa a variação de G com o passar do tempo, de um ponto a outro, isto é, a variação de G ocorrerá seja com o tempo, seja com as coordenadas do ponto do campo. O outro método de estudo da variação das grandezas associadas às partículas do fluido é o método de Euler, também já visto anteriormente no estudo de sistemas. Por esse método, o observador não acompanha a partícula ao longo da sua trajetória, mas se preocupa com o valor das grandezas nos pontos do campo, não se importando se a partícula está ou não ocupando o ponto observado. Dessa forma, o método permite a determinação de dois tipos de variações: a) Observa-se a variação da grandeza G de um ponto a outro no mesmo instante (obviamente os dois pontos serão ocupados por partículas diferentes) (Figura 11.5). Nesse caso, a variação da grandeza G será devida à posição de duas partículas distintas no espaço e será: G (P2 , t1 ) – (P1 , t1 ) Figura 11.5 Dividindo pela distância Δs e passando ao limite para Δs tendendo a zero, obtém-se: lim G (P2 , t1 ) – G (P1 , t1 ) = ∂G Δt→ 0 Δs ∂s (11.2)

Essa derivada denomina-se convectiva e é parcial, pois, mesmo que G seja função do tempo, este será considerado fixo, considerando-se apenas a variação de um ponto a outro no mesmo instante. b) Observa-se a variação da grandeza G num ponto com o passar do tempo. Nesse caso, o observador fixa um ponto do espaço e verifica a variação da grandeza com o passar do tempo. É óbvio que, se o fluido estiver em movimento, em cada instante uma partícula diferente ocupará aquele ponto. Nesse caso, a variação da grandeza G será: G (P1 , t 2 ) – G (P1 , t1 ) ou, dividindo por Δt e passando ao limite para Δt tendendo a zero:

<!-- p. 282 -->
lim G (P1 , t 2 ) – G (P1 , t1 ) = ∂G Δt→ 0 Δt ∂t (11.3)

Também se trata de uma derivada parcial, pois, mesmo que G varie de um ponto a outro do campo, sendo a variação no mesmo ponto, com o passar do tempo, as coordenadas do ponto serão consideradas fixas quando se efetuar a derivada. Uma partícula A passa pelo ponto O (0; 0; 0) no instante t = 0, com uma temperatura T = 1°C, e passa pelo ponto P1 (5; 0; 0), com T = 4°C no instante t1 = 1 s. Uma outra partícula B passa pelo ponto O (0; 0; 0) no instante t1 = 1 s, com T = 2°C. Usando aproximação por variações finitas, determinar: a) a derivada total; b) a derivada local; c) a derivada convectiva (medidas em cm); d) a velocidade na origem. e) Verificar que dG = ∂G + v ∂G.

dt ∂t ∂s Solução Instante t1 = 0 O(0;0;0) P1(5;0;0) x Instante t2 = 1s O(0;0;0)

a) dT = TA( P1 , t2 ) – TA(O, t1 ) = 4 – 1 = 3o C/s dt t2 – t1 1 b) ∂T = TB(O, t2 ) – TA(O, t1 ) = 2 – 1 = 1o C/s ∂t t2 – t1 1 c) ∂T = TA( P1 , t2 ) – TB(O, t2 ) = 4 – 2 = 0,4o C/cm ∂s Δs 5 d) v = Δs = 5 = 5 cm/s Δt 1 e) ∂T + v ∂T = 1+ 5 × 0,4 = 3o C/s = dT ∂t ∂s dt P1(5;0;0) x Não será efetuada a demonstração, mas pode-se verificar a validade da seguinte equação, ilustrada pelo exemplo anterior: dG = ∂G + r (v × ∇) G dt ∂t (11.4)

O símbolo ∇ (nabla) é um operador, apresentado a seguir em coordenadas cartesianas e cilíndricas.

<!-- p. 283 -->
C a p í t u l o 1 1 z Análise diferencial z 283 Coordenadas cartesianas:

∇ r = ex ∂r ∂x + e y ∂r ∂y + e z ∂ ∂z (11.5)

Coordenadas cilíndricas:

r ∇ = er ∂r ∂r + e θ ∂r r∂θ + e z ∂ ∂z (11.6) Note-se que a grandeza G pode ser escalar ou vetorial e que r v × ∇ forma um novo operador. Coordenadas cartesianas:

r v × ∇ = vx ∂ ∂x + vy ∂ ∂y + vz ∂ ∂z (11.7)

Coordenadas cilíndricas:

r v×∇ = vr ∂ + vθ ∂r r ∂ ∂θ + vz ∂ ∂z (11.8)

Seja o escoamento de um fluido em que o campo de velocidades num plano xy é dado por: vx = xt2; vy = xyt. Determinar as componentes ax e ay do campo de acelerações: a) pela derivada total; b) pelo segundo membro da Equação 11.4.

Solução a) ax = dvx dt = t2 dx dt + x2t = t2vx + 2xt = xt 4 + 2xt ay = dvy dt = yt dx dt + xt dy dt + xt = ytvx + xtvy + xy = xyt 3 + x2yt 2 + xy b) Na Equação 11.4 deve-se fazer G = vx e G = vy.

ax = dvx dt = ∂vx ∂t + r (v × ∇ )vx ax = dvx dt = ∂vx ∂t + ⎛⎜⎝ vx ∂ ∂x + vy ∂ ∂y ⎞⎟⎠ vx ax = dvx dt = ∂vx ∂t + vx ∂vx ∂x + vy ∂vx ∂y ax = dvx dt = 2xt + xt 2t 2 + xyt (0) = xt 4 + 2xt Analogamente:

ay = dvy dt = ∂vy ∂t + vx ∂vy ∂x + vy ∂vy ∂y ay = dvy dt = xy + xt 2yt + xytxt = xyt 3 + x2yt 2 + xy Note-se que as duas formas são equivalentes.

<!-- p. 284 -->
## 11.5 Análise dos movimentos de uma partícula fluida

Para efeito de simplificação, a análise será feita no plano, sendo que no espaço seria suficiente acrescentar os termos referentes a mais uma coordenada. As coordenadas adotadas são cartesianas e para melhor visualização será adotada uma partícula fluida com um formato geométrico regular (Figura 11.6). Figura 11.6 ∂v x ∂x = taxa de variação de vx na direção de x.

∂v y ∂y = taxa de variação de vy na direção de y.

∂v x ∂y = taxa de variação de vx na direção de y.

∂v y ∂x = taxa de variação de vy na direção de x.

O efeito das velocidades e das suas respectivas variações pode ser analisado de forma independente. a) Translação b) Deformação linear Figura 11.7 Figura 11.8

<!-- p. 285 -->
c) Deformação angular C a p í t u l o 1 1 z Análise diferencial z 285 Figura 11.9 O ângulo de deformação total será:

dα – dβ = ⎛ ⎜ ∂v y + ∂vx ⎞ ⎟ dt ⎝ ∂x ∂y ⎠ d) Rotação Se dα e δβ tiverem o mesmo sinal e o mesmo valor, a partícula sofrerá apenas uma rotação. Figura 11.10 Se os ângulos forem diferentes, o ângulo médio de rotação será:

dα + dβ = 1 ⎛ ⎜ ∂v y – ∂v x ⎞ ⎟ dt 2 2 ⎝ ∂x ∂y ⎠ e a velocidade ângular de rotação será:

Ω = 1 ⎛ ⎜ ∂v y – ∂v x ⎞ ⎟ 2 ⎝ ∂x ∂y ⎠ Superpondo todos esses efeitos em três dimensões, pode-se verificar que a velocidade de uma partícula é dada por três parcelas:

r v = r v0 + 1 2 ∇Φ + r Ω ∧ r r r Na Equação 11.9, v0 é a velocidade de translação.

(11.9) ∇Φ = grad Φ = ∂Φ ∂x r ex + ∂Φ ∂y r ey + ∂Φ ∂z r ez onde Φ é a ‘função deformação’ e, por exemplo:

<!-- p. 286 -->
∂Φ ∂x =2 ∂v x ∂x dx + ⎛ ⎜ ∂v x ⎝ ∂y + ∂v y ∂x ⎞ ⎟ ⎠ dy + ⎛ ⎝⎜ ∂v x ∂z + ∂v z ∂x ⎞ ⎟⎠ dz O termo ∂vx dx refere-se à deformação linear na direção de x, e os outros termos refe∂x rem-se às deforrmaçrões angulares.

r O termo Ω ∧ r representa a rotação da partícula, e Ω denomina-se ‘vetor turbilhão’. É dado por: r Ω = 1 ∇ ∧ r v = 1 rot r v 2 2 Lembrar que em coordenadas cartesianas:

rrr ex ey ex rot r v = ∂ r∂x ∂ r∂y ∂ r∂z = ⎛ ⎜ ∂v z ⎝ ∂y − ∂v y ∂z ⎞ ⎟ ⎠ r e x + ⎛ ⎝⎜ ∂v x ∂z − ∂vz ∂x ⎞r ⎟⎠ e y + ⎛ ⎜ ∂v y ⎝ ∂x − ∂v x ∂y ⎞ ⎟ ⎠ r e z vx vy vz O movimento dos fluidos é irrotacional se r Ω r = 0 ou rot v = 0. Nesse caso, as partículas do fluido não terão rotação em torno de um eixo próprio.

## 11.6 Dilatação volumétrica

Na expressão da função deformação Φ do item anterior, verificou-se que o termo ∂vx refere-se à deformação linear na direção de x. O significado de ∂vy e ∂vz ∂x será análogo, respectivamente, na direção de y e de z.

∂y ∂z Seja δ x a ‘dilatação linear’ na direção de x, definida conforme a Figura 11.11. Figura 11.11 Observa-se que: dx (1+ δ x )– dx = ∂v x ∂x dxdt Logo: δ x = ∂v x ∂x dt, e δx dt = ∂v x ∂x pode ser chamado de ‘velocidade de dilatação linear’.

Considerando a dilatação linear em todas as direções, pode-se obter a dilatação volumétrica (Figura 11.12).

<!-- p. 287 -->
C a p í t u l o 1 1 z Análise diferencial z 287 Figura 11.12 Seja: dV = dV0(1+Δ ), onde Δ = dilatação volumétrica, então: dx (1+ δ x ) dy (1+ δ y ) dz (1+ δ z ) = dxdydz (1+ Δ ) Desprezando os termos de maior ordem, obtém-se:

Δ =δx +δy +δz ou Δ = ∂vx + ∂vy + ∂vz = ∇ × r v = div r v dt ∂x ∂y ∂z r Conclui-se que div v pode ser interpretado como a velocidade de dilatação volumétrica.

## 11.7 Equação da continuidade na forma diferencial

Seja uma partícula de fluido de volume dV e massa ρdV. Essa partícula pode se deformar e se deslocar, mas a massa deverá se conservar com o passar do tempo (Figura 11.13). Figura 11.13 Logo:

ρdV = (ρ + dρ) dV (1+Δ)

ρ = ρ +ρΔ + dρ + dρΔ Desprezando o termo dρΔ, que é de segunda ordem, obtém-se dρ +ρΔ = 0, ou, dividindo por dt: dρ +ρ Δ = 0 dt dt Portanto: dρ r +ρ div v = 0 dt (11.10)

A Equação 11.10 é uma das formas interessantes da equação da continuidade na forma diferencial. Essa equação expressa a possibilidade de deformação de uma partícula com a conservação ou continuidade de sua massa. Logo, em qualquer problema deverá ser obedecida, sendo uma condição imprescindível à existência de um dado escoamento.

<!-- p. 288 -->
Das propriedades do operador ∇ pode-se verificar que:

div ρvr =ρ div r v+ r v × grad ρ Substituindo a Equação 11.11 na Equação 11.10, obtém-se:

dρ + div ρvr – r v × grad ρ = 0 dt mas, pela Equação 11.4: dρ dt = ∂ρ ∂t + r v × ∇ρ = ∂ρ ∂t + r v × grad ρ Logo: ∂ρ r ∂t + div ρv = 0 que é outra variante interessante da equação da continuidade.

Casos particulares a) Fluido incompressível → dρ = 0 dt Pela Equação 11.10 → div r v = 0 ∂ρ b) Regime permanente → ∂t = 0 Pela Equação 11.12 → div ρrv = 0 (11.11)

(11.12) (11.13) (11.14)

Um jato de fluido, simétrico em relação a um eixo, é dirigido contra um anteparo perpendicular ao eixo do jato, resultando no campo de velocidades: vx = m(t)x vy = m(t)y vz = –2m(t)z a) O regime é permanente? b) O fluido é incompressível? c) Determinar as linhas de corrente.

Solução a) Como o campo de velocidades é função de t, o regime é variado.

b) r div v = ∂vx + ∂vy + ∂vz = m(t) + m(t) – 2m(t) = 0 ∂x ∂y ∂z Logo, o fluido é incompressível. c) Linhas de corrente dx = dy → dx = dy vx vy m(t)x m(t)y Logo:

ln x = ln y + C ⇒ x = C1y que é a equação de um feixe de retas no plano xy, passando pela origem.

<!-- p. 289 -->
C a p í t u l o 1 1 z Análise diferencial z 289 Ainda: Logo:

dx = dz m(t)x –2m( t)z 2 lnx = – lnz + C' ou x2z = C2, que são hipérboles.

## 11.8 Equação fundamental do movimento de uma partícula de fluido

ideal (equação de Euler)

No Capítulo 1 definiu-se fluido ideal como sendo aquele cuja viscosidade é nula. A ausência da viscosidade e, portanto, das tensões de cisalhamento simplifica sobremaneira a segunda lei da dinâmica de Newton, já que as forças de contato irão se resumir ao efeito das pressões. r As forças de campo serão indicadars para um campo qualquer por fdm ou, particularmente, para o campo da gravidade por gdm.

r A força de pressão num ponto qualquer da superfície será dada por –pndA, lembrando que o versor da normal no ponto será sempre dirigido para fora.

Figura 11.14 Logo: ∫ r fdm – ∫ r pndA = ∫ r adm V A V Pode-se verificar que: ∫ r pndA = ∫ grad p dV e portanto: ∫ r ρfdV – ∫ grad p dV = ∫ ρardV A V V V V

<!-- p. 290 -->
ou, finalmente:

r r1 a = f – ρ grad p (11.15)

A Equação 11.15 em coordenadas cartesianas resulta em:

ax = ∂v x ∂t + vx ∂v x ∂x + vy ∂v x ∂y + vz ∂v x ∂z = fx −1 ρ ∂p ∂x ay = ∂v y ∂t + vx ∂v y ∂x + vy ∂v y ∂y + vz ∂v y ∂z = fy − 1 ρ ∂p ∂y az = ∂v z ∂t + vx ∂v z ∂x + vy ∂v z ∂y + vz ∂v z ∂z = fz −1 ρ ∂p ∂z (11.16) A Equação 11.15 em coordenadas cilíndricas resulta em:

ar = ∂vr ∂t + vr ∂v r ∂r + vθ r ∂v r ∂θ + vz ∂v r ∂z – v 2 θ r =fr 1 ∂p – ρ ∂r aθ = ∂vθ ∂t + vr ∂v θ ∂r + vθ r ∂v θ ∂θ + vz ∂v θ ∂θ + vr vθ r 1 ∂p = f θ – ρ r∂θ az = ∂vz ∂t + vr ∂v z ∂r + vθ r ∂v z ∂θ + vz ∂v z ∂z =fz 1 ∂p – ρ ∂z (11.17)

No caso geral, essas três equações podem apresentar cinco incógnitas:

a) o campo de velocidades, constituído por vx, vy e vz em coordenadas cartesianas, ou vr, vθ e vz em coordenadas cilíndricas; b) a distribuição das massas específicas; c) a distribuição das pressões.

Nesse caso, o sistema de equações apresentado terá necessidade do auxílio de mais duas equações.

Uma delas será a equação da continuidade:

dρ r +ρ div v = 0 dt e a outra deverá ser uma equação de estado que permita saber ρ = f(p, T)

A equação de estado introduz mais uma variável — a distribuição das temperaturas —, cuja solução exigirá a utilização de mais equações e condições que serão obtidas das disciplinas que tratam os efeitos térmicos. O que se pode notar é que, dependendo do problema, o número de equações é grande e de difícil solução. Em alguns casos, as hipóteses impostas para o problema permitem simplificações que tornam a solução mais confortável. A seguir, serão estudados alguns desses casos para que o leitor possa se familiarizar com o manuseio das equações.

### 11.8.1 Fluido incompressível em repouso, campo da gravidade

Nesse caso, mesmo que o fluido seja real, não existem tensões de cisalhamento e, portanto, não há manifestações do efeito da viscosidade.

<!-- p. 291 -->
C a p í t u l o 1 1 z Análise diferencial z 291 r r1 rr a = f – ρ grad p onde: f = g Sabe-se que o campor da gravidade deriva de um potencial escalar U, significando que existe U tal que grad U = g. Isto é:

∂U r ∂U r ∂U r r ∂x e x + ∂y e y + ∂z e z = –ge z ou ∂U ∂z = –g, logo U = –gz (U = 0 para z = 0)

Nesse caso, a equação de Euler resulta em:

r 1 a = grad U – ρ grad p (11.18) Como: ρ = cte, r ⎛ p⎞ a = grad ⎜U ⎝ – ρ ⎟ ⎠ Como por hipótese:

r a =0 ⇒ ⎛ p⎞ grad ⎜U ⎝ – ρ ⎟ ⎠ =0 Portanto: ∂⎛ ∂x ⎜U ⎝ − p ρ ⎞ ⎟ ⎠ r ex + ∂⎛ ∂y ⎜U ⎝ − p ρ ⎞ ⎟ ⎠ r ey + ∂ ∂z ⎛ ⎜U ⎝ − p ρ ⎞ ⎟ ⎠ r ez = 0 Logo: ∂ ∂x ⎛ ⎜U ⎝ − p⎞ ρ ⎟ ⎠ = 0 ⇒ U − p ρ = cte (x) ⇒ − gz − p ρ = c te (x) ou, como ρ = cte → p = cte(x). O mesmo acontece na direção de y, concluindo-se o que já se sabia pelo teorema de Stevin: que, num plano horizontal, num fluido em repouso, a pressão é constante em todos os pontos. Obtém-se, ainda:

–gz – p = cte (z) ρ ou p + γz = cte que nada mais é do que a expressão do teorema de Stevin.

### 11.8.2 Equilíbrio relativo para fluido incompressível

Embora esse assunto já tenha sido estudado no Capítulo 2, do ponto de vista da estática dos fluidos, será aqui reexaminado com a utilização da matemática pela equação de Euler. Entenda-se não como uma repetição, mas como uma forma diferente de análisar o mesmo problema e ao mesmo tempo uma maneira de se familiarizar com o manuseio da equação do capítulo atual. Lembre o leitor que, nesse caso, apesar de o fluido estar em movimento em relação a um inercial, estará em repouso em relação ao recipiente, no qual se fixará o sistema de referência. Estando o recipiente acelerado, do ponto de vista do sistema de referência fixo, a aceleração será vista como uma força de inércia, isto é:

<!-- p. 292 -->
rr1 f – a – ρ grad p = 0 Note-se que, ao passar a aceleração para o outro membro da equação, ela passa a integrar o membro das forças e, sendo a equação igual a zero, pode-se imaginar que, do ponto de vista relativo, o sistema esteja em equilíbrio.

Sendo: r f r =g ⇒ rr g–a– 1 grad p = 0 ρ ou, como já foi visto, utilizando a noção de potencial escalar:

r ⎛ p⎞ a = grad ⎜ –gz ⎝ – ρ ⎟ ⎠ Portanto: ax = ∂ ∂x ⎛ ⎜ –gz ⎝ – p⎞ ρ ⎟ ⎠ → –gz – p ρ = a xx +C ou e analogamente:

p γ +z = – ax g +C1 p γ +z = −ay g +C2 p γ +z = −az g +C3 Seja o tanque da figura, que contém água, submetido a uma aceleração r a no plano horizontal na direção x. Determinar a inclinação da superfície livre e a pressão nos pontos (A) e (B).

Solução Nesse caso, ay = 0 e az = 0.

Logo: p + γz = C2 (segundo y), e como z não varia na direção de y, conclui-se que nessa direção p = cte (y é a direção perpendicular à figura). Segundo z, vale p + γz = C3, o que mostra que na direção de z continua a valer o teorema de Stevin. Na direção de x:

p γ + z = – ax g x + C1 Na superfície livre, na escala efetiva, p = 0 e, portanto:

<!-- p. 293 -->
C a p í t u l o 1 1 z Análise diferencial z 293 z = – ax g x+ C1 que é a equação de uma reta de coeficiente angular – ax , isto é, tg θ = – ax .

g g Analisando diretamente a equação de Euler:

ρ( gr – ar ) = grad p Como grad p é um vetor normal às linhas isobáricas (p = cte), estas serão perpendiculares ao vetor r (g – ra), r que no Capítulo 2 foi denominado gef .

Pelo exposto, pA = γh A e pB = γh B.

Determinar a superfície livre de um líquido contido num recipiente cilíndrico em rotação com velocidade angular ω = cte.

Solução Nesse caso, é interessante utilizar coordenadas cilíndricas e r ω = ωer z . Logo: r g– r a= 1 grad p ou r a = grad ⎜⎛ – p – gz ⎟⎞ ρ ⎝ρ ⎠ onde r a = aceleração centrípeta = –ω2rre r Logo: ∂ r∂θ ⎜⎛ ⎝ – p ρ – gz ⎟⎞ ⎠ = 0 ⇒ p+ γz = C1(θ) ( segundo θ)

<!-- p. 294 -->
∂ ⎛ ⎜ – p – gz ⎞⎟ = 0 ∂z ⎝ ρ ⎠ ⇒ p + γz = C2( z ) ( segundo z ) ( teorema de Stevin )

∂ ⎜⎛ – p – gz⎞⎟ = –ω2r ∂r ⎝ ρ ⎠ ⇒ p + γz = ρω2r 2 2 + C3( r ) ( segundo r )

Na superfície livre, p = 0 na escala efetiva e adotando-se a origem no ponto em que o eixo z a intercepta, para r = 0, z = 0 e p = 0; portanto, C3(r) = 0.

Logo:

z = ρω2r 2 = ω2r 2 2 γ 2g Essa expressão no espaço é a equação de um parabolóide.

### 11.8.3 Escoamento em que a massa específica do fluido não depende da

temperatura (ρ = f (p))

Nesse caso, o fluido será denominado barotrópico.

Podem ser observados três casos notáveis: a) fluido incompressível (ρ = cte); b) escoamento isotérmico de gás perfeito ⎛ ⎜ ⎝ p ρ = c−te ⎞ ⎟ ⎠ ; c) escoamento adiabático de gás perfeito ⎛ ⎜ ⎝ p ρk ⎞ = c−te ⎟ . ⎠ Seja uma função F (p) tal que:

F (p) = ∫ dp ρ Nesse caso, dp dF (p) = ρ e portanto dF (p) dp = 1 ρ Logo: grad F (p) = ∂F (p) r ∂x e x + ∂F (p) ∂y r e y + ∂F (p) ∂z r e z = = dF (p) dp ∂p r ∂x e x + dF (p) dp ∂p r ∂y e y + dF (p) dp ∂p r ∂z e z = = dF (p) grad p = 1 grad p dp ρ r Na Equação 11.18, em que f deriva de um potencial escalar (caso do campo da gravidade): r 1 a = grad U – ρ grad p r dv = grad U – grad F (p) dt r dv = grad (U – F (p)) dt (11.19)

<!-- p. 295 -->
C a p í t u l o 1 1 z Análise diferencial z 295 mas verifica-se que:

r dv = ∂vr + r (v × ∇)rv = ∂vr + grad v2 + rot r v ∧ r v dt ∂t ∂t 2 Substituindo a Equação 11.20 na Equação 11.19, tem-se:

∂rv + grad v2 + rot r v ∧ r v = grad (U – F (p)) ∂t 2 ou ∂vr ∂t + grad ⎛ v2 ⎜ ⎝2 – U +F ⎞ (p)⎠⎟ + rot rv ∧ r v = 0 (11.20) (11.21)

Casos particulares da Equação 11.21 ⎛ ∂rv r⎞ 1) Regime permanente, escoamento irrotacional ⎝⎜ ∂t = 0; rot v = 0⎠⎟ ⎛ v2 ⎞ Nesse caso, grad ⎜ – U +F (p)⎟ = 0 ⎝2 ⎠ Logo: v2 – U + F (p) = cte para qualquer ponto. 2 ⎛ ∂rv ⎞ 2) Regime permanente, escoamento rotacional ⎝⎜ ∂t = 0⎠⎟ Logo: grad ⎛ v2 ⎜ ⎞ – U +F (p)⎟ rr + rot v × v = 0 ⎝2 ⎠ r Multiplicando escalarmente por v, obtém-se:

grad ⎛ v2 ⎜ ⎞r rrr – U +F (p)⎟ × v + rot v∧ v × v = 0 ⎝2 ⎠ r rr Das propriedades dasr operações vetoriais, sabe-se que rot v ∧ v × v = 0. r r Adotando um versor e s , tangente em cada ponto às linhas de corrente, isto é, v = ve s , obtém-se: grad ⎛ v2 ⎜ ⎝2 – U + F ⎞ (p)⎟⎠ × r ve s =0 ou grad ⎛ v2 ⎜ ⎝2 − U + F (p) ⎞ ⎟⎠ × r e s =0 Logo: v2 – U + F(p) = cte ao longo de uma linha de corrente. 2 Pelo que foi visto anteriormente:

U = -gz e F(p) = ∫ dp ρ Logo: v2 p + gz + = C 2 ρ No caso de fluido incompressível ∫ dp ρ = p ρ e resulta em:

<!-- p. 296 -->
v2 p v2 p 2 + gz + = C ou ρ +z+ 2g γ = C, que é a equação de Bernoulli, vista no Capítulo 4.

Por esse estudo, verifica-se que a equação de Bernoulli para uma partícula é válida para fluido ideal, incompressível, no campo da gravidade, em qualquer ponto, se o escoamento é irrotacional, ou ao longo de uma linha de corrente, se é rotacional. Uma aplicação interessante da equação de Euler refere-se ao uso de um sistemra dre corordenadas, denominado natural. Esse sistema é orientado pr or um terno ortonormal( e s , e n , e b ), adotado em cada pontro de uma linha de corrente, onde es é o versor tangente à linha de corrente em cada ponto,re n é o versor da normal com sentido positivo quando dirigido para o centro de currvaturra ere b é o versor da binormal, que forma com os outros dois um terno positivo, isto é, e b = e s ∧ e n (Figura 11.15). Figura 11.15 Nesse caso: ∇ r = es ∂r ∂s + e n ∂r ∂n + e b ∂ ∂b r v × ∇ =v ∂ ∂s r e ( r v × ∇ r )v = v ∂ ∂s ( r ve s ) = v ∂v ∂s r e s + v2 ∂e s ∂s rr Pode-se verificar que ∂e s ∂s = en R , onde R é o raio de curvatura da linha de corrente no ponto considerado.

Lembrando que:

r dv = r ∂v + r (v × ∇)rv = grad (U – F (p)) dt ∂t r ∂v ∂v r v2 r obtém-se:

∂t + v ∂s e s + R e n = grad (U – F (p))

ou, para regime permanente:

∂( v2/2) r ∂s e s v2 + R r en = ∂ r ∂s (U – F (p))e s ∂ r + ∂n (U – F (p))e n + ∂ ∂b (U – F r (p))e b Logo: ∫ v 2 –U + dp = cte (na direção de s)

2 ρ (11.22a)

∫ U – dp = cte (na direção de b) ρ (11.22b)

No campo da gravidade e fluido incompressível, a Equação 11.22.1 nada mais é do que a equação de Bernoulli, e a Equação 11.22b mostra que ao longo da binormal vale a distribuição hidrostática p/ γ + z = cte.

<!-- p. 297 -->
C a p í t u l o 1 1 z Análise diferencial r Na direção da normal e n obtém-se:

∫ ⎛ p ⎞ ⎛ p ⎞ 2 v2 ⎜ ⎝ ρ + gz ⎟ ⎠ – ⎜ ⎝ ρ + gz ⎟ ⎠ =– 1 dn R 2 1 Essa expressão permite examinar três casos.

1) Linhas de corrente paralelas (R → ∞ )

⎛p ⎞ ⎛p ⎞ ⎜ ⎝ ρ + gz ⎟ ⎠ = ⎜ ⎝ ρ + gz ⎟ ⎠ 2 1 z 297 (11.22.3)

2) Linhas de corrente curvas Conclui-se que a distribuição hidrostática, num fluido em movimento, somente é válida para linhas de corrente paralelas; quando isso não acontece, a pressão varia em função da curvatura. Isso, por exemplo, exige cuidados na confecção de tomadas de pressão, para que os manômetros indiquem a verdadeira pressão da seção (ver a figura a seguir). Outros fenômenos podem ser estudados a partir dos conceitos anteriores, e o leitor poderá tirar suas conclusões a partir das idéias desenvolvidas pelas equações apresentadas.

<!-- p. 298 -->
## 11.9 Escoamento bidimensional de fluido ideal, incompressível

No Capítulo 3 foi visto que, se o escoamento é bidimensional, ele se repete identicamente em planos paralelos ao do desenho (Figura 11.16). Figura 11.16 Apesar de as hipóteses desse escoamento parecerem discrepantes da realidade, a Figura 11.16 mostra alguns casos em que os resultados do modelo são relativamente compatíveis com os observados. De qualquer forma, o estudo de modelos pode servir para adquirir conhecimentos sobre o assunto, e as discrepâncias com a realidade podem ser estudadas e contornadas pela análise experimental. Seja uma equação diferencial do tipo:

P (x, y)dx +Q (x, y)dy = 0 (11.23)

onde P (x, y) e Q (x, y) têm derivadas parciais contínuas em qualquer ponto. O primeiro membro da Equação 11.23 diz-se diferencial exata se coincide com o diferencial dF (x,y) de alguma função F (x, y), isto é: ∂F ∂F P (x, y)dx +Q (x, y)dy = dx + dy = dF(x, y)

∂x ∂y Nesse caso, a solução da Equação 11.23 será: dF (x, y) = 0 → F (x, y) = cte Conclui-se que:

∂F (x, y) P(x, y) = ou ∂P (x, y) = ∂2 F ∂x ∂y ∂y∂x ∂F (x, y) Q (x, y) = ou ∂Q (x, y) = ∂2 F ∂y ∂x ∂x∂y Logo: ∂P (x, y) ∂y = ∂Q (x, y) ∂x (11.24)

A Equação 11.24 é a condição para que a expressão da Equação 11.23 seja uma diferencial exata. Pode-se verificar que a integração de uma diferencial exata independe do caminho.

<!-- p. 299 -->
C a p í t u l o 1 1 z Análise diferencial z 299 Seja a equação diferencial (2xy + 1)dx + (x2 + 4y)dy = 0.

Verificar se o primeiro membro é uma diferencial exata e integrá-la desde o ponto (0, 0) até o ponto (x, y). Solução Verificação Portanto:

P (x, y) = 2xy + 1⇒ ∂P = 2x ∂y Q (x, y) = x2 + 4y ⇒ ∂Q = 2x ∂x ∂P = ∂Q ∂y ∂x Seja a integração pelo caminho da figura:

Por outro caminho:

De outra forma:

dF (x, y) = ∂F dx + ∂F dy = P (x, y)dx + Q (x, y)dy ∂x ∂y ∫ P (x, y) = ∂F ⇒ F = x P (x, y) dx + f (y)

∂x 0 Como ∂F representa a variação de F (x, y) somente com x, a solução é uma constante em relação a x, que ∂x pode ser uma função de y (f (y)).

Logo:

F (x, y) = ∫ (2xy + 1)dx + f (y)

F (x, y) = 2x2y + x + f (y)

<!-- p. 300 -->
Derivando em relação a y, mantendo x constante:

∂F (x, y) = 2x2 + ∂f (y)

∂y ∂y Mas ∂F (x, y) = Q (x, y) = x2 + 4y ∂y Portanto:

2x2 + ∂f (y) = x2 + 4y ∂y ∂f (y) = −x2 + 4y ∂y Logo: ou, finalmente:

f (y) = –x2y + 4y2 + cte = –x2y + 2y2 + cte 2 F (x, y) = 2x2y + x – x2y + 2y + cte = x2y + x + 2y2 + cte F (x, y) = x2y + x + 2y2 = cte Pelo que foi visto anteriormente, a equação de uma linha de corrente num plano xy qualquer é dada por: dx dy = vx vy ou vx dy – vy dx = 0 r Sendo o fluido incompressível, pela Equação 11.13, div v = 0.

Logo:

∂vx + ∂vy = 0 ou ∂v x = – ∂v y ∂x ∂y ∂x ∂y (11.25) (11.26)

Comparando a Equação 11.25 com a Equação 11.23:

P (x, y) = –vy ou Q (x, y) = vx ∂P = − ∂vy ∂y ∂y ∂Q = − ∂vx ∂x ∂x e ∂P ∂y = ∂Q ∂y que é válido pela Equação 11.26. Logo, a Equação 11.25 é uma equação diferencial exata, o que significa que existe uma função Ψ tal que: dΨ = vx dy – vy dx = 0 (11.27)

A função Ψ é denominada função de corrente e é tal que, se dΨ = 0 ⇒ Ψ = cte, que pela Equação 11.27 é a equação de uma linha de corrente. Pelo exposto, num plano de um escoamento bidimensional, os pontos onde Ψ = cte pertencem a uma linha de corrente.

Observe-se o exemplo da Figura 11.17.

<!-- p. 301 -->
C a p í t u l o 1 1 z Análise diferencial z 301 Figura 11.17 O valor da constante denomina-se ‘cota da linha de corrente’. Sejam duas linhas de corrente quaisquer cujas cotas sejam Ψ1 e Ψ2 e seja uma profundidade unitária, perpendicular ao plano xy (Figura 11.18). Figura 11.18 Integrando dΨ = vx dy – vy dx de (1) a (2), ao longo da linha y = cte ou dx = 0, deve-se obter o mesmo resultado que se obteria ao longo de qualquer caminho, como foi explicado anteriormente. ∫ ∫ 2 2 dΨ 1 = v 1 x dy, já que dx = 0 ∫ ∫ Pela figura, observa-se que:

2dΨ = 2 dq, onde dq é a vazão através da área dA = dy1.

1 1 Logo:

Ψ2 – Ψ1 = q 1,2 (11.28)

A Equação 11.28 expressa que a diferença de cotas de duas linhas de corrente é igual à vazão que passa entre elas, por unidade de largura perpendicular ao plano do escoamento. Outras propriedades de Ψ: a)

dΨ = vx dy – vy dx dΨ = ∂Ψ dx + ∂Ψ dy ⇒ ∂x ∂y ∂Ψ ∂y = vx ∂Ψ ∂x = –vy (11.29) b) Logo: r rr rr rr r r r v = vx i + vy j = vx (j ∧ k) + vy (k ∧ i ) = – k ∧ (vx j – vy i ) = = – r k∧ ⎛ ⎝⎜ ∂Ψ ∂y r j + ∂Ψ ∂x r⎞ i ⎠⎟ = r –k ∧ grad Ψ | | |rv| = r –k ∧ grad Ψ

<!-- p. 302 -->
Cormo grad Ψ é perpendicular às linhas de corrente no plano xy, então o ângulo formado entre –k e grad Ψ é π/2. Logo: | | |rv| = r –k ∧ grad Ψ =|grad Ψ|sen π = ± | grad Ψ| 2 Como grad Ψ é a máxima variação de Y, o grad Ψ representa a variação de Y segundo a normal às linhas de corrente em cada ponto. Logo:

ou, na Figura 11.19:

|rv| = ± |grad Ψ| = ± dΨ dn dΨ = |vr| dn (11.30) Figura 11.19 | | Como dΨ = dq e rdq é constante pela equação da continuidade, então, se as linhas de corrente se aproximam, v aumenta ou vice-versa.

A idéia de função de corrente torna-se ainda mais interessante se o escoamento, além de o regime ser permanente e o fluido incompressível, também é irrotacional.

r Nesse caso: rot v = 0 ou ∂vy – ∂vx = 0 ∂x ∂y Existe um teorema que garante que, para que o campo de velocidades seja irrotacional, é condição necessária e suficiente que exista uma função φ, tal que:

r v = grad φ A função φ denomina-se ‘função potencial’ escalar das velocidades. Devido a isso, quando o escoamento é rotacional, é dito com potencial de velocidades.

Nesse caso:

r r r ∂φ r ∂φ r v = vx i + vy j = ∂x i + ∂y j e, portanto: ∂φ ∂φ vx = ∂x e vy = ∂y (11.31) Diante disso, como r v × grad Ψ =0 → grad φ × grad Ψ =0 e, portanto, as linhas φ = cte e Ψ = cte formam uma rede ortogonal, e as linhas φ = cte são denominadas equipotenciais (Figura 11.20).

<!-- p. 303 -->
C a p í t u l o 1 1 z Análise diferencial z 303 Figura 11.20 Propriedades conjuntas de φ ε Ψ a) No escoamento plano de fluido incompressível, em regime permanente, irrotacional, as linhas de corrente (equicorrentes) e as linhas equipotenciais formam uma rede ortogonal.

b) As funções φ ε Ψ obedecem à equação de Laplace, sendo, portanto, funções harmônicas. De fato: r v = grad φ → div r v = div grad φ = 0; logo: ∇ 2 φ = 0 Analogamente, verifica-se que ∇ 2 Ψ = 0 c) Pelas relações apresentadas anteriormente, obtém-se: Coordenadas cartesianas:

∂Ψ ∂φ vx = ∂y = ∂x ∂Ψ ∂φ vy = – ∂x = ∂y (11.32)

Coordenadas cilíndricas:

∂Ψ ∂φ vr = r∂θ = ∂r ∂Ψ ∂φ vθ = – ∂r = r∂θ (11.33)

Coordenadas naturais:

∂Ψ ∂φ vs = – ∂n = ∂s ∂Ψ ∂φ vn = ∂s = =0 ∂n (11.34) (11.35)

d)

Pela Equação 11.34: ⏐⏐⏐∂∂φs⏐⏐⏐=⏐⏐∂∂Ψn⏐⏐ Conclui-se que a variação de φ ao longo de r s é igual à variação de Ψ ao longo de r n; isso significa que φ ε Ψ formam uma rede quadrática.

e) O fato de φ ε Ψ obedecerem à equação de Laplace permite superpor soluções e fazer intercâmbios das duas funções.

f) A superfície de contato de um fluido em movimento com um corpo rígido fixo é uma linha de corrente (Figura 11.21).

<!-- p. 304 -->
Figura 11.21 De fato, como r v × r n =0 → grad φ × r n = 0 ou ∂φ ∂n ∂Ψ =0 = – ∂s Logo: Ψ(s) = cte g) Corolário Ao substituir uma linha equicorrente por uma superfície sólida, o escoamento não se altera. Sendo: vx = 4x – 6y vy = ky – f (x)

Determinar k e f (x) de forma que seja o campo de velocidades de um escoamento irrotacional de um fluido incompressível.

Determinar as funções de corrente e potencial.

Solução Incompressível:

div r v = 0 → ∂vx + ∂vy =0→ 4+ k =0 ∂x ∂y Irrotacional:

k = –4 rot r v = 0 → ∂vx – ∂vy =0→ – 6+ ∂f (x) = 0 ∂y ∂x ∂x Como f (x) é uma função só de x → df (x) = 6 dx f (x) = 6x + C Logo:

vx = 4x – 6y vy = –6x – 4y + C Na origem (0, 0)

→ r v = 0; logo:

C=0 Nesse caso: dΨ = ∂Ψ ∂x dx + ∂Ψ ∂y dy = –vydx + vxdy Logo:

∂Ψ = 4y + 6x → Ψ = 3x2 + 4xy + f (x) ∂x Então: ∂Ψ ∂y = 4x + df (y) dy = vx = 4x – 6y Logo:

df (y) = –6y ou f (y) = –3y2 + C dy Ψ = 3x2 + 4xy – 3y2 + C

<!-- p. 305 -->
C a p í t u l o 1 1 z Análise diferencial z 305 Se for adotado que na origem (0, 0), Ψ = 0 ⇒ C = 0 e finalmente:

Ψ = 3x2 + 4xy – 3y2 dφ = ∂φ ∂x dx + ∂φ ∂y dy = vxdx + vydy Logo: ∂φ ∂x = vx = 4x – 6y → φ = 2x2 – 6xy + f (y) Derivando em relação a y:

∂φ ∂y = –6x + df (y) dy = vy –6x + df (y) = –4y – 6x → f (y) = –2y2 + C dy Logo:

φ = 2x2 – 6xy – 2y2 + C Adotando φ = 0 na origem (0, 0), finalmente: φ = 2x2 – 6xy – 2y2 11.9.1 Análise de alguns tipos de escoamentos planos, irrotacionais, em regime permanente de fluido incompressível 11.9.1.1 Escoamento uniforme É o caso em que: Logo:

φ = v0x ∂φ vx = ∂x = v0 ∂φ vy = ∂y = 0 (11.36) (11.37)

O escoamento está representado na Figura 11.22.

Figura 11.22 ∂Ψ ∂Ψ As equicorrentes têm: ∂x = –vy e ∂y = vx Logo: ∂Ψ ∂y = v0 → Ψ = v0y +C Se para y = 0; Ψ= 0 → C = 0; logo Ψ = v0 y ∫ ∫ A vazão por unidade de espessura será dada por: q = 2dΨ 1 = 2 v 1 x dy = v 0 ( y 2 – y1 )

<!-- p. 306 -->
11.9.1.2 Fonte ou sorvedouro Fonte é um ponto que fornece fluido ao plano observado, e sorvedouro é um ponto que absorve o fluido. No caso da fonte, a função potencial em coordenadas cilíndricas é:

φ = A 2π ln r Campo de velocidades:

vr = ∂φ ∂r = ∂ ∂r ⎜⎝⎛ A 2π ln r⎞⎠⎟ A1 = 2π r ∂φ vθ = r∂θ = 0 Conclui-se que o campo de velocidades é radial, isto é:

∂Ψ A1 r∂θ = vr = 2π r Ψ = A θ +C 2π Se para θ = 0 adota-se Ψ = 0, então C = 0.

Logo: Ψ= A θ 2π As linhas de corrente são radiais caracterizadas por: A θ = cte 2π dΨ = A 2π dθ e integrando de 0 a 2π obtém-se: Ψ2 – Ψ1 = A.

Lembrar que a diferença entre duas equicorrentes é a vazão por unidade de espessura, Logo: A = q. Finalmente: φ = q 2π ln r Ψ= q θ 2π q vr = 2 πr No caso do sorvedouro, é só trocar os sinais.

Figura 11.23

<!-- p. 307 -->
C a p í t u l o 1 1 z Análise diferencial z 307 11.9.1.3 Vórtice ideal Nesse caso: φ = B 2π θ ∂φ r∂θ = vθ → B vθ = 2 πr → ∂Ψ vθ = – ∂r → Ψ = – B ln r 2π Logo, as linhas de corrente são linhas de r = cte; são, portanto, circunferências com centro na origem. Denomina-se circulação do vetor r v aΓ =∫ r vdP. Nesse caso: ∫ Γ = 2π – B rdθ = –B 0 2 πr A circulação Γ do vetor r v é a intensidade do vértice. Figura 11.24 11.9.1.4 Dipolo Foi visto que, pelo fato de φ ε Ψ serem funções harmônicas, pode-se invertê-las ou superpor diferentes funções. O dipolo é a superposição de uma fonte com um sorvedouro de mesma vazão e simétricos em relação à origem (Figura 11.25).

A fonte é representada por: φ1 = q 2π ln r1 e Ψ = q 2π θ1 e o sorvedouro por:

φ2 q = – 2π ln r2 e Ψ2 = – q 2π θ 2 Pela superposição dos dois escoamentos, obtém-se:

φ = φ1 +φ2 = q 2π ( ln r1 – ln r2 ) Figura 11.25

<!-- p. 308 -->
Mas r1 = r 2 + a 2 + 2ra cos θ e Logo:

r2 = r 2 + a 2 – 2ra cos θ φ = q 2π ⎡1 ⎢⎣2 ln (r 2 +a2 + 2ra cos θ) – 1 2 ln (r 2 +a2 – 2ra cos θ)⎤⎥⎦ Após algumas transformações algébricas e um desenvolvimento em série de potências, obtém-se: φ = q 4π ⎡2ra cos θ ⎢ ⎣ r2 +a2 2 – 3 ⎛⎝⎜ 2ra r2 cos θ +a2 ⎟⎠⎞ 3 + ⎤ ...⎥ ⎦ Passa-se ao limite para a → 0, isto é, superpõem-se a fonte e o sorvedouro na origem e ao mesmo tempo faz-se q → ∞ para que q a = m seja um número finito. Tem-se: 2π φ = m cos θ r onde m é a intensidade do dipolo.

Nesse caso:

∂φ m cos θ vr = ∂r = – r 2 ∂φ m sen θ vθ = r∂θ = – r 2 Como: ∂Ψ m cos θ r∂θ = vr = – r 2 Ψ = ∫ – m cos r θ dθ +f (r) = – m sen r θ +f (r)

∂Ψ m sen θ df (r)

m sen θ = ∂r r2 + dr = –vθ = r2 Logo:

df (r) = 0 ou f (r) = cte dr Adotando a constante igual a zero, obtém-se:

Ψ = – m sen θ r Passando para coordenadas cartesianas: cos θ = x e sen θ = y . Logo: r r x2 y2 r2 + r2 =1 ou r2 = x2 +y2 resultando em: φ = mx r2 = mx x2 +y2 my my e Ψ = r2 = x2 +y2 Para φ = cte e Ψ = cte, essas expressões representam circunferências passando pela origem (Figura 11.26).

<!-- p. 309 -->
C a p í t u l o 1 1 z Análise diferencial z 309 Figura 11.26 11.9.1.5 Superposição de um escoamento uniforme com um dipolo (Figura 11.27)

A superposição terá:

φ = v0 x + m cos r θ Ψ = v0 – m sen r θ Figura 11.27 O objetivo é encontrar a linha de corrente para a qual Ψ = 0, lembrando que ela pode ser substituída por uma superfície sólida. m sen θ v0y = r e pela figura y = r sen θ Logo: v0r sen θ = m sen r θ ou v0r sen θ – m sen r θ = 0 sen θ ⎜⎛⎝ v0 r – m r ⎞⎠⎟ = 0 Logo: sen θ = 0 ⇒ ⎧θ ⎩⎨θ = = 0 π ou v 0 r – m r = 0; logo: r= m , que é uma circunferência de centro na origem, com esse raio. v0

<!-- p. 310 -->
Conclui-se que esse escoamento representa o escoamento uniforme em volta de um cilindro de raio r (Figura 11.28). Na Figura 11.28, é interessante determinar o significado dos pontos (A) e (B).

φ = v0x + m cos r θ = v0r cos θ + m cos r θ Figura 11.28 vr ∂φ = ∂r = v0 cos θ – m cos r2 θ vθ = ∂φ r∂θ = –v 0 sen θ– m sen r2 θ Ponto (A) → ⎛ ⎜r = ⎝ m ; θ = π ⎞ ⎟ v0 ⎠ ⇒ vr = v0 cos π – m cos m π =0 v0 vθ = –v0 sen π – m sen m π =0 r v0 Logo, no ponto (A), v = 0, sendo um ponto de parada ou de estagnação. A mesma conclusão pode ser obtida para o ponto (B).

É dado o escoamento de um fluido incompressível, ideal (ρ = 1.000 kg/m3), em torno de um cilindro vertical de diâmetro 0,2 m. Determinar:

a) a pressão nos pontos (1) e (2) da figura, sabendo que a velocidade ao longe é v0 = 10 m/s e a pressão é p0 = 0; b) a equação da linha de corrente que passa no ponto (2).

<!-- p. 311 -->
C a p í t u l o 1 1 z Análise diferencial z 311 Solução Escoamento uniforme: Dipolo:

Escoamento sobre o cilindro:

φ = v0x = v0r cos θ Ψ = v0y = v0r sen θ φ = m cos θ r Ψ = – m sen θ r φ = v0r cos θ + m cos r θ Ψ = v0r sen θ – m sen r θ vr = ∂φ ∂r = v0 cos θ– m cos r2 θ = ⎝⎛⎜ v0 – m r2 ⎞⎟⎠ cos θ vθ = ∂φ r∂θ = –v0 sen θ– m sen r2 θ = – ⎜⎝⎛ v0 + m r2 ⎟⎠⎞ sen θ Para Ψ = 0 → v0r = m r → m = v0r 2 = 10 × 0,12 = 0,1 m 3/s Portanto:

φ = 10r cos θ + 0,1 cos θ r2 Ψ = 10r sen θ – 0,1 sen θ r2 vr = ⎝⎛⎜10 – 0r,21⎟⎠⎞ cos θ vθ = – ⎜⎝⎛10 + 0r,21⎞⎟⎠ sen θ a) Para o ponto (1): θ = 180o e r = 0,1 m.

vr1 = ⎝⎛⎜10 – 0,1 ⎞ 0,12 ⎠⎟ cos 180o =0 vθ 1 = – ⎜⎛⎝10 + 0,1 ⎞ 0,12 ⎟⎠ sen 180o =0 Para o ponto (2): θ = 30o e r = 0,2 m.

vr2 = ⎛⎜⎝10 – 0,1 ⎞ 0,2 2 ⎟⎠ cos 30o = 6,5 m/s Logo: vθ 2 = – ⎜⎝⎛10 + 0,1 ⎞ 0,2 2 ⎠⎟ sen 30o = –6,25 m/s | | r v= 6,5 r er – r 6,25 eθ ⇒ r v = 6,52 + 6,252 = 9 m/s Sendo o fluido ideal e incompressível e sendo o escoamento irrotacional, vale a equação de Bernoulli entre qualquer par de pontos. Lembrando que o plano mostrado é horizontal, portanto, Δz = 0, tem-se: v02 + p0 = v12 + p1 2g γ 2g γ p1 = ρv02 2 = 1.000 × 102 2 = 5× 104 Pa = 50 kPa v02 + p0 = v22 + p2 2g γ 2g γ

<!-- p. 312 -->
p2 = ρ 2 ( v02 – v22 )= 1.000 2 (102 – 92 )= 9.500 Pa = 9,5 kPa b) Lembrar que a linha de corrente é a linha para a qual Ψ= cte.

Deve-se, então, determinar a constante correspondente ao ponto (2).

Ψ = v0v2sen θ2 – m sen r2 θ2 = 10 × 0,2 × sen 30o – 0,1 sen 0,2 30o = 0,75 Logo: 10r sen θ – 0,1 sen θ = 0,75 r ou ⎛⎝⎜10r – 0r,1⎟⎞⎠ sen θ = 0,75 Portanto: r 2 – 0,075 r – 0,01 = 0 e, para cada θ, pode-se determinar o valor de r, permitindo o traçado da sen θ linha de corrente.

## 11.10 Equação de Navier-Stokes

A equação de Euler (Equação 11.15), vista anteriormente, é uma forma da equação da quantidade de movimento limitada a aplicações em que não haja efeitos da viscosidade. Para aplicações com fluidos reais, torna-se necessário considerar esses efeitos que produzem tensões de cisalhamento proporcionais às velocidades relativas entre duas partículas do fluido. Lembrar do Capítulo 1, que a existência de um escorregamento entre as partículas provoca o aparecimento das tensões de cisalhamento, naquela ocasião descrita pela lei de Newton da viscosidade.

No item 11.5, ao analisar o movimento das partículas do fluido, verificou-se que o deslizamento pode ser devido à translação, à rotação ou à deformação.

A previsibilidade desses movimentos das partículas só pode ser relativamente precisa em escoamentos bem comportados, como o laminar.

O equacionamento dos escoamentos turbulentos, em que existe uma aleatoriedade dos movimentos das partículas, exige um tratamento estatístico que foge das finalidades deste estudo. A equação de Navier-Stokes, que será introduzida a seguir, só permite descrever escoamentos laminares, ou pelo menos previsíveis de alguma forma.

Embora a equação utilize conceitos já introduzidos, não está nas finalidades deste desenvolvimento a sua dedução, sendo apresentado apenas o seu resultado, que representa a dinâmica da partícula, isto é, a equação da quantidade de movimento, agora com todos os seus termos. r a = r dv = r f – 1 grad p + 1 ν grad ( div r v) + ν∇ 2 r v dt ρ 3 (11.38) As primeiras parcelas do segundo membro provêm da equação de Euler, como foi visto no item 11.8; as duas últimas são a contribuição do efeito da viscosidade existente nos fluidos reais. A forma da terceira e quarta parcelas do segundo membro depende de hipóteses admitidas, necessárias para a dedução. Observa-se, experimentalmente, que essas hipóteses são exatas para gases e aproximadas para líquidos. O uso da equação de Navier-Stokes para casos gerais é de grande complexidade, exigindo métodos numéricos de integração que fogem do escopo deste estudo. Pode-seramenizar a complexidade aplicando-a para fluidos incompressíveis, já que para eles div v = 0 e a Equação 11.38 reduz-se a:

<!-- p. 313 -->
C a p í t u l o 1 1 z Análise diferencial z 313 r a = r f – 1 grad p + ν∇ 2 r v ρ (11.39)

onde ∇ 2 é o operador laplaceano, dado por:

∇2 ∂2 = ∂x2 ∂2 + ∂y2 ∂2 + ∂z 2 em coordenadas cartesianas e ∇2 ∂2 = ∂r 2 1∂ 1 + r ∂r + r 2 ∂2 ∂θ 2 ∂2 + ∂z 2 em coordenadas cilíndricas ν = Observar que 0, e no caso de a Equação 11.39 reduz-se à equação escoamento irrotacional emrquer rot rvdre=E0uel,ecrosnesoeqflüueindtoefmorenidtee,a∇l, i2svrto=é0,.se Lembrando que no campo da gravidade f = g = –ge z (supondo o plano xy horizontal), em coordenadas cartesianas a equação de Navier-Stokes resulta em:

∂v x ∂t + vx ∂v x ∂x + vy ∂v x ∂y + vz ∂v x ∂z 1 =–ρ ∂p ∂x + ν ⎛ ⎜ ⎝ ∂2 vx ∂x 2 + ∂2 vx ∂y 2 + ∂2 vx ∂z 2 ⎞ ⎟ ⎠ (11.40a) ∂v y ∂t + vx ∂v y ∂x + vy ∂v y ∂y + vz ∂v y ∂z 1 =–ρ ∂p ∂y + ν ⎛ ⎜⎝⎜ ∂2 vy ∂x 2 + ∂2 vy ∂y 2 + ∂2 vy ∂z 2 ⎞ ⎟⎠⎟ (11.40b) ∂v z ∂t + vx ∂v z ∂x + vy ∂v z ∂y + vz ∂v z ∂z = –g – 1 ρ ∂p ∂z + ν ⎛ ⎜ ⎝ ∂2 vz ∂x 2 + ∂2 vz ∂y 2 + ∂2 vz ∂z 2 ⎞ ⎟ ⎠ (11.40c) Em coordenadas cilíndricas, supondo z vertical, a equação resulta em:

∂v r ∂t + vr ∂v r ∂r + vθ r ∂v r ∂θ + vz ∂v r ∂z – v 2 θ 2 1 ∂p =– + ρ ∂r +ν ⎛ ⎜ ⎝ ∂2 vr ∂r 2 + 1 ∂vr r ∂r 1 + r2 ∂2 vr ∂θ 2 + ∂2 vr ∂z 2 2 – r2 ∂v θ ∂θ – vr r2 ⎞ ⎟ ⎠ ∂v θ ∂t + vr ∂v θ ∂r + vθ r ∂v θ ∂θ + vz ∂v θ ∂z + vr vθ r 1 ∂p = – ρ r∂θ + +ν ⎛ ⎜ ⎝ ∂2 vθ ∂r 2 1 + r ∂v θ ∂r + 1 r2 ∂2 vθ ∂θ 2 + ∂2 vθ ∂z 2 + 2 r2 ∂v r ∂θ – vθ r2 ⎞ ⎟ ⎠ ∂v z ∂t + vr ∂v z ∂r + vθ r ∂v z ∂θ + vz ∂v z ∂z 1 ∂p = –g – + ρ ∂z +ν ⎛ ⎜ ⎝ ∂2 vz ∂r 2 + 1 ∂vz r ∂r 1 + r2 ∂2 vz ∂θ 2 + ∂2 vz ∂z 2 ⎞ ⎟ ⎠ (11.41a) (11.41b) (11.41c)

## 11.11 Algumas aplicações da equação de Navier-Stokes

Para mostrar o manuseio da equação de Navier-Stokes serão apresentados a seguir alguns problemas de solução relativamente simples.

<!-- p. 314 -->
Dado o escoamento laminar, em regime permanente, de um fluido incompressível entre duas placas planas, horizontais, fixas, de dimensões infinitas, determinar a expressão do diagrama de velocidades e a perda de pressão ao longo do escoamento. Solução rr Pela figura, observa-se que v = vxex e que vx = f (z).

Como o regime é permanente e vy = 0 e vz = 0, as Equações 11.40 resultam em:

a) vx ∂vx ∂x = –1 ρ ∂p + ∂x ν ∂2vx ∂z 2 b) ∂p = 0 ⇒ p = cte( y ) ∂y c) ∂p + ρg = 0 ⇒ p = –ρgz + f (x) ou p + ρgz = f (x) ∂z Esse resultado mostra que, para cada seção x = cte, vale o teorema de Stevin, e para facilidade algébrica abrevia-se p + ρgz = p*, e ∂p* é função só de x. ∂x Além disso, como vx = f (z), implica que ∂vx ∂x = 0. Logo, a equação (a) resulta em: ∂p* ∂x = μ ∂2vx ∂z 2 , e como p* só é função de x dp* dx = μ ∂2vx ∂z 2 . Além disso, como vx = f (z), então: dp* dx =μ d 2vx. dz 2 Como o primeiro membro só é função de x e o segundo membro só é função de z, conclui-se que na realidade ambos correspondem a uma constante e podem ser integrados separadamente. Logo: μ d 2vx = β dz 2 dp* = β dx Assim, d 2vx = β dz2 μ ou dvx dz = β μ z+ C1 ou vx = βz 2 2μ + C1z + C2 p* = βx + C3 Condições de contorno 1) Para z = ± h ⇒ vx = 0, logo:

<!-- p. 315 -->
C a p í t u l o 1 1 z Análise diferencial z 315 0 = βh 2 2μ + C1h + C2 ⇒ ⎧⎪C2 ⎪⎪ ⎨ = – βh 2 2μ 0 = βh 2 2μ – C1h + C2 ⎪⎪C1 = 0 ⎪⎩ 2) Para z = 0 ⇒ vx = vmáx ⇒ vmáx = C2 Logo: vmáx = – βh 2 2μ ⇒ β = – 2μvmáx h2 Finalmente: vx = – 2μvmáx h2 z2 2μ + 2μvmáx h2 h2 2μ ⇒ vx = vmáx ⎜⎛1 ⎝ – z2 ⎞ h 2 ⎟ ⎠ A expressão resultante mostra que o diagrama de velocidades é parabólico.

Da outra equação diferencial: p* = βx + C3 Logo: p* = – 2μvmáx h2 x+ C3 Adotando para uma coordenada inicial x = 0 ⇒ C3 = p0*, obtém-se: p0* – p* = Δp* = 2μvmáx h2 x O escoamento analisado denomina-se ‘escoamento de Poiselle’.

No exemplo anterior, admitir a placa inferior fixa e a superior móvel, com velocidade v0. Determinar o diagrama de velocidades supondo dp = 0. dx Solução A primeira parte coincide com o problema anterior, resultando em:

μ d 2vx = 0 dz 2 que integrada resulta em:

dvx dz = C1 ⇒ vx = C1z + C2 Condições de contorno 1) Para z = 0 ⇒ vx = 0 ⇒ C2 = 0 2) Para z = h ⇒ vx = v0 ⇒ v0 = C1h ⇒ C1 = v0 h

<!-- p. 316 -->
Finalmente: vx = v0 h z Nesse caso, o diagrama é linear e o escoamento denomina-se ‘escoamento de Couette’. Um líquido escoa num plano inclinado com escoamento laminar, em regime permanente, dinamicamente estabelecido a uma certa distância do reservatório. Supondo escoamento bidimensional e desprezando o atrito com o ar, determinar a vazão em massa para uma largura b. Solução Se o escoamento é dinamicamente estabelecido ∂vx = 0.

∂x Simplificando os termos das equações 11.40, obtém-se:

a) 0 = g sen α – 1 ρ ∂p ∂x + ν ∂2vx ∂y2 b) 0 = –g cos α – 1 ∂p ρ ∂y c) 0 = ∂p ∂z De c) p = cte(z) (z é o eixo perpendicular ao plano da figura). De b) p = –ρgy cos α + f (x) Para y = h ⇒ p = 0 ⇒ 0 = –ρgh cos α + f (x) ou f (x) = ρgh cos α = cte De a) ∂2vx ∂y2 = – g sen ν α + 1 μ ∂p ∂x mas ∂p = 0; logo: ∂x ∂2vx = – ρg sen α ∂y2 μ Integrando: ∂vx ∂y = – ρg sen μ α y+ C1 vx = – ρg sen μ α y2 2 + C1y + C2 Condições de contorno 1) Para y = 0 ⇒ vx = 0 ⇒ C2 = 0

<!-- p. 317 -->
C a p í t u l o 1 1 z Análise diferencial z 317 2) Para y = h, ao desprezar o atrito com o ar, τ = 0 e, portanto:

μ ∂vx ∂y =τ = 0⇒ ∂vx ∂y = 0, logo C1 = ρgh sen α μ = gh sen α ν Portanto: vx = – gy2sen 2ν α + ghy sen ν α Finalmente: vx = gy sen ν α ⎝⎛⎜ h – y 2 ⎠⎞⎟ A velocidade média, numa seção transversal ao escoamento, é dada por (Capítulo 3): ∫ ∫ ∫ vm = 1 A vdA = 1 bh hgy 0 sen ν α ⎜⎛⎝ h – y 2 ⎞⎟⎠ bdy = g sen νh α h⎛ ⎜ yh – y2 ⎟⎞ dy = 0⎝ 2⎠ = g sen α ⎜⎛ y2h – y3 ⎞⎟ h = g sen α ⎛⎜ h 3 – h 3 ⎞⎟ = gh 3sen α νh ⎝ 2 6 ⎠ 0 νh ⎝ 2 6 ⎠ 3 νh vm = gh 2sen 3ν α Portanto, a vazão em massa será:

Qm = ρvmA = ρ gh 2sen 3ν α bh Finalmente: Qm = ρgbh 3 sen 3ν α Determinar o diagrama de velocidades numa seção do escoamento laminar de um fluido incompressível, em regime permanente, dinamicamente estabelecido num conduto de seção circular. Determinar a perda de carga entre duas seções do escoamento. Solução rr r r Adotando coordenadas cilíndricas:

Observe que vr = 0 e vθ = 0 ⇒ r v= v = r vr e r vxe x + vθ e θ + vxe x r Pela equação da continuidade, div v = 0, que em coordenadas cilíndricas fica:

1 ∂ ( rvr ) + 1 ∂vθ + ∂vx = 0 ⇒ ∂vx = 0 r ∂r r ∂θ ∂x ∂x Admite-se, ainda, por simetria que ∂vθ = 0. ∂θ

<!-- p. 318 -->
Examinando as equações 11.41, tem-se: a) ∂p* = 0 ∂r b) ∂p* = 0 ∂θ c) ∂p* ∂x = μ ⎛ ⎜ ⎝ ∂2vx ∂r 2 + 1 r ∂v x ⎞ ⎟ ∂r ⎠ onde p* = p + ρgz, como no primeiro exemplo.

Como o primeiro membro só é função de x e o segundo só de r, então as derivadas parciais confundem-se com as totais e o resultado dos dois membros deve coincidir com uma constante β.

(1) dp* = β dx (2) μ ⎛⎜ ⎝ d 2vx dr 2 + 1 r dvx dr ⎞⎟ ⎠ =β Integrando a (1) tem-se: p2* – p1* = β( x2 – x1 ) = βL (3)

A (2) resulta em: 1 r d dr ⎜⎛⎝ r dvx dr ⎞⎟⎠ = β μ ou d dr ⎜⎛⎝ r dvx dr ⎞⎠⎟ = βr μ Integrando uma primeira vez:

r dvx dr = βr 2 2μ + C1 Para r = 0 → C1 = 0, e pela lei de Newton da viscosidade, como τ = –μ ⎛⎜⎝ dvx dr ⎠⎞⎟ , então ⎜⎛⎝ dvx dr ⎟⎞⎠ r= 0 = –τ μ ≠ 0 O sinal negativo vem do fato de que o y da lei de Newton da viscosidade é medido a partir da menor velocidade, enquanto r é medido a partir do centro da tubulação, onde a velocidade é máxima. Logo: dvx dr = βr 2μ e integrando novamente vx = βr 2 4μ + C2 Para r = R → vx = 0, pelo princípio da aderência.

Logo: 0 = βR2 4μ + C2 Para r = 0 → vx = vmáx ⇒ C2 = vmáx e β = – vmáx 4μ R2 Portanto, vx = –vmáx r2 R2 + vmáx e finalmente: vx = ⎡ vmáx ⎢1 ⎢⎣ – ⎜⎝⎛ r R ⎞⎠⎟ 2 ⎤ ⎥ ⎥⎦ Esse resultado já é conhecido do Exemplo 3.1 do Capítulo 3, onde foi admitido sem nenhuma demonstração. Voltando à equação (3): p2* – p * 1 = – vmáx 4μL R2 ou p * 1 – p2* = 4μvmáxL R2 Lembrando que no escoamento laminar vm = vmáx 2 e que R = D 2 : p1* – p*2 = 32μvmL D2 ou ( p1 + γz 1 )– (p2 + γz 2 ) = 32μvmL D2

<!-- p. 319 -->
C a p í t u l o 1 1 z Análise diferencial z 319 Aplicando na equação da energia, com as hipóteses adotadas (Capítulo 4), a perda de carga de (1) a (2), tem-se: H p1,2 = ⎜⎝⎛ p1 γ + z1 ⎠⎞⎟ – ⎜⎝⎛ p2 γ + z2 ⎠⎞⎟ , já que vm1 = vm2 Logo: H p1,2 = 32μvmL γD2 Como a perda de carga de (1) a (2) é somente do tipo distribuída:

h f1,2 =f L v 2 m D 2g = 32μvmL γD2 ou f = 64μg = 64 ν, e como ν = 1 , obtém-se: f = 64 , ρgDvm vmD vmD Re Re verificando-se a expressão já vista e utilizada no Capítulo 7 para o escoamento laminar em condutos. Um viscosímetro de cilindros coaxiais utiliza um cilindro que gira no interior de outro. Admitindo que: a) o movimento entre os dois cilindros é laminar, quando o cilindro interno gira; b) as componentes radial e axial da velocidade são nulas; c) o escoamento não varia segundo o eixo z; d) despreza-se o efeito da base. Determinar o diagrama de velocidades e o momento causado pelas tensões de cisalhamento no cilindro externo, que é fixo. Solução vr = 0; vz = 0; ⇒ r v = vθ r e θ Pela equação da continuidade para fluido incompressível:

div rv = 1 ∂ ( rvr ) + 1 ∂vθ + ∂vz = 0 ⇒ ∂vθ = 0 r ∂r r ∂θ ∂z ∂θ Esse resultado mostra que vθ independe de θ e, como por hipótese independe de z, então vθ = f (r). A equação de Navier-Stokes segundo θ resulta em: 0 = ∂2vθ + 1 ∂vθ – vθ ∂r 2 r ∂r r 2

<!-- p. 320 -->
Como vθ só é função de r, as derivadas parciais coincidem com as totais e a expressão é equivalente a: d dr ⎝⎛⎜ dvθ dr + vθ r ⎟⎠⎞ = 0 ou dvθ dr + vθ r = C1 O primeiro membro equivale a: 1 d (vθ r), logo: r dr d (vθ dr r) = C1r ou vθ r = C1r 2 2 + C2, resultando em vθ = C1r 2 + C2 r Para r = R1 → vθ = ωR1 ⇒ ωR1 = C1R1 2 + C2 R1 Para r = R2 → vθ = 0 ⇒ 0 = C1R2 + C2 2 R2 Resolvendo o sistema, tem-se:

C1 = – 2ωR21 R22 – R21 C2 = ωR 21R 2 2 R 2 2 – R21 Logo: vθ = – ωR12 R22 – R12 r+ ωR21R22 R22 – R12 1 r ou vθ = ωR 21R 2 2 R22 – R12 1 ⎡ ⎢1 – r ⎣⎢ ⎜⎝⎛ r R ⎟⎞⎠ 2 ⎤ ⎥ ⎦⎥ Como τ = –μ dvθ dr ⇒ τ = μωR21R22 R 2 2 – R 2 1 1 r2 ⎡ ⎢1+ ⎣ ⎜⎛ ⎝ r R22 ⎟⎞ ⎠ ⎤ ⎥ ⎦ Para r = R2, isto é, junto ao cilindro externo:

τ = 2μωR12 R22 – R21 A força resultante das tensões de cisalhamento junto ao cilindro externo é:

Fτ = 2μωR12 R22 – R12 2 πR2h e o momento: Mτ = 4πμωhR12R22 R22 – R12 11.1 Dado o campo de velocidades vx = αx; vy = βy; vz = 0, determinar as trajetórias e as linhas de corrente. Resp.: Trajetórias: x = x0eαt; y = y0eβt; z = z 0 α Linhas de corrente: x = C1yβ ; z = C2

<!-- p. 321 -->
C a p í t u l o 1 1 z Análise diferencial z 321 11.2 r r rr Dado o campo de velocidades v (P, t) = 6xex + 6yey – 7tez , determinar:

a) a velocidade e a aceleração no ponto (3; 2; z), no instante t = 1; b) as linhas de corrente no instante t = 6/7; Resp.: c) a r trajetória r para r Pr0 (1; 1; r 0), no r instante r t= r 0.

a) v = 18ex + 12ey – 7ez ; a = 108ex + 72ey – 7ez b) x = C1y; x = e –z c) x = e6t; y = e 6t; z = –3,5t2 11.3 Dado o escoamento cujo campo de velocidades é:

vx = x t ; vy = y t ; vz = 0, determinar:

a) a equação da linha de corrente que passa pelo ponto P1 (2; 1; 2); b) a equação da trajetória que passa por P1, no instante t = 1; c) a aceleração num instante t qualquer, no ponto P1.

Resp.: a) x = 2y; z = 2; b) x = 2y; z = 2; c) r a = − 1 t2 r (2e x + r e y )

11.4 Sendo vx = x2 + z2 + 5; vy = y2 + z2, determinar a forma mais simples da componente vz que satisfaça a equação da continuidade para um fluido incompressível. Resp.: vz = –2z (x + y) 11.5 Dadas as componentes das velocidades de dois escoamentos de fluidos incompressíveis: (A)

⎪⎧vx = x2 – y ⎨ ⎪⎩vy = x3 – 2xy (B)

⎧⎪vx = y3 – 3x2y ⎨ ⎪⎩vy = 3xy2 – x3 a) Verificar se os dois escoamentos são possíveis.

b) c)

Verificar se são No movimento rotacionais ou irrotacionais. rotacional, determinar o lugar geométrico dos pontos, tal que: r Ω = 1/2 r ez .

Resp.: a) ambos são possíveis; b) (A) é rotacional; (B) é irrotacional; c) 3x2 – 2y = 0 11.6 Um fluido escoa em condições tais que sua massa específica ρ é função somente do tempo. Sendo o campo de velocidades vx = 4x; vy = –2y, determinar: a) a expressão de ρ (t) para que o escoamento seja possível; b) a equação das linhas de corrente. Resp.: a) ρ = Ke-2t; xy2 = C 11.7 rr No funil da figura, escoa um líquido com o campo de velocidades v = –vrer.

A vazão varia linearmente de 1 m3/s até zero entre o instante inicial e o final, atingido após 2 min. Determinar:

a) as componentes da velocidade; b) a equação das trajetórias; c) a aceleração.

<!-- p. 322 -->
Resp.: a) vr = 3 πrL ⎛⎜⎝1 – t 120 ⎞⎟⎠ ; vθ = 0; vz = 0 b) r = ⎡ ⎢ ⎣ 6 πL ⎛ ⎜ ⎝ t – t2 ⎞ ⎟ 240 ⎠ + r02 ⎤ ⎥ ⎦ c) r a = ⎡ −⎢ ⎢⎣ 1 40πLr – 9 π2L2r 3 ⎜⎝⎛ t 120 – 1⎞⎟⎠ 2 ⎤ ⎥ ⎦⎥ r er 11.8 Num plano, o escoamento de um fluido é definido por: vx = v0x + at; vy = v0y . Determinar: a) as linhas de corrente; b) as trajetórias.

Resp.: a) x= ⎜⎛ v0x + ⎜⎝ v0y at ⎞⎟ ⎟⎠ y+ C b) x = x0 + v0x t + at 2 2 ; y = v0y t + y0 11.9 Dado o campo de velocidades: r v = (16x2 + y) r ex + r 10e y + yz 2re z rr r r a) Qual é a velocidade angular do elemento fluido na posição definida pelo vetor r = 6ex + 3ey + 2e k? b) É possível ser o escoamento de um fluido incompressível? Resp.: a) r 2e x – 1 2 r ez ; b) não 11.10 As partículas de um fluido movem-se no plano xy com trajetórias definidas por: x = x0 + t; y = y0 + t2. a) Obter a equação e desenhar a trajetória da partícula que, no instante t = 0, encontra-se em P (0; 0). b) Determinar a equação das linhas de corrente.

c) Obter a equação e desenhar a linha de corrente que passa por P (0; 0), no instante t = 0,5. d) O movimento é permanente ou variado? Resp.:

a) x2 = y; b) x = y + C; c) x = y. 2t 11.11 Um fluido ideal incompressível escoa ao longo de duas paredes que formam um ângulo reto. O campo de velocidades é dado por: vx = 2ax; vy = –2ay. Determinar: a) a equação das linhas de corrente; b) as linhas isovelocidades (rv = cte ); c) a distribuição das pressões ao longo de Ox; d) a distribuição das pressões ao longo da bissetriz.

Resp.: a) xy = C; b) x2 + y2 = v2 ; 4a 2 c) p = p0 – 2a2ρx2; d) p = p0 – 4a2ρx2

<!-- p. 323 -->
C a p í t u l o 1 1 z Análise diferencial z 323 11.12 O movimento de um fluido incompressível de peso desprezível realiza-se segundo o campo de velocidades vx = ax; vy = by; vz = cz. a) Determinar as condições para as quais o movimento é possível.

b) Verificar a possibilidade de aplicar a equação de Bernoulli.

c) Calcular a resultante da força de pressão sobre a placa de vértices A (–m; 0; m); B (m; 0; –n); C (m; 0; n); D (–m; 0; n). Admitir que, no ponto (0; 0; 0), p = p0.

Resp.: a) a + b + c = 0; b) possível; c) F = 2n ⎜⎛ ⎝ 2mp 0 – ρa 2m 3 3 ⎟⎞ ⎠ 11.13 O cilindro da figura gira em torno de seu eixo com rotação constante ω. O líquido nele contido forma a superfície livre indicada e, a fim de determinar o desnível h, aplicou-se a equação de Bernoulli entre (1) e (2), obtendo-se h = – (ω R )2 , quando se sabe que o resultado correto é h = (ω R )2 . Explicar, apli2g 2g cando a equação de Euler, por que a equação de Bernoulli falha ao determinar o resultado. 11.14 Sendo vx = 4x – 6y; vy = ky – f (x), determinar k e f (x) para que este seja o campo de velocidades de um escoamento irrotacional de um fluido incompressível. Determinar as funções de corrente e potencial. Resp.: k = –4; f (x) = 6x + C; φ = 2x2 – 6xy – 2y2 + C; Ψ = 3x2 + 4xy – 3y2 + C 11.15 Seja um meteorito que penetra na atmosfera. Admitir em primeira aproximação que o escoamento seja bidimensional e irrotacional na região próxima ao ponto de estagnação. Sabe-se que o escoamento pode ser representado pela superposição de uma fonte de intensidade q, com origem em (O), com um escoamento uniforme de velocidade v0 na direção mostrada na figura. a) Determinar as expressões das funções potencial e de corrente correspondentes à superposição, em coordenadas polares. b) Determinar a expressão das componentes da velocidade em função de v0, q, θ e r. c) Se v0 = 1.000 m/s e o corpo tem raio de 1 m, determinar a intensidade da fonte para que se tenha o escoamento desejado. Resp.: a) Ψ = q 2π θ + v0 r sen θ; φ = q 2π ln r + v0 r cos θ b) vr = q 2 πr + v0 cos θ; vθ = –v0 sen θ; c) q = 2.000π m3/s/m 11.16 Dada a função de corrente Ψ = ar – bθ, para r ≠ 0, onde a e b são constantes positivas: a) determinar a equação das trajetórias;

<!-- p. 324 -->
b) calcular a vazão em volume através de uma superfície semicircular de raio r e centro na origem, de espessura unitária; c) verificar se o movimento é irrotacional e, se for, determinar a função potencial. Resp.: a) Se para t = 0, r = 0 e θ = 0 → r = 2bθ; b) q = –πb; c) φ = –bln r – arθ a 11.17 A função de corrente de um escoamento plano de um fluido incompressível, entre duas placas infinitas, paralelas, é dada por: Ψ = v0 y2 2L a) Determinar o diagrama de velocidades e representá-lo graficamente. b) Verificar se o escoamento é possível. c) O movimento é variado ou permanente? d) O movimento é rotacional ou irrotacional? e) Determinar a cota do ponto (C) que divide a seção (A) (B) em duas seções (AC) e (CB) de mesma vazão. Resp.: a) vx = v0 L x; b) possível; c) permanente; d) rotacional; e) yc =L 2 2 11.18 Dada a função potencial φ = x2 – y2 para um fluido incompressível em movimento plano irrotacional, determinar:

a) a função potencial; b) o campo de velocidades.

Resp.: a) Ψ = 2xy + C; b) vx = 2x; vy = –2y; vz = 0 11.19 No estudo analítico de um furacão, admitiu-se que o escoamento resulte da superposição de um vórtice ideal com um sorvedouro no ponto O. Sendo a função potencial do sorvedouro φ = – q ln r e a função de corrente do vórtice ideal Ψ = – Γ 2π ln r, onde q = 2 × 104 m3/s.m e Γ = 5 × 104 m2/s, determi2π nar:

a) a velocidade do escoamento no ponto P dado por xP = 300 m e yP = 400 m; b) o lugar geométrico dos pontos de mesma pressão que passa por P.

Sabe-se que ao longe p = p0 e v = v0 constantes.

Resp.: a) r v = – 20 π r er + 50 π r e θ ; b) r = q 2 + Γ2 1 = C 2 πv

<!-- p. 325 -->
C a p í t u l o 1 1 z Análise diferencial z 325 11.20 Seja Ψ = 9 + 6x – 4y + 7xy.

a) Verificar se essa função pode ser a função de corrente de um fluido incompressível. b) Verificar se o escoamento é irrotacional.

c) Determinar a velocidade no ponto (0; 0).

Resp.: a) sim; b) sim; c) r v = r –4e x – r 6e y 11.21 É dada a função de corrente Ψ = x2 + 2xy + 4t2y. No instante t = 2 s, determinar: a) Qual é a vazão por unidade de espessura entre (A) e (B)? b) Qual é a vazão por unidade de espessura entre (A) e (C)? Resp.: a) qBA = 9,6 m3/s. m; 9 m3/s. m 11.22 Dado o campo de velocidades do escoamento plano de um fluido ideal incompressível: vx = 2x2(2 – t ) – 6x f (y, t) ln t vy = –6x2y (2 – t) + 2y3(2 – t )

a) Determinar f (y, t) para que o escoamento seja possível. b) Com a f (y, t) determinada, obter a função de corrente Ψ quando t = 1 s. c) Se possível, determinar a função φ.

Resp.: a) f (y, t) = y2(2 – t ); b) Ψ = 2x3y – 2xy3 + C; c) φ = x4 – 3x2y2 + y4 + C ln t 2 2 11.23 No escoamento de um fluido incompressível entre duas placas fixas infinitas, o diagrama de velocidades é dado por vx = Cy (h – y), onde C é uma constante, h é a distância entre as duas placas e y é uma coordenada perpendicular às placas, com origem numa delas. Determinar vm e a vazão em volume por unidade de vmáx largura.

Resp.: vm = 2 ; Q = Ch 3 vmáx 3 6 11.24 Um líquido de viscosidade μ = 0,3 N. s escoa entre duas placas paralelas, infinitas, distantes 5 mm, m2 com escoamento laminar. O gradiente de pressões ao longo do escoamento é 2.000 N m2 /m . Determinar a tensão de cisalhamento na placa superior e a vazão em volume por unidade de profundidade. Resp.: τ = 2,5 N/m2; Q = 6,94 × 10–5 m3/s/m 11.25 Um fluido incompressível escoa no anel formado entre dois tubos concêntricos de seção circular. O escoamento é laminar e o raio externo do tubo menor é R1, enquanto o raio interno do maior é R2. a) Verificar se a equação do diagrama de velocidades é dada por:

v = 2 R 2 2 – r2 – 2rm2áxln ⎝⎜⎛ R2 r ⎠⎞⎟ vm R22 + R 2 1 – 2rm2 áx

<!-- p. 326 -->
onde: rmáx = R 2 2 – R 2 1 2 ln ⎛ ⎜ R2 ⎞ ⎟ ⎝ R1 ⎠ sendo r uma coordenada polar e rmáx a coordenada onde ocorre a velocidade máxima. b) Sendo R1 = 10 cm e R2 = 10,2 cm, determinar a coordenada da velocidade máxima e, para uma vazão de 0,1 L/s, obter vmáx. Resp.: rmáx = 10,1 cm; vmáx = 0,156 m/s 11.26 Apóia-se um peso sobre um pistão de 10 mm de diâmetro, e a leitura do manômetro da figura é 2 MPa. A viscosidade do fluido é 0,5 N.s/m2 e o comprimento do pistão é 10 cm. Adotando o modelo de duas placas planas paralelas, determinar a folga entre o pistão e o cilindro para que o pistão desça apenas 2 mm por minuto. Adotar uma queda de pressão linear ao longo do escoamento na folga. Resp.: 3,2 × 10–6 m 11.27 Uma chapa fina deve passar de forma contínua num banho de tinta contido num reservatório, como mostra a figura. Em regime permanente, o diagrama de velocidades bidimensional vz = f (x) é tal que, numa seção, a vazão é nula, já que parte da tinta sobe arrastada pela chapa e parte retorna por gravidade, mantendo a espessura constante. Como a velocidade da chapa é baixa, admite-se que o atrito com o ar (τ) é desprezível. Determinar:

a) a expressão do diagrama de velocidades; b) a velocidade de subida da chapa para que a espessura da camada de tinta seja h = 0,3 mm. Dados: νtinta = 5 × 10–5 m2/s; g = 10 m/s2.

Resp.: a) vz = gh ν y⎜⎛⎝ y 2h – 1⎞⎠⎟ + v0; b) v0 = 6 × 10–3 m/s.

<!-- p. 327 -->

# Capítulo 12 — Escoamento compressível

C a p í t u l o 1 2 z Escoamento compressível z 327

## 12.1 Introdução — Hipóteses — Conceitos fundamentais

No Capítulo 1, definiu-se fluido incompressível como sendo o que tem massa específica ρ constante em todos os pontos do escoamento. Logo, fluido compressível é aquele cuja massa específica varia de um ponto a outro. Na realidade, nenhum fluido, tampouco os sólidos, são perfeitamente incompressíveis; entretanto, se a variação da massa específica ρ for pequena e compatível com a precisão desejada, será lícito desprezar essa variação e equacionar o escoamento com a hipótese de ρ constante. Nesse caso, as equações básicas da continuidade, da energia e da quantidade de movimento têm um desenvolvimento relativamente simples, conforme foi visto nos capítulos 3, 4 e 5 deste estudo. Entretanto, ao equacionar os fluidos como incompressíveis, quando a massa específica varia sensivelmente, chega-se a conclusões quantitativas e até qualitativas que não condizem com as observações práticas, assim como não é possível prever acontecimentos como a onda de choque e o bloqueio dos condutos. A massa específica é uma função da pressão e da temperatura e, junto com os fenômenos equacionados pela Mecânica dos Fluidos, será necessário fazer uma análise dos efeitos térmicos estudados pela Termodinâmica. Nesse caso, o estudo realizado até aqui, que apenas em certas ocasiões esbarrou na consideração de efeitos térmicos, deverá ser adaptado ao uso das variáveis e conceitos tipicamente utilizados nos cursos de Termodinâmica, como energia interna, entalpia, entropia e outras. A complexidade, causada por efeitos térmicos no estudo dos escoamentos pela Mecânica dos Fluidos, pode ser atenuada admitindo-se algumas hipóteses simplificadoras que, até certo ponto, pouco influirão na modelagem. Essas hipóteses são: a) O escoamento é unidimensional ou uniforme nas seções.

Como este estudo irá se referir a gases em velocidades relativamente altas, os elevados números de Reynolds indicarão uma uniformização dos diagramas de velocidades, com exceção de uma camada muito fina junto à parede sólida, devido ao princípio da aderência. Dessa forma, a hipótese adotada aproxima-se bastante da realidade. Por outro lado, seria possível utilizar a velocidade média na seção, e para o cálculo da energia cinética o coeficiente α será aproximadamente unitário, conforme descrito no Capítulo 4. b) O regime é permanente. c) O fluido que escoa é um gás perfeito.

<!-- p. 328 -->
Na prática, nenhum gás obedece perfeitamente ao modelo de gás perfeito; entretanto, numa larga faixa de pressões e temperaturas, essa hipótese aproxima suficientemente os resultados aos observados na prática, simplificando as expressões matemáticas e permitindo uma análise qualitativa mais clara. As hipóteses descritas anteriormente serão sempre válidas no estudo a seguir, podendo ser ressaltado que ele irá se referir ao escoamento unidimensional, em regime permanente de um gás perfeito.

## 12.2 Definições

Apesar de os capítulos anteriores conterem termos que permitem considerar os efeitos térmicos, a ênfase, seja nos conceitos, seja nos exercícios de aplicação, foi sempre voltada para o estudo do escoamento de fluidos incompressíveis, sem explicitar os possíveis efeitos térmicos. Utilizando esse enfoque, a equação da energia, até o item 4.8, apresentou apenas parcelas mecânicas como energia cinética, potencial e pressão, cujo estudo tornou-se mais interessante ao considerá-las por unidade de peso e ao denominá-las cargas. Lembrar que os termos v2 p foram escritos 2g , z e γ e sua unidade resultou em metro, já que ao dividir energia por peso obtém-se unidade de comprimento. O atual entrelaçamento da Mecânica dos Fluidos com a Termodinâmica faz com que seja mais interessante trabalhar com energias por unidade de massa, denominadas específicas. De uma forma geral, a transformação de uma grandeza por unidade de peso para a respectiva por unidade de massa é realizada pela seguinte expressão:

Grandeza ou Grandeza específica = Grandeza × g Massa Peso (12.1)

Assim, por exemplo: v2 Energia cinética específica = 2 Energia potencial específica = gz Energia de pressão específica = p γ × g = p ρg × g = p ρ J N. m m m2 A unidade será: = kg kg = s2 .m = s2 A seguir, serão definidas as grandezas termodinâmicas necessárias a este estudo.

### 12.2.1 Energia interna (I)

Embora um significado mais amplo dessa grandeza possa ser obtido dos livros de Termodinâmica, para as finalidades deste estudo, será confundida com energia térmica e será função apenas da temperatura, representando o estado térmico do sistema. A energia interna específica será:

I u= m

### 12.2.2 Entalpia (H)

Definida por: H = I + pV

<!-- p. 329 -->
C a p í t u l o 1 2 z Escoamento compressível z 329 H I pV Por unidade de massa será: = + mmm e lembrando que V m = 1 ρ = v (volume específico) p h = u + = u + pv ρ

### 12.2.3 Entropia (S)

A variação de entropia é definida por:

onde: dS = ⎝⎛⎜⎜ ~ dQ T ⎟⎠⎞⎟ rev ~ Q = calor trocado pelo sistema (o símbolo é utilizado para que não haja confusão com o símbolo da vazão em volume)

T = temperatura absoluta O índice ‘rev’ significa ‘processo reversível’.

É interessante lembrar da Termodinâmica que um processo é reversível quando pode ser invertido e ao voltar ao estado inicial não haverá vestígios de sua realização no Universo. Todos os processos práticos são irreversíveis e algumas causas das irreversibilidades são: atrito, trocas de calor entre diferenças finitas de temperaturas, expansões e compressões bruscas, Por reações químicas e, unidade de massa:

ddse=umdmSa=fo⎜⎜⎛⎝rdmQ~Ta/mge⎞⎟⎟⎠rraevl, a = rapidez ⎛⎜⎝ dq T ⎠⎞⎟ rev dos processos.

dq Se o processo for irreversível, verifica-se que: ds > T Se o processo for adiabático (sem troca de calor), dq = 0 e ds > 0, o que mostra que, se não há troca de calor durante o processo, a entropia deve aumentar e, de certa forma, representa a J m2 irreversibilidade dele. A unidade será: kg.K = s2 . .K

## 12.3 Gás perfeito

No estudo a ser realizado neste capítulo, gás perfeito será o modelo matemático utilizado e caracterizado pelas propriedades a seguir: a) Equação de estado p = RT ρ (12.2)

onde: p = pressão na escala absoluta ρ = massa específica T = temperatura absoluta R = constante do gás Indicando por θ a grandeza fundamental temperatura, para não confundir com T, que ao longo do texto indicou a grandeza fundamental tempo: R = p RT ⇒ [R] = FL –2 FL–4 T 2 θ = L2 T –2 θ

<!-- p. 330 -->
m2 Logo, a unidade de R será: s 2 .K J m2 Por exemplo: R ar = 287 kg. k ou s2 .K Para obter o valor de R para outros gases, será necessáriorecorrer a textos de Termodinâmica ou lembrar que: R = R , de forma que basta dividir o valor da constante universal M mol dos gases R = 8.314,5 J pelo valor numérico da massa molecular do gás em estudo. mol b) A energia interna e a entalpia são funções somente da temperatura, isto é: u = f (T) e h = f (T) c) Os calores específicos a volume constante (cv) e a pressão constante (cp) são constantes do gás. Lembrar que: c v = ⎛⎝⎜ ∂u ∂T ⎟⎞⎠ V=c te para qualquer substância.

Para u = f(T) pode-se confundir a derivada parcial com a total e, portanto:

cv = ⎝⎜⎛ du dT ⎟⎠⎞ V = c t−e Apesar de cv ser determinado por um processo a volume constante, uma vez estabelecido, torna-se uma propriedade do gás, utilizável em qualquer caso em que for necessário. Integrando a expressão anterior, ao longo de um processo:

∫ ∫ 2 2 du 1 = c 1 v dT e ao considerar cv = cte:

u 2 – u1 = cv( T2 – T1 ) ou Δu = cvΔT (12.3a)

Observa-se que a hipótese de cv = cte simplifica sobremaneira a determinação das variações de energia interna dos gases ou a própria determinação da energia interna se for adotada uma origem. Esse modelo elimina a necessidade do uso de tabelas e, embora prejudique a precisão dos resultados quantitativos, permite interpretar mais facilmente os resultados qualitativos, facilitando a compreensão dos fenômenos que, de outra forma, se perderia no emaranhado das complicações matemáticas e nos dados das tabelas.

Da mesma forma: cp = ⎝⎜⎛ ∂h ∂T ⎞⎟⎠ p= c t−e , mas ao se adotar h = f (T) e cp = cte:

cp = ⎛⎝⎜ dh dT ⎠⎞⎟ p= c te e Δh = cpΔT (12.3b)

Se a origem da medida de u e h for adotada para T = 0, também se pode escrever:

u = c vT h = cpT (12.3c)

A partir dos calores específicos, podem ser obtidas as seguintes expressões úteis: k = cp , denominada constante adiabática cv (12.4) R = cp – cv (12.5)

<!-- p. 331 -->
C a p í t u l o 1 2 z Escoamento compressível z 331 R cv = k –1 kR cp = k –1 (12.6) (12.7)

## 12.4 Problema geral e equações básicas

A solução de um problema de escoamento de um fluido visa, dadas as propriedades do fluido numa seção e as condições de contorno, determinar as propriedades do fluido em outra seção. As variáveis de interesse normalmente são: v, p, T, ρ, h, u, s. Como existem sete variáveis, no problema mais geral, seriam necessárias sete equações. Entretanto, como u, h = f (T), serão necessárias apenas cinco (Figura 12.1). Figura 12.1 É claro que o problema pode ser invertido. Dadas as variáveis da seção (1), determinar as da seção (2); dadas as condições intermediárias ou as variáveis da seção (2), determinar as da seção (1) ou, também, dadas as variáveis das duas seções, verificar as condições intermediárias. Para a solução desses problemas, serão apresentadas a seguir as equações básicas disponíveis, a maioria já citada nos capítulos anteriores e algumas derivadas da Termodinâmica. Não esquecer que, pelas hipóteses fundamentais, o escoamento é unidimensional em regime permanente de um gás perfeito.

### 12.4.1 Equação da continuidade

Figura 12.2 Dadas duas seções quaisquer do escoamento, lembrar que, para regime permanente (Capítulo 3, Equação 3.12): Qm1 = Qm2 ρ1 v1 A1 = ρ 2 v2 A 2 (12.8) (12.9)

<!-- p. 332 -->
Além das equações que relacionam as propriedades em duas seções quaisquer, deseja-se também obter o relacionamento entre as propriedades em duas seções vizinhas, a uma distância infinitesimal (dx) (Figura 12.2). As equações diferenciais resultantes permitem analisar qualitativamente as tendências de cada variável, dependendo da hipótese adotada. As variáveis envolvidas serão representadas a montante (seção (1) no sentido do escoamento) pelo seu símbolo e a jusante (seção (2) no sentido do escoamento) pelo seu símbolo, somado a um diferencial, que pode ser positivo, negativo ou nulo, dependendo das condições entre (1) e (2). Por exemplo: Seção (1) ⇒ a área é A Seção (2) ⇒ a área é A + dA Se dA > 0, o conduto é divergente ⇒ Se dA < 0, o conduto é convergente ⇒ Se dA = 0, o conduto é de seção constante ⇒ As equações diferenciais assim construídas facilitam a análise da variação qualitativa das propriedades ao longo do escoamento. No caso da Figura 12.2:

ρvA = (ρ + dρ)(v + dv)(A + dA)

Efetuando o produto do segundo membro e desprezando os infinitésimos de segunda e terceira ordem, obtém-se: ρvA = ρvA + ρAdv +ρvdA + vAdρ Simplificando e dividindo tudo por ρ, tem-se: dρ dv dA + + =0 ρvA (12.10)

Note-se que a equação da continuidade é uma função f (ρ, v, A) = 0, que permite relacionar massas específicas, velocidades e áreas de duas seções do escoamento. Dada a geometria do escoamento, isto é, A1 e A2, essa equação cria apenas uma relação entre massa específica e velocidade, sem permitir a obtenção de seus valores numéricos. Lembrar que, ao estudar fluidos incompressíveis, como ρ1 = ρ2, era possível obter v2 em função de v1, desde que a geometria do conduto fosse conhecida.

### 12.4.2 Equação da energia

No Capítulo 4 obteve-se a Equação 4.37, que por unidade de massa resulta em:

<!-- p. 333 -->
C a p í t u l o 1 2 z Escoamento compressível z 333 α 1 v12 2 + p1 ρ1 + u1 + gz1 + gHM + q = α 2 v 2 2 2 + p2 ρ2 +u2 + gz 2 Como o escoamento é unidimensional, α 1 = α 2 = 1.

Por se tratar de um gás, a variação de energia potencial pode ser desprezada em comparação com os outros termos, e lembrando que u + p ρ = h, obtém-se: v12 2 + h1 + gHM +q = v 2 2 2 +h2 (12.11) Se entre as seções (1) e (2) não houver máquina:

v12 2 + h1 + q = v 2 2 2 +h2 (12.12)

Se o escoamento entre (1) e (2) for adiabático:

v12 2 + h1 = v 2 2 2 +h2 (12.13)

A Equação 12.13 mostra que, se entre (1) e (2) não houver fornecimento ou retirada de energia do fluido, a soma da energia cinética com a entalpia deverá ser constante em todas as seções do escoamento. Na forma diferencial, pela Figura 12.3, obtém-se:

v2 ( v + dv)2 + h + dq = + h + dh 2 2 Figura 12.3 Simplificando e desprezando o termo de segunda ordem:

dq = vdv + dh (12.14)

No caso em que o escoamento seja adiabático (dq = 0):

vdv = –dh ou vdv = – cp dT (12.15)

o que mostra que as variações de v e T são contrárias, isto é, se v aumenta, h e T devem diminuir, ou vice-versa. Note-se que h engloba as energias térmica e de pressão e, pela conservação da energia, um aumento da velocidade deverá ser obtido em detrimento da pressão e da temperatura. Pelo exposto, a equação da energia é uma função que relaciona v e h ou v e T, isto é: f (v, h) = 0 ou f (v, t) = 0 Junto com a equação da continuidade, a equação da energia forma um sistema de duas equações com três variáveis: ρ, v, T.

<!-- p. 334 -->
### 12.4.3 Equação da quantidade de movimento

Para facilidade algébrica, aplica-se a equação para um conduto reto de seção constante (Figura 12.4). Figura 12.4 Sendo o regime permanente, do Capítulo 5 obtém-se:

r r r rr FS = –[p1 A1 n 1 + p 2 A 2 n 2 + Qm ( v 2 – v1 )] Projetando na direção x:

FSx = p1 A 1 – p 2 A 2 + Q m ( v1 – v 2 ) e para uma distância infinitesimal dx: dFSx = pA – (p + dp) A + ρvA [v – (v + dv)] ou dFSx = –dp – ρvdv A Lembrando que FSx parede sólida entre (1) e éa (2), resultante das pressões supondo o escoamento e tensões de sem atrito (τ cisalhamento do fluido = 0), então dFSx = 0 e:

na dp = –ρvdv (12.16)

que é do tipo: f (p, ρ, v) = 0, que acrescenta uma equação ao sistema, mas introduz a variável p.

### 12.4.4 Equação de estado

p Pela hipótese de gás perfeito: ρ = RT que é do tipo f (p, ρ, T) = 0. Essa expressão completa quatro equações para quatro variáveis, v, ρ, T, p, tornando o sistema proposto determinado.

### 12.4.5 Variação de entropia

Quando a variação de entropia é importante, pode-se lançar mão das expressões da Termodinâmica para um gás perfeito, aqui introduzidas sem dedução.

dT dρ dT dp ds = cv T – R ρ ou ds = cp T –R p (12.17)

Essas equações são do tipo f (s, T, ρ) = 0 ou f (s, T, p) = 0 e acrescentam apenas a variável entropia como nova, mantendo o sistema determinado. Dessa forma, obtém-se o sistema de cinco equações a cinco incógnitas, necessário para a análise qualitativa das tendências ao longo do escoamento, ou das soluções quantitativas, quando necessário.

## 12.5 Velocidade do som

É a velocidade de propagação de uma perturbação da pressão causada num fluido.

<!-- p. 335 -->
C a p í t u l o 1 2 z Escoamento compressível z 335 A velocidade de propagação é função do estado do fluido e, portanto, é uma propriedade que pode ser relacionada com outras e é de grande utilidade no estudo do escoamento compressível. Para melhor compreender o fenômeno, suponha-se o modelo matemático constituído de um fluido perfeitamente incompressível (Figura 12.5). Figura 12.5 A partir da situação de equilíbrio, aplica-se no pistão uma força dF, provocando no fluido um aumento de pressão dp = dF . Se o fluido for perfeitamente incompressível, o aumento A de pressão dp se transmitirá imediatamente para a seção seguinte, desta para a próxima, e assim por diante, de forma que, instantaneamente, a camada de fluido mais afastada será submetida ao aumento da pressão e imediatamente o fluido será derramado. Essa descrição mostra que num fluido incompressível a ‘mensagem’ de que ele foi perturbado numa seção (aplicação do dp) transmite-se instantaneamente para todas as seções, propagando-se com velocidade infinita. Quando o fluido é compressível, ao deslocar o pistão, cria-se uma compressão na camada adjacente à sua face, que fica com uma pressão maior que a seguinte, expandindo-se contra ela. Esta, então, ficará mais comprimida que a próxima, expandindo-se contra a seguinte comprimindo-a, e assim por diante. Nota-se que esse processo de compressões e expansões sucessivas leva um tempo finito e, portanto, a ‘mensagem’ da aplicação do dp propaga-se com uma velocidade finita que será denominada ‘velocidade de propagação da perturbação da pressão’. Como esse fenômeno é semelhante ao fenômeno acústico de propagação do som, a velocidade de propagação da perturbação da pressão é denominada ‘velocidade do som’ e será representada daqui para a frente pelo símbolo c. Pelo que foi explicado, fluido incompressível pode ser definido como o que tem ρ = cte ou c = ∞, o que abre uma nova perspectiva para o estudo dos fluidos, já que a grandeza c passa a ser um valor representativo da compressibilidade deles. Neste ponto, é importante determinar relações entre a nova propriedade c e as propriedades já conhecidas dos fluidos, para que a velocidade do som possa ter alguma utilidade na interpretação dos fenômenos. Com essa finalidade, observar o modelo da Figura 12.6, em que o pistão se desloca com velocidade elementar dv, transmitindo ao fluido uma variação dp da pressão, cuja velocidade de propagação já vimos que é c. Figura 12.6

<!-- p. 336 -->
Numa fotografia instantânea seria observado o fluido na situação indicada pela Figura 12.6. A região à esquerda, já tendo recebido a ‘notícia’ da perturbação, assumirá a velocidade dv e novas propriedades (p + dp, ρ + dρ, T + dT), enquanto a região à direita da frente da onda, ainda não atingida por ela, que se desloca com velocidade c, terá as propriedades iniciais (v = 0, p, ρ, T). Adotando um tubo de corrente estacionário, haverá pontos em que, num certo instante, as propriedades seriam as iniciais e em outro instante o novo valor, o que caracteriza um regime variado, já que a situação varia de um instante a outro. Para caracterizar um regime permanente, será adotado um referencial móvel, isto é, um VC fixo na frente de onda, que se desloca com ela. A Figura 12.7 mostra o modelo adotado, em que o VC tem comprimento nulo, apenas envolvendo a onda. Figura 12.7 Para o observador da figura, o fluido penetrará sempre pela seção (1), com velocidade c e com as propriedades iniciais, e sairá sempre pela seção (2), com velocidade c – dv e com as novas propriedades. Essa constância das propriedades caracteriza um regime permanente, permitindo a aplicação das equações básicas. Equação da continuidade Qm1 = Qm2 ρAc = (ρ + dρ) A (c – dv)

ρc = ρc – ρdv + cdρ – dρdv Simplificando e desprezando o termo de segunda ordem: dρ dv = c ρ (12.18)

Equação da quantidade de movimento r r rr FS = –[p1 A1 n 1 + p 2 A 2 n 2 + Q m ( v 2 – v1 )] Projetando na direção de x:

dFSx = –[pA (1) + (p + dp) A(–1) + ρAc (–c + (c – dv))] Como FSx é a resultante das pressões e das tensões de cisalhamento na superfície lateral do VC, e esta tem área nula, pois o comprimento é nulo, então dFSx = 0, resultando em: 0 = –pA + pA – dpA + ρAcdv Logo: dp dv = ρc (12.19)

Igualando a Equação 12.18 com a Equação 12.19: dρ dp c= ρ ρc

<!-- p. 337 -->
C a p í t u l o 1 2 z Escoamento compressível z 337 e, portanto: c2 = dp dρ ou dp c= dρ (12.20)

Essa equação, que não admitiu nenhuma hipótese, é válida numa seção do escoamento de qualquer fluido e mostra que a velocidade do som está relacionada com a variação da massa específica causada pela variação de pressão. No caso limite de fluido incompressível, qualquer que seja dp, dρ será nulo, resultando em c = ∞. Um caso de grande interesse é a determinação da velocidade do som numa seção, quando se considera a hipótese de isoentrópico (s = cte ou ds = 0). Como ds = 0, as Equações 12.17 resultam em:

dT dp cp T = R p dT dρ cv T =R ρ Dividindo uma pela outra e lembrando que cp = k, obtém-se: cv dp p dρ = k ρ (12.21) p dp Como ρ = RT, então dρ = kRT e substituindo na Equação 12.20:

c = kRT (12.22)

## 12.6 Número de Mach (M)

É a relação entre a velocidade do fluido numa seção e a velocidade do som na mesma seção. Logo: M= v c (12.23)

O número de Mach permite classificar os escoamentos nos seguintes tipos:

• M < 0,2 — escoamento incompressível • 0,2 < M < 1 — escoamento subsônico • M = 1,0 — escoamento sônico • M > 1,0 — escoamento supersônico Esses escoamentos têm características distintas, conforme será visto mais adiante. Pelo exposto, os fluidos incompressíveis deveriam ter M = 0, pois c = ∞; entretanto, como nenhuma substância é perfeitamente incompressível quando sujeita a uma perturbação da pressão, faz-se, então, uma concessão à precisão até M ≤ 0,2, por razões que serão justificadas posteriormente. Assim, os escoamentos com baixos números de Mach podem ser estudados com a utilização das equações válidas para as hipóteses de fluido incompressível, isto é, supondo ρ ≅ cte.

<!-- p. 338 -->
## 12.7 Estado de estagnação – Relações entre as propriedades do fluido e

as propriedades do estado de estagnação Como já foi visto, a energia por unidade de massa de um fluido compõe-se de:

• v2 Energia cinética:

2 • Energia potencial: gz • p Energia de pressão: ρ • Energia interna ou térmica: u = cv T No caso do estudo de gases, já foi visto anteriormente que a variação de energia potencial, em geral, pode ser desprezada comparativamente à variação das outras energias. Logo, a energia total específica de um gás em movimento é dada por:

Energia total v2 p v2 p v2 massa = 2 + ρ + u = 2 + ρ + cv T = 2 + h (12.24)

Lembrando a equação da energia (Equação 12.11) entre duas seções (1) e (2) do escoamento: v12 2 + p1 ρ1 + cv T1 + q + gHM = v 2 2 2 + p2 ρ2 + cvT2 ou ⎛⎜ v 2 2 ⎝2 + p2 ρ2 + cv T2 ⎞⎟ ⎠ – ⎛⎜ ⎝ v12 2 + p1 ρ1 + c v T1 ⎞⎟ ⎠ = q + gHM (12.25) ou ⎛⎜ Energia total ⎞⎟ ⎝ Massa ⎠ 2 – ⎜⎛ Energia total ⎞⎟ ⎝ Massa ⎠ 1 = q + gHM (12.26)

A Equação 12.26 mostra que a variação da energia total do fluido só pode ocorrer quando há troca de calor ou trabalho com o meio. Se não existir nenhum desses dois efeitos, a energia total deverá se manter constante em todas as seções, isto é: ⎛⎝⎜ Energia total Massa ⎟⎠⎞ 1 = ⎜⎛⎝ Energia total Massa ⎠⎞⎟ 2 (12.27) v12 2 + p1 ρ1 + cv T1 = v 2 2 2 + p2 ρ2 + cvT2 (12.28a) ou v12 2 + h1 = v 2 2 2 +h2 (12.28b) Nessas equações, observa-se mais facilmente que variações da velocidade de uma seção a outra são possíveis à custa de variações da pressão e temperatura ou da entalpia, quando não há máquina nem trocas de calor. Denomina-se estado de estagnação de um fluido, numa seção do escoamento, o estado que se atinge ou se atingiria ao parar o fluido isoentropicamente, isto é, sem perdas de energia. Nota-se pela definição que o estado de estagnação será atingido quando se obtiver numa v2 seção a transformação da energia cinética em energia de pressão (p) e térmica (T). 2 O estado de estagnação não precisa, necessariamente, ser medido, já que, conhecendo a velocidade, ele pode ser calculado, tendo em vista que numa certa seção:

<!-- p. 339 -->
C a p í t u l o 1 2 z Escoamento compressível z 339 v2 2 p + ρ + cvT = p0 ρ0 + cvT0 = h0 v2 ou 2 + h = h 0 (12.29)

Daqui para a frente o índice (0) será utilizado para representar as propriedades do estado de estagnação: h0, p0, T0, ρ0. Obviamente, a pressão e a temperatura de estagnação se constituem na maior pressão e na maior temperatura que poderiam ser atingidas numa seção do escoamento, se toda a energia cinética fosse transformada em energia de pressão e térmica. Por sua vez, a entalpia de estagnação representa a máxima energia disponível para a obv2 tenção de energia cinética . 2 A Figura 12.8 mostra como poderiam ser concebidas as medidas da pressão e da temperatura de estagnação. Figura 12.8 O manômetro (1), cuja tomada de pressão é perpendicular às linhas de corrente do escoamento, registra apenas a pressão p das partículas do fluido que passam sucessivamente com velocidade v junto à tomada. Nota-se que essas partículas conservam a sua energia cinética. O manômetro (2) é ligado a um tubo de Pitot que faz a tomada de pressão na direção das linhas de corrente. As partículas de fluido, que incidem no tubo de Pitot sucessivamente, transmitem ao manômetro (2) não somente a mesma pressão registrada pelo manômetro (1), v2 mas também o efeito da energia cinética 2 , de maneira que p0 > p.

Da mesma forma, as partículas que passam pelo termômetro (1) conservam a sua energia cinética e o termômetro registra somente a temperatura do fluido em movimento. Já o termômetro (2) registra a temperatura do fluido, mais o efeito da energia cinética, pois as partículas de fluido, ao atingirem o bulbo, adquirem v = 0, transformando a sua energia cinética em energia térmica e, assim, T0 > T. O estado de estagnação será usado como referência da energia disponível em cada seção do escoamento do fluido. O conceito é válido também para fluidos incompressíveis, se bem que, nesse caso, o efeito da energia térmica é secundário. Aplicando a equação de Bernoulli na Figura 12.9, obtém-se:

v12 2g + p1 γ + z1 = v 2 2 2g + p2 γ + z 2, onde: z1 = z2 ;v2 = 0; p2 = p0

<!-- p. 340 -->
Figura 12.9 Portanto:

p 0 = v12 + p1 γ 2g γ ou, num ponto genérico:

ρv 2 p0 = 2 +p (12.30)

o que mostra que a pressão registrada pelo manômetro diferencial deve-se à energia cinética, já que: ρv 2 p0 – p = 2 = h (γ m – γ)

ou v= 2h ρ ( γ m – γ) = 2gh⎛⎜ γ m –1⎟⎞ ⎝γ ⎠ Para fluidos compressíveis o conceito é o mesmo, mas devem ser considerados os efeitos térmicos. Aplicando a Equação 12.13, na ausência de troca de calor, já que o processo é isoentrópico: v12 2 + h1 = v 2 2 2 +h2 (12.31)

Numa seção genérica, o estado de estagnação corresponde a v = 0, logo:

v2 2 +h =h0 v2 2 + cpT = cpT0 Dividindo por cpT:

T0 = 1+ v2 T 2cp T Pela Equação 12.8: Mas, pela Equação 12.22: ou T0 ( k –1)v2 = 1+ T 2kRT T0 T k –1 v2 = 1+ 2 c2 T0 = 1+ k –1M2 T 2 (12.32)

<!-- p. 341 -->
C a p í t u l o 1 2 z Escoamento compressível z 341 A Equação 12.32 mostra que T0 ou T = f (k, M) e, portanto, como k é função apenas do fluido, uma vez escolhido o gás, T T = f T0 (M). T0 Pela Equação 12.21, pode-se deduzir que para processos isoentrópicos:

1 p0 ρ k 0 p = ρk ou ρ 0 = ⎛⎜ p0 ⎟⎞ k ρ ⎝ p⎠ (12.33) mas p = RT e ρ p0 ρ0 = RT0 ⇒ p p0 ρ0 ρ = T T0 ⇒ T T0 = p0 p ρ ρ0 na Equação 12.32:

p0 ρ k –1 = 1+ p ρ0 2 e pela Equação 12.33:

k p0 p = ⎝⎛⎜1 + k –1 2 M 2 ⎠⎟⎞ k –1 (12.34)

Analogamente:

1 ρ0 ρ = ⎜⎛⎝1 + k –1 2 M 2 ⎞⎠⎟ k –1 (12.35)

Desenvolvendo a Equação 12.35 em série de potências, obtém-se:

p0 = ρv 2 p+ 2 ⎜⎛1+ M 2 ⎝4 + 2 − k M 2 +...⎞⎟ 24 ⎠ (12.36)

Se M for pequeno, então a Equação 12.36 reduz-se a:

ρv 2 p0 = p+ 2 que coincide com a Equação 12.30 para fluidos incompressíveis.

Se M ≤ 0,2, verifica-se que o desvio da Equação 12.36 para a Equação 12.30 é pouco maior que 1%, de forma que, nesse caso, o fluido pode ser considerado incompressível.

pρT As equações 12.33, 12.34 e 12.35 permitem obter os valores de p0 , ρ0 , T0 para cada valor de M, uma vez escolhido um certo gás ou, em outras palavras, escolhido o k (Apêndice – Tabela 1 – para k = 1,4). Assim, para cada seção do escoamento, pode-se obter a função f ⎜⎛ p , ρ , T , M ⎞⎟ = 0 numericamente. ⎝ p0 ρ0 T0 ⎠

## 12.8 Algumas aplicações da teoria

### 12.8.1 Medida da velocidade de um gás com tubo de Pitot em escoamento subsônico

A Figura 12.10 mostra um tubo de Pitot básico, ou tubo de impacto.

<!-- p. 342 -->
Figura 12.10 Pela Equação 12.34, tem-se:

k p0 p = ⎛⎝⎜ 1 + k – 2 1 M 2 ⎞⎠⎟ k– 1 ou, lembrando que M = v e c = kRT e isolando v, tem-se: c ⎡ k –1 ⎤ v= 2k k –1 RT ⎢ ⎢ ⎜⎛ ⎝ p0 p ⎟⎞ ⎠ k – 1⎥⎥ ⎣ ⎦ (12.37)

A Equação 12.37 mostra a maior complexidade das expressões quando se envolve a compressibilidade do fluido.

A equação manométrica escreve-se como foi explicado no Capítulo 2; entretanto, como o fluido que escoa é um gás cujo γ << γm, obtém-se:

p0 – p = γ m h ou p0 = γ mh –1 pp Substituindo na Equação 12.37:

v= ⎡ 2k k –1 RT ⎢⎢⎝⎛⎜1 + γ m h ⎟⎞ p⎠ k –1 k ⎤ – 1⎥⎥ ⎣ ⎦ (12.38)

### 12.8.2 Venturi em escoamento subsônico – Coeficiente de compressibilidade

Como foi visto anteriormente, o Venturi é um conduto convergente/divergente por meio do qual se cria uma diferença de pressão entre duas seções que permite, por exemplo, medir a vazão que escoa. Ao considerar o fluido compressível, a expressão final resultante difere sensivelmente daquela válida para incompressíveis, vista anteriormente. A Figura 12.11 mostra esquematicamente um Venturi em que escoa um gás subsonicamente.

<!-- p. 343 -->
C a p í t u l o 1 2 z Escoamento compressível z 343 Pela equação da continuidade: ρ1 v1 A1 = ρ 2 v2 A 2 ou v1 = v2 A2 A1 ρ2 ρ1 1 e, supondo o escoamento isoentrópico: ρ 2 = ⎛⎜ p2 ⎟⎞ k ρ1 ⎝ p1 ⎠ Logo: 1 v1 = v2 A2 A1 ⎛⎜ p2 ⎝ p1 ⎟⎞ k ⎠ Mas ou v12 2 + h1 = v 2 2 2 +h2 v12 2 + cp T1 = v 2 2 2 + cpT2 Portanto: v 2 2 – v12 = 2c p T1 ⎜⎛1 ⎝ – T2 T1 ⎞⎟ ⎠ v 2 2 – v12 = 2kR p1 k –1 Rρ1 ⎜⎛1 – ⎝ T2 T1 ⎞⎟ ⎠ mas como: k –1 T2 = ⎛⎜ p2 ⎟⎞ k T1 ⎝ p1 ⎠ então: v 2 2 – v12 ⎡ = 2k k –1 ⎢ p1 ⎢ ⎢⎣ ρ1 ⎜⎛ ⎝⎜⎜1 – ⎜⎛ ⎝ p2 p1 ⎟⎞ ⎠ k –1 k ⎟⎞ ⎟⎟⎠ ⎤ ⎥ ⎥ ⎦⎥ Figura 12.11 (12.39) (12.40)

<!-- p. 344 -->
Substituindo a Equação 12.39 na Equação 12.40, obtém-se:

v2 = ⎡ k –1 ⎤ 2k p1 k –1 ρ1 ⎢⎢1 – ⎣⎢ ⎛⎜ p2 ⎝ p1 ⎟⎞ ⎠ k ⎥ ⎥ ⎦⎥ 2 1– ⎛⎜ A 2 ⎟⎞ 2 ⎜⎛ p2 ⎟⎞ k ⎝ A1 ⎠ ⎝ p1 ⎠ A vazão em massa teórica, pois o escoamento foi considerado isoentrópico, será:

QmT = ρ2 v2 A2 = ρ2 A2 ⎡ k –1 ⎤ 2k p1 k –1 ρ1 ⎢⎢1 ⎣⎢ – ⎜⎛ ⎝ p2 p1 ⎟⎞ ⎠ k ⎥ ⎥ ⎦⎥ 2 1– ⎛⎜ A 2 ⎞⎟ 2 ⎛⎜ p2 ⎟⎞ k ⎝ A1 ⎠ ⎝ p1 ⎠ E, após algumas transformações, obtém-se:

QmT = 1 p1 RT1 ⎛⎜ ⎝ p2 p1 ⎟⎞ ⎠ k A 2 ⎡ k -1 ⎤ 2k k –1 ⎢⎢1 ⎣⎢ – ⎜⎛ ⎝ p2 p1 ⎟⎞ ⎠ k ⎥ ⎥ ⎥⎦ 2 1– ⎛⎜ A 2 ⎞⎟ 2 ⎛⎜ p2 ⎟⎞ k ⎝ A1 ⎠ ⎝ p1 ⎠ (12.41)

Supondo ρ1 = ρ 2 , isto é, escoamento incompressível, a Equação 12.41 simplifica-se para: Q ' m T = p1 RT1 A2 2⎜⎛1 – p2 ⎟⎞ ⎝ p1 ⎠ 1– ⎛⎜ A 2 ⎟⎞ 2 ⎝ A1 ⎠ (12.42) onde Q ' m T é a vazão em massa que se obteria supondo o escoamento de um gás perfeito, mas sem a variação de ρ. Logo, a relação entre QmT e Q ' m T fornece o desvio entre as vazões, ao se considerar o gás compressível e incompressível.

φ = QmT Q ' m T Esse coeficiente é denominado ‘coeficiente de compressibilidade’ e a sua expressão é obtida pelo quociente entre as equações 12.41 e 12.42.

<!-- p. 345 -->
C a p í t u l o 1 2 z Escoamento compressível z 345 1 φ = ⎜⎛ p2 ⎞⎟ k ⎝ p1 ⎠ ⎡ k k– 1 ⎢⎢1 ⎢⎣ – ⎛⎜ ⎝ p2 p1 ⎟⎞ ⎠ k -1 k ⎤ ⎥ ⎥ ⎦⎥ ⎡ ⎢1 – ⎣⎢ ⎛⎜ ⎝ A2 A1 ⎟⎞ 2 ⎠ ⎤ ⎥ ⎦⎥ ⎡ ⎢⎢1 – ⎢⎣ ⎛⎜ ⎝ A2 A1 ⎞⎟ ⎠ 2 ⎛⎜ ⎝ p2 p1 ⎟⎞ ⎠ 2 k ⎤ ⎥ ⎥ ⎥⎦ ⎛⎜1 – ⎝ p2 p1 ⎟⎞ ⎠ (12.43) No caso particular em que a seção (1) seja o ambiente e, portanto, um reservatório de grandes dimensões, A1 = ∞, logo: 1 φ = ⎜⎛ p2 ⎞⎟ k ⎝ p1 ⎠ ⎡ k –1 ⎤ k k– 1 ⎢⎢1 – ⎢⎣ ⎜⎛ ⎝ p2 p1 ⎞⎟ ⎠ k ⎥ ⎥ ⎦⎥ 1– p2 p1 (12.44) Assim: QmT = φ Q ' mT = φ p1 RT1 A2 2 ⎛⎜1– p2 ⎟⎞ ⎝ p1 ⎠ 1– ⎜⎛ A 2 ⎞⎟ 2 ⎝ A1 ⎠ (12.45)

É importante lembrar que essas equações foram obtidas supondo o escoamento isoentrópico, portanto adiabático e reversível. Retirando-se a hipótese de reversível, considerando o atrito, a vazão real pode ser calculada utilizando-se o coeficiente de vazão ou de descarga (CD), valor experimental definido no Capítulo 8.

CD = Qm QmT ou Q m = C DQ m T Logo: Qm = CD φ p1 RT1 A2 2 ⎜⎛1– p2 ⎞⎟ ⎝ p1 ⎠ 1– ⎛⎜ A 2 ⎟⎞ 2 ⎝ A1 ⎠ (12.46)

ou, no caso em que a seção (1) pertença ao ambiente: Qm = C D φ A 2 2ρ1( p1 – p2 ) (12.47)

onde φ é dado pela Equação 12.44.

### 12.8.3 Descarga de um gás para a atmosfera por um orifício de um reservatório de grandes dimensões

Seja o reservatório da Figura 12.12, onde o orifício é de bordo delgado. Pelos mesmos conceitos utilizados no caso de líquidos (Capítulo 8), forma-se a veia contraída, e, na seção (C), a área é a área contraída AC e a velocidade do jato é vC.

<!-- p. 346 -->
Figura 12.12 Supondo o escoamento isoentrópico, pela equação da energia:

v 2 C 2 =h0 –hC = cp(T0 – TC ) v 2 C 2 = cpT0 ⎛⎜1 – ⎝ TC T0 ⎞⎟ ⎠ ⎡ k –1 ⎤ = kR k –1 T0 ⎢⎢1 – ⎢⎣ ⎛⎜ ⎝ pC p0 ⎟⎞ ⎠ k ⎥ ⎥ ⎥⎦ Logo: vC = ⎡ k –1 ⎤ 2k k –1 RT0 ⎢⎢1 – ⎢⎣ ⎛⎜ ⎝ pC p0 ⎟⎞ ⎠ k ⎥ ⎥ ⎥⎦ (12.48) A vazão em massa teórica será:

1 QmT = ACρCvC = A Cρ0 ⎛⎜ ⎝ pC p0 ⎞⎟ ⎠ k vC A vazão real será obtida considerando-se o coeficiente de descarga, como foi feito no Venturi, lembrando, ainda, que no caso do orifício existe a contração do jato, que também é computada no coeficiente de descarga. Lembrar do Capítulo 8 que CD = CvCc.

1 Logo: Qm = C D A O ρ 0 ⎜⎛ ⎝ pC p0 ⎞⎟ k ⎠ vC (12.49)

Se na Equação 12.48 for considerado:

k –1 k –1 ⎜⎛ pC ⎞⎟ k ⎝ p0 ⎠ = ⎡ ⎢1 – ⎣ ⎜⎛ ⎝ p0 – pC p0 ⎟⎞ ⎠ ⎤ ⎥ ⎦ k Expandindo em série de potências, resulta:

k –1 ⎛⎜ pC ⎞⎟ k ⎝ p0 ⎠ =1– k –1 ⎛⎜ p0 – pC k ⎝ p0 ⎟⎞ – 1 ⎠ 2k ⎝⎛⎜ kk–1⎟⎠⎞ ⎛⎜ p0 – pC ⎝ p0 ⎞⎟ 2 – ⎠ ⎛⎜⎝ 6kk+21⎟⎞⎠ ⎜⎛⎝ k – k 1⎟⎠⎞ ⎛⎜ ⎝ p 0 –p p0 C ⎞⎟ 3 ⎠ + K Supondo que p0 – pC seja pequeno comparado com p0, então:

k –1 ⎛⎜ pC ⎞⎟ k ≅ 1– k –1 ⎜⎛ p0 – pC ⎟⎞ ⎝ p0 ⎠ k ⎝ p0 ⎠

<!-- p. 347 -->
C a p í t u l o 1 2 z Escoamento compressível z 347 e substituindo na Equação 12.48:

2 vC = ρ0 (p0 – pC )

(12.50)

que é a mesma expressão que se obteria para um líquido.

Entretanto, no caso em que p0 – pC não seja suficientemente pequeno para permitir que se despreze o segundo termo da série, tem-se: vC = 2 ρ0 (p0 – pC )

1+ 1 p0 – pC 2k p0 (12.51)

Comparando as equações 12.51 e 12.50, verifica-se que o erro que se comete ao considerar o gás incompressível corresponde ao segundo fator da expressão. 12.8.4 Propagação de uma onda de pressão num meio compressível homogêneo a partir de um ponto emissor Neste item mostram-se as primeiras diferenças entre os escoamentos subsônicos e supersônicos. O fenômeno analisado será a propagação de ondas de pressão a partir de um ponto emissor localizado no espaço, ocupado por um fluido de propriedades homogêneas. Do ponto de vista relativo, é indiferente que o fluido esteja em movimento ou em repouso em relação a um inercial. O que se irá supor é que o sistema de referência esteja fixo no fluido, de tal forma que seja sempre observado apenas o movimento do ponto emissor em relação ao fluido. Será analisada a propagação de ondas com a velocidade do som, a partir de um único ponto, em todas as direções, a partir do ponto emissor, formando frentes de onda esféricas, que no plano da figura serão vistas como circunferências. Por outro lado, as emissões serão observadas em instantes sucessivos, em intervalos de tempo discretos e iguais. a) Ponto em repouso (M = 0) Se o ponto estiver em repouso, as ondas, emitidas em instantes sucessivos e iguais, irão se propagar radialmente, como é mostrado na Figura 12.13, e todas as esferas serão concêntricas no ponto P. Figura 12.13 Suponha-se, por exemplo, que no instante t4 o sistema seja fotografado. Nesse instante, a onda emitida no instante t1 distará do ponto emissor P de um raio c (t4 – t1) = 3cΔt, onde Δt = t2 – t1 = t3 – t2 = t4 – t3. A onda emitida no instante t2 distará 2cΔt do ponto P, a onda emitida no instante t3 distará cΔt e, a do instante t4 ainda não terá se propagado no instante da fotografia (t4). A configuração do evento é mostrada na Figura 12.13, onde, devido ao repouso do ponto, ele será o centro comum a todas as esferas. O processo da propagação é facilmente explicado. Quando o ponto P aumenta localmente a pressão, o fluido nessa posição fica mais comprimido que o vizinho, contra o qual irá se expandir. Essa expansão, por sua vez, irá comprimir a camada vizinha, que se expandirá contra a próxima, e assim por diante, provocando a propagação da variação da pressão através do fluido.

<!-- p. 348 -->
Se o ponto está em repouso, a propagação é igual em todas as direções, fazendo com que a região perturbada continue com suas propriedades distribuídas homogeneamente (supondo emissões contínuas e não discretas), isto é, os mesmos p, T, ρ em todos os pontos da região perturbada, embora diferentes da região ainda não atingida. O mesmo poderia ser concluído se a velocidade v do ponto fosse bem menor que a velocidade c da propagação, isto é, se v/c = M fosse pequeno. A seguir, serão analisados os acontecimentos quando a velocidade do ponto emissor não for desprezível comparativamente com a velocidade de propagação da perturbação, isto é, se M atingir valores mais elevados. b) Ponto emissor com movimento subsônico (M 1) Para facilitar a compreensão, será adotado um valor particular do número de Mach, isto é, M = v/c = 0,5, portanto v = 0,5c. Isso significa que a velocidade do ponto emissor é a metade da velocidade de propagação da onda de pressão ou, por outro lado, no mesmo intervalo de tempo, a onda emitida num certo instante percorrerá o dobro da distância percorrida pelo ponto no mesmo intervalo de tempo. Da mesma forma que no caso do ponto em repouso, suponha-se a emissão de ondas sucessivas em intervalos de tempo iguais e que o sistema seja fotografado no instante t4 (Figura 12.14). Figura 12.14 Na fotografia, o ponto estaria na posição P (t4), tendo percorrido a distância 3vΔt. As outras posições não apareceriam na fotografia e representam o seu passado. A onda emitida no instante t1, no intervalo de tempo em que o ponto se desloca para P (t4) (instante da fotografia), percorrerá o dobro da distância percorrida pelo ponto, já que c = 2v. A onda emitida no instante t2 propaga-se a partir do ponto P (t2) no intervalo de tempo em que o ponto se desloca para P (t4), percorrendo o dobro da distância percorrida pelo ponto. Analogamente para a onda propagada a partir de P (t3). A onda emitida a partir do ponto P (t4) não aparece na foto, pois esse é o instante em que ela foi disparada e ainda não houve propagação. Na figura, nota-se perfeitamente a aproximação das ondas no sentido do movimento e um afastamento em sentido contrário, dando origem ao efeito Doppler. Além disso, a aproximação das ondas no sentido do movimento e o afastamento em sentido contrário alteram a distribuição das propriedades p, T e ρ do fluido na zona perturbada, diferentemente do caso em que o número de Mach era nulo ou muito pequeno. c) Ponto emissor com movimento sônico (M = 1) Nesse caso, a velocidade do ponto emissor é igual à velocidade do som, isto é, da onda de perturbação que se propaga a partir dele.

<!-- p. 349 -->
C a p í t u l o 1 2 z Escoamento compressível z 349 Na realidade, no sentido do movimento do ponto não haverá propagação, pois sendo v = c todas as perturbações se acumularão no próprio ponto, criando uma região de alta pressão denominada ‘barreira do som’ (Figura 12.15). A explicação para a construção é análoga à do item anterior. Figura 12.15 d) Ponto emissor com movimento supersônico (M 1) Para facilidade de raciocínio, admite-se, por exemplo, M = 2, isto é, v = 2c. Nesse caso, a velocidade do ponto é maior que a velocidade de propagação da onda de pressão causada no meio. Por causa disso, o ponto se desloca à frente das ondas que se propagam após a passagem do ponto (Figura 12.16). Figura 12.16 Nesse caso, o meio não recebe o ‘aviso’da passagem do ponto com antecedência pela propagação das ondas de pressão à sua frente, como no caso do subsônico. O ponto passa de repente pelo fluido e a propagação da perturbação acontece posteriormente. Esse fenômeno cria efeitos bastante sensíveis de compressibilidade e fenômenos não estudados no escoamento de fluidos incompressíveis ou subsônicos, como, por exemplo, o aparecimento de ondas de choque, cujo estudo será feito posteriormente. Na Figura 12.17 verifica-se que as esferas propagadas na passagem do ponto têm como superfície envolvente comum um cone, denominado cone de Mach.

<!-- p. 350 -->
Figura 12.17 Pela Figura 12.17, verifica-se que: sen β = c3Δt = c = 1 v3Δt v M ou o seno do semi-ângulo do cone de Mach é igual ao inverso do número de Mach do movimento. Nota-se que o espaço fica dividido em duas regiões distintas: uma interna ao cone, em que o meio está perturbado pela passagem do ponto, e outra externa, denominada zona de silêncio, em que o fluido ainda não foi perturbado. Na análise de efeitos sonoros, um observador somente perceberia a passagem do ponto quando viesse a ter contato com o cone de Mach. Um avião é considerado um ponto que voa a uma altitude de 500 m com M = 2. Quanto tempo levará para que um observador na terra ouça a perturbação a partir do instante em que o avião passou verticalmente acima de sua cabeça? Dados para o ar: k = 1,4; R = 287 m 2 e T = 300 K. s2K Solução Como o escoamento é supersônico, o observador perceberá a perturbação somente quando for atingido pelo cone de Mach. sen β = 1 = 1 ⇒ β = 30° M2 Logo:

s = h = 500 = 866 m tg β tg 30o Como:

M = v então v = M.c c

<!-- p. 351 -->
Mas Logo: e, portanto:

C a p í t u l o 1 2 z Escoamento compressível z 351 c = kRT = 1,4 × 287 × 300 = 347 m/s v = M.c = 2 × 347 = 694 m/s t = s = 866 = 1,2 s v 694 12.9 Escoamento unidimensional em regime permanente, isoentrópico, de um gás perfeito, em conduto de seção variável

### 12.9.1 Introdução

No item 12.2.3 foi visto que a variação de entropia por unidade de massa é dada por: ds = ⎜⎝⎛ dq T ⎠⎟⎞ rev Pela definição, conclui-se que, para que o escoamento seja isoentrópico, são necessárias duas condições: a) processo reversível (sem atrito, sem expansões bruscas, sem trocas de calor entre diferenças finitas de temperaturas etc.); b) processo adiabático (q = 0). Logo, para ser isoentrópico o processo precisa ser adiabático, reversível. É óbvio que, adotando essas hipóteses ao pé da letra, em condições práticas, nunca o escoamento seria isoentrópico. Entretanto, dentro de uma certa aproximação, esse tipo de escoamento será válido se os efeitos de irreversibilidades e trocas de calor forem relativamente pequenos. Os escoamentos reais terão uma boa aproximação com esse modelo se: a) as paredes do conduto forem isoladas termicamente; b) a área das paredes for relativamente pequena, não possibilitando grandes trocas de calor; c) a viscosidade do fluido for relativamente pequena, não produzindo grandes tensões de cisalhamento e, portanto, atrito intenso. Muitos escoamentos práticos podem ser estudados por esse modelo, cujas hipóteses, aplicadas nas equações básicas, conduzem a um trabalho algébrico relativamente simples e a conclusões de fácil visualização. Dessa forma, muitos escoamentos observados na prática podem ser resolvidos matematicamente e as equações obtidas poderão ser corrigidas por coeficientes empíricos, obtidos pela comparação dos resultados experimentais com os teóricos. Note-se que o estudo dos fluidos, em geral, e dos fluidos compressíveis, em particular, devido à sua complexidade, terá normalmente esse tipo de abordagem, isto é, o estabelecimento de hipóteses simplificadoras numa primeira aproximação e uma correção empírica posterior para a adaptação à realidade, já que o equacionamento exato é praticamente impossível pelo grande número de variáveis envolvidas. Dessa forma, o leitor deve ter consciência da importância da análise dimensional no estudo da Mecânica dos Fluidos. 12.9.2 Variação das propriedades do fluido ao longo do escoamento em função da variação da área da seção do conduto e do número de Mach Neste item será verificado que, quando o fluido escoa ao longo de um conduto de seção variável, convergente ou divergente, as suas propriedades irão variar ao longo do escoamento e, dependendo de o escoamento ser sub ou supersônico, essa variação terá características

<!-- p. 352 -->
opostas. Por outro lado, o fato de o escoamento ser isoentrópico implica a exigência da variação da área da seção, pois, de outra forma, as propriedades seriam constantes ao longo do escoamento, não existindo razões para o seu estudo. Como foi descrito no item 12.4, a solução do escoamento implicará a solução do sistema formado pelas equações básicas. Neste item, essa aplicação será realizada num trecho infinitesimal ao longo de um conduto convergente ou divergente (Figura 13.18). Pela equação da continuidade (Equação 12.10) dA dv dρ =– – A vρ Da Equação 12.17:

dT dp ds = cp T – R p RT ou Tds = cp dT – p dp Mas como: RT 1 cpdT = dh e p = ρ então:

dp Tds = dh – ρ Como nesse caso o escoamento é isoentrópico, ds = 0, e obtém-se: dp dh = ρ A equação da energia para escoamento adiabático (Equação 12.15) é:

dh = –vdv Igualando as equações 12.53 e 12.54 tem-se:

dp dp dv ρ = –vdv ou ρv2 = – v Substituindo a Equação 12.55 na Equação 12.52, tem-se: dA dp dρ A = ρv2 – ρ ou dA A dp = ρv2 ⎜⎛1– v2 ⎝ dρ ⎞⎟ dp ⎠ Figura 12.18 (12.52)

(12.53) (12.54) (12.55)

<!-- p. 353 -->
C a p í t u l o 1 2 z Escoamento compressível z 353 mas, pela Equação 12.20, dp = c2 , logo: dρ dA A dp = ρv2 ⎛⎜1 – ⎝ v2 c2 ⎟⎞ ⎠ dA A = dp ρv 2 (1– M 2 ) (12.56)

A Equação 12.56 é a equação fundamental para o escoamento em estudo. Pela equação, verifica-se imediatamente que M = 1 é uma fronteira para uma modificação de comportamento do escoamento.

Assim, se M < 1, dA e dp têm o mesmo sinal, evidenciando que, se a área diminuir (convergente), a pressão deverá diminuir, mas se a área aumentar no sentido do escoamento (divergente), a pressão deverá aumentar. Por outro lado, se M > 1, (1 – M2) < 0, dA e dp terão sinais contrários, evidenciando que, no convergente, a pressão aumentará ao longo do escoamento, enquanto, no divergente, a pressão diminuirá.

Pela Equação 12.55, observa-se que dp e dv têm sempre sinais contrários, logo a variação da pressão e da velocidade ao longo dos escoamentos é sempre contrária, isto é, se p aumenta, v diminui e vice-versa, independentemente do número de Mach.

Por essa observação, conclui-se que, nos escoamentos subsônicos (M < 1) ao longo de um convergente, a pressão diminui e a velocidade aumenta, enquanto num divergente acontece o contrário.

Isso mostra que os escoamentos subsônicos têm um comportamento qualitativo semelhante ao dos fluidos incompressíveis, que na realidade são um caso particular de escoamento subsônico em que M < 0,2.

Já os escoamentos supersônicos têm um comportamento qualitativo bem distinto, já que, ao longo do convergente, a pressão aumenta e a velocidade diminui, acontecendo o contrário no escoamento ao longo do divergente.

Para o leitor habituado a firmar seu raciocínio na visualização do escoamento de líquidos, já que não se enxergam os gases, esse comportamento deve parecer bastante estranho. Entretanto, não se deve esquecer que, no caso de líquidos, não há variação de ρ e, pela equação da continuidade, ao longo do escoamento, vA = cte. Nos escoamentos supersônicos, a variação da densidade ao longo do escoamento é muito grande e a equação da continuidade ρvA = cte sofre uma influência muito acentuada do ρ. Dessa forma, mesmo que A diminua ao longo do escoamento, a densidade aumenta de tal forma que a velocidade terá de diminuir.

Se A aumentar, o ρ diminui de tal forma que a velocidade deverá aumentar.

A seguir, reúnem-se as equações necessárias à análise qualitativa da variação das propriedades ao longo do escoamento:

dA A = dp ρv 2 (1−M 2 ) (12.57)

dp dv ρv2 = – v (12.58) dp dp dh = ρ ou cp dT = ρ (12.53) c = kRT c2 = dp dρ dp ou dρ = c2 (12.22) (12.20)

<!-- p. 354 -->
M=v c (12.23)

As equações 12.53, 12.22 e 12.20 mostram que dp, dρ e dT têm o mesmo sinal dentro das hipóteses impostas e, portanto, p, ρ e T têm a mesma tendência de variação ao longo do escoamento e, como c é proporcional a T , a velocidade do som tem a mesma característica. Pela Equação 12.58, nota-se que dp e dv têm sinais contrários, o que permite concluir que p e v têm tendências opostas. Pode-se então concluir que, sempre que p aumenta, ao longo do escoamento, T, ρ e c irão aumentar e v diminuir e, portanto, M = v diminui. Ao contrário, sempre que p diminui, c T, ρ e c diminuem e v aumenta e, portanto, M = v aumenta.

c A Tabela 12.1 resume essas conclusões.

Propriedade A p v T ρ c M Caso M<1 ↓ ↓ ↑ ↓ ↓ ↓ ↑ M<1 ↑ ↑ ↓ ↑ ↑ ↑ ↓ M >1 ↓ ↑ ↓ ↑ ↑ ↑ ↓ M >1 ↑ ↓ ↑ ↓ ↓ ↓ ↑ Equação utilizada — 12.57 12.58 12.53 12.20 12.22 12.23 Tabela 12.1 Variação das propriedades ao longo do escoamento isoentrópico em conduto de seção variável (↑ aumenta, ↓ diminui). No caso em que M = 1, pela Equação 12.57, observa-se que dA = 0. Como por hipótese a área é variável, conclui-se que o escoamento sônico só pode acontecer ou numa seção de área máxima ou numa de área mínima. Será mostrado a seguir que, se existir M = 1, ele será possível somente na mínima seção de um bocal convergente.

a) M < 1 Verifica-se pela Tabela 12.1 que M diminui ao longo do escoamento e, portanto, não poderá atingir M = 1 na seção de saída, que é a máxima. b) M > 1 Verifica-se pela Tabela 12.1 que M aumenta ao longo do escoamento e, portanto, não poderá atingir M = 1 na seção de saída, que é a máxima. c) M < 1 Verifica-se pela Tabela 12.1 que M aumenta ao longo do escoamento e poderá atingir M = 1 na seção de saída, que é a mínima. d) M > 1 Verifica-se pela Tabela 12.1 que M diminui ao longo do escoamento e poderá atingir M = 1 na seção de saída, que é a mínima.

<!-- p. 355 -->
C a p í t u l o 1 2 z Escoamento compressível z 355 Chega-se assim a uma conclusão muito importante: Se existir M = 1 no escoamento, isso deverá acontecer na mínima seção de um bocal convergente (Figura 12.19). Figura 12.19 A Figura 12.20 mostra que, se o convergente continuar a partir da condição em que M = 1 na saída, esta deixará de ser a seção mínima e novamente o M = 1 se deslocará para a nova seção de saída, alterando-se toda a distribuição dos números de Mach a montante do escoamento. Figura 12.20 A partir da Equação 12.57, supondo que dA = 0 e, portanto, A = cte, conclui-se que, para M ≠ 1, obrigatoriamente dp = 0 e, portanto, p = cte. Mas, se p = cte, pelas outras equações conclui-se que todas as outras propriedades serão constantes ao longo do escoamento. Logo, ao considerar o escoamento isoentrópico, não tem sentido considerar o conduto de seção constante, pois todas as propriedades seriam idênticas ao longo do escoamento e não haveria o que estudar. Na prática, os escoamentos são irreversíveis por causa do atrito e, portanto, mesmo num conduto de seção constante haverá variação das propriedades. Isso permite fazer o estudo da variação das propriedades ao longo de um conduto de seção constante por um modelo matemático que considere ds ≠ 0, como se abordará mais adiante.

### 12.9.3 Estado crítico

Estado crítico é o estado que corresponde a M = 1. As propriedades do fluido correspondentes ao estado crítico serão representadas por um asterisco (p* T*, ρ*, A* etc.), denominando-se, respectivamente: pressão crítica, temperatura crítica, massa específica crítica, área crítica etc. Pelo que se disse no item anterior, se ao longo do escoamento existir o estado crítico, este corresponderá à mínima seção do escoamento; entretanto, a mínima seção não será obrigatoriamente a área crítica, pois não terá, necessariamente, atingido na mesma M = 1. Pelo exposto, mesmo que no escoamento não se tenha atingido M = 1, o estado crítico ainda pode ser definido e corresponderia a uma seção imaginária, em que, nas condições dadas, seria possível atingir M = 1 (Figura 12.21).

<!-- p. 356 -->
M=1 Seção crítica (p*, T*, A*,…)

M¹1 M=1 Seção crítica imaginária Figura 12.21

### 12.9.4 Estado de estagnação no escoamento isoentrópico

No escoamento isoentrópico não há troca de calor, nem perdas de energia por ser reversível. Não havendo máquina no trecho estudado, a energia total deverá se conservar ao longo do escoamento, isto é, todas as transformações de energia cinética em energia de pressão e térmica, ou vice-versa, serão perfeitamente reversíveis. Disso se conclui que o estado de estagnação é comum a todas as seções e será uma referência que permitirá relacionar os estados de todas as seções do escoamento (Figura 12.22). Figura 12.22 Se o conduto for alimentado por um reservatório de grandes dimensões, como neste v = 0, o estado do fluido será o de estagnação e se repetirá em todas as seções do escoamento. Figura 12.23 A Tabela 1 do Apêndice apresentada no item 12.7, que relaciona M , p , T , ρ , é de p0 T0 ρ0 grande utilidade para a solução de problemas de escoamento isoentrópico, pois, determinados T0, p0, ρ0 em qualquer ponto, estes servirão de referência para qualquer seção.

<!-- p. 357 -->
C a p í t u l o 1 2 z Escoamento compressível z 357 Um compressor alimenta um reservatório de grandes dimensões em que o ar mantém-se constantemente com uma pressão de 1 MPa (abs) e uma temperatura de 30o C. O ar escapa com uma vazão de 0,3 kg/s por um conduto convergente, sem trocas de calor e com atrito desprezível. Numa seção do conduto está instalado um manômetro que registra 0,6 MPa (abs). Determinar ρ, v, A e T nesta seção. Dados para o ar: k = 1,4; R = 287 m2/s2.K. Solução Com p = 6 = 0,6 sem efetuar interpolação, da Tabela 1 do Apêndice obtém-se M = 0,88 e T = 0,8659. p0 10 T0 Logo:

T = 0,8659 × T0 = 0,8659 × (30 + 273) = 262,4 K = –10,6oC Como: c = kRT então: v = M kRT Logo:

v = 0,88 1,4 × 287 × 262,4 = 286 m/s A massa específica pode ser obtida pela equação de estado:

p = RT ou ρ = p = 0,6 × 106 = 8 kg/m 3 ρ RT 287 × 262,4 Como: então:

Qm = ρAv A = Qm ρv A = 0,3 = 1,31 × 10–4 m 2 = 1,31 cm 2 8 × 286 12.10 Escoamento isoentrópico em conduto convergente a partir de um reservatório de grandes dimensões Para melhor compreender os fenômenos que acontecem ao longo do escoamento isoentrópico de um fluido por um conduto de seção variável, será discutido o que acontece quando se varia a pressão a jusante do conduto, de forma a simular todas as possibilidades (Figura 12.24). Figura 12.24 Suponha-se que a válvula de descarga permita ajustar a pressão de jusante (pj) no valor desejado e que o escoamento no bocal se estabeleça subsônico. Com essas premissas, analisa-se a variação da pressão ao longo do escoamento, quando se diminui pj desde p0 até zero.

<!-- p. 358 -->
p Para melhor ilustrar, a Figura 12.25 mostra o gráfico de = f (x), onde x é a coordenada p p0 do eixo do conduto e é a relação entre a pressão numa seção na coordenada x e a pressão p0 de estagnação que, como já foi visto, é constante ao longo de todo o escoamento. Figura 12.25 1) A pressão a jusante é igual a p0 e não haverá escoamento. A pressão coincide em todos os pontos com p0. 2) Sendo pj < p0, a diferença de pressão provoca o escoamento para jusante. Sendo o escoamento subsônico, ao longo do escoamento a pressão diminui e a velocidade aumenta. O p0 e o pj formam as condições de contorno do escoamento, de tal forma que a partícula que sai com p0 do reservatório de montante terá uma redução de pressão gradativa para que saia com ps = pj. Essa condição coincide com o que se disse para fluidos compressíveis, para os quais se verificou que o jato na saída tem a pressão do ambiente onde é descarregado. 3) Nessa condição, pj = p* e o escoamento se ajusta para que ps = pj = p*. Nessa situação, Ms = 1 e, pelo que foi visto anteriormente, essa seção é a crítica, sendo a condição limite do escoamento. Evidentemente, ao diminuir a pressão de jusante, a vazão em massa no bocal vai aumentando, de forma que: Qm(1) < Q m(2) < Q m(3) Como na saída, no máximo M = 1, essa seção passa a regular a vazão, independentemente da diminuição do pj. Atinge-se então, nessa situação, a máxima vazão em massa que pode escoar no sistema. A máxima vazão em massa denomina-se ‘vazão crítica’ e o bocal diz-se ‘bloqueado’. 4) ORmeijdtaeut.ozDidneesdsfoalupfiojdraombaqaiu,xaeovadateiznpãgo*e,eopmbs s=merpav*sasn-aasmeseqaçunãetoépmdsem-sseaaniígdtuéamaslo-àsferceriígrtáuicuaalmpaaaprea*,xqjpáuaqanulqseãuMoersb=pruj1<sécpao*.nlioreservatório de jusante para se adaptar à pressão dele. Lembre que expansões bruscas são irreversíveis e, portanto, o escoamento da seção de saída para o reservatório de jusante não é isoentrópico (Figura 12.26). Figura 12.26

<!-- p. 359 -->
C a p í t u l o 1 2 z Escoamento compressível z 359 Verifica-se a seguir que a velocidade crítica (v*), ou a máxima velocidade que pode ser atingida no bocal convergente, é função somente das condições de estagnação. Isto é, dado o estado de estagnação, a máxima velocidade que pode ser atingida num bocal convergente com escoamento subsônico já está predestinada. Da Equação 12.31, relacionando o estado do fluido numa seção com o estado de estagnação: v2 2 +h =h0 v2 ou 2 + cpT = cpT0 v2 kRT + = kRT 0 2 k –1 k –1 ou v2 c2 + = kRT0 2 k –1 k –1 Aplicando essa expressão na seção crítica, onde v* = c:

v*2 ⎛⎜⎝ 1 2 + k 1 – 1⎠⎟⎞ = kRT 0 k –1 ou v*2 k +1 = kRT0 2(k –1) k –1 Finalmente:

v* = 2kRT0 k +1 (12.59)

A Equação 12.59 mostra que, dado um fluido e o estado de estagnação, ou o estado do reservatório de montante, a velocidade crítica fica prefixada e, como se sabe, acontecerá na mínima seção do bocal, que passa a ser a seção crítica. Seja a vazão em massa numa seção qualquer do escoamento:

Qm = ρvA p = RT vA Multiplicando e dividindo por p0, por T0 e rearranjando:

p Qm = p0 p0 v kRT kT 0 RT A T0 Lembrando que v = M e pelas equações 12.32 e 12.33: kRT Qm = ⎜⎛⎝1 + k −1M 2 2 ⎞⎠⎟ − K K– 1 p0 M k R ⎝⎛⎜1 + k –1 2 M 2 ⎠⎞⎟ A T0 ou Qm = k RT 0 p0 A M ⎜⎝⎛1+ k –1M 2 2 ⎠⎞⎟ – k+1 2(k– 1) (12.60) Essa expressão é válida para qualquer seção e qualquer situação. Na seção mínima do convergente, quando o escoamento está bloqueado, tem-se: A = A*, M = 1 e Qm = Qmc = Qmáx , então:

<!-- p. 360 -->
k +1 Qmc = k RT 0 p0 A* ⎛⎝⎜1 + k – 2 1⎠⎟⎞ – 2(k –1) (12.61)

Dividindo a Equação 12.60 pela Equação 12.61, obtém-se:

k +1 Qm Qmc = A A* M ⎜⎛1 ⎜ + k– 2 1 M ⎜ ⎝ k –1 1+ 2 2 ⎟⎞ ⎟ ⎟ ⎠ – 2(k –1) (12.62) A Equação 12.62 permite obter a relação entre a vazão do fluido numa situação qualquer e a vazão crítica ou máxima do bocal. Por outro lado, também pode ser interpretada como a relação da vazão numa seção qualquer do conduto e a vazão na seção crítica. Nesse caso, pela equação da continuidade, Qm =1; logo: Qmc k +1 A A* 1 = M ⎛⎜ 1 + ⎜ k –1M 2 2 ⎟⎞ ⎟ 2(k –1) ⎜ ⎝ k –1 1+ 2 ⎟ ⎠ (12.63)

A Tabela 1 do Apêndice mostra os valores de A A* = f(M ) para k = 1,4.

Lançando os valores dessa função num gráfico, obtém-se o diagrama qualitativo da Figura 12.27. Figura 12.27 O que se nota do diagrama é que, para cada seção do escoamento isoentrópico num conduto de seção variável, existem duas e apenas duas soluções possíveis, uma subsônica e outra supersônica.

O mesmo estudo em que foram deduzidas as equações 12.62 e 12.63, onde Qm Qmc A e A* fop ram obtidos em função do número de Mach, pode ser efetuado em função de , e as equap0 ções resultantes são:

<!-- p. 361 -->
C a p í t u l o 1 2 z Escoamento compressível z 361 1 1 1 k –1 Qm Qmc = A A* ⎜⎛⎝ k k +– 11⎠⎟⎞ 2 ⎝⎛⎜ k2+1⎠⎟⎞ k –1 ⎛⎜ ⎝ p p0 ⎟⎞ ⎠ k 1– ⎛⎜ p ⎟⎞ k ⎝ p0 ⎠ 1 1 1 k –1 A* A = ⎛⎝⎜ k k –+11⎠⎞⎟ 2 ⎛⎜⎝ k2+1⎟⎠⎞ k –1 ⎜⎛ ⎝ p p0 ⎟⎞ ⎠ k 1– ⎛⎜ p ⎞⎟ k ⎝ p0 ⎠ (12.64) (12.65)

Na mesma seção, a relação entre a vazão em massa que escoa e a vazão em massa crítica A é obtida adotando-se A* =1 na Equação 12.64, resultando em:

1 1 1 k –1 Qm Qmc = ⎝⎜⎛ k k –+11⎟⎠⎞ 2 ⎝⎜⎛ k2+1⎟⎠⎞ k –1 ⎜⎛ ⎝ p p0 ⎞⎟ ⎠ k 1– ⎜⎛ p ⎟⎞ k ⎝ p0 ⎠ (12.66)

## 12.11 Escoamento isoentrópico em conduto convergente/divergente a

partir de um reservatório de grandes dimensões Da mesma forma que no item 12.10, supõe-se o conduto ligado a dois reservatórios, um a montante, com suas propriedades constantes, e outro a jusante em que se pode variar a pressão desde p0 até zero. Na Figura 12.28, é mostrado o diagrama da variação da pressão ao longo do convergente/divergente para as diversas pressões a jusante. Figura 12.28 1) 2)

Quando pj = p0, não há escoamento no conduto. Quando pj < p0, processa-se o escoamento. Se pG > p*, o escoamento mantém-se subsônico ao longo de todo o conduto. No convergente, a velocidade aumenta e, portanto, a pressão diminui. Ao longo do divergente, a velocidade diminui e a pressão aumenta até alcançar ps = pj. A distribuição das pressões é tal que, ao longo do conduto, ajusta-se às condições de contorno, que são, respectivamente, p0 a 3)

montante e pj a jusante. e 4) Nessas condições, pj é tal que, na garganta, atinge-se p*, isto é, AG = A*.

<!-- p. 362 -->
Nessa condição, já foi visto que o bocal convergente fica bloqueado e ulteriores reduções da pressão a jusante não provocam mais o aumento da vazão em massa, nem variações nenhuma ao longo variação do no convergente. Assim, qualquer que seja bocal convergente, estabelecendo-se na gpaj r≤gpa'nj ,tnaãpo* se notará e M = 1.

O bocal divergente fica, então, sujeito a uma entrada fixa e a uma saída variável. Foi visto anteriormente que, se na seção mínima de um bocal M = 1, em cada seção do bocal existirão duas e apenas duas soluções isoentrópicas, uma subsônica e outra supersônica (Figura 12.27).

Se a jusante for fixado pj = p ' j , o escoamento se processará subsonicamente, de forma que a velocidade no divergente irá diminuir e a pressão irá aumentar até ps = p ' j na saída. Essa é a denominada primeira solução isoentrópica (caso (3) da Figura 12.28). Se a jusante for fixado pj = p '' j , o escoamento se processará supersonicamente e no divergente a velocidade aumentará, enquanto a pressão diminuirá até atingir ps = p '' j na saída (segunda solução isoentrópica, caso (4) da Figura 12.28).

Para qualquer pj < p ' j e pj ≠ p '' j , a jusante da garganta acontecerão fenômenos não-isoentrópicos, tais como ondas de choque e expansões bruscas. Estes são irreversíveis e não podem ser previstos pelo modelo matemático aqui estabelecido. Serão estudados em itens posteriores, com as hipóteses e o tratamento adequado.

Num reservatório de grandes dimensões, está armazenado ar ⎝⎛⎜ k = 1,4, R = 287 m2 s2K ⎟⎠⎞ , à pressão de 1 MPa (abs) e à temperatura de 300 K. Para a descarga do ar, é instalado um bocal convergente/divergente, com área de saída de 20 cm2 e área da garganta de 10 cm2. a) A partir de que pressão a jusante a vazão em massa será máxima? b) Qual seria a outra pressão a jusante que produziria um escoamento totalmente isoentrópico com M = 1 na garganta? c) Qual é a vazão em massa máxima? Resolver o problema sem interpolar na tabela.

Solução a) Como a vazão é máxima, AG = A* ⎧M s = 0,3 As AG = A* =2 ⇒ ⎪ ps ⎪⎪ ⎨ ⎪ p0 Ts = 0,9395 ⇒ = 0,9823 ps = 0,9395 × 1= 0,94 Mpa (abs) ⎪ T0 ⎩⎪Logo: pj = 0,94 MPa (abs)

b) A segunda solução isoentrópica será:

⎧M s = 2,2 As AG =2⇒ ⎪ ps ⎪⎪ ⎨ ⎪ p0 Ts = 0,9352 ⇒ = 0,5081 ps = 0,9352 × 1 ⎪ T0 ⎪⎩Logo: pj = 0,94 MPa (abs)

<!-- p. 363 -->
C a p í t u l o 1 2 z Escoamento compressível z 363 c) Qm = ρs vs As Ts = 0,9823 × 300 = 294,7 K ρs = ps RTs = 0,94 × 106 287 × 294,7 = 11,11 kg/m 3 vs = M s kRTs = 0,3 1,4 × 287 × 294,7 = 103,2 m/s Logo: Q'm = 11,11× 103,2 × 20 × 10–4 = 2,29 kg/s ou, na segunda solução isoentrópica:

Ts = 0,5081× 300 = 152,4 K ρs = ps RTs = 0,094 × 106 287 × 152,4 = 2,15 kg/m 3 vs = M s kRTs = 2,2 1,4 × 287 × 152,4 = 544,4 m/s Logo: Q'm' = 2,15 × 544,4 × 20 × 10–4 = 2,34 kg/s Obviamente, Q'm = Qm'' = Qmc , já que nas duas situações o bocal está bloqueado. A discrepância numérica deve-se à imprecisão causada pela falta de interpolação na tabela.

## 12.12 Onda de choque normal

No item 12.11, verificou-se que, para um conduto convergente/divergente, ao se atingir M = 1 na garganta, no divergente só podem existir duas soluções isoentrópicas, uma subsônica e outra supersônica. Essas soluções acontecerão para duas pressões específicas a jusante, que foram simbolizadas por p ' j e p '' j . Para outras pressões de saída entre essas duas, irá acontecer no divergente um fenômeno irreversível denominado onda de choque e que representa uma variação brusca das propriedades ao longo do escoamento.

Essa descontinuidade é causada basicamente pela incompatibilidade das condições de contorno com a possibilidade de um escoamento isoentrópico ao longo do conduto. Lembrar que, ao se atingir M = 1 na garganta, o divergente será alimentado pelo fluido no estado crítico, de forma que é razoável que não seja qualquer pressão de jusante compatível com o escoamento contínuo descontinuidade do no fluido. Assim, escoamento do para pressões divergente, na a jusante entre p ' j e p '' j qual, numa espessura será observada uma de 10–7m, as propriedades do fluido sofrerão uma variação muito brusca para se adaptar às condições energéticas estabelecidas pelo reservatório a jusante.

Pode-se, então, concluir que a onda de choque acontecerá sempre que as condições do fluido, numa certa seção, não forem compatíveis com as condições de contorno.

Ondas de choque podem ser observadas, por exemplo, no movimento supersônico de um avião. Nesse caso, o avião atinge o ar em repouso sem aviso prévio, já que as ondas de propagação da perturbação ficam para trás, não preparando o meio para o impacto da superfície sólida. Combustões excessivamente rápidas também causam um acúmulo de pressão, gerando a propagação de ondas de choque no meio. Tem-se como exemplos a explosão de bombas e a combustão excessivamente rápida da mistura na câmara de um motor de combustão interna, que origina o fenômeno denominado detonação, provocando a propagação de ondas de choque, cujo ruído característico é denominado popularmente de ‘batidas de pino’.

Pelos exemplos apresentados, a onda de choque, em geral, é um fenômeno indesejado, mas, às vezes, o brusco aumento da pressão na frente de onda pode ser utilizado em aplicações interessantes. Como exemplos, podem ser citados a introdução de gases em líquidos, a fabricação de espumas sólidas (polimerização), a calibração de transdutores de pressão em tubos de choque e outros.

<!-- p. 364 -->
Neste item, serão estudadas apenas ondas de choque estacionárias em condutos, e estas serão normais às linhas de corrente do escoamento, embora o estudo de ondas oblíquas siga os mesmos conceitos, envolvendo apenas maiores complicações algébricas no equacionamento. Além disso, apesar de a espessura das ondas de choque não ser nula, mas da ordem de grandeza do livre caminho médio das moléculas, por ser muito pequena, será tratada como uma descontinuidade matemática, na qual as propriedades do fluido variam sensivelmente através de uma seção. Nesta, as partículas do fluido em alta velocidade irão se chocar com as de baixa velocidade a jusante, dando origem a um fenômeno irreversível, com conseqüente aumento da entropia, o que não permite o estudo pelas hipóteses do escoamento isoentrópico.

### 12.12.1 Equacionamento matemático da onda de choque

Como já foi dito, o modelo matemático desse fenômeno corresponde à adoção de uma descontinuidade matemática das propriedades do fluido numa seção do escoamento (Figura 12.29). Figura 12.29 O tubo de corrente para a aplicação das equações básicas constitui-se de uma seção de entrada x e uma de saída y, diferenciadas pelas propriedades do fluido, já que geometricamente correspondem à mesma seção, tendo em vista que distam de uma espessura nula. A ausência de área lateral do tubo de corrente implica a impossibilidade de troca de calor com o meio, de forma que o fenômeno será considerado adiabático e irreversível, resultando obrigatoriamente num aumento da entropia do fluido entre as seções x e y (sy sx). Esse aumento de entropia é o sinal da existência de uma perda de energia que resultará numa alteração irremediável das condições de estagnação, em particular da pressão desse estado, já que a temperatura de estagnação se manterá constante devido ao caráter adiabático do escoamento. A seguir, serão aplicadas as equações básicas ao modelo adotado.

Equação da continuidade mas como Ax = Ay, então:

ρxvxAx =ρyvyAy ρxvx =ρyvy ou ρx = vy ρy vx (12.67)

Equação da energia (q = 0)

v 2 x 2 +hx = v 2 y 2 +hy ou v 2 x 2 + cpTx = v 2 y 2 + cpTy (12.68)

Na Equação 12.68, fazendo-se vx = 0, Tx = T0x e vy = 0, Ty = T0y , conclui-se que: T0x = T0y (12.69)

<!-- p. 365 -->
C a p í t u l o 1 2 z Escoamento compressível z 365 p Por outro lado, como ρ = RT, então, pela Equação 12.69:

p0x = p0y ρ0x ρ0y (12.70)

Equação da quantidade de movimento Pelo fato de a espessura da onda de choque ser nula, Fsx = 0; pela falta de área lateral, a equação reduz-se a:

e, portanto: Mas (px – py ) A +Qm(vx – vy ) =0 ou px – py + ρ x v 2 x – ρ y v 2 y =0 px + ρ x v 2 x = py + ρ y v 2 y T0 = 1+ k –1M 2 T 2 (12.71) Logo: Ty Tx = 1+ 1+ k –1 2 k –1 M M 2 x 2 y 2 (12.72)

Equação de estado Ty = py ρx Tx px ρy Substituindo na Equação 12.67, obtém-se:

Logo:

Ty = p y v y = p y cy M y = p y M y kRTy Tx p x v x p x cx M x p x M x kRTx Ty = py My Tx px Mx Ty ou Ty = ⎛⎜ py ⎞⎟ 2 ⎛⎜ M y ⎟⎞ 2 Tx Tx ⎝ px ⎠ ⎝MX ⎠ Igualando a Equação 12.72 com a Equação 12.73:

Mas py = Mx px My 1 + k– 2 1 M 2 y 1 + k +1 2 M 2 x c2 p =k ρ p =k ρ v2 v2 logo ρv2 = kpM 2 (12.73) (12.74)

Logo, a Equação 12.71 resulta em:

Portanto: px + kp xM 2 x = py + kp y M 2 y ou p x (1 + kM 2 x ) = p y (1 + kM 2 y ) py px = 1 1 + + kM kM 2 x 2 y (12.75)

<!-- p. 366 -->
Igualando as equações 12.74 e 12.75, tem-se:

My Mx 1+ k– 2 1 M 2 x 1+ k– 2 1 M 2 y = 1 1 + + k k M M 2 x 2 y Elevando ao quadrado ambos os membros e resolvendo a equação supondo My como incógnita, chega-se às soluções: M x =My My = M 2 x + 2 k –1 2k k –1 M 2 x –1 (12.76)

A primeira é a solução trivial, isto é, a inexistência da onda de choque. A segunda solução da Equação 12.75, resolvida para valores numéricos de Mx, mostra que, para valores deste maiores que 1, os valores de My são menores que 1, e vice-versa, o que denota a existência da descontinuidade. Pela equação de estado:

ρy = py Tx ρx px Ty e pelas equações 12.72 e 12.74, obtém-se:

Da Equação 12.70:

ρy = Mx ρx My 1+ k– 2 1 M 2 y 1+ k– 2 1 M 2 x = vx vy p0y = ρ0x = ρ0x ρx ρy p0x ρ0y ρx ρy ρ0y (12.77)

e pelas equações 12.35 e 12.77, obtém-se:

1 p0y p0x = Mx My ⎝⎛⎜1 + k –1M 2 2 x ⎟⎠⎞ k –1 1 ⎛⎝⎜1 + k– 2 1 M 2 y ⎞⎠⎟ 2 1 ⎛⎝⎜1 + k– 2 1 M 2 x ⎞⎠⎟ 2 1 ⎝⎜⎛1 + k– 2 1 M 2 y ⎟⎠⎞ k –1 k +1 ou p0y p0x M y ⎛⎝⎜1 + k– 2 1 M 2 x ⎞⎟⎠ 2(k –1) = k +1 M x ⎜⎝⎛1 + k– 2 1 M 2 y ⎟⎞⎠ 2(k –1)

<!-- p. 367 -->
C a p í t u l o 1 2 z Escoamento compressível z 367 Substituindo o valor de My obtido da Equação 12.76, chega-se a:

k p0y p0x = ⎜⎛ ⎜ k +1 2 M 2 x ⎝⎜ 1 + k– 2 1 M 2 x ⎟⎞ ⎟ ⎟ ⎠ k –1 1 ⎜⎛⎝ 2k k +1 M 2 x – k k +– 11⎠⎟⎞ 1– k (12.78) A irreversibilidade da onda de choque é medida pela variação da entropia. Como através da onda de choque o escoamento é adiabático, obrigatoriamente sy > sx. Pela Equação 12.17, pode-se obter: s y – s x = cp ln Ty /Tx k –1 (py/px ) k mas: T0 = k –12 1+ M2 T 2 k e p0 p = ⎜⎛⎝1 + k – 2 1 M 2 ⎠⎞⎟ k– 1 de forma que: e Ty = T0y ⎛⎝⎜ 1+ k –1 2 M 2 x ⎞⎠⎟ Tx T0x ⎜⎝⎛1 + k –1 2 M 2 y ⎠⎟⎞ k py px = p0y p0x ⎛⎜⎝1 + k– 2 1 M 2 x ⎠⎟⎞ k -1 k ⎛⎜⎝1 + k– 2 1 M 2 y ⎟⎠⎞ k -1 Logo: e, portanto:

Ty Tx k -1 ⎜⎛ py ⎞⎟ k ⎝ px ⎠ T0y T0x = k -1 ⎜⎝⎛⎜ p0y p0x ⎟⎞⎟⎠ k ⎜⎛ 1 + ⎜ k– 2 1 M 2 x ⎟⎞ ⎟ ⎜ ⎝ 1+ k– 2 1 M 2 y ⎟ ⎠ ⎛⎜ 1 + ⎜ k– 2 1 M 2 x ⎟⎞ ⎟ k ⋅ k -1 k -1 k ⎜ ⎝ 1+ k– 2 1 M 2 y ⎟ ⎠ T0y = T0x k -1 ⎛⎜⎜⎝ p0y p0x ⎠⎟⎞⎟ k s y – s x = cp ln T0y/ T0x k –1 (p0y/ p0x ) k

<!-- p. 368 -->
mas como T0y = T0x , então:

sy – sx = cp ln 1 k –1 ⎜⎜⎝⎛ p0y p0x ⎟⎞⎟⎠ k = –cp k –1 ln p0y k p0x ou sy – sx = –R ln p0y p0x = Rln p 0x p0y Logo:

Δs = R ln p0x p0y ou p0x Δs =eR p0y (12.79) (12.80)

A Equação 12.79 é o valor da irreversibilidade do fenômeno e, pela Equação 12.80, como Δs é positivo, nota-se perfeitamente que p 0x < p 0y e que a onda de choque causa uma perda de pressão de estagnação no escoamento, isto é:

p 0y<p 0x Pela Equação 12.78, pode-se obter também:

(12.81) Δs R = k k – 1 ⎡ ⎣⎢ ln ⎛⎝⎜ k +1 2 M 2 x ⎞⎟⎠ ln ⎛⎝⎜1 + k– 2 1 M 2 x ⎞⎠⎟ ⎤ ⎦⎥ + + 1 k –1 ln ⎜⎝⎛ 2k k +1 M 2 x – k k +– 11⎟⎞⎠ (12.82) Fixado o valor do k e dando gráfico resulta, qualitativamente, valores a Mx, obtém-se na Figura 12.30.

uma tabela de Δs R , que lançada num Figura 12.30 Verifica-se, então, a possibilidade de obter ondas de choque para Mx < 1, pois Δs < 0. Logo, ondas de choque só podem acontecer em escoamentos supersônicos e, através da onda de choque, o escoamento passará bruscamente para subsônico, conforme se pode concluir pela observação da segunda solução da Equação 12.76. Após essas conclusões, pode-se explicar fisicamente a existência dessa descontinuidade (Figura 12.31).

<!-- p. 369 -->
C a p í t u l o 1 2 z Escoamento compressível z 369 Figura 12.31 Seja um escoamento que a montante tenha condições supersônicas. Se a jusante as condições de contorno forem tais que ele tenha de assumir um escoamento subsônico, as partículas rápidas a montante em alguma seção encontrarão as lentas do escoamento subsônico, provocando um choque na interface. Esse choque provocará uma redução brusca da velocidade, com um conseqüente aumento da pressão, temperatura e densidade do fluido. Como a pressão aumenta e a velocidade diminui, nada se pode concluir sobre a pressão de estagnação; entretanto, como o fenômeno é irreversível, Δs > 0, logo p0y < p0x , sendo que Δp0 representará a perda de energia útil do sistema. Para um dado gás (k = cte):

A Equação 12.76 é do tipo My = f (Mx)

A Equação 12.74 é do tipo py px = f (M x , M y )

A Equação 12.77 é do tipo ρ ρ y x = f (M x , M y )

A Equação 12.72 é do tipo Ty Tx = f (M x , M y )

A Equação 12.78 é do tipo p0y p0x = f (M x )

A Equação 12.82 é do tipo Δs = f (M x )

De forma que, dados os valores a Mx > 1, é possível obter os valores numéricos de: My < 1, py > 1, ρ y > 1, Ty > 1, p0y < 1, Δs > 0 que, lançados na Tabela 2 do Apêndice, permitem relaciopx ρx Tx p0x nar todas as propriedades através da onda de choque normal.

A intensidade da onda de choque é representada pelo valor da relação py dada pela Equação 12.74; logo:

px Int OC = py px = 1 1 + + kM kM 2 x 2 y

### 12.12.2 Interpretação gráfica da onda de choque

Do item 12.12.1, pode-se observar que as equações básicas utilizadas foram: Equação da continuidade Qm = cte ou ρ x vx = ρ y vy pois A x = A y que é do tipo f1(ρ, v) = 0 (12.83) (12. 84)

<!-- p. 370 -->
Equação da energia v 2 x 2 + cpTx = v 2 y 2 + cpTy pois q = 0 que é do tipo f 2 ( v, T ) = 0 (12.85)

Equação da quantidade de movimento px + ρ x v 2 x = py + ρ y v 2 y pois FSx = 0 que é do tipo f 3( p, ρ, v) = 0 Equação de estado px ρy = Tx py ρx Ty que é do tipo f 4( p, ρ, T ) = 0 (12.86) (12.87)

Equação da entropia s y – s x = cp ln Ty/Tx k –1 ⎛⎜ py ⎟⎞ k ⎝ px ⎠ que é do tipo f 5( s, p, T ) = 0 (12.88)

Adotando como conhecidas as propriedades em uma das duas seções, x ou y, esse conjunto forma um sistema de cinco equações a cinco incógnitas: ρ, v, T, p e s. Adotando as equações:

(1) f1(ρ, v) = 0 (2) f 2 ( v, T ) = 0 (4) f 4( p, ρ, T ) = 0 (5) f 5( s, T, p) = 0 o sistema fica com quatro equações, com cinco incógnitas e, portanto, indeterminado. Adotando um valor de v na (1), obtém-se ρ e, na (2), T. Da (4), com p e T, obtém-se p, que, substituído na (5), permite obter s. Repetindo esse processo para todos os valores de v, obtém-se o conjunto de valores de v, ρ, T, p, s válidos para as quatro equações escolhidas, que admitem: Qm = cte, A = cte, q = 0 e s > 0, ou seja, um escoamento em conduto de seção constante, sem troca de calor, mas com s > 0 e, portanto, irreversível (por exemplo, com atrito). O conjunto de valores de s = f (T) assim obtido representaria os estados de um escoamento adiabático com atrito em conduto de seção constante. A linha s = f (T) denomina-se linha de Fanno, que, para uma vazão em massa qualquer, teria o aspecto qualitativo da Figura 12.32. Figura 12.32

<!-- p. 371 -->
C a p í t u l o 1 2 z Escoamento compressível z 371 O que se pode verificar, pelos valores numéricos obtidos pelo processo indicado, é que a máxima entropia corresponde a M = 1, o ramo superior corresponde aos estados de um escoamento subsônico, e o inferior, aos de um escoamento supersônico. Como o escoamento é irreversível e adiabático, os estados ao longo do escoamento só podem ser percorridos no sentido das entropias crescentes, isto é, no sentido indicado na Figura 12.32. Se forem adotadas as equações: (1) f1(ρ, v) = 0 (3) f 3( p, ρ, v) = 0 (4) f 4(ρ, p, T ) = 0 (5) f 5( s, p, T ) = 0 pelo mesmo procedimento descrito anteriormente, adota-se v na (1) e obtém-se ρ. Com ρ e v na (3), obtém-se p e, com ρ e p na (4), obtém-se T. Finalmente, com T e p na (5), obtém-se s. Nesse caso, pela equação (3), em que FSx = 0, supõe-se que não haja atrito; entretanto, pela equação (5), a existência de uma variação de s sugere a existência de trocas de calor ao longo do escoamento. Logo, esse conjunto de valores representa os estados possíveis de um escoamento ao longo de um conduto de seção constante, sem atrito, mas com trocas de calor. A linha s = f (T) nesse caso denomina-se linha de Rayleight e, para uma certa vazão, num diagrama T-s, terá o aspecto qualitativo mostrado na Figura 12.33. Figura 12.33 O que se pode verificar, pelos valores numéricos obtidos pelo procedimento descrito, é que, novamente, a máxima entropia corresponde a M = 1, o ramo superior corresponde a um escoamento subsônico, e o inferior, a um supersônico. A diferença em relação ao caso anterior é que, como nesse escoamento existe troca de calor, mas não há atrito, a entropia pode ser crescente ou decrescente ao longo do escoamento, dependendo se o calor é fornecido ao fluido ou dele retirado. A superposição dos gráficos para uma dada vazão corresponde à solução do sistema de cinco equações que descrevem a onda de choque (Figura 12.34). O que se nota é que as linhas se cruzam em dois pontos, um correspondente ao estado x e outro ao estado y, respectivamente, a montante e a jusante da onda de choque, como foi descrito anteriormente.

<!-- p. 372 -->
372 z Mecânica dos Fluidos T y Ty Tx x sx sy s Figura 12.34 Como a onda de choque provoca um aumento de entropia entre a entrada e a saída, o ponto x será o de menor entropia, localizado no ramo supersônico, e o ponto y será o de maior entropia, localizado no ramo subsônico. Conclui-se, como já havia sido obtido algebricamente, que a onda de choque é um fenômeno que pode acontecer em escoamentos supersônicos e que, através da onda de choque, o escoamento passa para subsônico. Além disso, corresponde a uma descontinuidade em que T cresce e, portanto, p e ρ crescem e v diminui bruscamente. Acredita-se que essa abordagem gráfica seja mais facilmente compreendida pelo leitor; entretanto, a abordagem algébrica é de utilidade para o estabelecimento quantitativo das variações das propriedades através da onda. montante p0 AG T0 v=0 p p0 1,0 p* p0 As jusante pj variável ps = pj = p0 ps = pj < p0 ps = pj' < p0 (1) (2) (3) ps = pN < p0 (4)

ps = p'j' < p0 (5) (6)

(7) x Figura 12.35

<!-- p. 373 -->
C a p í t u l o 1 2 z Escoamento compressível z 373

### 12.12.3 Complementação do estudo do escoamento ao longo de um bocal

convergente/divergente No item 12.11, verificou-se que o escoamento ao longo de um conduto convergente/divergente não tinha solução para certas pressões a jusante com as hipóteses do escoamento isoentrópico.

Com o conhecimento da onda de choque, o estudo pode ser completado e é representado na Figura 12.35.

1) p0 > pj > p ' j → Escoamento subsônico ao longo de todo o bocal. Ao diminuir pj, a vazão em massa vai aumentando.

2) pj = p ' j → pG = p* e M G = 1.

O escoamento torna-se bloqueado e é subsônico ao longo de todo o bocal.

3) p ' j > pj > pN → O escoamento passa por M = 1 na garganta e tende a adotar a solução supersônica no divergente. Entretanto, essa solução, que é compatível com p"j na saída, não é válida para pressões maiores. O escoamento mantém-se supersônico ao longo de um certo trecho do divergente e em alguma seção aparece uma onda de choque passando para subsônico, que é o escoamento compatível com a pressão de saída. Ao reduzir pj, a onda de choque vai caminhando para a seção de saída. 4) pj = pN → A onda de choque se estabelece exatamente na seção de saída. 5) pN > p j > p"j → Nessas pressões, a onda de choque normal vai sendo succionada para o ambiente de jusante, formando uma onda de choque oblíqua já no reservatório. Conforme pj vai diminuindo, a onda de choque vai sendo succionada cada vez mais para o reservatório, mantendo-se colada no conduto (Figura 12.36). ps = pN ps diminuindo e tendendo a p'j' Onda de choque oblíqua Figura 12.36 6) p j = p"j → A onda de choque é succionada para o infinito e desaparece, obtendo-se a segunda solução isoentrópica, com escoamento supersônico em todo o divergente e sem ondas de choque.

7) p j < p"j → O escoamento chega até a saída com ps < p"j , desembocando com pressão maior que a do ambiente. O reajustamento é feito por uma expansão brusca, não-isoentrópica, no reservatório de jusante.

O que deve ser ressaltado em relação ao escoamento de fluidos incompressíveis é a possibilidade de a pressão na seção de saída ser diferente daquela do ambiente.

A solução de problemas envolvendo bocais convergentes/divergentes ocorre supondo-se o escoamento isoentrópico até a seção da onda de choque (se existir). Ao atravessar a onda de choque, a solução envolve uma variação brusca das propriedades, que pode ser obtida pela Tabela 2 do Apêndice. Da onda de choque em diante, considera-se, novamente, um escoamento isoentrópico, mas com um novo estado de estagnação, pois, apesar de qcThu0oyeq,=upTeel0aaxl,tEpeqr0ayu-a<sçepã, 0oexx,1io2st.q6in4ud,eoAaa*ltoe=rlfao(nopgu0o)t.rdaCosopemsrcoooppar0miyeed≠naptdo0exA,s dax* e=ssesAçeãGoesectarAídt*yioc.aaNjauosjtuaens-sateen,tdepaodoranedoxnaem,ddapifldeoe-, rente de A * x e imaginária.

<!-- p. 374 -->
1. Dado o bocal convergente/divergente da figura, determinar o intervalo de pressões a jusante para ter: a) escoamento totalmente isoentrópico interna e externamente ao bocal; b) ondas de choque oblíquas na saída; c) jato com expansão na saída; d) onda de choque normal no divergente; Dados: AG = 74,6 cm2; As = 100 cm2; p0 = 1,5 MPa (abs); k = 1,4; R = 287 m2/s2K. Resolver com as Tabelas do Apêndice, sem interpolações. Solução As condições desejadas são exatamente as descritas pela teoria. Os intervalos são estabelecidos pela determinação de p'j , p N e pj'', como mostra a figura. Com As = 100 = 1,34 da Tabela1 do Apêndice, obtêm-se as duas soluções isoentrópicas, a subsônica e a suA* 74,6 persônica. M ' s = 0,5 ps' p0 = 0,8430 ⇒ p ' s = 0,8430 × 1,5 = 1,264 MPa (abs) = pj' M '' s = 1,7 p '' s p0 = 0,2026 ⇒ ps'' = 0,2026 × 1,5 = 0,304 MPa (abs) = p '' j A pressão pN é obtida supondo que o escoamento vá até a saída pela segunda solução isoentrópica, de forma que px = p '' j e pN = py. Logo, pela Tabela 2 do Apêndice, para onda de choque, como M '' s = M x = 1,7, então: py px = 3,205 → py = 3,205 × 0,304 = 0,974 MPa (abs) Assim, as respostas às questões propostas em MPa (abs) são:

a) 1,5 > pj ≥ 1,264 e pj = 0,304

<!-- p. 375 -->
C a p í t u l o 1 2 z Escoamento compressível z 375 b) 0,974 > pj > 0,304 c) 0,304 > pj ≥ 0 d) 1,264 > pj > 0,974 2. A temperatura e a pressão do ar de um reservatório que alimenta um convergente/divergente são, respectivamente, 444 K e 0,41 MPa (abs). A área da garganta é 6,25 cm2 e a de saída é 18,75 cm2. Nota-se uma onda de choque no divergente numa seção de área 12,5 cm2. a) Quais são os valores da pressão, temperatura e velocidade na seção de saída? b) Qual é o máximo valor da pressão de jusante que causa um escoamento totalmente supersônico no divergente? Solução a) O fato importante na solução deste exercício é que A* muda de montante para jusante da onda de choque, por causa da variação do estado de estagnação. Com Ac A* = 12,5 6,25 = 2 ⎯⎯Tabe⎯la 1⎯(A⎯pênd⎯i⎯ce)→ M X = 2,2 Apesar de existirem duas soluções para essa relação de áreas, a que interessa é a supersônica, por haver onda de choque. Com e Mx = 2,2 ⎯⎯Tabe⎯la 2⎯(A⎯pênd⎯i⎯ce)→ M y = 0,5471 p0y p0x = 0,6281→ p0y = 0,6281× 0,41 = 0,258 MPa (abs)

Assim, foi possível atravessar a onda de choque e determinar as propriedades a jusante. A partir da seção imediatamente a jusante, o escoamento é novamente isoentrópico, mas a partir da seção y haverá uma nova pressão de estagnação e uma nova área crítica de referência. Com My = 0,5471⎯⎯Tabe⎯la 1⎯(A⎯pênd⎯i⎯ce)→ Ac A * y = 1,27 → A * y = 12,5 1,27 = 9,84 cm 2 A relação entre a área de saída e a nova seção crítica é:

As A * y = 18,75 9,84 = 1,905 ⎯⎯Tab⎯ela 1⎯(Ap⎯ênd⎯i⎯ce)→ Ms = 0,32 ps = 0,9315 e p0y Ts = 0,9799 T0 Note-se que foi selecionada a solução subsônica, já que a jusante da onda de choque o escoamento é subsônico e também T0x = T0y , bastando escrever T0. Dessa forma:

<!-- p. 376 -->
ps = 0,9315 p0y = 0,9315 × 0,258 = 0,240 MPa (abs)

Ts = 0,9799 T0 = 0,9799 × 444 = 435 K vs = M s kRTs = 0,32 1,4 × 287 × 435 = 134 m/s b) A pressão máxima a jusante, que causa escoamento totalmente supersônico no divergente, é aquela que provoca uma onda de choque exatamente na seção de saída (pN). Dessa forma, até a seção de saída o escoamento será isoentrópico; logo A* = AG. As A * x = 18,75 6,25 = 3 ⎯⎯Tabe⎯la 1⎯(Ap⎯ênd⎯i⎯ce)→ Mx = 2,64 e ps x = 0,04711 p0x Logo: Com e ps x = 0,04711× 0,41 = 0,019 MPa (abs) Mx = 2,64 ⎯⎯Tabe⎯la 2⎯(A⎯pênd⎯i⎯ce)→ M s y = 0,5005 ps y = 7,965 ps x Logo: ps y = 7,965 × 0,019 = 0,151 MPa (abs) = p N Para qualquer pressão pj < 0,151 MPa (abs), o escoamento será totalmente supersônico no divergente.

## 12.13 Escoamento adiabático com atrito ao longo de condutos de seção

constante (escoamento de Fanno)

Neste item serão mostradas as características de mais um escoamento em função das hipóteses adotadas para a aplicação das equações básicas. Pelo que já foi visto anteriormente, o fato de o escoamento ser adiabático permite concluir que a temperatura de estagnação mantém-se constante ao longo do escoamento e o fato de ser com atrito garante o aumento da entropia. Seja um tubo de corrente (1) – (2) ao longo do escoamento (Figura 12.37).

As equações básicas resultam em:

1) Continuidade:

ρ1 v1 = ρ 2 v2 → f (ρ, v) = 0 2) Energia: T01 = T1 + v12 2 = T2 + v 2 2 2 = T02 → f (T, v) = 0 Figura 12.37 (12.89) (12.90)

<!-- p. 377 -->
C a p í t u l o 1 2 z Escoamento compressível z 377 3) Quantidade de movimento:

τA Lat = p1 A – p2 A + Qm ( v1 – v2 ) → f (τ, p, v) = 0 4) Equação de estado:

p1 = ρ 2 T1 → f (p, ρ, T) = 0 p2 ρ1 T2 (12.91) (12.92)

5) Entropia: s2 > s1 (12.93)

Excluindo a Equação 12.91, forma-se um sistema de quatro equações e cinco variáveis f (ρ, v, T, p, s) = 0. Substituindo adequadamente uma na outra, pode-se chegar a uma função T = f (s), que já foi visto que dá origem à linha de Fanno, que tem o aspecto qualitativo da Figura 12.38. Figura 12.38 Pela Figura 12.38, pode-se observar que em cada ramo da curva os estados só podem variar num sentido, já que a entropia deve obrigatoriamente aumentar ao longo do escoamento. Nota-se, então, que no ramo subsônico a velocidade aumenta ao longo do escoamento e a temperatura diminui; no supersônico acontece o contrário. Através de um equacionamento adequado, pode-se verificar que para smáx acontece M = 1, bloqueando o escoamento. Adotando um tubo de corrente de comprimento infinitesimal, pode-se obter a equação da quantidade de movimento na forma diferencial (Figura 12.39). Figura 12.39 resultando em:

dFSx = – dpA – Qm dv oσnddx,eodnFdSxesσer, ácoamreosufolitavnistetodnaos tensões de cisalhamento na superfície Capítulo 7, é o perímetro molhado.

lateral de área dALat =

<!-- p. 378 -->
Dessa forma: ou τσdx = dpA +ρAvdv τσdx = dp +ρvdv A 4A Lembrando que o diâmetro hidráulico é: DH = σ então:

4τdx = dp +ρvdv DH 4τ No Capítulo 7, pôde-se observar que: f = ρv2 e, portanto:

2 fdx ρv2 = dp + ρvdv DH 2 Após uma série de transformações, chega-se a:

dx (1– M 2 )dM 2 f= DH kM 4 ⎜⎛1+ k –1 2 M 2 ⎟⎞ ⎝2 ⎠ (12.94)

A Equação 12.94 pode ser integrada desde uma seção qualquer do conduto, onde o número de Mach é qualquer um, até a seção do máximo comprimento do conduto, onde M = 1 (lembrar que a curva de Fanno só pode ser percorrida num sentido em cada ramo). ∫ ∫ f xmáx dx = 1 (1– M 2 )

= 1 1– M 2 + k +1 ln k +1M 2 2 x DH M kM 4 ⎛⎜⎝1 + k –1M 2 2 ⎠⎞⎟ kM 2k 1+ k –1M 2 2 Como f = f (Re, DH/k) e a velocidade varia ao longo do escoamento, assim como a viscosidade é função da temperatura, que também varia, então o coeficiente de perda de carga f será uma variável ao longo do conduto. O que é possível, entre x e xmáx, é adotar um valor médio para f, que será indicado por f . Dessa forma: f DH ( x máx – x) = f (k, M)

O valor de xmáx – x pode ser denominado Lmáx e, adotando o valor de k, pode-se tabelar f L máx em função do número de Mach de qualquer seção adotada como a inicial (Tabela 3 do k Apêndice). Quando se deseja resolver um problema para um comprimento L qualquer entre duas seções (1) e (2), deve-se obter os valores de ⎜⎛ f L máx ⎞⎟ e ⎛⎜ f L máx ⎞⎟ da Tabela 3 do Apêndice e ⎝ LD H ⎠ 1 ⎝ D H ⎠ 2 lembrar que:

f L = ⎛⎜ f L máx ⎞⎟ – ⎜⎛ f L máx ⎟⎞ DH ⎝ DH ⎠1 ⎝ DH ⎠ 2 (12.95)

<!-- p. 379 -->
C a p í t u l o 1 2 z Escoamento compressível z 379 Utilizando as equações básicas, é possível relacionar as propriedades de uma seção qualquer com as propriedades da seção onde M = 1 (lembrar que as propriedades críticas são indicadas por um asterisco), e novamente verifica-se que essas propriedades são funções somente de k e M , permitindo o tabelamento para um dado valor de k (Tabela 3 do Apêndice). Ar escoa de um reservatório de grandes dimensões, através de um convergente, para um conduto de diâmetro 7,5 cm constante, de 15 m de comprimento, isolado termicamente. Na saída, a pressão é atmosférica (100 kPa), a temperatura é 20oC e o número de Mach é 0,9. Admite-se que o coeficiente de perda de carga ao longo do conduto seja em média f = 0,02. Admitindo-se que no bocal que liga o conduto ao reservatório o escoamento seja isoentrópico, determinar a pressão e a temperatura do ar do reservatório. Solução Lembrar que, do reservatório até a seção (1), o estado de estagnação se conserva. De (1) a (2) mantém-se T01 = T02 e p02 < p01 , devido às perdas por atrito.

Com M2 = 0,9 ⎯⎯Tabe⎯l⎯a 1→ T2 T0 = 0,8606 → T0 = 293 0,8606 = 340 K f L = 0,02 × 15 = 4 D 0,075 ⎧ p2 = 1,12913 → p* = 100 = 88,6 kPa (abs)

M 2 = 0,9 ⎯⎯Tabe⎯l⎯a 3→ ⎪⎪ p* ⎨⎪⎜⎛ f Lmáx ⎞⎟ 1,12913 = 0,0145 ⎩⎪⎝ D ⎠ 2 ⎛⎜ f Lmáx ⎞⎟ = ⎛⎜ f L⎞⎟ + ⎛⎜ f Lmáx ⎞⎟ = 4 + 0,0145 = 4,0145 ⎝ D ⎠1 ⎝ D ⎠ ⎝ D ⎠2 ⎛⎜ ⎝ f Lmáx D ⎞⎟ ⎠ 1 = 4,0145 ⎯⎯Tabe⎯la 3⎯(in⎯terp⎯olan⎯d⎯o)→ M 1 = 0,34 M1 = 0,34 ⎯⎯Tab⎯ela 3⎯(in⎯terp⎯olan⎯d⎯o)→ p1 p* = 3,23 → p1 = 3,23 × 88,6 = 286 kPa (abs)

Logo: p01 = p1 = 0,9231 286 = 0,9231 310 kPa (abs)

Da mesma forma que nos bocais convergentes/divergentes, partindo-se de um certo estado de estagnação no reservatório a montante, se a pressão a jusante for reduzida aos poucos, a vazão em massa no conduto irá aumentando até se atingir M = 1, quando o escoamento ficará bloqueado.

<!-- p. 380 -->
Como não é possível ultrapassar M = 1, pois haveria uma diminuição da entropia, ulteriores reduções da pressão a jusante causarão uma expansão brusca na saída, fora do conduto (Figura 12.40). Figura 12.40 O ar de um reservatório à pressão de 700 kPa (abs) e uma temperatura de 5oC escoa por um conduto isolado termicamente de 3 cm de diâmetro e 30 m de comprimento. A pressão de saída é 100 kPa (abs) e admite-se que o coeficiente de perda de carga médio seja 0,012. Do reservatório ao conduto, o ar é conduzido por um convergente isoentrópico. Determinar o número de Mach e a pressão na entrada do conduto. Solução Para verificar se o escoamento está bloqueado, assume-se que: L = Lmáx, isto é, Lmáx = 30 m. Logo: ⎜⎛ ⎝ f Lmáx D ⎞⎟ ⎠ 1 = 12 ⎯⎯Tabe⎯la 3⎯(in⎯ter⎯p.)→ ⎪⎧M 1 ⎨ p01 ⎩⎪ p * 0 = = 0,22 2,56 Portanto: p * 0 = p01 2,56 = 700 2,56 = 273 kPa (abs) Admitindo-se M2 = 1 pela Tabela 1 do Apêndice, p2 = p* p*0 = 0,528528 Portanto: p2 = 0,528528 × p*0 = 0,528528 × 273 = 144 kPa (abs) > p2 = 100 kPa (abs) dado. Logo, como p2 para M2 = 1 é maior que o p2 dado, que deveria coincidir com pj, conclui-se que a pressão de saída é menor que a que provocaria M2 = 1 e, portanto, o conduto está bloqueado. Nesse caso L = Lmáx e realmente M1 = 0,22.

<!-- p. 381 -->
Com C a p í t u l o 1 2 z Escoamento compressível z 381 M1 = 0,22⎯⎯Tabe⎯l⎯a 1→ p1 p01 = 0,9669 → p1 = 0,9669 × 700 = 677 kPa (abs)

Se o escoamento de Fanno for alimentado por um convergente/divergente em condições supersônicas, os estados do escoamento corresponderão ao ramo inferior da linha de Fanno (Figura 12.38). Nesta se observa que, ao longo do escoamento, a pressão e a temperatura aumentam por causa do atrito e o número de Mach diminui, podendo ser unitário no limite. Se a jusante a pressão pj for maior que p*, acontecerá uma onda de choque em alguma seção do conduto e, como já foi visto, o escoamento passará para subsônico a jusante da onda até a saída. Se a pressão de saída for aumentada gradativamente, a onda de choque caminhará para montante até se instalar no convergente/divergente que alimenta o conduto. Lembrar que, nessa situação, a vazão em massa será sempre a mesma, controlada pela garganta do bocal convergente/divergente. Continuando a aumentar a pressão a jusante, a onda de choque irá desaparecer ao chegar na garganta e finalmente o escoamento ficará totalmente subsônico. A partir dessa situação, o bocal não estará mais bloqueado e ulteriores aumentos da pressão a jusante provocarão uma redução na vazão em massa a partir do valor crítico. Ar escoa por um bocal convergente/divergente, cuja área da garganta é 20 cm2. Na saída, o divergente tem um diâmetro de 7,5 cm e alimenta um conduto circular de seção constante, isolado termicamente, de mesmo diâmetro e de 3,6 m de comprimento. O reservatório que alimenta o bocal está a uma pressão de 206 kPa (abs) e a uma temperatura de 60oC. Observa-se uma onda de choque no conduto a uma distância de 3 m da entrada e supõe-se que f = 0,008. Assumindo que no convergente/divergente o escoamento seja isoentrópico e que no conduto seja de Fanno, determinar a pressão de saída. Solução A1 = πD12 4 π × 7,5 2 = 4 = 44,18 cm2 A1 A* = 44,18 20 = 2,209 ⎯⎯Tab⎯ela⎯1→ ⎪⎧M1 ⎨ p1 ⎪⎩ p 0 = 2,32 = 0,07751 → p1 = 0,07751 × 206 = 20,1 kPa (abs)

M 1 = 2,32 ⎧⎛ ⎯⎯Tabe⎯l⎯a 3→ ⎨⎪⎪⎜⎝ f Lmáx D ⎞ ⎟ ⎠1 = 0,39 ⎪ p1 = 0,0332 → p* = 20,1 = 60,5 kPa (abs)

⎪⎩ p* 0,332 ⎛ f L⎞ ⎜⎟ = ⎛ ⎜ f Lmáx ⎞ ⎟ – ⎛ ⎜ f Lmáx ⎞ ⎟ ⎝ D ⎠ 1– Cx ⎝ D ⎠ 1 ⎝ D ⎠ Cx

<!-- p. 382 -->
⎛⎜ f Lmáx ⎟⎞ = ⎛⎜ f Lmáx ⎟⎞ – ⎛⎜ f L⎟⎞ = 0,39 – 0,008 × 3 = 0,07 ⎝ D ⎠ Cx ⎝ D ⎠ 1 ⎝ D ⎠ 0,075 ⎜⎛ ⎝ f Lmáx D ⎟⎞ ⎠ Cx = 0,07 ⎯⎯Tabe⎯l⎯a 3→ ⎧⎪M x ⎨ px ⎪⎩ p* = 1,4 = 0,6632 px = 0,6632 × 60,5 = 40,1 kPa (abs)

Mx = 1,4 ⎯⎯Tabe⎯l⎯a 2→ ⎪⎧M y = 0,7397 ⎨py ⎪⎩ px = 2,12 py = 2,12 × 40,1 = 85 kPa (abs)

⎧⎛⎜ f Lmáx ⎟⎞ = 0,12728 ⎪⎨ My = 0,7397 ⎯⎯Tabe⎯l⎯a 3→ ⎝ D ⎠ Cy py = 1,3548 ⎩⎪p*' p*' = 85 = 61,4 kPa (abs) 1,3848 ⎛⎜ f Lmáx ⎟⎞ = ⎜⎛ f Lmáx ⎟⎞ – ⎜⎛ f L⎞⎟ = 0,12728 – 0,008 × 0,6 = 0,0633 ⎝ D ⎠ 2 ⎝ D ⎠ Cy ⎝ D ⎠ y 0,075 ⎪⎩ ⎛ ⎜ ⎝ f Lmáx D ⎞ ⎟ ⎠ 2 = 0,0633 ⎯⎯Tabe⎯l⎯a 3→ ⎧⎨⎪Mpy2 p*' = = 0,82 1,254 p2 = 1,254 × 61,4 = 77 kPa (abs)

Neste item foram abordados apenas idéias básicas e exemplos simples envolvendo o escoamento de Fanno. Para um estudo mais detalhado, o leitor deverá recorrer a textos mais especializados sobre dinâmica dos gases. Pela mesma razão, deixa-se de analisar o escoamento de Rayleigh, sem atrito, com trocas de calor ao longo de condutos de seção constante, já que uma análise mais profunda foge do escopo deste estudo. 12.1 Uma massa de 10oC) para um 8 kg de oxigênio estado (2) (p2 = 5 sofre uma transformação de um estado (1) bar (abs) e T2 = 95oC). Sabendo que para o (p1 = 1,3 oxigênio bar k= (abs) 1,393 e e T1 cp = = 921,6 J, determinar:

a) a constante R da equação de estado; b) o calor específico a volume constante; c) a variação da energia interna; d) a variação da entalpia; e) a massa específica final. Resp.: a) R = 260 J/kg.K; b) cv = 661,6 J/kg.K; c) ΔI = 450 kJ; d) ΔH = 627 kJ; e) ρ2 = 5,226 kg/m3

<!-- p. 383 -->
C a p í t u l o 1 2 z Escoamento compressível z 383 12.2 As propriedades do ar são obtidas como uma média ponderada de seus componentes; dessa forma, admite-se que sua massa molecular seja 29. Um recipiente rígido de 2 m3 contém ar a 20 oC e uma pressão de 2 MPa (abs). O recipiente é aquecido até atingir uma pressão de 5 MPa (abs). Sabe-se que a constante universal dos gases é R = 8.315 J/kmol.K e que a constante adiabática de ar é k = 1,4. Determinar: a) os calores específicos a volume e pressão constantes; b) a temperatura final em oC; c) a variação de energia interna; d) a variação de entalpia. Resp.: a) cv = 717 J/kg.K; cp = 1.004 J/kg.K; b) T2 = 460oC; c) ΔI = 15 MJ; d) ΔH = 21 MJ 12.3 Ar a 20oC e 103 kPa (abs) é comprimido isoentropicamente de forma que seu volume se reduza a 40% do inicial. Sendo k = 1,4, determinar:

a) a pressão e a temperatura finais; b) a variação da energia interna específica; c) a variação da entalpia específica.

Resp.: a) p2 = 371 kPa (abs); T2 = 150oC; b) Δu = 93,2 kJ/kg; c) Δh = 130,5 kJ/kg 12.4 Ao longo de uma tubulação J/kg.K. Numa seção (1), um escoa vapor manômetro dinedáigcaua0,,4coMnPsiadeeruamdotegráms ôpmerefetritooi,ncdoimcak3=001o,C32. 7Eme copu=tr1a.8s7e2ção (2) a jusante, um manômetro indica 0,4 MPa e a temperatura é 150oC. Sendo a pressão atmosférica local 100 kPa, qual é a variação da entropia específica de (1) a (2)? Resp.: Δs = –568 J/kgK 12.5 Um projétil desloca-se em ar com uma velocidade de 360 km/h. Qual é o tipo de escoamento, se no local a temperatura é 20oC? Dados: k = 1,4 e R = 286 J/kg.K. Resp.: Escoamento subsônico com M = 0,29 12.6 Na seção de um escoamento de ar (k = 1,4), o manômetro ligado a um tubo de Pitot indica 20 kPa e um termômetro, mergulhado no escoamento para indicar a temperatura de estagnação, indica 50oC. Sabendo que o número de Mach nessa seção é 0,6 e que a pressão atmosférica local é 100 kPa, determinar a temperatura, a pressão, a massa específica e a velocidade do ar nessa seção. Resp.: T = 28,3oC; p = –5,9 kPa; ρ = 1,088 kg/m3; v = 209 m/s 12.7 Numa certa seção do escoamento de ar, a temperatura estática é 20oC. Um tubo de Pitot colocado no fluxo provoca um desnível de 20 mmHg num manômetro diferencial. Sendo a pressão 100 kPa (abs), qual é a velocidade do ar? Qual é o erro cometido ao se considerar o ar como incompressível? Dados: k = 1,4; R = 287 m2/s2K; e γHg = 136.000 N/m3 e patm = 100 kPa.

Resp.: v = 67,3 m/s; 0,45% 12.8 Mantidos os outros dados do Exemplo 12.7, qual seria o desnível de mercúrio no manômetro diferencial para uma velocidade do ar de 400 m/s? Qual é o erro cometido ao se considerar o ar como incompressível? Resp.: h = 970 mm; 27,8% 12.9 No Venturi da figura, escoa ar (k = 1e3A61.0=0050Nc/mm23.,Adeseteçrãmo i(n2a) rt:em área 1,4; R de 25 = 287 cm2 e m2/s2.K). Na seção (1) tem-se o coeficiente de descarga do p1 = 105 Venturi Pa (abs); T1 = é 0,95. Dado 20oC γHg = a) o coeficiente de compressibilidade; b) a vazão em massa; c) o erro cometido ao se considerar o fluido incompressível.

<!-- p. 384 -->
Resp.: a) φ = 0,47; b) Qm = 0,518 kg/s; erro = 113% 12.10 Hélio escoa através de um Venturi, que tem um diâmetro de aproximação de 15 cm e um diâmetro de garganta de 10 cm. A pressão e temperatura na seção de aproximação são, respectivamente, 200 kPa (abs) e 366 K. Um manômetro diferencial ligado entre as duas seções registra um desnível de 5,1 m, utilizando água como fluido manométrico. Determinar a vazão em massa do hélio. Dados: kHe = 1,665; cp He = 5.200 J/kg. K; CD = 0,95; γ H2O = 104 N/m 3. Resp.: Qm = 1,151 kg/s 12.11 Um recipiente de grandes dimensões contém hidrogênio a 1,5 bar (abs) e 550 K. Determinar a velocidade de descarga por um orifício de bordo delgado, para os seguintes casos: a) a massa específica do gás é considerada constante ao longo do escoamento; b) a massa específica do gás é variável ao longo do escoamento. Determinar o erro ao considerar o caso a). Dados: k = 1,405; cp = 14.532 J/kg.K; patm = 1 bar; supor cv = 1. Resp.: a)1.239 m/s; b) 1.328 m/s; c) 6,7% 12.12 Dois aviões equipados com sensores de ondas de pressão deslocam-se na mesma trajetória, um contra o outro, com velocidades de 2.130 km/h (avião 1) e 530 km/h (avião 2). No local do movimento, T = –55oC, k = 1,4 e R = 287 m2/s2K. a) Qual dos dois sensores registrará primeiro a presença do outro avião? b) Sabendo que o raio de propagação da onda registrada pelo sensor é 14.800 m, qual é a distância entre os aviões, no instante em que o sensor registra a presença do outro? c) Sabendo que o tempo mínimo de manobra para mudar a trajetória do avião (1) é 15 s e do avião (2) é 5 s, haverá colisão? Resp.: b) 7.440 m; c) haverá após 10 s 12.13 Num túnel aerodinâmico, o modelo de um projétil dá origem a uma onda de pressão cônica, cujo ângulo do vértice é 50o. A pressão e temperatura na região externa à onda são, respectivamente, 100 kPa (abs) e 22oC. Calcular a velocidade de escoamento do ar e o número de Mach nas condições indicadas. Dados: k = 1,4; R = 287 m2/s2.K. Resp.: v = 815 m/s; M = 2,37 12.14 Vapor de água escoa de um reservatório de grandes dimensões, onde a pressão é 105 Pa (abs) e a temperatura é 130oC, por um bocal, com escoamento isoentrópico. Sendo k = 1,33 e R = 462 m2/s2.K, determinar a temperatura, a velocidade, a pressão e a massa específica do estado crítico. Resp.: T* = 346 K; v* = 461 m/s; p* = 54 kPa (abs); ρ* = 0,338 kg/m3

<!-- p. 385 -->
C a p í t u l o 1 2 z Escoamento compressível z 385 12.15 Um reservatório de grandes dimensões contém ar à pressão de 1 MPa (abs) e temperatura de 300oC. O ar é descarregado ao ambiente por um bocal convergente de área de saída As = 2 × 10–4 m2. Supondo que o escoamento seja isoentrópico e bloqueado, qual é a vazão em massa? Dados: k = 1,4 e R = 287 m2/s2.K. Resp.: 0,338 kg/s 12.16 Na figura, o ar apresenta escoamento isoentrópico, bloqueado. Sabendo que a pressão de estagnação é 2 × 105Pa 136.000 N/m3.

(abs), determinar A1. Dados: k = 1,4; R = 287 m2/s2.K; As = 15 cm2; patm =105 Pa; γHg = Resp.: A1 = 20,1 cm2 12.17 O reservatório de grandes dimensões da figura descarrega o ar à atmosfera com escoamento isoentrópico. a) Qual é a temperatura indicada no termômetro? b) Qual é a vazão em massa na seção de saída? c) Qual é a vazão em massa na seção onde M = 0,3? d) Qual é a área da seção onde M = 0,3? e) Qual é a máxima vazão em massa que poderia ser obtida e como poderia ser provocada sem alterar a leitura do termômetro? Resp.: a) 373 K; b) 0,193 kg/s; c) 0,193 kg/s; d) 15,6 cm2; e) 0,396 kg/s 12.18 O reservatório da figura é de grandes dimensões e o escoamento no convergente é isoentrópico. Determinar: a) a pressão e a temperatura de estagnação; b) a leitura do manômetro M2, quando o tubo de Pitot é instalado na seção (A); c) a velocidade na seção (B); d) a área da seção crítica; e) o desnível h do mercúrio (γHg = 136.000 N/m3). Dados: AA = 3 × 10–3 m2; AB = 2 × 10–3 m2; T1 = 300 K; T2 = 290,7 K; pM1 = 1,79 × 105 Pa (abs); pM2 = 2 × 105 Pa (abs).

<!-- p. 386 -->
Resp.: a) T0 = 300 K; p0 = 2 × 105 Pa (abs); b) 2 × 105 Pa (abs); c) 136,7 m/s; d)1,26 × 10–3 m2; e) 64 mmHg 12.19 Um conduto para a exaustão do ar de um avião está fixado em sua parte superior. O avião voa com uma velocidade de 180 m/s. A temperatura e a pressão do ar em repouso são, respectivamente, –6oC e 100 kPa (abs). Determinar a velocidade e a temperatura numa seção do conduto onde M = 0,8. Adotar escoamento isoentrópico. Dados: k = 1,4; R = 287 m2/s2K. Resp.: T2 = 251 K; v2 = 254 m/s 12.20 Ar escoa isoentropicamente num conduto divergente. A pressão e a temperatura na seção (1) são, respectivamente, 0,34 MPa (abs) e 27oC e a velocidade é 312 m/s. Se A2 = 2,37, determinar a pressão, a temperatura e a velocidade na seção (2).

A1 Resp.: p2 = 0,55 MPa (abs); T2 = 345 K; v2 = 93,1 m/s 12.21 No dispositivo da figura, qual deve ser a rotação do eixo para que o número de Mach na saída seja igual a 1? Dados: 10 cm2.

o fluido é ar com escoamento isoentrópico, a temperatura ambiente é 293 K, Ae = 20 cm2, As = Resp.: 491 rpm e 3.604 rpm

<!-- p. 387 -->
C a p í t u l o 1 2 z Escoamento compressível z 387 12.22 Um bocal convergente/divergente de seção circular tem a montante um reservatório de grandes dimensões onde o ar tem p = 106 Pa (abs) e T = 650 K. Sabendo que o escoamento é isoentrópico e bloqueado e dados k = 1,4 e R = 287 m2/s2.K, determinar: a) a pressão, a temperatura e a massa específica na garganta:

b) o diâmetro da garganta para que a vazão em massa seja 34 kg/s; c) a temperatura e a velocidade na saída do divergente, sabendo que a pressão é 105 Pa (abs); d) a área da seção de saída.

Resp.:

a) p* = 5,28 410 cm2 × 105 Pa (abs); T* = 542 K; ρ* = 3,4 kg/m3; b) D = 0,165 m; c) Ts = 338 K; vs = 792 m/s; d) As = 12.23 A figura mostra um bocal convergente/divergente, em que o escoamento é isoentrópico, bloqueado e contínuo. O reservatório a montante é de grandes dimensões. a) Determinar a pressão, a temperatura e a massa específica de estagnação.

b) Determinar a pressão e a temperatura na garganta do bocal.

c) Se o tubo de Pitot for instalado na seção (2), qual será o novo desnível do mercúrio, mantido o outro ramo do manômetro diferencial? (Justifique.) Resp.: a) T0 = 310 K; p0 = 201,8 kPa (abs); ρ0 = 2,27 kg/m3; b) p* = 106,6 kPa (abs); T * = 258 K 12.24 Um pequeno foguete é testado num banco de provas. A saída dos gases de combustão é feita por um divergente, em que os gases sofrem uma expansão total até a pressão ambiente. A temperatura e a pressão na câmara de combustão são, respectivamente, 2.730 K e 3,4 MPa (abs) e a câmara de combustão é considerada um reservatório de grandes dimensões. O consumo total de oxidante e combustível é 4,5 kg/s. Supondo o escoamento isoentrópico e dados k = 1,4 e R = 287 m2/s2.K, determinar: a) a força de propulsão indicada no dinamômetro; b) a área da seção de saída; c) a área da seção crítica. Resp.: a) FSx = 8.388 N; b) As = 69,3 cm2; c) A* = 17,3 cm2

<!-- p. 388 -->
12.25 Para o bocal convergente/divergente da figura:

a) Quais são os valores da pressão de saída que permitem obter um escoamento totalmente isoentrópico bloqueado? b) Qual é a máxima vazão em massa? Resp.: a) p ' 3 = 0,622 MPa (abs); p'3' = 0,08 MPa (abs); b) Qmc = 16 4,2 kg/s 12.26 Um túnel aerodinâmico é projetado para uma vazão de ar de 6,3 kg/s. O número de Mach na seção de testes deverá ser igual a 2, quando a pressão e a temperatura de estagnação forem, respectivamente, 0,1 MPa (abs) e 260 K. Calcular a área da garganta, a de saída e as pressões, temperaturas e velocidades nessas seções, considerando o escoamento isoentrópico. Resp.: AG = 251 cm2; As = 424 cm2; p* = 52,8 kPa (abs); T* = 217 K; v* = 295 m/s; ps = 12,7 kPa (abs); Ts = 144 K; vs = 482 m/s 12.27 A velocidade dos gases na saída de um foguete é 2.000 m/s. A pressão na câmara de combustão é 1,51 MPa (abs). Sabendo que a área de saída é 319 cm2 e a da garganta 293 cm2 e que o escoamento é totalmente isoentrópico, determinar a pressão e a temperatura dos gases na saída do foguete e a força de propulsão. Supor que as propriedades dos gases coincidam com as do ar. Resp.: ps = 0,516 MPa (abs); Ts = 5.544 K; FSz = 41.342N 12.28 Em um bocal convergente/divergente escoa ar (k = 1,4; R = 287 m2/s2.K), proveniente de um reservatório de grandes dimensões. Numa seção do divergente, nota-se uma onda de choque e, no restante do conduto, supõe-se que o escoamento seja isoentrópico. A relação entre a pressão e a pressão do estado de estagnação na seção a montante da onda de choque é 0,272. Dados: para a saída ps = 105 Pa (abs); Ts = 300 K; As = 1,35 AGarganta; determinar:

<!-- p. 389 -->
C a p í t u l o 1 2 z Escoamento compressível z 389 a) a intensidade da onda de choque; b) se A * x ≠ A y*; c) as propriedades de estagnação a montante da onda de choque; d) a vazão em massa em função da área de saída; e) o esboço do diagrama do número de Mach em função do comprimento do bocal; f) a irreversibilidade da onda de choque (Δs).

Resp.: a) IntOC = 2,46; b) A * y = 1,075 Ax*; c) p0x = 1,3 × 105 Pa (abs); T0 = 317 K; d) Qm = 213,6As kg/s; f) Δs = 20,8 J/kg.K 12.29 No bocal convergente/divergente da figura escoa ar (k = 1,4; R = 287 m2/s2.K). Dados: Ts = 300 K; As = 2,0 AG; patm = 0,9 × 105 Pa; γHg = 1,36 × 105 N/m3.

a) Determinar a pressão e a temperatura do reservatório a montante. b) Determinar o desnível h indicado no manômetro. c) Completar os valores de p/p0 indicados no gráfico. Resp.: a)144 kPa (abs); 313 K; b) 0,474 m 12.30 A descarga de ar de um reservatório de grandes dimensões é feita por um bocal convergente/divergente que tem uma área da garganta de 10–3 m2 e uma área de saída de 2× 10–3 m2. Sabendo que o escoamento Ts = 505 é bloqueado e que no reservatório a K, pode-se afirmar que ocorre uma pressão é 106 Pa (abs) e na saída ps = 7,56 onda de choque? Dados: k = 1,4; R = 287 × 105 Pa (abs) m2/s2.K.

e Resp.: Sim 12.31 Se, com os dados do exercício anterior, ocorrer uma onda de choque normal numa seção de área 1,4 × 10–3, determinar: a) as propriedades de estagnação na seção de saída do divergente; b) a variação de velocidade entre a entrada e a saída da onda de choque; c) a vazão em massa. Resp.: a) T0y = 520 K; p0y = 830 kPa (abs); b) Δv = 357 m/s; c) Qm = 1,78 kg/s 12.32 No exercício anterior, determinar as propriedades nas seções de entrada e saída da onda de choque, na garganta e na saída do divergente, e esboçar em função do comprimento do bocal: a) o diagrama de p/p0; b) o diagrama de T/T0; c) o diagrama do número de Mach.

<!-- p. 390 -->
12.33 No convergente/divergente da figura, sabe-se que o escoamento imediatamente a montante da seção (1) é supersônico. Pelo desnível do manômetro diferencial, é possivel afirmar que na seção indicada existe uma onda de choque? Justifique. Dados: h = 1 m; A1 = 38 × 10–4 m2; As = 40 × 10–4 m2; Ts = 400 K; T0y = 429 K; γHg = 1,36 × 105 N/m3. Determinar:

a) o número de Mach na seção imediatamente a jusante da onda de choque; b) o número de Mach na seção de saída do bocal; c) as pressões de estagnação a montante e a jusante da onda de choque. Resp.: a) My = 0,66; b) Ms = 0,6; c) p0x = 1,01 × 106 Pa (abs); poy = 0,9 × 106 Pa(abs) 12.34 No ensaio de um bocal convergente/divergente, utilizou-se o ar contido num reservatório de grandes dimensões à pressão de 6,8 × 105 N/m2(abs) e à temperatura de 533 K. Para uma vazão em massa de 110 kg/s, obteve-se o diagrama da figura. Determinar: a) a área crítica; b) a área onde ocorre a onda de choque; c) a área da seção de saída. Esboçar os diagramas p = f (x) e T = f (x), especificando os valores de p e T nas seções de entrada, da garganta, da onda de choque e de saída do bocal. Resp.: a) A* = 924 cm2; b) AC = 1.371 cm2; c) As = 1.835 cm2 12.35 É dado um bocal convergente/divergente alimentado pelo reservatório da figura. Para uma certa pressão de jusante, a vazão em massa é máxima, a temperatura na seção (1) é 373 K e o escoamento é contínuo em todo o divergente. Modificando as condições a jusante, observa-se uma onda de choque na seção (1). Determinar a diferença de temperatura entre os pontos imediatamente a jusante e a montante da onda de choque e esquematizar a variação de pressão ao longo do bocal para as duas condições de jusante (k = 1,4; R = 287 m2/s2.K). Resp.: ΔT = 85 K

<!-- p. 391 -->
C a p í t u l o 1 2 z Escoamento compressível z 391 12.36 No bocal da figura escoa ar ( k = 1,4; R = 287 m2/s2.K). Numa certa condição, a seção de área mínima é crítica, a massa específica na seção (1), de área 160 cm2, é 1,225 kg/m3 e o escoamento até essa seção é isoentrópico. Variando a pressão a jusante, obteve-se uma segunda situação, ocorrendo uma onda de choque na seção (1). Para a segunda situação, determinar: a) a temperatura a montante da onda de choque; b) a vazão em massa; c) M e v na garganta. Resp.: a) 267 K; b) 4,29 kg/s; c) M = 1; v = 366 m/s 12.37 Quando a pressão e a temperatura atingem, respectivamente, 1 MPa (abs) e 300 K, entra em funcionamento a válvula de segurança da figura, que descarrega o ar ( k = 1,4; R = 287 m2/s2K) para outro reservatório, através de um bocal convergente/divergente. Determinar: a) os valores de M e T na seção de saída, onde p = 100 kPa (abs); b) os valores de M e T do jato na câmara de jusante, quando se forma uma onda de choque na seção de saída do bocal. Resp.: a) Ms = 2,16; Ts = 155 K; b) My = 0,552; Ty = 283 K 12.38 O ar escoa por um convergente/divergente. Numa seção do escoamento, forma-se uma onda de choque normal. As condições são tais que, no manômetro ligado ao tubo de Pitot da figura, o nível do mercúrio é igual nos dois ramos. Qual é a velocidade na seção a jusante da onda de choque? Resp.: v = 185 m/s 12.39 O ar de um reservatório escoa por um tubo isolado termicamente de diâmetro interno 7,5 cm e comprimento 15 m. Na saída, as condições são: p2 = 105 Pa (abs); T2 = 294 K e M2 = 0,9. Adota-se que o coeficiente de perda de carga distribuída seja 0,02 constante. Supondo o escoamento isoentrópico e contínuo desde o reservatório até o tubo isolado, determinar a temperatura e a pressão de estagnação no reservatório.

Resp.: T0 = 342 K; p0 = 322 k Pa (abs)

12.40 Seja um conduto isolado termicamente de 13,2 m de comprimento e 2,5 cm de diâmetro. O coeficiente de perda de carga distribuída médio é f = 0,008. Sabendo que na seção de entrada (1) o número de Mach é 0,3 e a pressão é 0,27 MPa (abs) e que o fluido que escoa é ar, determinar a queda de pressão entre a entrada e a saída. Resp.: Δp = 0,011 MPa

<!-- p. 392 -->
12.41 No esquema da figura, determinar T2, p2 e v2. Dados: M1 = 0,5; p1 = 0,14 MPa (abs) e M2 = 1. Resp.: p2 = 0,065 MPa (abs); T2 = 277 K; v2 = 334 m/s 12.42 Qual deve ser o comprimento de um conduto isolado de diâmetro 10 cm e f = 0,012, para que o ar que nele escoa passe de M = 3 para M = 2? Resp.: L = 1,8 m 12.43 Ar entra num conduto isolado termicamente de diâmetro 10 cm com M = 3, p = 0,1 MPa (abs) e T = 188 K. Sendo f = 0,01, determinar Lmáx, p*, T*,v*. Determinar também p, v e T na seção onde M = 2, assim como a distância entre a seção de M = 3 e M = 2. Resp.: Lmáx = 5,22 m; p* = 0,46 MPa (abs); T* = 439 K; v* = 420 m/s; L = 2,17 m; p = 0,19 MPa (abs); T = 292 K; v = 686 m/s 12.44 Qual é a vazão em massa máxima de ar que pode escoar de um reservatório à temperatura de 15,5oC por um conduto isolado termicamente de 2,5 cm de diâmetro e 6 m de comprimento? O ar é descarregado à atmosfera, cuja pressão é 100 kPa, e o coeficiente de perda de carga distribuída médio é 0,02. Resp.: Qm = 0,219 kg/s 12.45 Ar quente é retirado de uma sala que contém um forno, para manter um reservatório aquecido. A ligação entre a sala e o reservatório é feita por um convergente/divergente (isoentrópico) seguido de um conduto de seção constante (adiabático com atrito). No reservatório estão instalados um termômetro, um manômetro e um ventilador que mantêm o regime permanente. Determinar a leitura do manômetro, a leitura do termômetro e a vazão em massa. Dados: k = 1,4; R = 287 m2/s2.K. Resp.: p = 0,13 MPa (abs); T = 600 K; Qm = 1,68 kg/s

<!-- p. 393 -->
Exercícios selecionados z 393 Os exercícios propostos a seguir envolvem a teoria de diversos capítulos do livro, entretanto, como orientação, ao lado do número do exercício, será indicado o capítulo que ele pretende focalizar.

1. (Cap. 4) Por razões técnicas, pela bomba da instalação da figura devem passar sempre 50 L/s. A bomba fornece água (ã = 104 N/m3) aos tanques de grandes dimensões (1) e (2), com vazões, Sendo a área respectivamente: Q1 da seção de todos os = 20 L/s tubos A e = Q2 20 = 10 cm2, L/s. çB = 70% e a potência total dissipada pelos atritos Ndiss = 1,5 kW, determinar a potência no eixo da bomba e a sua carga manométrica.

Figura 1 Resp.: NB = 5,57 kW; HB = 11,1 m 2. (Cap. 4) No processo de produção de um gás líquido, o gás entra pela tubulação (1) (A1 = 0,8 m2) com p1 = 100 kPa(abs), T1 = 30oC, velocidade média na seção de 70 m/s e passa por um compressor e um resfriador, que provocam uma liquefação parcial. O gás líquido dirige-se para a seção (3), enquanto a fração gasosa é separada e desviada por (2) (A2 = 200 cm2), onde tem uma massa específica de 90 kg/m3 e uma velocidade média na seção de 10 m/s. O gás líquido é bombeado entre (3) e (4), onde adquire uma energia por unidade de peso de 100 m. Sendo o peso específico do gás líquido 4250 N/m3, qual = 287 m2/s2.K.

a potência em kW que ele recebe da bomba? Dados: p/ñ = RT; Rgás

<!-- p. 394 -->
Figura 2 Resp.: N = 46,3 kW 3. (Cap. 4) Na instalação da figura, a turbina recebe água do reservatório (0) e a descarrega no reservatório (3). A turbina aciona diretamente o eixo de uma bomba que eleva a água a 10 m de altura, onde é descarregada na atmosfera, com uma velocidade de 100 cm2 10 m/s. Dados: (área da seção Hp0,1 = 6,8 m; Hp3,4 = 1 m; Hp5,6 dos tubos); p1 = 200 kPa; ã = =1024mN;/çmB =3.

80%; çT = 0,91; At = Determinar a carga manométrica da turbina.

Figura 3 Resp.: HT = 30,9 m 4. (Cap. 4) No circuito da figura, a potência fornecida ao fluido pela bomba é 7,5 kW. O fluido é água (ã = 104 N/m3) e o fluido manométrico é mercúrio (ãHg = 1,36 × 105). A instalação está num plano horizontal e a bateria de manômetros, num plano vertical. Despreza-se a perda de carga no Venturi. Determinar: a) a vazão; b) a perda de carga na válvula. c) Substituindo-se a válvula por uma turbina de rendimento 75%, qual a potência que poderia ser extraída de seu eixo, mantido o resto constante? Dados: A1 = A2 = A3 = A4 = A5 = 10 cm2; A6 = 5 cm2.

<!-- p. 395 -->
Exercícios selecionados z 395 Figura 4 Resp.: a) 9,16 L/s; b) 56,5 m c) 3,9 kW 5. (Cap. 5) O tampão de base circular da figura está colocado concentricamente na tubulação horizontal de seção circular para controlar a vazão de água. Sendo ρ = 1.000 kg/m3 e desprezando a perda de carga, determinar a força F necessária para segurar o tampão. 5 cm V1 = 4 m/s F? 4 cm Figura 5 Resp.: F = 49,5 N 6. (Cap. 5) Duas bombas recalcam água (ã = 104 N/m3) para o sistema da figura, no qual é lançada na vertical para a atmosfera, na seção (4). O tubo de saída é isolado do resto da instalação por uma luva elástica. A bomba B1 recalca uma vazão de 5 L/s e a bomba B2 recalca 10 L/s. A potência dissipada total, desde a saída das bombas até (4), é 4,4 kW. Determinar: a) a velocidade do jato na seção (4); b) o módulo da força aplicada pela água no trecho de tubulação entre (3) e (4).

<!-- p. 396 -->
Figura 6 Resp.: Fsz = 346,5 N 7. (Cap. 5) No dispositivo da figura, o pistão de peso G = 29,4 kN desce muito lentamente dentro do cilindro de área 2 m2, empurrando a água (ã = 104 N/m3) pelos dois cotovelos instalados simetricamente. A vazão no cotovelo (1)-(2) é 5,8 L/s e a perda de carga é 2,7 m, enquanto no cotovelo (3)-(4) é 1,2 L/s e a perda de carga é 0,5 m. Determinar: a) a velocidade na seção (2), sendo A 2 = 2. A4 b) Tampando-se a seção (4), a vazão no cotovelo (1)-(2) passa a valer 6 L/s. Nesta condição, qual o momento torçor no eixo do cilindro? Figura 7 8. (Cap. 7) Numa fábrica constrói-se um trocador de calor, cujos diâmetros de entrada e saída são 10 cm. Para determinar o comprimento equivalente do trocador, constrói-se o circuito da figura, no qual todas as perdas singulares são consideradas desprezíveis, fluido é óleo menos a do trocador. Dados: de viscosidade cinemática í =p11=0–140m0 2k/Ps ae; p2 = 200 kPa; Q peso específico = ã 5 = L/s; o 8.000 N/m3; as tubulações são de diâmetro constante D = 10 cm; despreza-se o comprimento da bomba. Determinar o comprimento equivalente do trocador.

<!-- p. 397 -->
Exercícios selecionados z 397 Figura 8 9. (Cap. 7) Na instalação da figura são dados: Q = 4 L/s; área da seção das tubulações A = 20 cm2; potencia da máquina NM = 0,19 kW; a perda de carga distribuída é diretamente proporcional ao comprimento da tubulação; as perdas de carga singulares são desprezíveis; o fluido é óleo de peso específico 8.000 N/m3. Determinar: a) o sentido do escoamento; b) a perda de carga na instalação; c) o tipo de máquina; d) a diferença de pressão entre a entrada e a saída da máquina; e) o rendimento da máquina. Figura 9 10.(Cap. 6) A perda de pressão no escoamento laminar de um fluido, num conduto de seção circular constante com um certo comprimento, é função da massa específica, da viscosidade cinemática, da velocidade do fluido e do diâmetro do conduto. Verificou-se, experimentalmente, que a relação entre os adimensionais para tubos cujo comprimento é 100 vezes o diâmetro, é π1 π2 = 3.200, onde os adimensionais foram obtidos diretamente pelo teorema π, e π2 é o adimensional que contém a viscosidade cinemática. a) Determinar a equação física que permite obter a perda de pressão em tubos nessas condições.

b) Determinar a perda de carga num tubo horizontal nas condições dadas, quando nele escoa água (ñ = 1.000 kg/m3; í = 10–6 m2/s), sendo D = 2 cm e v = 0,1 m/s. c) É possível, pela equação determinada, calcular a perda de carga quando o fluido é água, o diâmetro é 10 cm e a velocidade é 10 m/s?

<!-- p. 398 -->
Resp.: a) Δp = 3.200 ρvν ; D para L = 100D; b) hf = 1,6 × 10–3 m; c) Não. 11.

(Cap. 7) válvula A válvula de um circuito, mostrada escoa uma vazão de 1,2 L/s de um na figura, tem fluido muito vDis1 c=o2socm(íe=D120=–41mcm2/s. ;Pãel=a 8.000 N/m3). Qual o coeficiente de perda de carga singular da válvula? (1) (2) 2m Resp.: ks = 0,865 gHg = 1,36 x 105 N/m3 Figura 10 12.(Cap. 7) Num trecho de conduto retangular (20 cm × 40 cm) para ventilação, escoa ar (ñ = 1,2 kg/m3), considerado incompressível, com uma vazão de 2 m3/s. Determinar: a) o coeficiente de perda de carga singular da válvula (2); b) a queda de pressão de (1) a (4) ao longo do conduto. Dados: ks3 = 10; Leq3 = 178 m; g = 10 m/s2; desprezar o comprimento das válvulas. 20 m (2) (3) ar (1) (4)

0,2 m gH2O = 104 N/m3 Figura 11 Resp.: a) ks2 = 5,33; b) Äp = 6,172 kPa 13.(Cap. 6) Para testar um pára-quedas no laboratório, prende-se um modelo semelhante, na escala 1/10, numa balança e sopra-se ar para cima com um ventilador, até que a balança indique zero. Sabe-se que a força de arrasto, causada pelo ar, é dada por: Fa = C a ρv 2 0 8 πD 2 , onde: D = diâmetro do pára-quedas; ñ = massa específica do ar; v0 = velocidade do ar em relação ao pára-quedas; Ca = coeficiente de arrasto do pára-quedas (adimensional característico do pára-quedas). O pára-quedas real, com pára-quedista e seus acessórios, pesa 1.000 N e ao se pendurar o modelo na balança, antes de ligar o ventilador, esta indica 10 kg. Deseja-se que o pára-quedista chegue ao solo com uma velocidade constante de 7 m/s. Com que velocidade do ar do ventilador a balança deverá indicar zero para o modelo?

<!-- p. 399 -->
balança Exercícios selecionados z 399 Fluxo de ar ventilador Figura 12 Resp.: vm = 22,1 m/s 14.(Cap. 9) Uma placa plana de espessura desprezível é presa por fios de dimensões e pesos desprezíveis, de forma a não poder girar livremente. Sopra-se ar para cima, com a velocidade na direção da placa com valor crescente, até que a balança indique zero; isto acontece com 10 m/s. O ar tem viscosidade cinemática 10–5m2/s, massa específica 1,2 kg/m3 e se admite que Recr = 106. a) Qual a massa indicada pela balança, que tem precisão até gramas, antes de se ligar o ventilador? b) Qual a tensão de cisalhamento média que age na placa? c) Qual a indicação da balança quando o fluxo de ar do ventilador tiver uma velocidade de 6 m/s? balança 3m 2,5 m ventilador Figura 13 Resp.: a) mpl = 0,079 kg; ô = 0,0509 N/m2; m = 0,061 kg.

15.(Cap. 9) Quando um automóvel se move numa estrada plana, as forças que agem contra o movimento são: a força de arrasto (Fa) e a força de resistência ao rolamento dos pneus (Frol), que se supõe independente da velocidade do veículo.

<!-- p. 400 -->
Coloca-se um automóvel de massa 1.200 kg numa descida cuja rampa é sensivelmente igual a 2o constante e, em ponto morto, deixa-se o veículo descer livremente. O painel é dotado de um acelerômetro calibrado em submúltiplos da aceleração da gravidade g, que no local vale 9,8 m/s2. Ao passar por 40 km/h e ao passar por 100 km/h, registram-se as acelerações indicadas pelo acelerômetro e verifica-se uma diferença de 0,03 g. A área frontal dorautomóvel ér 2 m2 e no local a massa específica do ar é 1,12 kg/m3. Lembrando que Fresultante = ma, qual o coeficiente de arrasto do automóvel? Resp.: Ca = 0,486 16.(Cap. 4) Na instalação da figura, a bomba envia 5 L/s de água (ã = 104 N/m3) para o reservatório superior e uma parte da vazão retorna para o tanque inferior. Dados: p6 = 100 kPa; Hp6,0 = 25 fluido pela bomba: N = m; 12 Hp0,1 = 10 m; Hp2,3 kW; área da seção = 5 m; Hp3,4,6 = 0; potência de todas as tubulações: A fornecida ao = 10 cm2. Determinar:

a) a vazão que retorna ao tanque inferior (Q6); b) a carga manométrica da bomba; c) a perda de carga de (4) a (5); d) a potência dissipada em toda a instalação.

Figura 14 Resp.: a) Q6 = 10 L/s; b) HB = 80 m; c) Hp4,5 = 125 m; d) Ndiss= 14 kW.

17.(Cap. 4) Uma bomba succiona água (ã = 10.000N/m3) de um reservatório, cujo nível se encontra a 1,5 m da sua seção de entrada, por um tubo de diâmetro de 50 mm. Na saída da bomba encontra-se um manômetro metálico que indica uma pressão de 750 kPa. A tubulação de recalque tem diâmetro de 50 mm por um comprimento de 30 m e nesse ponto ela se bifurca em dois ramais simétricos de 25 mm de diâmetro e 30 m de comprimento, que formam um ângulo de 30o entre si. Dados: • perda de carga nas tubulações de 50 mm de diâmetro: 0,1 m por metro de tubulação; • perda de carga nas tubulações de 25 mm de diâmetro: 0,14 m por metro de tubulação. Determinar: a) a vazão em volume em L/s; b) a altura ou carga manométrica da bomba.

<!-- p. 401 -->
Exercícios selecionados z 401 Figura 15 Resp.: a) Q = 15 L/s; b) HB = 80,5 m 18.(Cap. 6) A função representativa de um certo fenômeno é f (ñ; ì; v; F; c; L) = 0. Onde c = velocidade do som e L é um comprimento característico qualquer. Como no laboratório os ensaios são realizados com baixas velocidades, supõe-se desprezível o efeito da compressibilidade do fluido. Dados:

- para para o o pmroodtóetliop:oñ:mñ=p =1.14.40000kgk/gm/m3;3F; mFp==12.2.08000NN; .

Determinar a escala das viscosidades dinâmicas.

Resp.: kì = 0,96 19.(Cap. 6) Uma bomba B1, instalada como na figura, fornece uma vazão de 20L/s e uma pressão de saída de 390 kPa, girando com 3.450 rpm. Nessas condições, a potência dissipada na bomba é 2,6 kW. Para a análise dessa bomba dispõe-se da curva ηB = f (φ). Pede-se:

a) o diâmetro do rotor da bomba B1 em mm.

b) Substituindo o conjunto motobomba por outro que possui uma bomba B2, completamente semelhante à bomba B1, determinar a nova carga manométrica, sabendo que a rotação é a mesma da bomba B1 e que a relação dos diâmetros dos rotores é D1 = 1,5D2. Dados: γ H 2O = 104 N m3 ; g = 10 m/s2; H p 0,s ≅ 0; As = 40 cm2; ψ = gH B n 2D2 ; φ = Q nD3 . hB 80 (%) 70 60 50 40 30 20 10 0 0 Motor (0) 0,005 0,01 0,015 0,02 0,025 f Resp.: a) D = 259 mm; b) HB2 = 18,7 m As B (s) 1,75 m Figura 16

<!-- p. 402 -->
20.(Cap. 4) Na instalação da figura, a potência trocada entre o fluido e a máquina é 7,14kW. Se o escoamento é perfeitamente isotérmico e o fluxo de calor dissipado entre (0) e (e) é 4,2kW, determinar: a) o tipo de máquina; b) o fluxo de calor entre (s) e (1) em kW. Dados: ãH2O = 104 N/m3; Q = 42 L/s; g = 10 m/s2; A = 105 cm2 (área da seção da tubulação). Figura 17 Resp.: a) Bomba; b) Q~& ≅ 6 kW.

21.(Cap. 6) Um projétil que vai se deslocar em ar (ã = 10 N/m3; í = 10–5 m2/s), é testado com água (ã = 104 N/m3; í = 10–6 m2/s) num canal de provas, sendo obtidos os dados da tabela, que relacionam a força de resistência ao avanço com a velocidade do projétil. V 2 4 6 8 10 (m/s) F 40 100 180 300 450 (N)

Dado: F = f(ñ; v; L; ì). Qual a força que agirá no projétil quando ele se deslocar em ar com 80 m/s? Resp.: F = 30N 22.(Cap. 4) Num conduto de seção circular escoa água (ñ = 1.000kg/m3). Admite-se que nas seções (A) e (B) os diagramas de velocidades sejam os indicados na figura. Supondo pA = pB, determinar: a) a velocidade média na seção; b) o coeficiente da energia cinética na seção (A); c) a perda de carga entre (A) e (B). Resp.: a) vm = 8,75 m/s; b) áA = 3,12; c) Hp,A,B = 8,1 m Figura 18

<!-- p. 403 -->
Exercícios selecionados z 403 23.(Cap. 7) No trecho (1)-(2) do conduto da figura, o escoamento do fluido (ã = 8.000 N/m3) é laminar, a vazão é 10 L/s, o diâmetro é 8 cm e o Re = 1.000. No trecho (3)-(4) o diâmetro é 6 cm. O coeficiente da perda de carga da singularidade (2)-(3) é 1, referente à maior velocidade. Qual a pressão na seção (1)? Figura 19 Resp.: p1 = 65,12 kPa 24.(Cap. 7) No trecho de um conduto que alimenta um queimador de caldeira, escoam ar e combustível por dois tubos concêntricos, como mostra a figura. O ar, de massa específica 2 kg/m3, é considerado incompressível e percorre o tubo externo, onde se sabe que a perda de carga é 3m por metro de tubulação e que o coeficiente de perda de carga distribuída é 0,01. O combustível tem massa específica 800 kg/m3 e viscosidade cinemática 10–4 m2/s. A relação ar/combustível em massa deve ser 10/1. Dados: D1 = 65 mm; D2 = 70 mm; D3 = 740 mm, determinar: a) a velocidade do ar; b) a velocidade do combustível; c) a perda de carga do combustível no trecho indicado. Figura 20 Resp.: a) var = 63,4 m/s; b) vc = 2 m/s: c) h fc = 0,6 m 25.(Caps. 6 e 7) No escoamento por um tubo de um fluido muito viscoso, a perda de carga é dada por H p L = 51,87π 1 π 2 , onde π1 e π2 são os adimensionais obtidos de Q = f (D, g) e ν = f (v,D), pelo teorema dos π, usando as bases entre parênteses, e L é o comprimento da tubulação.

Desprezando as perdas de carga singulares, determinar:

a) os adimensionais pelo teorema dos ð, usando as bases dadas; b) a velocidade teórica do fluido na tubulação; c) a velocidade real do fluido na tubulação; d) o coeficiente de perda de carga distribuída.

<!-- p. 404 -->
10 m v = 10-4 m2/s g = 104 N/m3 L = 20 m D 2 cm Figura 21 Resp.: b) vt = 14,1 m/s; c) vr = 0,62 m/s d) f = 0,516 26.(Cap. 8) No esquema da figura, o nível da água é mantido constante. Determinar: a) o coeficiente de velocidade; b) o número de Reynolds teórico; c) o tempo que a água levará para subir 10 cm ao fechar o registro do bocal; d) a distância atingida pelo jato, pressurizando-se o tanque com ar comprimido, com p = 20 kPa; e) a perda de carga no bocal, supondo a perda na válvula desprezível. 1,5 m v= 104 N/m3 g = 10-6 m2/s Abocal = 3,14 cm2 Dados: gx2 y = 2v2 g = 10 m/s2 Atanque = 0,6 m2 Cc = 0,9 1m 2,2 m Figura 22 Resp.: a) Cv = 0,9; b) Ret = 1,1 × 105; c) t = 49 s; d) x = 3,37 m; e) Hp = 0,29 m 27.(Cap. 7) Uma sala de 4m × 6m × 3m é usada como cabine de pintura. Sabe-se que numa cabine de pintura o ar (ñ = 1,2 kg/m3 (constante); í = 10–5m2/s) deve ser trocado, por norma, no mínimo 60 vezes por hora. O ventilador joga o ar à pressão atmosférica e mantém a pressão da sala a –1kPa. O ar de reposição deve ser captado a uma certa distância por um conduto de seção quadrada de chapa de aço, de lados 20 cm. Sendo o comprimento equivalente do alargamento brusco 10 m, qual o comprimento máximo do conduto de captação? Conduto de seção quadrada Alargamento brusco Sala Ventilador Patm Patm Captação Lmáx p = -1 kPa Figura 23

<!-- p. 405 -->
Exercícios selecionados z 405 Resp.: Lmáx = 28 m 28.(Cap. 1) O pistão da figura levanta, com velocidade constante, um peso G = 2.000N sob a ação de uma pressão. Entre o pistão e o cilindro existe uma película de lubrificante (ρ = 800 kg/m3; ν = 10–3m2/s). Qual a velocidade de subida do peso, supondo desprezíveis os pesos da haste e do pistão? Figura 24 Resp.: v = 1,42 m/s 29.(Cap. 1) O dispositivo da figura gira a 1.200 rpm, acionado por um motor que mantém o torque constante, independentemente da rotação. Para variar a rotação, desloca-se o mancal móvel para a esquerda. Qual a nova rotação atingida, em rpm, deslocando totalmente o mancal? Dado: v = πnD. Dados:

D1 = 20 cm D2 = 20,1 cm d1 = 5 cm d2 = 5,01 cm L1 = 0,2 m L2 = 0,5 m lubrificante m = 10-2 N.s/m2 mancal móvel d1 d2 D1 D2 lubrificante motor eixo L2 L1 Figura 25 Resp.: n =1.668 rpm 30.(Caps. 5 e 7) A instalação da figura é utilizada num laboratório de hidráulica para medir o coeficiente de perda de carga distribuída (f) em tubulações. O reservatório, de grandes dimensões, é apoiado num dinamômetro eletrônico e, uma vez instalado o sistema, o leitor do dinamômetro é zerado. Ao abrir a tampa, e estabelecido o regime permanente, o leitor do dinamômetro indica 300N.

<!-- p. 406 -->
Dados: ks1 = 1; ñ = 1.000 kg/m3; g = 10 m/s2. Qual o coeficiente de perda de carga distribuída no escoamento assim estabelecido? tampa (0) (1)

1,5 m leitor 300N 6m dinamômetro D = 10 cm (2) Figura 26 Resp.: f = 0,0254 31.(Cap. 12) Um tubo Venturi é usado para medir a vazão em massa de ar numa tubulação. O tubo tem 15 cm de diâmetro e a garganta tem 7,5 cm de diâmetro. A pressão e a temperatura na maior seção são respectivamente 400 kPa(abs) e 20oC; e na garganta a pressão é 340 kPa(abs). Sendo dados para o ar: R = 287 m2/s2.K; 1004 m2/s2K e considerando o escoamento isoentrópico, pede-se: k = 1,4; cp = a) a vazão em massa; b) o número de Mach na garganta; c) o erro cometido ao considerar o fluido incompressível.

Resp.: a) Qm = 3,1 kg/s; b) M = 0,494; c) å = 11,3% 32.

(mCeanpt.e1a2)2O00akrP(aR(aarb=s)2e8730moC2/.sA2.Kv;ákl=vu1,l4a)

contido do pneu num pneu de quebra e o ar bicicleta começa está iniciala vazar. Supõe-se que a mínima seção da válvula seja a seção de saída, que tem um diâmetro de 2 mm. O ambiente está com 100 kPa e 30oC. Admite-se que durante o vazamento a temperatura do ar do pneu se mantenha constante.

a) A partir de que pressão do ar do pneu a vazão em massa começa a variar? b) Qual a vazão em massa no instante em que começa a variar? c) Qual a massa de ar que vazou do pneu, desde o instante do início do vazamento, até o instante em que a vazão em massa começa a variar, considerando que o volume interno do pneu se mantenha 6,2 × 10-3m3 aproximadamente constante? Resp.: a) p0 = 189 kPa(abs); b) Qm = 1,38 × 10–3 kg/s; c) Äm = 7,87 × 10-4 kg 33.(Cap. 7) Ao repor o óleo de um motor no posto de serviços, o frentista mantém o funil sempre constantemente cheio. Como o óleo tem uma elevada viscosidade cinemática (10–5 m2/s), supõe-se que o escoamento no funil seja laminar e, neste caso, sabe-se que o coeficiente de perda de carga distribuída é dado por f = 64 . Admite-se Re que no escoamento não haja perdas singulares importantes e que a perda de carga distribuída acontece somente no trecho cilíndrico do funil, cujo diâmetro é 8 mm. (g = 10 m/s2) a) Quanto tempo levará para repor o óleo, supondo que o carter do motor tenha uma capacidade para 3,5 L? b) Verificar se o escoamento é realmente laminar.

<!-- p. 407 -->
Exercícios selecionados z 407 Figura 27 Resp.: a) t = 55,7s; b) Re = 1.000 34.(Cap. 6) O bico injetor de um sistema de injeção eletrônica para motores é constituído de uma agulha que levanta, liberando um orifício que injeta o combustível devido a uma diferença de pressão Äp entre a entrada e a saída. Sabe-se que a vazão em volume Q que escoa pelo orifício é função da viscosidade do fluido ì, do diâmetro do orifício D e de Δp. Adotando como base ì, Δp e D, sabendo-se que para um dado motor L L o orifício tem D = 0,5 mm, qual o diâmetro do orifício para outro motor que necessita de 20% a mais de vazão de combustível, mantidas todas as outras variáveis? Resp.: D = 0,524mm Figura 28 35.(Cap. 12) A variação da pressão atmosférica com a altitude pode ser obtida pela expressão p = p NM ⎛ ⎜1− ⎝ 0,0065z T NM ⎞ ⎟ ⎠ 5, 26 , onde: pNM = 100 kPa (pressão ao nível do mar), TNM = 298K (temperatura ao nível do mar) e z = altitude em metros. Um míssil intercontinental é projetado para que voe numa altitude na qual a velocidade dos gases de propulsão, na saída, seja a máxima, sem que haja a perda de energia provocada por ondas de choque.

Os gases são descarregados da câmara de combustão (considerada de grandes dimensões), por um convergente/divergente que tem a área a de tura séa2íd.0a00AosC=.

2 m2. Na câmara Determinar:

de combustão a pressão é da garganta AG 200 kPa (abs) e = 1,13 m2 e a temperaa) a mínima altitude na qual deverá viajar o míssil; b) a vazão em massa dos gases de propulsão. Supor que as propriedades dos gases sejam iguais às do ar: k = 1,4; R = 287 m2/s2.K. Resp.: a) z = 11.090 m; b) Qm = 191 kg/s

<!-- p. 408 -->
36.(Caps. 5 e 9) Um barco tem a propulsão efetuada por uma bomba que succiona água (ñ = 1.000 kg/m3) na proa e a descarrega na popa. A área da seção de entrada na proa é suficientemente grande para se poder desprezar a velocidade, e na popa a área da seção de saída da água é 300 cm2. A velocidade da água no tubo de descarga é medida por um tubo de Pitot que indica 20 m/s. A área frontal do barco é 2 m2 e o coeficiente de arrasto é 0,35. As bocas de entrada e saída da água são suficientemente próximas do nível da água, para se poder adotar que a pressão seja atmosférica. Determinar a velocidade máxima do barco em km/h. Figura 29 Resp.: vb = 5,85 m/s = 21 km/h 37.(Cap. 12) No bocal da figura, o escoamento está bloqueado e até a seção (1) é isoentrópico. Numa outra situação (não desenhada) diminui-se a pressão a jusante e, até a seção (1), o escoamento continua isoentrópico e se observa que no manômetro a coluna inverte, isto é, fica mais alta do lado direito. a) Qual a altura do mercúrio na segunda situação? b) Qual a vazão em massa na seção (1) na primeira situação? c) Qual a vazão em massa na garganta na segunda situação? V=0 p = 800 kPa(abs) k = 1,4 R = 287 m2/s2.K TG = 311K (G) (1) A1 = 20 cm2 1,5 m gHg = 1,36 x 105 N/m3 Figura 30 Resp.: a) h = 1,55 m; b) Qm = 2,82 kg/s 38.(Cap. 9) Uma placa plana de espessura desprezível está presa por um fio a uma esfera oca de 10 cm de diâmetro externo e 1mm de espessura. A esfera é de um material de massa específica 7.800 kg/m3 e flutua no plano diametral num fluido de massa específica 2.500 kg/m3, como mostra a figura. Corta-se o fio e a placa desce com velocidade máxima de 0,5 m/s. Supondo desprezível o trecho de camada limite laminar na placa, determinar a viscosidade dinâmica do fluido.

<!-- p. 409 -->
Exercícios selecionados z 409 Figura 31 Resp.: ì =5,79 × 10–3N.s/m2 39.(Caps. 5 e 12) Uma plataforma de cargas é sustentada por quatro jatos de ar (R = 287 m2/s2.K) inclinados, para favorecer a estabilidade e as manobras. Admite-se que, na entrada e na saída, a pressão seja atmosférica e igual a 100 kPa e a temperatura seja 30oC. Admite-se que na entrada a área seja muito grande e na saída o diâmetro seja de 0,6 m. A plataforma é dimensionada para sustentar, em repouso, um total de 10 kN. a) Qual a mínima vazão em massa que deve ser produzida por cada ventilador? b) Qual a mínima potência do motor de cada ventilador, se o seu rendimento é 70% e a perda de carga ao longo dos condutos é desprezível? (1) (2) 15° SOLO Figura 32 Resp.: a) Qm = 29 kg/s; b) Nv = 165 kW 40.(Cap. 12) O esquema mostra um tubo convergente/divergente alimentado por um reservatório de grandes dimensões. Na seção de saída do divergente acontece uma onda de choque e as condições na seção imediatamente a jusante da onda são indicadas pelo termômetro T mergulhado no fluxo e pelos manômetros M1 e M2, cujas tomadas são respectivamente na direção do fluxo e a ele tangente. Sendo a pressão indicada pelo manômetro M1 0,15 MPa(abs), a temperatura igual a 0,2 MPa(abs), pelo indicada pelo termômetro Tmiagnuôaml aet1r2o7oMC2 igual a e a área da seção da onda de choque igual a 50 cm2, pede-se:

a) a pressão e a temperatura no reservatório que alimenta o conduto; b) a área da garganta; c) a vazão em massa.

<!-- p. 410 -->
410 z Mecânica dos Fluidos Figura 33 Resp.: a) p0x = 0,225 MPa(abs); T0 = 400K; b) AG = 39,5 cm2; c) Qm = 1,8kg/s Figura 33

<!-- p. 411 -->

# Apêndice — Tabelas para escoamentos compressíveis

Tabela 1 – Relações para o escoamento unidimensional, isoentrópico, de um gás perfeito com k = 1,4 M T/T0 p/p0 r./r0 A/A* 0,00 1,0000 1,0000 1,0000 ∞ 0,02 0,9999 0,9997 0,9998 28,94 0,04 0,9997 0,9989 0,9992 14,48 0,06 0,9993 0,9975 0,9982 9,666 0,08 0,9987 0,9955 0,9968 7,262 0,10 0,9980 0,9930 0,9950 5,822 0,12 0,9971 0,9900 0,9928 4,864 0,14 0,9961 0,9864 0,9903 4,182 0,16 0,9949 0,9823 0,9873 3,673 0,18 0,9936 0,9777 0,9840 3,278 0,20 0,9921 0,9725 0,9803 2,964 0,22 0,9904 0,9669 0,9762 2,708 0,24 0,9886 0,9607 0,9718 2,496 0,26 0,9867 0,9541 0,9670 2,317 0,28 0,9846 0,9470 0,9619 2,166 0,30 0,9823 0,9395 0,9564 2,035 0,32 0,9799 0,9315 0,9506 1,922 0,34 0,9774 0,9231 0,9445 1,823 0,36 0,9747 0,9143 0,9380 1,736 0,38 0,9719 0,9052 0,9313 1,659 0,40 0,9690 0,8956 0,9243 1,590 0,42 0,9659 0,8857 0,9170 1,529 0,44 0,9627 0,8755 0,9094 1,474 0,46 0,9594 0,8650 0,9016 1,425

<!-- p. 412 -->
M 0,48 0,50 0,52 0,54 0,56 0,58 0,60 0,62 0,64 0,66 0,68 0,70 0,72 0,74 0,76 0,78 0,80 0,82 0,84 0,86 0,88 0,90 0,92 0,94 0,96 0,98 1,00 1,02 1,04 1,06 1,08 1,10 1,12 1,14 1,16 1,18 1,20 1,22 1,24 1,26 1,28 1,30 1,32 T/T0 0,9560 0,9524 0,9487 0,9449 0,9410 0,9370 0,9328 0,9286 0,9243 0,9199 0,9154 0,9108 0,9061 0,9013 0,8964 0,8915 0,8865 0,8815 0,8763 0,8711 0,8659 0,8606 0,8552 0,8498 0,8444 0,8389 0,8333 0,8278 0,8222 0,8165 0,8108 0,8052 0,7994 0,7937 0,7880 0,7822 0,7764 0,7706 0,7648 0,7590 0,7532 0,7474 0,7416 p/p0 0,8541 0,8430 0,8317 0,8201 0,8082 0,7962 0,7840 0,7716 0,7591 0,7465 0,7338 0,7209 0,7080 0,6951 0,6821 0,6691 0,6560 0,6430 0,6300 0,6170 0,6041 0,5913 0,5785 0,5658 0,5532 0,5407 0,5283 0,5160 0,5039 0,4919 0,4801 0,4684 0,4568 0,4455 0,4343 0,4232 0,4124 0,4017 0,3912 0,3809 0,3708 0,3609 0,3512 H./H0 0,8935 0,8852 0,8766 0,8679 0,8589 0,8498 0,8405 0,8310 0,8213 0,8115 0,8016 0,7916 0,7814 0,7712 0,7609 0,7505 0,7400 0,7295 0,7189 0,7083 0,6977 0,6870 0,6764 0,6658 0,6551 0,6445 0,6339 0,6234 0,6129 0,6024 0,5920 0,5817 0,5714 0,5612 0,5511 0,5411 0,5311 0,5213 0,5115 0,5019 0,4923 0,4829 0,4736 A/A* 1,380 1,340 1,303 1,270 1,240 1,213 1,188 1,166 1,145 1,127 1,110 1,094 1,081 1,068 1,057 1,047 1,038 1,030 1,024 0,018 1,013 1,009 1,006 1,003 1,001 1,000 1,000 1,000 1,001 1,003 1,005 1,008 1,011 1,015 1,020 1,025 1,030 1,037 1,043 1,050 1,058 1,066 1,075

<!-- p. 413 -->
M 1,34 1,36 1,38 1,40 1,42 1,44 1,46 1,48 1,50 1,52 1,54 1,56 1,58 1,60 1,62 1,64 1,66 1,68 1,70 1,72 1,74 1,76 1,78 1,80 1,82 1,84 1,86 1,88 1,90 1,92 1,94 1,96 1,98 2,00 2,02 2,04 2,06 2,08 2,10 2,12 2,14 2,16 2,18 Tabelas para a solução de escoamentos de fluidos compressíveis z 413 T/T0 0,7358 0,7300 0,7242 0,7184 0,7126 0,7069 0,7011 0,6954 0,6897 0,6840 0,6783 0,6726 0,6670 0,6614 0,6558 0,6502 0,6447 0,6392 0,6337 0,6283 0,6229 0,6175 0,6121 0,6068 0,6015 0,5963 0,5911 0,5859 0,5807 0,5756 0,5705 0,5655 0,5605 0,5556 0,5506 0,5458 0,5409 0,5361 0,5314 0,5266 0,5219 0,5173 0,5127 p/p0 0,3417 0,3323 0,3232 0,3142 0,3055 0,2969 0,2886 0,2804 0,2724 0,2646 0,2570 0,2496 0,2423 0,2353 0,2284 0,2217 0,2152 0,2088 0,2026 0,1966 0,1907 0,1850 0,1794 0,1740 0,1688 0,1637 0,1587 0,1539 0,1492 0,1447 0,1403 0,1360 0,1318 0,1278 0,1239 0,1201 0,1164 0,1128 0,1094 0,1060 0,1027 0,09956 0,09650 H./H0 0,4644 0,4553 0,4463 0,4374 0,4287 0,4201 0,4116 0,4032 0,3950 0,3869 0,3789 0,3711 0,3633 0,3557 0,3483 0,3409 0,3337 0,3266 0,3197 0,3129 0,3062 0,2996 0,2931 0,2868 0,2806 0,2745 0,2686 0,2627 0,2570 0,2514 0,2459 0,2405 0,2352 0,2301 0,2250 0,2200 0,2152 0,2105 0,2058 0,2013 0,1968 0,1925 0,1882 A/A* 1,084 1,094 1,104 1,115 1,126 1,138 1,150 1,163 1,176 1,190 1,204 1,219 1,234 1,250 1,267 1,284 1,301 1,319 1,338 1,357 1,376 1,397 1,418 1,439 1,461 1,484 1,507 1,531 1,555 1,580 1,606 1,633 1,660 1,688 1,716 1,745 1,775 1,806 1,837 1,869 1,902 1,935 1,970

<!-- p. 414 -->
M 2,20 2,22 2,24 2,26 2,28 2,30 2,32 2,34 2,36 2,38 2,40 2,42 2,44 2,46 2,48 2,50 2,52 2,54 2,56 2,58 2,60 2,62 2,64 2,66 2,68 2,70 2,72 2,74 2,76 2,78 2,80 2,82 2,84 2,86 2,88 2,90 2,92 2,94 2,96 2,98 3,00 3,10 3,20 T/T0 0,5081 0,5036 0,4991 0,4947 0,4903 0,4859 0,4816 0,4773 0,4731 0,4689 0,4647 0,4606 0,4565 0,4524 0,4484 0,4444 0,4405 0,4366 0,4328 0,4289 0,4252 0,4214 0,4177 0,4141 0,4104 0,4068 0,4033 0,3998 0,3963 0,3928 0,3894 0,3860 0,3827 0,3794 0,3761 0,3729 0,3697 0,3665 0,3633 0,3602 0,3571 0,3422 0,3281 p/p0 0,09352 0,09064 0,08784 0,08514 0,08252 0,07997 0,07751 0,07513 0,07281 0,07057 0,06840 0,06630 0,06426 0,06229 0,06038 0,05853 0,05674 0,05500 0,05332 0,05169 0,05012 0,04859 0,04711 0,04568 0,04429 0,04295 0,04166 0,04039 0,03917 0,03800 0,03685 0,03574 0,03467 0,03363 0,03262 0,03165 0,03071 0,02980 0,02891 0,02805 0,02722 0,02345 0,02023 H./H0 0,1841 0,1800 0,1760 0,1721 0,1683 0,1646 0,1610 0,1574 0,1539 0,1505 0,1472 0,1440 0,1408 0,1377 0,1347 0,1317 0,1288 0,1260 0,1232 0,1205 0,1179 0,1153 0,1128 0,1103 0,1079 0,1056 0,1033 0,1010 0,09885 0,09671 0,09462 0,09259 0,09059 0,08865 0,08674 0,08489 0,08308 0,08130 0,07957 0,07788 0,07623 0,06852 0,06165 A/A* 2,005 2,041 2,078 2,115 2,154 2,193 2,233 2,274 2,316 2,359 2,403 2,448 2,494 2,540 2,588 2,637 2,687 2,737 2,789 2,842 2,896 2,951 3,007 3,065 3,123 3,183 3,244 3,306 3,370 3,434 3,500 3,567 3,636 3,706 3,777 3,850 3,924 3,999 4,076 4,155 4,235 4,657 5,121

<!-- p. 415 -->
M 3,30 3,40 3,50 3,60 3,70 Tabelas para a solução de escoamentos de fluidos compressíveis z 415 T/T0 0,3147 0,3019 0,2899 0,2784 0,2675 p/p0 0,01748 0,01512 0,01311 0,01138 0,009903 H./H0 0,05554 0,05009 0,04523 0,04089 0,03702 A/A* 5,629 6,184 6,790 7,450 8,169 Tabela 2 – Relações para onda de choque normal. Gás perfeito com k = 1,4 M N M y p0y./p0x Ty /.Tx py./px Hy./Hx 1,00 1,000 1,000 1,000 1,000 1,000 1,02 0,9805 1,000 1,013 1,047 1,033 1,04 0,9620 0,9999 1,026 1,095 1,067 1,06 0,9444 0,9998 1,039 1,144 1,101 1,08 0,9277 0,9994 1,052 1,194 1,135 1,10 0,9118 0,9989 1,065 1,245 1,169 1,12 0,8966 0,9982 1,078 1,297 1,203 1,14 0,8820 0,9973 1,090 1,350 1,238 1,16 0,8682 0,9961 1,103 1,403 1,272 1,18 0,8549 0,9946 1,115 1,458 1,307 1,20 0,8422 0,9928 1,128 1,513 1,342 1,22 0,8300 0,9907 1,141 1,570 1,376 1,24 0,8183 0,9884 1,153 1,627 1,411 1,26 0,8071 0,9857 1,166 1,686 1,446 1,28 0,7963 0,9827 1,178 1,745 1,481 1,30 0,7860 0,9794 1,191 1,805 1,516 1,32 0,7760 0,9757 1,204 1,866 1,551 1,34 0,7664 0,9718 1,216 1,928 1,585 1,36 0,7572 0,9676 1,229 1,991 1,620 1,38 0,7483 0,9630 1,242 2,055 1,655 1,40 0,7397 0,9582 1,255 2,120 1,690 1,42 0,7314 0,9531 1,268 2,186 1,724 1,44 0,7235 0,9477 1,281 2,253 1,759 1,46 0,7157 0,9420 1,294 2,320 1,793 1,48 0,7083 0,9360 1,307 2,389 1,828 1,50 0,7011 0,9298 1,320 2,458 1,862 1,52 0,6941 0,9233 1,334 2,529 1,896 1,54 0,6874 0,9166 1,347 2,600 1,930 1,56 0,6809 0,9097 1,361 2,673 1,964 1,58 0,6746 0,9026 1,374 2,746 1,998 1,60 0,6684 0,8952 1,388 2,820 2,032 1,62 0,6625 0,8876 1,402 2,895 2,065

<!-- p. 416 -->
M M N y 1,64 0,6568 1,66 0,6512 1,68 0,6458 1,70 0,6406 1,72 0,6355 1,74 0,6305 1,76 0,6257 1,78 0,6210 1,80 0,6165 1,82 0,6121 1,84 0,6078 1,86 0,6036 1,88 0,5996 1,90 0,5956 1,92 0,5918 1,94 0,5880 1,96 0,5844 1,98 0,5808 2,00 0,5774 2,02 0,5740 2,04 0,5707 2,06 0,5675 2,08 0,5643 2,10 0,5613 2,12 0,5583 2,14 0,5554 2,16 0,5525 2,18 0,5498 2,20 0,5471 2,22 0,5444 2,24 0,5418 2,26 0,5393 2,28 0,5368 2,30 0,5344 2,32 0,5321 2,34 0,5297 2,36 0,5275 2,38 0,5253 2,40 0,5231 2,42 0,5210 2,44 0,5189 2,46 0,5169 p0y./p0x 0,8799 0,8720 0,8640 0,8557 0,8474 0,8389 0,8302 0,8215 0,8127 0,8038 0,7947 0,7857 0,7766 0,7674 0,7581 0,7488 0,7395 0,7302 0,7209 0,7115 0,7022 0,6928 0,6835 0,6742 0,6649 0,6557 0,6464 0,6373 0,6281 0,6191 0,6100 0,6011 0,5921 0,5833 0,5745 0,5658 0,5572 0,5486 0,5402 0,5318 0,5234 0,5152 Ty /.Tx 1,416 1,430 1,444 1,458 1,473 1,487 1,502 1,517 1,532 1,547 1,562 1,577 1,592 1,608 1,624 1,639 1,655 1,671 1,687 1,704 1,720 1,737 1,754 1,770 1,787 1,805 1,822 1,839 1,857 1,875 1,892 1,910 1,929 1,947 1,965 1,984 2,002 2,021 2,040 2,059 2,079 2,098 py./px 2,971 3,048 3,126 3,205 3,285 3,366 3,447 3,530 3,613 3,698 3,783 3,870 3,957 4,045 4,134 4,224 4,315 4,407 4,500 4,594 4,689 4,784 4,881 4,978 5,077 5,176 5,277 5,378 5,480 5,583 5,687 5,792 5,898 6,005 6,113 6,222 6,331 6,442 6,553 6,666 6,779 6,894 Hy./Hx 2,099 2,132 2,165 2,198 2,230 2,263 2,295 2,327 2,359 2,391 2,422 2,454 2,485 2,516 2,546 2,577 2,607 2,637 2,667 2,696 2,725 2,755 2,783 2,812 2,840 2,868 2,896 2,924 2,951 2,978 3,005 3,032 3,058 3,085 3,110 3,136 3,162 3,187 3,212 3,237 3,261 3,285

<!-- p. 417 -->
Tabelas para a solução de escoamentos de fluidos compressíveis z 417 M N M y p0y./p0x Ty /.Tx py./px Hy./Hx 2,48 0,5149 0,5071 2,118 7,009 3,310 2,50 0,5130 0,4990 2,137 7,125 3,333 2,52 0,5111 0,4910 2,157 7,242 3,357 2,54 0,5092 0,4832 2,177 7,360 3,380 2,56 0,5074 0,4754 2,198 7,479 3,403 2,58 0,5056 0,4677 2,218 7,599 3,426 2,60 0,5039 0,4601 2,238 7,720 3,449 2,62 0,5022 0,4526 2,259 7,842 3,471 2,64 0,5005 0,4452 2,280 7,965 3,494 2,66 0,4988 0,4379 2,301 8,088 3,516 2,68 0,4972 0,4307 2,322 8,213 3,537 2,70 0,4956 0,4236 2,343 8,338 3,559 2,72 0,4941 0,4166 2,364 8,465 3,580 2,74 0,4926 0,4097 2,386 8,592 3,601 2,76 0,4911 0,4028 2,407 8,721 3,622 2,78 0,4897 0,3961 2,429 8,850 3,643 2,80 0,4882 0,3895 2,451 8,980 3,664 2,82 0,4868 0,3829 2,473 9,111 3,684 2,84 0,4854 0,3765 2,496 9,243 3,704 2,86 0,4840 0,3701 2,518 9,376 3,724 2,88 0,4827 0,3639 2,540 9,510 3,743 2,90 0,4814 0,3577 2,563 9,645 3,763 2,92 0,4801 0,3517 2,586 9,781 3,782 2,94 0,4788 0,3457 2,609 9,918 3,801 2,96 0,4776 0,3398 2,632 10,06 3,820 2,98 0,4764 0,3340 2,656 10,19 3,839 3,00 0,4752 0,3283 2,679 10,33 3,857 3,10 0,4695 0,3012 2,799 11,05 3,947 3,20 0,4644 0,2762 2,922 11,78 4,031 3,30 0,4596 0,2533 3,049 12,54 4,112 3,40 0,4552 0,2322 3,180 13,32 4,188 3,50 0,4512 0,2130 3,315 14,13 4,261 3,60 0,4474 0,1953 3,454 14,95 4,330 3,70 0,4440 0,1792 3,596 15,81 4,395 3,80 0,4407 0,1645 3,743 16,68 4,457 3,90 0,4377 0,1510 3,893 17,58 4,516 4,00 0,4350 0,1388 4,047 18,50 4,571 4,10 0,4324 0,1276 4,205 19,45 4,624 4,20 0,4299 0,1173 4,367 20,41 4,675 4,30 0,4277 0,1080 4,532 21,41 4,723 4,40 0,4255 0,09948 4,702 22,42 4,768 4,50 0,4236 0,09170 4,875 23,46 4,812

<!-- p. 418 -->
M M N y 4,60 0,4217 4,70 0,4199 4,80 0,4183 4,90 0,4167 5,00 0,4152 p0y./p0x 0,08459 0,07809 0,07214 0,06670 0,06172 Ty /.Tx 5,052 5,233 5,418 5,607 5,800 py./px 24,52 25,61 26,71 27,85 29,00 Hy./Hx 4,853 4,893 4,930 4,966 5,000 Tabela 3 – Relações para o escoamento unidimensional, adiabático com atrito, em conduto com seção constante. Linha de Fanno. Gás perfeito com k = 1,4 M p0./p0* T/T* p/p* V/V* fLmáx/Dh 0,00 ∞ 1,200 ∞ 0,0000 ∞ 0,02 28,94 1,200 54,77 0,02191 1778 0,04 14,48 1,200 27,38 0,04381 440,5 0,06 9,666 1,199 18,25 0,06570 193,0 0,08 7,262 1,199 13,68 0,08758 106,7 0,10 5,822 1,198 10,94 0,1094 66,92 0,12 4,864 1,197 9,116 0,1313 45,41 0,14 4,182 1,195 7,809 0,1531 32,51 0,16 3,673 1,194 6,829 0,1748 24,20 0,18 3,278 1,192 6,066 0,1965 18,54 0,20 2,964 1,191 5,456 0,2182 14,53 0,22 2,708 1,189 4,955 0,2398 11,60 0,24 2,496 1,186 4,538 0,2614 9,387 0,26 2,317 1,184 4,185 0,2829 7,688 0,28 2,166 1,182 3,882 0,3044 6,357 0,30 2,035 1,179 3,619 0,3257 5,299 0,32 1,922 1,176 3,389 0,3470 4,447 0,34 1,823 1,173 3,185 0,3682 3,752 0,36 1,736 1,170 3,004 0,3894 3,180 0,38 1,659 1,166 2,842 0,4104 2,706 0,40 1,590 1,163 2,696 0,4313 2,309 0,42 1,529 1,159 2,563 0,4522 1,974 0,44 1,474 1,155 2,443 0,4729 1,692 0,46 1,425 1,151 2,333 0,4936 1,451 0,48 1,380 1,147 2,231 0,5141 1,245 0,50 1,340 1,143 2,138 0,5345 1,069 0,52 1,303 1,138 2,052 0,5548 0,9174 0,54 1,270 1,134 1,972 0,5750 0,7866 0,56 1,240 1,129 1,898 0,5951 0,6736

<!-- p. 419 -->
Tabelas para a solução de escoamentos de fluidos compressíveis z 419 M p0./p0* T/T* p/p* V/V* fLmáx/Dh 0,58 1,213 1,124 1,828 0,6150 0,5757 0,60 1,188 1,119 1,763 0,6348 0,4908 0,62 1,166 1,114 1,703 0,6545 0,4172 0,64 1,145 1,109 1,646 0,6740 0,3533 0,66 1,127 1,104 1,592 0,6934 0,2979 0,68 1,110 1,098 1,541 0,7127 0,2498 0,70 1,094 1,093 1,493 0,7318 0,2081 0,72 1,081 1,087 1,448 0,7508 0,1722 0,74 1,068 1,082 1,405 0,7696 0,1411 0,76 1,057 1,076 1,365 0,7883 0,1145 0,78 1,047 1,070 1,326 0,8068 0,09167 0,80 1,038 1,064 1,289 0,8251 0,07229 0,82 1,030 1,058 1,254 0,8433 0,05593 0,84 1,024 1,052 1,221 0,8614 0,0226 0,86 1,018 1,045 1,189 0,8793 0,03097 0,88 1,013 1,039 1,158 0,8970 0,02180 0,90 1,0089 1,033 1,129 0,9146 0,01451 0,92 1,0056 1,026 1,101 0,9320 0,008913 0,94 1,0031 1,020 1,074 0,9493 0,004815 0,96 1,0014 1,013 1,049 0,9663 0,002057 0,98 1,0003 1,007 1,024 0,9832 0,0004947 1,00 1,0000 1,000 1,000 1,000 0,0000 1,02 1,0003 0,9933 0,9771 1,017 0,0004587 1,04 1,0013 0,9866 0,9551 1,033 0,001769 1,06 1,0029 0,9798 0,9338 1,049 0,003838 1,08 1,0051 0,9730 0,9134 1,065 0,006585 1,10 1,0079 0,9662 0,8936 1,081 0,009935 1,12 1,011 0,9593 0,8745 1,097 0,01382 1,14 1,015 0,9524 0,8561 1,113 0,01819 1,16 1,020 0,9455 0,8383 1,128 0,02298 1,18 1,025 0,9386 0,8210 1,143 0,02814 1,20 1,030 0,9317 0,8044 1,158 0,03364 1,22 1,037 0,9247 0,7882 1,173 0,03942 1,24 1,043 0,9178 0,7726 1,188 0,04547 1,26 1,050 0,9108 0,7574 1,203 0,05174 1,28 1,058 0,9038 0,7427 1,217 0,05820 1,30 1,066 0,8969 0,7285 1,231 0,06483 1,32 1,075 0,8899 0,7147 1,245 0,07161 1,34 1,084 0,8829 0,7012 1,259 0,07850 1,36 1,094 0,8760 0,6882 1,273 0,08550 1,38 1,104 0,8690 0,6755 1,286 0,09259 1,40 1,115 0,8621 0,6632 1,300 0,09974 1,42 1,126 0,8551 0,6512 1,313 0,1069 1,44 1,138 0,8482 0,6396 1,326 0,1142

<!-- p. 420 -->
M p0./p0* 1,46 1,150 1,48 1,163 1,50 1,176 1,52 1,190 1,54 1,204 1,56 1,219 1,58 1,234 1,60 1,250 1,62 1,267 1,64 1,284 1,66 1,301 1,68 1,319 1,70 1,338 1,72 1,357 1,74 1,376 1,76 1,397 1,78 1,418 1,80 1,439 1,82 1,461 1,84 1,484 1,86 1,507 1,88 1,531 1,90 1,555 1,92 1,580 1,94 1,606 1,96 1,633 1,98 1,660 2,00 1,688 2,02 1,716 2,04 1,745 2,06 1,775 2,08 1,806 2,10 1,837 2,12 1,869 2,14 1,902 2,16 1,935 2,18 1,970 2,20 2,005 2,22 2,041 2,24 2,078 2,26 2,115 2,28 2,154 2,30 2,193 2,32 2,233 T/T* 0,8413 0,8345 0,8276 0,8208 0,8139 0,8072 0,8004 0,7937 0,7870 0,7803 0,7736 0,7670 0,7605 0,7539 0,7474 0,7410 0,7345 0,7282 0,7218 0,7155 0,7093 0,7030 0,6969 0,6907 0,6847 0,6786 0,6726 0,6667 0,6608 0,6549 0,6491 0,6433 0,6376 0,6320 0,6263 0,6208 0,6152 0,6098 0,6043 0,5990 0,5936 0,5883 0,5831 0,5779 p/p* 0,6282 0,6172 0,6065 0,5960 0,5858 0,5759 0,5662 0,5568 0,5476 0,5386 0,5299 0,5213 0,5130 0,5048 0,4969 0,4891 0,4815 0,4741 0,4668 0,4597 0,4528 0,4460 0,4394 0,4329 0,4265 0,4203 0,4142 0,4083 0,4024 0,3967 0,3911 0,3856 0,3802 0,3750 0,3698 0,3648 0,3598 0,3549 0,3502 0,3455 0,3409 0,3364 0,3320 0,3277 V/V* 1,339 1,352 1,365 1,377 1,389 1,402 1,414 1,425 1,437 1,449 1,460 1,471 1,482 1,494 1,504 1,515 1,526 1,536 1,546 1,556 1,566 1,576 1,586 1,596 1,605 1,615 1,624 1,633 1,642 1,651 1,660 1,668 1,677 1,685 1,694 1,702 1,710 1,718 1,726 1,734 1,741 1,749 1,756 1,764 fLmáx/Dh 0,1215 0,1288 0,1361 0,1434 0,1506 0,1579 0,1651 0,1724 0,1795 0,1867 0,1938 0,2008 0,2078 0,2147 0,2216 0,2284 0,2352 0,2419 0,2485 0,2551 0,2616 0,2680 0,2743 0,2806 0,2868 0,2930 0,2990 0,3050 0,3109 0,3168 0,3225 0,3282 0,3339 0,3394 0,3449 0,3503 0,3556 0,3609 0,3661 0,3712 0,3763 0,3813 0,3862 0,3911

<!-- p. 421 -->
Tabelas para a solução de escoamentos de fluidos compressíveis z 421 M p0./p0* T/T* p/p* V/V* fLmáx/Dh 2,34 2,274 0,5728 0,3234 1,771 0,3959 2,36 2,316 0,5677 0,3193 1,778 0,4006 2,38 2,359 0,5626 0,3152 1,785 0,4053 2,40 2,403 0,5576 0,3111 1,792 0,4099 2,42 2,448 0,5527 0,3072 1,799 0,4144 2,44 2,494 0,5478 0,3033 1,806 0,4189 2,46 2,540 0,5429 0,2995 1,813 0,4233 2,48 2,588 0,5381 0,2958 1,819 0,4277 2,50 2,637 0,5333 0,2921 1,826 0,4320 2,52 2,687 0,5286 0,2885 1,832 0,4362 2,54 2,737 0,5239 0,2850 1,839 0,4404 2,56 2,789 0,5193 0,2815 1,845 0,4445 2,58 2,842 0,5147 0,2781 1,851 0,4486 2,60 2,896 0,5102 0,2747 1,857 0,4526 2,62 2,951 0,5057 0,2714 1,863 0,4565 2,64 3,007 0,5013 0,2682 1,869 0,4604 2,66 3,065 0,4969 0,2650 1,875 0,4643 2,68 3,123 0,4925 0,2619 1,881 0,4681 2,70 3,183 0,4882 0,2588 1,887 0,4718 2,72 3,244 0,4839 0,2558 1,892 0,4755 2,74 3,306 0,4797 0,2528 1,898 0,4792 2,76 3,370 0,4755 0,2499 1,903 0,4827 2,78 3,434 0,4714 0,2470 1,909 0,4863 2,80 3,500 0,4673 0,2441 1,914 0,4898 2,82 3,567 0,4632 0,2414 1,919 0,4932 2,84 3,636 0,4592 0,2386 1,925 0,4966 2,86 3,706 0,4553 0,2359 1,930 0,5000 2,88 3,777 0,4513 0,2333 1,935 0,5033 2,90 3,850 0,4474 0,2307 1,940 0,5065 2,92 3,924 0,4436 0,2281 1,945 0,5097 2,94 3,999 0,4398 0,2256 1,950 0,5129 2,96 4,076 0,4360 0,2231 1,954 0,5160 2,98 4,155 0,4323 0,2206 1,959 0,5191 3,00 4,235 0,4286 0,2182 1,964 0,5222 3,50 6,79 0,3478 0,1685 2,064 0,5864 4,00 10,72 0,2857 0,1336 2,138 0,6331 4,50 16,56 0,2376 0,1083 2,194 0,6676 5,00 25,00 0,2000 0,08944 2,236 0,6938

<!-- p. 423 -->

# Bibliografia

ÁSSY, T. M. Mecânica dos fluidos. São Paulo: Plêiade, 1996. BALLOFET, A. ; GOTELLI, L. M. & MEOLI, G. A. Mecânica dos fluidos. Buenos Aires: Ediar, 1952. DAUGHERTY, R. L. & FRANZINI, J. B. Fluid mechanics with engineerig applicatios. New York: McGraw-Hill, 1965. HANSEN, A. G. Fluid mechanics. New York: John Wiley & Sons, 1967. HUGHES, W. F. & BRIGHTON, J. A. Theory and problems of fluid dynamics. New York: Schaum, 1967. MARCHI, E. & RUBATTA, A. Meccanica dei fluidi, principi e applicazioni idrauliche. Bologna: Unione Tipográfico – Editrice Torinese, 1981. Notas de aulas da EPUSP, FEI e FEUMC ROUSE, H. Elementary mechanics of fluids. London: John Wiley & Sons, 1946. SCHLICHTING, H. Boundary layer theory. New York: McGraw-Hill, 1960. SHAMES, I. H. Mechanics of fluids. New York: McGraw-Hill, 1962. SHAPIRO, A. H. The Dynamics and thermodynamics of compressible fluid flow. New York: Ronald, 1953. SOKOLNIKOFF, I. S. & REDHEFFER, R. M. Mathematics of physics and modern engineering. McGraw-Hill, New York, 1966. STREETER, V. L. Handbook of fluid dynamics. New York: McGraw-Hill, 1961. ________ . & WYLIE, E. B. Mecânica dos fluidos. São Paulo: McGraw-Hill, 1982. VAN WYLEN, G. J. & SONNTAG, R. E. Fundamentos da termodinâmica clássica. São Paulo: Edgard Blücher, 1976.

<!-- p. 425 -->

# Índice remissivo

A C Aceleração, 3, 64, 65, 66, 232, 321, 400 local, 78 Aerodinâmico corpo, 235 Aerofólio, 237, 238 Alargamento brusco, 404 Área transversal,164 Arrasto (ou arraste), 208, 223, 237, 238, 239, 398, 399, 400, 408 de forma ou de pressão, 229, 232, 233, 235 de superfície, 228, 229, 230, 235 em cilindro, 232, 233 em esfera, 324, 235 B Barômetro, 2526, 63 Bocal bloqueado, 363, 373, 381, 408 choque normal em, 363-374 convergente, 217, 354, 355, 359, 362, 373, 389, 390, 391 convergente / divergente, 362, 373, 374, 389, 390, 391 medida de vazão em, 234, 235 Bomba carga ou altura manométrica da, 91, 270 Bordo de ataque, 165, 229, 230, 231, 240 Bordo de fuga, 231, 240 Bourdon manômetro de, 6 Bulbo, 339 Calores específicos a pressão constante, 330, 383 a volume constante, 330 Camada limite noção de, 164 em conduto forçado , 166 – 168, 15 em placa plana,164, 165, 166, 229, 232, 233, 235, 238 espessura da, 166, 229, 399 laminar, 166, 167 turbulenta, 166, 167 Campo de velocidade, 78, 290, 302, 320, 321, 324, 325 Carga cinética, 89, 91, 92, 115, 117, 119 de pressão, 22, 23, 24, 27, 34, 89, 91, manométrica, 91, 93, 156, 158, 160, 161, 394, 400, 401 potencial, 89, 91 Cargas singulares, perdas de, 168, 169, 176, 182, 184 Cavitação, 188, 189, 202 Centro das pressões, 30, 32, 34 Choque normal definição, 364 equações básicas, 365 Cinemática da partícula, 376 dos fluidos, 67 viscosidade, 9, 10, 142, 156, 208, 239, 403, 407 Circulação, 237, 307

<!-- p. 426 -->
Cisalhamento, tensão da (ver também Lei de Newfunção de, 300, 302, 323, 324, 325, ton da viscosidade), 3, 4, 12, 81, 82, , 224, 325, linha de, 70, 224, 300, 301, 303, , 322 399 tubo de, 70, 85, 97, 225, 242, 262, 336, 264, 376 Coeficiente Cotovelo, 133, 169, 185, 201, 204, 396 adimensional, 184, 214, 227, 228 Crítico fluidodinâmico, 227 estado, 355, 363, 384 da energia cinética, 99, 116, 256, 402 seção, 359, 360, 374, 375, 385, 387 de arrasto, 151, 153, 234, 239, 398, 400, 408 de compressibilidade ,342, 344, 383 D de descarga ou vazão, 219, 221, 222, 346, 383 de sustentação , 237, 241 Deformação de velocidade, 212, 220, 221, 404 angular, 285 de contração , 212, 220 linear, 284, 286 de vazão ou de descarga156, 213, 345 Densímetro, 62, 207, 218 Colebrook,176 Derivada Coluna piezométrica ou piezômetro, 27 convectiva, 282 Componente local, 252, 282, horizonal, 35, 36 total, 249, 281, 282, 283 vertical, 36 Descolamento, 217, 232, 233, 234, 235 Comprimento equivalente, 185, 186, 198, 396, Desviador de jato fixo, 126 404 Diafragma, 211, 233 Conduto com redução gradual da seção, 124 Diagrama Condutos forçados, 163, 166 de Moddy-Rouse, 179, 182, 187, 190, 194 Condutos industriais, 176 de velocidades, 3 14, 78, 82, 97, 115, 167, 210, Colebrook, 176 314, 326 Moody, 176 linear, 6, 7, 12, 13, 74 Rouse, 176 Diâmetro hidráulico, 164, 173, 176, 378 Constante Dilatação volumétrica adiabática, 11, 330, 383 dilatação linear, 286 do gás, 329 universal, 330, 383 Continuidade equação da, 74, 90, 169, 183, 190247, 302, 317, , 331, 332, , 369 Dimensional, análise, 5, 8, 9, 69, 141, 150 173, 184, 275, 351 Dinamômetro, 145, 146, 228, 239, 387, 406 Dipolo, 307, 308, 309, 311 Distribuída Controle superfície de, 244, 245, 247, 254 volume de, 106, , 251, 252, 254, 255, 275 coficiente de perda de carga, 197, 198, 202, 391, 403, 406 Duas placas, experiência das, 2, 3, 4 Coordenadas cartesianas, 77, 276, 282, 303, 208, 313 E cilíndricas,48, 267, 277, , 293, 303, 306, 313 naturais, 303 Corda interna,237 externa, 237 Corpo totalmente submerso ,37, 38, 39, 40, 153 parcialmente submerso,38, 40 Corrente Empuxo, 36, 37, 39, 40, 61, 136, 157, 206, 224 Energia cinética específica, 255, 328 potencial específica, 255, 328 de pressão, 86, 104, 226, 233, 328, 356 interna, 105, 255, 338, 382, 383 cinética, 86, 99, 141, 209, 225, 327, 356, 402 de pressão, 86, 104, 226, 339, 356

<!-- p. 427 -->
Índice remissivo z 427 equação da, 85, 90-106, 163, , 190, 209, 211, 319, 328, 370 interna, 105, 255, 256, 327, 382, 383 potencial, 85, 88, 194, 255, 328, 333, 338 Energias mecânicas associadas a um fluido Energia potencial (Ep), 85, 88, 194, 255, 338 PHR (Plano Horizontal de Referência), 85, 86, 90, 170, 188, 190 Energia cinética (Ec), 86, 88, 90, 141, 209, 327, 402 tipos de, 85 Entalpia, 106, 120, 327, 328 338, 383 Entropia variação de, 329, 334, 351 Equação de estado dos gases, 10, manométrica , 28, 29, 90, 209, 215, 342 da continuidade, 74, 85, 90, 195, 225, 290, 302, 352, 369 de Bernoulli, 87, 88, 100, 296, 311, 323, 339 dimensional, 142, 143, 144, 147, 148, 149 da energia geral para volume de controle, 254 para volume de controle acelerado, 262 do momento da quantidade de movimento , 265 da continuidade na forma diferencial, 287 de Euler, 289, 291, 293, 296, 312, 313, 323 de Navier-Stokes, 312, 313, 319 da energia, 85, 87, 190, 272, 319, 328, 352, 364, 370 de estado, 10, 290, 366, 370, 377, 382 da continuidade, 74, 190, 287, 331, 360, 365, 369 da energia, 85, 99, 100, 182, 195, 272, 338, 346, 370 da quantidade de movimento, 78, 172, 258, 365, 370, 377 de Bernoull, 87, 224, 225, 273, 296, 339 de estado, 10, 290, 329, 334, 365, 366, 382 de Laplace, 303 da energia para fluido real, 95 Equilíbrio relativo, 43, 291 Equipotenciais, linhas, 303 Equivalente, comprimento, 185, 186, 198, 396, 404 Escala absoluta, 10, 23, 24, 25, 52, 188, 191, 329 Escalas de semelhança, 152 Escoamento laminar, 69, 78, 100, 240, 314, 316, 317, 318, 319, 325, 397 turbulento, 69, 78, 115, 166, 275 de transição, 68, 69 uniforme, 97, 98, 165, 205, 305, 309, 310, 311, 323 incompressível, 10, 337, 344 sônico, 337, 354 supersônico, 337, 371, 373 isoentrópico, 343, 384, 385, 386, 387, 388, 391, 406 unidimensional, 71, 328, 351, 411, 418 de Fanno, 376, 381, 382 de Rayleigh, 382 adiabático, 104, 294, 352, 370, 376 bidimensional, 71, 73, 81, 84, 223, 298, 300, 316 compressível, 335 em condutos, 164, 165 irrotacional, 296, 297, 305, 306, 314, 321 na camada limite, 166 permanente, 108 sem atrito, 334 subsônico, 337, 341, 369, 371, 373, 383 tridimensional, 71 turbulento, 68, 69, 78, 168, 202, 210, 275, 312 variado ou variável, 351 Específico calor, 103, 382 massa, 8, 9, 100, 208, 327, 387, 403, 409 peso, 8, 19, 28, 30, 128, 396, 397 Estabilidade vertical, 38 à rotação, 39 Estabilidade, 38, 39, 41, 409 Estado crítico, 355, 363, 384 de estagnação, 338, 373, 375, 379, 388 equação de, 10, 290, 365, 366, 370, 377, 382 Estática dos fluidos, 43, 206, 291 Esteira, 232, 233 Experiência de Reynolds, 68, 69 F Fanno, linha de, 370, 377, 381, 418

<!-- p. 428 -->
FLT (força, comprimento e tempo), 5, 8, 141, 142, 147, 148, 156 Fluido barotrópico, 294 definição de, 1 ideal, 10, 87, 94, 95, 107, 296, 322, 325 incompressível, 10, 91, 95, 100, 102, 125 newtoniano, 4 Fluidodinâmica, 223, 228 Flutuador, 37-41 Fluxo de calor, 104, 105, 119, 120, 255, 256, 402 Fonte ou sorvedouro, 306, 307, 308, 232 Força elementar, 32, em superfícies reversas submersas, 35 numa superfície plana submersa, 30 em superfícies sólidas em movimento, 127 pressão, 172, 255, 289, 323 de sustentação, 223, 237, 238 de arrasto, 144, 146, 148, 228,230, 231240, 398 de inércia, 46, 291 de sustentação, 223, 237, 238 de arrasto total, 234 Formação de vapor, 188 Fórmula da perda de carga distribuída, 173 Froude, número de (Fr), 151, 153 Função de corrente, 30, 302, 323, 324, 325 potencial, 306, 324 G Gás perfeito, 10, 294, 327, 344, 351, 415, 418 Gradiente adverso de pressões, 232, 233, 235 da velocidade, 3, 15, 81, 116, 229, 230 Grandezas fundamentais e derivadas, 141 H Hidrostática, distribuição, 296, 297 I Inércia, momento de, 32, 41 Interna, energia, 105, 255, 256, 327, 382, 383 Interpretação da perda de carga, 102 Irreversibilidade, 329, 351, 367, 368, 389 Irrotacional, escoamento, 296, 297, 305, 306, 314, 321 Isoentrópico, escoamento, 343, 345, 360, 388, 391, 406 J Jato incidindo numa placa plana, 127 L Laminar, escoamento em placa plana, 166, 267, 168 em tubos, 167, 175, 318 entre placas paralelas, 315 Linha(s) da energia, 171, 191, 192 de corrente, 69, 70, 280, 298, 303, 310 equicorrentes, 303, 304, 310 equipotenciais303, 304, 310 piezométrica, 171, 172, 173, 191, 192 M Mach cone de, 349, 350 número de, 105, 151, 337, 348, 381, 383, 406 Manômetro com tubo em U, 27, de Bourdon, 26 Manuais de hidráulica, 184 Máquina hidráulica, 120, 188 Massa específica, 8, 9, 67, 146, 206, 207, 245, 247, 321, 400, 403, 409 Medida de massa específica, 296, 207 de vazão, 211-216, 218 de velocidade, 208-211, 341 de viscosidade, 207,208 em canais abertos, 218 Medidores volumétricos, 218 Meio, 242, 244, 245, 254, 2255, 259 Metacentro, 40 Método euleriano, 245, 248, 249 lagrangeano, 243, 243, 245, 248, 249 de utilização da equação

<!-- p. 429 -->
Índice remissivo z 429 MK*S, 3, 5, 8, 9, 11, 94, 143 MLT (massa, comprimento e tempo), 141, 143, 156 Momento da quantidade de movimento, 265-270 de inércia, 32, 41 Moody-Rouse, diagama de, 179, 182, 187, 190, 194 Movimento aleatório macroscópico, 69 N Nabla, 282 Natural, sistema de coordenadas, 48, 266, 280, 296 Navier-Stokes equação de, 312, 131, 319 aplicação da equação de, 313 Newton, lei de, da viscosidade, 3, 4, 5, 312, 318 Nikuradse experiência de, 174, 175, 176 forças viscosas, 174 Normal, onda de choque NPSH, 189 Número de Euler, 151, 153 de Froude, 151 de Mach, 105, 151, 227, 380, 381, 391, 406 de Reynolds, 69, 81, 144, 155, 184, 214, 231, 404 Números adimensionais, 144,145, 146, 153, 155, 157,162 na pesquisa de uma lei física, 144 típicos, 150 O Onda de choque equacionamento matemático da, 364 irreversibilidade, 367, 389 interpretação gráfica da, 369 normal, 363, 369, 373, 374, 389, 391, 415 Orifício de bordo delgado, 157, 211, 220, 384 P Partícula fluida, 275, 276, 284 Pascal, lei de, 21, 22 Perda distribuída, 179, 185, 190 Perda de carga distribuída, 168, 169, 186, 391, 406, 407 de carga singular, 176, 184, 202, 204, 205, 398 interpretação da, 102 distribuída, 179, 185, 190 locais ou singulares, 168 Perímetro molhado, 164, 377 Peso específico relativo para líquidos, 9 Piezômetro, 27, 65, 111, 113, 170, 208, 209, 221 Pitot, tubo de, 107, 108, 208, 219, 221, 385, 387, 408 Poise, 5, 11 Poiselle, 315 Ponto de estagnação, 209, 235, 323 em repouso, 347, 348 emissor com movimento sônico, 348 com movimento subsônico, 348 com movimento supersônico, 349 Potência da máquina, 92, 93, 113, 188, 203, 205, 397 do fluido, 92, 96, 100 Prensa hidráulica, 22, Pressão(ões) absoluta, 10, 23, 50, 56 carga de, 22, 23, 24, 27, 34, 89, 91 centro das, 30, 32, 34 de estagnação, 358, 368, 369, 375, 385, 391 de vapor, 25, , 188 dinâmica, 209, 221, 225 efetiva, 23, 30, 34, 92, 156, 196 escalas de, 23 na escala absoluta, 23, 25, 329, em torno de um ponto de um fluido em repouso, 20 atmosférica, 23, 92, 94, 126, 183, 261, 404, 408 unidades de, 24, 50 medidores de, 26, 206 barométrica, 24 Princípio da ação e reação, 121, 124, 260, 268 da aderência, 2, 3, 97, 165, 167, 318, 327 da conservação da energia de Arquimedes, 37 de d’Alambert, 44

<!-- p. 430 -->
Processo reversível, 329, 351 adiabático, 351 Propriedades extensivas, 252 intensivas, 252, 253 Q Quantidade de movimento, 78, 121, 242, 259, 265, 334, 336, 370, 377 R Raio hidráulico, 164 Rayleigh, 371, 382 Recalque, instalações de, 187 Recipiente com movimento de translação uniformemente acelerado segundo a horizontal, 43 com movimento de translação uniformemente acelerado segundo a vertical, 46 com movimento de translação uniformemente acelerado ao longo de um plano inclinado, 46 com movimento de rotação de velocidade angular ù constante, 48 Redução de seção e mudança de direção, 125 Regime (ou movimentos)

variado, 244, 245, 247, 260, 272, 336 permanente67, 79, 85, 120, 130, 268, 392, 406 laminar , 204 Relações entre escalas, 152 Rendimento noção de, 92 de bomba, 93 de turbina, 94 Reservatório de grandes dimensões, 67, 188, 356, 361, 390, 406, 410 Reynolds experiência de, 68 número de, 69, 81, 144, 214 234, 404 Rotacional, 295, 296, 321, 324 Rotâmetro, 217, 218 Rugosidade, 168, 169, 172, 174, 175, 176 S Saybolt, viscosímetro, 208 Semelhança (ou teoria dos modelos) Simplificação prática, 5 Sistema MK*S, 3, 5, 8, 9, 11, 94, 143 MKS Gioggi ou SI, 5, 8, 9, 143 CGS, 3, 5, 8, 9, 11, 143, 144 coerentes de unidades, 143 Som, velocidade do, 105, 150, 334, 348, 354 Sônico, 151, 338, 349, 350, 355 Sorvedouro, 306, 307, 308, 324 Stevin, teorema de, 19, 22, 28, 30, 291, 292, 314 Stoke, 9 Subsônico, 151, 361, 371, 372, 381, 383 Superfície de controle, 244, 245, 247, 254 Supersônico, 151, 337, 350, 363, 368, 375, 390 Sustentação, 223, 226, 238, 240, 241 T Temperatura absoluta, 10, 329 de estagnação, 339, 364, 376, 383, 385, 388 Tensão de cisalhamento, 3, 4, 12, 81, 82, 229, 325, 399 Teorema dos ð , 147, 155, 159, 16, 403 Termodinâmica, primeira lei da, 106, 254 Termômetro, 339, 383,385, 392, 410 Trajetórias e linhas de corrente, 69, 278 Tridimensional, escoamento, 71 Tubos de corrente, 70 Turbina, 87, 91, 130, 130, 134, 136, 139, , 204, 254, 394 Turbulento, escoamento, 69, 69, 78, 100, 202, 210, 275, 312 U Unidimensional, escoamento, 71, 73, 327, 351, 411, 418 Uniforme, diagrama de velocidade, 108 V Válvula de gaveta, 185, 186 tipo globo, 185, 186 de pé com crivo, 187 de retenção, 185, 187
