"""Gera o baralho Anki do TCC (v20) como texto importável: docs/Anki_TCC_v20.txt.
No Anki: Arquivo → Importar → escolher o arquivo. Os cabeçalhos #... já dizem separador,
HTML, tipo de nota (Básico), baralho e coluna de etiquetas. Fórmulas em MathJax: \\( ... \\)."""
from pathlib import Path

C = []   # (frente, verso, etiqueta)


def card(tag, frente, verso):
    C.append((frente, verso, tag))


# ---------------- 01 Problema e objetivos ----------------
t = "01_problema"
card(t, "Qual é o problema do TCC, em uma frase?",
     "Manter a pressão da barra perto da referência enquanto os bicos abrem e fecham um a um, numa barra com alimentação em série, usando uma válvula de alívio como atuador.")
card(t, "Por que a pressão sobe quando um bico fecha?",
     "Todos os bicos são alimentados pela mesma mangueira. Quando um fecha, sobra líquido na linha e a capacidade de saída diminui; a pressão sobe até a fonte entregar uma vazão que caiba nas saídas restantes.")
card(t, "Quanto a pressão sobe na bancada de Rosa et al. (2019), de 7 para 1 bico, com a válvula fechada?",
     "De 3,57 para 5,58 kgf/cm², cerca de 56% (Tabela 1).")
card(t, "Se a pressão sobe 56%, quanto sobe a vazão de cada bico aberto? Por quê?",
     "Cerca de 25%, porque a vazão varia com a raiz da pressão: \\(\\sqrt{1{,}56} \\approx 1{,}25\\).")
card(t, "Qual é a hipótese do trabalho?",
     "Um modelo de resistências fluídicas (bicos em paralelo, curva da bomba, válvula de alívio) mais a dinâmica da válvula basta para projetar um controlador simples que mantenha a pressão em ±10% da referência durante as trocas de bicos.")
card(t, "A hipótese foi confirmada?",
     "<b>Em parte, e só em simulação.</b> O PI atende nas trocas de um bico e na maior parte da troca aleatória, mas não quando três bicos fecham juntos.")
card(t, "Por que controlar a pressão e não a vazão?",
     "A pressão é a mesma para todos os bicos (H2). Segurando a pressão, segura-se a vazão de todos ao mesmo tempo, já que \\(Q = K\\sqrt{P}\\).")
card(t, "Por que a válvula de alívio como atuador, e não a rotação da bomba?",
     "É o atuador da bancada de referência, e há um ensaio medido do efeito dela (Tabela 2). A rotação da bomba exigiria modelar motor e inversor, sem dados publicados para conferir.")
card(t, "Quais são os cinco objetivos específicos?",
     "1) modelar pressão × vazão × nº de bicos, com fonte e válvula; 2) acrescentar a dinâmica da válvula; 3) sintonizar P e PI por alocação de polos; 4) acrescentar o <i>feedforward</i>; 5) comparar os três em simulação com métricas.")

# ---------------- 02 Fundamentos e modelo estático ----------------
t = "02_modelo_estatico"
card(t, "O que diz a lei de orifício? De onde ela vem?",
     "\\(Q = K\\sqrt{\\Delta P}\\): a vazão é proporcional à raiz da queda de pressão. Sai de Bernoulli + continuidade, com o coeficiente de descarga \\(C_D\\) (Brunetti, 2008, p. 212–213; Eq. 2.3).")
card(t, "O que é o coeficiente de descarga \\(C_D\\)?",
     "A razão entre a vazão real e a teórica (0 &lt; C_D &lt; 1). Reúne a veia contraída e as perdas por atrito. No trabalho ele fica dentro da constante \\(K\\).")
card(t, "O que é resistência fluídica?",
     "\\(\\Delta P = R_F\\,Q^2\\) (Eq. 2.4): a queda de pressão é proporcional ao quadrado da vazão. Dobrar a vazão quadruplica a queda.")
card(t, "Qual é a resistência equivalente de \\(n\\) bicos iguais em paralelo?",
     "\\(R_{eq} = R_1/n^2\\) (Eqs. 2.6 e 3.4), com \\(R_1 = 1/K^2\\). Dobrar o número de bicos abertos divide a resistência por quatro.")
card(t, "Qual a vantagem do modelo \\(R_1/n^2\\) sobre a fórmula de Rosa (Eq. 2.5)?",
     "Usa <b>um</b> parâmetro físico (a constante do bico) em vez de <b>quatro</b> coeficientes empíricos, e vale para qualquer número de bicos iguais. O erro relativo máximo é 5,9%, contra 18,5% da fórmula em n = 7.")
card(t, "Onde \\(R_1/n^2\\) é usado no controle e no simulador?",
     "Na forma \\(R_1/n^2\\), só na validação (Tabela 5, Figura 16). Nas contas, a mesma lei aparece como \\(Q_{barra} = nK\\sqrt{P}\\): no simulador (\\(C = nK + K_{v,max}\\alpha\\)), no <i>feedforward</i> (0,121 por bico), em \\(K_n = K\\,dP/dC\\) e no \\(K_g\\) independente de n.")
card(t, "Qual é a equação do balanço de vazões no nó (Eq. 3.10)?",
     "\\(Q_s(P) = [nK + K_v(\\alpha)]\\sqrt{P}\\): tudo o que a fonte entrega sai pelos bicos ou pela válvula (continuidade).")
card(t, "O que é a capacidade de saída \\(C\\)?",
     "\\(C = nK + K_{v,max}\\,\\alpha\\): bicos abertos mais válvula. A pressão depende de \\(n\\) e \\(\\alpha\\) <b>só através de C</b> (Eq. 3.11).")
card(t, "Como foi obtida a constante do bico \\(K\\) e quanto vale?",
     "Média de \\(Q/(n\\sqrt{P})\\) nos sete pontos da Tabela 1 (Eq. 3.2): \\(K\\) = 0,425 (L/min)/√(kgf/cm²). Os sete valores ficam entre 0,418 e 0,436.")
card(t, "Como a fonte (bomba + PCV) foi modelada?",
     "Por uma parábola \\(P = a_2Q_s^2 + a_1Q_s + a_0\\) ajustada por mínimos quadrados (Chapra, p. 393): \\(a_2\\) = −0,0355, \\(a_1\\) = −0,2018, \\(a_0\\) = 5,815. RMSE 0,006 kgf/cm²; uma reta teria erro 12× maior.")
card(t, "Por que a vazão da bomba de pistão cai quando os bicos fecham?",
     "Por causa da PCV, a válvula de controle de pressão por mola do conjunto da bomba, que devolve ao tanque a vazão que a barra não usa (Merritt, p. 321 e 337).")
card(t, "Como o programa resolve a pressão de equilíbrio?",
     "Por bissecção da Eq. (3.10) no intervalo [0, \\(a_0\\)], 100 repetições (Chapra, p. 101–102). Coincide com a forma explícita (3.11) com erro menor que 10⁻¹⁴.")
card(t, "Quanto o modelo estático acerta?",
     "Erro máximo de 0,7% na pressão e 2,3% na vazão. Na validação cruzada (deixa um de fora): 0,9% e 2,7%.")
card(t, "O que é a validação cruzada <i>leave-one-out</i>?",
     "Para cada um dos 7 pontos, ajusta-se \\(K\\) e a fonte com os outros 6 e prevê-se o ponto que ficou de fora. Mostra que o modelo prevê, não só decora.")
card(t, "Por que \\(K\\) dá 0,86 L/min a 4 bar, 7% abaixo dos 0,92 do catálogo?",
     "Explicação possível: perda de pressão na solenoide e no antigotejo, entre o sensor e a ponta. O bico trabalha com pressão um pouco menor que a medida.")

# ---------------- 03 Hipóteses e dinâmica ----------------
t = "03_hipoteses_dinamica"
card(t, "Cite as hipóteses H1 a H6.",
     "H1 escoamento permanente, incompressível, barra horizontal; H2 mesma pressão em todos os bicos; H3 bicos iguais com lei de orifício; H4 fonte como curva de 2º grau; H5 válvula linear; H6 pressão instantânea.")
card(t, "Por que H2 (mesma pressão em todos os bicos) é aceitável?",
     "Os sensores do começo e do fim da barra (PT-01 e PT-02) marcaram valores quase iguais, com vazão pequena (no máx. 5,6 L/min). Na análise dinâmica é comum considerar só as restrições intencionais (Merritt, p. 52).")
card(t, "Qual hipótese é estimativa e por quê?",
     "H5 (válvula linear) e os parâmetros \\(\\tau_a\\) e \\(\\omega_{max}\\): a curva e a velocidade da válvula não estão nas fontes consultadas.")
card(t, "O que diz H6 e como foi conferida?",
     "A pressão se ajusta na hora à válvula e aos bicos. Conferida com um modelo que inclui a capacitância da mangueira, \\((V/\\beta)\\,dP/dt\\) (Merritt, p. 53): o tempo fora da faixa mudou no máximo 0,4 p.p.")
card(t, "Qual é o modelo da válvula?",
     "Primeira ordem, \\(d\\alpha/dt = (\\alpha_c - \\alpha)/\\tau_a\\) (Eq. 3.12), com velocidade limitada a \\(\\omega_{max}\\) e abertura entre 0 e 1. \\(\\tau_a\\) = 0,2 s, \\(\\omega_{max}\\) = 0,5 s⁻¹ (curso total em 2 s).")
card(t, "O que significa a constante de tempo \\(\\tau_a\\)?",
     "Em \\(\\tau_a\\) a válvula percorre 63,2% da mudança; em \\(4\\tau_a\\) (0,8 s) fica a 2% do final (Ogata, p. 147; Castrucci, seção 3.4).")
card(t, "Como o tempo avança no simulador?",
     "Método de Euler com \\(\\Delta t\\) = 1 ms (Eq. 3.13; Chapra, p. 588). Com 2 ms o tempo fora muda 0,1 p.p.; com 10 ms muda 0,8 p.p.")
card(t, "Resuma o modelo dinâmico em uma frase.",
     "A pressão responde na hora (modelo estático a cada passo); quem demora é o motor da válvula.")

# ---------------- 04 Ganhos e feedforward ----------------
t = "04_ganhos_feedforward"
card(t, "O que é a abertura de equilíbrio \\(\\alpha_{ff}(n)\\)?",
     "A abertura que mantém \\(P = P_{ref}\\) com \\(n\\) bicos, isolando \\(\\alpha\\) na Eq. (3.10) (Eq. 3.14). \\(\\alpha_{ff}(7)\\) = 0,023 e \\(\\alpha_{ff}(1)\\) = 0,752.")
card(t, "Quanto a válvula precisa abrir para cada bico que fecha? Por quê?",
     "\\(K/K_{v,max}\\) = 0,425/3,5 = 0,121, porque o líquido que saía pelo bico agora precisa sair pela válvula.")
card(t, "Por que \\(\\alpha_0\\) = 0,023 é tão pequeno?",
     "Porque \\(P_{ref}\\) = 3,5 kgf/cm² está logo abaixo dos 3,56 que a fonte sustenta com sete bicos e a válvula fechada.")
card(t, "Por que \\(P_{ref}\\) = 3,5 kgf/cm²?",
     "A válvula de alívio só <b>baixa</b> a pressão. A referência precisa ficar abaixo do máximo com sete bicos (3,56). 4,0 não seria atingível com 6 ou 7 bicos.")
card(t, "Por que é preciso calcular o ganho da planta \\(K_g\\)?",
     "O controlador age na abertura, não na pressão; \\(K_g\\) traduz abertura em pressão. Ele 1) dá o sentido da correção (\\(K_g\\) &lt; 0 → \\(e = P - P_{ref}\\)); 2) forma o ganho de malha \\(K_c|K_g|\\) = 2,2, que define o erro do P (Eq. 2.9); 3) está nas fórmulas da sintonia (Eqs. 3.31 e 3.32). Sem \\(K_g\\) não dá para calcular \\(K_c\\).")
card(t, "Por que não se escolhe \\(K_c\\) sozinho?",
     "Quem define a resposta é o produto adimensional \\(K_c|K_g|\\) (\\(K_c\\) em (kgf/cm²)⁻¹, \\(K_g\\) em kgf/cm²). O mesmo \\(K_c\\) numa planta com \\(K_g\\) duas vezes maior daria uma malha duas vezes mais forte.")
card(t, "Como \\(K_g\\) e \\(K_n\\) são calculados na v20?",
     "Por derivada implícita do equilíbrio \\(F(P,C) = Q_s(P) - C\\sqrt{P} = 0\\): \\(dP/dC\\) (Eq. 3.15), depois \\(K_g = K_{v,max}\\,dP/dC\\) e \\(K_n = K\\,dP/dC\\) (Eqs. 3.16 e 3.17). A diferença centrada fica só como conferência.")
card(t, "Escreva \\(dP/dC\\) e diga quanto vale.",
     "\\(\\dfrac{dP}{dC} = \\dfrac{-\\sqrt{P}}{C/(2\\sqrt{P}) - dQ_s/dP} = \\dfrac{-1{,}871}{0{,}817 + 1{,}645} = -0{,}760\\)")
card(t, "O que significam os dois termos do denominador de \\(dP/dC\\)?",
     "Quando a pressão sobe: as saídas deixam passar mais (\\(C/2\\sqrt{P}\\) = 0,817) e a fonte entrega menos (\\(-dQ_s/dP\\) = 1,645). Os dois ajudam o nó a voltar ao equilíbrio.")
card(t, "Quanto valem \\(K_g\\) e \\(K_n\\) e o que significam?",
     "\\(K_g\\) = −2,66 kgf/cm² por unidade de abertura (abrir 0,01 baixa 0,027 kgf/cm²). \\(K_n\\) = −0,323 kgf/cm² por bico. Negativos: abrir válvula ou bico baixa a pressão.")
card(t, "Por que \\(K_g\\) não depende do número de bicos?",
     "Em \\(P_{ref}\\), \\(C\\) vale sempre 3,057 (a válvula compensa o bico), então \\(dP/dC\\) não muda. Consequência: <b>uma única sintonia serve para qualquer n</b>.")
card(t, "Onde o modelo da fonte entra no controle?",
     "1) em \\(K_g\\) e \\(K_n\\): o termo da fonte é ~2/3 do denominador de \\(dP/dC\\); 2) no <i>feedforward</i> e em \\(\\alpha_0\\) (\\(Q_s(P_{ref})\\)); 3) na escolha de \\(P_{ref}\\); 4) na escolha de \\(K_{v,max}\\); 5) no simulador, a cada 1 ms.")
card(t, "Se a bomba desse vazão constante, o que mudaria em \\(K_g\\)?",
     "\\(dQ_s/dP = 0\\) → \\(dP/dC\\) = −1,871/0,817 = −2,29 → \\(K_g\\) ≈ −8,0, três vezes maior; a sintonia seria outra. (Conta para resposta oral, não está no texto.)")

# ---------------- 05 Controladores ----------------
t = "05_controladores"
card(t, "Por que o erro é definido como \\(e = P - P_{ref}\\), ao contrário do usual?",
     "Porque pressão acima da referência pede <b>abrir</b> a válvula, e abrir a válvula diminui a pressão (\\(K_g\\) &lt; 0).")
card(t, "Qual é a lei de controle completa (Eq. 3.18)?",
     "\\(\\alpha_c = \\alpha_{ff}(n) + K_c\\left[e + \\frac{1}{T_i}\\int e\\,dt\\right]\\)")
card(t, "Como os três controladores saem da Eq. (3.18)?",
     "P: sem integral, base fixa \\(\\alpha_0\\). PI: com integral, base \\(\\alpha_0\\). PI+FF: a equação completa, com \\(\\alpha_{ff}(n)\\).")
card(t, "O que a ação proporcional faz e qual é o seu defeito?",
     "Corrige proporcional ao erro de agora, rápido. Sozinha deixa erro em regime: \\(e_{reg} = d/(1 + K_c|K_g|)\\) (Eq. 2.9; Castrucci, seção 3.11.3).")
card(t, "Por que a ação integral elimina o erro em regime?",
     "Ela acumula o erro e só para de mudar o comando quando o erro zera; aí mantém a válvula na posição certa.")
card(t, "Por que não foi usada a ação derivativa?",
     "1) amplifica ruído (Ogata, p. 159); 2) os saltos de pressão nas trocas dariam picos no comando (Ogata, p. 541); 3) com o PI, \\(K_c\\) e \\(T_i\\) já colocam os dois polos onde se quer.")
card(t, "Como a integral é calculada no programa?",
     "Soma de retângulos a cada 1 ms, \\(I_k = I_{k-1} + e_k\\,\\Delta t\\) (Eq. 3.19): retangular para trás (Chapra, p. 493; Castrucci, seção 12.2.2).")
card(t, "O que significa o tempo integral \\(T_i\\) = 0,084 s?",
     "Com erro constante, depois de \\(T_i\\) a parcela integral iguala a proporcional. \\(T_i\\) pequeno = ação integral forte.")
card(t, "O que é <i>windup</i>?",
     "Durante a saturação do atuador o erro demora a cair e a integral acumula demais; quando o atuador volta, a saída passa da referência e demora a acomodar (Castrucci, seção 6.3.4).")
card(t, "Qual anti-windup foi usado?",
     "Integração condicional (Fernandes; Goldemberg, 2001): o integrador para quando o comando está em 0 ou 1 e o erro pede para ir além (Eq. 2.13). Só no limite de posição.")
card(t, "Quanto o anti-windup importa?",
     "Sem ele, o C3 do PI iria de 8,3% para 29% fora da faixa. Estendido ao limite de velocidade, cairia para 3,2% (teste à parte).")
card(t, "O que é o <i>feedforward</i> e qual a condição para usá-lo?",
     "Comando calculado pela perturbação medida, antes de o erro aparecer. Exige perturbação medida (o sistema sabe quantos bicos estão abertos) e modelo preciso. É somado à realimentação, que corrige o resto (Castrucci, seção 7.8).")

# ---------------- 06 Laplace ----------------
t = "06_laplace"
card(t, "Por que foi preciso linearizar o modelo?",
     "A função de transferência só vale para sistemas lineares, e o modelo tem a raiz da lei de orifício e a curva da fonte. Cada relação foi trocada pela reta tangente no ponto de operação (Castrucci, seção 9.10.1).")
card(t, "Qual é o ponto de operação da linearização?",
     "Sete bicos, \\(P = P_{ref}\\) = 3,5 kgf/cm², \\(\\alpha_0\\) = 0,023, \\(C\\) = 3,057, \\(Q_s\\) = 5,72 L/min. Válvula sem limite de velocidade.")
card(t, "Quantas entradas tem a malha linear da v20? Por quê?",
     "Uma: o número de bicos \\(\\Delta N\\). A referência é fixa (\\(\\Delta P_{ref} = 0\\)) — caso de perturbação em degrau com referência nula (Castrucci, seção 3.11.3).")
card(t, "Quais são os blocos da Figura 13?",
     "Planta \\(\\Delta P = K_g\\Delta A + K_n\\Delta N\\) (3.21); válvula \\(1/(\\tau_a s + 1)\\) (3.22); PI \\(K_c(1 + 1/T_i s)\\) (3.23); <i>feedforward</i> \\(-K_n/K_g\\); realimentação direta.")
card(t, "O que é o ganho de malha \\(L(s)\\)?",
     "O produto dos blocos ao longo da malha: \\(L(s) = G_c(s)\\,|K_g|/(\\tau_a s + 1)\\).")
card(t, "Qual é a função de transferência da pressão aos bicos (Eq. 3.26)?",
     "\\(T_n(s) = \\dfrac{K_n}{1 + L(s)}\\) (Ogata, p. 22)")
card(t, "Escreva \\(T_{n,PI}(s)\\) (Eq. 3.28).",
     "\\(\\dfrac{K_n T_i s(\\tau_a s + 1)}{\\tau_a T_i s^2 + T_i(1 + K_c|K_g|)s + K_c|K_g|}\\)")
card(t, "Qual o <i>feedforward</i> ideal e como fica aqui?",
     "\\(F(s) = -G_2(s)/G_p(s)\\) (Castrucci, seção 7.8.1, Eq. 7.51). Com \\(G_2 = K_n\\) e \\(G_p = K_g\\): \\(\\Delta A_{ff} = -(K_n/K_g)\\Delta N\\), +0,121 por bico que fecha.")
card(t, "Por que o <i>feedforward</i> não muda a estabilidade?",
     "\\(T_{n,PI}\\) e \\(T_{n,PI+FF}\\) têm o mesmo denominador, \\(1 + L(s)\\) sem as frações. Mesma equação característica.")
card(t, "Por que o <i>feedforward</i> cancela o distúrbio em regime mas não na hora?",
     "O comando dele também passa pela válvula. O que sobra do distúrbio é \\(K_n\\,\\tau_a s/(\\tau_a s + 1)\\): zero em \\(s \\to 0\\), mas não no instante da troca.")
card(t, "Quanto erro o P deixa por bico, pelo teorema do valor final?",
     "\\(\\Delta P(\\infty) = -K_n/(1 + K_c|K_g|)\\) = 0,323/3,2 = 0,101 kgf/cm² acima da referência (Ogata, p. 198; Castrucci, seção 2.3.4).")
card(t, "Por que o PI zera o erro, olhando para \\(T_n(s)\\)?",
     "O \\(s\\) no numerador faz \\(T_n(0) = 0\\). É a Tabela 3.4 de Castrucci (seção 3.11.3): com um integrador no controlador, erro estacionário nulo para perturbação em degrau.")
card(t, "O P e o PI são estáveis para quais ganhos? O que limita o ganho na prática?",
     "Qualquer ganho positivo: todos os coeficientes da equação característica são positivos. Na prática, a velocidade da válvula (e, num equipamento real, ruído e período de leitura).")

# ---------------- 07 Sintonia ----------------
t = "07_sintonia"
card(t, "O que é alocação de polos?",
     "Escolher primeiro onde ficam os polos de malha fechada (como a malha deve responder) e depois calcular os ganhos que os levam lá (Ogata, p. 658; Castrucci, seção 8.2).")
card(t, "Qual é a forma padrão de 2ª ordem?",
     "\\(\\dfrac{\\omega_n^2}{s^2 + 2\\zeta\\omega_n s + \\omega_n^2}\\) (Eq. 2.10; Ogata, p. 151). \\(\\omega_n\\): rapidez; \\(\\zeta\\): amortecimento.")
card(t, "Qual foi a especificação da sintonia?",
     "\\(\\zeta\\) = 0,7 e \\(t_s\\) = 0,5 s (critério de 2%).")
card(t, "Por que \\(\\zeta\\) = 0,7?",
     "Sobressinal de cerca de 4,6% e acomodação quase mínima; pelo critério de 2% o mínimo fica perto de \\(\\zeta\\) = 0,76 (Ogata, p. 157).")
card(t, "Por que \\(t_s\\) = 0,5 s?",
     "Um pouco mais rápido que a válvula livre (\\(4\\tau_a\\) = 0,8 s) sem exigir dela, a toda hora, mais velocidade do que tem. E cabe na rampa para um bico (0,24 s).")
card(t, "Como saem \\(K_c\\) e \\(T_i\\)? (Eqs. 3.30–3.32)",
     "\\(\\omega_n = 4/(\\zeta t_s)\\) = 11,43 rad/s; \\(K_c = (2\\zeta\\omega_n\\tau_a - 1)/|K_g|\\) = 0,827; \\(T_i = K_c|K_g|/(\\tau_a\\omega_n^2)\\) = 0,084 s.")
card(t, "De onde vêm as duas equações que dão \\(K_c\\) e \\(T_i\\)?",
     "Da comparação termo a termo de \\(s^2 + \\frac{1 + K_c|K_g|}{\\tau_a}s + \\frac{K_c|K_g|}{\\tau_a T_i} = 0\\) com \\(s^2 + 2\\zeta\\omega_n s + \\omega_n^2\\).")
card(t, "Onde ficam os polos do PI e do P?",
     "PI: −8,0 ± j8,2. P: −16 (um polo só).")
card(t, "Por que o P usa o mesmo \\(K_c\\) do PI?",
     "A malha do P tem um polo só, então não há \\(\\zeta\\) para escolher. Com o mesmo ganho, a diferença P × PI mostra só o efeito da ação integral.")
card(t, "Por que a especificação de 0,5 s só é cumprida nas trocas de um bico?",
     "Um bico pede 0,121 de abertura: 0,121/0,5 ≈ 0,24 s de rampa, cabe. Três bicos pedem 0,36: só a rampa leva ~0,7 s. Por isso C1 acomoda em 0,44 s e C2 em 1,02 s.")
card(t, "Por que não Ziegler-Nichols? (só se perguntarem)",
     "A planta vista pelo controlador é de 1ª ordem: não tem curva em S nem oscila com ganho proporcional, então as regras não se aplicam (Ogata, p. 523–524). Com modelo, é mais direto calcular pela especificação.")

# ---------------- 08 Simulação ----------------
t = "08_simulacao"
card(t, "Descreva os cenários C1, C2 e C3.",
     "C1: um bico por vez, 7 → 1 → 7, a cada 2 s (26 s). C2: sequência do ensaio de Rosa, 7 → 4 em 2 s e 4 → 1 em 8 s (14 s). C3: trocas aleatórias a cada 0,1–0,5 s, 20 s, 66 trocas, semente fixa.")
card(t, "Qual é a faixa de tolerância e de onde vem?",
     "±10% na pressão, ISO 16122-2, item 4.5.4: 3,15 a 3,85 kgf/cm². Corresponde a ~±5% na vazão.")
card(t, "Quais métricas foram usadas?",
     "Tempo fora da faixa (principal, Eq. 3.34), IAE (Eq. 3.35), desvio máximo e tempo de acomodação em ±2% (não usado no C3).")
card(t, "Por que o tempo fora da faixa é a métrica principal?",
     "Com a máquina em velocidade constante, é a porcentagem da área aplicada fora da tolerância.")
card(t, "O que o IAE mede que o tempo fora da faixa não mede?",
     "<b>Quanto</b> a pressão errou, mesmo dentro da faixa. O tempo fora só diz <b>se</b> saiu.")
card(t, "O que o programa faz a cada passo de 1 ms?",
     "1) atualiza os bicos; 2) lê a pressão, calcula erro, anti-windup e comando; 3) move a válvula (Euler, limite de velocidade); 4) recalcula a pressão por bissecção; 5) guarda os valores.")
card(t, "Que bibliotecas o programa usa, e por quê?",
     "Só numpy e matplotlib, sem biblioteca de controle, para cada passo ficar visível no código. Código completo no Apêndice A.")
card(t, "Cite as conferências automáticas do programa.",
     "K = 0,425 e erros do ajuste; \\(P_{ref}\\) atingível; \\(K_g\\) e \\(K_n\\) analíticos = numéricos para todo n; \\(\\zeta\\) e \\(\\omega_n\\) iguais aos especificados; denominador de \\(T_n\\) bloco a bloco = forma fechada.")

# ---------------- 09 Resultados ----------------
t = "09_resultados"
card(t, "Tempo fora da faixa em malha aberta nos três cenários?",
     "69% (C1) a 91% (C3). Pressão sobe até 5,5 kgf/cm² (desvio de 58%).")
card(t, "Tempo fora da faixa do P em C1, C2, C3?",
     "38,5%, 46,3% e 50,1%.")
card(t, "Tempo fora da faixa do PI em C1, C2, C3?",
     "0,0%, 6,8% e 8,3%.")
card(t, "Tempo fora da faixa do PI+FF em C1, C2, C3?",
     "0,0%, 6,8% e 9,5%.")
card(t, "Onde a pressão para com o P, com 4 e com 1 bico?",
     "3,81 e 4,12 kgf/cm² — o erro da Eq. (2.9). A partir do quarto bico fechado, sai da faixa.")
card(t, "Confira o erro do P com 4 bicos pela Eq. (2.9).",
     "Sem controle iria a 4,54 (\\(d\\) = 1,04). \\(e = 1{,}04/(1 + 2{,}2) = 0{,}32\\) → 3,82 kgf/cm². O simulador deu 3,81.")
card(t, "Como o PI se comporta no C1?",
     "0% fora da faixa. Cada troca dá um pico de ~9,5% (dentro da faixa), corrigido em ~0,44 s.")
card(t, "Por que o pico do C2 (29,7%) não some com nenhum controlador?",
     "Quando três bicos fecham, a pressão salta para ~4,54 kgf/cm² <b>no mesmo instante</b>, com a válvula ainda na posição antiga. O controle só define quanto tempo leva para voltar (1,02 s).")
card(t, "O que reduziria o pico do C2?",
     "Começar a abrir a válvula um pouco <b>antes</b> de fechar as solenoides, ou uma válvula mais rápida.")
card(t, "Por que o <i>feedforward</i> não trouxe ganho?",
     "A pressão salta na hora (H6) e o PI, lendo em tempo real, já manda abrir no mesmo instante. Os dois pedem mais do que a válvula dá, e ela anda em rampa nos dois casos. Nas trocas rápidas (C3) o FF persegue alvos que mudam antes de a válvula chegar.")
card(t, "Em que caso o <i>feedforward</i> ajuda, segundo o Castrucci?",
     "No Exemplo 7.4 (seção 7.8.1), com planta de 1ª ordem com atraso puro: o FF age antes de a realimentação perceber o erro. Aqui não há atraso entre a troca e a leitura.")
card(t, "Quanto tempo a válvula passa na velocidade máxima no C3?",
     "68% do tempo com o PI e 75% com o PI+FF.")
card(t, "O que acontece com uma válvula mais rápida?",
     "\\(\\omega_{max}\\) = 1,0: PI 3,4% no C2 e 0,4% no C3. \\(\\omega_{max}\\) = 2,0: 1,7% e 0,2%. O FF continua sem vantagem.")
card(t, "Qual é o gargalo do sistema?",
     "A velocidade da válvula (\\(\\omega_{max}\\)), que é estimada. Dobrá-la corta o tempo fora do PI pela metade no C2 e para quase zero no C3.")
card(t, "O que a Figura 18 mostra?",
     "A função de transferência acerta o valor final do simulador nos três controladores (P para em 3,60). Sem limite de velocidade, simulador e FT ficam sobrepostos; com limite, a válvula anda em rampa e a correção demora mais que 0,5 s.")
card(t, "Traduza o C2 para o campo.",
     "A 15 km/h a máquina anda ~4,2 m/s. Os 6,8% de 14 s do PI são quase 1 s fora da faixa: uns 4 m com a pressão fora da tolerância.")

# ---------------- 10 Limitações e futuros ----------------
t = "10_limitacoes"
card(t, "Quais são as principais limitações?",
     "\\(\\tau_a\\), \\(\\omega_{max}\\) e curva da válvula estimados; sem medição no tempo para validar a dinâmica; sensor perfeito, sem ruído; leitura em tempo real idealizada; bancada de 7 bicos e 5 m.")
card(t, "A leitura em tempo real é realista? Qual período seria aceitável?",
     "É uma idealização. Na prática, o período deve ser ≥10× menor que o período das oscilações (Castrucci, seção 12.6): 2π/8,2 ≈ 0,77 s → ler a cada ~77 ms ou menos. Com 10 ms, o PI mudou 0,8 p.p.")
card(t, "Se o sensor tiver ruído, o que fazer?",
     "Reduzir o ganho pela própria especificação: pedir um \\(t_s\\) maior dá um \\(K_c\\) menor pela Eq. (3.31).")
card(t, "O modelo vale para uma barra comercial?",
     "Não diretamente: lá há dezenas de bicos e vazões muito maiores, e a perda ao longo da barra (H2) e talvez a capacitância (H6) precisariam entrar.")
card(t, "Cite os trabalhos futuros.",
     "Medir a válvula na bancada; ajustar \\(\\zeta\\) e \\(t_s\\) com ruído real; válvula mais rápida ou comando antecipado às solenoides; anti-windup no limite de velocidade; barras comerciais; validar com dados de campo.")

# ---------------- 11 Livros ----------------
t = "11_livros"
card(t, "Onde ler sobre PID na forma \\(K_c\\), \\(T_I\\), \\(T_D\\)?",
     "Ogata (2010), p. 21; Castrucci, Bittar e Sales (2018), seção 6.2 (padrão ISA).")
card(t, "Onde ler sobre erro estacionário com perturbação?",
     "Castrucci, Bittar e Sales (2018), seção 3.11.3 e Tabela 3.4 (perturbação em degrau, referência nula).")
card(t, "Onde ler sobre forma padrão de 2ª ordem, \\(M_p\\) e \\(t_s\\)?",
     "Ogata (2010), p. 151, 156 e 157; Castrucci et al. (2018), seções 3.5 e 3.6 (3.6.5 para \\(t_s\\)).")
card(t, "Onde ler sobre alocação (imposição) de polos?",
     "Ogata (2010), p. 522 e 658; Castrucci et al. (2018), seção 8.2.")
card(t, "Onde ler sobre <i>feedforward</i>?",
     "Castrucci et al. (2018), seções 7.8 e 7.8.1 (Eq. 7.51, Exemplo 7.4); Liu et al. (2018).")
card(t, "Onde ler sobre <i>windup</i> e anti-windup?",
     "Castrucci et al. (2018), seção 6.3.4 (o efeito); Fernandes e Goldemberg (2001), p. 5 (integração condicional).")
card(t, "Onde ler sobre linearização e saturação?",
     "Castrucci et al. (2018), seções 9.10.1 (linearização para pequenos sinais) e 9.10.2 (saturação).")
card(t, "Onde ler sobre teorema do valor final e diagramas de blocos?",
     "Ogata (2010), p. 198 e p. 22; Castrucci et al. (2018), seções 2.3.4 e 2.6.")
card(t, "Onde ler sobre lei de orifício e continuidade?",
     "Brunetti (2008), p. 75 (continuidade), p. 212–213 (veia contraída, orifício); Merritt (1967), p. 40–41.")
card(t, "Onde ler sobre os métodos numéricos usados?",
     "Chapra e Canale (2011): mínimos quadrados p. 393, bissecção p. 101–102, diferença centrada p. 75, retângulos p. 493, Euler p. 588 e 592.")
card(t, "Por que o Castrucci é citado por seção e não por página?",
     "A versão consultada é um <i>e-book</i> sem numeração de página; a citação por seção permite localizar o trecho.")

# ---------------- gravação ----------------
saida = Path(__file__).resolve().parents[2] / "docs" / "Anki_TCC_v20.txt"
linhas = ["#separator:tab", "#html:true", "#notetype:Básico", "#deck:TCC Pulverização v20", "#tags column:3"]
for f, v, tg in C:
    for campo in (f, v):
        assert "\t" not in campo and "\n" not in campo
    linhas.append(f"{f}\t{v}\ttcc {tg}")
saida.write_text("\n".join(linhas) + "\n", encoding="utf-8")
print(len(C), "cartoes ->", saida)
