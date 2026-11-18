# Revisão de clareza da v14 (leitor independente, 04/11/2026)

O que é: o diagnóstico de um agente revisor sobre `contexto/14.md`. Os números de linha referem-se a esse arquivo.

**Status (v15, 04/11/2026):** todos os itens 1–37, as repetições e as transições foram aplicados na v15 (ver nota A15 em `15.md`). Exceções: a referência do *feedforward* na 2.7.1 continua pendente.

Como usar:
- é a base da reescrita **v15**, que deve deixar o texto "redondo" sem mudar números nem escopo;
- antes de aplicar cada item, conferir se ele procede.

## Itens priorizados (mais grave primeiro)

### Modelo de resistência (3.3.1 e 4.1)

**1. Dois valores de R₁ sem explicação.** L602–607 (3.3.1) × L1119–1127 (4.1).
- Em 3.3.1, R₁ = 1/K² ≈ 5,54; em 4.1, R₁ = 5,58, tirado do ensaio com um bico.
- O simulador usa K = 0,425, que equivale a 5,54. A Tabela 6 usa 5,58.
- Correção: dizer isso explicitamente nas duas seções.

**2. Não fica claro onde o modelo R₁/n² é usado.**
- As Eqs. 3.3 e 3.4 são o mesmo modelo escrito de duas formas.
- A (3.4) serve para comparar com a Eq. 2.9; a (3.3) é a usada nas contas e no código.

**3. "Vale para qualquer número de bicos iguais"** é forte demais. Acrescentar "desde que a perda ao longo da barra seja desprezível (H2)".

**4. L547.** A frase "Ele parte da Equação (2.8)" está errada.
- A Eq. 2.8 é a soma em série de orifício e tubo, e o modelo despreza o tubo.
- Trocar por: "aplica a lei de orifício (Eq. 2.4) a cada saída (bicos e válvula) e acrescenta a curva da fonte".

### Nomes e dados da bancada

**5. Muitos nomes para a válvula atuadora:** reguladora, de alívio, de recirculação, agulha, PV, HV.
- Fixar "válvula de alívio (HV)", explicar os sinônimos uma vez em 3.2 e usar só esse nome depois.
- Em 3.3.2 (L611), a PCV também é chamada de "válvula de alívio". Trocar para que não se confunda com o atuador.

**6. A Tabela 2 parte de 4,00 kgf/cm², mas a Tabela 1 dá 3,57 na mesma condição.** A ressalva só aparece em 4.1. Avisar já em 3.2.

### Função de transferência (3.5.5)

**7. Falta transição e motivo.** Abrir com: "A sintonia foi feita no simulador; para entender por que o P deixa erro, por que o PI o elimina e se o FF altera a estabilidade…".

**8. Resultados numéricos na Metodologia.** Polos, ζ, t_s e 0,066 usam ganhos que só aparecem na seção 4.2. Duas saídas:
- levar os números para 4.2, junto da Figura 21;
- ou avisar em 3.5.5 que os números usam os ganhos da seção 4.2.

**9. A justificativa do sinal da realimentação está confusa.** Explicar seguindo a malha: K_g é negativo, então uma pressão acima da referência gera uma correção que baixa a pressão.

**10. O termo do FF (−K_n/K_g) aparece sem origem.**
- −K_n/K_g = 0,121 por bico, o mesmo K/K_v,max da Eq. 3.14.
- Esse comando passa pela válvula, por isso cancela o distúrbio no regime, mas não no instante da troca.
- Mostrar como se chega à Eq. 3.24.

**11. K_n sem procedência.**
- Dizer o ponto de cálculo: 7 bicos, α_ff(7), n variando de 6,5 a 7,5.
- Dizer que K_n varia com n, ao contrário de K_g.
- Acrescentar K_n na Tabela 4.

**12. Salto algébrico** para s² + 22,5s + 210. Dizer que a equação foi dividida por τ_aT_i = 0,0166 e que K_c|K_g| = 3,5.

**13. Remissão e afirmação erradas** em "K_cr = 2,93 (seção 3.5.4)".
- O número está na Tabela 9 e na seção 4.2, não na 3.5.4.
- Na função de transferência contínua, o P também seria estável com qualquer ganho, não só o PI.

### Cap. 2 e Conclusão

**14. Duas justificativas para a faixa de ±10%** (seções 2.5 e 1.1): os itens 4.5.4 e 4.8.8 da ISO.
- A faixa vem do item 4.5.4.
- O item 4.8.8 só mostra que a norma trata o fechamento de parte da barra como perturbação.
- O critério do trabalho é mais exigente, porque conta cada instante fora da faixa.

**15. Seção 2.6: parágrafo embaralhado.**
- "Em unidades práticas" vem logo depois da frase sobre Steward e Humburg, mas se refere à vazão desejada.
- A Eq. 2.11 nunca é usada depois.
- Reordenar e ligar à pressão como variável controlada.

**16. Conclusão: os objetivos estão trocados.**
- O 4º objetivo é o *feedforward*, que não aparece no parágrafo correspondente.
- A frase sobre K_g e a sintonia está no parágrafo do 2º objetivo e deve ir para o do 3º.

### Anti-windup e Cap. 3

**17. Seção 4.5: o anti-windup só por posição fica mal justificado** (8,9% contra 5,0%). Dizer que a forma da literatura foi mantida e que estendê-lo ao limite de velocidade é uma melhoria indicada pelo teste, a citar também nos trabalhos futuros.

**18. Seção 3.5.3:** "O limite de velocidade não congela o integrador" vem sem explicação. Acrescentar "efeito medido na seção 4.5".

**19. Seção 3.4.2:** o exemplo do C2 usa 0,36 e a Eq. 3.14 antes de definir os dois. Escrever "3 × 0,12 = 0,36 (seção 3.5.2)".

**20. Seção 3.5.1:** usa α_ff antes da definição. Inverter as seções 3.5.1 e 3.5.2, ou chamar de "abertura de equilíbrio".

**21. Muitos nomes para a abertura fixa:** α₀, abertura de equilíbrio, abertura inicial, `bias`. Definir α₀ = α_ff(7) = 0,023 e usar só esse nome.

### Números e tempos

**22. A duração do C2 (14 s) falta na Tabela 5.** O exemplo das 946 amostras não diz de qual cenário é.

**23. O erro de vazão de 2,3% não fecha** com a Tabela 7 arredondada, que dá 2,5%. Usar três casas e escrever "até 2,3%" em 3.7.3.

**24. O K_cr teórico de 3,02 aparece sem fórmula nem fonte.** Dar a fórmula, ou dizer "cálculo à parte com o modelo discreto".

**25. Seção 4.6:** "0,95 s fora da faixa" se confunde com os 0,95 s da acomodação do PI. Explicar como 6,8% de 14 s.

**26. Seção 4.5:** os 0,7 s da válvula e os 0,95 s de acomodação aparecem sem distinção.

**27. Seção 4.6:** "o PI pede movimentos menores" vem sem justificativa.
- O PI só corrige o erro que de fato apareceu.
- O FF manda a válvula para cada novo alvo inteiro, mesmo que ele mude logo depois.

### Remissões e transições

**28. Seção 2.4.4:** "É isso que sustenta a H2" tem a lógica invertida e cita a H2 antes de ela ser definida.

**29. Seção 2.3 × 3.3.2:** a 2.3 afirma como fato que a PCV faz a vazão cair, e a 3.3.2 trata isso como inferência. Usar "provavelmente" em 2.3.

**30. Seção 2.6.1:** "seções 4.2 e 3.8" deve ser só "seção 3.8".

**31. Seção 3.4.2:** frase longa sobre "sat". Dividir, e trocar "Fora do limite" por "Enquanto a velocidade não atinge o limite".

**32. Seção 3.3:** "nK + K_v(α)" aparece antes da definição dos símbolos. Escrever em palavras.

**33. Seção 4.2 × 3.5.4:** parecem dar duas causas para a oscilação. A amostragem define o período; o limite de velocidade define o formato em dente de serra.

**34. Seção 4.2:** "o mesmo resultado das seções 4.5 e 4.6" remete a algo que ainda não veio. Trocar por "conclusão que volta a aparecer…".

**35. Seção 4.3 e Tabela 10:**
- dizer em qual figura olhar;
- explicar "não acomoda (11 de 12)".

**36. L653–654:** falta a linha em branco antes de "### 3.4.2".

**37. Lista de símbolos:** faltam P_ref, α₀, C(s), G(s), E(s), os desvios Δ, t_s, d e e_reg.

## Repetições que podem ser cortadas

- **Motivos para usar a bancada de Rosa:** aparecem em 1.3 e em 3.2. Deixar a lista só em 3.2.
- **"Os autores deixaram a válvula como trabalho futuro":** aparece em L128 e L166. Cortar em L166.
- **Justificativa da H2:** aparece 5 vezes. Deixar completa só em 3.3; nos outros pontos, só "(H2)".
- **Três formas de ajustar a pressão:** aparecem em 1.3 e em 2.3. Deixar só em 2.3.
- **"K_g não depende de n":** aparece 3 vezes. Em 4.2, só "(Tabela 3)".
- **Erro do P:** aparece em 2.6, 3.5.5 e 4.4. Manter a dedução em 2.6 e os números só no Cap. 4.
- **K_cr teórico de 3,02:** aparece duas vezes. Explicar só em 4.2.
- **Ensaio de 10 ms:** aparece duas vezes. Em 3.4.3, só "(seção 4.2)".

## Transições a acrescentar

- **Fim de 1.4:** citar o modelo R₁/n² e a função de transferência.
- **Início do Cap. 2:** a ordem dos assuntos e por que cada um importa.
- **Início de 3.3:** "Com a bancada descrita, o próximo passo é traduzi-la em equações…".
- **Início de 3.5.5:** a frase-motivo do item 7.
- **Início de 3.6:** "Definidos o modelo e os controladores, falta dizer com quais números, situações e critérios eles foram testados".
- **Passagem de 4.1 para 4.2:** "Com o modelo estático conferido, ele é usado para medir o ganho e sintonizar".
- **Passagem de 4.3 para 4.4:** "A malha aberta mostra o tamanho do problema; as próximas seções, quanto cada controlador o reduz".
