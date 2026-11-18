

<!-- Text/cover.xhtml -->





  
  Controle Automático, 2ª edição
  
  



  
     [img:Illustration] 
  



<!-- Text/halftitle.xhtml -->





  Controle Automático, 2ª edição
  
  
  



  
     [img:Illustration] 
  



<!-- Text/gen.xhtml -->





  Controle Automático, 2ª edição
  
  
  



  
     [img:Illustration] 
  



<!-- Text/title.xhtml -->





  
  Controle Automático, 2ª edição
  
  



  
     [img:Illustration] 
  



<!-- Text/copyright.xhtml -->





  
  Controle Automático, 2ª edição
  
  



   


  Os autores e a editora empenharam-se para citar adequadamente e dar o devido crédito a todos os detentores dos direitos autorais de qualquer material utilizado neste livro, dispondo-se a possíveis acertos caso, inadvertidamente, a identificação de algum deles tenha sido omitida.


  Não é responsabilidade da editora nem dos autores a ocorrência de eventuais perdas ou danos a pessoas ou bens que tenham origem no uso desta publicação.


  Apesar dos melhores esforços dos autores, do editor e dos revisores, é inevitável que surjam erros no texto. Assim, são bem-vindas as comunicações de usuários sobre correções ou sugestões referentes ao conteúdo ou ao nível pedagógico que auxiliem o aprimoramento de edições futuras. Os comentários dos leitores podem ser encaminhados à LTC — Livros Técnicos e Científicos Editora pelo e-mail faleconosco@grupogen.com.br.


  Direitos exclusivos para a língua portuguesa


  Copyright © 2018 by


  LTC — Livros Técnicos e Científicos Editora Ltda.


  Uma editora integrante do GEN | Grupo Editorial Nacional


  Reservados todos os direitos. É proibida a duplicação ou reprodução deste volume, no todo ou em parte, sob quaisquer formas ou por quaisquer meios (eletrônico, mecânico, gravação, fotocópia, distribuição na internet ou outros), sem permissão expressa da editora.


  Travessa do Ouvidor, 11


  Rio de Janeiro, RJ – CEP 20040-040


  Tels.: 21-3543-0770 / 11-5080-0770


  Fax: 21-3543-0896


  faleconosco@grupogen.com.br


  www.grupogen.com.br


  Capa: Leônidas LeiteProdução digital: Geethik


  Imagens da capa e da 4a capa : © from2015 | iStockphoto.com e © nielubieklonu | iStockphoto.com


  CIP-BRASIL. CATALOGAÇÃO NA PUBLICAÇÃOSINDICATO NACIONAL DOS EDITORES DE LIVROS, RJ.


  
    C353c2. ed.


    Castrucci, Plínio de Lauro


    Controle automático / Plínio de Lauro Castrucci, Anselmo Bittar, Roberto Moura Sales. - 2. ed. - Rio de Janeiro : LTC, 2018.


    :il.; 28 cm.


    Inclui bibliografia e índice


    ISBN 978-8-5216-3561-1


    1. Controle automático. 2. Engenharia de sistemas. 3. Sistemas dinâmicos diferenciais. I. Bittar, Anselmo. II. Sales, Roberto Moura. III. Título.


    
      
        

        
      

      
        
          
            18-50057.

          

          
            CDD: 629.8CDU: 681.5

          
        

      
    

    Meri Gleice Rodrigues de Souza - Bibliotecária - CRB-7/6439

  



<!-- Text/fm01.xhtml -->





  
  Controle Automático, 2ª edição
  
  



  

## Prefácio


  Este é um livro didático concebido para apoio às disciplinas iniciais dos cursos de controle de sistemas dinâmicos. Por dinâmicos entendem-se sistemas, de qualquer natureza física, que sejam representáveis por equações diferenciais ou de diferenças na variável tempo.


  Organizar um curso de engenharia de controle dinâmico, cujo tema básico é a realimentação de sinais em suas inúmeras formas, é um desafio. As teorias mais gerais são muito abstratas, expressas em eficientes mas herméticas linguagens matemáticas, tais como o cálculo matricial, a análise funcional e os processos estocásticos. Por outro lado, as teorias mais úteis no sentido de resolver grande número de problemas práticos são incompletas. Isso nos leva a examinar o ambiente e a natureza das aplicações nas seguintes divisões:


  
    • controle de processos, cujo objeto são as plantas industriais, altos-fornos, usinas químicas, térmicas, de cimento, petroquímicas, de funcionamento contínuo ou por bateladas. Estas se caracterizam por dinâmica relativamente lenta, com respostas naturais de alguns minutos até muitas horas, e por uma tendência a apresentar não linearidades intrínsecas, como, por exemplo, as reações químicas e o produto das concentrações dos insumos. O objetivo do controle costuma estar muito ligado à estabilização em dados níveis operacionais e à segurança do processo;


    • controle de posição, cujo objeto são as posições e as velocidades de massas, que vão desde alguns gramas (robôs de manufatura de semicondutores) até toneladas (aeronaves, metrôs, radiotelescópios). O objetivo do controle costuma estar centrado em obter, nas respostas aos sinais de referência e às perturbações, a maior rapidez e a maior precisão que as fontes de energia e os medidores podem fornecer.

  


  Constata-se que a maioria das aplicações de controle é simples, quer em controle de processos, quer em controle de posição. São malhas com variáveis isoladas e processos bem próximos da linearidade, empregando o tradicional controlador PID (Proporcional + Integral + Derivativo), realizado atualmente de modo digital em CLPs (Controladores Lógicos Programáveis).


  Além dos controladores PID, não podem estar ausentes da formação inicial dos estudantes os seguintes temas: as arquiteturas consagradas no controle de processos (controle cascade, feedforward, de razão, etc.), seus símbolos pela norma ISA (International Society of Automation) e seus diagramas P&ID (Piping and Instrumentation Diagram).


  A primeira edição deste livro restringiu o tratamento do problema de controle aos modelos na forma de função de transferência, usualmente aplicados para sistemas com uma entrada e uma saída (sistemas SISO - Single Input Single Output), nos quais é fraca a interação entre as várias malhas de controle atuantes no processo.


  No entanto, embora a maioria dos problemas industriais seja tradicionalmente resolvida com modelos de função de transferência, a evolução das técnicas e programas de análise tem levado a um interesse crescente, nas instituições de ensino e nas aplicações, pela utilização da abordagem de variáveis de estado. Assim, nesta segunda edição foi incluído um capítulo apresentando modelos de espaço de estados e técnicas básicas de projeto baseadas em imposição de polos e no regulador linear quadrático, incluindo observador de estados.


  Este novo capítulo é ainda restrito aos sistemas SISO, mas foi elaborado como um primeiro passo para o estudo das técnicas de espaço de estados de sistemas MIMO (Multi Input Multi Output), que aparecem frequentemente nos sistemas modernos de controle de posição de alto desempenho, tais como robôs, aeronaves e laminadores.


  Este é um livro-texto com uma abordagem didática, que solicita intensa atividade do estudante em exemplos, exercícios resolvidos e exercícios propostos. O seu conteúdo permite ao professor selecionar temas com vários níveis de dificuldades e aplicações.


  O Capítulo 2, sobre Sistemas Dinâmicos, é muito bem detalhado, necessário apenas para a hipótese de os estudantes não terem passado por uma disciplina prévia de sistemas lineares. Os autores consideram possíveis e interessantes os seguintes roteiros de disciplinas semestrais:


  
    • primeira disciplina: Capítulos 1 a 8 ou Capítulo 1, revisão do Capítulo 2 e Capítulos 3 a 9;


    • segunda disciplina: Capítulos 9 a 13 ou Capítulos 10 a 13.

  


  Por fim, gostaríamos de agradecer a todos os amigos do Laboratório de Automação e Controle da Escola Politécnica da Universidade de São Paulo pelas valiosas sugestões e contribuições, aos nossos familiares e a todos que direta ou indiretamente contribuíram com este trabalho.


  Os Autores



<!-- Text/fm02.xhtml -->





  
  Controle Automático, 2ª edição
  
  



  

## Sobre os autores


  Plínio de Lauro Castrucci é engenheiro mecânico e eletricista pela Escola Politécnica da Universidade de São Paulo (Poli-USP). Obteve os títulos de D.I.C. em 1958 no Imperial College of Science and Technology, de livre-docente em 1964 e de professor titular em 1967 na Escola Politécnica da Universidade de São Paulo. Foi fundador e diretor da Amplimag Controles Automáticos (1963-1983), projetista pioneiro de amplificadores magnéticos e de acionamentos eletrônicos, inclusive para o Metrô de São Paulo. Foi diretor da Engesa Eletrônica e da Engesa Elétrica. Foi fundador e presidente da Sociedade Brasileira de Automática e consultor de várias empresas. É membro sênior do IEEE. É coautor de Curso de Ética em Administração (Atlas) e Engenharia de Automação Industrial (LTC).


  Anselmo Bittar graduou-se em Engenharia Elétrica em 1990 e obteve os títulos de mestre em 1993 e doutor em 1998 na Escola Politécnica da Universidade de São Paulo (Poli-USP). Atualmente é analista de sistemas do Departamento de Engenharia de Telecomunicações e Controle da Escola Politécnica da Universidade de São Paulo. Atua na área de pesquisa relacionada a sistemas de levitação eletromagnética.


  Roberto Moura Sales graduou-se em Engenharia Elétrica em 1975 e obteve os títulos de mestre em 1981, doutor em 1984, livre-docente em 1986 e professor titular em 1994 na Escola Politécnica da Universidade de São Paulo (Poli-USP). Suas principais áreas de ensino e pesquisa em controle automático incluem controle de processos industriais, levitação magnética, laminação e otimização.



<!-- Text/contents.xhtml -->





  Controle Automático, 2ª edição
  
  
  



  

## Sumário


  1 Introdução


  1.1 Conceitos gerais


  1.2 Realimentação


  1.3 Um pouco de história


  1.4 Modelos matemáticos


  1.5 Motivações técnicas e econômicas


  1.6 Variedades de controle


  1.7 O controle dinâmico inserido na automação


  1.8 Desenvolvimento de projetos


  1.9 Projeto auxiliado por computador


  2 Sistemas Dinâmicos


  2.1 Introdução


  2.2 Modelos matemáticos diferenciais


  2.2.1 Equações constitutivas


  2.2.2 Equações de equilíbrio


  2.2.3 Equações de conservação ou balanço de massa e energia


  2.3 Transformada de Laplace


  2.3.1 Transformada de Laplace de algumas funções


  2.3.2 Propriedades da transformada de Laplace


  2.3.3 Teorema do valor inicial


  2.3.4 Teorema do valor final


  2.4 Função de transferência


  2.5 Transformada de Laplace inversa


  2.5.1 Expansão em frações parciais


  2.6 Diagramas de blocos


  2.7 Estudo de caso: motor de corrente contínua


  2.7.1 Sistema em malha aberta com torque resistente


  2.7.2 Sistema em malha fechada: regulador de velocidade


  2.8 Implementação analógica de funções de transferência


  2.8.1 Amplificador inversor


  2.8.2 Amplificador não inversor


  2.8.3 Circuito somador


  2.8.4 Circuito integrador


  2.8.5 Circuito diferenciador


  2.8.6 Sistemas de primeira ordem


  2.8.7 Sistemas de segunda ordem


  2.8.8 Impedâncias complexas


  2.9 Exercícios resolvidos


  2.10 Exercícios propostos


  3 Análise no Domínio do Tempo


  3.1 Introdução


  3.2 Estabilidade de sistemas lineares


  3.2.1 Teorema da estabilidade linear


  3.3 Critério de estabilidade de Routh


  3.4 Sistemas de primeira ordem


  3.4.1 Resposta ao impulso


  3.4.2 Resposta ao degrau


  3.4.3 Resposta à rampa


  3.5 Sistemas de segunda ordem


  3.5.1 Sistema subamortecido: 0 < ξ < 1


  3.5.2 Sistema oscilatório: ξ = 0


  3.5.3 Sistema com amortecimento crítico: ξ = 1


  3.5.4 Sistema superamortecido: ξ > 1


  3.6 Características das respostas transitórias


  3.6.1 Tempo de atraso td


  3.6.2 Tempo de subida tr


  3.6.3 Tempo de pico tp


  3.6.4 Sobressinal máximo: Mp


  3.6.5 Tempo de acomodação: ts


  3.7 Sistemas com mais de dois polos


  3.8 Sistemas com zeros


  3.9 Sistemas com atraso puro ou atraso por transporte


  3.10 Resposta dos sistemas de controle por realimentação


  3.11 Erro estacionário ou permanente


  3.11.1 Degrau na referência e perturbação nula


  3.11.2 Rampa na referência e perturbação nula


  3.11.3 Perturbação em degrau e referência nula


  3.11.4 Perturbação em rampa e referência nula


  3.12 Exercícios resolvidos


  3.13 Exercícios propostos


  4 Lugar das Raízes


  4.1 Introdução


  4.2 O método do Lugar Geométrico das Raízes (L.G.R.)


  4.3 Regras para o traçado do lugar das raízes


  4.4 Realimentação positiva


  4.5 Lugar das raízes de sistemas com atraso puro


  4.5.1 Aproximações de Padé


  4.6 Compensação por meio do lugar das raízes


  4.6.1 Compensação por avanço de fase


  4.6.2 Compensação por atraso de fase


  4.6.3 Compensação por avanço e atraso de fase


  4.6.4 Compensação por realimentação auxiliar


  4.7 Implementação analógica de compensadores


  4.7.1 Compensador por avanço ou atraso de fase de ordem 1


  4.7.2 Compensador por avanço ou atraso de fase de ordem 2


  4.8 Exercícios resolvidos


  4.9 Exercícios propostos


  5 Análise e Compensação no Domínio da Frequência


  5.1 Introdução


  5.2 Diagramas de Bode


  5.2.1 Ganho constante


  5.2.2 Polo na origem


  5.2.3 Zero na origem


  5.2.4 Polo real fora da origem


  5.2.5 Zero real fora da origem


  5.2.6 Polos complexos conjugados


  5.2.7 Zeros complexos conjugados


  5.2.8 Sistemas gerais


  5.3 Identificação experimental de funções de transferência


  5.3.1 Medida da resposta em frequência


  5.4 Sistemas de fase mínima e de fase não mínima


  5.5 Sistemas com atraso puro ou atraso de transporte


  5.6 Diagramas de Nyquist


  5.7 Estabilidade de sistemas com realimentação


  5.7.1 Princípio do argumento


  5.7.2 Critério de estabilidade de Nyquist


  5.8 Margens de estabilidade


  5.9 Resposta em frequência da malha fechada


  5.9.1 Carta de Nichols


  5.10 Banda passante e frequência de corte


  5.11 Compensação por meio da resposta em frequência


  5.11.1 Compensação por avanço de fase


  5.11.2 Compensação por atraso de fase


  5.11.3 Compensação por avanço e atraso de fase


  5.12 Exercícios resolvidos


  5.13 Exercícios propostos


  6 Controladores PID


  6.1 Introdução


  6.2 A função de transferência do controlador PID


  6.3 Aspectos de implementação dos controladores PID


  6.3.1 Implementação do termo derivador


  6.3.2 Implementação sem derivada do erro


  6.3.3 Transferência manual-automático suave (bumpless)


  6.3.4 Antidisparo da referência (antireset windup)


  6.3.5 Algoritmo PID implementado em computador


  6.3.6 Implementação analógica


  6.4 Exercícios resolvidos


  6.5 Exercícios propostos


  7 Controle de Processos


  7.1 Introdução


  7.2 Ajuste por Ziegler-Nichols no domínio da frequência


  7.2.1 Primeiro método


  7.2.2 Segundo método


  7.3 Ajuste por Ziegler-Nichols no domínio do tempo


  7.4 Sintonia automática de controladores PID


  7.5 Ajuste SIMC - Skogestad Internal Model Control


  7.5.1 Regra SIMC 1


  7.5.2 Regra SIMC 2


  7.6 Termos e símbolos ISA


  7.6.1 Termos ISA


  7.6.2 Símbolos da ISA


  7.7 Arquitetura em cascata (cascade control)


  7.7.1 Projeto de controlador em cascata


  7.7.2 Controlador em cascata para reduzir não linearidades


  7.8 Alimentação avante (feedforward control)


  7.8.1 Projeto de controlador feedforward


  7.8.2 Controle de alternadores por feedforward


  7.8.3 Aplicação ao controle de razão (ratio control)


  7.9 Ganho adaptativo (gain scheduling)


  7.10 Introdução aos Controladores Lógicos Programáveis


  7.10.1 Arquitetura


  7.10.2 Linguagem de programação ladder


  7.10.3 Ajuste de escala dos sinais


  7.10.4 Ciclo de execução (scan)


  7.10.5 Controle dinâmico realizado por CLP


  7.10.6 A realidade industrial


  7.11 Exercícios resolvidos


  7.12 Exercícios propostos


  8 Projeto Algébrico pela Malha Fechada


  8.1 Introdução


  8.2 Imposição arbitrária de polos com realimentação unitária


  8.2.1 Condição para escolha arbitrária dos polos de malha fechada


  8.2.2 Condição para que a função de transferência Gc(s) seja própria


  8.3 Imposição de polos e model matching


  8.3.1 Projeto de compensadores para model matching


  8.4 Exercícios resolvidos


  8.5 Exercícios propostos


  9 Limitações de Projeto


  9.1 Introdução


  9.2 Critérios de qualidade


  9.3 Controlabilidade


  9.4 A complexidade dos objetivos do projeto


  9.5 Estratégia de projeto


  9.6 Limitações por fase não mínima


  9.7 Limitações por atraso puro


  9.7.1 Preditor de Smith


  9.8 Índice de desempenho ISE mínimo


  9.9 Robustez perante incertezas estruturadas


  9.10 Não linearidades


  9.10.1 Linearização para pequenos sinais


  9.10.2 Saturação


  9.10.3 Relé


  9.10.4 Zona morta


  9.10.5 Folga de engrenagens (backlash)


  9.10.6 Efeitos sobre a estabilidade


  9.11 Estudo de caso: antena de radar


  9.12 Exercícios resolvidos


  9.13 Exercícios propostos


  10 Sistemas de Tempo Discreto


  10.1 Introdução


  10.2 Transformada Z


  10.2.1 Transformada Z de algumas funções


  10.2.2 Algumas propriedades e teoremas da transformada Z


  10.2.3 Teorema do valor inicial


  10.2.4 Teorema do valor final


  10.3 Função de transferência


  10.3.1 Álgebra de blocos


  10.4 Resposta impulsiva


  10.5 Transformada Z inversa


  10.5.1 Expansão em série por divisão contínua


  10.5.2 Programa de computador


  10.5.3 Expansão em frações parciais


  10.6 Exercícios resolvidos


  10.7 Exercícios propostos


  11 Sistemas de Controle Digital


  11.1 Introdução


  11.2 Conversor A/D


  11.3 Conversor D/A


  11.4 Análise frequencial da amostragem e da recuperação


  11.5 Subsistema A/D + controlador + D/A


  11.5.1 Função de transferência do segurador de ordem zero


  11.6 Filtro ideal e segurador de ordem zero


  11.7 Mapeamento do plano s no plano z


  11.8 Subsistema D/A + processo + A/D


  11.9 Análise da malha fechada


  11.10 Estabilidade de sistemas de tempo discreto


  11.10.1 Critério de Routh


  11.10.2 Critério de Jury


  11.11 Exercícios resolvidos


  11.12 Exercícios propostos


  12 Projeto de Controladores Digitais


  12.1 Introdução


  12.2 Aproximações de tempo discreto


  12.2.1 Retangular para a frente


  12.2.2 Retangular para trás


  12.2.3 Transformação bilinear ou método de Tustin


  12.2.4 Transformação bilinear com compensação de prewarping


  12.2.5 Mapeamento polo-zero


  12.3 Projeto de controlador discreto a partir de projeto de controlador contínuo


  12.4 Erro estacionário ou permanente


  12.4.1 Degrau na referência


  12.4.2 Rampa na referência


  12.5 Polos no plano s e no plano z


  12.6 Influência do período de amostragem em transitórios


  12.7 Projeto de controlador no plano z


  12.8 Controlador PID discreto


  12.9 Controlador PID com ganho variável (adaptativo)


  12.10 Projeto no domínio da frequência


  12.10.1 Formas de mapeamento


  12.10.2 Diagramas de Bode


  12.10.3 Projeto do controlador


  12.11 Controlador dead beat


  12.11.1 Causalidade


  12.11.2 Erro estacionário


  12.11.3 Polos e zeros fora ou sobre a circunferência de raio unitário


  12.11.4 Eliminação de oscilações entre os instantes de amostragem


  12.12 Exercícios resolvidos


  12.13 Exercícios propostos


  13 Projeto de Controladores no Espaço de Estados


  13.1 Introdução


  13.2 Modelo de sistemas dinâmicos no espaço de estados


  13.3 Forma canônica controlável


  13.4 Forma canônica observável


  13.5 Conversão de estados para função de transferência


  13.6 Autovalores de uma matriz


  13.7 Estabilidade


  13.8 Posto de uma matriz


  13.9 Controlabilidade e observabilidade


  13.9.1 Condição de controlabilidade


  13.9.2 Condição de observabilidade


  13.10 Transformação de similaridade


  13.10.1 Transformação para a forma canônica controlável


  13.11 Controle por realimentação de estados contínuos


  13.11.1 Alocação de polos de malha fechada


  13.12 Regulador Linear Quadrático - RLQ


  13.12.1 Formulação do problema


  13.12.2 Procedimento de projeto para o Regulador Linear Quadrático


  13.13 Observador ou estimador de estados contínuos


  13.13.1 Formulação do problema


  13.13.2 Estrutura do observador de estados


  13.13.3 Procedimento de projeto do observador de estados


  13.13.4 Conexão entre controlador e observador de estados


  13.13.5 Função de transferência do bloco controlador+observador


  13.14 Inclusão de integrador contínuo na malha de controle


  13.15 Espaço de estados discretos


  13.15.1 Modelos no espaço de estados discretos


  13.15.2 Conversão de estados para função de transferência


  13.15.3 Autovalores


  13.15.4 Estabilidade


  13.16 Controle por realimentação de estados discretos


  13.16.1 Alocação de polos de malha fechada


  13.16.2 Regulador Linear Quadrático - RLQ


  13.17 Observador ou estimador de estados discretos


  13.17.1 Alocação de polos de malha fechada no observador


  13.17.2 Conexão entre controlador e observador de estados discretos


  13.17.3 Função de transferência do bloco controlador+observador


  13.18 Inclusão de integrador discreto na malha de controle


  13.19 Exercícios resolvidos


  13.20 Exercícios propostos


  Bibliografia



<!-- Text/halftitle1.xhtml -->





  Controle Automático, 2ª edição
  
  
  



  
     [img:Illustration] 
  



<!-- Text/chapter01.xhtml -->





  Controle Automático, 2ª edição
  
  
  



  

## 1


  

## Introdução


  

### 1.1 Conceitos gerais


  Controlar uma grandeza ou variável física significa alterar o seu valor de acordo com uma intenção. Porém, nem sempre isso é realizável perfeitamente, ou porque não se dispõe de energia suficiente ou porque há perturbações muito grandes ou muito rápidas. Por exemplo, para controlar variáveis climáticas não há energia suficiente e para controlar variáveis de processos industriais ou de transporte é preciso que os objetivos e as perturbações sejam compatíveis.


  Quando o operário de uma indústria dá partida em um motor ou age sobre uma válvula de um dado processo ele está realizando um controle manual. Embora um artesão possa dessa maneira obter resultados excepcionais, com atenção redobrada ao seu trabalho, geralmente a indústria precisa de produção rotineira, de qualidade constante, dia e noite. Quando, por essas ou outras razões, uma parte ou todas as funções do operário são delegadas a um equipamento, diz-se que o controle é automático.


  Há duas grandes classes de controle automático, em função da natureza da dinâmica do processo a controlar:


  • dinâmica tradicional. Originalmente, na física, dinâmica significava o fenômeno de força e energia produzindo movimento, segundo leis que se exprimiam por equações diferenciais tendo o tempo como variável independente. Mais tarde, dinâmica passou a representar qualquer fenômeno, físico, biológico ou até mesmo econômico, que fosse descrito por equações diferenciais.


  • dinâmica de eventos discretos. Existem atualmente inúmeros sistemas artificiais que não se descrevem por essas equações. Suas variáveis internas e de saída alteram-se sempre como consequência de variações quase instantâneas das entradas e de certos sensores internos, obedecendo a rígidas regras de causa e efeito, assumindo somente valores pertencentes a um conjunto finito, como, por exemplo, {0, 1}, {desligado, ligado}, {todos os números inteiros entre –100 e +100}. Exemplos: circuitos de chaves elétricas e temporizadores, estoques de peças, sistemas de partida e proteção de processos industriais. Devido ao papel representado pelas regras causais internas, tais sistemas são em parte modeláveis por lógica e por álgebra de Boole; por isso são ditos também sistemas lógicos ou logísticos. Mas seus melhores modelos matemáticos são os autômatos finitos e as redes de Petri.


  É tal a diferença entre essas duas dinâmicas, do ponto de vista dos seus modelos matemáticos, dos seus controles automáticos e das teorias associadas, que dois sugestivos nomes estão se firmando na engenharia:


  
    • sistemas conduzidos pelo tempo (time driven) para a primeira e


    • sistemas conduzidos por eventos (event driven) para a segunda.

  


  É evidente que a expressão "conduzidos pelo tempo" não significa que o tempo é a causa dos fenômenos. Significa apenas que a dinâmica do processo manifesta seus efeitos obrigatoriamente no desenrolar do tempo.


  O controle automático dos sistemas dinâmicos tradicionais, abreviadamente chamado de controle dinâmico, emprega o importante conceito da realimentação ou retroalimentação (feedback), que se realiza usualmente por eletrônica analógica ou digital (Figura 1.1 (a)). O controle automático dos sistemas com dinâmica de eventos discretos, abreviadamente dito controle de eventos, é feito por meio de outro sistema de eventos discretos que atualmente, em geral, se realiza por meio de eletrônica digital (Figura 1.1 (b)).


   [img:Illustration] 


  Figura 1.1 (a) Controle dinâmico. (b) Controle de eventos discretos.


  Cabe observar que na prática é impossível estabelecer um sistema de controle dinâmico sem o auxílio de um controle de eventos discretos destinado a dar partida no sistema dinâmico (start-up) e a protegê-lo de sobrecargas. Já o controle de eventos discretos pode ser unicamente de eventos discretos, como, por exemplo, o controle de um terminal bancário.


  Automação é outro termo ligado ao controle automático, isto é, aos equipamentos que substituem o homem em suas tarefas. Vem do neologismo em inglês automation, criado pela indústria em meados do século XX, em conexão com o controle dinâmico e com a eletrônica. Hoje significa simplesmente a presença de um computador num processo industrial ou comercial, com múltiplas funções, como está indicado na Figura 1.2.


   [img:Illustration] 


  Figura 1.2 Esquema da automação de um processo.


  

### 1.2 Realimentação


  Controlar a saída de uma planta ou de um processo por realimentação significa aplicar na sua entrada, após conveniente amplificação, o sinal resultante da diferença entre o valor desejado e o valor medido da saída. Geralmente, entre a comparação e a amplificação de potência é necessário tratar o sinal de uma forma muito especial. Este tratamento é realizado pelo controlador, que consiste numa das maiores responsabilidades da engenharia de controle. Normalmente o comparador e o controlador são implementados num único equipamento industrial ou num único programa computacional.


  Para ilustrar o que se demanda de um controlador automático, coloque-se o leitor na função de controlador manual do sistema da Figura 1.3.


   [img:Illustration] 


  Figura 1.3 Controle manual.


  Situado numa sala fechada, onde existem apenas um instrumento que mede a saída Y e um potenciômetro que aplica o sinal M ao processo, o leitor tem a função de manter o ponteiro do medidor no centro da sua escala, sabendo apenas que girar o botão do potenciômetro para a direita leva, devido aos equipamentos externos, a desvios finais do ponteiro também para a direita.


  Suponha, por exemplo, que o ponteiro comece a mover-se do centro para a esquerda. A reação do leitor será girar o botão para a direita, lentamente. Se porém, o ponteiro ainda continuar para a esquerda, o leitor apressar-se-á. Suponha que finalmente o ponteiro reaja e retorne na direção do centro. Quando ele parece que vai ultrapassar o centro, é a vez de o leitor girar o botão ao contrário, isto é, para a esquerda. Talvez então já se tenha uma intuição da reação do processo externo à sala e já se possa modular a ação sobre o botão com maior eficácia. Pode ser que reações muito rápidas sejam as mais indicadas, ou pode ser que as lentas e firmes sejam as melhores.


  Este exemplo mostra que um bom projeto do controlador deve absorver o conhecimento não apenas do objetivo de reduzir o erro, mas também das características dinâmicas do processo controlado e das amplitudes e frequências das perturbações atuantes no processo. As primeiras são resumidas, em engenharia, no modelo matemático do processo; as últimas são parte importante da especificação do sistema de controle.


  A Figura 1.4 ilustra os componentes fundamentais de um sistema de controle dinâmico em malha fechada (com realimentação), com as seguintes variáveis envolvidas:


  
    R: entrada ou referência ou set-point;


    Y : saída do processo ou planta;


    M : variável manipulada (entrada do amplificador ou atuador);


    E = R – Ym: erro atuante.


    Ym: saída medida com a mesma unidade de R.

  


   [img:Illustration] 


  Figura 1.4 Diagrama de blocos de um sistema em malha fechada.


  Normalmente a saída Y do processo é uma grandeza física, e para que esta possa ser comparada com a referência R é necessário convertê-la numa variável Ym com a mesma unidade de R. O elemento responsável por desempenhar esta função é o transdutor de medida ou sensor.


  

### 1.3 Um pouco de história


  Embora hoje se possa identificar, por toda parte, a presença de mecanismos de realimentação, os sistemas de controle inventados pelo homem antes do século XIX foram muito poucos. Os mais antigos foram os reguladores de nível de água por meio de válvulas acionadas por boias.


  O relógio de água de Ctesibius (Figura 1.5) foi inventado no período entre 300 e 0 a.C. Preferidos até o século XVII, os relógios de água consistiam em um reservatório com nível estabilizado por boia e com um orifício na base. Por causa do nível constante, o fluxo de saída também era constante; acumulando este fluxo em um segundo reservatório, dotado de escala vertical, o nível deste último indicava na escala o tempo decorrido.


  Mas a realimentação esteve na base da invenção que foi fundamental para a Revolução Industrial acontecer. Teve portanto extraodinário impacto econômico e social. Trata-se do Regulador de Velocidade para Motores a Vapor, criado por James Watt no final do século XVIII. É totalmente mecânico, conforme representado na Figura 1.6. De acordo com esta figura, o vapor empurra o pistão para cima, ao mesmo tempo em que uma válvula corrediça também é posicionada na parte superior da máquina a vapor. Quando o pistão atinge a posição superior, a válvula corrediça é empurrada para baixo. Dessa forma inverte-se o fluxo de vapor nos tubos T1 e T2, e o pistão é empurrado para baixo. Esse movimento de subida e descida do pistão faz girar uma roda com velocidade V, que é acoplada ao seu eixo. O eixo vertical A do regulador é movido com velocidade angular ω. Sobre as massas m agem então duas forças, a centrífuga, horizontal, e a da gravidade, vertical. Projetadas sobre a normal à barra b, que liga essas massas ao eixo A, as forças R e Ym se opõem.


   [img:Illustration] 


  Figura 1.5 Relógio de água de Ctesibius.


   [img:Illustration] 


  Figura 1.6 Regulador de velocidade de motores a vapor de James Watt.


  Se a velocidade de rotação ω é excessiva, a barra b gira para cima, as massas m se afastam do eixo A e o tubo B sobe, reduzindo o fluxo de vapor para o motor. As velocidades V do motor e ω do regulador são então reduzidas. Se a velocidade ω é baixa, o processo se inverte, o motor ganha mais vapor e aumenta a velocidade. Dependendo dos arranjos e dimensões dos componentes, as massas m tendem a estacionar em uma posição intermediária e o motor, em uma dada velocidade. Ocorre, assim, uma regulação automática da velocidade. Não é fácil identificar neste regulador as variáveis básicas dos sistemas a realimentação, pois o erro atuante E é a diferença entre as projeções das forças peso e centrífuga da massa m. A projeção da força peso é a referência R, e a projeção da força centrífuga é a variável Ym de medida da saída Y . A posição do tubo B representa a variável manipulada M, e a válvula de vapor representa um amplificador de potência.


  Nas primeiras décadas do século XX a telefonia a grandes distâncias exigia amplificadores eletrônicos de elevado ganho e boa fidelidade na reprodução de voz, qualidades que só podiam ser obtidas com realimentação de sinal em torno de amplificadores eletrônicos. Tornou-se mais agudo um problema que já se apresentava nos reguladores de Watt, que é a tendência a gerar oscilações indesejadas.


  A teoria da realimentação começa em 1868 com Maxwell, analisando as condições para se produzirem oscilações em sistemas descritos por equações diferenciais ordinárias lineares. Em 1877, Routh e Hurwitz criaram um critério algébrico sobre os coeficientes de equações diferenciais para garantir a existência ou não de oscilações. Mas foi somente em 1932, nas pesquisas da Bell Systems, que finalmente Nyquist estabeleceu o seu famoso Critério de Estabilidade, para que engenheiros passassem a projetar sistemas a realimentação com segurança.


  Importantes contribuições à teoria da realimentação têm-se apoiado, de maneira muito criativa, nas matemáticas. Muitos outros pesquisadores se notabilizaram: Liapunov (estabilidade não linear, 1896), Minorsky (1922), Evans (root locus, 1950), Wiener (controle ótimo Linear Quadrático Gaussiano ou LQG, em cerca de 1945), Kochenburger (1950), Pontriagin (controle ótimo, em cerca de 1950), Bellman (controle ótimo, em cerca de 1950) e Kalman (LQG, 1960). Alguns trabalhos consideraram os fenômenos via respostas em frequência, outros via respostas temporais. Ainda hoje, é preciso elaborar os projetos com ambos os instrumentos. Com os trabalhos de Pontriagin e Kalman, ficaram evidentes as extraordinárias qualidades da realimentação das variáveis de estado do objeto controlado.


  O papel fundamental do controle automático na realização dos voos espaciais trouxe ao centro das atenções o computador, como controlador de múltiplas variáveis de saída e como calculador on-line de trajetórias e manobras ótimas. No ambiente industrial, o computador digital logo também interessou como meio de controle, embora por outras razões: a facilidade de registrar fatos e dados de produção e de comunicar-se com operadores e com a administração geral. Mas o computador opera sobre números e exige desligamento do mundo externo enquanto os processa. Então, do ponto de vista do controle dinâmico ele só pode medir e atuar em instantes discretos, o que exige teorias de modelagem e controle adequadas para sistemas de tempo discreto.


  

### 1.4 Modelos matemáticos


  O aperfeiçoamento das teorias de controle leva naturalmente à expectativa de se atingirem objetivos de desempenho mais ambiciosos. No entanto, toda aplicação das teorias ao mundo real depende da fidelidade dos modelos matemáticos adotados. Daí a importância das técnicas de obtenção de modelos matemáticos na engenharia de controle.


  Existem duas abordagens que, nos casos mais complexos, se complementam.


  

### Métodos estruturalistas


  Identificam-se os mecanismos fundamentais em ação (físicos, químicos, mecânicos, etc.). Medemse os parâmetros (coeficientes de transmissão, de reação, de inércia, de atrito, etc.), por ensaios específicos ou por estimativas usuais dos projetistas dos equipamentos. Depois estabelecem-se as equações diferenciais, ou de diferenças, descritivas daqueles mecanismos.


  Por exemplo, se o processo é um motor com engrenagem redutora e carga de inércia e atrito, calcula-se a inércia rotacional referida ao eixo do motor, a partir das dimensões e das densidades das partes, medem-se os atritos e os torques eventuais "de carga". Depois, monta-se a equação diferencial que liga o torque do motor à velocidade do seu eixo.


  

### Métodos globalistas


  Ignorando fenômenos internos, mede-se o desempenho global, isto é, registram-se a entrada e a saída que são pertinentes ao controle automático desejado. Em geral, aplicam-se à entrada sinais convenientes (degrau, impulso ou senoide). Em processos mais complexos ou perigosos registramse os sinais normais de operação e depois aplica-se alguma técnica gráfica ou computacional, de origem matemática ou estatística, para estimar os parâmetros da equação diferencial que interliga ou justifica os dois registros.


  No exemplo anterior, este método implica aplicar ao motor um degrau de tensão e em registrálo junto com a consequente evolução da velocidade do eixo. Pode-se mostrar que, plotando esta evolução versus tempo, com ordenadas em escala logarítmica, ficam aparentes os parâmetros da equação diferencial procurada. Uma alternativa é ajustar os parâmetros de uma equação diferencial genérica, que minimiza o erro médio quadrático em relação à resposta medida.


  Na literatura de controle os métodos globalistas são chamados de identificação de sistemas.


  

### 1.5 Motivações técnicas e econômicas


  O emprego do controle automático (realimentação) objetiva um desempenho técnico específico, em que uma variável física deve obedecer a um sinal de referência e resistir a perturbações mais ou menos definidas, desempenho esse que costuma ser essencial para se atingirem metas mais abrangentes, usualmente de natureza econômica.


  Quanto ao desempenho técnico, há duas grandes famílias de aplicações ou problemas, designadas como controle de posição e controle de processos. A primeira refere-se ao controle de posição ou de velocidade de objetos, tais como: aeronaves, lançadores de satélites, automóveis, submarinos, lentos e precisos radiotelescópios, minúsculos leitores de CDs, discos rígidos, robôs industriais ou de cirurgia, etc. A segunda, controle de processos, refere-se à regulação de processos industriais, como: siderurgia, celulose, cimento, petróleo, químico, álcool, alimentos, medicamentos, etc. Embora as teorias da realimentação sejam válidas para ambos os campos de aplicação, há em cada um dificuldades específicas que levam, na prática, a uma especialização de engenheiros e de modos de comunicação técnica.


  Dado que este livro enfatiza como atingir as especificações de desempenho para os sistemas, neste capítulo inicial cabe posicionar melhor o seu potencial econômico. No controle de posição, o fator econômico leva, em geral, à busca de solução com dispêndio limitado ou energia mínima. Por isso, desde meados do século passado têm evoluído teorias de projeto que minimizam um funcional J do tipo


   [img:Illustration] 


  sendo e(t) o erro da variável controlada no instante t, u(t) o esforço de controle sobre o objeto controlado e λ uma constante positiva de ponderação do erro versus esforço de controle. Tais teorias são vitais, por exemplo, em missões espaciais.


  No controle de processos, o aspecto benefícios versus custos de investimento e de operação foi muito bem analisado em casos reais em [37]. Por exemplo, no caso de uma refinaria de petróleo o custo do investimento foi compensado pelos benefícios em apenas um ano de operação.


  É fácil entender a origem dos benefícios, considerando a operação industrial sob a óptica estatística. Considere, por exemplo, uma planta de papel em que o contrato de um dado produto costuma exigir como qualidade mínima uma espessura de papel maior ou igual a Ymin (Figura 1.7).


   [img:Illustration] 


  Figura 1.7 Processo de papel. (a) e (c) Regulação manual. (b) e (d) Regulação automática.


  A planta, regulada manualmente ou mal regulada automaticamente, produz uma espessura y1(t) de média Y1, conforme a Figura 1.7 (a). Com um bom sistema de controle é produzida a espessura y2(t) de média Y2, conforme a Figura 1.7 (b). Um resumo estatístico da questão, mostrando a distribuição amostral das espessuras, é apresentado nas Figuras 1.7 (c) e 1.7 (d). Note que como resultado do bom controle, a média Y2 é menor que Y1 e consequentemente há uma economia de material.


  Considere ainda um caso em que o processo opera perto da sua capacidade máxima de produção Qmax. A análise é semelhante: a produção média do processo regulado Q2 é maior que a do não regulado Q1. Consequentemente, a melhoria do controle proporciona um lucro de venda maior.


  

### 1.6 Variedades de controle


  Dizem-se analógicos os sinais de tempo contínuo, isto é, os que existem em qualquer instante de tempo no intervalo de observação. Dizem-se amostrados ou de tempo discreto os sinais que resultam dos analógicos por um processo de amostragem no tempo. E são chamados de digitais os sinais amostrados cujas amplitudes são convertidas por algum código digital, isto é, formado por zeros e uns.


  É tão abrangente no mundo atual a penetração dos computadores, sejam os de uso geral, sejam os controladores programáveis ou os microprocessadores dedicados, que, na prática, dificilmente se encontram transdutores de medida e controladores que não sejam digitais. No entanto, na realidade os indicadores de qualidade de desempenho continuam referidos às variáveis físicas, que são analógicas. Como as teorias fundamentais partem desse tipo de sinais, o mais comum é que o projeto do controlador seja feito como analógico e depois seja convertido em algoritmo digital para ser executado em computador. Para projetos mais exigentes há também técnicas de projeto diretamente em algoritmo digital, que estão apresentadas nos Capítulos 9 a 11.


  

### 1.7 O controle dinâmico inserido na automação


  É esclarecedor visualizar o controle por realimentação como parte de um sistema de automação, de amplo escopo e com vários níveis de hierarquia (Figura 1.8).


   [img:Illustration] 


  Figura 1.8 Hierarquia da automação.


  Por um lado, cada malha de controle (nível 1) se comunica com um processo físico, por exemplo um veículo, um reator químico ou uma coluna de destilação, via medidores e atuadores. De outro lado, ela recebe o sinal de referência não de um operador, mas de um outro computador (nível 2). Este, também de controle dinâmico, coordena os sinais de referência de várias malhas, de acordo com a fase de operação em que se está, que é definida por um computador de controle de eventos discretos (nível 3). O controlador de eventos faz a chamada automação operacional: comanda as operações de partida (start-up), de proteção contra sobrecargas e falhas, além das de implementação de receitas de produção ou de operação, que foram desenvolvidas de antemão para o processo. Essas receitas provêm de um nível 4, de computação off-line, em que se otimizam pontos de trabalho dos processos físicos ou trajetórias de veículos. Acima deles ainda se pode encontrar, nos grandes sistemas de automação, o nível 5, de planejamento da produção ou da operação do transporte, em função de pedidos e clientes.


  

### Exemplo 1.1


  Níveis de hierarquia num sistema de automação aeronáutica:


  Nível 1: servomecanismos eletro-hidráulicos das superfícies de ação aerodinâmica; reguladores das fontes de pressão hidráulica e dos geradores elétricos; reguladores dos motores de propulsão e dos condicionadores de ar, etc.


  Nível 2: coordenação multivariável das várias superfícies aerodinâmicas a partir de comandos do piloto ou do piloto automático.


  Nível 3: sequência de ligações de todos os subsistemas do processo, com segurança; alarmes de sobrecarga; medidores de recursos de voo; intertravamento de operações.


  Nível 4: estabelecimento dos trajetos viáveis e econômicos, dados de origem e destino.


  Nível 5: definição do programa de voos e escalas a partir da demanda dos clientes.


  ■


  

### Exemplo 1.2


  Níveis de hierarquia para automação de uma coluna de destilação:


  Nível 1: reguladores dos níveis dos tanques auxiliares para manutenção da operação; reguladores dos fluxos de entrada, do combustível de aquecimento, do refluxo e da saída leve.


  Nível 2: coordenação multivariável dos fluxos para manter as concentrações e produções nos valores desejados.


  Nível 3: sequência de ligações de todos os subsistemas do processo, com segurança; alarmes de sobrecarga e de falta de suprimentos à coluna.


  Nível 4: cálculos e simulações para fixar as concentrações e os fluxos de saída possíveis e econômicos, em função da qualidade do insumo e do equipamento disponível.


  Nível 5: programa de produção para atender a demandas.


  ■


  

### 1.8 Desenvolvimento de projetos


  Poucas áreas da engenharia contam com tantas teorias matemáticas quanto a do controle dinâmico, especialmente quando os modelos dos processos controlados são lineares. No entanto, deficiências inevitáveis dos modelos e do conhecimento dos sinais, além de limitações das teorias, levam ao fato de que o desenvolvimento completo de um controlador real consiste em cálculos, simulações, experimentos em escala reduzida em protótipos e, finalmente, ensaios na realização final.


  O processo de desenvolvimento inclui obrigatoriamente muitas escolhas, influenciadas pela experiência passada em problemas semelhantes e muitas revisões, baseadas em avaliações de conflitos, como desempenho versus realizabilidade física e desempenho versus custo.


  Por exemplo, uma escolha inicial do transdutor de medida da variável principal a ser controlada, de baixo custo, pode limitar o desempenho e ser recusada já nos pré-cálculos teóricos. Um transdutor mais rápido ou mais preciso e mais caro pode ser necessário. Limitações de custo, de peso ou de dimensões podem até mesmo, em certos casos, levar a uma atenuação das especificações.


  A Figura 1.9 resume as possíveis etapas e revisões do desenvolvimento do projeto de um sistema de controle.


   [img:Illustration] 


  Figura 1.9 Etapas do desenvolvimento do projeto de um sistema de controle.


  

### 1.9 Projeto auxiliado por computador


  Com o desenvolvimento de programas especializados, a engenharia de controle dinâmico tem alcançado um alto grau de amadurecimento nas últimas décadas, facilitando a utilização das técnicas de projeto de que este livro trata.


  Além disso, tais programas permitem simulações que são essenciais para a validação e a documentação de projetos, analisando inclusive aspectos como robustez a flutuações no processo controlado e efeitos de não linearidades.


  O programa mais conhecido é o MATLAB da MathWorks, atualmente muito utilizado em várias universidades nacionais e internacionais. Todos os projetos e simulações deste livro foram realizados por meio de pacotes de controle e de simulação de sistemas (Control System Toolbox e Simulink) do MATLAB. Por outro lado, os resultados apresentados também podem ser reproduzidos por meio de outros programas computacionais.


  Como alternativas importantes podem ser citados, por exemplo, os programas gratuitos OCTAVE e SCILAB ([51]).


  A Escola Politécnica da USP relata experiências muito bem sucedidas com o emprego sistemático do MATLAB, obtidas em atividades de ensino e pesquisa nos cursos de graduação e pós-graduação.



<!-- Text/chapter02.xhtml -->





  
  Controle Automático, 2ª edição
  
  



  

## 2


  

## Sistemas Dinâmicos


  

### 2.1 Introdução


  Normalmente, os processos dinâmicos de tempo contínuo são descritos por meio de equações diferenciais. Na abordagem clássica da engenharia de controle essas equações são reduzidas a equações diferenciais lineares, invariantes no tempo e com coeficientes constantes. Para facilitar o estudo dos processos utiliza-se a transformada de Laplace, que visa transformar essas equações diferenciais em equações algébricas de mais simples tratamento matemático.


  Neste capítulo são apresentados os seguintes tópicos: uma breve introdução das técnicas de modelagem por meio de equações diferenciais, a transformada de Laplace e as suas principais propriedades, o conceito de função de transferência e a representação de sistemas na forma de diagramas de blocos.


  

### 2.2 Modelos matemáticos diferenciais


  Modelos matemáticos são sempre idealizações do comportamento dos sistemas reais, válidas apenas para excitações dentro de certos limites de amplitude e de frequência. Na medida em que esses limites se ampliam cresce a complexidade dos modelos.


  Por exemplo, considere o sistema formado de um corpo metálico preso a uma extremidade de uma mola, cuja outra extremidade está engastada no solo. Para baixas frequências e pequenas amplitudes das forças aplicadas ao corpo o sistema pode ser descrito por meio de apenas duas variáveis (posição e velocidade da massa em relação ao solo) obedecendo a uma equação diferencial ordinária, linear, de coeficientes constantes, de segunda ordem. Se as forças são de frequência suficientemente alta, pode ser essencial considerar que a mola tem massa e flexibilidade distribuídas ao longo de seu comprimento e, neste caso, a equação será diferencial de derivadas parciais. Eventualmente, essa mola distribuída poderia ser aproximada por um número de massas e molas menores, conectadas sequencialmente, e a equação resultante seria ordinária de ordem mais elevada. Se as forças são de frequência baixa e de amplitude suficientemente elevada, pode ocorrer um comportamento não linear da mola, isto é, seus deslocamentos podem deixar de ser proporcionais às forças em jogo. Neste caso, a equação diferencial será ordinária não linear.


  É importante distinguir entre equações constitutivas, equações de equilíbrio e equações de conservação ou balanço de massa e energia. As equações constitutivas exprimem propriedades constitutivas dos componentes do sistema; por exemplo, o elongamento de uma mola é proporcional à força de tração. As equações de equilíbrio são meios eficientes para exprimir o balanço energético em situações específicas; por exemplo, a soma das correntes em um nó de um circuito elétrico deve ser zero. As equações de conservação ou balanço exprimem o equilíbrio obrigatório das quantidades de massa ou de energia em jogo nos componentes e nos sistemas: a massa, ou a energia, armazenada num sistema isolado é sempre igual à produzida internamente, mais a que entra e menos a que sai.


  Sistemas e equações são lineares quando a resposta à soma de dois sinais quaisquer é igual à soma das respostas dos sinais. Por exemplo, equações diferenciais de coeficientes constantes são lineares. Outro exemplo é a equação algébrica y(x) = ax, com a constante.


  A equação y(x) = ax + b, com a e b constantes, embora representável no plano (x, y) por uma reta, não é linear. De fato,


   [img:Illustration] 


  

#### 2.2.1 Equações constitutivas


  Na montagem de equações diferenciais de componentes de sistemas são geralmente úteis os conceitos de variáveis "através" e variáveis "sobre". Considere o circuito elétrico da Figura 2.1. A corrente i(t) que entra no resistor R é obrigatoriamente igual à que sai; por isso a corrente é dita uma variável "através" de R. Em oposição, a tensão elétrica v(t) no resistor é medida por diferença entre os potenciais nos terminais do resistor: é uma variável "sobre" R.


   [img:Illustration] 


  Figura 2.1 Circuito elétrico exemplificando as variáveis "através" e "sobre".


  Analogamente, o torque aplicado a uma mola torcional é variável "através" porque é igualmente mensurável nas duas extremidades. Já a distorção angular da mola é variável "sobre", pois é a diferença de posições angulares. A Tabela 2.1 estende esses conceitos a outros sistemas.


  Tabela 2.1 Exemplos de variáveis "através" e "sobre" para componentes de sistemas


  
    
      

      

      
    

    
      
        
          Componente

        

        
          Variável "através"

        

        
          Variável "sobre"

        
      


      
        
          Elétrico

        

        
          Corrente i(t)

        

        
          Tensão v(t)

        
      


      
        
          Mecânico em translação

        

        
          Força f(t)

        

        
          Velocidade vel(t)

        
      


      
        
          Mecânico em rotação

        

        
          Torque τ(t)

        

        
          Velocidade angular ω(t)

        
      


      
        
          Fluido

        

        
          Vazão volumétrica q(t)

        

        
          Pressão p(t)

        
      


      
        
          Térmico

        

        
          Fluxo térmico φ(t)

        

        
          Temperatura θ(t)

        
      

    
  

  Conforme é apresentado na Tabela 2.2, as leis básicas de vários fenômenos físicos para elementos ideais resultam em equações constitutivas semelhantes. Há três fenômenos fundamentais: o dissipativo de energia, o indutivo e o capacitivo; estes dois últimos são armazenadores de energia. Algumas expressões da Tabela 2.2 podem ser expressas por meio de integrais em vez de derivadas. Por exemplo, no caso da capacitância elétrica tem-se que


   [img:Illustration] 


  sendo v(0) a tensão inicial no capacitor.


  Tabela 2.2 Equações constitutivas de elementos ideais


   [img:Illustration] 


  Além dessas equações, há equações constitutivas especializadas muito comuns no campo da química e da termodinâmica, como, por exemplo,


  
    • velocidade de uma reação química

  


   [img:Illustration] 


  rA é a velocidade da reação que produz o componente A, em função da temperatura θ, dadas as constantes k0, E, R′ e a concentração CA.


  
    • equação de estado de um gás

  


   [img:Illustration] 


  para a pressão P, volume V, à temperatura θ, dadas as constantes n e R′.


  

#### 2.2.2 Equações de equilíbrio


  Diretamente das equações de conservação de energia podem ser deduzidas equações de equilíbrio de forças, conjugados e correntes elétricas.


  

### Exemplo 2.1


  Considere o deslocamento x(t) decorrente de uma força f(t), aplicada num sistema mecânico com massa M, mola com constante k (suposta ideal) e atrito viscoso com constante b (Figura 2.2).


   [img:Illustration] 


  Figura 2.2 Sistema mecânico.


  Aplicando a segunda lei de Newton ao corpo de massa M e considerando as equações da Tabela 2.2, obtém-se a equação diferencial que representa a dinâmica do sistema,


   [img:Illustration] 


  A Equação (2.5) é uma equação diferencial linear de segunda ordem a coeficientes constantes.


  ■


  

### Exemplo 2.2


  Considere o sistema elétrico com resistor, indutor e capacitor (circuito RLC paralelo) da Figura 2.3.


   [img:Illustration] 


  Figura 2.3 Circuito RLC paralelo.


  Aplicando a lei de Kirchhoff das correntes, resulta


   [img:Illustration] 


  Supondo condições iniciais nulas, das expressões da Tabela 2.2, obtém-se


   [img:Illustration] 


  ■


  

### Exemplo 2.3


  Considere um jogo de engrenagens que conecta um motor elétrico à sua carga mecânica, conforme é mostrado na Figura 2.4. Para uma dada potência de acionamento os motores elétricos têm, por natureza, um conjugado nominal mais baixo que o necessário na utilização industrial e uma velocidade nominal mais alta que a necessária. Para resolver esse problema intercala-se um jogo de engrenagens entre o motor e a carga.


   [img:Illustration] 


  Figura 2.4 Jogo de engrenagens entre motor e carga.


  A propriedade essencial de um par de engrenagens é que, nos dentes em contato, a velocidade e a força são as mesmas para os dois rotores, embora com direções opostas. Sendo ωm(t) e ωc(t) as velocidades angulares do motor e da carga, respectivamente, então


   [img:Illustration] 


  em que r é o raio da engrenagem no eixo do motor e R o raio da engrenagem no eixo da carga.


  A razão n dos raios nominais das rodas de engrenagens é dada por


   [img:Illustration] 


  Como a força produzida nos dentes de contato do motor fm(t) e da carga fc(t) é a mesma, então a equação de equilíbrio dinâmico rotacional pode ser escrita como


   [img:Illustration] 


  sendo:


  τm(t) e τc(t) os torques do motor e da carga;


  Jm e Jc as inércias do motor e da carga, respectivamente.


  Usando a relação (2.9), a Equação (2.10) pode ser escrita como


   [img:Illustration] 


  Uma regra mnemônica que facilita a modelagem de sistemas dinâmicos com engrenagens é:


  
    • inércias no eixo da carga são "refletidas" no eixo do motor, divididas por n2;


    • conjugados resistentes no eixo da carga são "refletidos" no motor, divididos por n.

  


  Se o interesse do analista é modelar o comportamento das posições angulares instantâneas θm(t), como é o caso dos servomecanismos, que são controladores de posição, então a Equação (2.11) resulta como


   [img:Illustration] 


  Se os dentes das engrenagens não têm nenhuma folga, o atrito entre eles provocará desgastes excessivos; havendo folga há um comportamento não linear sempre que o movimento passa de acelerado para freado e vice-versa, pois um dente-motor percorre a folga e vai pressionar outro dente da roda da carga, acarretando um problema chamado de histerese.


  ■


  

#### 2.2.3 Equações de conservação ou balanço de massa e energia


  Há sistemas das mais variadas constituições, baseados em variados fenômenos físicos, químicos, térmicos e outros. Por isso é bom ter um método de trabalho uniforme, como é o caso das equações de conservação ou balanço de massa e energia. O primeiro passo é identificar uma superfície fechada Σ, que separa o interior do exterior do sistema. Aplica-se, então, o princípio genérico da conservação


   [img:Illustration] 


  sendo que ACUMULAÇÃO e GERAÇÃO ocorrem no interior de Σ, enquanto ENTRADA e SAÍDA, através de Σ.


  
    • Conservação de massa total

  


   [img:Illustration] 


  • Conservação de massa por componente


   [img:Illustration] 


  • Conservação de energia


  Energia em sistemas termodinâmicos é tema complexo, especialmente quando envolve mudanças de estado ou de energia mecânica. Simplificadamente, pode-se considerar


   [img:Illustration] 


  sendo: E a energia interna; Q o calor transferido através de Σ e W o trabalho fornecido pelo sistema através de Σ.


  

### Exemplo 2.4


  Considere um aquecedor de ambiente por meio de resistores elétricos distribuídos sob o piso, conforme representado na Figura 2.5. As variáveis e constantes indicadas são


  φ(t): fluxo de calor injetado no ambiente;


  φs(t): fluxo perdido ou ganho pelas paredes para o exterior;


  θ(t): temperatura média do ambiente;


  θs(t): temperatura externa;


  Cθ : capacitância térmica do ambiente;


  Rθ : resistência térmica das paredes.


   [img:Illustration] 


  Figura 2.5 Aquecedor.


  Das fórmulas da Tabela 2.2 e do balanço térmico do ambiente resulta


   [img:Illustration] 


  Conhecidas as funções φ(t) e θs(t), a temperatura θ(t) é a solução de uma equação diferencial de primeira ordem.


  ■


  

### Exemplo 2.5


  Deseja-se modelar o tanque misturador industrial da Figura 2.6, em que o fluido de entrada tem concentração variável de sal X0(t) (kg/m3) e o fluido de saída tem concentração de sal X(t) (kg/m3). Estando o tanque cheio, a vazão de entrada F (m3/s) é constante e igual à vazão de saída. O agitador é suposto muito eficiente, de maneira que o conteúdo do tanque tem concentração de sal igual à da saída.


   [img:Illustration] 


  Figura 2.6 Esquema de um tanque misturador industrial.


  Da Equação (2.14) tem-se que a conservação de massa de sal, no intervalo de tempo dt, é


   [img:Illustration] 


  Logo, o modelo do misturador é dado pela equação diferencial


   [img:Illustration] 


  ■


  

### Exemplo 2.6


  Considere o esquema do sistema térmico da Figura 2.7, composto por um tanque com um agitador e um aquecedor no seu interior.


   [img:Illustration] 


  Figura 2.7 Sistema térmico.


  O tanque tem volume constante V (m3) e é fechado. Um líquido frio entra no tanque na temperatura constante θi (oC) e sai quente na temperatura θ(t) (oC), ambos na mesma taxa F (m3/s). O líquido possui capacidade térmica C (cal/(oC m3)) e é aquecido no interior do tanque por meio de uma resistência elétrica com fluxo de energia Qh(t) (cal/s).


  O agitador é considerado muito eficiente, de maneira que a temperatura no interior do tanque é homogeneizada instantaneamente em todo o volume V . Esta aproximação é necessária para que o processo seja modelável por parâmetros concentrados.


  Supondo que não há transferência de calor de dentro para fora e de fora para dentro do tanque, da equação de conservação de energia (2.16) tem-se que


   [img:Illustration] 


  O fenômeno energético importante é o calor, de modo que a energia armazenada no tanque é


   [img:Illustration] 


  Da Equação (2.20) obtém-se


   [img:Illustration] 


  Se a temperatura θ(t) for definida como saída do sistema e o fluxo de calor Qh(t) for definido como entrada, o modelo resultante é não linear, devido à presença da parcela constante CFθi. Fazendo a troca de variáveis θs(t) = θ(t) – θi, obtém-se o seguinte modelo linear


   [img:Illustration] 


  ■


  

### 2.3 Transformada de Laplace


  Na engenharia de controle, em vez da solução tradicional das equações diferenciais lineares emprega-se a transformada de Laplace. A transformada de Laplace converte equações diferenciais na variável real t em equações algébricas na variável complexa s. A vantagem em usar a transformada de Laplace é que as equações algébricas resultantes são mais simples de serem estudadas que as equações diferenciais originais. A solução das equações diferenciais por meio da transformada de Laplace segue a estrutura da Figura 2.8.


   [img:Illustration] 


  Figura 2.8 Etapas empregadas na solução de equações diferenciais lineares.


  A resposta de um sistema linear depende dos parâmetros do próprio sistema e pode ser sempre decomposta em duas partes: uma parte associada apenas às condições iniciais, chamada resposta livre, e outra associada apenas ao sinal de entrada, chamada resposta forçada. A Figura 2.9 resume essas dependências.


   [img:Illustration] 


  Figura 2.9 Dependências da resposta de um sistema linear.


  A transformada de Laplace de uma função f(t), com f(t) = 0 para t < 0, é definida como


   [img:Illustration] 


  sendo f(t) e t reais; F(s) e s complexos.


  A transformada (2.24) é chamada unilateral porque somente se aplica a funções de t que são nulas para t < 0. Existe também a transformada bilateral, usualmente empregada na engenharia de comunicações (Geromel [29]). O limite inferior da integral (2.24) é 0– para permitir que a integral contenha eventuais impulsos na origem.


  É claro que a convergência da integral (2.24), isto é, a existência da transformada de Laplace, depende do valor de s. Seja α o extremo inferior do conjunto de valores que a parte real de s pode assumir, mantendo a convergência; então α é chamada abscissa de convergência absoluta. Prova-se que, para existir a integral da definição (2.24), é suficiente que exista  [img:Illustration] , isto é, que esta integral seja convergente, para algum k real, positivo. O mínimo valor de para o qual ela converge é uma estimativa conservadora da abscissa α.


  

#### 2.3.1 Transformada de Laplace de algumas funções


  

### Degrau unitário


  A função degrau unitário é definida como


   [img:Illustration] 


  O gráfico da função degrau unitário é apresentado na Figura 2.10.


   [img:Illustration] 


  Figura 2.10 Função degrau unitário.


  Aplicando a definição de transformada de Laplace (2.24), obtém-se


   [img:Illustration] 


  

### Exponencial


  A função exponencial é definida como


   [img:Illustration] 


  sendo a uma constante.


  Aplicando a definição de transformada de Laplace (2.24), obtém-se


   [img:Illustration] 


  

### Rampa unitária


  A função rampa unitária é definida como


   [img:Illustration] 


  O gráfico da função rampa unitária é apresentado na Figura 2.11.


   [img:Illustration] 


  Figura 2.11 Função rampa unitária.


  Aplicando a definição de transformada de Laplace (2.24), obtém-se


   [img:Illustration] 


  

### Seno


  A função seno é definida como


   [img:Illustration] 


  em que ω é uma constante real qualquer.


  A função seno também pode ser escrita como


   [img:Illustration] 


  A transformada de Laplace da Equação (2.32) é dada por


   [img:Illustration] 


  Aplicando a transformada de Laplace da função exponencial (2.28) na Equação (2.33), obtém-se


   [img:Illustration] 


  

### Cosseno


  A função cosseno é definida como


   [img:Illustration] 


  em que ω é uma constante real qualquer.


  A função cosseno também pode ser escrita como


   [img:Illustration] 


  A transformada de Laplace da Equação (2.36) é dada por


   [img:Illustration] 


  Analogamente ao caso da função seno, aplicando a transformada de Laplace da função exponencial (2.28) na Equação (2.37), obtém-se


   [img:Illustration] 


  

### Impulso unitário


  A função pulso unitário, representada na Figura 2.12, é dada por


   [img:Illustration] 


  Chama-se unitário porque sua integral de –∞ a +∞ é igual a 1.


   [img:Illustration] 


  Figura 2.12 Função pulso unitário.


  A função impulso1 unitário ou função δ(t) de Dirac é o caso-limite da função pulso quando α → 0, ou seja,


   [img:Illustration] 


  A função impulso unitário "ocorre" apenas em t = 0, com amplitude infinita. Porém, a "área" sob a função é igual a 1. Desse modo, a função impulso unitário também pode ser definida como


   [img:Illustration] 


  Obviamente um sinal com amplitude infinita e duração nula não é fisicamente realizável. Porém, um sinal de amplitude "grande" e duração "pequena", com relação às características de resposta de um sistema, pode ser aproximado pela função impulso.


  A transformada de Laplace da função impulso unitário é dada por


   [img:Illustration] 


  pois o integrando só é não nulo na origem, onde a exponencial vale 1.


  

#### 2.3.2 Propriedades da transformada de Laplace


  

### Linearidade


   [img:Illustration] 


  

### Translação no campo complexo


  Seja a uma constante real ou complexa. Então


   [img:Illustration] 


  

### Mudança de escala de tempo


  Seja a > 0 uma constante. Então


   [img:Illustration] 


  Fazendo a mudança de variável τ = at, obtém-se


   [img:Illustration] 


  

### Translação no tempo


  Seja a ≥ 0 uma constante e f(t) = 0 para t < 0. Então f(t – a) representa o sinal f(t) translacionado "para depois", conforme mostra a Figura 2.13. Sua transformada é


   [img:Illustration] 


  Fazendo a mudança de variável τ = t – a e sabendo-se que f(τ) = 0 para τ < 0, obtém-se


   [img:Illustration] 


   [img:Illustration] 


  Figura 2.13 Funções f(t) e f(t – a).


  É importante observar que, para a < 0, a transformada de Laplace unilateral da função f(t–a) não é definida.


  

### Transformada da derivada de primeira ordem


  Seja f˙(t) a derivada de uma função f(t) com relação ao tempo. Então


   [img:Illustration] 


  Para demonstrar a expressão (2.48) basta aplicar a definição de transformada de Laplace e realizar uma integração por partes, ou seja,


   [img:Illustration] 


  Considerando que para a existência da transformada de Laplace o produto f(t)e–st deve tender a zero quando t tende a infinito, então


   [img:Illustration] 


  

### Transformada da derivada de segunda ordem


  Sendo g(t) = f˙(t), então


   [img:Illustration] 


  Logo,


   [img:Illustration] 


  

### Transformada da derivada de ordem n


  Genericamente


   [img:Illustration] 


  

### Transformada da integral


  Seja


   [img:Illustration] 


  Então,


   [img:Illustration] 


  De fato, da definição (2.52), tem-se que ϕ˙(t) = f(t). Aplicando a transformada da derivada de primeira ordem, obtém-se


   [img:Illustration] 


  

### Convolução geral


  Considere duas funções causais f(t) e g(t), nulas para t < 0. A operação de convolução,2 indicada por f(t) * g(t), é definida como


   [img:Illustration] 


  A transformada de Laplace da Equação (2.55) é dada por


   [img:Illustration] 


  A integral até t pode ser convertida em uma integral até ∞ por meio do seguinte artifício


   [img:Illustration] 


  sendo 1(t – τ) a função degrau unitário que vale 1 para t ≥ τ e zero para t < τ.


  Logo,


   [img:Illustration] 


  Fazendo a mudança de variável u = t – τ e notando que 1(u)f(u) = 0 para u < 0, obtém-se


   [img:Illustration] 


  O resultado (2.59) mostra que a transformada de Laplace da convolução de duas funções é igual ao produto das transformadas de Laplace de suas funções. É importante enfatizar que a transformada de Laplace do produto de duas funções no domínio do tempo é diferente do produto das transformadas de Laplace de suas funções, ou seja,


   [img:Illustration] 


  

#### 2.3.3 Teorema do valor inicial


  O teorema do valor inicial permite determinar o valor inicial de uma função f(t) em t = 0+ (instante mínimo para t positivo) a partir de sua transformada de Laplace. Se existir L[f(t)] = F(s) e se existirem os limites da Equação (2.61), então


   [img:Illustration] 


  Fazendo s → ∞ na transformada da derivada de primeira ordem (2.48), obtém-se


   [img:Illustration] 


  Supondo que f(t) é contínua inclusive na origem,3 então a sua derivada não contém impulsos.


  Logo


   [img:Illustration] 


  Portanto, da Equação (2.62) tem-se que


   [img:Illustration] 


  pois a função f(t) é contínua na origem, por hipótese.


  

#### 2.3.4 Teorema do valor final


  O teorema do valor final permite determinar o valor estacionário de uma função f(t) a partir de sua transformada de Laplace. Se existir L[f(t)] = F(s) e se existirem os limites da Equação (2.65), então


   [img:Illustration] 


  Para mostrar o teorema, basta fazer s → 0 na transformada da derivada de primeira ordem (2.48), ou seja,


   [img:Illustration] 


  Portanto,


   [img:Illustration] 


  Prova-se que este teorema não é válido se F(s) é descontínua em algum ponto de s, tal que ℜ(s) ≥ 0. De fato, quando ℜ(s) > 0, a função f(t) cresce exponencialmente, ao passo que quando ℜ(s) = 0 a função f(t) é composta de senoides e cossenoides. Em ambos os casos não existe o limite da função f(t) quando t tende a infinito.


  

### Exemplo 2.7


  Determine os valores inicial e final da função f(t), correspondente à transformada de Laplace


   [img:Illustration] 


  Pelo teorema do valor inicial (2.61), obtém-se


   [img:Illustration] 


  Pelo teorema do valor final (2.65), obtém-se


   [img:Illustration] 


  O mesmo resultado pode ser obtido observando-se na tabela de transformadas de Laplace (2.3) que


   [img:Illustration] 


  No caso de o denominador da função F(s) ser s(s – 2), o teorema do valor final não fornece o valor correto, pois a função f(t) cresce exponencialmente.


  ■


  Na Tabela 2.3 são apresentadas as transformadas de Laplace de algumas funções.4


  Tabela 2.3 Tabela de transformadas de Laplace


   [img:Illustration] 


  

### 2.4 Função de transferência


  Considere o sistema de tempo contínuo, linear e invariante no tempo, com entrada U(s) e saída Y(s) da Figura 2.14.


   [img:Illustration] 


  Figura 2.14 Função de transferência.


  
    A função de transferência G(s) é definida como o quociente da transformada de Laplace do sinal de saída Y(s) pela transformada de Laplace do seu sinal de entrada U(s), quando todas as condições iniciais são nulas (c.i. = 0), ou seja,


     [img:Illustration] 

  


  A função de transferência G(s) pode ser obtida a partir da equação diferencial que representa a dinâmica do sistema. Suponha que um sistema seja representado pela seguinte equação


   [img:Illustration] 


  Aplicando a transformada de Laplace nos dois membros da Equação (2.73) e supondo condições iniciais nulas,5 obtém-se


   [img:Illustration] 


  Analisando a Equação (2.74), percebe-se que a função de transferência de sistemas lineares com parâmetros concentrados, invariantes no tempo, é uma função racional de s, ou seja, é o quociente de dois polinômios em s, com coeficientes reais. Logo, raízes complexas só podem ocorrer se forem aos pares conjugados.


  Em todos os sistemas físicos reais a resposta não pode preceder à excitação. Em consequência, prova-se que o grau do polinômio do numerador é sempre menor ou igual ao grau do polinômio do denominador de G(s) (m ≤ n).


  Os pontos singulares em que a função G(s) ou suas derivadas tendem ao infinito são chamados de polos de G(s). Já os pontos em que a função G(s) se anula são chamados de zeros de G(s). No caso de G(s) ser racional, como na Equação (2.74), tem-se que


  
    • os polos são as raízes do polinômio do denominador de G(s);


    • os zeros são as raízes do polinômio do numerador de G(s).

  


  A função de transferência G(s) também pode ser escrita em termos de seus polos (p1, p2, ..., pn) e de seus zeros (z1, z2, ..., zm), ou seja,


   [img:Illustration] 


  

### Exemplo 2.8


  Considere a função de transferência


   [img:Illustration] 


  A função de transferência G(s) possui três polos, localizados em s = 0, s = –2–8j e s = –2+8j, e um zero finito localizado em s = –5. A distribuição de polos e zeros no plano s está representada na Figura 2.15. De acordo com esta figura, polos e zeros do plano s são sempre representados pelos símbolos "×" e "∘", respectivamente.


   [img:Illustration] 


  Figura 2.15 Distribuição de polos e zeros no plano s.


  ■


  

### Exemplo 2.9 Sistema de inércia e atrito rotacional


   [img:Illustration] 


  Figura 2.16 Sistema de inércia e atrito rotacional.


  Considere o sistema da Figura 2.16, em que J representa a inércia rotacional e B representa o coeficiente de atrito rotacional. Supondo que a entrada do sistema é o torque τ(t) e que a saída é o deslocamento angular θ(t), a equação diferencial que representa a dinâmica do sistema é dada por


   [img:Illustration] 


  Aplicando a propriedade da derivada e supondo condições iniciais nulas, a transformada de Laplace da Equação (2.77) resulta como


   [img:Illustration] 


  Logo, a função de transferência do sistema é dada por


   [img:Illustration] 


  A função de transferência (2.79) possui dois polos, localizados em s = 0 e em s = –B/J, conforme representado na Figura 2.17.


   [img:Illustration] 


  Figura 2.17 Distribuição de polos e zeros no plano s.


  ■


  

### 2.5 Transformada de Laplace inversa


  A transformada inversa de uma função F(s) para t ≥ 0 é dada por


   [img:Illustration] 


  em que c é um número real tal que a trajetória de integração é uma reta paralela ao eixo imaginário, localizada à direita de todos os polos de F(s).


  Raramente a inversa da transformada de Laplace é calculada pela integral (2.80). A maneira mais simples e usual é utilizando uma tabela de transformadas. No caso de F(s) ser uma função racional de s, isto é, o quociente de dois polinômios que não existe na tabela, a sua consulta deve ser precedida de uma expansão da função F(s) em frações parciais.


  

#### 2.5.1 Expansão em frações parciais


  Considere a função


   [img:Illustration] 


  em que (p1, p2, ..., pn) são os polos de F(s).


  O método da expansão em frações parciais consiste em expandir a função (2.81) em frações que podem ser facilmente identificáveis na tabela de transformadas de Laplace (2.3).


  

### Polos distintos


  Se F(s) possuir apenas polos distintos, então pode-se realizar a seguinte expansão


   [img:Illustration] 


  e cada coeficiente ai(i = 1, 2, ..., n), chamado resíduo de F(s), vale


   [img:Illustration] 


  Da tabela de transformadas de Laplace (2.3) tem-se que


   [img:Illustration] 


  Logo,


   [img:Illustration] 


  

### Exemplo 2.10


  Determine a transformada inversa de Laplace da função


   [img:Illustration] 


  Expandindo F(s) em frações parciais, obtém-se


   [img:Illustration] 


  em que


   [img:Illustration] 


  Portanto,


   [img:Illustration] 


  Da tabela de transformadas de Laplace (2.3) obtém-se


   [img:Illustration] 


  Outra maneira de calcular os coeficientes da expansão em frações parciais é a seguinte:


   [img:Illustration] 


  Identificando os polinômios dos numeradores, tem-se que


   [img:Illustration] 


  Comparando os coeficientes dos dois membros da Equação (2.93), obtém-se a1 = 2 e a2 = –1.


  ■


  

### Exemplo 2.11


  Determine a transformada inversa de Laplace da função


   [img:Illustration] 


  Como o grau do polinômio do numerador é igual ao grau do polinômio do denominador (m = n = 2), então é necessário realizar primeiramente uma divisão polinomial, ou seja,


   [img:Illustration] 


  Da tabela de transformadas de Laplace (2.3) obtém-se


   [img:Illustration] 


  

### Exemplo 2.12


  Determine a transformada inversa de Laplace da função


   [img:Illustration] 


  Expandindo F(s) em frações parciais, obtém-se


   [img:Illustration] 


  sendo


   [img:Illustration] 


  Como os coeficientes de F(s) são reais e os polos são complexos conjugados, pode-se provar que os resíduos correspondentes são complexos conjugados. Então


   [img:Illustration] 


  sendo  [img:Illustration]  o complexo conjugado de a1.


  Portanto,


   [img:Illustration] 


  Da tabela de transformadas de Laplace (2.3) obtém-se


   [img:Illustration] 


  Outra maneira de calcular a transformada inversa quando os polos são complexos conjugados é usar diretamente as funções tabeladas


   [img:Illustration] 


  Escrevendo F(s) no formato das funções tabeladas (2.103) e (2.104), obtém-se


   [img:Illustration] 


  Portanto, a transformada inversa de F(s) é dada por


   [img:Illustration] 


  

### Polos múltiplos


  Se F(s) possuir um polo p com multiplicidade r, então devem ser desenvolvidas r frações, associadas a p, ou seja,


   [img:Illustration] 


  Cada constante bj(j = 1, 2, ..., r) pode ser calculada como


   [img:Illustration] 


  A Equação (2.107) também se aplica no caso de F(s) possuir polos complexos conjugados múltiplos.


  

### Exemplo 2.13


  Determine a transformada inversa de Laplace da função


   [img:Illustration] 


  Note que F(s) possui um polo múltiplo em s = –1, com multiplicidade r = 2. Assim, F(s) pode ser expandida na seguinte soma de frações parciais


   [img:Illustration] 


  sendo


   [img:Illustration] 


  Portanto,


   [img:Illustration] 


  Da tabela de transformadas de Laplace (2.3) obtém-se


   [img:Illustration] 


  Os coeficientes da expansão em frações parciais também podem ser calculados através de uma comparação dos coeficientes do polinômio do numerador, ou seja,


   [img:Illustration] 


  Logo,


   [img:Illustration] 


  Comparando os coeficientes dos dois membros da Equação (2.113), obtém-se o seguinte sistema


   [img:Illustration] 


  Resolvendo o sistema (2.114), obtém-se


   [img:Illustration] 


  ■


  

### 2.6 Diagramas de blocos


  A análise de sistemas em engenharia costuma ser feita a partir de sua representação em diagramas de blocos. A representação convencional de um bloco é realizada por meio de um retângulo, com a função de transferência correspondente escrita em seu interior.


  O diagrama de blocos de um sistema com função de transferência G(s), entrada U(s) e saída Y(s) é apresentado na Figura 2.18.


   [img:Illustration] 


  Figura 2.18 Representação de uma função de transferência.


  A representação da Figura 2.18 mostra que os sinais de entrada e saída estão relacionados por


   [img:Illustration] 


  O sentido dos sinais entre os blocos é indicado por setas. A questão fundamental a ser esclarecida, antes de justapor e interligar dois blocos, é garantir que a ligação não altera o valor da variável intermediária. Em outras palavras, só podem ser interligados blocos quando a impedância de saída do primeiro bloco é pequena com relação à impedância de entrada do segundo bloco. Se esta condição não for satisfeita será necessário calcular a função de transferência global dos dois blocos em conjunto e associá-la a um único bloco.


  Além dos blocos, utilizam-se também símbolos para efetuar a soma ou a subtração algébrica de sinais, conforme é apresentado na Figura 2.19. No domínio do tempo, os sinais a serem somados ou subtraídos devem possuir as mesmas unidades para que o resultado tenha algum significado.


   [img:Illustration] 


  Figura 2.19 Símbolos para somar ou subtrair sinais.


  

### Diagrama de blocos de um sistema em malha fechada


  Na Figura 2.20 é apresentado o diagrama de blocos de um sistema genérico em malha fechada. O sinal "menos" no somador é tradicionalmente adotado nos sistemas de controle em malha fechada, para enfatizar que o controle exige realimentação negativa.


   [img:Illustration] 


  Figura 2.20 Diagrama de blocos de um sistema de controle em malha fechada.


  No diagrama de blocos da Figura 2.20 os seguintes sinais podem ser observados:


  
    R(s): sinal de referência ou set-point ou sinal desejado para a saída;


    Y(s): sinal de saída do sistema G(s);


    E(s): sinal de erro (E(s) = R(s) – X(s) = R(s) – H(s)Y(s));


    X(s): sinal de saída do bloco H(s).

  


  Um sistema de controle está em malha fechada quando o sinal de sua saída é usado para modificar sinais internos, ocorrendo aquilo que se chama de realimentação (feedback) do sinal de saída. Isso é o que se pode verificar no diagrama de blocos da Figura 2.20, onde o sinal de entrada do sistema G(s), que é o sinal de erro E(s), também depende da saída Y(s), pois E(s) = R(s) – H(s)Y(s).


  O bloco H(s) pode representar, por exemplo, a função de transferência de um elemento de medição ou sensor. Supondo que o sinal de referência seja uma tensão elétrica em volts e que o sinal de saída do sistema G(s) seja uma temperatura em graus Celsius, o bloco H(s) tem a função de converter o sinal medido de graus Celsius para volts, compatibilizando as unidades entre os sinais representados por R(s) e X(s).


  

### Função de transferência de malha aberta


  Define-se a função de transferência de malha aberta FTMA(s) como a função que se encontra em cascata, ao percorrer a malha de realimentação, sem considerar o somador. De acordo com o diagrama de blocos da Figura 2.20, a função de transferência de malha aberta FTMA(s) é dada por


   [img:Illustration] 


  

### Função de transferência de malha fechada


  De acordo com o diagrama de blocos da Figura 2.20, tem-se que


   [img:Illustration] 


  Da Equação (2.117), tem-se que a função de transferência de malha fechada FTMF(s) é dada por


   [img:Illustration] 


  
    Regra prática: a função de transferência de malha fechada é igual à função de transferência direta G(s), dividida por um mais a função de transferência de malha aberta G(s)H(s).

  


  No caso de a realimentação ser unitária, então H(s) = 1. Neste caso, a função de transferência de malha fechada é dada por


   [img:Illustration] 


  

### Álgebra de blocos


  Os diagramas de blocos podem ser arranjados utilizando-se regras de equivalência, que constituem a "álgebra" dos diagramas de blocos. A regra fundamental é a dos blocos em cascata da Figura 2.21.


   [img:Illustration] 


  Figura 2.21 Diagrama de blocos em cascata.


  A função de transferência total de dois blocos em cascata é igual ao produto das funções de transferência G1(s) e G2(s) dos blocos isolados. Para justificar esta afirmação basta usar a definição de função de transferência


   [img:Illustration] 


  Algebricamente,


   [img:Illustration] 


  Nas Figuras 2.22 e 2.23 são apresentados alguns diagramas de blocos, sendo os esquemas da esquerda equivalentes aos da direita. A verificação dessas equivalências é feita simplesmente calculando a função de transferência nos dois lados.


   [img:Illustration] 


  Figura 2.22 Diagramas de blocos equivalentes.


   [img:Illustration] 


  Figura 2.23 Diagramas de blocos equivalentes com realimentação.


  

### 2.7 Estudo de caso: motor de corrente contínua


  Os motores de corrente contínua são muito utilizados nas indústrias, pois são empregados para realizar diversos tipos de acionamentos mecânicos.6 A Figura 2.24 representa um esquema de um motor de corrente contínua controlado por armadura.


   [img:Illustration] 


  Figura 2.24 Esquema de um motor de corrente contínua controlado por armadura.


  As variáveis e constantes indicadas na Figura 2.24 são:


  ea(t): tensão de armadura;


  ia(t): corrente de armadura;


  Ra: resistência de armadura;


  La: indutância de armadura;


  ic(t): corrente de campo do motor;


  τ(t): torque do motor;


  θ(t): posição angular do eixo;


  B: atrito angular;


  J : inércia do conjunto formado pelo rotor do motor e pela carga mecânica;


  Kt: constante de proporcionalidade entre o conjugado motor e a corrente de armadura;


  Kv : constante de proporcionalidade entre a força contraeletromotriz gerada pela armadura em rotação e a velocidade angular do eixo.


  As equações que representam a dinâmica do sistema da Figura 2.24 são dadas por


   [img:Illustration] 


  Aplicando a propriedade da derivada e supondo condições iniciais nulas, as transformadas de Laplace das Equações (2.123), (2.124) e (2.125) resultam em


   [img:Illustration] 


  Considerando a tensão de armadura ea(t) como a entrada e θ(t) como a saída do sistema, resulta na seguinte função de transferência:


   [img:Illustration] 


  Em um grande número de situações a indutância La da armadura é muito pequena e os sinais são relativamente lentos, de modo que


   [img:Illustration] 


  Assim, a função de transferência (2.129) pode ser simplificada para


   [img:Illustration] 


  Se a variável de saída for a velocidade angular ω(t) do eixo do motor, ou seja,


   [img:Illustration] 


  então a função de transferência resulta como


   [img:Illustration] 


  sendo


   [img:Illustration] 


  e


   [img:Illustration] 


  

#### 2.7.1 Sistema em malha aberta com torque resistente


  Suponha agora que se deseja estudar o sistema em malha aberta com um torque resistente τc(t) aplicado ao eixo de carga. Por exemplo, num processo de laminação de aço isso equivale ao caso em que o motor está acionando um laminador e a chapa de aço penetra entre os seus cilindros, alterando a velocidade do motor. Considerando desprezível a queda de tensão na indutância La e supondo apenas pequenas variações em torno dos valores nominais de trabalho do motor, então as equações diferenciais do sistema resultam como


   [img:Illustration] 


  Aplicando a transformada de Laplace nas Equações (2.135), (2.136) e (2.137) e supondo condições iniciais nulas, obtém-se


   [img:Illustration] 


  sendo Tc(s) = L[τc(t)].


  Simplificadamente, a Equação (2.138) pode ser escrita como


   [img:Illustration] 


  sendo


   [img:Illustration] 


  Supondo que a tensão de armadura ea(t) é proporcional à velocidade angular de referência ωr(t), isto é,


   [img:Illustration] 


  então,


   [img:Illustration] 


  A partir da Equação (2.141) pode-se estudar o comportamento da velocidade angular do motor quando um torque resistente é aplicado no eixo da carga. A Figura 2.25 apresenta o esquema na forma de diagrama de blocos do sistema em malha aberta.


   [img:Illustration] 


  Figura 2.25 Sistema em malha aberta com torque resistente aplicado no eixo da carga.


  

### Constante de tempo


  A constante de tempo T do sistema em malha aberta é dada por


   [img:Illustration] 


  Portanto, a velocidade da resposta transitória não pode ser alterada, pois a constante de tempo T depende apenas de parâmetros fixos do motor e da carga.


  

### Erro estacionário


  Supondo que as entradas Ωr(s) e Tc(s) do sistema da Figura 2.25 sejam degraus com amplitudes A1 e A2, ou seja, Ωr(s) = A1/s e Tc(s) = A2/s, então a Equação (2.141) pode ser escrita como


   [img:Illustration] 


  O valor estacionário da velocidade angular pode ser calculado através do teorema do valor final (2.65), ou seja,


   [img:Illustration] 


  O erro estacionário e(∞) é dado por


   [img:Illustration] 


  Portanto, o erro estacionário depende de parâmetros fixos do motor e da carga. Pode-se mostrar que reduzir esse erro implica um grande aumento do peso e do custo do motor.


  

#### 2.7.2 Sistema em malha fechada: regulador de velocidade


  O regulador de velocidade visa realizar acionamento mecânico com velocidade estabilizada por meio de um motor elétrico. Para estabilizar a velocidade contra flutuações de tensão e de conjugado de carga recomenda-se naturalmente uma malha de controle automático por realimentação, conforme esquematizado na Figura 2.26.


   [img:Illustration] 


  Figura 2.26 Esquema do sistema em malha fechada.


  O sistema em malha fechada da Figura 2.26 é constituído de


  • um potenciômetro, transdutor da velocidade angular desejada, em rpm, para o sinal elétrico ωr(t), em volts;


  • um tacogerador, transdutor da velocidade angular medida, em rpm, para o sinal elétrico ω(t), em volts;


  • um amplificador de potência, alimentado pela rede elétrica, com ganho igual a Kp ;


  • um controlador com ganho igual a Kc, que tem a função de amplificar o sinal de erro e(t) = ωr(t) – ω(t).


  Supondo por simplicidade que as funções de transferência do tacogerador e do potenciômetro sejam iguais a 1 e que a tensão de armadura seja ea(t) = Ke(t), em que K = KcKp, então o sistema da Figura 2.26 pode ser representado pelo diagrama de blocos da Figura 2.27.


   [img:Illustration] 


  Figura 2.27 Diagrama de blocos do sistema em malha fechada.


  De acordo com o sistema da Figura 2.27 tem-se que


   [img:Illustration] 


  ou


   [img:Illustration] 


  Portanto,


   [img:Illustration] 


  

### Constante de tempo


  De acordo com a Equação (2.148), a constante de tempo Tf do sistema em malha fechada é dada por


   [img:Illustration] 


  Como as constantes T e Km têm valores fixos, para obter uma constante de tempo Tf "pequena" e consequentemente uma velocidade de resposta transitória "rápida" basta aumentar o ganho K através de um aumento do ganho Kc do controlador.


  

### Erro estacionário


  Supondo que as entradas Ωr(s) e Tc(s) do sistema da Figura 2.27 sejam degraus com amplitudes A1 e A2, ou seja, Ωr(s) = A1/s e Tc(s) = A2/s, então a Equação (2.148) pode ser escrita como


   [img:Illustration] 


  O valor estacionário da velocidade angular pode ser calculado através do teorema do valor final (2.65), ou seja,


   [img:Illustration] 


  O erro estacionário e(∞) é dado por


   [img:Illustration] 


  Se o ganho Kc do controlador for ajustado de modo que


  KKm ≫ 1 e KKm ≫ A1 + Kr A2,


  então o erro de regime no estado estacionário será necessariamente "pequeno".


  
    Consequências do controle em malha fechada


    No sistema em malha fechada é possível obter respostas mais rápidas e com erro estacionário "pequeno" através de um ajuste de ganho do controlador.

  


  

### 2.8 Implementação analógica de funções de transferência


  Funções de transferência podem ser implementadas analogicamente por meio de circuitos eletrônicos denominados amplificadores operacionais. Esses circuitos possuem duas entradas (v+(t) e v–(t)) e uma saída vs(t), conforme representado na Figura 2.28.


   [img:Illustration] 


  Figura 2.28 Amplificador operacional.


  O amplificador operacional ideal possui as seguintes características:


  
    • elevada impedância de entrada, para que as entradas do amplificador sejam usadas apenas para observar os sinais, sem consumir e nem fornecer corrente;


    • baixa impedância de saída, para fornecer uma tensão vs(t), independente da carga de saída;


    • tensão de saída vs(t), dada por

  


   [img:Illustration] 


  sendo A um ganho de valor muito elevado (A → ∞).


  Sendo vs(t) uma tensão finita, da Equação (2.153) tem-se que


   [img:Illustration] 


  Como as duas entradas v+(t) e v–(t) são fisicamente distintas, mas com as mesmas tensões, designou-se este estado de curto-circuito virtual.


  

#### 2.8.1 Amplificador inversor


  Considere o circuito com a realimentação negativa por meio da resistência R2, de acordo com a Figura 2.29.


   [img:Illustration] 


  Figura 2.29 Amplificador inversor.


  Como v+(t) = v–(t) e como a entrada v+(t) está ligada ao terra, então v–(t) = 0. Neste caso diz-se que a entrada v–(t) é um terra virtual.


  Do circuito da Figura 2.29 tem-se que a corrente i(t) vale


   [img:Illustration] 


  Devido à alta impedância de entrada, a corrente de entrada no amplificador é nula. Portanto, toda a corrente i(t) passa pela resistência R2. Assim,


   [img:Illustration] 


  Comparando as Equações (2.155) e (2.156), obtém-se


   [img:Illustration] 


  Se R1 = R2, então vs(t) = –ve(t).


  

#### 2.8.2 Amplificador não inversor


  Para evitar que a tensão de saída vs(t) tenha sinal inverso ao da tensão de entrada ve(t) pode-se configurar o amplificador operacional no seu modo não inversor, representado na Figura 2.30.


   [img:Illustration] 


  Figura 2.30 Amplificador não inversor.


  A corrente i(t) vale


   [img:Illustration] 


  Como v+(t) = v–(t) = ve(t), então


   [img:Illustration] 


  Portanto,


   [img:Illustration] 


  

#### 2.8.3 Circuito somador


  O amplificador operacional pode ser empregado para realizar a soma de tensões, de acordo com o esquema na Figura 2.31.


   [img:Illustration] 


  Figura 2.31 Circuito somador.


  Pela lei das correntes de Kirchhoff, tem-se que


   [img:Illustration] 


  Sabendo-se que v+(t) = v–(t) = 0 e empregando a lei de Ohm, obtém-se


   [img:Illustration] 


  ou


   [img:Illustration] 


  Se R = R1 = R2 = R3 = ... = Rn, então


   [img:Illustration] 


  

#### 2.8.4 Circuito integrador


  O circuito eletrônico com amplificador operacional capaz de realizar cálculo integral está representado na Figura 2.32.


   [img:Illustration] 


  Figura 2.32 Circuito integrador.


  A queda de tensão no capacitor vale


   [img:Illustration] 


  Sabendo-se que vs(t) = –vc(t) e supondo tensão inicial nula no capacitor (vc(0) = 0), então


   [img:Illustration] 


  Se RC = 1, obtém-se


   [img:Illustration] 


  

#### 2.8.5 Circuito diferenciador


  Para obter um circuito diferenciador basta trocar de lugar a resistência pelo capacitor no circuito integrador. O circuito diferenciador resultante é apresentado na Figura 2.33.


   [img:Illustration] 


  Figura 2.33 Circuito diferenciador.


  A corrente no capacitor vale


   [img:Illustration] 


  Logo,


   [img:Illustration] 


  Se RC = 1, obtém-se


   [img:Illustration] 


  Suponha, por exemplo, que a tensão de entrada seja ve(t) = sen ωt. Da Equação (2.170) tem-se que vs(t) = –ω cos ωt, ou seja, a amplitude da tensão de saída é proporcional à frequência ω do sinal de entrada. Se esta frequência for elevada, então a amplitude da tensão de saída também será elevada. Por esta razão o circuito diferenciador não é muito usado na prática, pois este amplifica ruídos de alta frequência presentes na maioria dos instrumentos de medição.


  

#### 2.8.6 Sistemas de primeira ordem


  Considere um sistema de primeira ordem com entrada U(s), saída Y(s) e com função de transferência


   [img:Illustration] 


  sendo que K e p são constantes. A equação diferencial correspondente é


   [img:Illustration] 


  O circuito eletrônico correspondente à Equação (2.172) é apresentado na Figura 2.34. Neste circuito supõe-se que K = R/R1, p = R/R2 e RC = 1.


   [img:Illustration] 


  Figura 2.34 Circuito eletrônico correspondente a um sistema de primeira ordem.


  

#### 2.8.7 Sistemas de segunda ordem


  Considere um sistema de segunda ordem com entrada U(s), saída Y(s) e com função de transferência


   [img:Illustration] 


  sendo K, a1 e a0 constantes. A equação diferencial correspondente é


   [img:Illustration] 


  O circuito eletrônico correspondente à Equação (2.174) é apresentado na Figura 2.35. Neste circuito supõe-se que K = R/R1, a1 = R/R2, a0 = R/R3 e RC = 1.


   [img:Illustration] 


  Figura 2.35 Circuito eletrônico correspondente a um sistema de segunda ordem.


  

#### 2.8.8 Impedâncias complexas


  A impedância complexa Z(s) entre os terminais do circuito elétrico da Figura 2.36 é igual à divisão da transformada de Laplace da tensão V(s) pela transformada de Laplace da corrente I(s), supondo condições iniciais nulas, ou seja,


   [img:Illustration] 


   [img:Illustration] 


  Figura 2.36 Circuito elétrico com dois terminais.


  Se o componente entre os terminais for uma resistência R, então


   [img:Illustration] 


  Se o componente entre os terminais for um capacitor C, com tensão inicial nula, então


   [img:Illustration] 


  Se o componente entre os terminais for uma indutância L, com corrente inicial nula, então


   [img:Illustration] 


  O circuito eletrônico com amplificador operacional na configuração inversora da Figura 2.37 pode ser empregado para implementar controladores com diversos tipos de funções de transferência. Para isso basta fazer uma escolha adequada das impedâncias Z1(s) e Z2(s).


   [img:Illustration] 


  Figura 2.37 Configuração de um amplificador inversor para implementar uma função de transferência.


  Usando procedimento análogo ao realizado no domínio do tempo a função de transferência do circuito, que relaciona a transformada de Laplace da tensão de saída Vs(s) com a transformada de Laplace da tensão de entrada Ve(s), é dada por


   [img:Illustration] 


  

### 2.9 Exercícios resolvidos


  

### Exercício 2.1


  Considere o circuito elétrico RLC série da Figura 2.38.


   [img:Illustration] 


  Figura 2.38 Circuito elétrico RLC série.


  Supondo que a entrada do circuito é a tensão v(t) e que a saída é a tensão vc(t) no capacitor, determine a função de transferência G(s), conforme representado na Figura 2.39.


   [img:Illustration] 


  Figura 2.39 Função de transferência.


  Solução


  Aplicando a lei de Kirchhoff, obtém-se


   [img:Illustration] 


  Sabendo-se que a corrente i(t) é dada por


   [img:Illustration] 


  então,


   [img:Illustration] 


  Aplicando a transformada de Laplace na Equação (2.182) com condições iniciais nulas, obtém-se


   [img:Illustration] 


  Logo, a função de transferência G(s) é dada por


   [img:Illustration] 


  

### Exercício 2.2


  Considere um tanque de um processo industrial, conforme representado na Figura 2.40.


   [img:Illustration] 


  Figura 2.40 Tanque industrial.


  As variáveis envolvidas no sistema são:


  qe(t): desvio do fluxo de entrada em relação ao seu valor em regime estacionário (m3/min);


  qs(t): desvio do fluxo de saída em relação ao seu valor em regime estacionário (m3/min);


  h(t): desvio na altura do nível em relação ao seu valor em regime estacionário (m);


  C: capacitância correspondente à área da superfície de líquido no tanque (m2);


  R: resistência ao fluxo de líquido na tubulação (min/m2).


  Em um pequeno intervalo de tempo dt o volume de líquido acumulado no tanque é Cdh(t), que deve ser igual ao volume de líquido de entrada menos o volume de líquido de saída, ou seja,


   [img:Illustration] 


  Sabe-se que a taxa de fluxo qs(t) através da restrição de saída é proporcional (K) à raiz quadrada da altura h(t) da coluna de líquido, ou seja,


   [img:Illustration] 


  Porém, para pequenas variações de fluxo qs(t) em torno de um ponto de trabalho pode-se linearizar a função (2.186) e obter7


   [img:Illustration] 


  em que R é uma constante que pode ser determinada experimentalmente.


  Das Equações (2.187) e (2.185) obtém-se


   [img:Illustration] 


  Supondo que a saída do sistema a ser controlada é o nível do tanque h(t) e que a entrada é o fluxo qe(t), aplicando a transformada de Laplace na Equação (2.188), obtém-se a seguinte função de transferência H(s)


   [img:Illustration] 


  Por outro lado, supondo que a saída do sistema seja o fluxo qs(t), em vez do nível h(t), e como H(s) = RQs(s), então a função de transferência resulta como


   [img:Illustration] 


  

### Exercício 2.3


  Considere o sistema da Figura 2.41.


   [img:Illustration] 


  Figura 2.41 Sistema G(s).


  Sabendo-se que


   [img:Illustration] 


  determine a resposta da saída y(t) quando a entrada u(t) for um degrau unitário.


  Solução


  Da definição de função de transferência (2.72), tem-se que


   [img:Illustration] 


  Como u(t) é um degrau unitário, então U(s) = 1/s. Assim,


   [img:Illustration] 


  Note que a função Y(s) possui um par de polos complexos conjugados e dois polos na origem (multiplicidade r = 2). A expansão em frações parciais dos polos complexos conjugados pode ser realizada através de uma combinação das funções tabeladas


   [img:Illustration] 


  Expandindo a função Y(s), obtém-se


   [img:Illustration] 


  Logo,


   [img:Illustration] 


  Comparando os coeficientes dos dois membros da Equação (2.113), obtém-se o seguinte sistema


   [img:Illustration] 


  A solução do sistema (2.198) resulta como


   [img:Illustration] 


  Da tabela de transformadas de Laplace obtém-se


   [img:Illustration] 


  

### Exercício 2.4


  Determine a função de transferência Vs(s)/Ve(s) do sistema da Figura 2.42 e calcule a resposta temporal vs(t) quando ve(t) é um degrau unitário. Suponha condições iniciais nulas.


   [img:Illustration] 


  Figura 2.42 Sistema com amplificadores operacionais.


  Solução


  As impedâncias Z1(s) e Zs(s) são dadas, respectivamente, por


   [img:Illustration] 


  Da Equação (2.179) obtém-se a função de transferência


   [img:Illustration] 


  Quando a entrada do circuito é um degrau unitário, então Ve(s) = 1/s. Então


   [img:Illustration] 


  Expandindo Vs(s) em frações parciais, obtém-se


   [img:Illustration] 


  com


   [img:Illustration] 


  Portanto


   [img:Illustration] 


  Supondo R1C1 ≠ R2C2, da tabela de transformadas de Laplace (2.3) obtém-se


   [img:Illustration] 


  

### Exercício 2.5


  Sabendo-se que o circuito eletrônico com amplificadores operacionais da Figura 2.43 representa o diagrama de blocos do sistema em malha fechada da Figura 2.44, calcule:


  a) o ganho K e a constante de tempo T, em função dos componentes passivos do circuito;


  b) o valor final da saída vs(∞), quando é aplicado um degrau unitário na entrada ve(t).


   [img:Illustration] 


  Figura 2.43 Sistema em malha fechada com amplificadores operacionais.


   [img:Illustration] 


  Figura 2.44 Diagrama de blocos do sistema em malha fechada.


  Solução


  Da Figura 2.43 tem-se que


   [img:Illustration] 


  Do diagrama em blocos da Figura 2.44 tem-se que


   [img:Illustration] 


  Comparando as Equações (2.212) e (2.213), obtém-se K = 1 e T = RC.


  A função de transferência do sistema em malha fechada é dada por


   [img:Illustration] 


  Sabendo-se que a entrada ve(t) é um degrau unitário (Ve(s) = 1/s), do teorema do valor final (2.65) tem-se que


   [img:Illustration] 


  

### 2.10 Exercícios propostos


  

### Exercício 2.6


  Considere o sistema de suspensão de um cesto por meio de uma polia, conforme representado na Figura 2.45.


   [img:Illustration] 


  Figura 2.45 Sistema de suspensão de um cesto por meio de uma polia.


  Sabe-se que o cesto tem massa M, a polia tem momento de inércia J, raio externo r e atrito desprezível. Impondo o equilíbrio de forças verticais no cesto e o equlíbrio de conjugados na polia, mostre que o movimento vertical do cesto é descrito pela seguinte equação diferencial:


   [img:Illustration] 


  sendo g a aceleração da gravidade.


  

### Exercício 2.7


  Deduza a equação diferencial que modela o tanque misturador de líquido do Exemplo 2.5, supondo que nele ocorre uma reação química interna que produz o sal à taxa r = –kX(t) [ kg/(m3s) ], com k constante. Suponha que a reação química tenha efeito térmico desprezível.


  

### Exercício 2.8


  Determine a função de transferência Qs2(s)/Qe1(s) do sistema com dois tanques interligados da Figura 2.46, em termos das constantes R1, R2, C1 e C2. Suponha para pequenas variações que


   [img:Illustration] 


   [img:Illustration] 


  Figura 2.46 Dois tanques interligados.


  

### Exercício 2.9


  Considere o sistema mecânico da Figura 2.47 com massa M, constante de mola k e constante de amortecedor b.


   [img:Illustration] 


  Figura 2.47 Sistema mecânico.


  Sendo x1(t) e x2(t) deslocamentos e f(t) a força aplicada, determine as funções de transferência X1(s)/F(s), X2(s)/X1(s) e X2(s)/F(s).


  

### Exercício 2.10


  Determine a função de transferência Θm(s)/Tm(s) do sistema com engrenagens da Figura 2.48, sabendo-se que: τm(t) é o torque do motor; θm(t) é a posição angular do eixo do motor; Jm é o momento de inércia do motor; θA(t) é a posição angular do eixo da carga; JA é o momento de inércia da carga; K é uma constante de torção; B é o coeficiente de amortecimento e n é o fator de redução das engrenagens.


   [img:Illustration] 


  Figura 2.48 Sistema com engrenagens.


  

### Exercício 2.11


  Calcule as transformadas de Laplace das seguintes funções:


  
    a) f(t) = e–at sen ωt ;


    b) f(t) = e–at cos ωt .

  


  

### Exercício 2.12


  Determine a transformada inversa de Laplace das funções:


   [img:Illustration] 


  

### Exercício 2.13


  Determine as funções de transferência de cada um dos sistemas da rede RC da Figura 2.49. Suponha que a entrada seja a tensão ve(t) e que a saída seja a tensão vs(t).


   [img:Illustration] 


  Figura 2.49 Sistemas de rede RC.


  

### Exercício 2.14


  Resolva as seguintes equações diferenciais usando a transformada de Laplace:


   [img:Illustration] 


  

### Exercício 2.15


  Desenhe os esquemas dos circuitos analógicos correspondentes às seguintes equações diferenciais:


   [img:Illustration] 


  

### Exercício 2.16


  Um servomecanismo foi acoplado a um microscópio, como ilustrado na Figura 2.50, para realizar o controle da posição de uma plataforma de testes de circuitos integrados.


   [img:Illustration] 


  Figura 2.50 Servomecanismo acoplado a microscópio para controle da posição de uma plataforma de testes de circuitos integrados.


  O servomecanismo é composto por um motor de corrente contínua, com realimentação tacométrica da velocidade ω(t), cujo diagrama de blocos está representado na Figura 2.51.


   [img:Illustration] 


  Figura 2.51 Servomecanismo com realimentação tacométrica de velocidade.


  
    Aplicando-se um degrau unitário na entrada θr(t), calcule:


    a) a função de transferência do sistema em malha fechada θ(s)/θr(s);


    b) a resposta temporal θ(t) da posição angular;


    c) o valor final θ(∞) da posição angular.

  


  

### Exercício 2.17


  Determine a função de transferência Y(s)/R(s) do sistema da Figura 2.52 e calcule os valores inicial e final de y(t) quando R(s) for um degrau unitário.


   [img:Illustration] 


  Figura 2.52 Sistema com realimentação.


  

### Exercício 2.18


  Considere o sistema da Figura 2.53.


   [img:Illustration] 


  Figura 2.53 Sistema com entrada de referência R(s) e de perturbação P(s).


  a) Determine as funções de transferência:


   [img:Illustration] 


  b) Sabendo-se que R(s) e P(s) são entradas do tipo degrau unitário, calcule os valores estacionários y(∞) e e(∞) nos casos do item anterior.


  

### Exercício 2.19


  Determine a função de transferência Y(s)/R(s) do diagrama de blocos da Figura 2.54.


   [img:Illustration] 


  Figura 2.54 Diagrama de blocos de um sistema com múltiplos laços.


  

### Exercício 2.20


  Determine a função de transferência Vs(s)/Ve(s) do sistema da Figura 2.55 e calcule a resposta temporal vs(t) quando ve(t) é um degrau unitário. Suponha condições iniciais nulas.


   [img:Illustration] 


  Figura 2.55 Sistema com amplificadores operacionais.


  


  __________


  1A função impulso pertence à classe de funções chamadas de generalizadas. Por simplicidade, esta é apresentada aqui de maneira intuitiva, sem o devido rigor matemático.


  2A operação de convolução é fundamental na teoria dos sistemas lineares: se f(t) é o sinal de entrada e g(t) é a resposta do sistema ao impulso unitário, então, a convolução f(t) * g(t) é a saída do sistema.


  3A demonstração para funções descontínuas na origem pode ser encontrada em Orsini [50].


  4Os coeficientes a, b, c, d, n, ω, ωn e ξ são constantes e f(t) = 0 para t < 0.


  5A exigência de condições iniciais nulas é essencial para garantir a unicidade da função de transferência.


  6Recentemente a tecnologia dos motores de indução, energizados por conversores eletrônicos de frequência variável, tem substituído a dos motores de corrente contínua em muitas aplicações. As constantes de tempo elétricas dessa nova tecnologia são menores que as da anterior, mas os resultados da sua análise dinâmica são inteiramente análogos aos desta seção.


  7Ver Seção 9.10.1.



<!-- Text/chapter03.xhtml -->





  
  Controle Automático, 2ª edição
  
  



  

## 3


  

## Análise no Domínio do Tempo


  

### 3.1 Introdução


  Uma das especificações usuais, empregadas na análise de sistemas de controle dinâmico, é a sua resposta temporal quando sinais particulares são aplicados a suas entradas. Normalmente estes são sinais simples, tais como impulso, degrau, rampa e sinal senoidal, cujas transformadas de Laplace são funções racionais.


  Neste capítulo é apresentada a definição de estabilidade de sistemas lineares e o critério de Routh, que permite determinar faixas de valores para os parâmetros da função de transferência do sistema, para que o mesmo seja estável. Em seguida são apresentadas as respostas transitórias de sistemas de primeira e segunda ordens e as suas principais características de desempenho. Por fim são estudados o comportamento do erro no estado estacionário e alguns índices de desempenho, consagrados na engenharia de controle, tais como sobressinal, tempo de subida, tempo de acomodação, etc.


  

### 3.2 Estabilidade de sistemas lineares


  Estabilidade é um objetivo fundamental em qualquer projeto de engenharia de sistemas. Sem estabilidade de alguma variável significativa pode-se afirmar que o sistema não tem utilidade industrial. Mesmo no caso de um oscilador eletrônico para radiotransmissão que, de certo ponto de vista, pode ser classificado como instável, mas cuja utilidade prática requer a estabilidade da frequência e da amplitude da oscilação do sinal.


  Para sistemas lineares é sempre adotado o conceito de estabilidade BIBO (Bounded Input Bounded Output), que é definida impondo uma condição sobre a amplitude do sinal de saída dada uma condição sobre a amplitude do sinal de entrada.


  
    Um sistema linear é BIBO estável se qualquer sinal de entrada com amplitude finita (bounded) produz sinal de saída com amplitude também finita (bounded).

  


  A palavra qualquer na definição anterior é fundamental e tem o objetivo de assegurar que num sistema estável BIBO nenhum sinal de saída do sistema pode disparar em amplitude sem que haja uma excitação intencional, uma entrada de amplitude não limitada. A estabilidade BIBO é, portanto, um requisito prático de segurança, de utilidade operacional do sistema.


  Para sistemas não lineares outros conceitos de estabilidade são necessários, mas sempre resultam em segurança e previsibilidade de comportamento.


  

#### 3.2.1 Teorema da estabilidade linear


  O teorema, enunciado a seguir e provado em Geromel [29], tem extraordinária importância em engenharia de controle.


  
    Teorema 3.1 Um sistema linear invariante no tempo é BIBO estável se e somente se todos os polos de sua função de transferência estão localizados no semiplano esquerdo aberto do plano s, excluído o eixo imaginário.

  


  Na Figura 3.1 está representada em cor cinza a "região estável" do plano s.


   [img:Illustration] 


  Figura 3.1 "Região estável" do plano s.


  

### Exemplo 3.1


  Considere o sistema linear da Figura 3.2.


   [img:Illustration] 


  Figura 3.2 Sistema linear.


  A função de transferência G(s) é dada por


   [img:Illustration] 


  • Se a > 0 o sistema G(s) é BIBO estável, pois o seu polo está localizado no semiplano esquerdo aberto do plano s.


  • Se a < 0 o sistema G(s) é BIBO instável, pois o seu polo está localizado no semiplano direito aberto do plano s.


  Aplicando na entrada U(s) do sistema um sinal com amplitude finita como, por exemplo, um degrau unitário, obtém-se


   [img:Illustration] 


  Expandindo Y(s) em frações parciais, obtém-se


   [img:Illustration] 


  A transformada de Laplace inversa da Equação (3.3) é dada por


   [img:Illustration] 


  • Se a > 0, a resposta (3.4) possui uma exponencial decrescente. O sinal com amplitude finita (degrau unitário), aplicado na entrada do sistema, produz um sinal de saída também com amplitude finita, pois para t tendendo a infinito y(∞) = 1.


  • Se a < 0, a resposta (3.4) possui uma exponencial crescente. O sinal com amplitude finita (degrau unitário), aplicado na entrada do sistema, produz um sinal de saída com amplitude ilimitada, pois para t tendendo a infinito y(∞) = ∞.


  Portanto, o sistema é BIBO estável para a > 0 e BIBO instável para a < 0.


  ■


  

### Exemplo 3.2


  Supondo que a função de transferência do sistema da Figura 3.2 seja


   [img:Illustration] 


  então o sistema G(s) é BIBO instável, pois os seus polos (s1 = +j e s2 = –j) estão localizados sobre o eixo imaginário do plano s.


  Justificativa: aplicando-se em G(s) uma entrada com amplitude finita como, por exemplo, um sinal cossenoidal u(t) = cos t ⇒ U(s) = s/(s2 + 1), resulta


   [img:Illustration] 


  Da tabela de transformadas de Laplace obtém-se


   [img:Illustration] 


  que é um sinal de amplitude não finita.


  Logo, em sistemas com polos sobre o eixo imaginário um sinal com amplitude finita pode produzir uma saída com amplitude ilimitada. Portanto, tais sistemas são BIBO instáveis.


  O caso de polos no eixo imaginário corresponde na prática aos sistemas ressonantes com perdas de energia desprezíveis como, por exemplo, as estruturas mecânicas. Como se sabe da experiência, aplicando um sinal na frequência da ressonância, por pequeno que seja, a amplitude da resposta tende a infinito.


  ■


  

### 3.3 Critério de estabilidade de Routh


  Considere um sistema com função de transferência G(s) dada por


   [img:Illustration] 


  sendo N(s) e D(s) correspondentes ao numerador e ao denominador de G(s), respectivamente.


  O critério de Routh1 permite determinar quantos polos da função de transferência G(s) pertencem ao semiplano direito aberto do plano s, sem precisar calcular as raízes do polinômio D(s). Portanto, este critério permite determinar se o sistema G(s) é ou não estável.


  Para isso, primeiramente escreva o polinômio característico D(s) na forma


   [img:Illustration] 


  
    Condição 1: Se no polinômio D(s) estiver faltando algum dos coeficientes ai(i = 0, 1, 2, . . ., n), isto é, se D(s) tiver algum coeficiente ai = 0 ou se todos os coeficientes ai não tiverem o mesmo sinal, então pode-se concluir imediatamente que o sistema G(s) é BIBO instável. Caso contrário, deve-se verificar a condição 2.

  


  
    Condição 2: Se todos os coeficientes ai do polinômio D(s) estiverem presentes, isto é, se nenhum deles for nulo e se todos os coeficientes tiverem o mesmo sinal (todos positivos ou todos negativos), então deve-se organizar os coeficientes de acordo com a tabela de Routh 3.1. O sistema G(s) é BIBO estável se todos os elementos da primeira coluna de coeficientes da tabela de Routh tiverem o mesmo sinal. Caso contrário, o sistema G(s) é BIBO instável. Esta é uma condição necessária e suficiente para determinar se G(s) é BIBO estável ou instável.

  


  Tabela 3.1 Tabela de Routh


   [img:Illustration] 


  Os coeficientes (bi, ci, . . .) da tabela de Routh são calculados como


   [img:Illustration] 


  
    Critério de Routh: o número de raízes com parte real positiva é igual ao número de mudanças de sinal dos elementos da primeira coluna de coeficientes da tabela de Routh.

  


  Caso algum coeficiente calculado da primeira coluna da tabela de Routh (b1, c1,...) seja nulo, então o sistema também é BIBO instável.


  Uma importante aplicação do critério de Routh é na determinação da estabilidade de um sistema quando há um ou mais parâmetros variáveis, como por exemplo, o ganho de um controlador.


  

### Exemplo 3.3


  Considere um sistema com função de transferência


   [img:Illustration] 


  O polinômio do denominador de G(s) é dado por


   [img:Illustration] 


  
    • Se a = 0, um dos coeficientes do polinômio D(s) é nulo e com isso o sistema G(s) é BIBO instável.


    • Se a < 0, um dos coeficientes do polinômio D(s) tem sinal trocado e com isso o sistema G(s) é BIBO instável.


    • Se a > 0, para determinar se o sistema G(s) é estável ou instável é necessário montar a tabela de Routh 3.2.

  


  Tabela 3.2 Tabela de Routh


   [img:Illustration] 


  Os coeficientes b1, b2 e c1 da tabela de Routh são calculados como


   [img:Illustration] 


  Todos os coeficientes da primeira coluna da tabela de Routh têm o mesmo sinal quando


   [img:Illustration] 


  Portanto, o sistema G(s) é BIBO estável se e somente se a >  [img:illustration] .


  Para 0 < a <  [img:Illustration]  ocorrem duas mudanças de sinal na primeira coluna de coeficientes da tabela de Routh, isto é, uma mudança da linha s2 para s1 e outra mudança da linha s1 para s0. Isso significa que o sistema tem dois polos no semiplano direito aberto do plano s. Portanto, nesse caso G(s) é BIBO instável.


  Note que, para a =  [img:Illustration] , o coeficiente b1 é igual a zero e com isso todos os elementos da terceira linha da tabela são nulos. Pode-se verificar neste exemplo que G(s) resulta com dois polos sobre o eixo imaginário. Logo, para a =  [img:Illustration]  o sistema G(s) é BIBO instável.


  ■


  

### 3.4 Sistemas de primeira ordem


  Seja um sistema linear de primeira ordem, conforme representado na Figura 3.3.


   [img:Illustration] 


  Figura 3.3 Sistema linear de primeira ordem.


  A função de transferência G(s) do sistema da Figura 3.3 é dada por


   [img:Illustration] 


  sendo T > 0 chamada de constante de tempo do sistema.


  

#### 3.4.1 Resposta ao impulso


  Fisicamente o impulso é um pulso de duração muito pequena e serve para descrever uma variável física que só se altera durante um intervalo de tempo desprezível como, por exemplo, nos fenômenos de choque mecânico. Considerando que é fisicamente impossível a resposta de qualquer sistema real anteceder ao sinal que o excita, toda resposta ao impulso deve ser nula para t < 0. Esta é a chamada condição de realizabilidade física.


  Quando a entrada do sistema da Figura 3.3 é um impulso unitário, isto é u(t) = δ(t), então U(s) = 1. Da Equação (3.16) tem-se que


   [img:Illustration] 


  Portanto, a resposta temporal y(t) da saída do sistema é dada por


   [img:Illustration] 


  O gráfico da resposta ao impulso unitário para T > 0 é apresentado na Figura 3.4.


   [img:Illustration] 


  Figura 3.4 Resposta ao impulso unitário de um sistema de primeira ordem.


  Como a transformada de Laplace da resposta ao impulso Y(s) é a própria função de transferência G(s) do sistema, um registro experimental da resposta ao impulso permitiria estimar a constante de tempo T do sistema: T seria o tempo decorrido da aplicação do impulso até a resposta reduzir-se a 0,368 do valor inicial.


  No entanto, devido à possibilidade de ocorrência de ruídos coincidentes com o momento da medida a qualidade desta identificação é menos segura que a de outros métodos.


  

#### 3.4.2 Resposta ao degrau


  Quando a entrada do sistema da Figura 3.3 é um degrau de amplitude A, isto é, u(t) = A para t ≥ 0, então U(s) = A/s. Da Equação (3.16) tem-se que


   [img:Illustration] 


  cuja transformada inversa fornece a resposta ao degrau y(t), dada por


   [img:Illustration] 


  O gráfico da resposta ao degrau para T > 0 é apresentado na Figura 3.5.


   [img:Illustration] 


  Figura 3.5 Resposta ao degrau de um sistema de primeira ordem.


  Uma das características importantes dessa resposta é que em t = T o valor da resposta é y(T) = 0,632A, ou seja, a resposta y(t) alcança 63,2% de sua variação final. Fisicamente, no instante T a principal parte da energia ou do significado da resposta já ocorreu. Por isso T é chamada de constante de tempo do sistema. Quanto menor for a constante de tempo, mais rápida é a resposta do sistema.


  O valor final da saída quando t tende a infinito é dado por


   [img:Illustration] 


  Logo,


   [img:Illustration] 


  Aplicando o logaritmo natural ao módulo dos membros da Equação (3.22), obtém-se


   [img:Illustration] 


  A expressão (3.23) representa a equação de uma reta, conforme representado na Figura 3.6.


   [img:Illustration] 


  Figura 3.6 Gráfico de ln y(t) – y(∞)| em função de t.


  Portanto, para se determinar experimentalmente se um sistema é ou não de primeira ordem e qual é a sua constante de tempo T basta desenhar o gráfico de ln |y(t) – y(∞)| em função de t. Se a curva obtida se aproximar de uma reta, então o sistema é de primeira ordem e a inclinação da reta é igual a –1/T.


  O tempo de subida tr(rise time) de sistemas de primeira ordem é definido como o tempo para a resposta ao degrau ir de 10% a 90% do seu valor final, conforme é mostrado na Figura 3.7.


   [img:Illustration] 


  Figura 3.7 Tempo de subida tr de um sistema de primeira ordem.


  O tempo de subida tr também serve para estimar a constante de tempo T. Sendo t1 e t2 os instantes em que a resposta vale 0,1A e 0,9A, respectivamente, então


   [img:Illustration] 


  ou


   [img:Illustration] 


  Dividindo a Equação (3.26) pela Equação (3.27), obtém-se


   [img:Illustration] 


  Como tr = t2 – t1,


   [img:Illustration] 


  

#### 3.4.3 Resposta à rampa


  Quando a entrada do sistema da Figura 3.3 é uma rampa unitária, isto é u(t) = t para t ≥ 0, então U(s) = 1/s2. Da Equação (3.16) tem-se que


   [img:Illustration] 


  cuja transformada inversa é dada por


   [img:Illustration] 


  Para T > 0, o gráfico da resposta y(t) para entrada rampa unitária é apresentado na Figura 3.8.


   [img:Illustration] 


  Figura 3.8 Resposta y(t) para entrada rampa unitária r(t).


  O erro e(t) entre a entrada u(t) e a saída y(t) do sistema é dado por


   [img:Illustration] 


  Logo, o erro no estado estacionário vale


   [img:Illustration] 


  Portanto, quanto menor for a constante de tempo T menor será o erro e(∞) no estado estacionário e mais rápido será o transitório da saída y(t).


  Analisando-se as respostas (3.18), (3.20) e (3.31), conclui-se que:


  
    • a resposta ao impulso unitário é igual à derivada da resposta ao degrau unitário (A = 1);


    • a resposta ao degrau unitário (A = 1) é igual à derivada da resposta à rampa unitária.

  


  

### 3.5 Sistemas de segunda ordem


  Considere um sistema de segunda ordem normalizado para ganho unitário quando s = 0, conforme representado na Figura 3.9.


   [img:Illustration] 


  Figura 3.9 Sistema de segunda ordem.


  A função de transferência G(s) do sistema da Figura 3.9 é dada por


   [img:Illustration] 


  O comportamento dinâmico dos sistemas de segunda ordem é determinado inteiramente pelos parâmetros ξ e ωn. O coeficiente ωn > 0 é a frequência natural não amortecida e ξ é o coeficiente de amortecimento.


  Os polos s1 e s2 da função de transferência (3.34) são


   [img:Illustration] 


  Para que o sistema seja estável é necessário que os polos s1 e s2 estejam localizados no semiplano esquerdo aberto do plano s, isto é, o coeficiente de amortecimento ξ > 0 pode assumir os seguintes valores:


  
    • 0 < ξ < 1: os polos s1 e s2 são complexos conjugados e o sistema é dito subamortecido;


    • ξ = 1: os polos s1 e s2 são reais e iguais e diz-se que o sistema tem amortecimento crítico;


    • ξ > 1: os polos s1 e s2 são reais e diferentes e o sistema é superamortecido ou sobreamortecido.

  


  Se ξ = 0, o sistema não é estável e a resposta do sistema é oscilatória, isto é, sem amortecimento.


  A seguir são estudadas as respostas ao degrau unitário para cada um desses casos.


  

#### 3.5.1 Sistema subamortecido: 0 < ξ < 1


  Para 0 < ξ < 1 os polos do sistema são complexos conjugados, ou seja,


   [img:Illustration] 


  sendo  [img:Illustration]  chamada de frequência natural amortecida. Os polos do sistema estão representados na Figura 3.10.


   [img:Illustration] 


  Figura 3.10 Polos complexos conjugados.


  Nota-se na Figura 3.10 que o coeficiente de amortecimento ξ é dado por


   [img:Illustration] 


  Quando a entrada do sistema da Figura 3.9 é um degrau unitário, isto é U(s) = 1/s, tem-se da Equação (3.34) que


   [img:Illustration] 


  Expandindo Y(s), obtém-se


   [img:Illustration] 


  Da tabela de transformadas de Laplace obtém-se a resposta do sistema


   [img:Illustration] 


  ou


   [img:Illustration] 


  Na Figura 3.11 é apresentado o gráfico da resposta ao degrau para ξ = 0,3.


   [img:Illustration] 


  Figura 3.11 Resposta ao degrau para ξ = 0,3.


  Analisando-se o gráfico da Figura 3.11 pode-se perceber que a resposta y(t) é uma oscilação amortecida com frequência ωd e as envoltórias da oscilação são exponenciais com constante de tempo T = 1/ξωn. Nota-se também que o valor estacionário da saída é y(∞) = 1, ou seja, a saída tende a seguir a entrada u(t).


  

#### 3.5.2 Sistema oscilatório: ξ = 0


  Quando o coeficiente de amortecimento é nulo, os polos do sistema (3.34) são complexos conjugados (s1 = jωn, s2 = –jωn) e estão localizados sobre o eixo imaginário, conforme representado na Figura 3.12.


   [img:Illustration] 


  Figura 3.12 Polos complexos conjugados sobre o eixo imaginário.


  Fazendo ξ = 0 na Equação (3.38), a transformada de Laplace da saída Y(s) resulta


   [img:Illustration] 


  Logo,


   [img:Illustration] 


  O gráfico da resposta ao degrau é apresentado na Figura 3.13. Analisando-se este gráfico podese perceber que a resposta y(t) não tem amortecimento, ou seja, é uma oscilação senoidal com frequência natural ωn. Daí a denominação de ωn ser chamada de frequência natural não amortecida. Nesse caso pode-se dizer que o transitório não decai ou que só existe resposta permanente.


   [img:Illustration] 


  Figura 3.13 Resposta ao degrau para ξ = 0.


  

#### 3.5.3 Sistema com amortecimento crítico: ξ = 1


  Quando ξ = 1, a função de transferência (3.34) resulta


   [img:Illustration] 


  Nesse caso a função de transferência tem dois polos reais negativos e iguais a –ωn, conforme representado na Figura 3.14.


   [img:Illustration] 


  Figura 3.14 Polo duplo em ωn.


  Fazendo U(s) = 1/s na Equação (3.44), obtém-se


   [img:Illustration] 


  Logo,


   [img:Illustration] 


  Na Figura 3.15 é apresentado o gráfico da resposta ao degrau para ξ = 1.


   [img:Illustration] 


  Figura 3.15 Resposta ao degrau para ξ = 1.


  Analisando-se o gráfico da Figura 3.15 pode-se perceber que o valor estacionário da saída é y(∞) = 1, ou seja, a saída tende a seguir a entrada u(t). O tempo de subida de 10% a 90% do valor final pode ser calculado numericamente e vale, aproximadamente,


   [img:Illustration] 


  

#### 3.5.4 Sistema superamortecido: ξ > 1


  Para ξ > 1 os polos do sistema são reais e diferentes, ou seja:


   [img:Illustration] 


  Os polos do sistema estão representados na Figura 3.16.


   [img:Illustration] 


  Figura 3.16 Polos reais e diferentes.


  Quando a entrada do sistema da Figura 3.9 é um degrau unitário, isto é, U(s) = 1/s, tem-se da Equação (3.34) que


   [img:Illustration] 


  Logo,


   [img:Illustration] 


  Na Figura 3.17 é apresentada uma comparação entre os gráficos da resposta ao degrau para


   [img:Illustration] 


  Figura 3.17 Resposta ao degrau para ξ = 2 e ξ = 1.


  Analisando-se os gráficos da Figura 3.17 pode-se perceber que a resposta ao degrau de um sistema superamortecido (ξ > 1) é mais lenta que a resposta de um sistema com amortecimento crítico (ξ = 1).


  Na Figura 3.18 são apresentados os gráficos da resposta ao degrau de y(t) em função de ωnt para diversos valores do coeficiente de amortecimento ξ. Conforme se pode perceber, as respostas dos sistemas subamortecidos (ξ < 1) cruzam o valor final mais rapidamente que as respostas dos sistemas com amortecimento crítico (ξ = 1) e superamortecidos (ξ > 1).


   [img:Illustration] 


  Figura 3.18 Gráficos de y(t) em função de ωnt.


  Na Figura 3.19 são apresentados os gráficos da resposta ao degrau de y(t) em função do coeficiente de amortecimento ξ e de ωnt.


   [img:Illustration] 


  Figura 3.19 Gráficos de y(t) em função de ξ e ωnt.


  

### 3.6 Características das respostas transitórias


  Em muitos casos as características de desempenho desejadas nos sistemas, especialmente nos sistemas de controle a realimentação, são resumidas em termos de alguns poucos indicadores que são medidos nas respostas. Esses indicadores são empregados como especificações de projeto de sistemas de controle, e só têm sentido no caso de sistemas estáveis.


  As respostas ao degrau têm importância porque na prática podem ser facilmente medidas, bastando para isso modificar o patamar das entradas e registrar as saídas. É bom lembrar que as respostas transitórias dependem das condições iniciais e podem ser perturbadas por ruídos, que são comuns nos ambientes industriais. Por isso costuma-se repetir as medidas buscando partir de uma condição inicial padrão (de preferência o repouso, isto é, a saída e todas as suas derivadas nulas) e depois estimar a média das medidas.


  Na Figura 3.20 estão indicados os principais parâmetros utilizados na engenharia como medidas de desempenho de sistemas subamortecidos. Esses parâmetros e seus nomes internacionais são os seguintes:


  
    • td: tempo de atraso (delay time);


    • tr : tempo de subida (rise time);


    • tp: tempo de pico (peak time);


    • ts: tempo de acomodação (settling time);


    • Mp: sobressinal máximo (overshoot ou maximum peak).

  


  No caso de sistemas com amortecimento crítico e sistemas superamortecidos apenas o tempo de atraso e o tempo de subida são considerados como medidas de desempenho, pois nestes sistemas não há sobressinal. Para sistemas de ordem elevada esses parâmetros também podem ser adotados.


   [img:Illustration] 


  Figura 3.20 Parâmetros para medidas de desempenho de sistemas subamortecidos.


  

#### 3.6.1 Tempo de atraso td


  O tempo de atraso td é o tempo necessário para a resposta ao degrau alcançar pela primeira vez a metade do valor final, isto é, 0,5y(∞).


  

#### 3.6.2 Tempo de subida tr


  Para sistemas com amortecimento crítico ou sistemas superamortecidos o tempo de subida tr normalmente é definido como o tempo necessário para a resposta ao degrau ir de 10% a 90% do seu valor final.


  Para sistemas subamortecidos define-se o tempo de subida tr como o primeiro instante em que a resposta ao degrau alcança 100% do seu valor final. Da resposta ao degrau (3.41) para sistemas subamortecidos de segunda ordem tem-se que


   [img:Illustration] 


  ou seja,


   [img:Illustration] 


  com


   [img:Illustration] 


  Portanto,


   [img:Illustration] 


  

#### 3.6.3 Tempo de pico tp


  O tempo de pico tp é o tempo necessário para a resposta ao degrau alcançar o primeiro pico de sobressinal, que somente ocorre em sistemas subamortecidos. No instante de pico a derivada da resposta ao degrau é nula. Para sistemas de segunda ordem tem-se da Equação (3.41) que


   [img:Illustration] 


  ou


   [img:Illustration] 


  Da Figura 3.10 tem-se que wd = wnsen (β) e ξ = cos (β). Então


   [img:Illustration] 


  ou


   [img:Illustration] 


  Logo,


   [img:Illustration] 


  Portanto, o primeiro pico ocorre em ωdtp = π, ou seja,


   [img:Illustration] 


  

#### 3.6.4 Sobressinal máximo: Mp


  O sobressinal máximo é definido como o máximo valor de pico da resposta menos o seu valor final em porcentagem do seu valor final, ou seja,


   [img:Illustration] 


  Para sistemas de segunda ordem subamortecidos tem-se da Equação (3.41) que


   [img:Illustration] 


  e


   [img:Illustration] 


  Logo,


   [img:Illustration] 


  Como  [img:Illustration] ,


   [img:Illustration] 


  Da Figura 3.10 tem-se que sen (β) = ωd/ωn e  [img:Illustration] . Portanto,


   [img:Illustration] 


  ou


   [img:Illustration] 


  Note que o sobressinal é função exclusiva do coeficiente de amortecimento ξ. A Figura 3.21 é muito útil para estimar ξ a partir da medida do sobressinal Mp.


   [img:Illustration] 


  Figura 3.21 Sobressinal Mp(%) em função de ξ.


  

#### 3.6.5 Tempo de acomodação: ts


  O tempo de acomodação é o tempo necessário para que a resposta ao degrau passe a permanecer dentro de uma faixa de tolerância de em ±∊ em torno do valor final, conforme é mostrado na Figura 3.20. Esta faixa é usualmente especificada em porcentagem do valor final (±5% ou ±2% de y(∞)).


  Para o sistema de segunda ordem subamortecido da Figura 3.11 a constante de tempo das envoltórias é T = 1/ξωn. Assim, o tempo de acomodação ts, para o qual os valores da resposta permanecem dentro de uma faixa de ±5% em torno do valor final, ocorre aproximadamente quando


   [img:Illustration] 


  ou


   [img:Illustration] 


  Analogamente, para uma faixa de ±2% em torno do valor final tem-se que


   [img:Illustration] 


  ou


   [img:Illustration] 


  Portanto, utilizando o critério de 5%, o tempo de acomodação ts é aproximadamente três vezes a constante de tempo T. Já pelo critério de 2%, ts é aproximadamente quatro vezes a constante de tempo T.


  Note que, dado o coeficiente de amortecimento ξ, o tempo de acomodação é inversamente proporcional à frequência natural não amortecida ωn do sistema. Como o valor de ξ é normalmente determinado pelo sobressinal máximo Mp requerido ou permitido, o tempo de acomodação é determinado pela frequência natural não amortecida ωn.


  Na prática da engenharia normalmente deseja-se atender a duas exigências conflitantes: resposta transitória rápida e resposta bem amortecida, isto é, sem sobressinal. Em geral, dada a ordem da dinâmica do sistema não se podem minimizar sobressinal e tempo de subida simultaneamente.


  

### 3.7 Sistemas com mais de dois polos


  Considere um sistema de terceira ordem subamortecido (0 < ξ < 1) com dois polos complexos conjugados em  [img:Illustration]  e com um terceiro polo no eixo real em s3 = –p < 0. Suponha que a função de transferência deste sistema seja dada por


   [img:Illustration] 


  Aplicando-se um degrau unitário na entrada U(s), obtém-se


   [img:Illustration] 


  com


   [img:Illustration] 


  A Equação (3.71) também pode ser escrita como


   [img:Illustration] 


  No domínio do tempo tem-se que


   [img:Illustration] 


  Analisando a Equação (3.73) verifica-se que quando o polo real em s = –p está bem mais à esquerda dos polos complexos conjugados no plano s, isto é, para p >> ξωn, a exponencial devida ao polo real tenderá a zero muito mais rapidamente que a exponencial devida aos polos complexos. Desse modo o polo real em s = –p terá pouca influência na resposta, e a mesma será devida quase exclusivamente aos polos complexos conjugados, que são chamados de polos dominantes.


  Logo, para p >> ξωn, as respostas dos sistemas de terceira ordem são próximas das respostas dos sistemas de segunda ordem subamortecidos (0 < ξ < 1). Nesse caso, as fórmulas do sobressinal, tempo de subida, tempo de pico, tempo de acomodação, etc., deduzidas para os sistemas de segunda ordem, também podem ser empregadas para os polos dominantes de um sistema de terceira ordem.


  De fato, quando o polo real em s = p está bem mais à esquerda dos polos complexos, isto é, para p tendendo a infinito, tem-se que a = –1, b = –2ξωn e c = 0. Com isso, a saída Y(s) resulta


   [img:Illustration] 


  que corresponde à saída de um sistema de segunda ordem com entrada degrau unitário.


  Porém, se o polo real em s = p estiver perto dos polos complexos este também afetará a resposta do sistema. Nesse caso o comportamento do sistema de terceira ordem não será próximo do sistema de segunda ordem. Na prática, os comportamentos dos sistemas de segunda e terceira ordens são aceitos como próximos quando o polo real estiver localizado pelo menos cinco constantes de tempo mais à esquerda dos polos complexos conjugados dominantes, isto é, para p ≥ 5ξωn.


  A análise efetuada aqui para sistemas de terceira ordem também pode ser estendida para sistemas com mais de três polos sem a existência de zeros.


  

### Exemplo 3.4


  Considere os sistemas com as seguintes funções de transferência:


   [img:Illustration] 


  O sistema G1(s) é de segunda ordem, com coeficiente de amortecimento ξ = 0,28 e frequência natural ωn = 5. Logo, a parte real dos polos complexos conjugados é –ξωn = –1,4. Os sistemas G2(s), G3(s) e G4(s) são de terceira ordem com polo real em s = –3, s = –7 e s = –20, respectivamente.


  Aplicando um degrau unitário na entrada de cada um desses sistemas e calculando a transformada inversa, obtém-se a resposta temporal. A resposta y1(t) é dada pela Equação (3.40), e as respostas y2(t), y3(t) e y4(t) podem ser calculadas por meio da Equação (3.73), ou seja,


   [img:Illustration] 


  Os gráficos das respostas y1(t), y2(t), y3(t) e y4(t) são apresentados na Figura (3.22). Note que a resposta y4(t) é a que está mais próxima da resposta y1(t) do sistema de segunda ordem, pois o sistema G4(s) posssui um polo real em s = –20, que é o mais distante dos polos complexos conjugados dominantes.


   [img:Illustration] 


  Figura 3.22 Respostas ao degrau unitário dos sistemas G1(s), G2(s), G3(s) e G4(s).


  ■


  

### 3.8 Sistemas com zeros


  Considere um sistema de segunda ordem subamortecido (0 < ξ < 1) com dois polos complexos conjugados e um zero no eixo real em s = –1/T. Suponha que a função de transferência deste sistema seja dada por


   [img:Illustration] 


  Aplicando-se um degrau unitário na entrada U(s), obtém-se


   [img:Illustration] 


  A Equação (3.80) também pode ser escrita como


   [img:Illustration] 


  No domínio do tempo tem-se que


   [img:Illustration] 


  Analisando a Equação (3.82) verifica-se que quando a constante T é "pequena", ou seja, quando o zero real em s = –1/T está distante dos polos complexos conjugados no plano s, tem-se que  [img:Illustration] . Neste caso a resposta transitória é a mesma que foi calculada para sistemas de segunda ordem subamortecidos (Equação (3.40)), ou seja, o zero terá pouca influência na resposta. Porém, quanto mais próximo o zero estiver dos polos complexos dominantes maior será o seu efeito sobre a resposta transitória.


  

### Exemplo 3.5


  Considere os sistemas com as seguintes funções de transferência:


   [img:Illustration] 


  O sistema G1(s) é de segunda ordem, com coeficiente de amortecimento ξ = 0,28 e frequência natural ωn = 5, de modo que a parte real dos polos complexos conjugados é –ξωn = –1,4. Os sistemas G2(s), G3(s) e G4(s) possuem um zero real em s = –2, s = –20 e s = +2, respectivamente.


  Aplicando um degrau unitário na entrada de cada um desses sistemas e calculando a transformada inversa obtêm-se as respostas temporais


   [img:Illustration] 


  Os gráficos de y1(t), y2(t), y3(t) e y4(t) são apresentados na Figura (3.23). Note que a resposta y3(t) é a que está mais próxima da resposta y1(t) do sistema de segunda ordem, pois G3(s) posssui um zero real em s = –20, que é o mais distante dos polos complexos conjugados dominantes.


   [img:Illustration] 


  Figura 3.23 Respostas ao degrau unitário dos sistemas G1(s), G2(s), G3(s) e G4(s).


  Um resultado interessante pode ser observado quando o zero está localizado no semiplano direito do plano s, que é o caso do sistema G4(s), cujo zero se localiza em s = +2. Neste caso a saída y4(t) se direciona nos instantes iniciais em sentido contrário ao seu valor estacionário. Os sistemas que apresentam tal característica são chamados de sistemas de fase não mínima.


  ■


  

### 3.9 Sistemas com atraso puro ou atraso por transporte


  O atraso puro ou atraso por transporte (time delay) é um fenômeno muito frequente em sistemas com escoamento de fluidos. Tempo morto e retardo velocidade-distância também constituem sinônimos usuais. Considere, por exemplo, o sistema da Figura 3.24, no qual um líquido escoa a uma vazão volumétrica q constante através de um tubo isolado com secção reta uniforme de área A e comprimento L. A densidade e a capacidade calorífica do líquido são constantes e a parede do tubo é um isolante térmico. No estado inicial o sistema está em regime estacionário e a temperatura de entrada é igual à temperatura de saída, ou seja, θe(0) = θs(0).


   [img:Illustration] 


  Figura 3.24 Escoamento de um líquido numa tubulação.


  Deseja-se obter a função de transferência que relaciona a temperatura de entrada θe(t) com a temperatura de saída θs(t) do fluido. Dadas as hipóteses enunciadas, especialmente a de não haver perdas de calor para as paredes do tubo, uma perturbação de temperatura na entrada é percebida sem atenuação na saída depois de α segundos, que é o tempo necessário para as partículas do fluido percorrerem o tubo. Esse tempo é dado por


   [img:Illustration] 


  Na Figura 3.25 são apresentadas as respostas temporais da temperatura de entrada θe(t) e saída θs(t). Note que o fenômeno independe de como a temperatura θe(t) evolui.


   [img:Illustration] 


  Figura 3.25 Respostas temporais das temperaturas de entrada e saída numa tubulação.


  Pelo gráfico da Figura 3.25 percebe-se que a temperatura de saída possui um atraso de tempo α com relação à temperatura de entrada, ou seja,


   [img:Illustration] 


  Aplicando-se a transformada de Laplace e a propriedade da translação no tempo na Equação (3.88), obtém-se


   [img:Illustration] 


  Portanto, a função de transferência de um atraso puro ou retardo é dada por


   [img:Illustration] 


  

### 3.10 Resposta dos sistemas de controle por realimentação


  Num sistema de controle por realimentação, além do sinal de referência R(s) é importante considerar o sinal de perturbação P(s), conforme representado na Figura 3.26.


   [img:Illustration] 


  Figura 3.26 Diagrama de blocos de um sistema com realimentação.


  No sistema da Figura 3.26 estão representadas as seguintes variáveis:


  Gc(s): controlador;


  G1(s) e G2(s): plantas ou processos controlados;


  H(s): transdutor de medida;


  R(s): referência;


  Y(s): saída controlada;


  P(s): perturbação;


  E(s): erro entre a referência e a saída do transdutor de medida.


  Do sistema da Figura 3.26 tem-se que


   [img:Illustration] 


  Substituindo (3.91) em (3.92) e rearranjando os termos, obtém-se uma importante expressão geral para a transformada de Laplace da variável controlada Y(s), dada por


   [img:Illustration] 


  No diagrama em blocos da Figura 3.26 a função de transferência de malha aberta Gma(s) é definida como a função de transferência que se encontra em cascata, ao percorrer a malha de realimentação, excetuando-se o somador, ou seja,


   [img:Illustration] 


  Note que na expressão (3.93) a variável Y(s) tem duas parcelas.


  A primeira é igual ao sinal R(s) multiplicado por uma fração cujo numerador é o produto das funções de transferência encontradas pelo sinal, quando este percorre a malha de R(s) até Y(s), e cujo denominador é a unidade mais a função de transferência de malha aberta.


  A segunda parcela é igual ao sinal P(s) multiplicado por uma fração cujo numerador é a função de transferência encontrada pelo sinal, quando este percorre a malha de P(s) até Y(s), e cujo denominador é igual ao da primeira parcela.


  A transformada de Laplace inversa da expressão (3.93) permite obter a resposta do sistema quando determinados sinais são aplicados nas entradas de referência e de perturbação.


  

### 3.11 Erro estacionário ou permanente


  Em um sistema de controle dinâmico também é muito comum e operacionalmente significativa a especificação de seu desempenho por meio do erro estacionário ou erro em regime permanente, quando estão presentes certos tipos de sinal de referência ou de perturbação pela carga.


  Quando o sinal de entrada é o degrau e o erro atuante é expresso como uma fração em porcentagem da amplitude do degrau, então o erro estacionário é denominado astatismo.


  Substituindo a Equação (3.92) na Equação (3.91) e rearranjando os termos, obtém-se uma expressão para a transformada de Laplace do erro E(s) dada por


   [img:Illustration] 


  A expressão (3.95) também pode ser escrita em termos da função de transferência de malha aberta (3.94), ou seja,


   [img:Illustration] 


  A seguir são obtidas expressões para o erro estacionário, quando sinais de referência e de perturbação são aplicados na entrada do sistema. Os tipos de sinais de referência e de perturbação mais importantes são o degrau e a rampa.


  
    É importante ressaltar que o sinal E(s) representa o erro entre o sinal de referência R(s) e a saída controlada Y(s) apenas quando a realimentação é unitária, ou seja, H(s) = 1.

  


  

#### 3.11.1 Degrau na referência e perturbação nula


  Se o sistema for estável, isto é, se os polos de malha fechada estiverem localizados no semiplano esquerdo aberto do plano s, então o erro estacionário e(∞) pode ser calculado por meio do teorema do valor final. Supondo que um degrau de amplitude A é aplicado na referência (R(s) = A/s) e que a perturbação é nula, então, aplicando o teorema do valor final na expressão (3.96), obtém-se


   [img:Illustration] 


  Genericamente, a função de transferência de malha aberta Gma(s) pode ser escrita como


   [img:Illustration] 


  sendo K um ganho, τi(i = 1, ..., m) e Tj(j = 1, ..., n) constantes de tempo e L indica a quantidade de integradores ou polos na origem de Gma(s). Usualmente um sistema é chamado de tipo (0, 1, 2, . . .) de acordo com a sua quantidade (L = 0, 1, 2,...) de polos na origem.


  Substituindo (3.98) em (3.97), obtém-se


   [img:Illustration] 


  

#### 3.11.2 Rampa na referência e perturbação nula


  Supondo que uma rampa r(t) = At é aplicada na referência (R(s) = A/s2) e que a perturbação é nula, então, pelo teorema do valor final, tem-se que


   [img:Illustration] 


  Da expressão (3.98) tem-se que


   [img:Illustration] 


  Portanto,


   [img:Illustration] 


  Na Tabela 3.3 estão resumidos os erros estacionários para sistemas tipo 0, 1 e 2 (L = 0, 1 e 2) para degrau e rampa na referência com perturbação nula.


  Tabela 3.3 Erros estacionários para sistemas tipo 0, 1 e 2 com perturbação nula


   [img:Illustration] 


  

#### 3.11.3 Perturbação em degrau e referência nula


  Supondo que a perturbação P(s) é um degrau de amplitude A e que a referência é nula, então, aplicando o teorema do valor final na expressão (3.96), obtém-se


   [img:Illustration] 


  A função de transferência G2(s)H(s) pode ser escrita, genericamente, como


   [img:Illustration] 


  sendo Kp um ganho, αi(i = 1, ..., p) e βj(j = 1, ..., q) constantes de tempo e M ≤ L indica a quantidade de integradores ou polos na origem de G2(s)H(s).


  Substituindo (3.98) e (3.104) em (3.103), obtém-se


   [img:Illustration] 


  Portanto,


   [img:Illustration] 


  Na Tabela 3.4 são apresentados alguns erros estacionários para perturbação em degrau e referência nula.


  Tabela 3.4 Erros estacionários para perturbação em degrau e referência nula


   [img:Illustration] 


  

#### 3.11.4 Perturbação em rampa e referência nula


  Supondo que a perturbação é uma rampa (p(t) = At ⇒ P(s) = A/s2) e que a referência é nula, então, aplicando o teorema do valor final na expressão (3.96), obtém-se


   [img:Illustration] 


  Substituindo (3.98) e (3.104) em (3.107), obtém-se


   [img:Illustration] 


  Portanto,


   [img:Illustration] 


  Na Tabela 3.5 são apresentados alguns erros estacionários para perturbação em rampa e referência nula.


  Tabela 3.5 Erros estacionários para perturbação em rampa e referência nula


   [img:Illustration] 


  

### 3.12 Exercícios resolvidos


  

### Exercício 3.1


  Usando o critério de Routh, determine se o polinômio característico a seguir representa um sistema estável ou instável.


   [img:Illustration] 


  Solução


  Como todos os coeficientes de D(s) estão presentes e têm o mesmo sinal, então para determinar se o sistema é estável ou instável deve-se organizar os coeficientes na tabela de Routh 3.6.


  Tabela 3.6 Tabela de Routh


   [img:Illustration] 


  Os coeficientes b1, b2, c1 e d1 da tabela de Routh são calculados como


   [img:Illustration] 


  A Tabela 3.6 possui duas mudanças de sinal na primeira coluna de coeficientes. A primeira mudança de sinal ocorre de a1 = 1 na linha de s3 para b1 = –10 na linha de s2. A segunda ocorre de b1 = –10 na linha de s2 para c1 = 12 na linha de s1.


  Pelo Critério de Routh, o número de raízes com parte real positiva é igual ao número de mudanças de sinal nos elementos da primeira coluna de coeficientes. Logo, o sistema possui dois polos no semiplano direito do plano s e dessa forma é BIBO instável. De fato, utilizando algoritmos de cálculo numérico, tem-se que as raízes de D(s) são: –1, –2 e 1 ± 2j.


  

### Exercício 3.2


  Usando o critério de Routh, determine se o polinômio característico a seguir representa um sistema estável ou instável.


   [img:Illustration] 


  Solução


  Como todos os coeficientes de D(s) estão presentes e têm o mesmo sinal, então para determinar se o sistema é estável ou instável deve-se organizar os coeficientes na tabela de Routh 3.7.


  Tabela 3.7 Tabela de Routh


   [img:Illustration] 


  Como há um coeficiente nulo na primeira coluna da tabela (b1 = 0), o sistema é BIBO instável. Neste caso, o coeficiente c1 não pode ser calculado, pois é necessário realizar uma divisão por b1. Utilizando algoritmos de cálculo numérico, tem-se que as raízes de D(s) são: 0,3090 ± 0,9511j e –0,8090 ± 0,5878j, ou seja, D(s) possui duas raízes complexas conjugadas localizadas no semiplano direito do plano s.


  

### Exercício 3.3


  Usando o critério de Routh, determine se o polinômio característico a seguir representa um sistema estável ou instável.


   [img:Illustration] 


  Solução


  Como todos os coeficientes de D(s) estão presentes e têm o mesmo sinal, então para determinar se o sistema é estável ou instável deve-se organizar os coeficientes na tabela de Routh 3.8.


  Tabela 3.8 Tabela de Routh


   [img:Illustration] 


  Como há um coeficiente nulo na primeira coluna da tabela (b1 = 0), o sistema é BIBO instável. Utilizando algoritmos de cálculo numérico, as raízes de D(s) são: –0,5 ± 0,866j, +0,5 ± 0,866j e –1. Nota-se ainda que toda a linha de s3 é nula e que D(s) possui quatro raízes complexas conjugadas simétricas com relação à origem do plano s.


  

### Exercício 3.4


  Determine os valores do ganho K para que o sistema com função de transferência


   [img:Illustration] 


  seja estável.


  Solução


  O polinômio do denominador de G(s) é dado por D(s) = s4 + 4s3 + Ks2 + 16s + 12.


  • Se K = 0, um dos coeficientes do polinômio D(s) é nulo e com isso o sistema G(s) é BIBO instável.


  • Se K < 0, um dos coeficientes do polinômio D(s) tem sinal trocado e com isso o sistema G(s) é BIBO instável.


  • Se K > 0, para determinar se o sistema G(s) é estável ou instável é necessário montar a tabela de Routh 3.9.


  Tabela 3.9 Tabela de Routh


   [img:Illustration] 


  Os coeficientes b1, b2, c1, c2 e d1 da tabela de Routh são calculados como


   [img:Illustration] 


  Todos os coeficientes da primeira coluna da tabela de Routh têm o mesmo sinal quando


   [img:Illustration] 


  As condições (3.123) e (3.124) são satisfeitas simultaneamente apenas para K > 7. Portanto, o sistema G(s) é BIBO estável se e somente se K > 7.


  Para K = 7 o coeficiente c1 da tabela de Routh é nulo. Nesse caso D(s) possui polos sobre o eixo imaginário e com isso o sistema G(s) é BIBO instável.


  

### Exercício 3.5


  Determine os valores do ganho K para que o sistema em malha fechada da Figura 3.27 seja estável.


   [img:Illustration] 


  Figura 3.27 Sistema em malha fechada.


  Solução


  A função de transferência do sistema em malha fechada é dada por


   [img:Illustration] 


  Para que todos os coeficientes do polinômio do denominador da função (3.125) estejam presentes é necessário que


   [img:Illustration] 


  Para que todos os coeficientes do polinômio do denominador da função (3.125) tenham o mesmo sinal é necessário que


   [img:Illustration] 


  Para determinar os valores do ganho K que estabilizam o sistema em malha fechada é necessário montar a tabela de Routh 3.10.


  Tabela 3.10 Tabela de Routh


   [img:Illustration] 


  Os coeficientes b1 e c1 da tabela de Routh são calculados como


   [img:Illustration] 


  Todos os coeficientes da primeira coluna da tabela de Routh têm o mesmo sinal quando


   [img:Illustration] 


  A partir da condição (3.130) conclui-se que o sistema em malha fechada é BIBO estável se e somente se K > 6.


  

### Exercício 3.6


  Determine a região dos ganhos Kc e KI do controlador PI (Proporcional+Integral) para que o sistema em malha fechada da Figura 3.28 seja estável.


   [img:Illustration] 


  Figura 3.28 Controlador PI para a saída de um processo.


  Solução


  A função de transferência do sistema em malha fechada é dada por


   [img:Illustration] 


  A partir do denominador da função (3.131) obtém-se a tabela de Routh 3.11.


  Tabela 3.11 Tabela de Routh


   [img:Illustration] 


  Os coeficientes b1 e c1 da tabela de Routh são calculados como


   [img:Illustration] 


  Todos os coeficientes da primeira coluna da tabela de Routh têm o mesmo sinal quando


   [img:Illustration] 


  Para que o sistema em malha fechada seja estável, os valores dos ganhos Kc e KI devem estar localizados na região sombreada da Figura 3.29.


   [img:Illustration] 


  Figura 3.29 Região dos ganhos Kc e KI para estabilidade do sistema em malha fechada.


  

### Exercício 3.7


  Aplicando-se um degrau unitário na entrada r(t) do sistema da Figura 3.30, calcule o tempo de subida, o tempo de pico, o sobressinal máximo e o tempo de acomodação pelos critérios de 5% e 2%.


   [img:Illustration] 


  Figura 3.30 Sistema de segunda ordem.


  Solução


  A função de transferência de malha fechada é dada por


   [img:Illustration] 


  Comparando a função (3.135) com a função de transferência de sistemas de segunda ordem


   [img:Illustration] 


  obtém-se ωn = 4 e ξ = 0,5.


  O tempo de subida tr é dado por


   [img:Illustration] 


  O tempo de pico tp é dado por


   [img:Illustration] 


  O sobressinal máximo Mp é calculado como


   [img:Illustration] 


  Pelo critério de 5%, o tempo de acomodação vale aproximadamente


   [img:Illustration] 


  Pelo critério de 2%, o tempo de acomodação vale aproximadamente


   [img:Illustration] 


  O gráfico da resposta ao degrau é apresentado na Figura 3.31.


   [img:Illustration] 


  Figura 3.31 Resposta ao degrau unitário.


  

### Exercício 3.8


  Deseja-se identificar a função de transferência G(s) de um processo. Aplicando-se um degrau unitário na sua entrada u(t) no instante t = 0 mediu-se a saída y(t), cujo gráfico está representado na Figura 3.32. Determine a função de transferência G(s) do processo.


   [img:Illustration] 


  Figura 3.32 Resposta ao degrau unitário.


  Solução


  No gráfico da Figura 3.32 verifica-se que a saída do sistema começa a responder somente a partir de t = 6. Isso significa que o sistema possui um atraso puro α = 6. Após este instante o gráfico é semelhante à resposta transitória de um sistema de primeira ordem. Portanto, a função de transferência é do tipo


   [img:Illustration] 


  Sabendo-se que a entrada u(t) é um degrau unitário (U(s) = 1/s), a constante k pode ser obtida por meio do teorema do valor final


   [img:Illustration] 


  O valor da constante de tempo T é obtido quando a saída y(t) alcança 63,2% do seu valor final, ou seja,


   [img:Illustration] 


  Do gráfico, obtém-se imediatamente que T ≅ 10 – 6 ≅ 4. Portanto,


   [img:Illustration] 


  

### Exercício 3.9


  Um servomecanismo, composto por um motor de corrente contínua com realimentação tacométrica da velocidade ω(t), está representado no diagrama de blocos da Figura 3.33.


   [img:Illustration] 


  Figura 3.33 Servossistema com realimentação tacométrica.


  Aplicando-se um degrau unitário na entrada θr(t), a posição angular θ(t) apresenta uma resposta com sobressinal máximo de 20% e um tempo de subida de 0,3 s. Calcule:


  a) o tempo de pico e o tempo de acomodação segundo os critérios de 5% e 2%;


  b) os valores dos ganhos Km e K que produzem essa resposta.


  Solução


  O coeficiente de amortecimento ξ é obtido a partir do sobressinal máximo Mp, ou seja,


   [img:Illustration] 


  O tempo de subida tr é dado por


   [img:Illustration] 


  Assim, a frequência natural não amortecida ωn é dada por


   [img:Illustration] 


  O tempo de pico tp é dado por


   [img:Illustration] 


  Pelo critério de 5% o tempo de acomodação vale aproximadamente


   [img:Illustration] 


  Pelo critério de 2% o tempo de acomodação vale aproximadamente


   [img:Illustration] 


  Sabendo-se que L[ω(t)]= Ω(s), da Figura 3.33 tem-se que a função de transferência Ω(s)/E(s) da realimentação de velocidade é dada por


   [img:Illustration] 


  Como θ(s)/Ω(s) = 1/s, o diagrama de blocos simplificado do sistema é o da Figura 3.34.


   [img:Illustration] 


  Figura 3.34 Diagrama de blocos simplificado.


  Logo,


   [img:Illustration] 


  Comparando os coeficientes na Equação (3.153), obtém-se


   [img:Illustration] 


  

### Exercício 3.10


  Aplicando-se um degrau unitário na entrada u(t) de um processo, mediu-se a sua saída y(t), cujo gráfico está representado na Figura 3.35. Determine a função de transferência G(s) do processo.


   [img:Illustration] 


  Figura 3.35 Resposta ao degrau unitário.


  Solução


  O gráfico da Figura 3.35 pode ser associado ao comportamento transitório de sistemas de segunda ordem subamortecidos (0 < ξ < 1). Portanto, a função de transferência é do tipo


   [img:Illustration] 


  Sabendo-se que a entrada u(t) é um degrau unitário (U(s) = 1/s), a constante k pode ser determinada por meio do teorema do valor final


   [img:Illustration] 


  O sobressinal Mp vale


   [img:Illustration] 


  A partir do sobressinal Mp obtém-se o coeficiente de amortecimento ξ, ou seja,


   [img:Illustration] 


  A frequência natural ωn pode ser determinada por meio do instante de pico máximo, ou seja,


   [img:Illustration] 


  Portanto,


   [img:Illustration] 


  

### Exercício 3.11


  Determine os valores do coeficiente de amortecimento ξ e da frequência natural não amortecida ωn para que o sistema em malha fechada da Figura 3.36 tenha um sobressinal máximo Mp ≤ 16,3% e um tempo de acomodação segundo o critério de 5% menor ou igual a 3s.


   [img:Illustration] 


  Figura 3.36 Sistema de segunda ordem.


  Solução


  O sobressinal máximo deve ser


   [img:Illustration] 


  Como ξ = cos (β), então β ≤ 60o.


  Pelo critério de 5%, o tempo de acomodação deve ser


   [img:Illustration] 


  A região do plano s, que satisfaz às especificações no domínio do tempo, é apresentada em sombreado na Figura 3.37.


   [img:Illustration] 


  Figura 3.37 Região que satisfaz às especificações no domínio do tempo.


  

### Exercício 3.12


  Considere o diagrama de blocos da Figura 3.38, que representa um regulador de velocidade. Supondo que seja aplicado um degrau unitário na referência ωr(t), calcule o erro no estado estacionário e desenhe o gráfico da resposta transitória de ω(t).


   [img:Illustration] 


  Figura 3.38 Diagrama de blocos de um regulador de velocidade.


  Solução


  A transformada de Laplace do erro e(t) é dada por


   [img:Illustration] 


  Sabendo-se que é aplicado um degrau unitário na referência (Ωr(s) = 1/s), o erro estacionário e(∞) pode ser calculado por meio do teorema do valor final, ou seja,


   [img:Illustration] 


  A função de transferência de malha fechada é dada por


   [img:Illustration] 


  Como Ωr(s) é um degrau unitário, então


   [img:Illustration] 


  Portanto,


   [img:Illustration] 


  O gráfico da resposta transitória de ω(t) é apresentado na Figura 3.39. Note neste gráfico que e(∞) = ωr (∞) – ω(∞) = 1 – 0,5 = 0,5.


   [img:Illustration] 


  Figura 3.39 Resposta transitória de ω(t).


  

### 3.13 Exercícios propostos


  

### Exercício 3.13


  Usando o critério de Routh, determine se os polinômios característicos a seguir representam sistemas estáveis ou instáveis.


  a) D(s) = s3 + 12s2 + 20s.


  b) D(s) = s3 + 4s2 + s – 6.


  c) D(s) = s4 + 6s3 + 18s2 + 24s + 16.


  d) D(s) = s4 + 2s3 + 2s2 + 10s + 25.


  e) D(s) = s5 + 3s4 + 2s3 + 6s2 + 6s + 9.


  

### Exercício 3.14


  Considere o sistema com realimentação unitária da Figura 3.40.


   [img:Illustration] 


  Figura 3.40 Sistema com realimentação unitária.


  Usando o critério de Routh, determine a faixa de valores do ganho k que estabiliza os seguintes sistemas:


   [img:Illustration] 


  

### Exercício 3.15


  Considere o sistema de primeira ordem da Figura 3.41.


   [img:Illustration] 


  Figura 3.41 Sistema de primeira ordem.


  Sabendo-se que é aplicado um degrau de amplitude 2 em r(t), determine:


  
    a) se o sistema em malha fechada é estável ou instável;


    b) a resposta temporal y(t);


    c) o erro estacionário;


    d) o tempo de subida tr.

  


  

### Exercício 3.16


  Deseja-se identificar a função de transferência do processo da Figura 3.42. Aplicando-se um degrau unitário na entrada u(t) mediu-se a saída do processo y(t), cujo gráfico está representado na Figura 3.43. Determine a função de transferência do processo.


   [img:Illustration] 


  Figura 3.42 Processo a ser identificado.


   [img:Illustration] 


  Figura 3.43 Resposta ao degrau unitário na entrada u(t).


  

### Exercício 3.17


  Deseja-se identificar a função de transferência do sistema de segunda ordem da Figura 3.44. Aplicando-se um degrau unitário na referência r(t) mediu-se a saída y(t), cujo gráfico está representado na Figura 3.45. Determine a função de transferência do sistema.


   [img:Illustration] 


  Figura 3.44 Sistema de segunda ordem a ser identificado.


   [img:Illustration] 


  Figura 3.45 Resposta ao degrau unitário na referência r(t).


  

### Exercício 3.18


  Um laminador de chapas de aço de múltiplas passagens troca material com uma enroladeiradesenroladeira como a mostrada na Figura 3.46. Ela é acionada por um motor de corrente contínua com redutor de velocidade. Em regime estacionário, a tensão de alimentação de entrada é de 200 VCC e leva o cilindro à velocidade angular de 100 rpm. A constante de tempo mecânica que é válida quando trabalhando como enroladeira depende muito da quantidade de chapas de aço enrolada. Um ensaio para estimar o maior valor da constante de tempo consiste em levar a bobina totalmente carregada até uma certa velocidade angular, desligar a energia elétrica e registrar a velocidade versus tempo. Sabendo que a velocidade leva 1 minuto para reduzir-se em 63%, calcule a função de transferência da enroladeira.


   [img:Illustration] 


  Figura 3.46 Enroladeira e desenroladeira de chapas de aço. Cortesia da Usiminas. Ver [44].


  

### Exercício 3.19


  Aplicando-se um degrau unitário na entrada r(t) do sistema da Figura 3.47, a resposta y(t) apresenta um sobressinal máximo de 25,4% e um tempo de acomodação de 1s pelo critério de 2%. Calcule o tempo de pico, o tempo de subida e determine a função de transferência do sistema de malha aberta.


   [img:Illustration] 


  Figura 3.47 Sistema de segunda ordem.


  

### Exercício 3.20


  O diagrama de blocos da Figura 3.48 representa um motor CC com realimentação auxiliar da velocidade angular w(t).


   [img:Illustration] 


  Figura 3.48 Motor CC com realimentação auxiliar de velocidade.


  Aplicando-se um degrau unitário na referência r(t), deseja-se que a resposta da posição x(t) apresente um sobressinal máximo de 10% e um tempo de pico de 0,5s. Calcule:


  a) o tempo de subida e o tempo de acomodação segundo os critérios de 5% e 2%;


  b) os ganhos Kc e Kt que produzem a resposta desejada.


  

### Exercício 3.21


  Determine os erros no estado estacionário do sistema de controle da Figura 3.49 quando são aplicados degraus unitários nas entradas de:


  a) referência R(s) (supor D(s) = 0);


  b) perturbação D(s) (supor R(s) = 0).


   [img:Illustration] 


  Figura 3.49 Processo industrial com entradas de referência R(s) e de perturbação D(s).


  

### Exercício 3.22


  Considere o sistema com realimentação unitária da Figura 3.50.


   [img:Illustration] 


  Figura 3.50 Sistema com realimentação unitária.


  Calcule os erros estacionários para entrada degrau e rampa, com coeficiente A = 1, para os seguintes sistemas:


   [img:Illustration] 


  


  __________


  1Uma prova do critério de estabilidade de Routh pode ser encontrada em [14].



<!-- Text/chapter04.xhtml -->

  Controle Automático, 2ª edição
  
  
  

  

## 4

  

## Lugar das Raízes

  

### 4.1 Introdução

  O método do lugar geométrico das raízes foi criado por W. R. Evans1 e consiste em um gráfico, construído a partir do conhecimento dos polos e zeros do sistema em malha aberta, que permite visualizar de que forma os polos do sistema em malha fechada variam quando se altera o valor do ganho do sistema em malha aberta.

  Este método é um excelente instrumento de análise dos efeitos dinâmicos da realimentação de sinais, sem que para isso seja necessário calcular soluções de equações diferenciais lineares. Atualmente esta técnica é aplicada no projeto de sistemas de controle por meio de pacotes computacionais.

  

### 4.2 O método do Lugar Geométrico das Raízes (L.G.R.)

  Considere o sistema em malha fechada da Figura 4.1.

   [img:Illustration] 

  Figura 4.1 Diagrama de blocos de um sistema em malha fechada.

  A função de transferência de malha fechada é dada por

   [img:Illustration] 

  Os polos de malha fechada são as raízes da equação característica

   [img:Illustration] 

  Escrevendo a Equação (4.2) na forma complexa, obtém-se

   [img:Illustration] 

  sendo G(s)H(s) a função de transferência do sistema em malha aberta.

  A Equação (4.3) pode ser desdobrada em duas:

  
    • condição de módulo:

     [img:Illustration] 

    • condição de fase:

     [img:Illustration] 

  

  A função de transferência de malha aberta G(s)H(s) pode ser escrita na forma de polos e zeros

   [img:Illustration] 

  em que z1, z2, . . ., zm são os zeros de malha aberta, p1, p2, . . ., pn são os polos de malha aberta e k > 0 é o coeficiente de ganho, suposto positivo2.

  Da Equação (4.6), a condição de módulo pode ser escrita como

   [img:Illustration] 

  Assim, o valor do ganho k, associado a qualquer ponto do plano s, pode ser obtido por

   [img:Illustration] 

  Da Equação (4.6), a condição de fase para k > 0 pode ser escrita como

   [img:Illustration] 

  Conforme representado na Figura 4.2, a fase do vetor s – p é o ângulo θ, medido no sentido anti-horário a partir do eixo real.

   [img:Illustration] 

  Figura 4.2 Fase θ do número complexo s – p.

  
    O lugar geométrico das raízes L.G.R. é um gráfico no plano s que mostra a posição de todos os polos de malha fechada quando o ganho k varia de 0 a ∞. A condição de fase (4.9) é a condição geométrica que permite determinar se um dado ponto pertence ou não ao L.G.R.

  

  

### Exemplo 4.1

  Deseja-se determinar o lugar das raízes sobre o eixo real do sistema em malha fechada com realimentação unitária (H(s) = 1) da Figura 4.3.

   [img:Illustration] 

  Figura 4.3 Sistema em malha fechada com realimentação unitária.

  A função de transferência de malha aberta é dada por

   [img:Illustration] 

  A condição de fase é dada por

   [img:Illustration] 

  Para verificar quais são os segmentos do eixo real que pertencem ao lugar das raízes, basta selecionar pontos de teste ao acaso (s1, s2, s3 e s4), conforme mostrado na Figura 4.4, e depois verificar quais são os pontos que satisfazem a condição de fase.

   [img:Illustration] 

  Figura 4.4 Pontos de teste do eixo real.

   [img:Illustration] 

  Entre os pontos testados (s1, s2, s3 e s4) a condição de fase é satisfeita apenas para s2 e s4. Note que a condição de fase também é satisfeita para qualquer outro ponto que for escolhido nos segmentos de reta entre 0 e –1 e entre –2 e –∞. Portanto, o lugar das raízes de todos os polos de malha fechada sobre o eixo real se encontra nesses dois segmentos.

  Os polos de malha fechada também podem ser calculados a partir da função de transferência de malha fechada

   [img:Illustration] 

  Variando-se o ganho k, pode-se obter os polos de malha fechada de acordo com a Tabela 4.1.

  Tabela 4.1 Polos de malha fechada

  
    
      
        

        

        
      

      
        
          
            k = 0

            k = 0,1

            k = 1

            k = 5

            k = 10

            k = 100

            k → ∞

          

          
            s = 0

            s = –0,05

            s = –0,38

            s = –0,81

            s = –0,90

            s = –0,99

            s → –1

          

          
            s = –2

            s = –2,05

            s = –2,62

            s = –6,19

            s = –11,10

            s = –101,01

            s → –∞

          
        

      
    
  

  Analisando-se a Tabela 4.1, verifica-se que à medida que o ganho k varia de zero a infinito os polos de malha fechada variam de 0 a –1 e de –2 a –∞. O gráfico do lugar geométrico das raízes de todos os polos de malha fechada é representado pelas linhas grossas da Figura 4.5.

   [img:Illustration] 

  Figura 4.5 Lugar geométrico das raízes.

  Analisando-se as Figuras 4.4 e 4.5 verifica-se que à direita do ponto de teste s1 não há raízes, isto é, a quantidade de polos e zeros é nula (quantidade par). Logo, o segmento do intervalo de 0 a +∞ não faz parte do lugar das raízes.

  À direita do ponto de teste s2 há 1 raiz (quantidade ímpar), isto é, há o polo em s = 0. Logo, o segmento do intervalo de –1 a 0 faz parte do lugar das raízes.

  À direita do ponto de teste s3 há 2 raízes (quantidade par), isto é, há o zero em s = –1 e o polo em s = 0. Logo, o segmento do intervalo de –2 a –1 não faz parte do lugar das raízes.

  Por fim, à direita do ponto de teste s4 há 3 raízes (quantidade ímpar), isto é, há o polo em s = –2, o zero em s = –1 e o polo em s = 0. Logo, o segmento do intervalo de –∞ a –2 faz parte do lugar das raízes.

  ■

  Portanto, do exemplo anterior conclui-se que:

  
    • se o número de polos ou zeros reais à direita do ponto de teste for ímpar, então o segmento que contém o ponto de teste pertence ao lugar das raízes;

    • o lugar das raízes começa num polo e termina num zero, formando segmentos alternados ao longo do eixo real. Quando a quantidade de polos for maior que a de zeros, o lugar das raízes termina no infinito;

    • o sentido das flechas do lugar das raízes indica o sentido dos valores crescentes do ganho k.

  

  

### 4.3 Regras para o traçado do lugar das raízes

  

### Número de ramos

  Marcar os polos e zeros da função de transferência de malha aberta G(s)H(s) com os símbolos "×" e "O", respectivamente. O número de ramos é igual ao número n de polos.

  

### Simetria

  Como o polinômio do denominador da função de transferência de malha fechada tem coeficientes reais, as suas raízes podem ser apenas reais ou complexas conjugadas. Logo, o lugar das raízes é simétrico em relação ao eixo real do plano complexo.

  

### Lugar das raízes sobre o eixo real

  Pares de zeros ou polos complexos conjugados não afetam a condição de fase sobre o eixo real. Conforme se pode verificar no exemplo da Figura 4.6, a soma dos ângulos de cada polo complexo com relação ao ponto de teste s é

   [img:Illustration] 

   [img:Illustration] 

  Figura 4.6 Ângulos de um par de polos complexos conjugados.

  Por outro lado, com relação aos polos e zeros reais sabe-se que:

  • cada zero ou cada polo real de malha aberta contribui com uma fase de 180o, se estiver à direita de um ponto de teste s;

  • cada zero ou cada polo real de malha aberta não afeta a condição de fase, se estiver à esquerda de um ponto de teste s.

  
    Logo, um ponto de teste s sobre o eixo real pertence ao lugar das raízes se o número total de polos e zeros à direita deste ponto for ímpar.

  

  

### Pontos de início e término

  O lugar das raízes consiste no lugar geométrico de todos os polos de malha fechada para 0 < k < ∞. O ponto de início ou partida corresponde a k → 0 e o ponto de término ou chegada corresponde a k → ∞.

  Os polos de malha fechada são as raízes da equação característica 1 + G(s)H(s) = 0, ou seja,

   [img:Illustration] 

  Para k → 0 as raízes da Equação (4.14) tendem para as raízes de (s–p1)(s–p2) . . . (s–pn) = 0.

  
    Portanto, o lugar das raízes "começa" nos n polos de malha aberta.

  

  Da condição de módulo G(s)H(s)| = 1 tem-se que

   [img:Illustration] 

  Para k → ∞ as raízes da Equação (4.15) tendem para as raízes de |s − z1||s − z2| . . . |s − zm| = 0.

  
    Portanto, o lugar das raízes "termina" nos m zeros de malha aberta.

  

  

### Assíntotas

  O número de ramos é igual ao número n de polos. Como o número n de polos é normalmente maior que o número m de zeros, então m ramos terminam nos zeros e n – m ramos terminam no infinito, seguindo assíntotas. Portanto, o número de assíntotas é igual a n – m.

  Da condição de fase (4.9) tem-se que

   [img:Illustration] 

  Num ponto s suficientemente afastado, tal que o seu módulo seja muito maior que o módulo dos polos e zeros de malha aberta, então os ângulos da Equação (4.16) podem ser considerados aproximadamente iguais a um ângulo α qualquer, ou seja,

   [img:Illustration] 

  Pode-se demonstrar que as assíntotas cruzam o eixo real no ponto

   [img:Illustration] 

  

### Pontos de partida e chegada sobre o eixo real

  Se existirem dois polos de malha aberta adjacentes sobre o eixo real e se o segmento entre eles fizer parte do lugar das raízes, então haverá pelo menos um ponto de partida neste segmento.

  Analogamente, se existirem dois zeros de malha aberta adjacentes sobre o eixo real e se o segmento entre eles fizer parte do lugar das raízes, então haverá pelo menos um ponto de chegada neste segmento.3 Os pontos de partida e chegada sobre o eixo real também são chamados de pontos de ramificação.

  Considere a equação característica (4.2):

  1 + G(s)H(s) = 0.

  Supondo

   [img:Illustration] 

  a equação característica pode ser escrita como

   [img:Illustration] 

  Prova-se que os pontos de partida ou chegada sobre o eixo real podem ser calculados a partir das raízes de

   [img:Illustration] 

  A solução da Equação (4.21) é uma condição necessária, mas não suficiente para a existência de pontos de partida ou de chegada. Se uma raiz da Equação (4.21) não pertencer ao lugar das raízes do eixo real, então essa raiz não corresponde nem a um ponto de partida nem a um ponto de chegada.

  

### Ângulo de partida de um polo complexo e de chegada em um zero complexo

  Permite determinar a direção dos ramos do lugar das raízes nas proximidades dos polos e zeros complexos conjugados. Escolhendo-se um ponto de teste nas proximidades de um polo ou zero complexo pode-se considerar que a soma das contribuições angulares de todos os outros polos e zeros permanece invariável. Assim, da condição de fase (4.9) o ângulo de partida de um polo complexo p1 pode ser determinado como

   [img:Illustration] 

  Da mesma forma, o ângulo de chegada em um zero complexo z1 pode ser determinado como

   [img:Illustration] 

  Na Figura 4.7 são esquematizados os lugares das raízes de alguns sistemas com realimentação negativa.

   [img:Illustration] 

  Figura 4.7 Lugar das raízes de alguns sistemas com realimentação negativa.

  

### Exemplo 4.2

  Deseja-se desenhar o lugar das raízes do sistema da Figura 4.8.

   [img:Illustration] 

  Figura 4.8 Sistema em malha fechada com realimentação unitária.

  Primeiramente devem-se marcar os polos de malha aberta conforme mostrado na Figura 4.9. A seguir devem-se selecionar pontos de teste s1, s2 e s3 nos segmentos do eixo real. Como à direita de s1 não há raízes (quantidade par) e à direita de s3 há 2 raízes (quantidade par), os segmentos de 0 a +∞ e de –10 a –∞ não fazem parte do lugar das raízes. Logo, apenas o segmento de –10 a 0 faz parte do lugar das raízes, pois à direita de s2 há 1 raiz (quantidade ímpar).

   [img:Illustration] 

  Figura 4.9 Polos e pontos de teste.

  Como a quantidade de polos (n = 2) é maior que a quantidade de zeros (m = 0), então n–m = 2 ramos terminam no infinito, seguindo assíntotas com os ângulos

   [img:Illustration] 

  As assíntotas cruzam o eixo real no ponto

   [img:Illustration] 

  O lugar das raízes começa nos polos e termina nos zeros de malha aberta, quando k varia de zero a infinito. Como há dois polos de malha aberta adjacentes sobre o eixo real (s = 0 e s = –10) e como o segmento entre eles faz parte do lugar das raízes, então há um ponto de partida neste segmento. A equação característica do sistema em malha fechada é dada por

   [img:Illustration] 

  Aplicando a condição (4.21), obtém-se

   [img:Illustration] 

  Portanto, há um ponto de partida em s = –5.

  O gráfico do lugar geométrico das raízes apresenta o aspecto da Figura 4.10. Note que ao desenhar o gráfico do lugar das raízes o mesmo também deve satisfazer à propriedade de simetria com relação ao eixo real.

   [img:Illustration] 

  Figura 4.10 Lugar geométrico das raízes.

  Analisando-se o gráfico da Figura 4.10 verifica-se que o sistema em malha fechada é sempre estável para qualquer k > 0, pois as linhas do lugar das raízes que representam os polos de malha fechada se localizam no semiplano esquerdo aberto do plano s.

  ■

  

### 4.4 Realimentação positiva

  Sistemas de controle complexos podem possuir uma malha com realimentação positiva interna estabilizada pela malha externa, conforme mostra a Figura 4.11.

   [img:Illustration] 

  Figura 4.11 Diagrama de blocos de um sistema com realimentação positiva.

  A função de transferência da malha fechada interna é dada por

   [img:Illustration] 

  Os polos de malha fechada são as raízes da equação característica

   [img:Illustration] 

  A Equação (4.29) pode ser desdobrada em duas:

  
    • condição de módulo: |G(s)| = 1.

    • condição de fase:  [img:Illustration] 

  

  As regras para a construção do lugar das raízes são semelhantes às vistas anteriormente. Devido à alteração da condição de fase há algumas exceções descritas a seguir.

  

### Lugar das raízes sobre o eixo real

  Um ponto de teste sobre o eixo real pertence ao lugar das raízes se o número total de polos e zeros à direita desse ponto for um número par.

  

### Ângulos das assíntotas

  O cálculo dos ângulos das assíntotas é modificado para

   [img:Illustration] 

  

### Ângulo de partida de um polo complexo e de chegada em um zero complexo

  Da condição de fase para k > 0, o ângulo de partida de um polo complexo p1 pode ser determinado como

   [img:Illustration] 

  Da mesma forma, o ângulo de chegada em um zero complexo z1 pode ser determinado como

   [img:Illustration] 

  

### Exemplo 4.3

  Supondo k > 0, determine o lugar das raízes do sistema com realimentação positiva que tem função de transferência

   [img:Illustration] 

  Primeiramente devem-se marcar os polos e o zero de malha aberta no eixo real. À direita do polo em s = –1 não há raízes (quantidade par). Logo, o segmento do eixo real de –1 a +∞ faz parte do lugar das raízes. O segmento entre –2 e –1 não faz parte do lugar das raízes, pois à direita do polo em s = –2 há uma raiz em s = –1 (quantidade ímpar). O outro segmento que também faz parte do lugar das raízes é o que está entre –3 e –2, pois à direita do zero em s = –3 há duas raízes (quantidade par). Já o segmento do intervalo de –3 a –∞ também não faz parte do lugar das raízes, pois à direita de qualquer ponto de teste deste segmento (excluindo-se o zero em s = –3) há três raízes (quantidade ímpar).

  Conforme representado na Figura 4.12, o lugar das raízes possui um segmento que começa no polo em s = –2 e termina no zero em s = –3 e outro segmento que começa no polo em s = –1 e termina em +∞ quando k varia de zero a infinito

   [img:Illustration] 

  Figura 4.12 Lugar geométrico das raízes.

  ■

  

### 4.5 Lugar das raízes de sistemas com atraso puro

  Em muitos processos industriais são encontrados com frequência sistemas com atraso puro ou atraso por transporte. Conforme foi visto na Seção 3.9, a função de transferência de um atraso puro é

   [img:Illustration] 

  Um sistema estável em malha aberta, de ordem 1 e com atraso puro, pode ser instável em malha fechada pois é possível que, para algum ganho k, o lugar das raízes se localize sobre o eixo imaginário ou no semiplano direito do plano s.

  

### Exemplo 4.4

  Considere o sistema estável em malha aberta com função de transferência

   [img:Illustration] 

  A função de transferência de malha fechada é

   [img:Illustration] 

  É possível verificar se o lugar das raízes tem polos sobre o eixo imaginário fazendo a substituição s = 0 + jω no denominador de Gmf (s), ou seja,

   [img:Illustration] 

  Igualando a zero as partes real e imaginária da Equação (4.36), obtém-se

   [img:Illustration] 

  cuja solução é ω ≅ 1,14446 e k ≅ 1,5.

  Como ω é um ângulo, na realidade o lugar das raízes tem infinitos pontos ω±2πr (r = 0, 1, 2, . . .) sobre o eixo imaginário. Em termos de estabilidade apenas o ponto em r = 0 tem importância, pois ele determina o maior ganho para o sistema ser estável em malha fechada, isto é, k < 1,5.

  ■

  

#### 4.5.1 Aproximações de Padé

  Como a representação do atraso puro não é uma função de transferência racional, há diversas aproximações que podem ser utilizadas para a função exponencial. As melhores são as aproximações de Padé de ordem (m, n), sendo m e n os graus dos polinômios do numerador e do denominador, respectivamente. Na Tabela 4.2 são apresentadas as aproximações de Padé para a função e–αs de ordens (1,1), (2,2) e (3,3).

  Tabela 4.2 Aproximações de Padé para a função e–αs

   [img:Illustration] 

  

### Exemplo 4.5

  Considere a função de transferência de um processo dada por

   [img:Illustration] 

  Usando as aproximações de Padé da Tabela 4.2, obtêm-se as seguintes funções de transferência:

   [img:Illustration] 

  Na Figura 4.13 são apresentadas as saídas dos sistemas G(s), G1(s), G2(s) e G3(s) para degraus unitários aplicados em suas entradas. Observe que quanto maior é a ordem da função de transferência melhor é a aproximação para a função G(s). Por outro lado, aumenta-se também a complexidade dos cálculos.

   [img:Illustration] 

  Figura 4.13 Saídas dos sistemas G(s), G1(s), G2(s) e G3(s) para degraus unitários aplicados em suas entradas.

  ■

  

### Exemplo 4.6

  Utilizando a aproximação de Padé de ordem(1,1) na função de transferência de malha aberta (4.34), obtém-se

   [img:Illustration] 

  cuja função de transferência de malha fechada com realimentação unitária é

   [img:Illustration] 

  Supondo k > 0, pelo critério de Routh o sistema em malha fechada (4.44) é estável para 0 < k < 2. Observe que o maior valor de k desta análise é superior ao ganho k < 1,5, obtido com a função de transferência exata no exemplo 4.4. Isso se deve à aproximação de Padé de ordem(1,1). Para melhorar a precisão, nos projetos devem-se usar aproximações de ordens mais elevadas, porém os cálculos são mais complexos.

  A função de transferência de malha aberta da Equação (4.43) é de um sistema com realimentação positiva e produz o lugar das raízes da Figura 4.14. Note que o lugar das raízes começa no semiplano esquerdo do plano s, cruza o eixo imaginário nos pontos  [img:Illustration]  para k = 2 e vai para o semiplano direito para k > 2.

   [img:Illustration] 

  Figura 4.14 Lugar das raízes da função (4.43).

  

### 4.6 Compensação por meio do lugar das raízes

  Projetar um controlador ou um compensador significa modificar a resposta de um sistema de modo que sua saída atenda a determinadas especificações. Os controladores são formados por funções de transferência que adicionam polos e zeros ao sistema. Um esquema de controle típico de um processo em malha fechada com realimentação da saída é apresentado na Figura 4.15.

   [img:Illustration] 

  Figura 4.15 Diagrama de blocos de um sistema de controle em malha fechada.

  De um modo geral, três especificações são muito importantes no projeto de sistemas de controle:

  
    • estabilidade;

    • erro estacionário "pequeno" ou nulo;

    • desempenho, que consiste em sobressinal "baixo" e tempo de resposta transitória "pequeno".

  

  A especificação de estabilidade é essencial para qualquer sistema em malha fechada, pois não há sistema instável que tenha utilidade prática. A característica de erro estacionário "pequeno" ou nulo é desejável para uma grande quantidade de sistemas em que se espera que as saídas sigam determinadas referências ou estejam pelo menos próximas dos valores desejados. Já a especificação de desempenho está relacionada ao sobressinal e ao tempo de resposta transitória. Normalmente deseja-se que a resposta transitória tenha um sobressinal "baixo" e um tempo de resposta "pequeno" (tempo de subida, de pico, de acomodação, etc.).

  Muitas vezes as etapas de projeto de sistemas de controle resultam de um procedimento de tentativa e erro até que as especificações desejadas sejam atingidas. Uma vez adotadas as especificações de projeto, o próximo passo consiste em projetar o controlador, calculando os seus parâmetros. Após esta etapa deve-se realizar uma análise do sistema com a realimentação para verificar se as especificações de projeto inicialmente adotadas foram atingidas. Se os resultados forem satisfatórios pode-se passar para a etapa de implementação do controlador. Caso contrário, novos projetos de controladores devem ser realizados. Um esquema desse procedimento de projeto está sistematizado na Figura 4.16.

  Conforme foi visto no Capítulo 3, para sistemas de ordem elevada (maior ou igual a 3) normalmente a resposta do sistema em malha fechada é dominada pelos polos de malha fechada que se localizam mais próximos do eixo imaginário, chamados polos dominantes. Porém, caso a resposta não dependa apenas desses polos, a resposta do sistema compensado pode não produzir os resultados desejados. Por essa razão, após a realização do projeto é importante analisar a resposta do sistema em malha fechada, por meio de uma simulação em computador, verificando se os resultados estão de acordo com as especificações desejadas.

   [img:Illustration] 

  Figura 4.16 Esquema dos procedimentos de projeto de sistemas de controle.

  Quando as especificações de projeto são fornecidas em termos da resposta transitória temporal o projeto do controlador a partir do sistema em malha aberta pode ser realizado por meio da técnica do lugar das raízes.

  

#### 4.6.1 Compensação por avanço de fase

  A compensação por avanço de fase (phase lead) tem a propriedade de melhorar a resposta temporal do sistema, reduzindo o sobressinal e o tempo de resposta transitória. Para verificar esta propriedade basta notar que quando o compensador por avanço de fase é incluído na malha o ponto de intersecção das assíntotas com o eixo real, calculado pela Equação (4.18), é deslocado para a esquerda do plano s. Com isso, o lugar das raízes também se desloca para a esquerda, fazendo com que o sobressinal e o tempo de resposta sejam reduzidos.

  O bloco típico de um compensador por avanço de fase tem a função de transferência

   [img:Illustration] 

  O diagrama de polos e zeros de um compensador por avanço de fase é apresentado na Figura 4.17. O zero do compensador zc deve estar localizado mais próximo do eixo imaginário, quando comparado ao polo pc. A designação avanço de fase reside no fato de que para qualquer ponto s com Re < 0 e Im > 0 o compensador Gc(s) adiciona fase na malha aberta, pois ∠Gc(s) = ϕ–θ > 0.

   [img:Illustration] 

  Figura 4.17 Diagrama de polos e zeros de um compensador por avanço de fase.

  Basicamente, a metodologia de projeto consiste em determinar as posições dos polos de malha fechada dominantes que satisfazem às especificações de desempenho desejadas, como sobressinal e tempo de resposta transitória (tempo de subida, pico, acomodação, etc.). O zero e o polo do compensador Gc(s) devem ser alocados de tal forma que o lugar das raízes passe pelos polos de malha fechada dominantes. Uma vez fixada a posição do zero do compensador a posição do polo pode ser determinada por meio da condição de fase (4.5). Depois disso o ganho k pode ser obtido por meio da condição de módulo (4.4).

  

### Exemplo 4.7

  Um servomecanismo, composto por um motor de corrente contínua, possui a função de transferência

   [img:Illustration] 

  e Θ(s) e Ea(s) representam as transformadas de Laplace da posição angular do eixo e da tensão de armadura, respectivamente. O diagrama de blocos do sistema em malha fechada sem compensador é apresentado na Figura 4.18.

   [img:Illustration] 

  Figura 4.18 Diagrama de blocos do sistema em malha fechada sem compensador.

  A função de transferência de malha fechada do sistema de segunda ordem é dada por

   [img:Illustration] 

  sendo Θr (s) a posição angular desejada,  [img:Illustration]  (rad/s) a frequência natural não amortecida e  [img:Illustration]  o coeficiente de amortecimento. Quando é aplicado um degrau unitário na entrada θr (t), a saída θ(t) apresenta a resposta da Figura 4.19.

   [img:Illustration] 

  Figura 4.19 Resposta ao degrau unitário do sistema em malha fechada sem compensador.

  De acordo com a Figura 4.19, o sobressinal vale

   [img:Illustration] 

  e o tempo de acomodação, segundo o critério de 2%, é

   [img:Illustration] 

  Deseja-se projetar um compensador Gc(s), conforme representado no diagrama de blocos da Figura (4.20), de modo que o coeficiente de amortecimento dos polos de malha fechada dominantes seja ξ = 0,5 (Mp ≅ 16%) e o tempo de acomodação seja reduzido para ts(2%) ≅ 2 s, isto é

   [img:Illustration] 

  Portanto, para que as especificações sejam satisfeitas, os polos de malha fechada dominantes devem estar localizados em

   [img:Illustration] 

   [img:Illustration] 

  Figura 4.20 Diagrama de blocos do sistema em malha fechada com compensador.

  Se Gc(s) for apenas um ganho, isto é, Gc(s) = k, é impossível satisfazer às especificações fornecidas. Conforme se pode perceber pelo lugar das raízes da Figura 4.21, variando-se apenas o ganho k os polos de malha fechada nunca passam pelos polos calculados em (4.51).

   [img:Illustration] 

  Figura 4.21 Lugar das raízes sem compensador.

  Para deslocar o lugar das raízes para a esquerda pode-se empregar um compensador por avanço de fase

   [img:Illustration] 

  Adotando o zero do compensador na mesma posição que a parte real dos polos de malha fechada dominantes (zc = 2) o polo do compensador pode ser calculado pela condição de fase, ou seja,

   [img:Illustration] 

  No polo de malha fechada  [img:Illustration]  tem-se que

   [img:Illustration] 

  Calculando a tangente dos dois membros da Equação (4.54), obtém-se

   [img:Illustration] 

  O valor do ganho kc > 0 pode ser obtido por meio da condição de módulo, ou seja,

   [img:Illustration] 

  No polo de malha fechada  [img:Illustration]  obtém-se

   [img:Illustration] 

  Portanto,

   [img:Illustration] 

  O lugar das raízes do sistema com o compensador (4.58) é apresentado na Figura 4.22.

   [img:Illustration] 

  Figura 4.22 Lugar das raízes com compensador.

  O sistema em malha fechada com o compensador (4.58) resulta num sistema de ordem 3, cuja função de transferência é dada por

   [img:Illustration] 

  Outra solução para o projeto do compensador pode ser obtida por meio de uma análise direta do lugar das raízes. Se o zero zc do compensador for cancelado com o polo estável4 da planta (s = –zc = –1) e se o polo do compensador for alocado na posição s = –pc = –4, então o lugar das raízes passa exatamente pelos polos de malha fechada desejados  [img:Illustration] . Isso é o que mostra o gráfico do lugar das raízes da Figura 4.23.

   [img:Illustration] 

  Figura 4.23 Lugar das raízes com o cancelamento do zero do compensador com o polo da planta.

  Com isso, o sistema em malha aberta Gma(s) resultante é de ordem 2, isto é,

   [img:Illustration] 

  O valor do ganho kc > 0 em qualquer polo de malha fechada desejado pode ser calculado por meio da condição de módulo, ou seja,

   [img:Illustration] 

  Portanto, a função de transferência do compensador é dada por

   [img:Illustration] 

  A função de transferência de malha fechada com o compensador (4.62) é dada por

   [img:Illustration] 

  As respostas ao degrau unitário do sistema não compensado (4.47), do sistema compensado de segunda ordem (4.63) e do sistema compensado de terceira ordem (4.59) são apresentadas na Figura 4.24. Como o sistema (4.59) é de terceira ordem e o polo localizado em s = –2,6 está próximo dos polos complexos conjugados, a resposta transitória possui um sobressinal um pouco maior que o desejado (Mp ≅ 16 %). Já o sistema (4.63), por ser de segunda ordem, produz uma resposta de acordo com as especificações.

  No projeto de compensadores nem sempre é possível realizar cancelamentos de modo a reduzir a ordem do sistema. Em sistemas de ordem elevada, se os polos dominantes estiverem próximos dos demais polos e zeros a resposta transitória pode não ocorrer exatamente de acordo com as especificações desejadas. Por essa razão, é necessário analisar os resultados obtidos empregando-se também recursos computacionais. O projeto do compensador deve ser refeito até que os resultados obtidos possam ser considerados satisfatórios.

   [img:Illustration] 

  Figura 4.24 Respostas ao degrau unitário do sistema não compensado (4.47), do sistema compensado de segunda ordem (4.63) e do sistema compensado de terceira ordem (4.59).

  ■

  

#### 4.6.2 Compensação por atraso de fase

  O bloco típico de um compensador por atraso de fase (lag phase) tem a função de transferência

   [img:Illustration] 

  O diagrama de polos e zeros de um compensador por atraso de fase é apresentado na Figura 4.25. O polo do compensador pc deve estar localizado mais próximo do eixo imaginário, quando comparado ao zero zc. A designação atraso de fase reside no fato de que para qualquer ponto s com Re < 0 e Im > 0 o compensador Gc(s) diminui a fase da malha aberta, pois ∠Gc(s) = φ – θ < 0.

   [img:Illustration] 

  Figura 4.25 Diagrama de polos e zeros de um compensador por atraso de fase.

  A compensação por atraso de fase é indicada quando a resposta transitória é satisfatória, mas o erro no estado estacionário precisa ser melhorado. Ao contrário do compensador por avanço, o compensador por atraso tende a piorar a resposta transitória pois tende a deslocar o lugar das raízes no sentido da direita do semiplano s. Para que o lugar das raízes não seja modificado com a inclusão do compensador na malha a contribuição de fase do compensador deve ser próxima de zero. De acordo com a Figura 4.26, isso somente é possível se o polo pc e o zero zc do compensador estiverem próximos um do outro.

   [img:Illustration] 

  Figura 4.26 Lugar das raízes. (a) Sem compensador. (b) Com compensador.

  Analisando a Figura 4.26 verifica-se que quando o polo pc e o zero zc do compensador estão próximos a contribuição de fase é praticamente nula. Além disso, as distâncias do polo pc e do zero zc até o ponto s, onde estaria um polo de malha fechada desejado, são praticamente as mesmas. Com isso, o ganho kc do compensador vale aproximadamente 1, pois os vetores que representam estas distâncias são aproximadamente iguais.

  Considere um sistema com realimentação unitária, sem o compensador por atraso de fase, cuja função de transferência de malha aberta seja dada por

   [img:Illustration] 

  sendo k um ganho, τi (i = 1, . . ., m) e Tj (j = 1, . . ., n) constantes de tempo não nulas.

  Aplicando-se uma rampa unitária na referência, o erro estacionário sem compensador es(∞) pode ser calculado por meio do teorema do valor final, ou seja,

   [img:Illustration] 

  Considere agora um sistema com compensador por atraso de fase, com kc ≅ 1. A função de transferência de malha aberta é dada por

   [img:Illustration] 

  Aplicando-se uma rampa unitária na referência, o erro estacionário com compensador ec(∞) vale

   [img:Illustration] 

  Das Equações (4.66) e (4.68) tem-se que a relação entre os erros estacionários com e sem compensador é dada por

   [img:Illustration] 

  Para que o erro estacionário com compensador ec(∞) seja, por exemplo, 10 vezes menor que o erro sem compensador es(∞) o zero do compensador deve ser 10 vezes maior que o seu polo, isto é, zc = 10pc. Portanto, a única maneira de a relação entre o zero e o polo ser "grande" de modo a reduzir o erro estacionário e, simultaneamente, ter o polo e o zero do compensador próximos um do outro, para que a resposta transitória não seja afetada, é que pc e zc devem estar localizados próximos da origem. Assim, escolhendo por exemplo o polo em pc = –0,01 o zero deve estar em zc = –0,1.

  

### Exemplo 4.8

  Considere um sistema com a seguinte função de transferência de malha aberta:

   [img:Illustration] 

  O diagrama de blocos do sistema em malha fechada sem compensador é apresentado na Figura 4.27.

   [img:Illustration] 

  Figura 4.27 Diagrama de blocos do sistema em malha fechada sem compensador.

  A função de transferência de malha fechada é dada por

   [img:Illustration] 

  Logo, os polos de malha fechada dominantes do sistema sem compensador estão localizados em s1,2 = –0,776 ± 2,045j, com coeficiente de amortecimento ξ ≅ 0,355 e frequência natural ωn ≅ 2,188.

  Aplicando-se um degrau unitário na referência, o erro estacionário es(∞) sem compensador é

   [img:Illustration] 

  Deseja-se projetar um compensador Gc(s) por atraso de fase de modo a reduzir o erro estacionário em 10 vezes, sem que a resposta transitória tenha mudança significativa. A função de transferência de malha aberta com o compensador Gc(s) é dada por

   [img:Illustration] 

  Logo, o erro estacionário ec(∞) com compensador vale

   [img:Illustration] 

  Para que a resposta transitória não tenha mudança significativa com o compensador Gc(s), a posição dos polos de malha fechada dominantes deve ser praticamente a mesma no lugar das raízes. Para isso, o ganho kc deve valer aproximadamente 1. Logo,

   [img:Illustration] 

  Escolhendo arbitrariamente o valor do polo pc = 0,01 próximo da origem, obtém-se zc = 0,1225.

   [img:Illustration] 

  Figura 4.28 Lugar das raízes do sistema compensado.

  Na Figura 4.28 é apresentado o lugar das raízes do sistema compensado. Traçando uma reta pelo coeficiente de amortecimento ξ ≅ 0,355 obtêm-se os polos de malha fechada dominantes do sistema compensado, que estão em s1,2 = –0,74 ± 1,96j.

  O ganho kc pode ser ajustado pela condição de módulo

   [img:Illustration] 

  Portanto, a função de transferência do compensador por atraso de fase é

   [img:Illustration] 

  A função de transferência de malha fechada do sistema compensado é dada por

   [img:Illustration] 

  Na Figura 4.29 são apresentados os gráficos da resposta ao degrau unitário dos sistemas em malha fechada compensado e não compensado. A inclusão do compensador aumenta a ordem do sistema de 3 para 4, acrescentando um polo em s = –0,103 e um zero em s = –0,1225 próximos dos polos dominantes. Com isso, a resposta transitória do sistema compensado é um pouco diferente do sistema não compensado. Porém, o erro estacionário foi reduzido de acordo com o esperado.

   [img:Illustration] 

  Figura 4.29 Respostas ao degrau unitário dos sistemas compensado e não compensado.

  ■

  

#### 4.6.3 Compensação por avanço e atraso de fase

  A compensação por avanço e atraso de fase (lead-lag phase) é muito utilizada na prática, e aplica os dois recursos analisados anteriormente. Esta compensação é indicada quando é necessário melhorar simultaneamente a resposta transitória e o erro no estado estacionário.

  Primeiramente, projeta-se um compensador por avanço de fase para melhorar a resposta transitória. Depois calcula-se quanto o erro estacionário ainda deve ser melhorado. Por fim, projeta-se o compensador por atraso de fase para satisfazer a especificação do erro estacionário.

  

### Exemplo 4.9

  Projete um compensador por avanço e atraso de fase para o sistema da Figura 4.30, de modo que a resposta para entrada do tipo degrau na referência apresente:

  
    • polos dominantes com coeficiente de amortecimento ξ = 0,5 e frequência ωn = 2 (rad/s);

    • erro no estado estacionário de 0,02.

  

   [img:Illustration] 

  Figura 4.30 Diagrama de blocos de um sistema em malha fechada sem compensador.

  Para que as especificações sejam satisfeitas os polos de malha fechada dominantes do sistema compensado devem estar localizados em

   [img:Illustration] 

  Se os polos dominantes tiverem influência predominante na dinâmica do sistema, então a resposta ao degrau deve apresentar um sobressinal próximo de Mp ≅ 16,3% e um tempo de acomodação próximo de ts ≅ 3 s (critério 5%).

  A função de transferência do compensador por avanço de fase é dada por

   [img:Illustration] 

  Cancelando o zero do compensador com um dos polos em s = –1 do processo, a função de transferência de malha aberta resulta como

   [img:Illustration] 

  Pela condição de fase

   [img:Illustration] 

  ou

   [img:Illustration] 

  No polo de malha fechada  [img:Illustration]  tem-se que

   [img:Illustration] 

  Calculando a tangente dos dois membros da Equação (4.84), obtém-se

   [img:Illustration] 

  O valor do ganho kc > 0 pode ser obtido por meio da condição de módulo, ou seja,

   [img:Illustration] 

  Portanto, a função de transferência do compensador por avanço de fase é dada por

   [img:Illustration] 

  O lugar das raízes do sistema com o compensador (4.87) é apresentado na Figura 4.31.

   [img:Illustration] 

  Figura 4.31 Lugar das raízes com o compensador por avanço de fase.

  A função de transferência de malha fechada apenas com o compensador por avanço de fase é dada por

   [img:Illustration] 

  cuja resposta ao degrau unitário é apresentada na Figura 4.32. Note que o sistema em malha fechada com o compensador por avanço de fase apresenta um transitório próximo das especificações (sobressinal Mp ≅ 16,2% e tempo de acomodação ts ≅ 3 s, pelo critério de 5%). Porém, o erro estacionário ainda é elevado, pois e(∞) = 1 – 0,68 = 0,32.

   [img:Illustration] 

  Figura 4.32 Resposta ao degrau unitário do sistema em malha fechada apenas com o compensador por avanço de fase.

  A seguir, deve-se projetar um compensador por atraso de fase de modo a reduzir o erro estacionário para 0,02, sem que o transitório do sistema com o compensador por avanço de fase tenha alteração significativa.

  Supondo que a função de transferência do compensador por atraso de fase seja dada por

   [img:Illustration] 

  a função de transferência de malha aberta com o compensador por avanço e atraso de fase é

   [img:Illustration] 

  Logo, o erro estacionário e(∞) com o compensador por avanço e atraso de fase vale

   [img:Illustration] 

  Para que o transitório não tenha mudança significativa com o compensador por atraso de fase, a posição dos polos de malha fechada dominantes deve ser praticamente a mesma no lugar das raízes. Para isso, o ganho kat deve valer aproximadamente 1. Assim,

   [img:Illustration] 

  Escolhendo arbitrariamente o polo pat = 0,01 próximo da origem, obtém-se zat = 0,2333.

  Na Figura 4.33 é apresentado o lugar das raízes do sistema compensado. Traçando uma reta pelo coeficiente de amortecimento ξ = 0,5 obtêm-se os polos de malha fechada dominantes do sistema compensado, que estão em s1,2 = –0,93 ± 1,61j.

   [img:Illustration] 

  Figura 4.33 Lugar das raízes do sistema compensado.

  O ganho kat pode ser ajustado pela condição de módulo

   [img:Illustration] 

  Portanto, a função de transferência do compensador por avanço e atraso de fase é dada pelo produto das Equações (4.87) e (4.89), ou seja,

   [img:Illustration] 

  A função de transferência de malha fechada do sistema compensado resultante é de quarta ordem e é dada por

   [img:Illustration] 

  Na Figura 4.34 são apresentados os gráficos da resposta ao degrau unitário dos sistemas em malha fechada sem compensador, apenas com o compensador por avanço (4.87) e com o compensador por avanço e atraso (4.94). A inclusão do compensador por atraso aumenta a ordem do sistema de 3 para 4, acrescentando um polo em s = –0,17 e um zero em s = –0,2333 próximos dos polos dominantes, afetando dessa maneira a resposta transitória. Porém, o erro estacionário foi reduzido de acordo com o esperado.

   [img:Illustration] 

  Figura 4.34 Respostas ao degrau unitário dos sistemas em malha fechada sem compensador, apenas com o compensador por avanço (4.87) e com o compensador por avanço e atraso (4.94).

  ■

  

#### 4.6.4 Compensação por realimentação auxiliar

  Nas seções anteriores os compensadores foram projetados para serem ligados em série com o processo, de modo a modificarem o lugar das raízes para produzirem uma resposta transitória desejada. Sistemas de controle também podem ser projetados com a inclusão de uma malha de realimentação auxiliar, conforme mostra a Figura 4.35.

   [img:Illustration] 

  Figura 4.35 Sistema com realimentação auxiliar.

  Este é um método de extraordinário poder, tanto para estabilizar quanto para aperfeiçoar os transientes do sistema. Em contrapartida, exige equipamento e custo adicional como, por exemplo, a inclusão de mais um sensor na malha. A realimentação auxiliar é comumente utilizada em motores, para controlar a posição angular θ(t) de um eixo. Nesse caso a realimentação adicional é realizada por meio de um sensor da velocidade ω(t), que pode ser um tacômetro com ganho Kt. O ganho Kp pode representar um potenciômetro que visa converter a posição angular θ(t) numa tensão equivalente vp(t).

  Agrupando o ganho Kp com a função G2(s) e deslocando a realimentação auxiliar, o diagrama de blocos da Figura 4.35 pode ser representado de forma equivalente pelo diagrama da Figura 4.36.

   [img:Illustration] 

  Figura 4.36 Sistema com realimentação auxiliar equivalente.

  Da Figura 4.36 tem-se que

   [img:Illustration] 

  Com o resultado da Equação (4.96) pode-se simplificar o diagrama de blocos da Figura 4.36 para o diagrama da Figura 4.37.

   [img:Illustration] 

  Figura 4.37 Diagrama de blocos equivalente ao da Figura 4.36.

  A função de transferência de malha aberta G(s)H(s) do sistema da Figura 4.37 é

   [img:Illustration] 

  Sem a realimentação auxiliar, a função de transferência de malha aberta é

   [img:Illustration] 

  Comparando as Equações (4.97) e (4.98) verifica-se que o efeito de se acrescentar a realimentação auxiliar é equivalente a substituir os polos e zeros de G2(s) pelos polos e zeros de G2(s)Kp + Kt. Esta mudança visa alterar o lugar das raízes para que o mesmo passe pelos polos de malha fechada que satisfazem à especificação da resposta transitória desejada.

  

### Exemplo 4.10

  Deseja-se controlar a posição angular θ(t) do eixo de um motor representado pelo diagrama de blocos da Figura 4.38.

   [img:Illustration] 

  Figura 4.38 Diagrama de blocos de um motor com realimentação auxiliar da velocidade ω(t).

  Considere inicialmente o sistema da Figura 4.38 sem a realimentação auxiliar, cuja função de transferência de malha aberta é

   [img:Illustration] 

  A função de transferência de malha fechada de segunda ordem é

   [img:Illustration] 

  O lugar das raízes do sistema sem a realimentação auxiliar é apresentado na Figura 4.39.

   [img:Illustration] 

  Figura 4.39 Lugar das raízes sem a realimentação auxiliar.

  Supondo que o ganho k seja ajustado para que os polos de malha fechada sejam complexos conjugados com coeficiente de amortecimento ξ = 0,5 (Mp ≅ 16,3%), então, da Equação (4.100) tem-se que 1 = 2ξωn ⇒ ωn = 1 (rad/s). Logo,  [img:Illustration] 

  O tempo de acomodação (critério 2%) da resposta ao degrau unitário resulta

   [img:Illustration] 

  Suponha que o tempo de acomodação deva ser reduzido para 2 s, mantendo-se o valor do coeficiente de amortecimento ξ = 0,5. Neste caso, tem-se que

   [img:Illustration] 

  Para ts(2%) ≅ 2 s, os novos polos de malha fechada devem estar localizados em

   [img:Illustration] 

  Note que sem a realimentação auxiliar é impossível fazer com que o lugar das raízes da Figura 4.39 passe pelos polos de malha fechada (4.103).

  Considere agora o sistema da Figura 4.38 com realimentação auxiliar. Da Equação (4.97) tem-se que a função de transferência de malha aberta é dada por

   [img:Illustration] 

  ou seja, quando é feita a realimentação auxiliar aparece um zero em s = –1/Kt na função de transferência de malha aberta. O lugar das raízes do sistema com a realimentação auxiliar é apresentado na Figura 4.40.

   [img:Illustration] 

  Figura 4.40 Lugar das raízes com a realimentação auxiliar. (a) 0 < Kt < 1. (b) Kt > 1.

  Para Kt > 1 os polos de malha fechada são sempre reais e a resposta transitória é sempre amortecida. Porém, como um dos polos está próximo do eixo imaginário a resposta transitória é lenta.

  Para 0 < Kt < 1 é possível fazer com que o lugar das raízes passe pelos polos de projeto (4.103). O valor do ganho Kt pode ser determinado pela condição de fase

   [img:Illustration] 

  No polo de malha fechada  [img:Illustration]  tem-se que

   [img:Illustration] 

  Calculando a tangente dos dois membros da Equação (4.106) resulta

   [img:Illustration] 

  O valor do ganho k > 0 pode ser obtido por meio da condição de módulo, ou seja,

   [img:Illustration] 

  Os valores dos ganhos k e Kt também podem ser obtidos a partir da função de transferência de malha fechada Θ(s)/Θr (s). Da Figura 4.38 tem-se que

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  Comparando os coeficentes dos polinômios da Equação (4.110), obtém-se que  [img:Illustration]  e 1 + k Kt = 2ξωn ⇒ Kt = 0,1875.

  Na Figura 4.41 são apresentados os gráficos da resposta ao degrau unitário dos sistemas em malha fechada sem realimentação auxiliar (4.100) e com realimentação auxiliar (4.110). As duas respostas apresentam o mesmo sobressinal (Mp ≅ 16%). Porém, a resposta transitória do sistema com realimentação auxiliar é mais rápida (ts(2%) ≅ 2 s) que a resposta do sistema sem este recurso (ts(2%) ≅ 8 s).

   [img:Illustration] 

  Figura 4.41 Respostas ao degrau unitário do sistema sem realimentação auxiliar e com realimentação auxiliar.

  ■

  

### 4.7 Implementação analógica de compensadores

  Os compensadores por avanço ou atraso de fase podem ser implementados analogicamente por meio de amplificadores operacionais.

  

#### 4.7.1 Compensador por avanço ou atraso de fase de ordem 1

  A função de transferência do compensador por avanço ou atraso de fase de ordem 1 é dada por

   [img:Illustration] 

  O circuito eletrônico equivalente está representado na Figura 4.42. Deste circuito tem-se que

   [img:Illustration] 

  Assim,

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  O circuito da Figura 4.42 é um compensador por avanço de fase quando R1C1 > R2C2 e é um compensador por atraso de fase quando R1C1 < R2C2.

   [img:Illustration] 

  Figura 4.42 Circuito eletrônico do compensador por avanço ou atraso de fase de ordem 1.

  

#### 4.7.2 Compensador por avanço ou atraso de fase de ordem 2

  A função de transferência do compensador por avanço ou atraso de fase de ordem 2 é dada por

   [img:Illustration] 

  O circuito eletrônico equivalente está representado na Figura 4.43. Deste circuito tem-se que

   [img:Illustration] 

  Assim,

   [img:Illustration] 

   [img:Illustration] 

  Figura 4.43 Circuito eletrônico do compensador por avanço ou atraso de fase de ordem 2.

  

### 4.8 Exercícios resolvidos

  

### Exercício 4.1

  Desenhe o lugar das raízes e determine a faixa de valores do ganho k do controlador de modo que o sistema em malha fechada da Figura 4.44 seja estável.

   [img:Illustration] 

  Figura 4.44 Diagrama de blocos de um sistema em malha fechada.

  Solução

  Primeiramente deve-se marcar os polos e o zero de malha aberta no eixo real. À direita do polo em s = +6 não há raízes (quantidade par). Logo, o segmento do eixo real de +6 a +∞ não faz parte do lugar das raízes. O segmento entre 0 e +6 faz parte do lugar das raízes, pois à direita do polo, na origem, há uma raiz em s = +6 (quantidade ímpar). O segmento do intervalo de –2 a 0 também não faz parte do lugar das raízes, pois à direita do zero em s = –2 há duas raízes (quantidade par). O outro segmento que também faz parte do lugar das raízes é o que está entre –∞ e –2, pois à direita de qualquer ponto deste segmento há três raízes (quantidade ímpar).

  O lugar das raízes começa nos polos e termina nos zeros de malha aberta quando k varia de zero a infinito. Como há dois polos de malha aberta adjacentes sobre o eixo real (s = 0 e s = +6) e como o segmento entre eles faz parte do lugar das raízes, então há um ponto de partida neste segmento. Da mesma forma, como o segmento de –∞ a –2 pertence ao lugar das raízes e considerando que há dois zeros neste segmento, isto é, um zero em s = –2 e outro em s = –∞, então também há um ponto de chegada neste segmento.

  A função de transferência do sistema em malha fechada é dada por

   [img:Illustration] 

  Assim, a equação característica é

   [img:Illustration] 

  Aplicando a condição (4.21), obtém-se

   [img:Illustration] 

  ou seja,

   [img:Illustration] 

  Extraindo as raízes do polinômio (4.123) verifica-se que há um ponto de partida em s = +2 e um ponto de chegada em s = –6. O gráfico do lugar geométrico das raízes apresenta o aspecto da Figura 4.45.

   [img:Illustration] 

  Figura 4.45 Lugar geométrico das raízes.

  Para mostrar que parte do lugar das raízes forma uma circunferência basta verificar a condição de fase (4.5), ou seja,

   [img:Illustration] 

  Substituindo s = a + jω e escolhendo r = 0, obtém-se

   [img:Illustration] 

  ou

   [img:Illustration] 

  Aplicando a identidade trigonométrica

   [img:Illustration] 

  obtém-se

   [img:Illustration] 

  A Equação (4.127) também pode ser escrita como

   [img:Illustration] 

  que representa a equação de uma circunferência com centro no ponto (–2, 0) e raio igual a 4.

  Para determinar a faixa de valores do ganho k de modo que o sistema em malha fechada seja estável basta aplicar o critério de Routh. Os coeficientes do polinômio do denominador da função de transferência de malha fechada (4.120) estão presentes e têm o mesmo sinal quando k > 6. Portanto, o sistema em malha fechada é estável para k > 6.

  Outra maneira de encontrar o valor de k é determinar os pontos de cruzamento do lugar das raízes com o eixo imaginário, bastando para isso fazer s = jω na equação característica. Igualando as partes real e imaginária a zero obtêm-se os pontos de cruzamento e o valor de k nestes pontos. Então,

   [img:Illustration] 

  Logo, a parte imaginária da Equação (4.129) é nula para k = 6 e os pontos de cruzamento do lugar das raízes no eixo imaginário estão localizados em  [img:Illustration] 

  

### Exercício 4.2

  Desenhe o lugar das raízes e determine a faixa de valores do ganho k de modo que o sistema em malha fechada da Figura 4.46 seja estável.

   [img:Illustration] 

  4.46 Diagrama de blocos de um sistema em malha fechada.

  Solução

  A função de transferência de malha aberta possui um zero em s = –1 (m = 1) e três polos (n = 3), sendo um polo localizado em s = +1 e os outros dois em s = –2. No eixo real apenas o segmento entre –1 e +1 faz parte do lugar das raízes, pois à direita do zero em s = –1 a quantidade de raízes é um número ímpar, isto é, há um polo em s = +1. Os demais segmentos, localizados nos intervalos de –∞ a –2 , –2 a –1 e +1 a +∞, não fazem parte do lugar das raízes pois a quantidade de raízes localizadas à direita de qualquer ponto de teste desses segmentos resulta sempre num número par.

  Assim, o lugar das raízes possui n = 3 ramos. Um ramo começa no polo em s = +1 e termina no zero em s = –1, e os outros dois ramos começam nos polos em s = –2 e terminam no infinito, seguindo assíntotas com os seguintes ângulos:

   [img:Illustration] 

  As assíntotas cruzam o eixo real no ponto

   [img:Illustration] 

  O gráfico do lugar geométrico das raízes apresenta o aspecto da Figura 4.47. Note que o mesmo deve satisfazer à propriedade de simetria com relação ao eixo real.

   [img:Illustration] 

  Figura 4.47 Lugar geométrico das raízes.

  O valor de k > 0, em qualquer ponto do lugar das raízes, pode ser calculado a partir da condição de módulo (4.4), ou seja,

   [img:Illustration] 

  Calculando o valor de k em s = 0, obtém-se k = 4. Com isso, o sistema em malha fechada é estável para qualquer valor de k > 4, pois neste caso as linhas do lugar das raízes, que representam os polos de malha fechada, estão sempre localizadas no semiplano esquerdo do plano s.

  

### Exercício 4.3

  Desenhe o lugar das raízes e determine a faixa de valores do ganho k de modo que o sistema em malha fechada da Figura 4.48 seja estável.

   [img:Illustration] 

  Figura 4.48 Diagrama de blocos de um sistema em malha fechada.

  Solução

  A função de transferência de malha aberta possui um polo na origem e dois polos complexos conjugados localizados em s = –4 ± 2j. Assim, o lugar das raízes possui n = 3 ramos, sendo os ângulos das assíntotas:

   [img:Illustration] 

  Um ramo começa no polo em s = 0 e termina em –∞ seguindo a assíntota de 180o. Os outros dois ramos começam nos polos complexos e terminam no infinito seguindo as assíntotas com ângulos de 60o e 300o.

  As assíntotas cruzam o eixo real no ponto

   [img:Illustration] 

  A função de transferência de malha fechada é dada por

   [img:Illustration] 

  Assim, a equação característica é

   [img:Illustration] 

  Os pontos de partida e de chegada no eixo real são calculados a partir da condição (4.21), ou seja,

   [img:Illustration] 

  As raízes da Equação (4.137) são s = –2 e s ≅ –3,33. Como estes pontos fazem parte do lugar das raízes, então eles são pontos de partida e de chegada. O gráfico do lugar geométrico das raízes apresenta o aspecto da Figura 4.49.

   [img:Illustration] 

  Figura 4.49 Lugar geométrico das raízes.

  Os ângulos de partida dos polos complexos podem ser calculados pela condição de fase. Por exemplo, o ângulo de partida do polo em s = –4 + 2j é dado por

   [img:Illustration] 

  Para determinar a faixa de valores do ganho k de modo que o sistema em malha fechada seja estável basta aplicar o critério de Routh. A partir do denominador da função de transferência de malha fechada (4.135) pode-se montar a Tabela 4.3.

  Tabela 4.3 Tabela de Routh

   [img:Illustration] 

  Os coeficientes b1 e c1 da tabela de Routh valem

   [img:Illustration] 

  Todos os coeficientes da primeira coluna da tabela de Routh têm o mesmo sinal para

   [img:Illustration] 

  Portanto, o sistema em malha fechada é estável para 0 < k < 160.

  Outra maneira de encontrar o valor de k é determinar os pontos de cruzamento do lugar das raízes com o eixo imaginário, bastando para isso fazer s = jω na equação característica (4.136). Igualando as partes real e imaginária a zero obtêm-se os pontos de cruzamento e o valor de k nesses pontos. Então,

   [img:Illustration] 

  Logo, os pontos de cruzamento do lugar das raízes no eixo imaginário estão localizados em  [img:Illustration] , e o valor de k nestes pontos vale k = 8ω2 = 160.

  

### Exercício 4.4

  Desenhe o lugar das raízes e determine a faixa de valores do ganho k de modo que o sistema em malha fechada da Figura 4.50 seja estável.

   [img:Illustration] 

  Figura 4.50 Diagrama de blocos de um sistema em malha fechada.

  Solução

  A função de transferência de malha aberta possui quatro polos, que estão localizados em s = 0, s = –1 (polo duplo) e s = –2. Os segmentos do eixo real que fazem parte do lugar das raízes estão nos intervalos de 0 a –1 e de –1 a –2. O lugar das raízes possui n = 4 ramos, que começam nos polos e terminam no infinito seguindo assíntotas com os ângulos:

   [img:Illustration] 

  As assíntotas cruzam o eixo real no ponto

   [img:Illustration] 

  A função de transferência de malha fechada é dada por

   [img:Illustration] 

  Assim, a equação característica é

   [img:Illustration] 

  Os pontos de partida do eixo real são calculados a partir da condição (4.21), ou seja,

   [img:Illustration] 

  As raízes da Equação (4.146) são s ≅ –0,29, s ≅ –1,71 e s = –1. Como estes pontos fazem parte do lugar das raízes eles são pontos de partida do eixo real. O gráfico do lugar geométrico das raízes apresenta o aspecto da Figura 4.51.

   [img:Illustration] 

  Figura 4.51 Lugar geométrico das raízes.

  Para determinar a faixa de valores do ganho k de modo que o sistema em malha fechada seja estável basta aplicar o critério de Routh. A partir do denominador da função de transferência de malha fechada (4.144) pode-se montar a Tabela 4.4.

  Tabela 4.4 Tabela de Routh

   [img:Illustration] 

  Os coeficientes da tabela de Routh valem

   [img:Illustration] 

  Todos os coeficientes da primeira coluna da tabela de Routh têm o mesmo sinal para

   [img:Illustration] 

  Portanto, o sistema em malha fechada é estável para 0 < k < 2,25.

  Outra maneira de encontrar o valor de k é determinar os pontos de cruzamento do lugar das raízes com o eixo imaginário, bastando para isso fazer s = jω na equação característica (4.145). Igualando as partes real e imaginária a zero obtêm-se os pontos de cruzamento e o valor de k nesses pontos. Então,

   [img:Illustration] 

  Logo, os pontos de cruzamento do lugar das raízes no eixo imaginário estão localizados em  [img:Illustration]  e o valor de k nestes pontos vale k = 5ω2 – ω4 = 2,25.

  

### Exercício 4.5

  Desenhe o lugar das raízes do sistema em malha fechada da Figura 4.52.

   [img:Illustration] 

  Figura 4.52 Diagrama de blocos de um sistema em malha fechada.

  Solução

  A função de transferência de malha aberta possui n = 2 polos (s = 0 e s = –4) e m = 2 zeros  [img:Illustration] . O segmento do eixo real no intervalo aberto de 0 a –4 pertence ao lugar das raízes, pois à direita de qualquer ponto deste segmento há um número ímpar de raízes. O lugar das raízes começa nos polos e termina nos zeros de malha aberta, quando k varia de zero a infinito. Como há dois polos de malha aberta adjacentes sobre o eixo real (s = 0 e s = –4) e como o segmento entre eles faz parte do lugar das raízes, então há um ponto de partida neste segmento.

  A função de transferência do sistema em malha fechada é dada por

   [img:Illustration] 

  Assim, a equação característica é

   [img:Illustration] 

  Aplicando a condição (4.21), obtém-se

   [img:Illustration] 

  ou seja,

   [img:Illustration] 

  As raízes do polinômio (4.153) são s = –1 e s = +2. Porém, apenas o ponto s = –1 é ponto de partida, pois o ponto em s = +2 não faz parte do lugar das raízes.

  O gráfico do lugar geométrico das raízes apresenta o aspecto da Figura 4.53.

   [img:Illustration] 

  Figura 4.53 Lugar geométrico das raízes.

  O valor de k > 0 em qualquer ponto do lugar das raízes pode ser calculado a partir da condição de módulo (4.4), ou seja,

   [img:Illustration] 

  Calculando o valor de k no ponto de partida em s = –1, obtém-se k = 1.

  Para mostrar que parte do lugar das raízes forma uma circunferência basta verificar a condição de fase (4.5), ou seja,

   [img:Illustration] 

  Substituindo s = a + jω e escolhendo r = 0, obtém-se

   [img:Illustration] 

  ou

   [img:Illustration] 

  Sabendo-se que

   [img:Illustration] 

  obtém-se

   [img:Illustration] 

  A Equação (4.158) pode ser simplificada para

   [img:Illustration] 

  que representa a equação de uma circunferência com centro no ponto ( [img:Illustration] , 0) e raio igual a 1,5.

  

### Exercício 4.6

  Considere o sistema estável em malha aberta cuja função de transferência é

   [img:Illustration] 

  Utilizando a aproximação de Padé de ordem(2,2), pede-se que

  • desenhe o lugar das raízes;

  • determine os pontos de cruzamento do lugar das raízes com o eixo imaginário e a faixa de valores do ganho k de modo que o sistema em malha fechada seja estável.

  Solução

  Da Tabela 4.2, obtém-se

   [img:Illustration] 

  com zeros em s = 1,5 ± 0,866j e com polos em s = –1 e s = –1,5 ± 0,866j.

  O gráfico do lugar das raízes está representado na Figura 4.54. Note que o sistema com atraso puro (4.160) é estável em malha fechada apenas para uma faixa de valores do ganho k, pois o lugar das raízes cruza o eixo imaginário.

   [img:Illustration] 

  4.54 Lugar das raízes.

  A função de transferência de malha fechada com realimentação unitária é

   [img:Illustration] 

  Os pontos de cruzamento do lugar das raízes com o eixo imaginário podem ser determinados por meio da substituição s = 0 + jω no denominador da função Gmf (s), ou seja,

   [img:Illustration] 

  ou

   [img:Illustration] 

  Igualando a zero as partes imaginária e real, obtém-se

   [img:Illustration] 

  A única solução da Equação (4.166) para k > 0 é k ≅ 1,54. Logo, os pontos de cruzamento do lugar das raízes com o eixo imaginário são ωj = ±1,17j.

  Do lugar das raízes conclui-se que o sistema em malha fechada é estável para 0 < k < 1,54. Observe que com a aproximação de Padé de ordem (2,2) o valor de k é um pouco maior que o ganho k < 1,5, calculado por meio da função exata no Exemplo 4.4.

  

### Exercício 4.7

  Considere um sistema com realimentação unitária cujo gráfico do lugar das raízes é apresentado na Figura 4.55. Sabendo-se que é aplicado um degrau unitário na referência, calcule:

  a) o ganho para que a resposta do sistema em malha fechada tenha amortecimento crítico;

  b) ganho e o tempo de subida para que a resposta do sistema em malha fechada tenha um sobressinal máximo de 16,3%;

  c) o erro estacionário em cada um dos casos anteriores.

   [img:Illustration] 

  Figura 4.55 Lugar das raízes.

  Solução

  a) O gráfico do lugar das raízes da Figura 4.55 representa um sistema de segunda ordem com função de transferência de malha aberta

   [img:Illustration] 

  A resposta do sistema em malha fechada tem amortecimento crítico quando os polos de malha fechada são reais e iguais. Pelo lugar das raízes isso ocorre em s = –5. Da condição de módulo (4.4)

   [img:Illustration] 

  b) O sobressinal é dado por

   [img:Illustration] 

  cujo coeficiente de amortecimento vale ξ ≅ 0,5.

  Para que a resposta transitória tenha sobressinal os polos de malha fechada devem ser complexos conjugados. Do lugar das raízes a parte real desses polos vale –ξωn = –5.

  Logo, ωn = 10 (rad/s), e os polos de malha fechada devem estar localizados em

   [img:Illustration] 

  Da condição de módulo (4.4)

   [img:Illustration] 

  O tempo de subida é dado por

   [img:Illustration] 

  c) O erro estacionário pode ser calculado pelo teorema do valor final

   [img:Illustration] 

  Para k = 9 ⇒ e(∞) ≅ 0,64 e para k = 84 ⇒ e(∞) ≅ 0,16.

  

### Exercício 4.8

  Desenhe o lugar das raízes para o sistema da Figura 4.56 quando o parâmetro p é variável e classifique a resposta transitória da saída quando a entrada de referência é do tipo degrau.

   [img:Illustration] 

  4.56 Sistema com um parâmetro p variável.

  Solução

  A função de transferência de malha fechada é dada por

   [img:Illustration] 

  Para desenhar o lugar das raízes é necessário que o parâmetro p funcione como um ganho variável e apareça como um fator multiplicador na função de transferência de malha aberta G(s)H(s). Isto pode ser conseguido dividindo-se o numerador e o denominador de (4.174) pelos termos do denominador desta equação que não possuem o parâmetro p, ou seja,

   [img:Illustration] 

  Da Equação (4.175) pode-se identificar a função de transferência de malha aberta equivalente

   [img:Illustration] 

  O lugar das raízes quando o parâmetro p varia de 0 a ∞ é apresentado na Figura 4.57.

   [img:Illustration] 

  Figura 4.57 Lugar das raízes com um parâmetro p variável.

  O valor do parâmetro p no ponto de chegada s = –6 pode ser calculado pela condição de módulo, ou seja,

   [img:Illustration] 

  Do lugar das raízes tem-se que:

  • para 0 < p < 8 os polos de malha fechada são complexos conjugados e a resposta transitória é subamortecida;

  • para p = 0 e p = 8 os polos de malha fechada são reais e iguais a s = –2 e s = –6, respectivamente, e a resposta transitória tem amortecimento crítico;

  • para p > 8 os polos de malha fechada são reais e diferentes e a resposta transitória é superamortecida.

  

### Exercício 4.9

  O diagrama de blocos da Figura 4.58 representa um motor CC com realimentação auxiliar da velocidade v(t). Determine os valores dos ganhos Kc e Kt para que a resposta da posição x(t) apresente um tempo de subida tr = 0,4 s e coeficiente de amortecimento ξ = 0,7 quando é aplicado um degrau na referência.

   [img:Illustration] 

  Figura 4.58 Motor CC com realimentação auxiliar da velocidade v(t).

  Solução

  Do tempo de subida obtém-se a frequência natural ωn, ou seja,

   [img:Illustration] 

  A função de transferência da malha interna é

   [img:Illustration] 

  A função de transferência da malha externa é

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  Na Figura 4.59 é apresentada a resposta x(t) para um degrau unitário na referência xref (t). Para ξ = 0,7 o sobressinal é Mp ≅ 4,6%.

   [img:Illustration] 

  Figura 4.59 Resposta x(t) para um degrau unitário na referência xref (t).

  

### Exercício 4.10

  Um pêndulo invertido é montado sobre um carrinho que se movimenta no eixo horizontal x(t) por meio de um motor CC acoplado ao trilho. O pêndulo possui movimento angular θ(t), conforme é mostrado na Figura 4.60. Deseja-se obter um modelo que descreva o comportamento dinâmico do sistema e projetar um sistema de controle para equilibrar o pêndulo na posição vertical, conforme o carrinho se movimenta no eixo x(t). Suponha que a aceleração da gravidade é g = 10 (m/s2) e que o pêndulo tem comprimento 2l = 1 (m), massa m, momento de inércia J e centro de gravidade no ponto G. Para pequenas variações em torno do ponto de equilíbrio deseja-se que a resposta tenha um tempo de subida tr = 0,5 s e coeficiente de amortecimento ξ = 0,7.

   [img:Illustration] 

  Figura 4.60 Pêndulo invertido sobre um carrinho com movimento no eixo x(t).

  Solução

  O centro de gravidade do pêndulo é o ponto (xG(t) , yG(t)). Da Figura 4.60 tem-se

   [img:Illustration] 

  O movimento de rotação do pêndulo em torno do centro de gravidade é dado por

   [img:Illustration] 

  Supondo que o momento de inércia seja desprezível (J ≅ 0) e que o desvio angular θ(t) em torno da posição vertical seja "pequeno", então podem-se fazer as seguintes aproximações: sen θ(t) ≅ θ(t) e cos θ(t) ≅ 1. Assim,

   [img:Illustration] 

  O movimento horizontal do centro de gravidade do pêndulo é dado por

   [img:Illustration] 

  e o movimento vertical por

   [img:Illustration] 

  Da Equação (4.186) obtém-se

   [img:Illustration] 

  O emprego das aproximações sen θ(t) ≅ θ(t) e cos θ(t) ≅ 1 tem a vantagem de tornar linear o sistema resultante. Isto tem como consequência que o sistema de controle só funciona em regiões próximas do ponto de equilíbrio, isto é, para pequenas variações do ângulo θ(t). Das Equações (4.183) e (4.184) obtêm-se

   [img:Illustration] 

  Da Equação (4.189) obtém-se

   [img:Illustration] 

  ou

   [img:Illustration] 

  Aplicando a transformada de Laplace, com condições iniciais nulas, obtém-se a função de transferência

   [img:Illustration] 

  A função de transferência (4.194) possui como entrada a posição x(t) do carrinho e como saída o desvio angular θ(t). Uma função de transferência alternativa é considerar como saída a posição xG(t) do centro de gravidade, em vez do ângulo θ(t), isto é,

   [img:Illustration] 

  ou seja,

   [img:Illustration] 

  A vantagem em considerar como saída a posição xG(t) e não o ângulo θ(t) é que o sistema de controle também funciona em superfícies inclinadas, cujo ângulo total formado com a vertical é a soma de θ(t) com o ângulo da inclinação da superfície. Quando a realimentação é feita pela posição θ(t) o controlador tende a fazer θ(t) ≅ 0, mas deixando o pêndulo inclinado devido ao ângulo da superfície. Se esta inclinação for elevada o pêndulo pode sair da região de equilíbrio, instabilizando o sistema. Isso já não ocorre quando a realimentação é feita pela posição xG(t), que é a soma da posição x(t) com a projeção de um ângulo qualquer no eixo horizontal.

   [img:Illustration] 

  Figura 4.61 Diagrama de blocos completo do sistema.

  Na Figura 4.61 é apresentado o diagrama de blocos completo do sistema, incluindo o sistema de controle do motor CC, responsável pelo movimento do carrinho no eixo x(t). Para o controle da posição x(t) pode-se empregar um ganho proporcional Kc e outro Kt na realimentação auxiliar de velocidade do motor. O cálculo desses ganhos pode ser feito por meio de especificações transitórias, semelhantes às do Exercício 4.9.

  No estado estacionário a função de transferência X(s)/Xref (s) tem ganho 1. Desse modo o diagrama de blocos pode ser simplificado de acordo com a Figura 4.62.

   [img:Illustration] 

  Figura 4.62 Diagrama de blocos simplificado do sistema.

  O pêndulo invertido é um sistema instável em malha aberta. Para deslocar o polo instável para o semiplano esquerdo do plano s pode-se utilizar um compensador Gc(s) por avanço de fase com função de transferência

   [img:Illustration] 

  Cancelando o zero do compensador com o polo estável do pêndulo  [img:Illustration]  a função de transferência de malha aberta resulta como

   [img:Illustration] 

  Para kc > 0 o sistema em malha fechada é sempre instável, conforme mostra o lugar das raízes da Figura 4.63.

   [img:Illustration] 

  Figura 4.63 Lugar das raízes para kc > 0.

  Para kc < 0 o sistema em malha fechada é estável para uma faixa de ganho kc, conforme mostra o lugar das raízes da Figura 4.64.

   [img:Illustration] 

  Figura 4.64 Lugar das raízes para kc < 0.

  Do tempo de subida obtém-se a frequência natural ωn, ou seja,

   [img:Illustration] 

  Para que as especificações de transitório sejam satisfeitas os polos de malha fechada devem estar localizados em

   [img:Illustration] 

  Para que o lugar das raízes passe pelos polos s1 e s2 é preciso que

   [img:Illustration] 

  O ganho kc < 0, em qualquer ponto do lugar das raízes, pode ser calculado por meio da condição de módulo. Num dos polos de malha fechada tem-se que

   [img:Illustration] 

  ou

   [img:Illustration] 

  Portanto, a função de transferência do compensador por avanço de fase é

   [img:Illustration] 

  Da condição de módulo pode-se calcular o valor do ganho kc < 0 na origem s = 0, ou seja,

   [img:Illustration] 

  Portanto, com o compensador por avanço de fase o sistema em malha fechada é estável apenas para kc < –3.

  Na Figura 4.65 é apresentada a resposta xG(t) para um degrau unitário na referência xGref (t). Para ξ = 0,7 o sobressinal é Mp = [ (2,53 – 2,42)/2,42 ] 100% ≅ 4,6%. Note que a resposta possui um erro estacionário

   [img:Illustration] 

   [img:Illustration] 

  Figura 4.65 Resposta xG(t) para um degrau unitário na referência xGref (t).

  É importante observar que como o sistema real é não linear e como este foi aproximado por um sistema linear, o projetista deve estar atento para o fato de que o compensador projetado funciona apenas para pequenas variações em torno do ponto de equilíbrio θ(t) ≅ 0.

  

### Exercício 4.11

  Considere o sistema da Figura 4.66.

   [img:Illustration] 

  Figura 4.66 Diagrama de blocos do sistema em malha fechada.

  Deseja-se especificar os polos de malha fechada dominantes com coeficiente de amortecimento ξ = 0,5 e frequência natural ωn = 4 (rad/s).

  • Mostre que não é possível satisfazer às especificações se Gc(s) = k.

  • Determine a função de transferência do compensador Gc(s), de modo que os polos de malha fechada dominantes satisfaçam às especificações desejadas.

  Solução

  Para que as especificações sejam satisfeitas os polos de malha fechada dominantes devem estar localizados em

   [img:Illustration] 

  Se Gc(s) = k a função de transferência de malha aberta é G(s) = k/s2 e o lugar das raízes correspondente é o da Figura 4.67. Nesse caso o sistema em malha fechada é BIBO instável, pois os polos de malha fechada estão sempre localizados sobre o eixo imaginário para qualquer 0 < k < ∞.

   [img:Illustration] 

  Figura 4.67 Lugar das raízes com Gc(s) = k.

  Para que o lugar das raízes passe pelos polos  [img:Illustration]  é necessário deslocar o lugar das raízes para a esquerda do plano s. Para isso pode-se empregar um compensador por avanço de fase

   [img:Illustration] 

  Com isso, a função de transferência de malha aberta fica

   [img:Illustration] 

  O polo e o zero do compensador podem ser alocados em diversas posições. Supondo que o polo compensador está 10 vezes mais distante que o seu zero (pc = 10zc), da condição de fase tem-se que

   [img:Illustration] 

  No polo de malha fechada  [img:Illustration]  tem-se que

   [img:Illustration] 

  Calculando a tangente dos dois membros da Equação (4.211), obtém-se

   [img:Illustration] 

  Resolvendo a Equação (4.212), obtém-se  [img:Illustration] , cuja solução é zc ≅ 0,45 ou zc ≅ 3,55.

  O valor do ganho kc > 0 pode ser obtido por meio da condição de módulo, ou seja,

   [img:Illustration] 

  sendo s um dos polos de malha fechada  [img:Illustration] 

  Para zc = 0,45 e pc = 4,5 obtém-se kc ≅ 18 e

   [img:Illustration] 

  Para zc = 3,55 e pc = 35,5 obtém-se kc ≅ 142 e

   [img:Illustration] 

  O lugar das raízes do sistema com os compensadores (4.214) e (4.215) é apresentado nas Figuras 4.68 (a) e (b).

   [img:Illustration] 

  Figura 4.68 Lugar das raízes. (a) compensador (4.214) e (b) compensador (4.215).

  O sistema em malha fechada resultante é de ordem 3. Com o compensador (4.214) tem-se que

   [img:Illustration] 

  e com o compensador (4.215)

   [img:Illustration] 

  de modo que os polos complexos conjugados dessas duas funções satisfazem à especificação (4.207).

  As respostas ao degrau unitário do sistema em malha fechada com os compensadores (4.214) e (4.215) são apresentadas na Figura 4.69 (a) e (b), respectivamente. Sistemas de segunda ordem com coeficiente de amortecimento ξ = 0,5 e frequência natural ωn = 4 (rad/s) produzem resposta transitória com sobressinal Mp ≅ 16,3% e tempo de subida tr ≅ 0,6 s. Os resultados apresentados na Figura 4.69 são um pouco diferentes pelo fato de o sistema em malha fechada ser de terceira ordem. Daí a importância de verificar, por meio de simulações computacionais, se os resultados obtidos são satisfatórios. Caso contrário o projeto do compensador deve ser refeito.

   [img:Illustration] 

  Figura 4.69 Respostas ao degrau unitário. (a) compensador (4.214) e (b) compensador (4.215).

  

### Exercício 4.12

  Projete um compensador Gc(s) para o processo industrial com atraso puro da Figura 4.70 de modo que:

  • o erro estacionário seja de 0,02 quando é aplicado um degrau unitário na referência;

  • a resposta transitória dos sistemas em malha fechada com e sem compensador não tenha alteração significativa.

   [img:Illustration] 

  Figura 4.70 Sistema em malha fechada de um processo industrial.

  Solução

  Usando a aproximação de Padé de ordem (1,1) da Tabela 4.2, a função de transferência do processo resulta como

   [img:Illustration] 

  Supondo Gc(s) = 1, a função de transferência de malha fechada é

   [img:Illustration] 

  cujos polos de malha fechada estão localizados em s1,2 ≅ –1,50 ± 1,32j, com coeficiente de amortecimento ξ = 0,75 e frequência natural ωn = 2.

  Para obter um erro estacionário de 0,02 pode-se usar um compensador por atraso de fase com função de transferência

   [img:Illustration] 

  A função de transferência de malha aberta com o compensador Gc(s) é

   [img:Illustration] 

  Logo, o erro estacionário com compensador para um degrau unitário na referência vale

   [img:Illustration] 

  Para que a resposta transitória não tenha mudança significativa com o compensador Gc(s) a posição dos polos de malha fechada dominantes deve ser praticamente a mesma no lugar das raízes. Para isso, o ganho kc deve valer aproximadamente 1. Logo,

   [img:Illustration] 

  Escolhendo arbitrariamente o valor do polo pc = 0,001 próximo da origem, obtém-se zc = 0,147.

  Na Figura 4.71 é apresentado o lugar das raízes do sistema compensado. Traçando uma reta pelo coeficiente de amortecimento ξ ≅ 0,75 obtêm-se os polos de malha fechada dominantes do sistema compensado que estão em s1,2 = –1,45 ± 1,28j.

   [img:Illustration] 

  Figura 4.71 Lugar das raízes do sistema compensado.

  O ganho kc pode ser ajustado pela condição de módulo

   [img:Illustration] 

  Portanto, a função de transferência do compensador por atraso de fase é

   [img:Illustration] 

  A função de transferência de malha fechada resultante é

   [img:Illustration] 

  A Figura 4.72 mostra as respostas ao degrau unitário do sistema em malha fechada sem compensador (4.220) e com compensador (4.227). Observe que o transitório inicial das duas respostas é semelhante. Devido ao zero no semiplano direito do plano s, resultante da aproximação de Padé, a resposta se direciona nos instantes iniciais em sentido contrário ao seu valor estacionário.

  Note que o erro estacionário do sistema com compensador está de acordo com o especificado (e(∞) = 0,02) e é bem menor que o erro do sistema sem compensador (e(∞) = 1 – 0,25 = 0,75).

   [img:Illustration] 

  4.72 Respostas ao degrau unitário do sistema em malha fechada com e sem compensador.

  Como o compensador Gc(s) foi projetado a partir do modelo (4.219), com o atraso puro sendo aproximado por uma função de transferência racional, é importante verificar se a resposta transitória do sistema em malha fechada com atraso puro é satisfatória. Na Figura 4.73 é mostrada a resposta ao degrau unitário do sistema em malha fechada original da Figura 4.70 com o compensador (4.226).

   [img:Illustration] 

  Figura 4.73 Resposta ao degrau unitário do sistema em malha fechada original.

  Conforme se pode observar na Figura 4.73 não há compensador que consiga eliminar o efeito do atraso puro.

  

### 4.9 Exercícios propostos

  

### Exercício 4.13

  Considere o sistema da Figura 4.74.

   [img:Illustration] 

  Figura 4.74 Diagrama de blocos de um sistema em malha fechada.

  Desenhe o lugar das raízes e determine a faixa de valores do ganho k, que estabiliza o sistema em malha fechada para as seguintes funções de transferência:

   [img:Illustration] 

  

### Exercício 4.14

  Recentemente um novo sistema de transporte ferroviário tem sido objeto de pesquisa [4]. A principal característica desse sistema é que o trem é levitado, com forças de guiagem e propulsão geradas magneticamente. Devido à ausência de atrito de contato o veículo pode atingir altíssimas velocidades com muito mais segurança que os aviões. Diversas tecnologias têm sido desenvolvidas para conseguir levitar o trem, e algumas delas utilizam eletroímãs. Para levitar o trem é necessário controlar os entreferros desses eletroímãs. A função de transferência do sistema de levitação eletromagnética de um trem está representada no diagrama de blocos da Figura 4.75.

   [img:Illustration] 

  Figura 4.75 Diagrama de blocos do sistema em malha fechada.

  Deseja-se projetar um compensador Gc(s) de modo que a resposta da saída y(t), quando é aplicado um degrau unitário na referência r(t), apresente um sobressinal de 16,3% e um tempo de subida de 1 s.

  • Mostre que não é possível satisfazer às especificações se Gc(s) = k.

  • Determine a função de transferência do compensador Gc(s) de modo que os polos de malha fechada dominantes satisfaçam às especificações desejadas.

  

### Exercício 4.15

  Considere o sistema de controle da Figura 4.76.

   [img:Illustration] 

  4.76 Sistema de controle em malha fechada.

  O lugar das raízes de quatro sistemas está representado na Figura 4.77.

   [img:Illustration] 

  Figura 4.77 Lugar das raízes de quatro sistemas.

  Para cada um dos quatro sistemas, determine:

  a) a função de transferência da planta;

  b) quais sistemas possuem resposta transitória sempre amortecida;

  c) quais sistemas possuem resposta transitória com erro estacionário nulo quando é aplicado um degrau unitário na referência;

  d) a faixa de valores do controlador k para que o sistema em malha fechada seja estável;

  e) quais sistemas podem possuir resposta transitória com tempo de acomodação ts ≤ 2 s pelo critério de 2%.

  

### Exercício 4.16

  Projete um compensador Gc(s) por avanço de fase para o sistema da Figura 4.78 de modo que a resposta da saída y(t), quando é aplicado um degrau unitário na referência r(t), seja a mesma do gráfico da Figura 4.79.

   [img:Illustration] 

  Figura 4.78 Diagrama de blocos do sistema em malha fechada.

   [img:Illustration] 

  Figura 4.79 Resposta ao degrau unitário.

  

### Exercício 4.17

  Projete um compensador Gc(s) por atraso de fase para o sistema da Figura 4.80 de modo que a resposta para entrada do tipo rampa unitária na referência apresente erro estacionário de 0,1 sem que a resposta transitória tenha mudança significativa.

   [img:Illustration] 

  Figura 4.80 Diagrama de blocos do sistema em malha fechada.

  

### Exercício 4.18

  Projete um compensador Gc(s) por avanço e atraso de fase para o sistema da Figura 4.80 de modo que a resposta para entrada do tipo rampa unitária na referência apresente:

  • polos dominantes com coeficiente de amortecimento ξ = 0,5 e frequência ωn = 1 (rad/s);

  • erro estacionário de 0,1.

  

### Exercício 4.19

  Considere o motor CC com realimentação auxiliar da velocidade ω(t) da Figura 4.81.

   [img:Illustration] 

  Figura 4.81 Motor CC com realimentação auxiliar da velocidade ω(t).

  Desenhe o lugar das raízes e determine o valor do ganho Kt de modo que o sobressinal seja Mp = 10% quando é aplicado um degrau unitário na referência θr (t).

  Calcule também o tempo de subida tr, o tempo de pico tp e o tempo de acomodação (critérios de 2% e 5%) da resposta ao degrau.

  

### Exercício 4.20

  Projete um compensador por avanço e atraso de fase para o pêndulo invertido do Exercício 4.10. Para pequenas variações em torno do ponto de equilíbrio, deseja-se que:

  • a resposta tenha um tempo de subida tr = 0,5 s e coeficiente de amortecimento ξ = 0,7.

  • ocorra erro estacionário nulo quando é aplicado um degrau na referência.

  

### Exercício 4.21

  Considere um processo de fundição para a produção de barras de alumínio5 cuja função de transferência é

   [img:Illustration] 

  Utilizando aproximações de Padé de ordem (1,1) e (2,2), pede-se que

  • desenhe o lugar das raízes;

  • determine os pontos de cruzamento do lugar das raízes com o eixo imaginário e a faixa de valores do ganho k de modo que o sistema em malha fechada seja estável.

  

### Exercício 4.22

  Usando aproximação de Padé de ordem 1 para o processo de fundição do Exercício 4.21, projete um compensador por atraso de fase de modo que as seguintes especificações sejam satisfeitas:

  • o erro estacionário seja de 0,05 quando é aplicado um degrau unitário na referência;

  • as respostas transitórias dos sistemas em malha fechada com e sem compensador não tenham alteração significativa.

  

  __________

  1Ver referências [22] e [23].

  2O ganho k é considerado positivo, mas esta não é uma condição essencial no método do lugar das raízes.

  3Isso também ocorre quando um dos zeros está no infinito.

  4O cancelamento nunca deve ser realizado com polos instáveis, pois na prática este cancelamento pode não ser perfeito, fazendo com que o sistema tenha polos de malha fechada no semiplano direito, tornando-o instável.

  5Ver Exercício 9.3.

<!-- Text/chapter05.xhtml -->

  
  Controle Automático, 2ª edição
  
  

  

## 5

  

## Análise e Compensação no Domínio da Frequência

  

### 5.1 Introdução

  Desde a década de 1930 as respostas em frequência têm sido instrumentos consagrados para analisar e projetar sistemas técnicos de desempenho dinâmico, dispositivos elétricos, mecânicos, reguladores de processos industriais, servomecanismos, etc.

  A resposta em frequência de um sistema estável, linear e invariante no tempo consiste no conjunto das respostas do sistema, em regime permanente (após decorridos os transitórios), quando sinais senoidais de diversas frequências são aplicados na sua entrada. Suas representações gráficas têm grande poder de informação sobre a dinâmica dos sistemas em geral, permitindo identificar experimentalmente os seus modelos matemáticos e, no caso dos sistemas a realimentação, projetar com segurança os seus controladores.

  Considere o sistema linear e invariante no tempo da Figura 5.1 com função de transferência G(s). Sendo G(s) estável, sabe-se que para qualquer entrada u(t) de amplitude finita a saída y(t) também se mantém finita.

   [img:Illustration] 

  Figura 5.1 Sistema G(s) estável, linear e invariante no tempo.

  Suponha que G(s) está sujeito a um sinal senoidal de entrada u(t), de uma dada frequência ω e amplitude A, isto é,

   [img:Illustration] 

  cuja transformada de Laplace é

   [img:Illustration] 

  A transformada de Laplace da saída é dada por

   [img:Illustration] 

  Supondo, por simplicidade, que G(s) possui apenas um par de polos complexos conjugados e n polos reais distintos (–p1, –p2, . . ., –pn), então Y(s) pode ser expandida em frações parciais, ou seja,

   [img:Illustration] 

  sendo c1, c2, . . ., cn constantes e a* o complexo conjugado de a, que são calculados por

   [img:Illustration] 

  A transformada inversa de Laplace da Equação (5.4) é dada por

   [img:Illustration] 

  Sendo G(s) estável, todos os seus polos (–p1, –p2, . . ., –pn) têm parte real negativa. Com isso, as exponenciais correspondentes a estes polos tendem a zero quando t tende a infinito, restando apenas os dois primeiros termos da Equação (5.7), ou seja,

   [img:Illustration] 

  Sendo G(jω)| e ϕ(ω), o módulo e a fase de G(jω), respectivamente, então,

   [img:Illustration] 

  Da Equação (5.8) obtém-se

   [img:Illustration] 

  O resultado da Equação (5.11) permite concluir que:

  
    • a saída em regime permanente de um sistema estável, linear e invariante no tempo com entrada senoidal é também uma senoide com a mesma frequência da entrada;

    • a amplitude da senoide de saída vale: |Y(jω)|=|G(jω|.|U(jω)| = A|G(jω)| ;

    • a defasagem entre entrada e saída é dada por:  [img:Illustration] 

    • para obter a completa descrição dos efeitos da entrada senoidal no sistema G(s) basta substituir s por jω em G(s) e calcular o módulo e a fase do número complexo resultante.

  

  São estes resultados que justificam o nome de resposta em frequência para a função G(jω).

  

### Exemplo 5.1

  Determinar a saída y∞(t) em regime permanente do sistema linear e invariante no tempo da Figura 5.2, quando é aplicada a entrada u(t) = 2 sen(3t).

   [img:Illustration] 

  Figura 5.2 Sistema estável, linear e invariante no tempo.

  O sinal de entrada u(t) é uma senoide com frequência ω = 3 rad/s e amplitude A = 2. Logo, a saída y∞(t) em regime permanente também é uma senoide com a mesma frequência da entrada. Da Equação (5.11) obtém-se

   [img:Illustration] 

  Substituindo s por jω no sistema da Figura 5.2, obtém-se

   [img:Illustration] 

  Para ω = 3

   [img:Illustration] 

  A fase de G(j3) vale

   [img:Illustration] 

  Portanto, a saída y∞(t) em regime permanente é dada por

   [img:Illustration] 

  ■

  

### 5.2 Diagramas de Bode

  Os diagramas de Bode consistem em dois gráficos que, conjuntamente, representam a resposta em frequência:

  
    • módulo de G(jω) versus frequência ω, ambos em escala logarítmica;

    • fase de G(jω) versus frequência ω, esta última em escala logarítmica.

  

  O módulo de G(jω) pode ser também representado por 20 log G(jω)|, ou seja, empregando a unidade denominada decibel (dB). As vantagens em desenhar os gráficos em escalas logarítmicas são as seguintes:

  • permitem transformar produtos e divisões em somas e subtrações, respectivamente;

  • fornecem boas aproximações por meio de segmentos de reta, sendo suas intersecções facilmente associadas aos polos e zeros da função de transferência;

  • permitem abranger maiores faixas de valores das variáveis envolvidas, especialmente da frequência.

  A seguir são apresentados os gráficos de Bode de diversos termos que podem aparecer numa função de transferência.

  

#### 5.2.1 Ganho constante

  Neste caso particular a função de transferência é apenas um ganho k constante em qualquer frequência. O módulo de G(jω) em decibéis é dado por

   [img:Illustration] 

  A fase de G(jω) em graus é dada por

   [img:Illustration] 

  Na Figura 5.3 são apresentados os gráficos de Bode do ganho constante.

   [img:Illustration] 

  Figura 5.3 Gráficos de Bode do ganho constante.

  

#### 5.2.2 Polo na origem

  Quando a função de transferência possui um polo na origem, ou seja, G(s) = 1/s, o módulo de G(jω) em decibéis é dado por

   [img:Illustration] 

  Alguns valores do módulo de G(jω) em decibéis são apresentados na Tabela 5.1.

  Tabela 5.1 | G(jω) | (dB)

  
    
      
        

        
      

      
        
          
            w (rad/s)

          

          
            | G(jw) | (dB)

          
        

        
          
            0,1

            1

            10

            100

          

          
            20

            0

            –20

            –40

          
        

      
    
  

  Definindo x(ω) = log ω, a Equação (5.19) pode ser escrita na forma linear | G(jω) |= –20 x(ω). Este resultado mostra que o gráfico do G(jω)|, em escala logarítmica, é uma reta com inclinação de –20 dB/década, ou seja, na medida em que a frequência aumenta de 10 vezes o ganho diminui de 20 decibéis. Note que esta reta passa por 0 (dB) na frequência ω = 1 (rad/s).

  A fase de um polo na origem vale ∠G(jw) = –90o para qualquer frequência ω.

  Na Figura 5.4 são apresentados os gráficos de Bode de um polo na origem.

   [img:Illustration] 

  Figura 5.4 Gráficos de Bode de um polo na origem.

  

#### 5.2.3 Zero na origem

  Quando a função de transferência possuir um zero na origem, tem-se que

   [img:Illustration] 

  O gráfico do módulo de um zero na origem é uma reta com inclinação de +20 dB/década, que passa por 0 dB na frequência ω = 1 (rad/s). Já a fase vale ∠G(jω) = 90o para qualquer frequência ω.

  Na Figura 5.5 são apresentados os gráficos de Bode de um zero na origem.

   [img:Illustration] 

  Figura 5.5 Gráficos de Bode de um zero na origem.

  Note que os gráficos de Bode de um zero na origem são os mesmos do polo na origem com os sinais do módulo e da fase invertidos.

  

#### 5.2.4 Polo real fora da origem

  Considere a função de transferência com constante de tempo T de um sistema de primeira ordem

   [img:Illustration] 

  O módulo de G(jω) em decibéis é dado por

   [img:Illustration] 

  e a fase de G(jω) vale

   [img:Illustration] 

  Para ωT << 1, ou seja, em baixas frequências tem-se que

  | G(jω) |≅ –20 log |1| ≅ 0 (dB)   e   ∠G(jω) ≅ 0o.

  Para ωT >> 1, ou seja, em altas frequências tem-se que

  G(jω) |≅ –20 log |jωT| (dB)   e   ∠G(jω) ≅ –90o.

  Neste último caso o módulo representa uma reta com inclinação de –20 dB/década.

  Por fim, na frequência do polo, ou seja, para  [img:Illustration] , tem-se que

   [img:Illustration] 

  Na Tabela 5.2 estão resumidos estes resultados. Desse modo, dividindo o eixo das frequências em duas regiões (frequências menores e maiores que a frequência do polo em ω = 1/T) consegue-se desenhar os gráficos de Bode, conforme é apresentado na Figura 5.6.

  Tabela 5.2 Módulo e fase de G(jω)

   [img:Illustration] 

   [img:Illustration] 

  Figura 5.6 Gráficos de Bode de um polo real em  [img:Illustration] .

  Para  [img:Illustration]  tem-se que  [img:Illustration]  e para  [img:Illustration]  tem-se que  [img:Illustration] , o que resulta num erro de 6o quando se compara com as aproximações de fase da Tabela 5.2.

  Dado um registro experimental da resposta em frequência de um sistema de primeira ordem, a assíntota no gráfico do módulo é um segmento de reta cuja intersecção com o eixo de 0 dB permite localizar o polo real da função de transferência (5.21).

  

#### 5.2.5 Zero real fora da origem

  Considere o caso em que a função de transferência1 possui um termo do tipo (Ts + 1) em seu numerador, isto é, um zero em s = –1/T. Supondo G(jω) = jωT + 1, o módulo de G(jω) em decibéis é dado por

   [img:Illustration] 

  e a fase de G(jω) vale

   [img:Illustration] 

  Para desenhar os gráficos de Bode de um zero real fora da origem pode-se realizar análise semelhante ao caso anterior do polo real, ou seja, basta dividir os gráficos em duas regiões, considerando as baixas frequências em que ωT << 1 e as altas frequências em que ωT >> 1. Estes resultados estão resumidos na Tabela 5.3.

  Tabela 5.3 Módulo e fase de G(jω)

   [img:Illustration] 

  Os gráficos de Bode de um zero real em  [img:Illustration]  são apresentados na Figura 5.7. Note que estes gráficos são os mesmos do polo real, com a diferença de que os sinais do módulo e da fase devem ser invertidos.

   [img:Illustration] 

  Figura 5.7 Gráficos de Bode de um zero real em  [img:Illustration] .

  Conforme se pode verificar na Figura 5.7, para um gráfico de módulo obtido experimentalmente a intersecção da assíntota com o eixo de 0 dB permite localizar o zero real da função de transferência.

  

#### 5.2.6 Polos complexos conjugados

  Considere a função de transferência de um sistema de segunda ordem

   [img:Illustration] 

  Substituindo s por jω, o módulo de G(jω) em decibéis é dado por

   [img:Illustration] 

  Em baixas frequências, ou seja, para ω << ωn, tem-se que

   [img:Illustration] 

  Em altas frequências, ou seja, para ω >> ωn, tem-se que

   [img:Illustration] 

  isto é, em altas frequências o gráfico do módulo de G(jω) é uma reta com inclinação de –40 dB por década que cruza o eixo da frequência no ponto ω = ωn.

  Na frequência ω = ωn

   [img:Illustration] 

  Substituindo s por jω na Equação (5.26), a fase de G(jω) pode ser calculada por

   [img:Illustration] 

  Em baixas frequências, ou seja, para ω << ωn, tem-se que

   [img:Illustration] 

  Em altas frequências, ou seja, para ω >> ωn, tem-se que

   [img:Illustration] 

  e na frequência ω = ωn

   [img:Illustration] 

  Estes resultados estão resumidos na Tabela 5.4.

  Tabela 5.4 Módulo e fase de G(jω)

   [img:Illustration] 

  Na Figura 5.8 é apresentado o gráfico do módulo de G(jω) em dB para ξ = 1. Em altas frequências o gráfico do módulo é uma reta com inclinação de –40 dB/década. Note que para um gráfico de módulo obtido experimentalmente a intersecção da assíntota com o eixo de 0 dB permite identificar a frequência natural ωn do sistema.

   [img:Illustration] 

  Figura 5.8 Gráfico de G(jω)| (dB) para ξ = 1.

  Obviamente, o gráfico exato do G(jω)| depende do coeficiente de amortecimento ξ. Nas proximidades da frequência ωn pode existir um pico de ressonância, que é tanto maior quanto menor é o amortecimento ξ do sistema. Na Figura 5.9 são apresentados os gráficos de Bode de polos complexos conjugados. A frequência de ressonância ωr pode ser determinada calculando-se o ponto máximo da função

   [img:Illustration] 

  que ocorre em

   [img:Illustration] 

  O valor do ganho na frequência de ressonância ωr é dado por

   [img:Illustration] 

  Na Figura 5.10 é apresentado o gráfico do pico de ressonância Mr (dB) em função do coeficiente de amortecimento ξ. Na prática, normalmente as respostas transitórias aceitáveis têm coeficiente de amortecimento 0,4 ≤ ξ ≤ 0,7, que corresponde a um pico de ressonância 0 dB ≤ Mr ≤ 3 dB.

   [img:Illustration] 

  Figura 5.9 Gráficos de Bode de polos complexos conjugados.

   [img:Illustration] 

  Figura 5.10 Pico de ressonância Mr (dB) em função de ξ.

  

#### 5.2.7 Zeros complexos conjugados

  Neste caso a função de transferência2 deve possuir termos do tipo  [img:Illustration] 

  Supondo

   [img:Illustration] 

  o módulo de G(jω) em decibéis é dado por

   [img:Illustration] 

  e a fase de G(jω) vale

   [img:Illustration] 

  Para desenhar os gráficos de Bode pode-se realizar análise semelhante ao caso anterior dos polos complexos conjugados, ou seja, basta dividir os gráficos em duas regiões, considerando as baixas frequências em que ω << ωn e as altas frequências em que ω >> ωn. Estes resultados estão resumidos na Tabela 5.5. Note que os gráficos dos zeros complexos conjugados são os mesmos dos polos complexos conjugados, com a diferença de que os sinais do módulo e da fase devem ser invertidos.

  Tabela 5.5 Módulo e fase de G(jω)

   [img:Illustration] 

  Na Figura 5.11 são apresentados os gráficos de Bode de zeros complexos conjugados.

   [img:Illustration] 

  Figura 5.11 Gráficos de Bode de zeros complexos conjugados.

  

#### 5.2.8 Sistemas gerais

  Para construir os gráficos de Bode de um sistema contendo diversos fatores (polos e zeros), basta primeiramente desenhar os gráficos para cada fator e depois somar as ordenadas das curvas de cada fator para obter os gráficos do sistema completo. De fato, considere o sistema representado por

   [img:Illustration] 

  sendo k, ω, Ta e Tb números reais.

  Escrevendo G(jω) em coordenadas polares, obtém-se

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  Aplicando o logaritmo na Equação (5.43), obtém-se

   [img:Illustration] 

  Em decibéis, a Equação (5.44) resulta como

   [img:Illustration] 

  ou seja, para obter o gráfico do módulo de G(jω) em decibéis basta realizar a soma algébrica dos gráficos dos módulos de cada fator de G(jω).

  Da Equação (5.42) tem-se que a fase de G(jω) é a soma das fases de cada fator, ou seja,

   [img:Illustration] 

  

### Exemplo 5.2

  Deseja-se obter os gráficos de Bode do sistema com função de transferência

   [img:Illustration] 

  A função (5.47) também pode ser escrita como

   [img:Illustration] 

  Para obter os gráficos de Bode da função (5.48) basta desenhar os gráficos de cada fator separadamente (ganho constante k = 10, zero real em s = –1, polo na origem e polo real em s = –10) e depois somar as ordenadas de cada curva. Os gráficos de Bode da função (5.48) estão apresentados na Figura 5.12. Observe que devido à presença do integrador (polo na origem), o gráfico do módulo em baixas frequências é uma reta com inclinação de –20 dB/década.

  Gráficos aproximados da função (5.48) podem ser obtidos somando-se as aproximações assintóticas dos gráficos dos fatores. Esta aproximação é boa, exceto nas frequências correspondentes aos polos e zeros.

   [img:Illustration] 

  Figura 5.12 Gráficos de Bode da função (5.48).

  ■

  

### 5.3 Identificação experimental de funções de transferência

  Basicamente, a função de transferência que representa a dinâmica do funcionamento de um processo pode ser obtida de três maneiras:

  • escrevendo as equações diferenciais ou algébricas e medindo diretamente os parâmetros (massas, atritos, resistências, indutâncias, ganhos de amplificadores, etc.);

  • por meio da resposta ao degrau, para sistemas de dinâmica simples, medindo constante de tempo, valor estacionário, pico de ressonância, tempo de subida, instante de pico ou tempo de acomodação;

  • através da resposta em frequência e identificação gráfica de cada um dos fatores da função de transferência.

  

#### 5.3.1 Medida da resposta em frequência

  Aplicando um sinal senoidal na entrada de um sistema estável, linear e invariante no tempo, após o estabelecimento do regime permanente, o sinal de saída também será senoidal com a mesma frequência da entrada, conforme mostrado na Equação (5.11). Para a medida da resposta em frequência esta operação deve ser repetida em um número suficiente de frequências para caracterizar a resposta. Conforme mostrado na Figura 5.13, para cada frequência ω devem ser medidas:

  • as amplitudes das senoides de entrada |U(jω)| e de saída |Y(jω)|;

  • a defasagem ϕ(ω) entre entrada e saída.

  O módulo da função de transferência é dado por

   [img:Illustration] 

  e a fase por

   [img:Illustration] 

  Para medir a defasagem ϕ(ω) é necessário observar os sinais de entrada u(t) e saída y(t) simultaneamente, conforme exemplificado na Figura 5.13.

   [img:Illustration] 

  Figura 5.13 Observação simultânea dos sinais de entrada u(t) e saída y(t).

  O módulo e a fase de G(jω) também podem ser medidos através da figura de Lissajous. Conforme representado na Figura 5.14, o gráfico resultante é uma elipse formada pelos pontos (u(t), y(t)), ou seja, com u(t) no eixo das abcissas e y(t) no eixo das ordenadas.

   [img:Illustration] 

  Figura 5.14 Figura de Lissajous.

  Da Figura 5.14 tem-se que

   [img:Illustration] 

  e prova-se que

   [img:Illustration] 

  Após serem realizadas as medidas do módulo e da defasagem em um número suficiente de frequências, os pontos medidos devem ser colocados em gráficos de Bode, traçando-se segmentos de reta ou aproximações assintóticas que passem por estes pontos. Polos e zeros da função de transferência são localizados nas frequências em que ocorrem mudanças de inclinação dessas assíntotas.

  No caso do módulo as inclinações dos segmentos de reta devem ser números múltiplos de ±20 dB/década. Se, por exemplo, numa certa frequência ω a inclinação de um segmento de reta muda de –20 dB/década para –40 dB/década, isso significa que nesta frequência há um polo real, ou seja, um termo do tipo 1/(Ts + 1). Caso contrário, se nesta mesma frequência ω a inclinação do segmento de reta muda de –20 dB/década para uma reta paralela ao eixo da frequência, isso significa que há um zero real, ou seja, um termo do tipo (Ts + 1). Se, por outro lado, a inclinação do segmento de reta muda de –20 dB/década para –60 dB/década, com a existência de um pico de ressonância, isso significa que há um par de polos complexos conjugados, acrescentando um termo do tipo  [img:Illustration] ) na função de transferência.

  Se em baixas frequências, isto é, para ω → 0, o segmento de reta tem uma inclinação de –20L dB/década, isso significa que há L polos na origem (L = 1, 2, 3, . . .). Caso contrário, se a inclinação é de +20L dB/década, isso significa que há L zeros na origem. Caso o segmento de reta seja horizontal, então a função de transferência não possui polos e nem zeros na origem. Quanto ao ganho constante k da função de transferência, este pode ser medido diretamente a partir do valor do módulo em baixas frequências.

  Uma vez obtida a função de transferência a partir das aproximações assintóticas da curva de módulo, convém calcular as defasagens e comparar com as defasagens medidas. Este procedimento permite realizar uma verificação das aproximações adotadas, além de permiter ajustes nas frequências dos polos e zeros.

  

### Exemplo 5.3

  Desejando-se identificar a função de transferência G(s) de um processo estável, linear e invariante no tempo, aplicaram-se sinais senoidais com amplitude U(jω)| na sua entrada e mediram-se as correspondentes amplitudes Y(jω)| dos sinais de saída. Para cada frequência ω calculou-se |G(jω)| = |Y(jω)|/|U(jω)|, cujos pontos estão representados no gráfico da Figura 5.15. A seguir traçaram-se assíntotas (retas tracejadas) de modo a obter a frequência dos polos da função de transferência.

   [img:Illustration] 

  Figura 5.15 Gráfico de G(jω)| (dB).

  Analisando-se o gráfico da Figura 5.15 verifica-se que próximo da frequência ω ≅ 0,1 o módulo de G(jω) vale 20 dB. Com isso o ganho constante k da função de transferência vale

   [img:Illustration] 

  Entre as frequências ω = 0,1 e ω = 1 há uma assíntota horizontal paralela ao eixo da frequência. Com isso conclui-se que o sistema não possui polos ou zeros na origem. Esta assíntota horizontal muda de inclinação a partir da frequência ω = 1, passando a ter uma inclinação de –20 dB/década até a frequência ω = 10. Como essa mudança de inclinação ocorreu na frequência ω = 1, conclui-se que o sistema possui um polo real em s = –1, ou seja, a função de transferência possui um fator do tipo

   [img:Illustration] 

  Entre as frequências ω = 10 e ω = 100 há uma assíntota com inclinação de –60 dB/década, e nota-se também a presença de um pico de ressonância nas proximidades da frequência ωr ≅ 10. Com isso conclui-se que o sistema possui um par de polos complexos conjugados. Note que a assíntota com inclinação de –60 dB/década é o resultado da soma das assíntotas do polo real (–20 dB/década) com a assíntota dos polos complexos conjugados (–40 dB/década).

  Do gráfico (5.15) verifica-se que o pico de ressonância ocorre na frequência ωr ≅ 10 (rad/s) e o ganho vale Mr ≅ 8 dB. Da Equação (5.37) tem-se que

   [img:Illustration] 

  e da Equação (5.36) tem-se que

   [img:Illustration] 

  Assim, a função de transferência também possui um fator do tipo

   [img:Illustration] 

  De (5.53), (5.54) e (5.57) conclui-se que a função de transferência do processo é dada por

   [img:Illustration] 

  ■

  

### 5.4 Sistemas de fase mínima e de fase não mínima

  Os sistemas estáveis3 que têm função de transferência com todos os seus zeros no semiplano esquerdo do plano s são chamados de sistemas de fase mínima, e os que têm um ou mais zeros no semiplano direito são ditos de fase não mínima. Justificam-se tais denominações considerando os seguintes exemplos de sistemas estáveis:

   [img:Illustration] 

  e

   [img:Illustration] 

  sendo z > 0 e p > 0.

  Pela definição anterior, o sistema G1(s) é de fase mínima, pois o seu zero s = –z está localizado no semiplano esquerdo do plano s, enquanto G2(s) é de fase não mínima, pois o seu zero s = z está localizado no semiplano direito do plano s.

  Note que ambas as funções G1(jω) e G2(jω) possuem o mesmo módulo,

   [img:Illustration] 

  Porém, as fases de G1(jω) e G2(jω) são diferentes:

   [img:Illustration] 

  Das Equações (5.62) e (5.63) tem-se que em baixas frequências

   [img:Illustration] 

  mas em altas frequências

   [img:Illustration] 

  Portanto, duas funções de transferência idênticas em módulo podem ter diferenças significativas de fase. Na Figura 5.16 são apresentados os gráficos da fase de G1(jω) e G2(jω) para z = 10 e p = 1. Note que a fase de G1(jω) é menor que a de G2(jω). Tal efeito ocorre sempre que há zeros no semiplano direito do plano s. Por esta razão pode-se dizer que G1(s) é de fase mínima e G2(s) é de fase não mínima.

   [img:Illustration] 

  Figura 5.16 Gráficos da fase de G1(jω) e G2(jω).

  Aplicando um degrau unitário na entrada do sistema G2(s), a saída Y2(s) é dada por

   [img:Illustration] 

  No domínio do tempo tem-se que

   [img:Illustration] 

  Os valores inicial e final da saída y2(t) são

   [img:Illustration] 

  Na Figura 5.17 é apresentado o gráfico da resposta y2(t) para o caso de z = p = 1. Note que a saída do sistema no instante inicial possui sinal contrário ao do valor final, tornando a resposta transitória mais lenta.

   [img:Illustration] 

  Figura 5.17 Gráfico da resposta ao degrau unitário do sistema G2(s) para z = p = 1.

  Sistemas de fase não mínima estão presentes em diversos tipos de sistemas, tais como circuitos elétricos do tipo ponte, processos industriais, modelos macroeconômicos, etc. O seu controle por realimentação é, em geral, de projeto mais difícil.

  

### Exemplo 5.4

  Considere o circuito elétrico RC em ponte da Figura 5.18 com tensão de entrada E1(s) e tensão de saída E2(s).

   [img:Illustration] 

  Figura 5.18 Circuito elétrico RC em ponte.

  Analisando o circuito elétrico da Figura 5.18, tem-se que

   [img:Illustration] 

  Logo, a função de transferência é dada por

   [img:Illustration] 

  Como R > 0 e C > 0, o sistema da Figura 5.18 é um sistema de fase não mínima.

  ■

  

### 5.5 Sistemas com atraso puro ou atraso de transporte

  Conforme foi visto no Capítulo 3, num sistema com atraso puro ou atraso de transporte um sinal de entrada somente é percebido sem atenuação na saída depois de um certo tempo α > 0. Este tempo α também é chamado de retardo ou tempo morto.

  Nos sistemas com atraso puro, a entrada u(t) e a saída y(t) estão relacionadas por

   [img:Illustration] 

  cuja função de transferência é

   [img:Illustration] 

  Na Figura 5.19 são apresentados os gráficos de entrada e saída de um sistema com atraso puro.

   [img:Illustration] 

  Figura 5.19 Gráficos de entrada e saída de um sistema com atraso puro α.

  Substituindo s por jω na Equação (5.73), obtém-se

   [img:Illustration] 

  O módulo da resposta em frequência de G(jω) é

   [img:Illustration] 

  e a fase de G(jω) vale ∠G(jω) = –ωα.

  Portanto, um bloco de atraso puro não afeta o ganho, pois |G(jω)| = 1. Apenas a fase é afetada, pois cresce linearmente com a frequência ω. Veja a Figura 5.20.

   [img:Illustration] 

  Figura 5.20 Gráfico da fase de um atraso puro.

  A presença de um atraso por transporte num sistema de controle pode torná-lo muito mais difícil de controlar. Numa planta industrial raramente os retardos podem ser eliminados por completo.

  

### 5.6 Diagramas de Nyquist

  São diagramas polares que permitem representar as respostas em frequência (módulo e fase) num único gráfico. Considere, por exemplo, o sistema de primeira ordem

   [img:Illustration] 

  O módulo de G(jω) é dado por

   [img:Illustration] 

  e a fase de G(jω) por

   [img:Illustration] 

  Para desenhar o diagrama polar da função G(jω) basta calcular o módulo e a fase de G(jω) para frequências 0 ≤ ω < ∞. Na Tabela 5.6 são apresentados alguns valores do módulo e da fase de G(jω).

  Tabela 5.6 Módulo e fase da função G(jω) (5.76)

   [img:Illustration] 

  Prova-se que o diagrama de Nyquist da função G(jω) (5.76) é uma semicircunferência, conforme representado na Figura 5.21.

   [img:Illustration] 

  Figura 5.21 Diagrama de Nyquist da função G(jω) (5.76).

  Considere agora a função de transferência de um sistema de segunda ordem

   [img:Illustration] 

  O módulo de G(jω) é dado por

   [img:Illustration] 

  e a fase de G(jω) por

   [img:Illustration] 

  Na Tabela 5.7 são apresentados alguns valores do módulo e da fase de G(jω) para algumas frequências 0 ≤ ω < ∞.

  Tabela 5.7 Módulo e fase da função G(jω) (5.79)

  
    
      
        

        

        
      

      
        
          
            ω

          

          
            G(jω)|

          

          
            ∠G(jω)

          
        

        
          
            0

            ωn

            ∞

          

          
            1

            1/(2ξ)

            0

          

          
            0o

            –90o

            –180o

          
        

      
    
  

  Os diagramas de Nyquist da função G(jω) (5.79) para ξ = 0,5 e ξ = 1 são apresentados na Figura 5.22.

   [img:Illustration] 

  Figura 5.22 Diagrama de Nyquist da função G(jω) (5.79).

  

### 5.7 Estabilidade de sistemas com realimentação

  No Capítulo 3 foi estudada a estabilidade BIBO de sistemas lineares por meio da condição necessária e suficiente de que os seus polos estejam localizados no semiplano esquerdo aberto do plano s. Respostas em frequência de sistemas instáveis não têm significado físico, pois não são mensuráveis. Uma vez energizados estes sistemas, qualquer excitação ou ruído é suficiente para levar a saída a disparar até valores infinitos, seja com crescimento monotônico, seja com oscilação crescente. Mas tem sido de extrema importância para a tecnologia de sistemas de controle o fato de existir um conjunto de condições sobre a resposta em frequência de malha aberta, que garante a estabilidade do sistema quando a malha é fechada. Tais condições foram originalmente estabelecidas pelo teorema de Nyquist, que foi um dos mais bem-sucedidos resultados teóricos da engenharia de controle do Século XX.

  No Século XIX os motores a vapor eram vitais para a indústria, e os reguladores de velocidade, inventados por J. Watt em 1780, eram essenciais, mas à medida que se melhoravam os materiais e o acabamento dos componentes desses reguladores um sério problema se tornava frequente: os sistemas tendiam a oscilar, isto é, sua velocidade tendia a variar ciclicamente em torno do valor desejado. Engenheiros e físicos notáveis como Maxwell (1831-1879) e Vyschnegradsky estudaram a questão e esclareceram o seu aspecto teórico, via equações diferenciais. Mas, na prática, os reguladores eram projetados e aperfeiçoados por intuição, e as indústrias dependiam de alguns técnicos "milagrosos" que viajavam continuamente pela Europa "curando oscilações".

  Em 1915 a Bell System provou a viabilidade técnica da telefonia transcontinental por meio de um link entre Nova York e São Francisco, empregando meia tonelada de fio de cobre por milha de linha aérea e seis ampliadores-repetidores eletrônicos para tornar aceitáveis a atenuação e a distorção total. Reduzir o custo em cobre exigia ampliadores de ganho elevado e de complicadas respostas em frequência. H. Black propôs empregar realimentação e obteve sucesso em 1932, com imensas dificuldades para dominar as oscilações. No mesmo ano Nyquist publicou o seu Critério de Estabilidade, resultado da aplicação magistral da Transformada de Laplace e do Princípio do Argumento de Cauchy. Era a teoria certa para transformar prática e intuição em engenharia, pois ela permitia garantir estabilidade a partir de medidas nos componentes, e assim projetar com segurança os controladores.

  

#### 5.7.1 Princípio do argumento

  Considere uma função racional F(s) da variável complexa s dada por

   [img:Illustration] 

  sendo z1, z2, . . ., zn os zeros de F(s), p1, p2, . . ., pn os polos de F(s) e k o ganho.

  O Princípio do Argumento de Cauchy pode ser enunciado do seguinte modo.

  
    Suponha que um ponto do plano s percorra uma curva fechada γ neste plano, no sentido horário, e que o correspondente ponto F(s) percorra outra curva Γ, também fechada, no plano F(s). O número N de vezes que a curva Γ envolve a origem no plano F(s), no sentido horário, é igual ao número de zeros Nz menos o número de polos Np da função F(s), que estão internos à curva γ, ou seja,

     [img:Illustration] 

  

  Observações:

  • Supõe-se que a curva γ não contém polos e nem zeros de F(s);

  • O número N negativo representa envolvimentos no sentido anti-horário.

  Na Figura 5.23 são apresentados exemplos de aplicação do Princípio do Argumento. Na Figura 5.23 (a) a curva γ envolve o zero z1 (Nz = 1) e nenhum polo (Np = 0) no sentido horário. Logo, a curva Γ do plano F(s) deve envolver a origem uma vez no sentido horário, pois N = 1 – 0 = 1.

  Na Figura 5.23 (b) a curva γ envolve o zero z3 (Nz = 1) e o polo p3 (Np = 1) no sentido horário. Logo, a curva Γ do plano F(s) não deve envolver a origem nenhuma vez, pois N = 1 – 1 = 0.

  Na Figura 5.23 (c) a curva γ envolve os zeros z1, z2 e z3 (Nz = 3) e o polo p3 (Np = 1) no sentido horário. Logo, a curva Γ do plano F(s) deve envolver a origem duas vezes no sentido horário, pois N = 3 – 1 = 2.

  Na Figura 5.23 (d) a curva γ envolve o polo p3 (Np = 1) e nenhum zero (Nz = 0) no sentido horário. Logo, o número de envolvimentos da origem pela curva Γ no plano F(s) é N = 0 – 1 = –1. Como o sinal de N é negativo, a curva Γ deve envolver a origem uma vez em sentido contrário, isto é, no sentido anti-horário.

   [img:Illustration] 

  Figura 5.23 Exemplos de aplicação do princípio do argumento.

  

#### 5.7.2 Critério de estabilidade de Nyquist

  Considere o sistema em malha fechada da Figura 5.24.

   [img:Illustration] 

  Figura 5.24 Diagrama de blocos de um sistema em malha fechada.

  A função de transferência de malha fechada é dada por

   [img:Illustration] 

  Os polos de malha fechada são as raízes da equação característica

   [img:Illustration] 

  A função de transferência de malha aberta G(s)H(s) pode ser escrita como o quociente de dois polinômios, ou seja,

   [img:Illustration] 

  Assim, a Equação (5.85) pode ser escrita como

   [img:Illustration] 

  Denotando o semiplano direito do plano s por SPD, da Equação (5.87) definem-se:

  • Nz igual ao número de zeros de 1 + G(s)H(s) no SPD, que é o número de polos de malha fechada no SPD (raízes de D(s) + N(s) no SPD);

  • Np igual ao número de polos de 1 + G(s)H(s) no SPD, que é o número de polos de malha aberta no SPD (raízes de D(s) no SPD).

  Para que o sistema em malha fechada (5.84) seja BIBO estável é necessário que não tenha qualquer polo localizado no semiplano direito do plano s e também sobre o eixo imaginário. Esta condição pode ser verificada por meio do Princípio do Argumento. Suponha uma curva fechada γ, denominada contorno de Nyquist, constituída do eixo imaginário do plano s e de uma semicircunferência de raio r arbitrariamente grande, que envolva inteiramente o semiplano direito de s, conforme é mostrado na Figura 5.25.

   [img:Illustration] 

  Figura 5.25 Contorno de Nyquist.

  Seja Γ a curva representativa da imagem de 1+ G(s)H(s), calculada sobre a curva γ. Suponha que 1+ G(s)H(s) possua Np polos no semiplano direito de s e que Γ envolva a origem N vezes no sentido horário. Pelo Princípio do Argumento, o número de zeros Nz envolvido por γ é

   [img:Illustration] 

  
    Como Nz é o número de polos de malha fechada no semiplano direito do plano s, então o sistema (5.84) é estável se e somente se Nz = 0, ou seja,

     [img:Illustration] 

    que é o critério de estabilidade de Nyquist.

  

  Geralmente, desenha-se a curva de G(s)H(s) em vez de 1 + G(s)H(s). Nesse caso, o número de envolvimentos da origem do plano 1+ G(s)H(s) se transforma no número de envolvimentos do ponto –1 + j0 do plano G(s)H(s).

  Portanto, o critério de estabilidade de Nyquist pode ser enunciado assim:

  
    Um sistema em malha fechada é estável se e somente se o número de envolvimentos do ponto −1 + j0 pela curva G(s)H(s) no sentido anti-horário for igual ao número de polos de malha aberta com parte real positiva.

  

  Se G(s)H(s) não possuir polos no semiplano direito de s (Np = 0), então, para que o sistema em malha fechada seja estável, a curva de G(s)H(s) não deve envolver o ponto –1 + j0.

  Se o número de polos de malha aberta com parte real positiva Np for diferente de zero, então N é negativo. Com isso, o número de envolvimentos do ponto –1 + j0 deve ocorrer em sentido contrário, ou seja, no sentido anti-horário.

  O traçado do diagrama polar de Nyquist é a imagem do eixo s = jω do contorno de Nyquist da Figura 5.25 para –∞ < ω < ∞.

  

### Exemplo 5.5

  Considere um sistema com a função de transferência de malha aberta

   [img:Illustration] 

  cujos polos são s = –1 e s = –10.

  O módulo de G(jω)H(jω) é dado por

   [img:Illustration] 

  e a fase por

   [img:Illustration] 

  Na Tabela 5.8 são apresentados os valores do módulo e da fase de G(jω)H(jω) para algumas frequências 0 ≤ ω < ∞.

  Tabela 5.8 Módulo e fase da função (5.90)

  
    
      

      

      

      

      

      

      

      
    

    
      
        
          ω

        

        
          0

        

        
          0,5

        

        
          1,3

        

        
          3,2

        

        
          10

        

        
          100

        

        
          ∞

        
      

      
        
          G(jω)H(jω)|

        

        
          10

        

        
          8,93

        

        
          6,05

        

        
          2,84

        

        
          0,70

        

        
          0,01

        

        
          0

        
      

      
        
          ∠G(jω)H(jω)

        

        
          0o

        

        
          –29,43o

        

        
          –59,84o

        

        
          –90,39o

        

        
          –129,29o

        

        
          –173,72o

        

        
          –180o

        
      

    
  

  O contorno de Nyquist é apresentado na Figura 5.26, e o correspondente diagrama polar de Nyquist da função (5.90) para –∞ < ω < ∞ é apresentado na Figura 5.27. O traçado do diagrama polar da Figura 5.27 é a imagem do eixo jω do contorno de Nyquist. Já a semicircunferência de raio infinito no semiplano direito de s é mapeada na origem do diagrama polar de G(jω)H(jω).

   [img:Illustration] 

  Figura 5.26 Contorno de Nyquist.

   [img:Illustration] 

  Figura 5.27 Diagrama polar de Nyquist da função (5.90).

  O sistema em malha aberta (5.90) não possui polos no semiplano direito (Np = 0). Conforme é mostrado na Figura 5.27, o diagrama polar de Nyquist não envolve o ponto –1 + j0 (N = 0). Portanto, conclui-se que o sistema em malha fechada é estável.

  ■

  

### Exemplo 5.6

  Considere um sistema com a função de transferência de malha aberta

   [img:Illustration] 

  cujos polos são s = +2 e s = –10.

  O módulo de G(jω)H(jω) é dado por

   [img:Illustration] 

  e a fase por

   [img:Illustration] 

  Na Tabela 5.9 são apresentados os valores do módulo e da fase de G(jω)H(jω) para algumas frequências 0 ≤ ω < ∞.

  Tabela 5.9 Módulo e fase da função (5.93)

  
    
      

      

      

      

      

      
    

    
      
        
          ω

        

        
          0

        

        
          1,6

        

        
          3,2

        

        
          12,2

        

        
          ∞

        
      

      
        
          |G(jω)H(jω)|

        

        
          2

        

        
          1,5

        

        
          1,0

        

        
          0,2

        

        
          0

        
      

      
        
          ∠G(jω)H(jω)

        

        
          180o

        

        
          –150,4o

        

        
          –139,8o

        

        
          –150,0o

        

        
          180o

        
      

    
  

  O contorno de Nyquist é o mesmo da Figura 5.26. O diagrama polar de Nyquist da função (5.93) para –∞ < ω < ∞ é apresentado na Figura 5.28. O traçado do diagrama polar é a imagem do eixo jω do contorno de Nyquist. Já a semicircunferência de raio infinito, no semiplano direito de s do contorno de Nyquist, é mapeada num único ponto do diagrama polar, isto é, na origem.

   [img:Illustration] 

  Figura 5.28 Diagrama polar de Nyquist da função (5.93).

  O sistema em malha aberta (5.93) possui um polo no semiplano direito (Np = 1). Como o diagrama polar envolve o ponto –1+ j0 uma vez no sentido anti-horário (N = –1), então o sistema em malha fechada é estável.

  ■

  

### Exemplo 5.7

  Considere um servomecanismo com função de transferência de malha aberta

   [img:Illustration] 

  cujos polos são s = 0 e s = –1/T, com k > 0 e T > 0.

  O Princípio do Argumento pressupõe que o contorno de Nyquist γ não passe por polos de malha aberta. Caso a função de transferência G(s)H(s) tenha polos sobre o eixo imaginário é preciso fazer um artifício para que a curva γ desvie desses polos. Isto é possível por meio de semicircunferências de raio ρ arbitrariamente pequeno no semiplano direito de s.

  Como a função (5.96) possui um polo na origem, o contorno de Nyquist deve ter o aspecto da Figura 5.29 (a). Para desenhar o diagrama polar de Nyquist é preciso analisar o percurso de Nyquist em cada trecho do seu contorno.

   [img:Illustration] 

  Figura 5.29 (a) Contorno de Nyquist. (b) Diagrama polar.

  • trecho abc: representa a pequena semicircunferência de raio ρ em torno do polo na origem no contorno de Nyquist, ou seja,

   [img:Illustration] 

  O mapeamento de G(s)H(s) para ρ → 0 é

   [img:Illustration] 

  Portanto, para ρ → 0 o módulo de G(jω)H(jω) tende a infinito. Como a fase ϕ varia de –90o a +90o, a fase de G(jω)H(jω) varia de +90o a –90o no diagrama polar. O trecho abc correspondente no diagrama polar é mostrado na Figura 5.29 (b).

  • trecho cd: a frequência varia de ω = 0+ a ω = +∞. Substituindo s por jω na Equação (5.96) o módulo de G(jω)H(jω) é dado por

   [img:Illustration] 

  e a fase é dada por

   [img:Illustration] 

  Assim,

  para ω = 0+ ⇒|G(jω)H(jω)|→ ∞ e ∠G(jω)H(jω) = –90o e

  para ω → +∞ ⇒ |G(jω)H(jω)| = 0 e ∠G(jω)H(jω) = –180o.

  Portanto, o trecho cd do contorno de Nyquist é mapeado no trecho que vai do ponto c até a origem no diagrama polar.

  • trecho de: a frequência varia de ω = +∞ a ω = –∞. Neste caso, G(jω)H(jω)| = 0 e o mapeamento corresponde a um único ponto, que é a origem do diagrama polar.

  • trecho ea: a frequência varia de ω = –∞ a ω = 0–. Como G(s)H(s) é uma função racional, o gráfico polar é simétrico com relação ao eixo real. Portanto, o trecho ea do contorno de Nyquist é mapeado no trecho que vai da origem até o ponto a no diagrama polar.

  Logo, como o sistema em malha aberta (5.96) não possui polos no semiplano direito (Np = 0) e como o diagrama polar de Nyquist da Figura 5.29 (b) não envolve o ponto –1 + j0 (N = 0), conclui-se que o sistema em malha fechada é estável.

  ■

  

### Exemplo 5.8

  Considere um sistema de posicionamento com um elemento de integração como, por exemplo, um motor elétrico ou hidráulico que tem a função de transferência de malha aberta

   [img:Illustration] 

  cujos polos são s = 0, s = –1 (polo duplo). Como a função (5.101) tem um polo na origem, o contorno de Nyquist tem o formato da Figura 5.30.

   [img:Illustration] 

  Figura 5.30 Contorno de Nyquist.

  Para desenhar o diagrama polar de Nyquist é preciso analisar o percurso de Nyquist em cada trecho do seu contorno.

  • trecho abc: representa a pequena semicircunferência de raio ρ em torno do polo na origem no contorno de Nyquist, ou seja,

   [img:Illustration] 

  O mapeamento de G(s)H(s) para ρ → 0 é

   [img:Illustration] 

  Portanto, para ρ → 0 o módulo de G(jω)H(jω) tende a infinito. Como a fase ϕ varia de –90o a +90o, a fase de G(jω)H(jω) varia de +90o a –90o no diagrama polar. O trecho abc correspondente no diagrama polar é mostrado na Figura 5.31.

  • trecho cd: a frequência varia de ω = 0+ a ω = +∞. Substituindo s por jω na Equação (5.101), obtém-se

   [img:Illustration] 

  O módulo de G(jω)H(jω) é dado por

   [img:Illustration] 

   [img:Illustration] 

  Figura 5.31 Diagrama polar de Nyquist. (a) Estável k < 2. (b) Instável k > 2.

  e a fase é dada por

   [img:Illustration] 

  Assim,

  para ω = 0+ ⇒ |G(jω)H(jω)|→ ∞ e ∠G(jω)H(jω) = –90o e

  para ω → +∞ ⇒ |G(jω)H(jω)| = 0 e ∠G(jω)H(jω) = –270o.

  Portanto, o trecho cd do contorno de Nyquist é mapeado no trecho que vai do ponto c até a origem no diagrama polar. Para que a fase de G(jω)H(jω) seja –270o em ω → +∞, o diagrama polar deve cruzar o eixo real. No ponto de cruzamento a parte imaginária de G(jω)H(jω) é zero. Da Equação (5.104) verifica-se que isso ocorre para ω = 1. Com isso, o ponto de cruzamento com o eixo real ocorre em

   [img:Illustration] 

  Como o sistema em malha aberta (5.101) não possui polos no semiplano direito (Np = 0), para que o sistema em malha fechada seja estável N = –Np = 0, ou seja, o diagrama de Nyquist não deve envolver o ponto –1+ j0 (Figura 5.31 (a)). Isso ocorre desde que

   [img:Illustration] 

  Conforme a Figura 5.31 (b), para k > 2 o diagrama de Nyquist envolve duas vezes (N = 2) no sentido horário o ponto –1+ j0. Com isso, o sistema em malha fechada terá 2 polos no semiplano direito (Nz = 2) e será instável. Para k = 2, o diagrama cruza o eixo real exatamente no ponto –1 + j0, sendo também instável.

  • trecho de: a frequência varia de ω = +∞ a ω = –∞. Neste caso G(jω)H(jω)| = 0 e o mapeamento corresponde a um único ponto, que é a origem do diagrama polar.

  • trecho ea: a frequência varia de ω = –∞ a ω = 0–. Como o diagrama polar deve ser simétrico com relação ao eixo real, o trecho ea do contorno de Nyquist é mapeado no trecho que vai da origem até o ponto a no diagrama polar.

  ■

  

### 5.8 Margens de estabilidade

  As principais vantagens em estudar a estabilidade de um sistema a partir da sua resposta em frequência são:

  • pode ser aplicada tanto para a função de transferência calculada como para a resposta em frequência medida experimentalmente, que muitas vezes é mais fácil de ser obtida;

  • fornece uma indicação de margens de segurança nos sistemas estáveis em malha fechada, tais como variações máximas no ganho CC ou em quaisquer parâmetros, que o sistema tolera sem perder a estabilidade;

  • sugere modificações no sistema para evitar a instabilidade ou melhorar o desempenho;

  • generalidade, que permite analisar sistemas com funções de transferências com atrasos puros e sistemas com múltiplas malhas.

  Sinteticamente, as margens de estabilidade são medidas da distância do diagrama de Nyquist até o ponto –1 + j0. Essas medidas são a margem de ganho MG e a margem de fase MF.

  A margem de ganho MG indica quantas vezes o módulo da função de transferência de um sistema em malha aberta, na frequência ω em que a fase é –180o, deve ser aumentado ou diminuído para que o diagrama de Nyquist passe pelo ponto crítico –1 + j0, ou seja,

   [img:Illustration] 

  Na Figura 5.32 estão representadas partes dos diagramas polares de sistemas em malha aberta de fase mínima e que não têm polos no semiplano direito de s. Para esta classe de sistemas, apenas, pode-se concluir que para G(jω)H(jω)| < 1 (Figura 5.32 (a)) o sistema em malha fechada é estável, pois o diagrama polar não irá envolver o ponto −1 + j0. Porém, para |G(jω)H(jω)| > 1 (Figura 5.32 (b)) o sistema em malha fechada é instável, pois o diagrama polar irá envolver o ponto –1 + j0.

   [img:Illustration] 

  Figura 5.32 (a) Sistema em malha fechada estável. (b) Sistema em malha fechada instável.

  A margem de fase MF indica quanto a fase de um sistema em malha aberta, na frequência em que o módulo é igual a 1, deve ser variada para que o diagrama de Nyquist passe pelo ponto crítico –1 + j0, ou seja,

   [img:Illustration] 

  De acordo com a Figura 5.32 (a) o sistema em malha fechada é estável se MF > 0, e de acordo com a Figura 5.32 (b) é instável se MF ≤ 0.

  Para sistemas de malha aberta estáveis as margens de estabilidade também podem ser medidas nos diagramas de Bode, conforme é mostrado na Figura 5.33. Neste caso a margem de ganho é expressa em decibéis no gráfico do módulo.

   [img:Illustration] 

  Figura 5.33 (a) Sistema em malha fechada estável. (b) Sistema em malha fechada instável.

  Em decibéis a margem de ganho é dada por

   [img:Illustration] 

  na frequência ω em que ∠G(jω)H(jω) = –180o.

  Da Equação (5.111), se G(jω)H(jω)| < 1 então a margem de ganho em (dB) é positiva, e se G(jω)H(jω)| > 1 a margem de ganho em (dB) é negativa. De acordo com a Figura 5.33, um sistema é estável em malha fechada se as margens de ganho e fase forem positivas. Caso contrário o sistema em malha fechada é instável.

  Sistemas de primeira e segunda ordens possuem margem de ganho infinita, pois a fase nunca atinge –180o.

  Para sistemas de malha aberta instáveis recomenda-se que a análise de estabilidade seja realizada por meio de um diagrama polar de Nyquist completo, verificando-se o número de envolvimentos do ponto (–1 + j0), pois esta informação é difícil de ser extraída a partir dos diagramas de Bode.

  

### 5.9 Resposta em frequência da malha fechada

  Considere um sistema ideal em malha fechada com realimentação unitária (H(s) = 1), conforme representado na Figura 5.34.

   [img:Illustration] 

  Figura 5.34 Sistema em malha fechada com realimentação unitária.

  Supondo que G(s) é de fase mínima e não tem polos no semiplano direito de s, então parte do diagrama polar de Nyquist pode ser representado de acordo com a Figura 5.35.

   [img:Illustration] 

  Figura 5.35 Diagrama polar de G(jω).

  De acordo com a Figura 5.35, o vetor  [img:Illustration]  representa o número complexo G(jω) e  [img:Illustration]  é o vetor de 1 + G(jω) em cada frequência ω.

  São bastante úteis as seguintes expressões

   [img:Illustration] 

  De acordo com a Figura 5.35 e com as expressões (5.112) e (5.113), verifica-se que

  • quanto mais perto do ponto –1+j0 passar G(jω), maior será o pico da resposta de Y(jω)/R(jω);

  • quando ω → ∞⇒ G(jω) → 0. Logo, Y(jω)/R(jω) tende a 0;

  • quando ω → 0 ⇒ G(jω) → ∞. Logo, Y(jω)/R(jω) tende a 1;

  • o erro atuante na frequência ω é inversamente proporcional à distância do ponto –1 + j0 ao ponto da curva de G(jω).

  

#### 5.9.1 Carta de Nichols

  A resposta em frequência do sistema em malha fechada (5.112) também pode ser representada em termos de um módulo M(ω) e de uma fase α(ω), ambos em função da frequência ω, ou seja,

   [img:Illustration] 

  Considerando que

   [img:Illustration] 

  então, o módulo M(ω) da expressão (5.114) pode ser escrito como

   [img:Illustration] 

  ou

   [img:Illustration] 

  Rearranjando os termos da Equação (5.117), obtém-se

   [img:Illustration] 

  A expressão (5.118) representa a equação de uma circunferência com centro no ponto

   [img:Illustration] 

  e com raio

   [img:Illustration] 

  Fixando valores constantes para M(ω), diversas famílias de circunferências podem ser desenhadas no plano G(jω) = x + jy.

  Análise semelhante pode ser feita para a obtenção de famílias de curvas para α(ω) constante. Assim, da Equação (5.114) tem-se que

   [img:Illustration] 

  Aplicando a tangente nos dois membros da Equação (5.119), obtém-se

   [img:Illustration] 

  Rearranjando os termos da Equação (5.120), obtém-se

   [img:Illustration] 

  A expressão (5.121) representa a equação de uma circunferência com centro no ponto

   [img:Illustration] 

  e com raio

   [img:Illustration] 

  Fixando valores constantes para N(ω), diversas famílias de circunferências podem ser desenhadas no plano G(jω). Como os pontos (0, 0) e (–1, 0) são soluções da Equação (5.121), então todas as circunferências para N(ω) constante passam através da origem e do ponto –1 + j0.

  Nos projetos de realimentação é importante prever a resposta em frequência da malha fechada (5.114) a partir da resposta em frequência da malha aberta G(jω). Para isso, Nichols desenvolveu uma carta muito eficiente, em cujo eixo das abscissas é representada a fase de G(jω) e em cujo eixo das ordenadas é representado o módulo de G(jω). Nela foram desenhadas famílias de circunferências associadas a M(ω) constante e a α(ω) constante. Plotando a curva de G(jω) sobre essa carta é possível ler imediatamente nas intersecções com as curvas os valores do módulo M(ω) e da fase α(ω) da função de transferência de malha fechada. A carta de Nichols está apresentada na Figura 5.37 e serve para qualquer função de transferência de malha aberta.

  Considere agora o caso de realimentação não unitária da Figura 5.36 em que H(jω) = 1. Neste caso o cálculo da resposta em frequência de malha fechada Y(jω)/R(jω) pode ser feito por meio dos seguintes passos:

  i) desenhar os gráficos de Bode de G(jω)H(jω);

  ii) transportar a informação do item a) para a carta de Nichols e obter Y(jω)/R(jω);

  iii) construir os gráficos de Bode de Y(jω)/R(jω);

  iv) somar ao resultado do item c) às curvas de Bode de 1/H(jω).

   [img:Illustration] 

  Figura 5.36 (a) Diagrama de blocos de um sistema com realimentação não unitária. (b) Diagrama de blocos equivalente.

   [img:Illustration] 

  Figura 5.37 Carta de Nichols.

  

### Exemplo 5.9

  Foi realizada experimentalmente a resposta em frequência de um sistema em malha aberta. Para cada frequência ω foram medidos o módulo e a fase de G(jω), que estão apresentados na Tabela 5.10.

  Tabela 5.10 Resposta em frequência de um sistema em malha aberta G(jω)

  
    
      

      

      

      

      

      

      

      

      

      

      
    

    
      
        
          ω

        

        
          0,13

        

        
          0,18

        

        
          0,25

        

        
          0,42

        

        
          0,6

        

        
          0,78

        

        
          1

        

        
          1,35

        

        
          1,87

        

        
          4,2

        
      

      
        
          |G(jω)| (dB)

        

        
          15,3

        

        
          12,3

        

        
          9,3

        

        
          3,8

        

        
          –0,5

        

        
          –4,3

        

        
          –8,4

        

        
          –13,9

        

        
          –20,7

        

        
          –40

        
      

      
        
          ∠G(jω) (graus)

        

        
          –105

        

        
          –110

        

        
          –118

        

        
          –135

        

        
          –152

        

        
          –166

        

        
          –180

        

        
          –197

        

        
          –214

        

        
          –243

        
      

    
  

  Deseja-se obter a resposta em frequência do sistema em malha fechada com realimentação unitária determinando os valores da margem de ganho MG, da margem de fase MF, do pico de ressonância Mr e de sua frequência ωr.

  Alocando os pontos da Tabela 5.10 na carta de Nichols, pode-se ler diretamente da carta a resposta em frequência do sistema em malha fechada cujos pontos são apresentados na Tabela 5.11.

   [img:Illustration] 

  Figura 5.38 Carta de Nichols para os dados da Tabela 5.10.

  Tabela 5.11 Resposta em frequência do sistema em malha fechada  [img:Illustration] 

   [img:Illustration] 

  Os gráficos de Bode do sistema em malha fechada, construídos a partir da Tabela 5.11, estão apresentados na Figura 5.39.

   [img:Illustration] 

  Figura 5.39 Resposta em frequência do sistema em malha fechada.

  A margem de ganho MG corresponde a menos o ganho de malha aberta em (dB) na frequência em que a fase de malha aberta vale –180o. Já a margem de fase MF corresponde a 180o mais a fase de malha aberta na frequência em que o módulo de malha aberta vale 0 dB. Os valores aproximados são MG ≅ 8,4 e MF ≅ 30o.

  O pico de ressonância Mr corresponde ao maior ganho da resposta em frequência do sistema em malha fechada. Da Figura 5.39 tem-se que Mr ≅ 6 dB e ocorre na frequência ωr ≅ 0,6 rad/s. Na carta de Nichols o pico de ressonância corresponde ao ponto em que a curva de malha fechada é tangente à curva de ganho máximo da carta.

  ■

  

### 5.10 Banda passante e frequência de corte

  A banda passante, ou faixa de passagem, é a faixa de frequências na qual um sistema G(jω) é capaz de responder substancialmente à excitação dos sinais de entrada. Esta faixa é limitada pela frequência de corte ωc do sistema.

  A frequência de corte ωc é definida como aquela em que o ganho cai a  [img:Illustration]  (71%) do ganho em baixas frequências, que corresponde à transmissão de 50% da potência. Em decibéis este valor corresponde a –3 dB. A frequência de corte fornece uma fronteira adequada para a supressão de ruídos de altas frequências por meio de filtros. Tais ruídos estão presentes na maioria dos atuadores e instrumentos de medição dos processos.

  A banda passante e a frequência de corte estão indicadas na Figura 5.40.

   [img:Illustration] 

  Figura 5.40 Banda passante e frequência de corte.

  

### Exemplo 5.10

  Considere dois sistemas de primeira ordem com função de transferência

   [img:Illustration] 

  As respostas em frequência destes dois sistemas estão apresentadas na Figura 5.41 (a). Note que o sistema G1(s) tem uma banda passante maior (ωc = 1), pois o seu polo está localizado em s = –1, enquanto o sistema G2(s) tem uma banda passante menor (ωc = 0,5), pois o seu polo está localizado em s = –0,5. Com isso, a resposta ao degrau unitário do sistema G1(s) é mais rápida que a do sistema G2(s). Isso é o que pode ser verificado na Figura 5.41 (b) por meio das saídas y1(t) e y2(t) dos sistemas G1(s) e G2(s), respectivamente.

   [img:Illustration] 

  Figura 5.41 (a) Resposta em frequência. (b) Resposta ao degrau unitário.

  ■

  

### 5.11 Compensação por meio da resposta em frequência

  Um dos famosos teoremas de Bode prova que em cada frequência a fase de um sistema linear qualquer de fase mínima é calculada por meio de uma integral da derivada da função módulo sobre todas as frequências. Mas há também no integrando uma função ponderadora que dá peso dominante à derivada nas décadas frequenciais em torno da frequência em que se calcula a fase.

  Assim, se a derivada se conserva perto de –20 dB/década, em torno da frequência em que o ganho é 0 dB, a fase resulta perto de –90o. Como essa defasagem garante margem de fase positiva e, portanto, a estabilidade do sistema em malha fechada, resulta uma orientação simples e eficaz de como projetar um sistema estável. Para isso, basta introduzir elementos dinâmicos na malha aberta de modo que a curva de Bode do módulo caia à taxa de aproximadamente –20 dB/década.

  Devido ao objetivo de "equalizar" a declividade da curva de ganho em –20 dB/década, aqueles elementos dinâmicos introduzidos consistem em um equalizador. A compensação por meio de diagramas de Bode também pode ser chamada de "equalização".

  Se a inclinação da curva de módulo nas proximidades da frequência de cruzamento da linha de 0 dB for de –60 dB/década, então o sistema em malha fechada é instável pois a fase do sistema nas proximidades dessa frequência vai necessariamente ser bem menor que –180o. Se a curva de módulo tiver uma inclinação de –40 dB/década, então o sistema em malha fechada pode ser estável ou instável com pequenas margens de estabilidade.

  A compensação por meio da resposta em frequência é indicada quando as especificações de resposta do sistema são fornecidas em termos das margens de estabilidade (ganho e fase) e do erro no estado estacionário, com a vantagem de que a restrição de erro estacionário é mais fácil de ser implementada no domínio da frequência do que por meio da técnica do lugar das raízes.

  

#### 5.11.1 Compensação por avanço de fase

  A compensação por avanço de fase (phase lead) por meio da resposta em frequência visa aumentar a margem de fase, reduzindo por conseguinte o sobressinal da resposta transitória. Além disso, a compensação aumenta a banda passante, tornando a resposta transitória mais rápida. O bloco típico de um compensador por avanço de fase tem a função de transferência

   [img:Illustration] 

  O diagrama de polos e zeros de um compensador por avanço de fase é apresentado na Figura 5.42. O zero do compensador –1/T deve estar localizado mais próximo do eixo imaginário, quando comparado ao polo –1/(aT).

   [img:Illustration] 

  Figura 5.42 Diagrama de polos e zeros de um compensador por avanço de fase.

  Os diagramas de Bode do compensador (5.122) estão apresentados na Figura 5.43. Note que o compensador possui fase positiva em todas as frequências. Daí a designação de avanço de fase. Com este compensador a fase sofre um acréscimo significativo apenas nas proximidades da frequência ωm. Já o ganho é menor em baixas frequências e maior em altas frequências.

   [img:Illustration] 

  Figura 5.43 Diagramas de Bode do compensador por avanço de fase Gc(s).

  Da Equação (5.122), tem-se que a fase ϕ de Gc(jω) é dada por

   [img:Illustration] 

  Derivando a Equação (5.123) com relação a ω e igualando a zero pode-se encontrar a frequência ωm onde ocorre a máxima fase ϕm de Gc(jω), ou seja,

   [img:Illustration] 

  Na frequência ωm tem-se que

   [img:Illustration] 

  Assim, o módulo de Gc(jωm) é dado por

   [img:Illustration] 

  e a fase por

   [img:Illustration] 

  ou

   [img:Illustration] 

  

### Exemplo 5.11

  Considere a função de transferência de um motor de corrente contínua cuja função de transferência é dada por

   [img:Illustration] 

  sendo Θ(s) e Ea(s) as transformadas de Laplace da posição angular do eixo e da tensão de armadura, respectivamente.

  Os gráficos de Bode do sistema (5.129) são apresentados na Figura 5.44. A margem de fase é medida na frequência ω ≅ 2,1 (rad/s) em que o ganho vale 0 (dB) e vale MF ≅ 25,2o. Já a margem de ganho é infinita, pois a curva de fase nunca atinge 180o.

   [img:Illustration] 

  Figura 5.44 Gráficos de Bode do sistema G(s).

  O sistema em malha fechada com realimentação unitária é apresentado na Figura 5.45.

   [img:Illustration] 

  Figura 5.45 Diagrama de blocos do sistema em malha fechada sem compensador.

  Aplicando-se uma rampa unitária na referência (θr(t) = t) o erro no estado estacionário e(∞) vale

   [img:Illustration] 

  Para melhorar a resposta do sistema deseja-se projetar um compensador Gc(s), conforme representado na Figura (5.46), de modo que as seguintes especificações sejam satisfeitas:

  • erro estacionário e(∞) = 0,02 para entrada de referência do tipo rampa unitária;

  • margem de fase MF ≅ 50o.

   [img:Illustration] 

  Figura 5.46 Diagrama de blocos do sistema em malha fechada com compensador.

  A função de transferência de malha aberta Gma(s) com compensador é dada por

   [img:Illustration] 

  A constante k do compensador Gc(s) pode ser obtida a partir da especificação do erro estacionário, ou seja,

   [img:Illustration] 

  Logo k = 10 ou, em decibéis, k = 20 log 10 = 20 dB.

  Os gráficos de Bode de kG(jω) são apresentados na Figura 5.47. Note que com o ganho k do compensador o gráfico do módulo desloca-se na direção vertical de k = 20 dB. Logo, o ponto de cruzamento da curva de módulo em 0 dB (ganho 1) desloca-se para a direita, ocorrendo numa frequência mais alta em w ≅ 7 (rad/s). Com isso, a margem de fase é reduzida para MF ≅ 8o.

   [img:Illustration] 

  Figura 5.47 Gráficos de Bode de k G(jω).

  A margem de fase é determinada pela frequência de cruzamento em que o ganho do sistema em malha aberta vale 1 ou 0 dB. Assim, para que a margem de fase seja de 50o o compensador deve fornecer uma fase de pelo menos 50o – 8o = 42o. Porém, conforme se pode perceber no gráfico do módulo de Gc(jω) da Figura 5.43, o ganho do compensador cresce a partir da frequência 1/T, fazendo com que a frequência de cruzamento de ganho 1 do sistema em malha aberta seja deslocada para a direita. Logo, o avanço de fase máximo ϕm a ser fornecido pelo compensador deve ser na realidade um pouco maior que 42o. Adotando uma parcela de correção4 de 3o a mais, então ϕm ≅ 50o – 8o + 3o ≅ 45o.

  Da Equação (5.128) obtém-se o valor de a, ou seja,

   [img:Illustration] 

  e da Equação (5.126) obtém-se

   [img:Illustration] 

  Na frequência ωm o ganho de malha aberta deve ser igual a 1 ou 0 dB, ou seja,

   [img:Illustration] 

  Logo, o módulo do sistema não compensado deve valer, na frequência ωm,

   [img:Illustration] 

  Da Equação (5.124) obtém-se o valor de T, ou seja,

   [img:Illustration] 

  Portanto, a função de transferência do compensador que satisfaz às especificações é dada por

   [img:Illustration] 

  Os gráficos de Bode do sistema em malha aberta compensado Gma(jω) = Gc(jω)G(jω), mostrando a margem de fase MF ≅ 50o, são apresentados na Figura 5.48.

  Na Figura 5.49 são apresentados os gráficos das respostas transitórias dos sistemas em malha fechada compensado e não compensado para uma entrada de referência do tipo rampa unitária (θr(t) = t ⇒ Θr(s) = 1/s2). Note a redução do erro no estado estacionário.

  Como a frequência de ganho 1 ou 0 dB do sistema em malha aberta aumentou de 2,1 para 10,9 (rad/s), a resposta transitória do sistema compensado ficou mais rápida. Isso também pode ser verificado por meio de uma comparação das respostas em frequência dos sistemas em malha fechada compensado e não compensado da Figura 5.50. Note que a banda passante do sistema compensado é maior que a do não compensado. Além disso, o aumento da margem de fase para 50o possibilitou uma redução significativa do pico de ressonância.

   [img:Illustration] 

  Figura 5.48 Gráficos de Bode de G(jω), Gc(jω) e Gma(jω).

   [img:Illustration] 

  Figura 5.49 Saídas compensada e não compensada dos sistemas em malha fechada para entrada do tipo rampa unitária.

   [img:Illustration] 

  Figura 5.50 Respostas em frequência dos sistemas em malha fechada compensado e não compensado.

  ■

  

#### 5.11.2 Compensação por atraso de fase

  O bloco típico de um compensador por atraso de fase (lag phase) tem a função de transferência

   [img:Illustration] 

  O diagrama de polos e zeros de um compensador por atraso de fase é apresentado na Figura 5.51. O polo do compensador –1/(aT) deve estar localizado mais próximo do eixo imaginário, quando comparado ao zero –1/T.

   [img:Illustration] 

  Figura 5.51 Diagrama de polos e zeros de um compensador por atraso de fase.

  Os diagramas de Bode do compensador (5.139) estão apresentados na Figura 5.52. Note que o compensador possui fase negativa em todas as frequências, daí a designação de atraso de fase. Apesar do título atraso de fase, a utilidade desse compensador não está relacionada à fase, mas sim ao ajuste de ganho que possibilita. Como o ganho é maior em baixas frequências e menor em altas, o compensador pode ser empregado para reduzir o ganho em altas frequências para melhorar a margem de fase e a consequente resposta transitória, ou, inversamente, manter a margem de fase e aumentar o ganho em baixas frequências para reduzir o erro estacionário.

  A dificuldade do método consiste em que na região onde o ganho do compensador decresce ele introduz defasagem negativa, isto é, instabilizante. Por isso essa região deve ser colocada bem abaixo da região crítica, onde o ganho vale 1. Já a redução do ganho em altas frequências diminui a banda passante, prejudicando a rapidez com que o sistema reproduz o sinal de referência.

   [img:Illustration] 

  Figura 5.52 Diagramas de Bode do compensador por atraso de fase Gc(jω).

  

### Exemplo 5.12

  Considere um sistema com a seguinte função de transferência de malha aberta:

   [img:Illustration] 

  Os diagramas de Bode do sistema (5.140) são apresentados na Figura 5.54. A partir destes gráficos obtêm-se as seguintes margens de estabilidade: MG ≅ 16 dB e MF ≅ 51o. Portanto, este sistema em malha fechada é estável. O diagrama de blocos do sistema em malha fechada sem compensador é apresentado na Figura 5.53.

   [img:Illustration] 

  Figura 5.53 Diagrama de blocos do sistema em malha fechada sem compensador.

  Aplicando-se um degrau unitário na referência, o erro estacionário es(∞) sem compensador é

   [img:Illustration] 

   [img:Illustration] 

  Figura 5.54 Diagramas de Bode da função G(jω) (5.140).

  Deseja-se projetar um compensador Gc(s) por atraso de fase de modo a reduzir o erro estacionário em 10 vezes, mantendo o valor da margem de fase. A função de transferência de malha aberta com o compensador Gc(s) é dada por

   [img:Illustration] 

  O erro estacionário ec(∞) com compensador vale

   [img:Illustration] 

  Na Figura 5.55 são apresentados os gráficos de Bode de kG(jω). Como o compensador possui fase negativa, quando este for incluído na malha ocorrerá uma redução na margem de fase. Prevendo esse efeito é necessário ajustar a margem de fase num valor maior que o desejado para realizar o cálculo do compensador.5 Por essa razão, neste exemplo a margem de fase é ajustada para 55o.

  Em seguida deve-se encontrar a frequência que determina a margem de fase MF ≅ 55o ajustada. No gráfico de fase da Figura 5.55 verifica-se que a fase da curva de kG(jω), que vale –180o + 55o = –125o, ocorre na frequência ω ≅ 1,6 (rad/s). Nesta frequência o módulo de kG(jω) vale aproximadamente +23 dB. Portanto, o compensador deve fornecer uma redução de ganho de –23 dB, ou seja,

   [img:Illustration] 

   [img:Illustration] 

  Figura 5.55 Diagramas de Bode da função kG(jω).

  Em altas frequências tem-se que

   [img:Illustration] 

  Para não reduzir a margem de fase, o zero do compensador deve ser escolhido abaixo da frequência crítica ω ≅ 1,6 (rad/s). Escolhendo o zero uma década abaixo desta frequência, obtémse s = –1/T = –0,16 ⇒ T = 6,25.

  Logo, a função de transferência do compensador resulta como

   [img:Illustration] 

  Na Figura 5.56 são apresentados os diagramas de Bode do sistema não compensado G(jω), do sistema compensado Gc(jω)G(jω) e do compensador Gc(jω). Note que em baixas frequências o ganho do sistema compensado é maior que o do sistema não compensado, possibilitando assim reduzir o erro estacionário. Na frequência de ganho 1 ou 0 dB a margem de fase resultante do sistema compensado é a mesma do sistema não compensado (MF ≅ 51o), permitindo, dessa forma, obter respostas transitórias semelhantes.

  Na Figura 5.57 são apresentadas as respostas ao degrau unitário dos sistemas compensado e não compensado. Note que as respostas transitórias têm sobressinal semelhante, porém o erro estácionário da resposta do sistema compensado é bem menor.

   [img:Illustration] 

  Figura 5.56 Diagramas de Bode do sistema não compensado G(jω), do sistema compensado Gc(jω)G(jω) e do compensador Gc(jω).

   [img:Illustration] 

  Figura 5.57 Respostas ao degrau unitário dos sistemas compensado e não compensado.

  

#### 5.11.3 Compensação por avanço e atraso de fase

  A compensação por avanço e atraso de fase (lead-lag phase) aplica os dois recursos analisados anteriormente. Esta compensação é indicada quando é necessário melhorar simultaneamente as margens de estabilidade e o erro no estado estacionário.

  Em vez de usar funções de transferências individuais com amplificadores individuais para o avanço e para o atraso, pode-se usar uma função de transferência única com apenas um amplificador k. A função de transferência do compensador por avanço e atraso de fase é dada por

   [img:Illustration] 

  A função de transferência responsável pelo avanço de fase na Equação 5.147 é

   [img:Illustration] 

  e a função de transferência responsável pelo atraso de fase é

   [img:Illustration] 

  Na Figura 5.58 são apresentados os diagramas de Bode do compensador por avanço e atraso de fase Gc(jω).

   [img:Illustration] 

  Figura 5.58 Diagramas de Bode do compensador por avanço e atraso de fase Gc(jω).

  Para projetar um compensador por avanço e atraso de fase primeiramente calcula-se o ganho do amplificador k, que fornece o erro estacionário desejado. Em seguida projeta-se o compensador por atraso de fase Gat(s) para reduzir o ganho em altas frequências e, com isso, atenuar ruídos presentes na maioria dos atuadores e instrumentos de medição. Por fim, projeta-se o compensador por avanço de fase Gav(s) para satisfazer à especificação da margem de fase.

  

### Exemplo 5.13

  Projete um compensador por avanço e atraso de fase para o sistema da Figura 5.59, tal que:

  • a resposta para entrada do tipo degrau na referência apresente erro estacionário de 0,02;

  • a margem de fase seja de 50o.

   [img:Illustration] 

  Figura 5.59 Diagrama de blocos de um sistema em malha fechada sem compensador.

  A função de transferência de malha aberta com o compensador por avanço e atraso de fase é dada por

   [img:Illustration] 

  sendo G(s) a função de transferência da planta.

  O erro estacionário e(∞) para entrada do tipo degrau na referência vale

   [img:Illustration] 

  Os diagramas de Bode de kG(jω) são apresentados na Figura 5.60. As margens de estabilidade mostradas nesses gráficos são MF ≅ –15o e MG ≅ –6 dB. Logo, apenas com o ajuste do ganho k o sistema em malha fechada é instável.

   [img:Illustration] 

  Figura 5.60 Gráficos de Bode de kG(jω).

  Para obter uma margem de fase de 50o é necessário o projeto de um compensador por avanço e atraso de fase. O compensador por avanço Gav(s) melhora a margem de fase, mas aumenta o ganho em altas frequências que, por sua vez, é reduzido com o compensador por atraso Gat(s).

  A margem de fase é medida na frequência de corte ωc em que o ganho vale 1 ou 0 dB. O próximo passo é escolher esta frequência, de modo que o sistema com o compensador Gc(s) tenha uma margem de fase MF = 50o. Assim,

   [img:Illustration] 

  Supõe-se que a margem de fase de 50o seja completamente fornecida pelo compensador por avanço, isto é, ∠Gav(jωc) = 50o, e que o atraso de fase do compensador Gat(s), na frequência de corte, seja aproximadamente6 ∠Gat(jωc) ≅ –5o. Então, a frequência de corte escolhida irá ocorrer onde a fase da planta é ∠G(jωc) = –175o. Da Figura 5.61 obtém-se que a frequência de corte vale ωc ≅ 4,1 (rad/s).

   [img:Illustration] 

  Figura 5.61 Fase de G(jω) em função da frequência.

  O compensador por atraso de fase Gat(s) deve ser projetado de modo a não afetar a margem de fase. Assim, a frequência de corte superior de Gat(s) é escolhida uma década abaixo da frequência de corte ωc, onde é medida a margem de fase, ou seja, 1/T2 = 0,41 (rad/s).

  O valor de α é calculado a partir do ângulo de fase ϕm = MF = 50o a ser fornecido pelo compensador por avanço Gav(s). Da Equação (5.128) tem-se que

   [img:Illustration] 

  Como a = 1/α, então,

   [img:Illustration] 

  Logo, a função de transferência do compensador por atraso de fase é

   [img:Illustration] 

  A fase máxima ϕm do compensador por avanço de fase Gav(s) deve ocorrer na frequência de corte ωc. Da Equação (5.124) tem-se que

   [img:Illustration] 

  Logo, a função de transferência do compensador por avanço de fase é

   [img:Illustration] 

  Na Figura 5.62 é apresentado o gráfico da fase de Gav(jω), mostrando ϕm = 50o.

   [img:Illustration] 

  Figura 5.62 Fase de G(jω) em função da frequência.

  A função de transferência do compensador por avanço e atraso de fase é dada por

   [img:Illustration] 

  Na Figura 5.63 são apresentados os diagramas de Bode da planta G(jω), do compensador por avanço e atraso de fase Gc(jω) e da função de transferência de malha aberta Gma(jω). A margem de fase é dada por

   [img:Illustration] 

  sendo ∠Gc(jωc) = ∠Gat(jωc)+ ∠Gav(jωc) = –5o + 50o = 45o.

  A função de transferência do sistema em malha fechada com compensador é dada por

   [img:Illustration] 

  que é um sistema de quinta ordem.

  Na Figura 5.64 são apresentadas as respostas ao degrau unitário dos sistemas em malha fechada com compensador e sem compensador. Note que o erro estacionário está de acordo com o especificado, ou seja, e(∞) = 1 – 0,98 = 0,02.

   [img:Illustration] 

  Figura 5.63 Gráficos de Bode de G(jω), Gc(jω) e Gma(jω).

   [img:Illustration] 

  Figura 5.64 Respostas ao degrau unitário dos sistemas em malha fechada com compensador e sem compensador.

  

### 5.12 Exercícios resolvidos

  

### Exercício 5.1

  A resposta em frequência G(jω) de um processo industrial está representada pelos diagramas de Bode da Figura 5.65.

   [img:Illustration] 

  Figura 5.65 Diagramas de Bode da função G(jω).

  a) Determine a função de transferência do processo.

  b) Sabendo-se que a entrada do processo é u(t) = 10sen(100t), determine a saída y∞(t) em regime permanente.

  Solução

  a) No diagrama do módulo veriﬁca-se que a partir da frequência 10 (rad/s) o gráﬁco é uma reta com inclinação de −20 dB/década. Como a fase de G(jω) vale −45o nesta frequência, então G(s) possui um polo em s = −10.

  O ganho pode ser determinado a partir da curva do módulo em baixas frequências. Como 20 log k = 20, então, k = 10. Portanto, a função de transferência G(s) é

   [img:Illustration] 

  b) A amplitude do sinal senoidal de entrada é A = 10 e possui frequência ω = 100 (rad/s). A saída em regime permanente é dada pela Equação (5.11), ou seja,

   [img:Illustration] 

  Dos diagramas de Bode tem-se que |G(j100)| = 0 (dB) ⇒ |G(j100)| = 1 e ∠G(j100) ≅ −84o. Portanto,

   [img:Illustration] 

  

### Exercício 5.2

  Considere o diagrama de blocos da Figura 5.66 de um servomecanismo utilizado para acionamentos mecânicos.

   [img:Illustration] 

  Figura 5.66 Diagrama de blocos de um servomecanismo.

  Desenhe os gráﬁcos de Bode do sistema em malha aberta e determine as margens de ganho e de fase. Desenhe também os gráﬁcos de Bode do sistema em malha fechada e determine a frequência e o ganho no pico de ressonância.

  Solução

  A função de transferência de malha aberta é dada por

   [img:Illustration] 

  sendo Θ(s) e Ea(s) as transformadas de Laplace da posição angular do eixo e da tensão de armadura, respectivamente.

  Os gráﬁcos de Bode do sistema (5.164) são apresentados na Figura 5.67. Conforme se pode ver nesta ﬁgura, o gráﬁco do módulo de G(jω) é formado pela soma de três gráﬁcos: do ganho constante 20 log 25 ≅ 28 dB, do integrador (1/s) e do polo real em s = −4. Já o gráﬁco de Bode da fase de G(jω) é a soma da fase do integrador (−90o) com a fase do polo real em s = −4.

  A fase de G(jω) nunca atinge −180o. Logo, a margem de ganho MG é inﬁnita. Já a margem de fase MF é medida na frequência em que |G(jω)| = 0dB ou |G(jω)| = 1, isto é,

   [img:Illustration] 

   [img:Illustration] 

  Figura 5.67 Gráﬁcos de Bode do sistema (5.164).

  Para ω = 9,6 tem-se que

   [img:Illustration] 

  A margem de fase é dada por

   [img:Illustration] 

  A função de transferência do sistema em malha fechada é dada por

   [img:Illustration] 

  que corresponde à função de transferência de sistemas de segunda ordem

   [img:Illustration] 

  com ωn = 10 e ξ = 0,2.

  Os gráﬁcos de Bode do sistema (5.168) são apresentados na Figura 5.68. Como os polos do sistema em malha fechada são complexos conjugados, o gráﬁco do módulo de G(jω) em altas frequências apresenta uma assíntota com inclinação de −40 dB/década.

   [img:Illustration] 

  Figura 5.68 Gráﬁcos de Bode do sistema em malha fechada (5.168).

  O pico de ressonância ocorre na frequência

   [img:Illustration] 

  O valor do ganho Mr na frequência de ressonância ωr é dado por

   [img:Illustration] 

  

### Exercício 5.3

  Desenhe os diagramas de Bode correspondentes à função de transferência

   [img:Illustration] 

  Solução

  A função de transferência (5.172) possui um zero real em s = −5, um polo real em s = −1 e dois polos complexos conjugados em s = −0,5 ± 9,9875j.

  Escrevendo a função (5.172) no formato

   [img:Illustration] 

  obtém-se

   [img:Illustration] 

  com k = 10, T1 = 0,2, T2 = 1, ωn = 10 e ξ = 0,05.

  Os gráﬁcos de Bode do sistema (5.174) são apresentados na Figura 5.69. Conforme se pode ver nesta ﬁgura o gráﬁco do módulo de G(jω) é formado pela soma de quatro gráﬁcos: do ganho constante 20 log k = 20 dB, do zero real em s = −5, do polo real em s = −1 e dos polos complexos conjugados. Já o gráﬁco de Bode da fase de G(jω) é formado pela soma de três gráﬁcos: do zero real em s = −5, do polo real em s = −1 e dos polos complexos conjugados.

   [img:Illustration] 

  Figura 5.69 Gráﬁcos de Bode da função (5.172).

  O pico de ressonância devido aos polos complexos conjugados ocorre na frequência

   [img:Illustration] 

  

### Exercício 5.4

  Considere um sistema com a função de transferência de malha aberta

   [img:Illustration] 

  O módulo de G(jω)H(jω) é dado por

   [img:Illustration] 

  e a fase por

   [img:Illustration] 

  Na Tabela 5.12 são apresentados os valores do módulo e da fase de G(jω)H(jω) para algumas frequências 0 ≤ ω < ∞.

  Tabela 5.12 Módulo e fase da função G(jω)H(jω)

  
    
      

      

      

      

      

      

      

      

      

      
    

    
      
        
          ω

        

        
          0

        

        
          0,18

        

        
          0,37

        

        
          0,58

        

        
          0,84

        

        
          1,19

        

        
          1,73

        

        
          2,77

        

        
          ∞

        
      

      
        
          |G(jω)H(jω)|

        

        
          0,9

        

        
          0,89

        

        
          0,84

        

        
          0,78

        

        
          0,69

        

        
          0,58

        

        
          0,45

        

        
          0,31

        

        
          0

        
      

      
        
          ∠G(jω)H(jω)

        

        
          180o

        

        
          149o

        

        
          119o

        

        
          90o

        

        
          60o

        

        
          30o

        

        
          0o

        

        
          −30o

        

        
          −90o

        
      

    
  

  O contorno de Nyquist é o mesmo da Figura 5.25. O diagrama de Nyquist para −∞ <ω < ∞ é apresentado na Figura 5.70. O traçado do diagrama polar é a imagem do eixo jω do contorno de Nyquist. Já a semicircunferência de raio inﬁnito no semiplano direito de s do contorno de Nyquist é mapeada na origem do diagrama polar.

   [img:Illustration] 

  Figura 5.70 Diagrama polar de Nyquist.

  Como o sistema em malha aberta (5.176) não possui polos no semiplano direito (Np = 0) e como o diagrama polar não envolve o ponto −1 + j0 (N = 0), então o número de polos de mallha fechada no semiplano direito é zero (Nz = N + Np = 0). Portanto, o sistema em malha fechada é estável.

  

### Exercício 5.5

  Considere um sistema que tem a função de transferência de malha aberta

   [img:Illustration] 

  Desenhe o diagrama de Nyquist e analise a estabilidade do sistema em malha fechada.

  Solução

  A função G(s)H(s) tem um polo em s = 0 e outro em s = 1. Como a função (5.179) tem um polo na origem, o contorno de Nyquist tem o formato da Figura 5.71 (a).

   [img:Illustration] 

  Figura 5.71 (a) Contorno de Nyquist. (b) Diagrama polar de Nyquist.

  Para desenhar o diagrama polar de Nyquist da Figura 5.71 (b) é preciso analisar o percurso de Nyquist em cada trecho do seu contorno.

  • trecho abc: representa a pequena semicircunferência de raio ρ em torno do polo na origem no contorno de Nyquist. Fazendo

   [img:Illustration] 

  o mapeamento de G(s)H(s) para ρ → 0 é

   [img:Illustration] 

  Portanto, para ρ → 0 o módulo de G(jω)H(jω) tende a inﬁnito e a fase de G(jω)H(jω) tende a −180o − ϕ. Como a fase ϕ varia de −90o a +90o, a fase de G(jω)H(jω) também varia de −90o a +90o no diagrama polar. O trecho abc correspondente do diagrama polar é mostrado na Figura 5.71 (b).

  • trecho cd: a frequência varia de ω = 0+ a ω = +∞. Substituindo s por jω na Equação (5.179), obtém-se

   [img:Illustration] 

  O módulo de G(jω)H(jω) é dado por

   [img:Illustration] 

  e a fase é dada por

   [img:Illustration] 

  Assim,

  para ω = 0+ ⇒ |G(jω)H(jω)| → ∞ e ∠G(jω)H(jω) = 90o e

  para ω → +∞ ⇒ |G(jω)H(jω)| = 0 e ∠G(jω)H(jω) = 180o.

  Portanto, o trecho cd do contorno de Nyquist é mapeado no trecho que vai do ponto c até a origem no diagrama polar.

  • trecho de: a frequência varia de ω = +∞ a ω = −∞. Neste caso, |G(jω)H(jω)| = 0 e o mapeamento corresponde a um único ponto, que é a origem do diagrama polar.

  • trecho ea: a frequência varia de ω = −∞ a ω = 0−. Como o diagrama polar deve ser simétrico com relação ao eixo real, o trecho ea do contorno de Nyquist é mapeado no trecho que vai da origem até o ponto a no diagrama polar.

  Assim, o diagrama de Nyquist da Figura 5.71 (b) envolve uma vez o ponto −1+ j0 no sentido horário (N = 1). Como o sistema em malha aberta (5.179) possui um polo no semiplano direito (Np = 1), então o número de polos de malha fechada no semiplano direito é

   [img:Illustration] 

  Portanto, o sistema em malha fechada é instável para qualquer valor de k.

  

### Exercício 5.6

  Desenhe o diagrama de Nyquist e analise a estabilidade da malha fechada do sistema que tem a função de transferência de malha aberta

   [img:Illustration] 

  Solução

  A função G(s)H(s) tem um polo duplo em s = 0 e outro em s = −1/τ. Como a função (5.186) tem polos na origem, o contorno de Nyquist tem o formato da Figura 5.71 (a). Para desenhar o diagrama de Nyquist é preciso analisar cada trecho do contorno, como no exercício anterior.

  • trecho abc: representa a pequena semicircunferência de raio ρ em torno do polo na origem no contorno de Nyquist. Fazendo contorno de Nyquist. Fazendo

   [img:Illustration] 

  o mapeamento de G(s)H(s) para ρ → 0 é

   [img:Illustration] 

  Portanto, para ρ → 0 o módulo de G(jω)H(jω) tende a inﬁnito. Como a fase ϕ varia de −90o a +90o, a fase de G(jω)H(jω) varia de +180o a −180o, percorrendo um círculo completo quando ω varia de ω = 0− a ω = 0+.

  • trecho cd: a frequência varia de ω = 0+ a ω = +∞. Substituindo s por jω na Equação (5.186), obtém-se

   [img:Illustration] 

  e a fase é dada por

   [img:Illustration] 

  Assim,

  para ω = 0+ ⇒ |G(jω)H(jω)| → ∞ e ∠G(jω)H(jω) = −180o e

  para ω → +∞ ⇒ |G(jω)H(jω)| = 0 e ∠G(jω)H(jω) = −270o.

  Portanto, neste trecho o diagrama de Nyquist ﬁca no segundo quadrante, pois a fase de G(jω)H(jω) varia de −180o a −270o.

  • trecho de: a frequência varia de ω = +∞ a ω = −∞. Neste caso, o mapeamento corresponde à origem do diagrama polar.

  • trecho ea: a frequência varia de ω = −∞ a ω = 0−. Basta completar o diagrama polar de modo que este seja simétrico com relação ao eixo real.

  O diagrama polar de Nyquist é apresentado na Figura 5.72. Como a função (5.186) não possui polos no semiplano direito (Np = 0) e como o diagrama envolve duas vezes o ponto −1 + j0 no sentido horário (N = 2), então o número de polos de malha fechada no semiplano direito é

   [img:Illustration] 

  Portanto, o sistema em malha fechada é instável para qualquer valor de k.

   [img:Illustration] 

  Figura 5.72 Diagrama polar de Nyquist.

  

### Exercício 5.7

  Considere o sistema em malha fechada da Figura 5.73. Os diagramas de Bode da planta G(s) são apresentados na Figura 5.74.

   [img:Illustration] 

  Figura 5.73 Sistema em malha fechada.

   [img:Illustration] 

  Figura 5.74 Diagramas de Bode da planta G(jω).

  Determine:

  a) a função de transferência da planta;

  b) o valor do ganho do controlador K para que a margem de fase seja de 45o.

  c) o erro estacionário, quando é aplicado um degrau unitário na referência.

  Solução

  a) No diagrama do módulo se veriﬁca que em baixas frequências o gráﬁco é uma reta com inclinação de −20 dB/década, sendo o ganho 0 dB na frequência 1 (rad/s). Logo, G(s) possui um polo em s = 0. A partir da frequência 10 (rad/s) a inclinação da reta muda para −40 dB/década, que é o resultado da soma da inclinação da assíntota do polo na origem com a inclinação da assíntota de um polo em s = −10. Note que nesta frequência a fase de G(jω) vale −135o, que é o resultado da soma da fase de −90o do polo na origem com a fase de −45o do polo em s = −10.

  Portanto, a função de transferência é

   [img:Illustration] 

  b) Para que a margem de fase seja MF = 45o, a fase de G(jω) deve valer

   [img:Illustration] 

  cujo valor ocorre na frequência 10 (rad/s).

  Para que o ganho do gráﬁco do módulo seja 0 dB na frequência 10 (rad/s), o ganho K do controlador deve valer aproximadamente 23 dB, ou seja, 20 log K ≅ 23 dB. Portanto, K ≅ 14,1.

  c) O erro estacionário é nulo, pois a planta possui um integrador (polo na origem).

  

### Exercício 5.8

  Considere o sistema da Figura 5.75. Qual o valor da margem de ganho? Determine o valor do ganho k de modo que a margem de fase seja MF = 60o.

   [img:Illustration] 

  Figura 5.75 Diagrama de blocos de um sistema.

  Solução

  A função de transferência de malha aberta é dada por

   [img:Illustration] 

  Como G(s) possui apenas dois polos na origem, a fase de G(jω) nunca cruza a linha de −180o. Portanto, a margem de ganho é inﬁnita.

  Substituindo s por jω na Equação (5.194), obtém-se

   [img:Illustration] 

  Para que a margem de fase seja MF = 60o, a fase de G(jω) deve valer

   [img:Illustration] 

  Assim,

   [img:Illustration] 

  Portanto, na frequência ω =  [img:Illustration]  rad/s o módulo de G(jω) deve ser igual a 1, ou seja,

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  

### Exercício 5.9

  Considere o sistema da Figura 5.76.

   [img:Illustration] 

  Figura 5.76 Diagrama de blocos de um sistema.

  • Supondo K = 1, calcule a margem de ganho e a margem de fase.

  • Analise a estabilidade do sistema em malha fechada em termos do ganho K.

  Solução

  A função de transferência de malha aberta é dada por

   [img:Illustration] 

  Substituindo s por jω na Equação (5.200), obtém-se

   [img:Illustration] 

  A margem de ganho é calculada na frequência ω > 0 em que ∠G(jω) = −180o, ou seja,

   [img:Illustration] 

  Da Equação (5.109), com H(jω) = 1, tem-se que

   [img:Illustration] 

  A margem de fase é calculada na frequência ω > 0 em que |G(jω)| = 1, ou seja,

   [img:Illustration] 

  resultando

   [img:Illustration] 

  cuja única solução real, para ω > 0, é ω ≅ 1,23.

  Da Equação (5.110), com H(jω) = 1, tem-se que

   [img:Illustration] 

  Os resultados (5.203) e (5.206) signiﬁcam que o ganho K do controlador pode ser aumentado em até 3 vezes, de modo que o sistema em malha fechada seja estável. De fato, para K = 3 a função de transferência de malha fechada é

   [img:Illustration] 

  cujos polos são s = −6 e s = ±  [img:Illustration] j.

  Portanto, o sistema em malha fechada é estável para 0 <K < 3.

  

### 5.13 Exercícios propostos

  

### Exercício 5.10

  Determinar a saída y∞(t) em regime permanente do sistema linear e invariante no tempo da Figura 5.77, quando é aplicada a entrada u(t) = 3 sen(5t + 30o).

   [img:Illustration] 

  Figura 5.77 Sistema linear e invariante no tempo.

  

### Exercício 5.11

  Desenhe os diagramas de Bode correspondentes às seguintes funções de transferência:

   [img:Illustration] 

  

### Exercício 5.12

  Determine as funções de transferência G1(s) e G2(s) correspondentes aos diagramas de Bode das Figuras 5.78 (a) e (b), respectivamente.

   [img:Illustration] 

  Figura 5.78 (a) Módulo de G1(jω). (b) Módulo de G2(jω).

  

### Exercício 5.13

  Foi medida experimentalmente a resposta em frequência de um sistema cujos dados estão apresentados na Tabela 5.13. Desenhe os diagramas de Bode e determine a função de transferência G(s) correspondente.

  Tabela 5.13 Módulo e fase da função G(jω)

  
    
      
        

        

        
      

      
        
          
            ω

          

          
            |G(jω)| (dB)

          

          
            ∠G(jω) (graus)

          
        

        
          
            0,1

          

          
            54

          

          
            −96

          
        

        
          
            0,2

          

          
            48

          

          
            −101

          
        

        
          
            0,5

          

          
            39

          

          
            −116

          
        

        
          
            1

          

          
            31

          

          
            −135

          
        

        
          
            2

          

          
            21

          

          
            −153

          
        

        
          
            5

          

          
            6

          

          
            −169

          
        

        
          
            10

          

          
            −6

          

          
            −174

          
        

        
          
            20

          

          
            −18

          

          
            −177

          
        

        
          
            50

          

          
            −34

          

          
            −179

          
        

        
          
            100

          

          
            −46

          

          
            −180

          
        

      
    
  

  

### Exercício 5.14

  A resposta em frequência de um sistema em malha aberta G(jω) está indicada na Figura 5.79.

  Determine as margens de ganho e de fase. O sistema em malha fechada com realimentação unitária é estável ou instável?

   [img:Illustration] 

  Figura 5.79 Resposta em frequência de um sistema G(jω).

  

### Exercício 5.15

  Supondo que no sistema em malha aberta da Figura 5.79 seja feita uma realimentação unitária, determine o valor do erro no estado estacionário do sistema em malha fechada quando é aplicado um degrau unitário na referência.

  

### Exercício 5.16

  Um servossistema tem função de transferência de malha aberta

   [img:Illustration] 

  Sabendo-se que o ganho k é ajustado para que a margem de fase seja de 45o, determine a margem de ganho.

  

### Exercício 5.17

  Considere o sistema da Figura 5.80.

   [img:Illustration] 

  Figura 5.80 Diagrama de blocos de um sistema.

  a) Determine o valor do controlador Kc para que a margem de ganho seja de 20 dB.

  b) Determine a margem de fase para o valor de Kc calculado no item anterior.

  

### Exercício 5.18

  Considere o diagrama de blocos do sistema da Figura 5.81. Determine os valores de k e a, de modo que o pico de ressonância seja Mr = 1,04 e ocorra na frequência ωr = 11,55 rad/s.

   [img:Illustration] 

  Figura 5.81 Diagrama de blocos de um sistema.

  

### Exercício 5.19

  Analise a estabilidade dos sistemas em malha fechada desenhando os diagramas de Nyquist dos seguintes sistemas em malha aberta G(s)H(s):

   [img:Illustration] 

  

### Exercício 5.20

  Considere o diagrama de blocos do sistema da Figura 5.82. Determine por meio da carta de Nichols a frequência e o pico de ressonância do sistema em malha fechada.

   [img:Illustration] 

  Figura 5.82 Diagrama de blocos de um sistema.

  

### Exercício 5.21

  Sabendo-se que K > 0 é um controlador proporcional e G(s) é a função de transferência de um processo, a resposta em frequência de G(jω) é apresentada na carta de Nichols da Figura 5.83.

   [img:Illustration] 

  Figura 5.83 Carta de Nichols.

  a) Para K = 1, determine:

  a.1) a margem de ganho em (dB);

  a.2) a margem de fase em graus;

  a.3) o valor do pico de ressonância Mr (dB) do sistema em malha fechada;

  a.4) a frequência de ressonância ωr (rad/s) do sistema em malha fechada;

  a.5) o erro no estado estacionário quando é aplicado um degrau unitário na referência.

  b) Determine o valor do controlador K para que a margem de ganho seja de 35 dB.

  

### Exercício 5.22

  Considere o diagrama de blocos do sistema da Figura 5.84. Determine a banda passante do sistema em malha aberta e a banda passante do sistema em malha fechada.

   [img:Illustration] 

  Figura 5.84 Diagrama de blocos de um sistema.

  

### Exercício 5.23

  Projete um compensador Gc(s) por avanço de fase para o sistema da Figura 5.85, de modo que as seguintes especiﬁcações sejam satisfeitas:

  • erro estacionário de −0,1 para entrada de referência do tipo degrau unitário;

  • margem de fase de 50o.

   [img:Illustration] 

  Figura 5.85 Diagrama de blocos do sistema em malha fechada.

  

### Exercício 5.24

  Projete um compensador Gc(s) por atraso de fase para o sistema da Figura 5.86, de modo que a resposta para entrada do tipo rampa unitária na referência apresente erro estacionário de 0,05 sem alterar o valor da margem de fase.

   [img:Illustration] 

  Figura 5.86 Diagrama de blocos do sistema em malha fechada.

  

### Exercício 5.25

  Projete um compensador Gc(s) por avanço e atraso de fase para o sistema da Figura 5.86, de modo que as seguintes especiﬁcações sejam satisfeitas:

  • erro estacionário de 0,05 para entrada de referência do tipo rampa unitária;

  • margem de fase de 50o.

  

### Exercício 5.26

  Considere um processo de fundição para a produção de barras de alumínio7 cuja função de transferência é

   [img:Illustration] 

  Projete um compensador por atraso de fase de modo que as seguintes especiﬁcações sejam satisfeitas:

  • erro estacionário de 0,05 para entrada de referência do tipo degrau unitário;

  • margem de ganho de 10 dB.

  

  __________

  1Funções de transferência com apenas um zero no numerador não são usualmente implementadas, devido aos elevados ganhos em altas frequências que amplificam ruídos e acarretam saturação dos dispositivos.

  2Funções de transferência em que o grau do numerador é maior que o do denominador não são usualmente implementadas.

  3São os sistemas que têm todos os seus polos localizados no semiplano esquerdo aberto do plano s.

  4Caso esta correção não produza um resultado satisfatório, o projeto do compensador deve ser refeito.

  5Na prática este ajuste pode ser até 10o maior. Caso os resultados não sejam satisfatórios, o projeto do compensador deve ser refeito.

  6Caso esta aproximação não seja satisfatória, o projeto do compensador deve ser refeito.

  7Ver Exercício 9.3.

<!-- Text/chapter06.xhtml -->

  Controle Automático, 2ª edição
  
  
  

  

## 6

  

## Controladores PID

  

### 6.1 Introdução

  Ao longo das últimas décadas teorias matemáticas dedicadas ao controle ótimo e ao controle robusto têm produzido importantes resultados, indispensáveis nas aplicações aeronáuticas, aeroespaciais e similares. No entanto, algumas arquiteturas especiais utilizando algoritmos clássicos, chamados de PID ou P+I+D, têm demonstrado notável eﬁcácia e praticidade no controle dos processos industriais. Esses controladores PID, ainda mais quando inseridos nos computadores industriais e nos controladores lógicos programáveis, mantêm-se como um dos principais equipamentos de controle.

  O nome PID deriva do fato de que sua função de transferência contém a soma das ações Proporcional, Integradora e Derivadora. Seus parâmetros são de fácil ajuste e sua construção é adequadamente robusta para o ambiente industrial. O sucesso do controlador PID também decorreu de uma bem-sucedida padronização, na sua versão eletrônica, desde 1950.

  Neste capítulo, além de estudar as diversas versões dos controladores PID, por meio do Lugar das Raízes e dos Diagramas de Bode, são apresentadas as suas implementações analógicas e digital. Também são estudados dois complementos inerentes aos controladores PID:

  • transição suave (bumpless transition), entre as operações manual e automática e

  • antidisparo da integral (antireset windup).

  

### 6.2 A função de transferência do controlador PID

  O modelo matemático de um controlador PID, conforme o padrão ISA, é dado por

   [img:Illustration] 

  sendo:

  m(t): sinal de saída do controlador, chamado de variável manipulada;

  e(t): sinal de entrada do controlador, chamado de erro atuante;

  Kc, TI e TD: parâmetros de ajuste do controlador.

  As três parcelas do controlador PID correspondem aos efeitos Proporcional, Integrador e Derivador do sinal de erro atuante. Note que neste modelo os coeﬁcientes de cada parcela são interdependentes (Kc, Kc/TI e KcTD).

  Tradicionalmente é utilizada a seguinte denominação, relativa aos parâmetros de ajuste do controlador PID:

  Kc: ganho proporcional;

  Kc/TI: ganho da integral (reset gain);

  KcTD: ganho da derivada (rate gain).

  A função de transferência correspondente ao modelo da Equação (6.1) é

   [img:Illustration] 

  ou seja, o controlador PID(s) possui um polo na origem e dois zeros reais ou complexos conjugados em

   [img:Illustration] 

  Os controladores PID também são muito empregados com efeitos parciais:

  • PI (Proporcional mais Integrador) para o qual se adota TD = 0. Neste caso tem-se a função de transferência

   [img:Illustration] 

  que apresenta um zero real em −1/TI e um polo na origem.

  • PD (Proporcional mais Derivador) para o qual se adota TI → ∞. Neste caso tem-se

   [img:Illustration] 

  que apresenta um zero real em −1/TD.

  É útil analisar separadamente o efeito temporal de cada uma das três parcelas. Os efeitos dos termos proporcional e integral são mostrados na Figura 6.1, supondo um sinal de erro atuante do tipo pulso, de amplitude E.

   [img:Illustration] 

  Figura 6.1 (a) Sinal de erro atuante de amplitude E. (b) Sinal gerado pela ação proporcional. (c) Sinal gerado pela ação integral.

  O sinal do tipo pulso, utilizado para analisar o efeito das ações proporcional e integral, não é adequado para a análise do efeito correspondente à derivada devido às descontinuidades no início e no ﬁnal do sinal. Assim, na Figura 6.2 utiliza-se uma rampa unitária como sinal de erro atuante para mostrar o efeito da derivada no controlador PID.

   [img:Illustration] 

  Figura 6.2 (a) Sinal de erro atuante (rampa unitária). (b) Sinal gerado pela ação derivadora.

  Para obter o aspecto geral dos gráﬁcos de Bode do controlador PID na Figura 6.3, considere a situação em que os zeros s1 e s2 do controlador são reais, com (s1 ≠ s2). Para isso, da Equação (6.5) deve-se ter  [img:Illustration]  − 4TI TD > 0. O gráﬁco do módulo possui em baixas frequências uma declividade de −20 dB/década, com predomínio da ação integradora, e em altas frequências possui uma declividade de +20 dB/década, com predomínio da ação derivadora. A defasagem varia de −90o a +90o.

   [img:Illustration] 

  Figura 6.3 Diagramas de Bode do controlador PID com zeros reais s1 ≠ s2.

  Como importantes características do controlador PID no domínio da frequência deve-se destacar o ganho tendendo a inﬁnito em baixas frequências, cuja função é reduzir o erro estacionário, e o avanço de fase acima da frequência  [img:Illustration]  cuja propriedade é melhorar a estabilidade relativa do sistema. Normalmente procura-se ajustar os parâmetros do controlador PID de forma que o atraso de fase produzido pelo termo integrador ocorra em frequências baixas, de forma a não afetar a estabilidade relativa do sistema.

  Os gráﬁcos de Bode dos controladores PI e PD são muito mais simples, como mostrado nas Figuras 6.4 e 6.5, respectivamente. O gráﬁco do módulo do controlador PI troca de declividade de −20 dB/década para 0 na frequência 1/TI e, como o controlador PID, produz ganhos elevados em baixas frequências, que reduzem o erro estacionário. Porém, o atraso de fase do controlador PI piora a estabilidade relativa do sistema. Já no caso do controlador PD a declividade passa de 0 para +20 dB/década na frequência 1/TD e produz um avanço de fase, cuja função é melhorar a estabilidade relativa do sistema.

   [img:Illustration] 

  Figura 6.4 Diagramas de Bode do controlador PI com zero real em  [img:Illustration] 

   [img:Illustration] 

  Figura 6.5 Diagramas de Bode do controlador PD com zero real em  [img:Illustration] 

  É interessante observar que os gráﬁcos de Bode do controlador PID da Figura 6.3 diferem dos gráﬁcos do controlador por avanço e atraso de fase da Figura 5.58. Embora pretendam ter o mesmo efeito estabilizante, o gráﬁco de módulo do PID, em teoria, tem ganhos tendendo ao inﬁnito tanto em frequências muito baixas como em frequências muito altas. Para limitar o ganho em altas frequências deve-se ressaltar que, na prática, é comum a adição de uma parcela atenuadora, que consiste na inclusão de um polo de alta frequência na função de transferência do controlador (ver Seção 6.3.1).

  Dada a simplicidade das funções de transferência dos controladores PI e PD, é comum a determinação dos parâmetros correspondentes utilizando-se o método do lugar das raízes, seguida de uma análise das margens de estabilidade por meio dos gráﬁcos de Bode. Já para os controladores PID as técnicas de ajuste mais frequentes baseiam-se em regras heurísticas (ver Seções 7.2 e 7.5).

  

### Exemplo 6.1

  Considere o diagrama de blocos da Figura 6.6.

   [img:Illustration] 

  Figura 6.6 Diagrama de blocos de um sistema em malha fechada.

  Sendo a função de transferência da planta

   [img:Illustration] 

  deseja-se analisar o comportamento deste sistema com os controladores P, PI, PD e PID.

  

### Controlador P

  Para Gc(s) = Kc o diagrama do lugar das raízes é apresentado na Figura 6.7.

   [img:Illustration] 

  Figura 6.7 Lugar das raízes com o controlador P.

  Para s = −3 os polos de malha fechada são reais e iguais. Neste ponto o ganho vale

   [img:Illustration] 

  Portanto:

  • para 0 < Kc ≤ 4 os polos de malha fechada são reais e a resposta ao degrau na referência é amortecida;

  • para Kc > 4 os polos de malha fechada são complexos conjugados e a resposta ao degrau na referência é subamortecida.

  Para entradas do tipo degrau unitário na referência R(s) e na perturbação D(s) tem-se que

   [img:Illustration] 

  O erro estacionário pode ser calculado por meio do teorema do valor ﬁnal.

   [img:Illustration] 

  Logo, o erro estacionário é não nulo para Kc > 0. Porém,

  • para Kc "pequeno" o erro estacionário é "grande", e

  • para Kc "grande" o erro estacionário é "pequeno".

  Na Figura 6.8 são apresentados os gráﬁcos da resposta ao degrau unitário na referência, com perturbação nula (D(s) = 0), para Kc = 4 e Kc = 100. Note que

  • para Kc = 4, a resposta transitória é mais lenta, amortecida e o erro estacionário vale

   [img:Illustration] 

  • para Kc = 100, a resposta transitória é mais rápida, subamortecida e o erro estacionário vale

   [img:Illustration] 

   [img:Illustration] 

  Figura 6.8 Resposta ao degrau unitário em r(t) com controlador P e d(t) = 0.

  Os diagramas de Bode de KcG(jω) são apresentados na Figura 6.9. Para Kc = 4 a margem de ganho é inﬁnita, pois o gráﬁco de fase nunca cruza a linha de 180o e a margem de fase também é inﬁnita, pois o gráﬁco do módulo nunca cruza a linha de 0 dB. Já para Kc = 100 a margem de ganho é inﬁnita e a margem de fase vale MF ≅ 34,2o.

   [img:Illustration] 

  Figura 6.9 Diagramas de Bode da função de malha aberta com controlador P.

  

### Controlador PI

  A função de transferência do controlador PI é dada por

   [img:Illustration] 

  Um procedimento bastante usual é adotar TI de forma que o zero do controlador cancele o polo mais lento da planta, neste exemplo em s = −1. Assim, supondo TI = 1 o lugar das raízes ﬁca como mostrado na Figura 6.10.

   [img:Illustration] 

  Figura 6.10 Lugar das raízes com o controlador PI.

  Comparando a Figura 6.10 com a Figura 6.7 veriﬁca-se que o controlador PI desloca o lugar das raízes para a direita do plano s, o que faz piorar a estabilidade relativa do sistema.

  Os polos de malha fechada são reais e iguais em s = −2,5. Neste ponto o ganho vale

   [img:Illustration] 

  Logo,

  • para 0 < Kc ≤ 6,25 os polos de malha fechada são reais e a resposta ao degrau na referência é amortecida;

  • para Kc > 6,25 os polos de malha fechada são complexos conjugados e a resposta ao degrau na referência é subamortecida.

  Um ponto importante a ser observado é que para quaisquer valores de Kc e TI tem-se que o erro estacionário para entradas do tipo degrau nos sinais de referência R(s) e de perturbação D(s) é igual a zero, independentemente da função de transferência da planta. Esta é a principal característica do termo integrador do controlador PI, válida também para os controladores PID. Esta propriedade pode ser veriﬁcada analiticamente a partir do teorema do valor final.

  Para R(s) = D(s) = A/s tem-se que

   [img:Illustration] 

  Na Figura 6.11 é apresentada a resposta ao degrau unitário na referência, com perturbação nula, e na Figura 6.12 é apresentada a resposta ao degrau unitário na perturbação, com referência nula. Em ambas as respostas foram adotados TI = 1, Kc = 6,25 e Kc = 100. Analisando a Figura 6.11 verifica-se que o erro estacionário é sempre nulo. Para Kc = 100 a resposta ao degrau na referência tem um sobressinal Mp ≅ 44,4%, que é maior que o sobressinal Mp ≅ 31,6%, obtido com o controlador proporcional, para o mesmo ganho Kc = 100 da Figura 6.8. Isso porque o controlador PI piora a estabilidade relativa do sistema. Embora TI tenha sido ajustado para cancelar um polo da planta, obviamente outros ajustes para Kc e TI podem ser empregados para atender a uma dada especificação de transitório.

   [img:Illustration] 

  Figura 6.11 Resposta ao degrau unitário em r(t) com controlador PI e d(t) = 0.

   [img:Illustration] 

  Figura 6.12 Resposta ao degrau unitário em d(t) com controlador PI e r(t) = 0.

  A Figura 6.12 mostra que a saída estacionária tende para a sua referência (y(∞) = r(∞) = 0), sendo a perturbação do tipo degrau unitário (D(s) = 1/s) completamente rejeitada no estado estacionário.

  Os diagramas de Bode de Gc(jω)G(jω) são apresentados na Figura 6.13. Como o gráfico de fase nunca cruza a linha de 180o as margens de ganho para Kc = 6,25 e Kc = 100 são infinitas. Porém, para Kc = 6,25 a margem de fase vale MF ≅ 76o e para Kc = 100 a margem de fase vale MF ≅ 28o. Note que para Kc = 100 a margem de fase é menor, quando comparada com a margem de fase do sistema com o controlador proporcional na Figura 6.9.

   [img:Illustration] 

  Figura 6.13 Diagramas de Bode da função de malha aberta com controlador PI.

  

### Controlador PD

  A função de transferência do controlador PD é dada por

   [img:Illustration] 

  Adotando TD = 1, de forma que o zero do controlador cancele o polo mais lento da planta, o lugar das raízes fica como mostrado na Figura 6.14. Conforme se pode verificar o lugar das raízes se desloca para a esquerda, aumentando a estabilidade relativa do sistema. Em particular para o valor de TD adotado pode-se ajustar um ganho elevado para Kc, que a resposta transitória é sempre superamortecida.

   [img:Illustration] 

  Figura 6.14 Lugar das raízes com o controlador PD.

  Aplicando-se entradas do tipo degrau unitário na referência R(s) e na perturbação D(s), o erro estacionário vale

   [img:Illustration] 

  Logo, o erro estacionário é não nulo para Kc > 0. Porém,

  • para Kc "pequeno" o erro estacionário é "grande" e

  • para Kc "grande" o erro estacionário é "pequeno".

  Na Figura 6.15 é apresentado o gráfico da resposta ao degrau unitário na referência, com perturbação nula, para Kc = 100. Verifica-se que com o controlador PD foi possível obter uma resposta rápida e sem sobressinal, o que não ocorreu com os controladores P e PI. Para D(s) = 0 o erro estacionário vale

   [img:Illustration] 

   [img:Illustration] 

  Figura 6.15 Resposta ao degrau unitário em r(t) com controlador PD e d(t) = 0.

  Os diagramas de Bode de Gc(jω)G(jω) são apresentados na Figura 6.16. A margem de ganho é infinita e a margem de fase vale MF ≅ 93o. Note que para o mesmo ganho Kc = 100 a margem de fase obtida com o controlador PD é maior que as margens de fase obtidas com os controladores P e PI.

   [img:Illustration] 

  Figura 6.16 Diagramas de Bode da função de malha aberta com controlador PD.

  

### Controlador PID

  A função de transferência do controlador PID é dada por

   [img:Illustration] 

  Adotando TI = 6/5 e TD = 1/6, de modo que os zeros do controlador cancelem os polos da planta, a função de transferência de malha aberta resulta

   [img:Illustration] 

  O lugar das raízes é apresentado na Figura 6.17. Neste exemplo o controlador PID possui todas as vantagens dos controladores P, PI e PD:

  • aumentando-se o ganho Kc pode-se obter uma resposta rápida e sempre superamortecida;

  • o erro estacionário é nulo para entradas do tipo degrau na referência e na perturbação.

   [img:Illustration] 

  Figura 6.17 Lugar das raízes com o controlador PID.

  Na Figura 6.18 é apresentado o gráfico da resposta ao degrau unitário na referência, com perturbação nula, para Kc = 100.

   [img:Illustration] 

  Figura 6.18 Resposta ao degrau unitário em r(t) com controlador PID e d(t) = 0.

  Os diagramas de Bode de Gc(jω)G(jω) são apresentados na Figura 6.19. A margem de ganho é infinita e a margem de fase vale MF ≅ 90o, que é maior que as margens de fase obtidas com os controladores P e PI.

   [img:Illustration] 

  Figura 6.19 Diagramas de Bode da função de malha aberta com controlador PID.

  ■

  

### 6.3 Aspectos de implementação dos controladores PID

  O controlador PID, na forma apresentada na Seção 6.2, apresenta alguns inconvenientes associados à possibilidade de saturação de componentes da malha de controle e à transferência da operação do processo do modo manual para o modo automático.

  Nesta seção são consideradas algumas técnicas consagradas na implementação de controladores PID que visam contornar esses inconvenientes.

  

#### 6.3.1 Implementação do termo derivador

  Conforme citado na Seção 6.2, o termo associado à derivada no controlador PID produz um ganho que tende ao infinito em frequências altas. Como nas aplicações de controle a presença de ruídos é inevitável, esses ganhos altos levam à saturação os elementos finais de controle como, por exemplo, amplificadores e atuadores.

  De forma a contornar esse problema a função de transferência do controlador PID é usualmente modificada, acrescentando-se um filtro passa-baixas ao termo associado à derivada, que resulta como

   [img:Illustration] 

  sendo N um parâmetro tipicamente adotado entre 0,05 e 0,17 (ver [36] e [55]).

  No caso do controlador PD, cuja função de transferência original é

   [img:Illustration] 

  a inclusão do filtro passa-baixas resulta na função de transferência modificada

   [img:Illustration] 

  Na Figura 6.20 são mostrados os gráficos de Bode do módulo do controlador PD na forma original (6.23) e na forma modificada (6.24), incluindo o filtro passa-baixas. Fica evidente o efeito de atenuação do ganho em frequências altas a partir da frequência  [img:Illustration] 

   [img:Illustration] 

  Figura 6.20 Diagramas de Bode do módulo do PD original e do PD modificado com a inclusão do filtro passa-baixas.

  

#### 6.3.2 Implementação sem derivada do erro

  Nos problemas de regulação da saída da planta, em que o sinal de referência é mantido em níveis constantes, a derivada do erro pode produzir picos nos amplificadores e atuadores quando se muda o nível do sinal de referência. Nesta operação, ao se aplicar um sinal do tipo degrau na referência ocorre também um degrau no sinal de erro, e o termo derivador, por sua vez, produz picos na saída do controlador.

  Em vez de calcular a derivada do erro, como na equação

   [img:Illustration] 

  uma solução é implementar a derivada apenas como realimentação do sinal de saída da planta, ou seja,

   [img:Illustration] 

  O diagrama de blocos desta implementação é apresentado na Figura 6.21. Note que os sinais de controle M(s), produzidos pelas Equações (6.25) e (6.26), são idênticos a menos do instante em que ocorre o degrau no sinal de referência.

   [img:Illustration] 

  Figura 6.21 Diagrama de blocos do sistema de controle sem derivada do erro.

  

#### 6.3.3 Transferência manual-automático suave (bumpless)

  A transferência manual-automático suave (bumpless) visa evitar saltos na variável manipulada m(t) quando o operador, após levar manualmente o processo até sua região de trabalho normal, transfere o sistema de controle manual para PID automático.

  O problema tem origem no fato de que na fase manual o termo integrador do PID integra no tempo grandes diferenças existentes entre o sinal de referência r(t) e o sinal de saída y(t), levando em geral a saída do PID à saturação. Ao passar para automático o processo todo sofre uma forte perturbação que só se reduz lentamente à medida que a saída do PID sai da saturação. O esquema de transferência simples, que não evita o choque quando ocorre a transferência de manual (M) para automático (A), é mostrado na Figura 6.22.

   [img:Illustration] 

  Figura 6.22 Transferência automático-manual simples.

  Uma solução para este problema é implementar o PID por meio de um bloco de ganho Kc em cascata com uma malha com realimentação KB(s) conveniente, conforme a Figura 6.23.

   [img:Illustration] 

  Figura 6.23 Transferência manual-automático suave (bumpless).

  Da Figura 6.23 tem-se que na posição automática

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  KB(s) é calculado a partir da identidade

   [img:Illustration] 

  Da Equação (6.29) tem-se que

   [img:Illustration] 

  Na posição manual e'(t) = 0 e m(t) é igual à saída de KB(s) com entrada mM(t), gerada manualmente pelo operador. Como KB(s) tem ganho unitário em frequências baixas (KB (0) = 1) e mM(t) é por natureza um sinal de frequências baixas, resulta m(t) ≅ mM(t) e, assim, KB(s) não prejudica as ações do operador.

  Na Figura 6.23 o chaveamento de manual para automático se faz por chave dupla, de forma que seja na posição manual, seja na automática o sinal de atuação m(t) sai do bloco KB(s), evitando-se assim qualquer transitório por causa do termo integral.

  

#### 6.3.4 Antidisparo da referência (antireset windup)

  O termo integral da função de transferência do controlador PID é fundamental para eliminar o erro estacionário decorrente de sinais do tipo degrau, na referência ou na perturbação.

  No entanto, quando um elemento do atuador ou do processo sofre saturação existe um efeito secundário muito prejudicial. Nessa condição o erro atuante permanece grande por um tempo muito maior que o previsto pelo modelo linear, e o termo integral do erro atuante acumula um grande valor. Mesmo que o sistema volte ao funcionamento linear é necessário um tempo muito grande para que o erro atuante, com sinal contrário ao que ocorreu na saturação, reduza o valor do termo integral. O resultado é uma excessiva degradação do desempenho da realimentação. Como o efeito que se observa externamente se parece com um disparo do sinal da referência, consagrou-se na prática o nome reset windup.

  De fato, seja o controlador PI

   [img:Illustration] 

  Suponha que em t = ts seja aplicado um degrau positivo na referência r(t), que produz um erro atuante excepcionalmente grande, levando m(t) ao nível de saturação M do atuador. Devido à dinâmica do processo, suponha que a saída demore até t = tf para atingir a referência e reduzir o erro atuante. Devido à ação integradora do controlador PI, o valor acumulado em m(t), entre o início da saturação ts e o seu final tf, pode atingir um valor

   [img:Illustration] 

  Após o tempo tf o sinal algébrico de e(t) se torna negativo e m(t) começa a diminuir, conforme a equação

   [img:Illustration] 

  Consequentemente, m(t) se mantém na saturação por um longo tempo após o instante tf. Este é o chamado disparo (windup) pela ação do termo integral (reset).

  Uma solução para o problema é mostrada na Figura 6.24, na qual é utilizado um mecanismo chamado de realimentação externa.

   [img:Illustration] 

  Figura 6.24 Esquema de controlador PI com antidisparo da referência (antireset windup).

  O algoritmo PI tem seu termo integral realizado em um ramo de realimentação, em torno de um bloco com saturação, no mesmo nível M em que ocorre a saturação do atuador do processo. O sinal de saída m*(t) para este bloco é dado por

   [img:Illustration] 

  A função de transferência do controlador da Figura 6.24, antes de entrar na saturação do controlador, é igual à do PI original, pois

   [img:Illustration] 

  ou seja,

   [img:Illustration] 

  Após o tempo tf, com o aumento do sinal de saída da planta, o erro se torna negativo e o controlador sai da saturação. O sinal na entrada da planta fica valendo

   [img:Illustration] 

  Neste instante, a condição inicial da variável m2(t) encontra-se com valor M ≠ 0, que deve ser levado em conta. Para isso, considerando a equação diferencial correspondente ao bloco com entrada m*(t) e saída m2(t), tem-se que

   [img:Illustration] 

  Aplicando a transformada de Laplace na Equação (6.38) e supondo condição inicial M, obtém-se

   [img:Illustration] 

  Isolando a variável M2(s), tem-se que

   [img:Illustration] 

  A transformada de Laplace na Equação (6.37) produz

   [img:Illustration] 

  Isolando a variável M*(s), obtém-se

   [img:Illustration] 

  cuja transformada inversa de Laplace é

   [img:Illustration] 

  pois supõe-se que após o tempo tf, o erro e(t) se torna negativo.

  Como M << Mw, fica comprovada a ação antireset windup. Convém observar que o antireset windup é muito mais simples de realizar em computador ou em CLP (Controlador Lógico Programável), suprimindo a integração do sinal e(t) quando m(t) atinge o nível de saturação M. Além disso, a chamada forma de velocidade do algoritmo PID digital, da seção seguinte, elimina por si o disparo da referência.

  

#### 6.3.5 Algoritmo PID implementado em computador

  Diz-se que um computador opera em tempo real quando é capaz de aceitar medidas digitais no instante k, executar operações lógicas e cálculos preestabelecidos e apresentar os resultados no instante k + τ, τ > 0.

  Qualquer computador operando em tempo real pode realizar aproximadamente um controlador PID. Basta que seja programado para executar a equação de diferenças finitas que se aproxime da equação diferencial do algoritmo PID (ver Capítulo 11). Considerando o controlador PID sem a derivada do erro

   [img:Illustration] 

  a equação diferencial correspondente é

   [img:Illustration] 

  Supondo, como é frequente, que o tempo de cálculo τ é muito menor que o tempo T entre as interações com o processo controlado pode-se adotar como algoritmo PID digital

   [img:Illustration] 

  que é a chamada forma de posição, pois requer o cálculo do valor pleno de m(kT) a cada passo.

  A chamada forma de velocidade, que calcula apenas o incremento Δm(kT) a cada passo, é

   [img:Illustration] 

   [img:Illustration] 

  Esta forma exige um integrador adicional para reconstruir m(kT) a partir de Δm(kT), pois

   [img:Illustration] 

  e tem a vantagem de que, na hipótese de uma falha do computador ou de uma interrupção por emergência, no retorno ao funcionamento a variável m(kT) se encontrará no último valor válido, e não em zero. A forma de velocidade é de fato a forma preferida.

  

#### 6.3.6 Implementação analógica

  Com o avanço tecnológico dos computadores e dos equipamentos de processamento digital de sinais a implementação de controladores na forma digital está sendo cada vez mais utilizada na prática. Algumas vantagens da implementação digital sobre a analógica são: maior precisão dos cálculos1, implementação mais simples por meio de um programa computacional, fácil programação, menor interferência de ruído, maior grau de integração e compactação, entre outras. A única vantagem da implementação analógica é que como os processos em geral são analógicos não é necessário realizar a conversão digital. Apesar disso, muitas indústrias utilizam até hoje controladores que foram implementados analogicamente. Na Figura 6.25 são apresentados os circuitos eletrônicos com amplificadores operacionais de alguns controladores e na Tabela 6.1 são apresentadas as correspondentes funções de transferência.

  Tabela 6.1 Funções de transferência e parâmetros dos circuitos da Figura 6.25

   [img:Illustration] 

   [img:Illustration] 

  Figura 6.25 Circuitos eletrônicos com amplificadores operacionais de alguns controladores.

  

### 6.4 Exercícios resolvidos

  

### Exercício 6.1

  Considere o controle da posição do eixo de um motor CC, controlado pela armadura, acionando a junta de um braço de um robô da Figura 6.26.

   [img:Illustration] 

  Figura 6.26 Braços de robôs.

  O diagrama de blocos do sistema de controle correspondente, usando um controlador PD, é apresentado na Figura 6.27.

   [img:Illustration] 

  Figura 6.27 Diagrama de blocos do sistema de controle de um braço de um robô.

  a) Desenhe o lugar das raízes e determine os valores de TD de modo que a resposta ao degrau na referência seja sempre amortecida para ∀Kc > 0.

  b) Calcule o erro estacionário para um degrau unitário aplicado na referência r(t) e na perturbação d(t).

  c) Supondo TD = 1 e D(s) = 0, determine o valor de Kc de modo que a resposta ao degrau unitário na referência tenha um tempo de subida de tr = 1s.

  Solução

  a) Sendo  [img:Illustration]  então a função de transferência de malha aberta é

   [img:Illustration] 

  cujos polos são s = 0 e s = −1 e cujo zero é  [img:Illustration] 

  Dependendo do valor de TD são possíveis as alternativas mostradas na Figura 6.28 para o lugar das raízes.

   [img:Illustration] 

  Figura 6.28 Lugar das raízes. (a) TD < 1. (b) TD > 1. (c) TD = 1.

  A resposta transitória é amortecida para Kc > 0 quando os polos de malha fechada são reais. Isso ocorre nas Figuras 6.28 (b) e (c). Portanto, a especificação é satisfeita para TD ≥ 1.

  b) Para entradas do tipo degrau unitário na referência R(s) e na perturbação D(s) tem-se que

   [img:Illustration] 

  O erro estacionário pode ser calculado por meio do teorema do valor final. Aplicando-se um degrau unitário na referência (R(s) = 1/s), com D(s) = 0, tem-se que

   [img:Illustration] 

  Aplicando-se um degrau unitário de perturbação (D(s) = 1/s), com R(s) = 0, tem-se que

   [img:Illustration] 

  
    Importante

    Neste exemplo o erro estacionário para um degrau na referência resulta igual a zero devido ao polo na origem presente na planta, e não devido às características do controlador PD.

    Já o erro estacionário para um degrau na perturbação é diferente de zero mesmo com o polo da planta na origem.

  

  c) Para TD = 1 e D(s) = 0, a função de transferência de malha fechada resulta como

   [img:Illustration] 

  Para R(s) = 1/s, a transformada inversa de Y(s) é

   [img:Illustration] 

  O tempo de subida tr (rise time) de sistemas de primeira ordem é definido como o tempo para a resposta ao degrau ir de 10% a 90% do seu valor final (y(∞) = 1).

  Sendo t1 e t2 os instantes em que a resposta vale 0,1 e 0,9, respectivamente, então,

   [img:Illustration] 

  Dividindo a Equação (6.56) pela Equação (6.57), obtém-se

   [img:Illustration] 

  Como tr = t2 − t1 = 1, então,

   [img:Illustration] 

  A resposta ao degrau unitário na referência, com d(t) = 0, é apresentada na Figura 6.29.

   [img:Illustration] 

  Figura 6.29 Resposta ao degrau unitário na referência com d(t) = 0.

  

### Exercício 6.2

  Projete um controlador Gc(s) para o sistema da Figura 6.30, de modo que a resposta da saída y(t) do sistema em malha fechada para uma entrada do tipo degrau unitário na referência seja a mesma do gráfico da Figura 6.31.

   [img:Illustration] 

  Figura 6.30 Diagrama de blocos de um sistema em malha fechada.

   [img:Illustration] 

  Figura 6.31 Resposta ao degrau unitário na referência.

  Solução

  De acordo com a Figura 6.31, a resposta transitória tem um sobressinal

   [img:Illustration] 

  cujo coeficiente de amortecimento vale ξ ≅ 0,456.

  Do gráfico da Figura 6.31 tem-se que o tempo de pico da resposta vale

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  Para que as especificações de transitório sejam satisfeitas os polos de malha fechada devem estar localizados em

   [img:Illustration] 

  Como a planta não possui integrador e a resposta transitória possui erro estacionário nulo, pois e(∞) = 1 − y(∞) = 0, então o integrador deve estar no controlador.

  Supondo que o controlador Gc(s) seja um PI, então a função de transferência de malha aberta é dada por

   [img:Illustration] 

  Para que as especificações sejam satisfeitas o lugar das raízes deve passar pelos polos de malha fechada (6.63). Isso pode ser conseguido cancelando-se o zero do controlador em  [img:Illustration]  com o polo em s = −0,2 da planta. Com isso o lugar das raízes resulta como na Figura 6.32.

   [img:Illustration] 

  Figura 6.32 Lugar das raízes com o controlador PI.

  O valor do ganho Kc > 0 em qualquer ponto do lugar de raízes pode ser calculado por meio da condição de módulo, ou seja,

   [img:Illustration] 

  Portanto, a função de transferência do controlador PI é dada por

   [img:Illustration] 

  

### Exercício 6.3

  Projete um controlador Gc(s) para o sistema da Figura 6.33 de modo que a resposta da saída y(t) do sistema em malha fechada para uma entrada do tipo degrau na referência tenha:

  • sobressinal máximo de 16,3%;

  • tempo de acomodação de 4 s, segundo o critério de 2%;

  • erro estacionário nulo.

   [img:Illustration] 

  Figura 6.33 Diagrama de blocos de um sistema em malha fechada.

  Solução

  O primeiro passo consiste em converter as especificações de projeto nos correspondentes polos de malha fechada desejados. Para isso basta determinar os valores do coeficiente de amortecimento ξ e da frequência natural não amortecida ωn, que podem ser obtidos a partir do sobressinal Mp e do tempo de acomodação ts, respectivamente. Assim,

   [img:Illustration] 

  O tempo de acomodação, segundo o critério de 2%, é dado por

   [img:Illustration] 

  Para que as especificações de transitório sejam satisfeitas os polos de malha fechada devem estar localizados em

   [img:Illustration] 

  Como a planta possui um polo na origem, o controlador não necessita de integrador para que a resposta ao degrau na referência tenha erro estacionário nulo. Com um controlador proporcional, isto é, Gc(s) = Kc, é impossível satisfazer as especificações de transitório pois o lugar das raízes não passa pelos polos de malha fechada desejados (6.69), conforme se pode verificar na Figura 6.34.

   [img:Illustration] 

  Figura 6.34 Lugar das raízes com um controlador proporcional.

  Para deslocar o lugar das raízes para a esquerda do plano s pode-se empregar um controlador PD modificado

   [img:Illustration] 

  Para que o lugar das raízes passe pelos polos de malha fechada desejados basta cancelar o zero do controlador com o polo estável da planta. Para que isso ocorra basta escolher TD = 0,5 e adotar N = 1. Dessa forma a função de transferência de malha aberta é dada por

   [img:Illustration] 

  O valor do ganho Kc > 0 em qualquer ponto do lugar de raízes pode ser calculado por meio da condição de módulo, ou seja,

   [img:Illustration] 

  Como o sistema em malha fechada resultante é de segunda ordem, o ganho Kc também pode ser calculado por

   [img:Illustration] 

  Logo, 4Kc =  [img:Illustration]  ⇒ Kc = 1.

  Portanto, a função de transferência do controlador é

   [img:Illustration] 

  

### Exercício 6.4

  Projete um controlador PID para o levitador eletromagnético da Figura 6.35, de modo que os polos de malha fechada dominantes tenham coeficiente de amortecimento ξ = 0,5 e frequência natural ωn = 2 rad/s.

   [img:Illustration] 

  Figura 6.35 Diagrama de blocos do sistema em malha fechada.

  Solução

  Para que a especificação seja satisfeita os polos de malha fechada dominantes devem estar localizados em

   [img:Illustration] 

  Um dos zeros do controlador PID pode ser cancelado2 com o polo estável da planta, ou seja, s = –a = −1.

  A constante b pode ser determinada por meio da condição de fase, ou seja,

   [img:Illustration] 

  Para s = – +  [img:Illustration] j

   [img:Illustration] 

  ou

   [img:Illustration] 

  Na Figura 6.36 é mostrado o lugar das raízes para a = 1 e b = 1,33.

   [img:Illustration] 

  Figura 6.36 Lugar das raízes para a = 1 e b = 1,33.

  A constante K > 0 pode ser determinada por meio da condição de módulo

   [img:Illustration] 

  ou

   [img:Illustration] 

  Portanto, a função de transferência do controlador PID é

   [img:Illustration] 

  A função de transferência de malha fechada é

   [img:Illustration] 

  cujos polos são s1,2 = –1 ±  [img:Illustration] j.

  

### Exercício 6.5

  Determine a função de transferência do controlador PID modificado da Figura 6.37.

   [img:Illustration] 

  Figura 6.37 Circuito eletrônico de um controlador PID modificado.

  Solução

  A impedância Z1(s) vale

   [img:Illustration] 

  e a impedância Z2(s)

   [img:Illustration] 

  A função de transferência é dada por

   [img:Illustration] 

  ou

   [img:Illustration] 

  com R2C2 ≠ R1C1 e

   [img:Illustration] 

  

### Exercício 6.6

  Considere um processo industrial com função de transferência

   [img:Illustration] 

  Projete um controlador de modo que as seguintes especificações sejam satisfeitas:

  • erro estacionário nulo para entrada de referência do tipo degrau unitário;

  • margem de ganho de 10 dB.

  Solução

  Para que a resposta ao degrau unitário na referência tenha erro estacionário nulo a função de transferência de malha aberta deve possuir um integrador. Supondo que o controlador Gc(s) seja um PI, então a função de transferência de malha aberta é dada por

   [img:Illustration] 

  Cancelando o zero do controlador com polo da planta (TI = 1/3), então

   [img:Illustration] 

  cujos diagramas de Bode para Kc = 1 são apresentados na Figura 6.38.

   [img:Illustration] 

  Figura 6.38 Diagramas de Bode da função de malha aberta Gma(jω) para Kc = 1.

  Como a margem de ganho (MG ≅ −2,1 dB) e a margem de fase (MF ≅ −24,6o) são negativas, o sistema em malha fechada é instável. Para estabilizá-lo basta reduzir o ganho Kc, de modo que as margens de ganho e fase se tornem positivas.

  Para que o valor da margem de ganho seja 10 dB o ganho Kc deve ser reduzido de −12,1 dB.

  Assim,

   [img:Illustration] 

  Na Figura 6.39 são apresentados os diagramas de Bode da função de transferência de malha aberta para Kc = 0,248. Observe que MG = 10 dB e MF ≅ 61,6o. Logo, o sistema em malha fechada é estável.

   [img:Illustration] 

  Figura 6.39 Diagramas de Bode da função de malha aberta Gma(jω) para Kc = 0,248.

  Portanto, a função de transferência do controlador é

   [img:Illustration] 

  Na Figura 6.40 são apresentadas as respostas ao degrau unitário dos sistemas em malha aberta sem controlador e em malha fechada com controlador. Observe que no sistema em malha fechada com controlador o erro estacionário é nulo, pois a saída estacionária vale 1.

   [img:Illustration] 

  Figura 6.40 Respostas ao degrau unitário dos sistemas em malha aberta sem controlador e em malha fechada com controlador.

  

### 6.5 Exercícios propostos

  

### Exercício 6.7

  Uma mesma planta foi controlada pelos seguintes controladores: P, PD, PI, PID. Em todos os casos a sintonia dos controladores foi cuidadosamente ajustada tendo em vista os seguintes critérios:

  • Erro de regime ao degrau o menor possível.

  • Sobressinal o menor possível.

  • Ganhos não muito elevados para impedir a saturação da saída dos controladores.

  Na Figura 6.41 são apresentadas as respostas y(t) para degraus unitários aplicados na referência dos sistemas em malha fechada com cada um dos controladores considerados. Associe os gráficos aos controladores correspondentes e justifique sua escolha.

   [img:Illustration] 

  Figura 6.41 Respostas para degraus unitários aplicados na referência.

  

### Exercício 6.8

  Determine os valores das constantes K e a do controlador PID da Figura 6.42, de modo que o sistema em malha fechada tenha um coeficiente de amortecimento ξ = 0,4 e um tempo de acomodação ts = 1s (critério de 2%) quando é aplicado um degrau na referência.

   [img:Illustration] 

  Figura 6.42 Diagrama de blocos de um sistema em malha fechada com controlador PID.

  

### Exercício 6.9

  Projete um controlador Gc(s) para o sistema da Figura 6.43 de modo que a resposta da saída y(t) do sistema em malha fechada para uma entrada do tipo degrau unitário na referência seja a mesma do gráfico da Figura 6.44.

   [img:Illustration] 

  Figura 6.43 Diagrama de blocos de um sistema em malha fechada.

   [img:Illustration] 

  Figura 6.44 Resposta ao degrau unitário na referência.

  

### Exercício 6.10

  Projete um controlador PD modificado para o levitador eletromagnético da Figura 6.45 de modo que os polos de malha fechada dominantes tenham coeficiente de amortecimento ξ = 0,5 e frequência natural ωn = 2 rad/s. Suponha N entre 0,05 e 0,17.

   [img:Illustration] 

  Figura 6.45 Diagrama de blocos do sistema em malha fechada com controlador PD modificado.

  

### Exercício 6.11

  Mostre que as funções de transferência dos controladores da Figura 6.25 correspondem às funções apresentadas na Tabela 6.1.

  

### Exercício 6.12

  Projete um controlador Gc(s) para o sistema da Figura 6.46 de modo que a resposta da saída y(t) do sistema em malha fechada para uma entrada do tipo degrau na referência tenha:

  • sobressinal máximo de 10%;

  • tempo de subida de 0,2 s;

  • erro estacionário nulo.

   [img:Illustration] 

  Figura 6.46 Diagrama de blocos de um sistema em malha fechada.

  

### Exercício 6.13

  Projete um controlador PID para a planta da Figura 6.47 de modo que os polos de malha fechada dominantes estejam localizados em s1,2 = −1 ±  [img:Illustration] j.

   [img:Illustration] 

  Figura 6.47 Diagrama de blocos do sistema em malha fechada.

  

### Exercício 6.14

  Considere a planta com função de transferência

   [img:Illustration] 

  a) Projete um controlador proporcional de modo que a margem de ganho seja de 10 dB.

  b) Projete um controlador proporcional de modo que a margem de fase seja de 40o.

  c) Projete um controlador PD modificado de modo que a margem de ganho seja de 10 dB e a margem de fase seja de 40o.

  

### Exercício 6.15

  Considere um processo de fundição para a produção de barras de alumínio3 cuja função de transferência é

   [img:Illustration] 

  Projete um controlador de modo que as seguintes especificações sejam satisfeitas:

  • erro estacionário nulo para entrada de referência do tipo degrau unitário;

  • margem de ganho de 10 dB.

  

  __________

  1A precisão dos cálculos analógicos depende da precisão limitada de componentes eletrônicos, enquanto a precisão dos cálculos digitais depende da quantidade de circuitos de chaveamento.

  2Não se deve cancelar polos instáveis, pois na prática o cancelamento pode não ser perfeito e o sistema em malha fechada resultante pode ser instável.

  3Ver Exercício 9.3.

<!-- Text/chapter07.xhtml -->

  
  Controle Automático, 2ª edição
  
  

  

## 7

  

## Controle de Processos

  

### 7.1 Introdução

  Os processos industriais caracterizam-se usualmente por:

  • grandes dimensões físicas;

  • importantes atrasos puros;

  • constantes de tempo longas (de minutos a horas);

  • elevados coeficientes de amortecimento (devido às importantes perdas energéticas);

  • forte interação entre malhas de controle (inerente ao próprio processo);

  • não linearidades importantes ("suaves").

  O controle de tais processos é tradicionalmente chamado de Controle de Processos, em oposição ao controle de posição e velocidade nos sistemas mecânicos, genericamente designado por Controle de Posição. Além disso, no ambiente industrial alguns termos foram adotados para designar as variáveis e os coeficientes dos modelos dos sistemas a realimentação, termos esses diferentes dos adotados na intensa atividade de pesquisa teórica em controle. Termos como reset gain e rate gain permanecem como linguagem obrigatória na comunicação industrial.

  Neste capítulo são introduzidos os termos e símbolos da ISA (International Society of Automation) e, sempre que possível, os esquemas de controle ISA são reproduzidos como diagramas de blocos. Também são apresentadas as importantes regras de Ziegler e Nichols, que permitem as sintonias dos PIDs em campo e as regras SIMC (Skogestad Internal Model Control), que são muito eficientes porque admitem atraso puro no modelo da planta.

  Também são fundamentais certas arquiteturas com base no controlador PID:

  • contra perturbações ao processo: conexão de malhas em cascata (cascade control) e alimentação avante (feedforward);

  • contra não linearidades "suaves": controle de razão e ganho adaptativo (gain scheduling).

  Após 1960 a indústria sentiu a necessidade de um outro tipo de controle automático, o controle lógico dos eventos discretos, visando realizar a automatização das operações nas manufaturas, das partidas dos processos industriais, das suas proteções e dos programas de produção em batelada. Por isso, e perante as potencialidades dos computadores, a General Motors em dado momento especificou as características básicas de um computador industrial: teria de ser fisicamente robusto e especializado para executar regras de natureza temporal e lógica. Esta foi a origem do Controlador Lógico Programável (CLP), equipamento que alcançou enorme sucesso e que desde logo incorporou também a capacidade de realizar digitalmente os controladores PID.

  

### 7.2 Ajuste por Ziegler-Nichols no domínio da frequência

  Na prática industrial é muitas vezes necessário ajustar os parâmetros de um controlador no campo sem prévios modelos matemáticos e cálculos. Para tal fim, John G. Ziegler e Nathaniel B. Nichols [56] desenvolveram técnicas que, além de eficaz em muitos casos de processos químicos, térmicos, etc., têm a vantagem de abranger peculiaridades e parâmetros parasitas que os modelos matemáticos raramente incorporam. Seu inconveniente é exigir que o sistema real seja levado por algum tempo ao limiar da estabilidade, com o apreciável custo da perda de produção. A seguir são apresentados os passos de ajuste de dois métodos propostos por Ziegler e Nichols.

  

#### 7.2.1 Primeiro método

  Este experimento deve ser realizado com o sistema em malha fechada. Os passos para ajuste dos ganhos do controlador são os seguintes:

   

  passo 1: ajuste TD e 1/TI do controlador P+I+D em zero;

  passo 2: aumente lentamente o ganho Kc até que a saída do sistema oscile periodicamente. Se isso não ocorrer, o método não se aplica;

  passo 3: seja Ku o ganho final e Pu o período da oscilação (Figura 7.1); passo 4: ajuste os parâmetros do controlador de acordo com a Tabela 7.1.

   [img:Illustration] 

  Figura 7.1 Oscilação periódica da saída y(t) de um sistema.

  Tabela 7.1 Regras de ajuste para o primeiro método de Ziegler-Nichols

  
    
      
        

        

        

        
      

      
        
          
            Tipo de controlador

          

          
            Kc

          

          
            1/TI

          

          
            TD

          
        

        
          
            P

          

          
            0,5Ku

          

          
            0

          

          
            0

          
        

        
          
            PD

          

          
            0,6Ku

          

          
            0

          

          
            Pu/8

          
        

        
          
            PI

          

          
            0,45Ku

          

          
            1,2/Pu

          

          
            0

          
        

        
          
            PID

          

          
            0,6Ku

          

          
            2/Pu

          

          
            Pu/8

          
        

      
    
  

  

#### 7.2.2 Segundo método

  Este experimento também deve ser realizado com o sistema em malha fechada. Os passos para ajuste dos ganhos do controlador são os seguintes:

   

  passo 1: ajuste TD e 1/TI do controlador P+I+D em zero;

  passo 2: aumente lentamente o ganho Kc até que a saída do sistema oscile periodicamente. Se isso não ocorrer, o método não se aplica;

  passo 3: reduza o ganho Kc à metade;

  passo 4: diminua TI até que a saída do sistema oscile periodicamente;

  passo 5: duplique o valor de TI ;

  passo 6: ajuste TD = TI.

  

### Exemplo 7.1

  Considere o sistema de controle da Figura 7.2, para o qual é aplicado o segundo método de Ziegler-Nichols para ajuste dos parâmetros do controlador PID.

   [img:Illustration] 

  Figura 7.2 Sistema em malha fechada com controlador PID.

  No passo 1 faz-se TD = 0 e TI = 10000, de forma que 1/TI seja próximo de zero. No passo 2 aumenta-se Kc até 48,5, quando a margem de fase é igual a zero e a saída do sistema em malha fechada começa a oscilar. No passo 3 o valor de Kc é então reduzido à metade, ou seja, para Kc = 24,25. Na Figura 7.3 são mostrados os gráficos de Bode correspondentes aos passos 2 e 3.

   [img:Illustration] 

  Figura 7.3 Diagramas de Bode para TD = 0 e TI = 10000, com Kc = 48,5 e Kc = 24,25.

  Na Figura 7.4 é mostrada a resposta do sistema em malha fechada para um degrau unitário na referência, com os parâmetros do controlador ajustados em Kc = 24,25, TD = 0 e TI = 10000. Como o sistema está perto da instabilidade a resposta transitória é subamortecida, com sobressinal elevado (Mp ≅ 65%). É interessante observar que nesta fase do ajuste o PID atua como um controlador proporcional. Este fato justifica o erro estacionário e(∞) = 1−y(∞) ≅ 1−0,92 ≅ 0,08.

  No passo 4 diminui-se o valor de TI até TI = 1,1, quando a margem de fase fica novamente igual a zero e o sistema volta a oscilar. No passo 5 este valor é então duplicado, ou seja, para TI = 2,2. Na Figura 7.5 são mostrados os gráficos de Bode correspondentes aos passos 4 e 5.

   [img:Illustration] 

  Figura 7.4 Resposta ao degrau unitário para Kc = 24,25, TD = 0 e TI = 10000.

   [img:Illustration] 

  Figura 7.5 Diagramas de Bode para Kc = 24,25 e TD = 0, com TI = 1,1 e TI = 2,2.

   [img:Illustration] 

  Figura 7.6 Resposta ao degrau unitário para Kc = 24,25, TD = 0 e TI = 2,2.

  Na Figura 7.6 é apresentada a resposta do sistema em malha fechada para um degrau unitário na referência e os parâmetros ajustados em Kc = 24,25, TD = 0 e TI = 2,2. O efeito do integrador fica evidente com o erro estacionário nulo. Porém, o sobressinal é elevado (Mp ≅ 75%) devido aos baixos valores das margens de estabilidade (MG ≅ 3 dB e MF ≅ 8o).

  No passo 6 faz-se TD = TI = 2,2. Os gráficos de Bode correspondentes são apresentados na Figura 7.7. Note que as margens de estabilidade são agora satisfatórias (MG infinita e MF ≅ 40o).

   [img:Illustration] 

  Figura 7.7 Diagramas de Bode para Kc = 24,25 e TD = TI = 2,2.

  Na Figura 7.8 é apresentada a resposta do sistema em malha fechada para um degrau unitário na referência e os parâmetros ajustados em Kc = 24,25 e TD = TI = 2,2. É evidente o amplo efeito de equalização do compensador final, gerando boa estabilidade pelas margens e bons transientes pela banda de passagem (sobressinal Mp ≅ 24%).

   [img:Illustration] 

  Figura 7.8 Resposta ao degrau unitário para Kc = 24,25 e TD = TI = 2,2.

  

### 7.3 Ajuste por Ziegler-Nichols no domínio do tempo

  Em muitas aplicações industriais, a resposta ao degrau em malha aberta de um processo estável apresenta o aspecto de uma curva em forma de um "S" semelhante à da Figura 7.9, que é chamada curva de reação.

   [img:Illustration] 

  Figura 7.9 Resposta ao degrau em malha aberta de um sistema estável.

  Se a saída y(t) do processo apresentar um gráfico semelhante ao da Figura 7.9, então o modelo do processo pode ser aproximado por um sistema de primeira ordem com função de transferência

   [img:Illustration] 

  sendo que K é o ganho, T é a constante de tempo e L é o atraso de transporte.

  Traçando-se uma reta tangente ao ponto de inflexão da curva de reação, obtém-se no instante inicial o parâmetro a. Já o parâmetro L consiste no atraso de tempo a partir do qual o sistema começa a responder. A partir das medidas de a e L, Ziegler e Nichols propuseram em [56] ajustar os parâmetros do controlador PID de acordo com a Tabela 7.2.

  Tabela 7.2 Regras de ajuste de Ziegler-Nichols para o método da curva de reação.

  
    
      
        

        

        

        
      

      
        
          
            Tipo de controlador

          

          
            Kc

          

          
            1/TI

          

          
            TD

          
        

        
          
            P

          

          
            1/a

          

          
            0

          

          
            0

          
        

        
          
            PI

          

          
            0,9/a

          

          
            0,3/L

          

          
            0

          
        

        
          
            PID

          

          
            1,2/a

          

          
            0,5/L

          

          
            0,5L

          
        

      
    
  

  

### 7.4 Sintonia automática de controladores PID

  Para ajustar o controlador PID de acordo com os métodos das Seções 7.2.1 e 7.2.2 é necessário aumentar o ganho Kc até que a saída do sistema oscile periodicamente. Esse procedimento tem um inconveniente indesejável em muitas aplicações industriais que é o de levar a saída do processo para próximo da instabilidade.

  Uma método alternativo para ajuste dos parâmetros do controlador PID é o da sintonia automática baseada no método do relé, que consiste na inclusão de um relé com histerese na malha de realimentação de acordo com a Figura 7.10. Esta inclusão faz com que a saída do processo oscile dentro de um ciclo limite, o que equivale a aplicar na entrada do processo um sinal com frequência próxima daquela em que ocorrem o cruzamento em 0 dB e margem de fase 0o.

   [img:Illustration] 

  Figura 7.10 Diagrama de blocos da sintonia automática de um controlador PID usando um relé com histerese.

  Observe que na Figura 7.10 há uma chave que permite escolher entre o relé e o controlador PID. Quando for necessário sintonizar o controlador PID basta fechar a malha utilizando o relé. Caso o sistema apresente uma oscilação sustentada na saída, o sinal u(t) será uma onda quadrada com amplitude d com o mesmo período e fase oposta a y(t). A largura b da histerese pode ser ajustada com base no nível de ruído da malha e é útil para evitar um chaveamento indevido do relé. Se a saída do processo apresentar uma oscilação periódica deve-se medir a amplitude a e o período Pu da oscilação, conforme a Figura 7.11.

   [img:Illustration] 

  Figura 7.11 Saída do processo com oscilação periódica e amplitude sustentada.

  O ganho Ku é determinado por meio de uma aproximação da função descritiva do relé, obtida por meio da expansão em série de Fourier de uma onda quadrada [35], ou seja,

   [img:Illustration] 

  A partir do ganho Ku e do período Pu, os parâmetros Kc, Ti e Td do controlador PID são ajustados de acordo com a Tabela 7.1. Uma vez determinados esses parâmetros, a chave pode então ser trocada automaticamente da posição do relé para o controlador PID.

  

### 7.5 Ajuste SIMC - Skogestad Internal Model Control

  Em controle de processos industriais de escala média ou grande é comum o modelo da planta constituir-se aproximadamente de um atraso puro e de uma função de transferência de primeira ou de segunda ordem usualmente superamortecida.

  Conforme foi visto na Seção 5.5, a função de transferência de um atraso puro é e−αs. A defasagem é igual a −αω, mas no gráfico de fase de Bode, que é semilogarítmico, a defasagem diminui muito rapidamente acima da frequência ω. O efeito é sempre instabilizante na malha de controle. Além disso não existe sistema físico que compense um atraso puro, pois a função de transferência inversa não é fisicamente realizável.

  Skogestad [53] deduziu várias regras muito simples e eficazes para o ajuste do controlador PID, a partir da idéia do controlador com modelo interno (Internal Model Control - IMC). A seguir são apresentadas duas dessas regras.

  

#### 7.5.1 Regra SIMC 1

  Seja a planta de primeira ordem

   [img:Illustration] 

  e se deseje a seguinte função de transferência de malha fechada

   [img:Illustration] 

  aceitando o fato de que o atraso puro não pode ser eliminado.

  Para degraus de referência e de perturbação sobre a planta utilize o controlador PI

   [img:Illustration] 

  com

   [img:Illustration] 

  e

   [img:Illustration] 

  O autor da regra recomenda escolher τc = α. O Exemplo 7.2 mostra o efeito de escolher τc = α e τc = 2α sobre a resposta ao degrau.

  

### Exemplo 7.2

  Calcule um controlador PI, usando a regra SIMC 1, para o sistema da Figura 7.12.

   [img:Illustration] 

  Figura 7.12 Sistema em malha fechada.

  A função de transferência da planta é

   [img:Illustration] 

  Comparando as Equações (7.3) e (7.8) obtêm-se K = 1, τ = 10 e α = 1.

  • Supondo τc = α, as constantes do controlador PI são

   [img:Illustration] 

  e

   [img:Illustration] 

  Portanto, o controlador PI é

   [img:Illustration] 

  • Supondo τc = 2α, as constantes do controlador PI são

   [img:Illustration] 

  e

   [img:Illustration] 

  Portanto, o controlador PI é

   [img:Illustration] 

  Na Figura 7.13 são apresentadas as respostas ao degrau unitário na referência com o controlador PI para τc = α e para τc = 2α, e a resposta ao degrau unitário do sistema em malha aberta sem controlador. Comparando as respostas verifica-se que a resposta transitória sem controlador é bem mais lenta que as respostas com controlador. A resposta com o controlador PI para τc = α tem um pequeno sobressinal, porém é mais rápida que a resposta com o controlador PI para τc = 2α.

   [img:Illustration] 

  Figura 7.13 Resposta ao degrau unitário.

  

#### 7.5.2 Regra SIMC 2

  Seja a planta de segunda ordem com polos reais

   [img:Illustration] 

  O controlador recomendado pela regra SIMC 2 é um PID modificado

   [img:Illustration] 

  com

   [img:Illustration] 

  O autor da regra recomenda escolher τc = α para respostas rápidas e τc > α para maior robustez.

  

### 7.6 Termos e símbolos ISA

  Nesta seção são apresentados os termos correntes em controle de processos industriais aprovados pelas normas ISA (International Society of Automation), assim como sua relação com os termos correntes na teoria de controle dinâmico. Também são introduzidos alguns símbolos da norma usados para documentar a instrumentação conhecida pela sigla P&ID (Piping and Instrumentation Diagram), que é um diagrama esquemático de tubulações, equipamentos e conexões de instrumentação.1

  

#### 7.6.1 Termos ISA

  • Set-point (sinal de referência)

  Valor da variável de referência r(t) do sistema. O nome pressupõe, como é de fato comum no ambiente de processos contínuos industriais, que o objetivo do controle é regular ou estabilizar a variável de saída em torno de um valor fixo.

  • Off-set

  Diferença de valor entre a variável de referência e a de saída em regime estacionário. Corresponde ao erro atuante estacionário e(∞) e pode ser enunciado em porcentagem ou em per-unit.

  • Banda Proporcional (BP)

  É definida como a porcentagem de excursão total da variável de saída y(t) da planta, necessária para provocar uma variação total de 0 a 100% da variável manipulada m(t) (Figura 7.14).

  A banda proporcional exprime o alcance do funcionamento linear do sistema em termos de variação da saída da planta.

   [img:Illustration] 

  Figura 7.14 Diagrama de blocos de um sistema de controle com atuador e transdutor.

  A Figura 7.15 mostra que uma variação da saída y(t) entre 30% e 70% do seu valor máximo produz uma variação da variável manipulada m(t) entre 0% e 100%, implicando assim uma banda proporcional de 40%.

   [img:Illustration] 

  Figura 7.15 Banda proporcional.

  Supondo que Gc(s) seja um controlador PID com função de transferência

   [img:Illustration] 

  então a banda proporcional é dada por

   [img:Illustration] 

  • Tempo TR de avanço de rampa (rate time)

  O tempo de avanço de rampa se aplica aos controladores PD e PID. É o avanço temporal TR que o termo derivador produz na saída m(t) do controlador para uma entrada e(t) do tipo rampa.

  A função de transferência de um controlador PD é dada por

   [img:Illustration] 

  Aplicando-se uma rampa e(t) = At na entrada do controlador, tem-se que

   [img:Illustration] 

  cuja resposta temporal é

   [img:Illustration] 

  A resposta temporal m(t) está representada na Figura 7.16, cuja inclinação vale arctan(KcA).

  Logo,

   [img:Illustration] 

  Portanto, TR = TD.

   [img:Illustration] 

  Figura 7.16 Efeitos das ações P e D para uma rampa de entrada num controlador PD.

  • Tempo TS de duplicação (reset time)

  O tempo de duplicação se aplica aos controladores PI e PID. É o intervalo temporal necessário para que a saída m(t) do controlador varie por ação integral tanto quanto varia por ação proporcional em resposta a um degrau na variável de entrada e(t).

  A função de transferência de um controlador PI é dada por

   [img:Illustration] 

  Aplicando-se um degrau de amplitude A na entrada e(t) do controlador, tem-se que

   [img:Illustration] 

  cuja resposta temporal é

   [img:Illustration] 

  A resposta temporal m(t) está representada na Figura 7.17, cuja inclinação vale arctan  [img:Illustration] .

  Logo,

   [img:Illustration] 

  Portanto, TS = TI.

   [img:Illustration] 

  Figura 7.17 Efeitos das ações P e I para um degrau na entrada de um controlador PI.

  

#### 7.6.2 Símbolos da ISA

  Fisicamente os três elementos fundamentais de qualquer sistema a realimentação são o transdutor da saída, o controlador (somador mais amplificador, com compensação dinâmica) e o atuador. Sabe-se que todos os elementos da malha aberta influem na estabilidade e na qualidade do controle, mas são certamente os componentes do processo controlado que têm prioridade na comunicação entre os engenheiros industriais, de várias especialidades, e os instrumentistas que instalam e mantêm os equipamentos.

  Por ser comum que uma unidade industrial tenha milhares de transdutores, sensores, atuadores e controladores, a ISA (International Society of Automation) padronizou os símbolos desses equipamentos enfatizando os modos de montagem e disciplinando sua designação e listagem. Os símbolos da ISA são mais expressivos das conexões físicas do que das relações de causa e efeito e das dinâmicas dos processos. São menos informativos para o projetista de algoritmos de controle, mas o conhecimento deles é recomendável por uma questão de comunicação técnica.

  Devido à universalidade das representações ISA e de diagrama de blocos a maioria dos temas que se seguem neste capítulo é mostrada por meio das duas.

  • Normas da ISA

  
    Círculos representam transdutores, calculadores ou controladores.

    Linhas cheias representam comunicação física e transmissão de sinal.

    Linhas tracejadas representam a comunicação entre controlador e atuador.

    A primeira letra dos códigos dos círculos refere-se, em geral, à natureza da variável física.

    A segunda letra dos códigos dos círculos refere-se à função do elemento.

  

  Na Tabela 7.3 são apresentados alguns códigos dessa simbologia.

  Tabela 7.3 Símbolos da ISA

   [img:Illustration] 

  Exemplos:

  TC: controlador de temperatura;

  FV : válvula que comanda entrada de fluxo;

  FC: controlador de fluxo.

  Na Figura 7.18 são apresentados mais alguns símbolos de instrumentação e sinais da norma P&ID.

   [img:Illustration] 

  Figura 7.18 Símbolos de instrumentação e sinais da norma P&ID.

  

### 7.7 Arquitetura em cascata (cascade control)

  A arquitetura em cascata é um dos mais importantes métodos para aperfeiçoar um sistema de controle. Este método utiliza dois controladores padronizados PID e mede duas variáveis do sistema. Para explicá-lo, considere um exemplo de processo industrial típico [37].

  

### Exemplo 7.3

  Considere o tanque de aquecimento por circulação de óleo quente da Figura 7.19, cujo objetivo é controlar a temperatura y(t). Há três perturbações no processo: a vazão de entrada do produto e a sua temperatura, que estão representadas pela variável p(t), e a pressão p0(t) do reservatório de óleo quente.

   [img:Illustration] 

  Figura 7.19 Esquema P&ID de tanque aquecido com controlador PID simples.

  Na Figura 7.19 têm-se os seguintes símbolos da ISA:

  TC: transdutor e controlador de temperatura;

  TI: indicador de temperatura e

  FV : eletroválvula de controle da vazão de óleo para o tanque.

  Um transdutor e controlador PID simples mede a temperatura y(t) do fluido que sai e atua sobre o sinal elétrico m(t), que aciona a eletroválvula de admissão de óleo. A Figura 7.19 mostra esse sistema pelo esquema da instrumentação da ISA, e a Figura 7.20 pela forma de diagrama de blocos. Para concentrar a atenção na perturbação p0(t), pois esta é a principal fonte de perturbação que altera a taxa de aquecimento, a Figura 7.20 não mostra a perturbação p(t).

   [img:Illustration] 

  Figura 7.20 Diagrama de blocos da Figura 7.19 com controlador PID simples.

  O esquema da ISA da Figura 7.19 é graficamente mais simples e mais próximo do que os técnicos de montagem de instrumentação industrial precisam. Já o esquema na forma de diagrama de blocos da Figura 7.20 é mais valioso para a análise dinâmica do sistema e para o projeto do controlador. Os blocos H(s), Gc(s) e o comparador são internos ao controlador TC. O bloco Gp(s) representa a dinâmica da eletroválvula FV e do tanque de aquecimento até a temperatura de saída Y(s). Já o bloco G2(s) representa a dinâmica da pressão de óleo P0(s) até a temperatura de saída Y(s) do produto.

  Quando a pressão p0(t) de óleo aumenta o calor transferido para o tanque é maior, aumentando com isso a temperatura y(t) do tanque. Assim, o controlador reduz a abertura da válvula para compensar o aumento de temperatura. Quando o efeito da perturbação da pressão de óleo é compensado por um controle com realimentação simples a resposta é lenta, pois primeiro a temperatura do tanque deve ser perturbada para que depois o controlador possa responder.

  O controle cascade faz uma medida adicional de uma variável do processo, que é utilizada para compensar a ocorrência de uma perturbação. Neste exemplo a variável medida é o fluxo de óleo quente y′(t), cuja vantagem é que a malha de controle de fluxo é rápida com relação à dinâmica da planta, e assim a correção das variações da pressão do óleo ocorre muito antes de haver efeitos sobre a temperatura y(t) do tanque. Usualmente chama-se a malha mais lenta, de controle da saída do processo, de principal, e a outra malha, que é rápida, de secundária.

  O controle cascade deste sistema está esquematizado na forma P&ID na Figura 7.21 e na forma de diagrama de blocos na Figura 7.22. O ponto fundamental é que a variável de saída m(t) do controlador de temperatura TC da Figura 7.19 passa a ser o set-point ou o sinal de referência r′(t) para o controlador do fluxo de óleo FC na Figura 7.21.

   [img:Illustration] 

  Figura 7.21 Esquema P&ID de tanque aquecido com controle cascade.

  Na Figura 7.21 têm-se os seguintes símbolos da ISA:

  TC: transdutor e controlador de temperatura;

  TI: indicador de temperatura;

  FV : eletroválvula de controle da vazão de óleo para o tanque; e

  FC: controlador de fluxo.

  No diagrama de blocos da Figura 7.22 os blocos Gc(s), H(s) e o comparador da malha externa fazem parte do controlador TC. Já os blocos Gc′(s), H′(s) e o comparador da malha interna representam o controlador de fluxo FC. O bloco G1(s) é a função de transferência do fluxo de óleo Y′(s) até a temperatura de saída Y(s). O bloco G1′(s) representa a dinâmica da eletroválvula FV do sinal M′(s) até o fluxo de óleo Y′(s). O bloco G2′(s) representa a dinâmica da pressão do reservatório de óleo P0(s) até o fluxo de óleo Y′(s).

   [img:Illustration] 

  Figura 7.22 Diagrama de blocos da Figura 7.21 com controle cascade.

  Observações:

  • A propriedade do processo que enseja a aplicação da arquitetura cascade com sucesso é ser a malha secundária mais rápida.

  • Este fato também facilita a sintonia independente dos dois controladores PID.

  Considerando a diferença de faixas de passagem das duas malhas no diagrama de blocos da Figura 7.22, é adequado fazer a seguinte análise simplificada: passado o transitório da malha secundária, que é rápida, pode-se considerar o seu erro atuante pequeno e, portanto, válidas as expressões

   [img:Illustration] 

  

#### 7.7.1 Projeto de controlador em cascata

  • Projetar pelas regras SIMC os controladores de malha simples, com base na Figura 7.20, e cascade, com base na Figura 7.22, supondo que

   [img:Illustration] 

  Gp(s) = G(s)G1(s) e H(s) = H′(s) = G2′(s) = 1.

  • Comparar o desempenho dos dois sistemas de controle por meio das respostas a um degrau unitário na referência r(t) e na perturbação da pressão de óleo p0(t).

  • Examinar a robustez dos controladores projetados por meio de uma resposta a um degrau na referência r(t), supondo que a planta G1(s) tenha um aumento de 20% no atraso nominal. Para isso, considere p0(t) = 0 e troque a função de transferência (7.33) por

   [img:Illustration] 

  • Examinar a robustez dos controladores projetados por meio de uma resposta a um degrau na perturbação da pressão de óleo p0(t), supondo que a planta G1(s) tenha um aumento de 20% na constante de tempo e uma diminuição de 10% no ganho. Para isso, considere r(t) = 0 e troque a função de transferência (7.33) por

   [img:Illustration] 

  

### Projeto de controlador PID simples

  A função de transferência da planta é dada por

   [img:Illustration] 

  que é uma função de transferência de segunda ordem amortecida.

  Da regra SIMC 2 tem-se que

   [img:Illustration] 

  Logo, K = 1, α = 0,9, τ1 = 0,1 e τ2 = 1.

  Escolhendo τc = 2α, os parâmetros do controlador PID são

   [img:Illustration] 

  Assim, a função de transferência do controlador PID é

   [img:Illustration] 

  

### Projeto de controlador PI para a malha interna (rápida)

  Para um sistema de controle cascade, como na Figura 7.22, para a malha interna (rápida) tem-se uma planta de primeira ordem. Da regra SIMC 1 tem-se que

   [img:Illustration] 

  com K = 1, α = 0,1 e τ = 0,1.

  Escolhendo τc = 2α, os parâmetros do controlador PI são

   [img:Illustration] 

  e

   [img:Illustration] 

  Assim, a função de transferência do controlador PI é

   [img:Illustration] 

  

### Projeto de controlador PI para a malha externa (lenta)

  Supondo, por facilidade, que a função de transferência da malha fechada interna é mais rápida que a da malha externa, então, após o transitório,

   [img:Illustration] 

  Sendo a planta de primeira ordem, da regra SIMC 1 tem-se que

   [img:Illustration] 

  com K = 1, α = 0,8 e τ = 1.

  Escolhendo τc = 2α, os parâmetros do controlador PI são

   [img:Illustration] 

  Assim, a função de transferência do controlador PI é

   [img:Illustration] 

  

### Efeito dinâmico dos controladores cascade e PID

  As respostas ao degrau unitário na referência r(t) e na perturbação da pressão de óleo p0(t) são apresentadas nas Figuras 7.23 e 7.24, respectivamente. Observa-se que na Figura 7.23 não há diferença significativa entre as respostas, enquanto na Figura 7.24 a influência do sinal de perturbação na saída é bem menor com o controlador cascade.

   [img:Illustration] 

  Figura 7.23 Resposta ao degrau unitário na referência r(t), com p0(t) = 0.

   [img:Illustration] 

  Figura 7.24 Resposta ao degrau unitário de perturbação na pressão p0(t), com r(t) = 0.

  

### Análise de robustez para variações de parâmetros no modelo da planta

  As Figuras 7.25 e 7.26 mostram a influência de um aumento de 20% no atraso nominal da planta G1(s) sobre a resposta ao degrau unitário na referência para os esquemas de controle PID e cascade, respectivamente. Conforme pode-se perceber, em ambos os esquemas ocorreu uma boa robustez com relação à variação desse parâmetro.

   [img:Illustration] 

  Figura 7.25 Resposta ao degrau unitário na referência r(t) com controlador PID.

   [img:Illustration] 

  Figura 7.26 Resposta ao degrau unitário na referência r(t) com controlador "cascade".

  A Figura 7.27 mostra a influência de um aumento de 20% na constante de tempo e uma diminuição de 10% no ganho da planta G1(s) sobre as respostas a um degrau de perturbação na pressão de óleo para os controladores PID e cascade. Assim como nos resultados com atraso nominal, mostrados na Figura 7.24, também aqui tem-se um melhor desempenho com o controlador cascade.

   [img:Illustration] 

  Figura 7.27 Resposta ao degrau unitário na perturbação da pressão de óleo p0(t).

  

#### 7.7.2 Controlador em cascata para reduzir não linearidades

  Uma das aplicações interessantes do sistema cascade é na redução, que pode ser drástica, dos comportamentos não lineares de válvulas de controle de processo. Devido ao atrito seco elevado as válvulas frequentemente "colam" e subitamente "saltam" para posições excessivas, traduzindo-se em zonas mortas2 de até 30% e em oscilações da malha em que estão inseridas. O problema pode ser muito reduzido instalando-se uma malha secundária de cascade em torno da válvula com um controlador apenas do tipo proporcional (P), com alto ganho Kc. Este controlador é usualmente chamado de "posicionador de válvula".

   [img:Illustration] 

  Figura 7.28 (a) Esquema ISA. (b) Diagrama de blocos.

  Na Figura 7.28 são apresentados os esquema ISA e o diagrama de blocos do sistema de controle. O controlador de temperatura TC informa a posição desejada rv(t) da válvula, e o controlador de tensão EC amplifica o sinal de erro atuante até que a válvula "descole" da zona morta. Pode ocorrer uma oscilação da válvula em alta frequência, em relação à dinâmica do processo, o que não prejudica o controle propriamente dito.

  

### 7.8 Alimentação avante (feedforward control)

  Esta técnica tem semelhança com a do cascade apenas no sentido de que serve para reduzir efeitos de perturbações mais graves, auxiliando o controle da realimentação principal. E tem a fundamental diferença de que não acrescenta malha de realimentação secundária ao sistema, pois é um mecanismo de malha aberta. Apesar de os textos de controle a realimentação darem pouca importância, a alimentação avante ou feedforward control é antiga e fundamental na engenharia de controle.

  A alimentação avante baseia-se em medir diretamente uma perturbação, amplificar, transformar o sinal e adicioná-lo à entrada do processo, de forma que seja anulado o efeito daquela perturbação na variável de saída do processo. O cancelamento não precisa ser perfeito, pois a malha de realimentação é que dá qualidades de precisão ao sistema.

  Já foi dito que diante do desafio de regular uma unidade industrial ou um processo qualquer de natureza nova o engenheiro deve primeiro examinar se é possível conceber alguma alimentação avante e, em caso afirmativo, analisar a viabilidade de instalação. Somente depois é que devem ser realizados ensaios para estimar modelos dinâmicos e desenvolver o controle a realimentação. Há casos de equipamentos em que é virtualmente impossível obter o desempenho desejado sem o feedforward, como, por exemplo, nos reguladores de tensão dos geradores de energia elétrica, em que a perturbação medida é a corrente solicitada pela carga do gerador.

  

#### 7.8.1 Projeto de controlador feedforward

  As Figuras 7.29 e 7.30 mostram, respectivamente, o esquema ISA e o diagrama de blocos de um tanque aquecedor. O objetivo é manter a temperatura de saída y(t) próxima da referência r(t). Neste exemplo a pressão de óleo p0(t), com dinâmica mais rápida que a planta, não varia significativamente, de modo que não é necessário implementar um controle cascade composto por uma malha secundária de realimentação.

  Porém, a temperatura de entrada te(t) varia com amplitude e velocidades excessivas, suficientes para perturbar a temperatura de saída y(t). O objetivo é projetar um controlador feedforward que reduza o efeito da perturbação da temperatura de entrada te(t).

   [img:Illustration] 

  Figura 7.29 Esquema P&ID de tanque aquecido com controle feedforward.

  Na Figura 7.29 têm-se os seguintes símbolos da ISA:

  TC: transdutor e controlador de temperatura;

  FV : eletroválvula de controle da vazão de óleo quente;

  TI: medidor de temperatura;

  TY 1: calculador, que realiza a função de transferência feedforward;

  TY 2: somador.

   [img:Illustration] 

  Figura 7.30 Diagrama de blocos da Figura 7.29 com controle feedforward.

  No diagrama de blocos da Figura 7.30 os blocos Gc(s), H(s) e o comparador fazem parte do controlador TC. O bloco Gp(s) representa a dinâmica do tanque e G2(s) representa a dinâmica da perturbação da temperatura de entrada Te(s) até a temperatura de saída do tanque Y(s). F(s) é uma função de transferência adaptada à dinâmica do processo, calculada por TY 1.

  O projeto do bloco de alimentação avante F(s) pode ser estabelecido genericamente com base no diagrama de blocos da Figura 7.30. Para que o efeito de Te(s) sobre Y(s) seja nulo é suficiente que

   [img:Illustration] 

  Como se vê claramente no diagrama de blocos, a alimentação avante F(s) não fecha nenhuma malha e, portanto, não pode gerar instabilidade. Um problema possível na aplicação da função F(s), calculada por (7.51), ocorre quando Gp(s) é de fase não mínima. Neste caso, como Gp(s) tem zeros no semiplano direito do plano s, F(s) tem polos instáveis. A solução é contentar-se com um controle feedforward menos perfeito e suprimir da fórmula (7.51) os fatores de Gp(s) que representam os zeros do semiplano direito. Quando Gp(s) possuir atraso puro também deve ser suprimido de F(s), pois este não pode ser compensado por feedforward.

  Observações:

  • O feedforward não constitui uma malha de controle.

  • O feedforward não se restringe a perturbações rápidas como o cascade.

  • Sem os diagramas de blocos há dificuldade em distinguir feedforward de cascade.

  

### Exemplo 7.4

  Projete um controlador Gc(s) para a malha de realimentação e um controlador feedforward F(s) para o sistema da Figura 7.30. Suponha H(s) = 1 e considere

   [img:Illustration] 

  Sendo a planta de primeira ordem, da regra SIMC 1 tem-se que

   [img:Illustration] 

  com constante de tempo τ = 10, ganho K = 1 e atraso puro α = 1.

  Escolhendo τc = 2α, os parâmetros do controlador PI são

   [img:Illustration] 

  Assim, a função de transferência do controlador PI é

   [img:Illustration] 

  Como o atraso puro de Gp(s) não pode ser compensado por feedforward este deve ser suprimido, de modo que

   [img:Illustration] 

  Da Equação (7.51), obtém-se

   [img:Illustration] 

  A Figura 7.31 apresenta as respostas y(t) para entrada de perturbação te(t) do tipo degrau unitário com controlador por realimentação Gc(s) e referência r(t) nula. Note que a perturbação é rejeitada mais rapidamente quando há feedforward, embora neste exemplo exista a dificuldade do atraso puro na sua ação.

   [img:Illustration] 

  Figura 7.31 Resposta ao degrau unitário de perturbação te(t) com controlador por realimentação Gc(s) e r(t) = 0.

  A robustez dos controladores projetados pode ser examinada analisando-se o comportamento do sistema quando a planta Gp(s) tem variações nos seus parâmetros. Nas Figuras 7.32 e 7.33 são apresentadas as respostas a um degrau unitário na entrada de perturbação te(t), com r(t) = 0, supondo que a planta Gp(s) tem variações de ±10% na constante de tempo e no ganho. Note que com o controlador feedforward as perturbações causam variações menores na temperatura de saída y(t) e são mais rapidamente eliminadas.

   [img:Illustration] 

  Figura 7.32 Resposta ao degrau unitário de perturbação te(t) com variações de ±10% na constante de tempo e no ganho da planta, com controlador Gc(s) e sem controlador feedforward.

   [img:Illustration] 

  Figura 7.33 Resposta ao degrau unitário de perturbação te(t) com variações de ±10% na constante de tempo e no ganho da planta, com controlador Gc(s) e com controlador feedforward.

  A Figura 7.34 mostra a resposta da planta, suposta sem atraso puro e com variações de ±10% na constante de tempo e no ganho da planta, com os controladores por realimentação Gc(s) e feedforward F(s). Conclui-se que sem o atraso há apreciável melhora da resposta transitória pela ação do controlador feedforward.

   [img:Illustration] 

  Figura 7.34 Resposta ao degrau unitário de perturbação te(t) supondo a planta sem atraso puro, com variações de ±10% na constante de tempo e no ganho, com controlador Gc(s) e com controlador feedforward F(s).

  ■

  

#### 7.8.2 Controle de alternadores por feedforward

  A tensão de saída dos alternadores rotativos é estabilizada por meio da tensão contínua aplicada ao enrolamento de excitação (de campo). Isto é muito conveniente porque a potência de excitação é uma pequena fração da potência da máquina. Mas uma contrapartida inevitável é que tal campo apresenta indutância de valor elevado, o que ralenta a variação desejada no campo magnético da máquina e, portanto, a correção da sua tensão de saída. O resultado é altamente insatisfatório quando na carga ocorrem partidas de motores de porte.

  Uma solução impraticável seria aumentar de muitas vezes a tensão contínua e a potência instantânea máxima da fonte da excitação. A solução universal é, no entanto, uma realimentação avante que detecta a corrente de carga (origem das principais perturbações na tensão do alternador) e age sobre a excitação da máquina. Realiza-se com um transformador de corrente T e um retificador S, de potência adequada, cuja saída se soma no campo do motor à variável de manipulação do controle a realimentação.

  

#### 7.8.3 Aplicação ao controle de razão (ratio control)

  É muito frequente na indústria de processos contínuos a presença de misturadores de líquidos ou gases com o objetivo de produzir uma razão constante (estabilizada) dos componentes na saída. Uma das soluções emprega um esquema de controle feedforward sobre uma malha de realimentação rápida e a outra emprega um bloco não linear de cálculo de divisão. A Figura 7.35 mostra esses dois esquemas de controle.

  Sendo os líquidos incompressíveis e Kr a razão desejada dos componentes na saída, a razão dos fluxos de entrada no misturador também deve ser igual a Kr = fc(t)/fi(t).

  Seja a vazão fi(t), irregular e independente, isto é, a variável de perturbação da mistura, e seja fc(t) o fluxo controlado. No esquema da Figura 7.35 (a) o controlador feedforward FY multiplica a medida fi(t) por Kr e, assim, gera o sinal de referência r(t) para a malha de realimentação formada pelo controlador PID FC e pela válvula FV. Esta malha, que deve ser rápida, tende a impor fc(t) = Krfi(t) e, portanto, a impor a razão desejada.

  No esquema da Figura 7.35 (b) o bloco FY divide a medida fc(t) por fi(t), fornecendo ao controlador PID FC a medida da razão real K da mistura. Tendo o PID FC como sinal de referência a razão desejada Kr, sua ação leva a impor a convergência K → Kr.

   [img:Illustration] 

  Figura 7.35 Esquema P&ID de controle de razão. (a) Usando feedforward e realimentação. (b) Usando um bloco calculador de divisão e realimentação.

  

### 7.9 Ganho adaptativo (gain scheduling)

  Com certa frequência, não linearidades dos processos são relativamente lentas e associáveis a determinadas variáveis auxiliares no processo que são direta ou indiretamente mensuráveis.

  Exemplos:

  • a vazão Q de um tanque, por um registro de saída inferior, depende do nível de líquido pela conhecida expressão não linear  [img:Illustration] , sendo K uma constante característica do registro e H a altura da coluna de líquido;

  • a inércia J do cilindro de uma bobinadeira de aço depende da espessura já enrolada H e da inércia do cilindro vazio J0, conforme uma expressão do tipo J = J0 + K(H − H0)n.

  Um método para enfrentar o problema consiste em projetar um controlador linear, mas com ganho ou outros parâmetros automaticamente ajustados em função da variável indicadora (H, nos exemplos). Como frequentemente basta variar o ganho CC do controlador, esta técnica é chamada de ganho adaptativo.

  O sistema final é não linear porque nas suas equações aparecem produtos de variáveis. Se, nos exemplos anteriores, H varia lentamente em comparação com a resposta dinâmica do sistema de malha fechada, não há problemas de estabilidade com o método. Se H varia na mesma faixa de frequências, a estabilidade é muito afetada. Dado que as teorias que garantem estabilidade não linear são complexas e na prática geram projetos muito conservadores, a solução é verificar a estabilidade por meio de extensa simulação computacional e modificar o projeto até que fique satisfatório.

  O ganho adaptativo, assim como o ajuste de outros parâmetros do controlador, é muito simples de implementar utilizando controladores a computador. Além disso, a regra de ajuste do controlador pode até mesmo ser substituída pela consulta a tabelas, arquivadas na memória do computador e oriundas da experiência acumulada no campo ou nas simulações.

  

### 7.10 Introdução aos Controladores Lógicos Programáveis

  O Controlador Lógico Programável − CLP é um dispositivo digital desenvolvido na década de 1960 para o controle de máquinas e processos no ambiente agressivo das indústrias. Em princípio devia receber informações lógicas ou numéricas e, com base em regras armazenadas em sua memória, comandar ações específicas, tais como: energização ou desenergização de motores e chaves, sequenciamento lógico, temporização, contagem e operações aritméticas através de módulos de entradas e saídas digitais ou analógicas.

  Como substituto de circuitos de relés esse equipamento se mostrou mais confiável e de custo menor, seja em material e na fiação associada, seja em espaço, na mão de obra de instalação e na localização de falhas. Com ele, alterar a fiação de um circuito de relés transformou-se simplesmente na alteração de um programa.

  Atualmente os CLPs trabalham em rede e realizam rapidamente operações matemáticas e estatísticas complexas, dentre elas os algoritmos PID de controle dinâmico.

  A programação se faz por meio de um computador pessoal (o terminal de programação), pois em geral os CLPs não possuem teclado completo nem vídeo. A linguagem de programação mais comum é a linguagem ladder (escada), em referência aos clássicos esquemas ladder dos circuitos lógicos a relés. Operacionalmente o programa é desenvolvido em esquema ladder no vídeo por meio de blocos-padrão da linguagem, usando teclado e mouse do PC. Depois de testado o programa é transferido do PC para a memória do CLP. Detalhes da construção e da programação de CLPs podem ser encontrados em [40].

  

#### 7.10.1 Arquitetura

  Um CLP é constituído basicamente de fonte de alimentação, Unidade Central de Processamento (CPU), memória e dispositivos de entradas e saídas, conforme esquematizado na Figura 7.36.

   [img:Illustration] 

  Figura 7.36 Esquema básico de um CLP.

  A função de cada um dos elementos da Figura 7.36 é:

  Unidade Central de Processamento (CPU): controla o CLP. É constituída pelo processador, memória e por um barramento com circuitos auxiliares de controle.

  Processador: gerencia todas as funções do CLP e do ciclo de varredura. Executa o programa do fabricante, o processamento dos dados de acordo com o programa do usuário e atualiza continuamente a memória.

  Memória do sistema operacional: armazena o programa elaborado pelo fabricante, que realiza a partida (start-up) do CLP e que traduz o programa do usuário em instruções a serem executadas pelo processador. É uma memória não volátil que pode ser do tipo ROM (Read Only Memory) ou EPROM (Erasable Programmable Read Only Memory).

  Memória do usuário: armazena o programa aplicativo desenvolvido pelo usuário. É uma memória do tipo EEPROM (Electrically Erasable Programmable Read Only Memory) ou EPROM, podendo ainda ser uma memória RAM (Random Access Memory) com bateria.

  Memória de dados: conserva uma tabela de dados atuais, utilizados pelo programa do usuário, além da imagem das variáveis das entradas e saídas, que são lidas e escritas em momentos determinados pelo ciclo de execução (scan), conservando-as entre períodos sucessivos. Esta memória é do tipo RAM volátil, mas que pode possuir bateria.

  Barramento: composto por barramento de dados, de endereços e de controle que interliga os elementos do sistema conforme é solicitado pelo processador.

  Dispositivos de entradas e saídas: utilizados na conexão com os dispositivos situados em campo, como sensores e atuadores. Possuem a função de filtragem e isolamento dos sinais de campo com a CPU. Há entradas e saídas digitais e analógicas. Os sinais digitais (0 ou 1, 0 ou 12VCC e 0 ou 110VCA) são os que provêm de chaves ou relés, sensores de limites de variáveis e de comandos manuais. Os sinais analógicos são os que provêm de transdutores de medida ou que traduzem comandos analógicos, como as referências dos controladores dinâmicos. Naturalmente os CLPs só processam sinais analógicos depois de amostrados no tempo e convertidos em sinais digitais.

  Fonte de alimentação: responsável pela tensão de alimentação de todo o CLP.

  

#### 7.10.2 Linguagem de programação ladder

  A linguagem ladder (escada) é a linguagem de programação de CLPs mais utilizada. É uma linguagem gráfica de alto nível, simples de ser assimilada, que foi desenvolvida para imitar a lógica de relés ou diagramas de contatos. Os elementos básicos desta lógica (Figura 7.37) utilizam:

  • contatos normalmente abertos (NA), que normalmente interrompem a passagem de corrente;

  • contatos normalmente fechados (NF), que normalmente permitem a passagem de corrente e

  • bobinas, que representam os terminais de saída, energizados ou não.

   [img:Illustration] 

  Figura 7.37 Contatos NA, NF e bobina.

  Na programação ladder os elementos são dispostos horizontalmente em linhas, conforme é mostrado na Figura 7.38. Duas barras verticais paralelas são ligadas pela lógica de controle, formando os degraus (rungs) da escada, e cada degrau possui linhas e colunas. Durante um ciclo de scan a CPU executa as instruções do programa começando pela primeira instrução da primeira linha, da esquerda para a direita, indo de cima para baixo até a última instrução da última linha.

  Na Figura 7.38 estão exemplificadas algumas intruções simples:

  • lógica E (and): a saída Y1 é energizada (Y1 = 1) quando os contatos X1 E X2 estão fechados (X1 = X2 = 1). Em álgebra de Boole: Y1 = X1 · X2 ;

  • lógica OU (or): a saída Y2 é energizada (Y 2 = 1) quando um dos contatos ou ambos X3 OU X4 estão fechados (X3 = X4 = 1). Em álgebra de Boole: Y2 = X3 + X4 ;

  • lógica NÃO (not): a saída Y 3 é energizada (Y 3 = 1) quando o contato X5 está desligado (X5 = 0), ou seja, Y3 = X5.

   [img:Illustration] 

  Figura 7.38 Programação em linguagem ladder.

  A Figura 7.39 mostra o diagrama ladder do comando de uma saída Y, com contato de retenção, que realiza a seguinte lógica booleana:

   [img:Illustration] 

  isto é, Y = 1 se e somente se (X1 = X2 = 1 OU Y = 1) E X3 = 0.

   [img:Illustration] 

  Figura 7.39 Programa ladder com contato de retenção Y.

  Cada linha horizontal de conexões gráficas no diagrama ladder impõe uma dependência lógica. No exemplo da Figura 7.39 a saída Y é energizada (Y = 1) se X1 e X2 estiverem fechados (X1 = X2 = 1) ou se o contato de retenção Y estiver fechado (Y = 1) e se o contato X3 também estiver fechado (X3 = 0 ou X3 = 1).

  As instruções básicas da maioria dos CLPs podem ser agrupadas em sete categorias: lógica de relé ou instrução de bit, transferência de dados, temporização e contagem, aritmética, manipulação de dados, controle de fluxo e avançada.

  Todos os tipos de instruções pertencem a dois grandes grupos: instruções de entrada e instruções de saída. As instruções de entrada leem os estados atuais das variáveis do processo controlado, enquanto as instruções de saída impõem o resultado lógico desejado sobre as variáveis de saída. Estas, por sua vez, devem agir sobre o processo via atuadores. Durante a execução de uma instrução de entrada, o estado de um bit em um determinado endereço é examinado. Durante a execução da instrução de saída, a continuidade lógica da linha correpondente é examinada e conforme haja continuidade ou não, o estado do bit no endereço de saída é alterado para 1 ou para 0.

  Embora na essência a linguagem ladder se destine a processar somente variáveis binárias (1-0 ou on-off), nada impede que com os recursos atuais dos processadores digitais seja utilizada para um cálculo complexo sobre quaisquer variáveis na forma digital, como é o caso dos controladores PID.

  

#### 7.10.3 Ajuste de escala dos sinais

  As variáveis podem precisar de mudança de escala antes de seu uso no estágio seguinte de um programa. Suponha, por exemplo, que no cálculo do erro E = R − Y a saída Y do processo seja medida por um sensor que produz um sinal de 0 a 24 volts DC e que a referência R seja o sinal ajustado num potenciômetro de 0 a 10 volts DC. Além disso, suponha que a saída U do algoritmo de controle seja calculada com 16 bits, o conversor digital-analógico (D/A), que a seguir processa U, transforma o número de 16 bits com sinal algébrico num sinal de −10 a +10 volts DC.

  Na mudança de escala de uma variável V para uma variável escalonada Ves duas operações algébricas são, em geral, necessárias: multiplicação, para ajuste do alcance, e adição, para ajuste do off-set ou zero da escala. Para estabelecê-las simultaneamente convém seguir duas regras:

  Ajuste do alcance:

   [img:Illustration] 

  Ajuste do off-set:

   [img:Illustration] 

  Variável escalonada:

   [img:Illustration] 

  

### Exemplo 7.5

  Um transdutor transforma o alcance da rotação V de um motor em uma excursão de 1 a 9 volts DC. O conversor A/D converte o sinal em números binários de 204 a 1844. Para a sua utilização nos cálculos deseja-se reescalonar a medida de −3000 a +3000.

   [img:Illustration] 

  Portanto, a variável escalonada é Ves = 3,658V − 3746.

  ■

  

#### 7.10.4 Ciclo de execução (scan)

  Quando em operação o CLP realiza repetidamente as seguintes operações:

  1) atualização das entradas;

  2) processamento das instruções do programa na ordem estabelecida;

  3) atualização das saídas;

  4) realização de diagnósticos.

  A varredura é processada em ciclo fechado, como mostra a Figura 7.40. O controlador lê todas as portas de entrada, processa todas as instruções e atualiza as portas de saída. Por fim são realizados diagnósticos do sistema, como calcular o tempo de varredura (scan time), calcular o tempo máximo permitido para a execução de cada scan e verificar se os dispositivos de entrada e saída estão com funcionamento normal de operação. Para o primeiro ciclo a imagem das variáveis de entrada é zerada. Durante o processamento do programa, alguns tipos de CLP permitem a atualização imediata das entradas e saídas.

   [img:Illustration] 

  Figura 7.40 Ciclo de execução (scan).

  Usualmente o CLP de um processo industrial executa muitas funções: processa comandos do operador, aplica receitas de produção, protege equipamentos contra sobrecargas, informa o operador e realiza controle dinâmico. Num programa é possível estimar o período de scan somando os tempos associados às suas linhas (rungs), quer sejam de lógica, quer sejam de cálculo, a partir de tabelas do fabricante do CLP. Quando há controle dinâmico tornam-se também muito importantes os tempos de conversão do sinal analógico para digital A/D e de digital para analógico D/A. Note que alguma flutuação no período de scan é inevitável em virtude da manipulação de arquivos ou da presença de malhas lógicas.

  

### Exemplo 7.6

  Em um determinado CLP são números típicos:

  • conversão A/D de 3 variáveis: 50 ms ;

  • cálculo do algoritmo de controle de uma malha SISO: 50 μs ;

  • lógica para iniciar, encerrar e proteger o processo industrial: 50 ms.

  Portanto, o período de scan é de aproximadamente 100 ms.

  ■

  

#### 7.10.5 Controle dinâmico realizado por CLP

  Dado que durante cada período de scan as saídas permanecem inalteradas, o período de scan é importante para a dinâmica do controle porque representa um atraso puro na dinâmica da malha. Por essa razão os CLPs têm evoluído em sua arquitetura a fim de reduzir esse inconveniente.

  Suponha que um controlador dinâmico, projetado no domínio de tempo contínuo, deva ser implementado em um CLP. Antes de tudo é preciso traduzir o algoritmo de cálculo, ou seja, é preciso converter a função de transferência do controlador numa equação de diferenças na variável kT, com k inteiro. Os programas que realizam controladores PID em CLPs comerciais fazem essas transformações automaticamente. Na Seção 6.3.5 foi deduzida a equação de diferenças para um controlador PID genérico, resultando na equação de diferenças (6.46).

  Nos CLPs básicos, em que o algoritmo é simplesmente inserido no programa geral, o sinal m(kT) é calculado a partir dos sinais disponíveis em kT e em instantes anteriores, mas só é aplicado à planta quando transferido à saída, isto é, após um período T de scan. Portanto, um atraso puro T é introduzido na dinâmica da malha de controle.

  Nos CLPs mais avançados há usualmente módulos de entrada-saída ditos "inteligentes" ou intruções de entrada-saída imediatas, que calculam m(kT) e transmitem o resultado imediatamente à saída do CLP. O atraso puro fica assim restrito, praticamente, à soma dos tempos T′ de conversão dos sinais A/D e D/A, que é usualmente muito menor que o período T de scan do CLP (ver [39] e [42]).

  Como os sistemas físicos são analógicos, há uma necessidade de converter o sinal de tempo discreto m(kT) em um sinal de tempo contínuo m0(t). Os dispositivos de conversão mais usuais são os extrapoladores ou seguradores de ordem zero (zero order hold). O termo "ordem zero" decorre do fato de a função m0(t) ser aproximada em cada intervalo [kT ; (k + 1)T] por um valor constante, ou seja, por um polinômio de ordem zero.

  O atraso puro na reconstrução de um sinal senoidal é importante para considerações dinâmicas na malha de controle e pode ser visto na Figura 7.41. O efeito físico de m0(t) é aproximadamente equivalente ao do sinal me(t), que corresponde ao sinal contínuo original m(t), defasado de 0,5T.

   [img:Illustration] 

  Figura 7.41 Sinais original m(t), amostrado e extrapolado m0(t) e equivalente me(t).

  Portanto, há na realidade dois atrasos na operação de um controlador realizado por CLP: o devido ao scan(T nos CLPs básicos e T′ desprezível nos CLPs avançados), mais o atraso devido ao extrapolador (aproximadamente 0,5T). Observe na Figura 7.42 que nos CLPs básicos o sinal m(kT) é aplicado na planta a partir de (k + 1)T, produzindo um atraso total aproximado de 1,5T. Já nos CLPs avançados o sinal m(kT) é aplicado na planta a partir de kT + T′, com T′ desprezível (T′ << T), produzindo um atraso total aproximado de 0,5T.

   [img:Illustration] 

  Figura 7.42 Atrasos em CLPs: (a) básicos; (b) avançados.

  Quanto ao efeito sobre a estabilidade da malha de controle, é fundamental examinar o efeito de ambos, por exemplo, na redução da margem de fase nas frequências críticas dos critérios de estabilidade de Nyquist e Bode.

  

#### 7.10.6 A realidade industrial

  É de grande interesse examinar em quais campos da atividade industrial o atraso puro gerado pelo CLP realmente prejudica o desempenho e a estabilidade do sistema de controle dinâmico. Na prática, considera-se aceitável que a influência do atraso puro (e−jωc 1,5T ou e−jωc 0,5T) produza uma redução de no máximo 10o na margem de fase, medida na frequência de corte ωc da banda passante do sistema em malha aberta. Assim, os atrasos devidos aos CLPs podem ocorrer nos seguintes casos:

  • CLPs básicos:

   [img:Illustration] 

  • CLPs avançados:

   [img:Illustration] 

  Supondo T ≅ 100 ms, o CLP controlaria bem sistemas cujas faixas de passagem fossem ωc < 1,2 (rad/s) num CLP básico e ωc < 3,5 (rad/s) num CLP avançado.

  Sistemas industriais reais, geralmente de grande porte, têm grandes constantes de tempo. Portanto, as frequências de corte de suas malhas fechadas são relativamente baixas, com as ordens de grandeza da Tabela 7.4.

  Tabela 7.4 Faixas de passagem ωc da resposta frequencial de malha fechada de alguns processos industriais

  
    
      
        

        
      

      
        
          
            Processos

          

          
            ωc (rad/s)

          
        

        
          
            1) Fornos, misturadores, reatores químicos

          

          
            < 0,01

          
        

        
          
            2) Destiladores

          

          
            0,1

          
        

        
          
            3) Laminadores, bobinadeiras

          

          
            1

          
        

        
          
            4) Máquinas-ferramenta

          

          
            10

          
        

        
          
            5) Pequenos robôs

          

          
            > 30

          
        

      
    
  

  Portanto, pelo menos nas três primeiras categorias de processos da Tabela 7.4, os CLPs comerciais básicos são suficientes. Em casos de maiores exigências quanto à faixa de passagem, CLPs dedicados exclusivamente ao controle dinâmico ou CLPs avançados são economicamente viáveis. Em todos os casos, o projeto dos controladores pode ser feito no domínio contínuo, desde que se garanta uma margem de estabilidade adicional de 10o.

  

### 7.11 Exercícios resolvidos

  

### Exercício 7.1

  Projete um controlador PID para o sistema da Figura 7.43 usando as regras de Ziegler-Nichols.

   [img:Illustration] 

  Figura 7.43 Diagrama de blocos de um sistema em malha fechada.

  Solução

  

### Primeiro método

  Passo 1: fazer TD = 0 e TI → ∞.

  Passo 2: aumentar o ganho Kc até que a saída do sistema oscile periodicamente. O ganho final vale Ku. Para isso, o lugar das raízes deve cruzar o eixo imaginário quando Kc varia de 0 a infinito, caso contrário o método não se aplica.

   [img:Illustration] 

  Figura 7.44 Lugar das raízes quando Gc(s) = Kc.

  Na Figura 7.44 é apresentado o lugar das raízes para Gc(s) = Kc. Para Kc = Ku o sistema oscila periodicamente, pois os polos de malha fechada estão sobre o eixo imaginário.

  Supondo Gc(s) = Ku, a função de transferência de malha fechada é dada por

   [img:Illustration] 

  Substituindo s = jω no denominador da Equação (7.68), obtém-se

   [img:Illustration] 

  ou

   [img:Illustration] 

  Passo 3: a frequência da oscilação é  [img:Illustration]  e o período da oscilação vale

   [img:Illustration] 

  Da Equação (7.70) obtém-se

   [img:Illustration] 

  Passo 4: ajustar os parâmetros do controlador de acordo com a Tabela 7.1, ou seja,

   [img:Illustration] 

  Portanto, a função de transferência do controlador PID resulta

   [img:Illustration] 

  

### Segundo método

  Os passos 1 e 2 são iguais aos do primeiro método.

  Passo 3:  [img:Illustration] .

  Passo 4: determinar o valor de TI de modo que o sistema em malha fechada oscile periodicamente. Para isso basta determinar o valor de TI de modo que o sistema em malha fechada tenha polos sobre o eixo imaginário.

  Supondo  [img:Illustration] , a função de transferência de malha fechada é dada por

   [img:Illustration] 

  Substituindo s = jω no denominador da Equação (7.77), obtém-se

   [img:Illustration] 

  ou

   [img:Illustration] 

  A frequência da oscilação é obtida de 36 − 6ω2 = 0. Logo,  [img:Illustration] . Da Equação (7.70) tem-se que

   [img:Illustration] 

  Passo 5: duplicar o valor de TI. Logo, TI = 2.

  Passo 6: ajustar TD = TI = 2.

  Portanto, a função de transferência do controlador PID resulta

   [img:Illustration] 

  Na Figura 7.45 são apresentadas as respostas ao degrau unitário do sistema em malha fechada, com os controladores PID (7.76) e (7.81). A melhor resposta é a do sistema com o controlador (7.81), calculado pelo pelo segundo método, pois a resposta é mais rápida e tem sobressinal menor.

   [img:Illustration] 

  Figura 7.45 Resposta ao degrau unitário na referência do sistema em malha fechada.

  

### Exercício 7.2

  Considere um sistema de controle cascade para o acionamento elétrico de velocidade formado pelo conjunto motor, redutor e carga mecânica da Figura 7.46. A perturbação, objeto do cascade, consiste nas flutuações da rede que afetam instantaneamente a saída do amplificador de potência.

   [img:Illustration] 

  Figura 7.46 Diagrama de blocos do sistema com controlador cascade.

  Pede-se:

  • determine o controlador proporcional Kc para a malha interna (rápida), de modo que o erro estacionário e′(∞) para um degrau unitário em R′(s) seja de 2,5%;

  • projete um controlador Gc(s) para a malha externa (lenta) por meio das regras SIMC;

  • projete um controlador PID simples, por meio das regras SIMC, sem a realimentação interna do esquema cascade;

  • compare as respostas ao degrau na referência e na perturbação dos sistemas com os controladores cascade e PID.

  Solução

  

### Cálculo do controlador proporcional para a malha interna (rápida)

  Na malha interna o erro estacionário para R′(s) = 1/s é

   [img:Illustration] 

  Portanto, Kc = 19,5.

  

### Projeto do controlador PI para a malha externa (lenta)

  Para P0(s) = 0, a função de transferência da malha fechada interna é

   [img:Illustration] 

  A malha lenta tem como função de transferência do sistema controlado

   [img:Illustration] 

  A aproximação realizada na Equação (7.84) é justificada pelo fato de que o primeiro fator é aproximadamente igual a 1 nas frequências da faixa de passagem do segundo fator, isto é, entre 0 e 0,05(rad/s).

  Da regra SIMC 1 tem-se que

   [img:Illustration] 

  ou seja, K = 1, α = 0,2 e τ = 20.

  Escolhendo τc = α, os parâmetros do controlador PI são

   [img:Illustration] 

  Portanto, a função de transferência do controlador PI é

   [img:Illustration] 

  

### Projeto do controlador PID sem a malha cascade

  Considere o sistema da Figura 7.47.

   [img:Illustration] 

  Figura 7.47 Diagrama de blocos do sistema com controlador PID.

  Para P0(s) = 0, a função de transferência do sistema controlado é

   [img:Illustration] 

  Da regra SIMC 2 tem-se que

   [img:Illustration] 

  Logo, K = 2, α = 0,2, τ1 = 1 e τ2 = 20.

  Escolhendo τc = α, os parâmetros do controlador PID são

   [img:Illustration] 

  Assim, a função de transferência do controlador PID é

   [img:Illustration] 

  

### Efeito dinâmico dos controladores PID e cascade

  As respostas ao degrau unitário na referência r(t) e na perturbação p0(t) são apresentadas nas Figuras 7.48 e 7.49, respectivamente. Essas respostas podem ser obtidas por meio de simulação computacional dos diagramas de blocos das Figuras 7.46 e 7.47.

  Observa-se que na Figura 7.48 a resposta com o controlador cascade apresenta um sobressinal de 30% e um tempo de subida menor que a resposta com o controlador PID. Já na Figura 7.49 fica evidente a vantagem do controlador cascade, que rejeita o sinal de perturbação muito mais rapidamente que o controlador PID.

   [img:Illustration] 

  Figura 7.48 Resposta ao degrau unitário na referência r(t), com p0(t) = 0.

   [img:Illustration] 

  Figura 7.49 Resposta ao degrau unitário na perturbação p0(t), com r(t) = 0.

  

### Exercício 7.3

  Nos reguladores de tensão dos alternadores é obrigatório o emprego de um controlador feedforward para compensar com suficiente rapidez as quedas de tensão decorrentes da partida de motores conectados como carga. O diagrama de blocos do sistema de controle de um alternador está representado na Figura 7.50.

   [img:Illustration] 

  Figura 7.50 Diagrama de blocos do sistema de controle de um alternador.

  Pede-se:

  • determine a relação do conjunto transformador de corrente e retificador que constituem o controlador feedforward F(s);

  • calcule o controlador proporcional Kc para que o erro estacionário, para um degrau unitário aplicado em R(s), seja de 1%;

  • compare as respostas para um degrau i(t) = 50A na perturbação de carga com e sem o controlador feedforward.

  Solução

  Para que o efeito da perturbação I(s) seja nulo na saída V(s) é suficiente que

   [img:Illustration] 

  A função de transferência de malha aberta é dada pelo produto dos blocos que estão na malha de realimentação, ou seja,

   [img:Illustration] 

  O erro estacionário para R(s) = 1/s é

   [img:Illustration] 

  Portanto, Kc = 99.

  Sem o controlador feedforward(F(s) = 0) a função de transferência da perturbação I(s) até a saída V(s), com r(t) = 0, é

   [img:Illustration] 

  Na Figura 7.51 é apresentada a resposta v(t) para um degrau de perturbação i(t) = 50 A, sem o controlador feedforward. Note que a perturbação de corrente causa um desvio máximo de aproximadamente −19 V.

   [img:Illustration] 

  Figura 7.51 Resposta v(t) para um degrau de perturbação i(t) = 50 A sem o controlador feedforward.

  Se o modelo for exato,3 com o controlador feedforward o efeito da perturbação I(s) na saída V(s) é nulo, pois

   [img:Illustration] 

  Portanto,

   [img:Illustration] 

  

### Exercício 7.4

  Num processo metalúrgico industrial utiliza-se um compensador lead-lag para regular a velocidade de um bobinador de chapas de aço. O diagrama de blocos do sistema é apresentado na Figura 7.52.

   [img:Illustration] 

  Figura 7.52 Diagrama de blocos de um sistema para regular a velocidade de um bobinador de chapas de aço.

  Pede-se:

  • desenhe o gráfico de Bode do módulo da função de transferência de malha aberta;

  • determine a frequência da faixa de passagem ou frequência de corte;

  • verifique se é possível implementar o compensador num CLP com período de scan T = 0,1 s.

  Solução

  O gráfico de Bode do módulo da função de transferência de malha aberta |Gma(jω)| (dB) é apresentado na Figura 7.53. A frequência da faixa de passagem é a frequência de corte em que o gráfico do módulo cruza a linha de 0 dB, ou seja, em ωc = 0,4 (rad/s).

   [img:Illustration] 

  Figura 7.53 Módulo da função de transferência de malha aberta.

  Para um período de scan T = 0,1 s, num CLP básico tem-se que

   [img:Illustration] 

  e num CLP avançado

   [img:Illustration] 

  Portanto, o compensador pode ser implementado em ambos os tipos de CLPs.

  Na Figura 7.54 são apresentadas as respostas ao degrau unitário na referência com o compensador lead-lag implementado nas formas contínua e discreta. O controlador lead-lag é implementado num CLP na forma discreta por meio de uma equação de diferenças.4

   [img:Illustration] 

  Figura 7.54 Respostas ao degrau unitário na referência com o compensador lead-lag implementado nas formas contínua e discreta.

  Comparando os gráficos da Figura 7.54 observa-se que a resposta transitória, obtida com o compensador implementado na forma discreta, possui um sobressinal um pouco maior que a resposta obtida com o compensador implementado na forma contínua. O resultado dessa comparação confirma a regra prática proposta em (7.101).

  

### 7.12 Exercícios propostos

  

### Exercício 7.5

  Considere o sistema da Figura 7.55.

   [img:Illustration] 

  Figura 7.55 Diagrama de blocos de um sistema em malha fechada.

  Projete controladores Gc(s) por meio das regras SIMC e desenhe as correspondentes respostas em frequência de malha aberta e de malha fechada para as seguintes plantas:

   [img:Illustration] 

  

### Exercício 7.6

  Para os três controladores do Exercício 7.5, informe:

  a) Banda Proporcional (BP);

  b) Tempo TR de avanço de rampa (rate time);

  c) Tempo TS de duplicação (reset time).

  

### Exercício 7.7

  Considere o regulador de velocidade do motor elétrico da Figura 7.56. Há duas malhas de realimentação: a interna, que controla a corrente no motor, e a externa, que controla a velocidade. A malha interna é rápida, comparada com a externa, que é mais lenta devido à inércia mecânica da carga do motor. Desenhe o diagrama P&ID correspondente.

   [img:Illustration] 

  Figura 7.56 Diagrama de blocos de um regulador de velocidade.

  

### Exercício 7.8

  Descreva em palavras a função dos seguintes códigos ISA:

  FI, SI, MC, TC, LC, DY e TY.

  

### Exercício 7.9

  Explique a diferença entre os controladores cascade e feedforward para reduzir perturbações nos processos industriais.

  

### Exercício 7.10

  Explique por que não se pode aplicar um controlador cascade no Exemplo 7.4, para reduzir os efeitos da temperatura te(t) de entrada ou da vazão de líquido de entrada na temperatura y(t) do produto de saída.

  

### Exercício 7.11

  No reator químico com camisa de resfriamento, esquematizado na Figura 7.57, a temperatura do líquido dentro do tanque tin(t) deve ser bem estabilizada. O nível do líquido é constante, por meio de ação regulatória na saída do produto. A variável de manipulação para controlar a temperatura no tanque é a vazão do líquido de resfriamento, que é reciclada. Quanto maior essa vazão mais resfriamento ocorre. Há várias possíveis perturbações: a pressão pe(t) do líquido resfriador, a temperatura te(t) do mesmo líquido, a pressão na saída da bomba pb(t), a concentração do líquido de entrada x(t), que influi na velocidade da reação química, e a vazão q(t) do líquido de entrada. Faça um diagrama de blocos que contemple todas essas perturbações considerando intuitivamente a rapidez dos seus efeitos sobre a variável de saída do reator, que é a concentração y(t). Examine a viabilidade de sucesso de cada possível esquema de controle cascade.

   [img:Illustration] 

  Figura 7.57 Reator químico.

  

### Exercício 7.12

  Determine a função de transferência Y(s)/P0(s) no diagrama de blocos com controle cascade da Figura 7.22. Suponha R(s) = 0.

  

### Exercício 7.13

  Um processo de reação química ocorre em dois tanques em cascata, com fluxo de produto aproximadamente constante. A variável de manipulação é a vazão FA(s) do reagente, e há também perturbações na vazão FV(s) do solvente. A medida da concentração X(s) na saída do produto exige atraso de transporte de 0,5 s. Com base no diagrama de blocos da Figura 7.58, projete um controlador Gc(s) pela regra SIMC e um feedforward F(s) para reduzir o efeito das flutuações na vazão FV(s). Simule, por meio de um programa computacional, a resposta ao degrau de perturbação com e sem o controlador feedforward.

   [img:Illustration] 

  Figura 7.58 Diagrama de blocos do processo com controlador feedforward.

  

### Exercício 7.14

  Projete um controlador PID para o sistema da Figura 7.59 usando as regras de Ziegler-Nichols.

   [img:Illustration] 

  Figura 7.59 Diagrama de blocos de um sistema em malha fechada.

  

### Exercício 7.15

  Deseja-se realizar os controladores dos Exercícios 7.2 e 7.3 por meio de Controladores Lógicos Programáveis. Estime os maiores períodos de scan que podem ser aceitos sem deterioração apreciável das margens de estabilidade das malhas de controle.

  

  __________

  1Não confundir esquema de instrumentação P&ID com controlador ou algoritmo PID.

  2O efeito desta não linearidade é analisado no Capítulo 9.

  3Em decorrência das incertezas do modelo do sistema real, a resposta normalmente apresenta algum valor não nulo.

  4Neste exemplo a função de transferência discreta foi obtida pelo método do mapeamento polo-zero. Detalhes dessa implementação podem ser estudados nos capítulos finais do livro.

<!-- Text/chapter08.xhtml -->

  Controle Automático, 2ª edição
  
  
  

  

## 8

  

## Projeto Algébrico pela Malha Fechada

  

### 8.1 Introdução

  No Capítulo 3 mostrou-se que a posição dos polos da função de transferência de um sistema é fundamental para definir forma e duração das respostas transientes. No Capítulo 4 mostrou-se que a realimentação gera um sistema em malha fechada cujos polos são diferentes daqueles do sistema original e que o método do lugar das raízes permite projetar compensadores que localizam adequadamente os polos de malha fechada.

  Neste capítulo é apresentada uma abordagem algébrica para o mesmo objetivo, chamada de imposição ou alocação de polos de malha fechada. Este método, assim como o método do lugar das raízes, não permite a imposição dos zeros de malha fechada. No caso mais geral polos e zeros de malha fechada podem ser especificados por meio do método da imposição de polos e zeros ou casamento de modelos (model matching 1), tratado da Seção 8.3.

  O problema é então o seguinte: dada uma planta com função de transferência Gp(s), projetar um compensador tal que o sistema em malha fechada tenha os mesmos polos que a função de transferência de um modelo especificado.

  Para exemplificar o método algébrico, considere o sistema de controle da Figura 4.20, no qual a função de transferência do sistema a ser controlado é

   [img:Illustration] 

  Suponha agora que o projetista deva atender à especificação de que os polos dominantes de malha fechada estejam localizados em  [img:Illustration] , como no Exemplo 4.7. Conforme mostrado, o projeto pelo método do lugar das raízes não é único. Um dos projetos possíveis levou ao compensador da Equação (4.58)

   [img:Illustration] 

  Com este compensador a função de transferência de malha fechada (4.59) apresenta os polos dominantes especificados em  [img:Illustration] , além de um polo localizado em s = −2,6 e de um zero em s = −2.

  A ideia do método algébrico é partir de um compensador com função de transferência

   [img:Illustration] 

  e do polinômio especificado para os polos de malha fechada. Este polinômio deverá ter ordem 3, já que a planta tem dois polos e o compensador um polo. As raízes desse polinômio deverão ter dois polos dominantes e um terceiro polo real não dominante. A título de ilustração, considere este terceiro polo especificado na mesma posição obtida pelo método do lugar das raízes (Equação (4.59)), ou seja, em s = −2,6. Os polos de malha fechada serão, assim, as raízes do polinômio

   [img:Illustration] 

  Para o compensador (8.2) e para a planta (8.1) tem-se que a função de transferência de malha fechada Gmf(s), com realimentação unitária, é dada por

   [img:Illustration] 

  Igualando o denominador da Equação (8.4) com o polinômio especificado (8.3), tem-se que

   [img:Illustration] 

  e, portanto,

  d1 = 1 d0 = 5,6 c1 = 4,16 c0 = 8,32.

  Assim, o compensador obtido é

   [img:Illustration] 

  Logo, a função de transferência de malha fechada é dada por

   [img:Illustration] 

  Em ambos os projetos, pelo método do lugar das raízes e pelo método algébrico, o zero obtido em s = −2 não foi especificado. Como os zeros também afetam os transitórios das respostas, é importante avaliar esses efeitos por meio de simulações antes de se passar à etapa de implementação dos compensadores.

  

### 8.2 Imposição arbitrária de polos com realimentação unitária

  Nesta seção considera-se o método de imposição ou relocação de polos para o sistema em malha fechada com realimentação unitária da Figura 8.1.

   [img:Illustration] 

  Figura 8.1 Sistema em malha fechada com realimentação unitária.

  Por meio da escolha adequada do compensador Gc(s) é possível obter qualquer configuração especificada para os polos de malha fechada, desde que não haja restrições para os zeros da malha fechada. Note que estas restrições têm origem tanto nos zeros da planta quanto nos zeros do compensador a ser escolhido.

  Considere o sistema da Figura 8.1, com Gp(s) = B(s)/A(s) e Gc(s) = C(s)/D(s), sendo A(s), B(s), C(s) e D(s) polinômios com coeficientes reais. Então,

   [img:Illustration] 

  Sendo F(s) o polinômio cujas raízes são os polos especificados para o sistema em malha fechada, deseja-se:

  • definir condições para que os polos especificados possam ser arbitrariamente escolhidos e

  • estabelecer um procedimento para a determinação de C(s) e D(s) que realize tal imposição de polos.

  Da Equação (8.8) tem-se que o problema de imposição de polos corresponde à solução da equação polinomial

   [img:Illustration] 

  A equação polinomial (8.8) é chamada equação Diofantina. Os polinômios A(s), B(s) e F(s) são dados e os polinômios C(s) e D(s) do compensador são incógnitas. Deve-se observar que o polinômio C(s) aparece no numerador da função de transferência de malha fechada e, assim, não se tem controle sobre os zeros de malha fechada.

  Para que F(s) seja realmente arbitrário é necessário supor que A(s) e B(s) não possuem fatores comuns. Caso contrário, supondo A(s) = (s − p)A(s) e B(s) = (s − p)B(s), a equação Diofantina fica

   [img:Illustration] 

  e, com isso, F(s) não pode ser arbitrário, já que possui necessariamente o fator comum (s − p).

  
    Para que Gp(s) = B(s)/A(s) e Gc(s) = C(s)/D(s) sejam funções de transferência fisicamente realizáveis deve-se ter grau[B(s)] ≤ grau[A(s)] e grau[C(s)] ≤ grau[D(s)]. Logo, se grau[A(s)] = n e grau[D(s)] = m, o polinômio dos polos de malha fechada, F(s), deve ter grau n + m.

  

  Sejam

   [img:Illustration] 

  As condições an = 0 e dm = 0 garantem que a planta e o compensador possuem funções de transferência próprias, isto é, o grau do polinômio do numerador é menor ou igual ao grau do denominador.

  Sendo grau[F(s)] = n + m, o polinômio F(s) pode ser escrito como

   [img:Illustration] 

  Substituindo os polinômios A(s), B(s), C(s), D(s) e F(s) na equação Diofantina (8.9), obtém-se

   [img:Illustration] 

  Reagrupando os termos no lado esquerdo e identificando os coeficientes de mesma potência de s em cada lado, tem-se que

   [img:Illustration] 

  Resulta, assim, que a equação Diofantina é equivalente a um sistema de n + m + 1 equações algébricas em 2(m + 1) incógnitas. Colocando este sistema na forma matricial, obtém-se

   [img:Illustration] 

  A matriz Sm, chamada matriz de Sylvester, tem n + m + 1 linhas, 2(m + 1) colunas e é formada pelos coeficientes de A(s) e B(s). O método recomendado para a construção da matriz Sm é o seguinte:

  • as duas primeiras colunas de Sm são formadas pelos coeficientes de A(s) e B(s) em ordem crescente das potências de s, seguidos de m linhas de zeros;

  • as duas últimas colunas são formadas por zeros nas m primeiras linhas, seguidos pelos coeficientes de A(s) e B(s).

  

### Exemplo 8.1

  Suponha

   [img:Illustration] 

  com n = 1 e m = 2.

  Como b1 = c1 = c2 = 0, as equações para determinação de C(s) e D(s), na forma matricial, são escritas como

   [img:Illustration] 

  

#### 8.2.1 Condição para escolha arbitrária dos polos de malha fechada

  É uma propriedade conhecida da teoria de sistemas lineares [14] que a condição necessária e suficiente para a Equação (8.14) ter solução, qualquer que seja f, é que Sm tenha posto linha completo.2 Por outro lado, uma condição necessária para que Sm tenha posto linha completo é que o número de colunas seja maior ou igual ao número de linhas, ou seja,

  2(m + 1) ≥ n + m +1 ou m ≥ n − 1.

  Supondo m ≥ n − 1, pode-se mostrar que a matriz Sm tem posto linha completo se e só se B(s) e A(s) forem polinômios coprimos, ou seja, não tiverem fatores comuns [14], hipótese esta já assumida anteriormente. Nesta condição,

  • se m = n − 1, então Sm é uma matriz quadrada de ordem 2n e, para cada F(s) escolhido, a solução da equação Diofantina é única, e

  • se m > n − 1, haverá um número de incógnitas maior do que o número de equações. Neste caso a solução não é única, e alguns parâmetros do compensador podem ser escolhidos de forma a atender outros objetivos de projeto.

  
    Portanto, sendo B(s) e A(s) polinômios coprimos, para que os polos de malha fechada possam ser arbitrariamente escolhidos deve-se ter m ≥ n − 1, sendo n e m os graus dos polinômios dos denominadores da planta Gp(s) e do compensador Gc(s), respectivamente.

  

  Para o caso em que m < n − 1, é possível que alguns polos possam ser escolhidos, mas não qualquer conjunto de polos.

  

#### 8.2.2 Condição para que a função de transferência Gc(s) seja própria

  Uma vez garantida a existência do compensador para F(s) arbitrário, de grau n + m, resta determinar as condições para que a função de transferência Gc(s) do compensador seja própria, ou seja, grau[C(s)] ≤ grau[D(s)]. Supondo que B(s) e A(s) são polinômios coprimos, três casos são considerados.

  

### • Caso 1: grau[B(s)] < grau[A(s)]

  Neste caso, tem-se bn = 0, e a última equação do sistema (8.14) é

   [img:Illustration] 

  Assim, se fn+m ≠ 0, então dm ≠ 0 e  [img:Illustration]  é própria.

  
    Portanto, sendo B(s) e A(s) polinômios coprimos, para que a função de transferência Gc(s) do compensador seja própria basta que a função de transferência Gp(s) da planta tenha grau[B(s)] < grau[A(s)].

  

  

### Exemplo 8.2

  Considere uma planta com função de transferência

   [img:Illustration] 

  Para que o polinômio F(s) possa ser arbitrariamente escolhido deve-se ter um compensador de grau m ≥ n − 1. Assumindo m = 1, tem-se que grau[F(s)] = n + m = 2 + 1 = 3, e nessas condições sabe-se que o compensador será único e com função de transferência própria. Assim, considere, por exemplo, os seguintes polos especificados para a função de transferência de malha fechada:

  s = −1 + j, s = −1 − j e s = −2,

  ou seja,

   [img:Illustration] 

  Sendo m = 1, a função de transferência do compensador é do tipo

   [img:Illustration] 

  O sistema de equações na forma matricial é dado por

   [img:Illustration] 

  Substituindo os valores numéricos, obtém-se

   [img:Illustration] 

  cuja solução é

  d0 = 3, c0 = 4, d1 = 1, c1 = 3.

  Portanto, a função de transferência do compensador é

   [img:Illustration] 

  Logo, a função de transferência de malha fechada Gmf(s) é dada por

   [img:Illustration] 

  Pode-se observar que o denominador F(s) é o mesmo especificado em (8.18). Por outro lado, o projeto não permite que se tenha controle sobre o numerador da função de transferência de malha fechada, que apresenta um zero em s = −4/3. Como este zero afeta o transitório da resposta do sistema é importante avaliar o seu efeito, por meio de simulações, antes de se passar à etapa de implementação do compensador.

  ■

  

### • Caso 2: grau[B(s)] = grau[A(s)] = n e m = n − 1

  Neste caso Sm é uma matriz quadrada e a solução da Equação (8.14) é única. Não há garantia de que dm = dn−1 ≠ 0, e o compensador pode resultar impróprio.

  

### Exemplo 8.3

  Considere uma planta com função de transferência

   [img:Illustration] 

  Neste exemplo grau[B(s)] = grau[A(s)] = n = 2 e m = n − 1 = 1.

  Sendo grau[F(s)] = n + m = 2 + 1 = 3 e adotando

   [img:Illustration] 

  da Equação (8.14) tem-se que

   [img:Illustration] 

  ou seja,

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  Portanto, a função de transferência do compensador é

   [img:Illustration] 

  que é uma função de transferência não própria.

  Este é um exemplo típico para o qual é possível impor F(s) arbitrário, porém não se pode garantir que Gc(s) seja própria para qualquer F(s).

  ■

  

### • Caso 3: grau[B(s)] = grau[A(s)] e m > n − 1

  Neste caso a solução da Equação (8.14) não é única, e é sempre possível encontrar um compensador estritamente próprio para realizar a imposição de polos arbitrária.

  

### Exemplo 8.4

  Considere uma planta com função de transferência

   [img:Illustration] 

  Neste exemplo grau[B(s)] = grau[A(s)] = n = 1 e m = 1 >n − 1 = 0.

  Sendo grau[F(s)] = n + m = 1 + 1 = 2 e adotando

   [img:Illustration] 

  da Equação (8.14) tem-se que

   [img:Illustration] 

  ou seja,

   [img:Illustration] 

  Neste caso o sistema (8.33) possui 3 equações e 4 incógnitas e, portanto, o sistema tem infinitas soluções. Para garantir que a função de transferência Gc(s) seja própria basta adotar d1 ≠ 0. Impondo d1 = 1, obtém-se

  d0 = 6, c0 = −2, c1 = 0.

  Portanto, a função de transferência do compensador é

   [img:Illustration] 

  ■

  

### 8.3 Imposição de polos e model matching

  Nos exemplos anteriores a solução apresentada para o problema de imposição de polos define a localização dos polos de malha fechada, porém não estabelece nenhuma condição para os zeros de malha fechada. A consequência desse fato é que o transitório do sistema em malha fechada pode não atender às especificações de projeto, uma vez que este transitório é função tanto dos polos quanto dos zeros de malha fechada.

  Na prática é comum o seguinte procedimento: escolhe-se um conjunto de polos para a malha fechada e calcula-se o compensador pela Equação (8.14). Em seguida verifica-se, por simulação computacional, se a resposta do sistema em malha fechada atende às especificações de projeto. Caso isso não ocorra novos polos são propostos para a malha fechada e recalcula-se o compensador.

  No problema de imposição de polos e zeros, conhecido como model matching (casamento de modelo), tanto os polos quanto os zeros de malha fechada são especificados. O compensador é então calculado de forma que o sistema em malha fechada apresente esses polos e zeros.

  Embora seja mais fácil obter um transitório especificado no problema de model matching, este problema apresenta, como é de se esperar, condições de solução mais restritivas do que o de imposição de polos apenas.

  

#### 8.3.1 Projeto de compensadores para model matching

  A configuração de realimentação unitária da Figura 8.1 permite, sob certas condições, impor arbitrariamente os polos de malha fechada. No entanto esta configuração não é adequada para a solução do problema de model matching. Nesta seção o problema de model matching é tratado a partir do diagrama de blocos da Figura 8.2.

   [img:Illustration] 

  Figura 8.2 Diagrama de blocos para o problema de model matching.

  A seguinte notação é adotada para a Figura 8.2:

   [img:Illustration] 

  O compensador Gff(s) é chamado de compensador de feedforward (alimentação avante) e Gc(s) é chamado de compensador de feedback (realimentação). Considerando apenas o caso em que Gp(s), Gff(s) e Gc(s) são funções estritamente próprias, a função de transferência de R(s) para Y(s) na Figura (8.2) é dada por

   [img:Illustration] 

  O problema de model matching pode ser formulado da seguinte maneira: dada a planta Gp(s), com B(s) e A(s) polinômios coprimos e com grau[B(s)] < grau[A(s)] = n e dada a função de transferência G0(s) = B0(s)/A0(s) própria, com B0(s) e A0(s) polinômios coprimos, e supondo3 grau[A0(s)] − grau[B0(s)] ≥ grau[A(s)] − grau[B(s)], determinar Gff(s) e Gc(s) próprias tal que

   [img:Illustration] 

  A solução é dada pelo procedimento descrito a seguir.

  

### • Passo 1

  Cancele os fatores comuns ao numerador e ao denominador em

   [img:Illustration] 

  e defina Bp(s) e Ap(s) coprimos tal que

   [img:Illustration] 

  Das Equações (8.36) e (8.38) obtém-se

   [img:Illustration] 

  Deve-se observar que fazer L(s) = Bp(s) e calcular D(s) e M(s) a partir da equação

   [img:Illustration] 

  não garante que os compensadores Gff(s) e Gc(s) resultantes sejam próprios. Este fato justifica os passos seguintes do procedimento.

  

### • Passo 2

  Escolha um polinômio Ap(s) com raízes no semiplano esquerdo do plano s tal que

   [img:Illustration] 

  No passo 3 pode-se verificar que o polinômio Ap(s) é cancelado ao longo dos cálculos.

  

### • Passo 3

  Da Equação (8.39) tem-se

   [img:Illustration] 

  Defina

   [img:Illustration] 

  e determine D(s) e M(s) a partir de

   [img:Illustration] 

  Denotando

   [img:Illustration] 

  com m ≥ n − 1. Por meio de manipulações algébricas simples os coeficientes dos polinômios D(s) e M(s) podem ser obtidos a partir da solução do sistema linear (8.48).

   [img:Illustration] 

  Pode-se mostrar ([2] e [13]) que este procedimento produz compensadores Gff(s) e Gc(s) próprios.

  

### Exemplo 8.5

  Seja grau[A(s)] = n = 1 e

   [img:Illustration] 

  Deseja-se projetar compensadores Gff(s) e Gc(s), como no diagrama de blocos da Figura 8.2, para imposição de polos e zeros, sendo

   [img:Illustration] 

  

### • Passo 1

  Calcule G(s)

   [img:Illustration] 

  Note que B0(s) = s +1 e B(s) = 1 não possuem fatores comuns para serem cancelados.

  Portanto,

   [img:Illustration] 

  e

   [img:Illustration] 

  

### • Passo 2

  Seja o polinômio Ap(s) escolhido com raízes no semiplano esquerdo do plano s e tal que

   [img:Illustration] 

  Como grau[Ap(s)] = 2 e como grau[Ap(s)] deve ser maior ou igual a 0, para que a condição (8.54) seja satisfeita pode-se adotar, por exemplo, grau[Ap(s)] = 0, com

   [img:Illustration] 

  

### • Passo 3

  Calcule

   [img:Illustration] 

  Sendo grau[F(s)] = 2 = n + m = 1 + m, então, m = 1. Logo,

   [img:Illustration] 

  Usando a Equação (8.48), os coeficientes dos polinômios D(s) e M(s) podem ser determinados a partir da solução do sistema linear

   [img:Illustration] 

  Neste exemplo, devido à escolha de Ap(s) com grau 0 o sistema de equações resultou indeterminado, ou seja, com 3 equações e 4 incógnitas. Consequentemente, o problema terá infinitas soluções. De fato, substituindo os valores numéricos resulta

   [img:Illustration] 

  ou

   [img:Illustration] 

  Adotando d0 = 0,5, obtém-se m0 = 11 e m1 = 4,5. As funções de transferência dos controladores são

   [img:Illustration] 

  Logo, a função de transferência de malha fechada é dada por

   [img:Illustration] 

  que está de acordo com a função de transferência especificada em (8.50).

  ■

  

### 8.4 Exercícios resolvidos

  

### Exercício 8.1

  Considere o sistema da Figura 8.3.

   [img:Illustration] 

  Figura 8.3 Sistema com duas massas e uma mola.

  Na Figura 8.3, x1 e x2 indicam as posições das massas M1 e M2, k é a constante da mola e u(t) e w(t) representam forças aplicadas às massas.

  As equações diferenciais que representam a dinâmica do sistema da Figura 8.3 são

   [img:Illustration] 

  Aplicando a transformada de Laplace nas Equações (8.66) e (8.67) com condições iniciais nulas (x1(0) = ẋ1(0) = x2(0) = ẋ2(0) = 0), obtém-se

   [img:Illustration] 

  Isolando X1(s) na Equação (8.68) e substituindo na Equação (8.69), com W(s) = 0, a função de transferência da planta com entrada U(s) e saída X2(s) é dada pela Equação (8.70) e é evidentemente instável.

   [img:Illustration] 

  A malha de controle, indicando as funções de transferência e os sinais de referência e de perturbação, é mostrada na Figura 8.4.

   [img:Illustration] 

  Figura 8.4 Malha de controle do sistema com duas massas e uma mola.

  Seguindo a abordagem do método algébrico, para que os polos do sistema em malha fechada, raízes de F(s), possam ser arbitrariamente escolhidos deve-se ter um compensador de grau m ≥ n − 1 = 4 − 1 = 3. Assumindo m = 3, tem-se que grau[F(s)] = n + m = 4 + 3 = 7. Nessas condições sabe-se que o compensador é único e com função de transferência própria.

  Assim, de forma a estabilizar o sistema em malha fechada considere, por exemplo, os seguintes polos especificados para a função de transferência de malha fechada:

  s = −2, s = −2, s = −2, s = −1, s = −1, s = −1+ 2j e s = −1 − 2j,

  ou seja,

   [img:Illustration] 

  O compensador Gc(s) tem a função de transferência

   [img:Illustration] 

  e é determinado pela solução da equação matricial

   [img:Illustration] 

  Supondo M1 = M2 = k = 1, a Equação (8.70) fica

   [img:Illustration] 

  Substituindo os valores numéricos na Equação (8.73), obtém-se

   [img:Illustration] 

  cuja solução é

  d0 = 108, c0 = 40, d1 = 44, c1 = 156, d2 = 10, c2 = 38, d3 = 1, c3 = 141.

  Logo, a função de transferência do compensador é

   [img:Illustration] 

  Do diagrama de blocos da Figura 8.4 tem-se que

   [img:Illustration] 

  Supondo que o sinal de referência é nulo (R(s) = 0), a função de transferência do sistema em malha fechada, que possui como entrada a perturbação W(s) e como saída a posição X2(s), é dada por

   [img:Illustration] 

  A resposta x2(t) para uma perturbação w(t) do tipo degrau unitário é apresentada na Figura 8.5. Nota-se nesta figura que apesar de a Equação (8.78) possuir polos e zeros complexos conjugados a resposta ao degrau não apresenta sobressinal.

   [img:Illustration] 

  Figura 8.5 Resposta x2(t) quando w(t) é um degrau unitário.

  

### Exercício 8.2

  Considere o sistema massa-mola da Figura 8.6, na qual a saída x(t) indica a posição da massa M, k é a constante da mola e f(t) representa a força externa aplicada à massa.

   [img:Illustration] 

  Figura 8.6 Sistema massa-mola.

  Supondo M = 1 e k = 1, projete compensadores Gff(s) = L(s)/D(s) e Gc(s) = M(s)/D(s), como no diagrama de blocos da Figura 8.2, para imposição de polos e zeros, sendo

   [img:Illustration] 

  Solução

  A equação diferencial que representa a dinâmica do sistema massa-mola da Figura 8.6 é

   [img:Illustration] 

  Aplicando a transformada de Laplace na Equação (8.80), com condições iniciais nulas (x(0) = ẋ (0) = 0), obtém-se a função de transferência

   [img:Illustration] 

  

### • Passo 1

  Calcule

   [img:Illustration] 

  Note que B0(s) = s + 10 e B(s) = 1 não possuem fatores comuns para serem cancelados.

  Portanto,

   [img:Illustration] 

  e

   [img:Illustration] 

  

### • Passo 2

  Seja o polinômio Ap(s), escolhido com raízes no semiplano esquerdo do plano s e tal que

   [img:Illustration] 

  Como grau[Ap(s)] = 3 e como grau[Ap(s)] deve ser maior ou igual a 0, para que a condição (8.85) seja satisfeita pode-se adotar, por exemplo, grau[Ap(s)] = 0, com

   [img:Illustration] 

  

### • Passo 3

  Calcule

   [img:Illustration] 

  Sendo grau[F(s)] = 3 = n + m = 2 + m, então, m = 1. Logo,

   [img:Illustration] 

  Usando a Equação (8.48) os coeficientes dos polinômios D(s) e M(s) podem ser determinados a partir da solução do sistema linear

   [img:Illustration] 

  Substituindo os valores numéricos, resulta

   [img:Illustration] 

  ou

   [img:Illustration] 

  Portanto, as funções de transferência dos controladores são

   [img:Illustration] 

  Logo, a função de transferência de malha fechada é dada por

   [img:Illustration] 

  que está de acordo com a função de transferência especificada em (8.79).

  Na Figura 8.7 são apresentadas as respostas x(t) para um degrau unitário aplicado na entrada f(t) do sistema em malha aberta, sem compensadores, e na referência r(t) do sistema em malha fechada da Figura (8.2) com os compensadores Gff(s) e Gc(s). Note que sem os compensadores a saída x(t) é oscilatória, enquanto com os compensadores a saída torna-se superamortecida.

   [img:Illustration] 

  Figura 8.7 Respostas x(t) para um degrau unitário aplicado na entrada f(t) do sistema em malha aberta e na referência r(t) do sistema em malha fechada.

  

### Exercício 8.3

  Projete um controlador para um levitador eletromagnético com função de transferência

   [img:Illustration] 

  de modo que os polos de malha fechada dominantes tenham coeficiente de amortecimento ξ = 0,5 e frequência natural ωn = 2 (rad/s).

  Solução

  

### Imposição de polos com realimentação unitária

  Para que a especificação seja satisfeita os polos de malha fechada dominantes devem estar localizados em

   [img:Illustration] 

  Para que o polinômio F(s) possa ser arbitrariamente escolhido deve-se ter um compensador de grau m ≥ n − 1. Assumindo m = 1, tem-se que grau[F(s)] = n + m = 2 + 1 = 3. Logo, é necessário escolher a posição de um terceiro polo p de malha fechada. Para que a resposta transitória não seja afetada este deve ser escolhido pelo menos 5 constantes de tempo mais à esquerda dos polos complexos conjugados dominantes, isto é, p ≤ −5ξωn. Escolhendo p = −10, obtém-se

   [img:Illustration] 

  Sendo m = 1, a função de transferência do compensador é do tipo

   [img:Illustration] 

  O sistema de equações na forma matricial é dado por

   [img:Illustration] 

  Substituindo os valores numéricos, obtém-se

   [img:Illustration] 

  ou

   [img:Illustration] 

  Portanto, a função de transferência do compensador é

   [img:Illustration] 

  Logo, a função de transferência de malha fechada Gmf(s) é dada por

   [img:Illustration] 

  Observe que o denominador de Gmf(s) está de acordo com o polinômio F(s) (8.100). Porém, o projeto não permite controle sobre o zero de Gmf(s) que, neste projeto, está localizado em s = −2,08. Quanto mais longe dos polos de malha fechada dominantes, menos influência o zero tem na resposta transitória do sistema.

  

### Imposição de polos e model matching

  Neste projeto é possível adotar o zero de malha fechada mais distante dos polos complexos conjugados dominantes, de modo que este influencie menos na resposta transitória. Assim, escolhendo o zero de malha fechada em s = −5 e o terceiro polo de malha fechada em s = −10, obtém-se

   [img:Illustration] 

  Neste projeto também é possível adotar o ganho k na Equação (8.107), de modo a obter um determinado erro estacionário. Aplicando o teorema do valor final na Equação (8.107), para que a saída estacionária seja igual à entrada numa resposta ao degrau, o ganho necessário é k = 8.

  

### • Passo 1

  Calcule

   [img:Illustration] 

  Note que B0(s) = 8s + 40 e B(s) = 1 não possuem fatores comuns para serem cancelados.

  Portanto,

   [img:Illustration] 

  

### • Passo 2

  Seja o polinômio Ap(s), escolhido com raízes no semiplano esquerdo do plano s e tal que

   [img:Illustration] 

  Como grau[Ap(s)] = 3 e como grau[Ap(s)] deve ser maior ou igual a 0, para que a condição (8.111) seja satisfeita pode-se adotar, por exemplo, grau[Ap(s)] = 0, com

   [img:Illustration] 

  

### • Passo 3

  Calcule

   [img:Illustration] 

  Sendo grau[F(s)] = 3 = n + m = 2 + m, então, m = 1. Logo,

   [img:Illustration] 

  Usando a Equação (8.48) os coeficientes dos polinômios D(s) e M(s) podem ser determinados a partir da solução do sistema linear

   [img:Illustration] 

  Portanto, as funções de transferência dos controladores são

   [img:Illustration] 

  Logo, a função de transferência de malha fechada é dada por

   [img:Illustration] 

  que está de acordo com a função de transferência especificada em (8.108).

  Na Figura 8.8 são apresentadas as respostas ao degrau unitário nas referências dos sistemas em malha fechada (8.106) e (8.121).

   [img:Illustration] 

  Figura 8.8 Respostas ao degrau unitário nas referências dos sistemas (8.106) e (8.121).

  Observe que a resposta transitória obtida com o projeto por realimentação unitária apresenta erro estacionário não nulo (e(∞) = 1 − 1,3 = −0,3) e um sobressinal maior (Mp ≅ 28%) que o especificado para ξ = 0,5 (Mp ≅ 16,3%). Isso se deve à influência do zero em s = −2,08 da função de transferência (8.106), que está próximo dos polos complexos conjugados dominantes. Já a resposta transitória obtida por model matching apresenta um sobressinal menor (Mp ≅ 17,6%) devido à menor influência do zero em s = −5 da função de transferência (8.107), que foi alocado mais distante dos polos complexos conjugados dominantes. Além disso, neste projeto o erro estacionário é nulo devido à uma escolha adequada do ganho k na Equação (8.107).

  

### 8.5 Exercícios propostos

  

### Exercício 8.4

  Considere o sistema de controle da Figura 8.1. Projete o compensador Gc(s) para cada um dos seguintes casos:

   [img:Illustration] 

  

### Exercício 8.5

  Considere o sistema de controle da Figura 8.2. Projete os compensadores Gc(s) e Gff(s) para cada um dos seguintes casos:

   [img:Illustration] 

  

### Exercício 8.6

  Refaça o Exemplo 8.5, adotando grau[Ap(s)] > 0.

  

### Exercício 8.7

  Projete um compensador por imposição de polos para um sistema em malha fechada com realimentação unitária, de modo que os polos de malha fechada dominantes tenham coeficiente de amortecimento ξ = 0,5 e frequência natural ωn = 4 (rad/s). Considere as seguintes plantas:

   [img:Illustration] 

  

### Exercício 8.8

  Refaça o Exercício 8.7 projetando compensadores por imposição de polos e model matching. Considere também a especificação de erro estacionário nulo para resposta ao degrau na referência.

  

  __________

  1Ver [2], [13] e [30].

  2Diz-se que uma matriz tem posto linha completo quando todas as suas linhas são linearmente independentes.

  3Esta condição garante que existem Gff(s) e Gc(s) próprias. Ver [2].

<!-- Text/chapter09.xhtml -->

  Controle Automático, 2ª edição
  
  
  

  

## 9

  

## Limitações de Projeto

  

### 9.1 Introdução

  Neste capítulo deseja-se discutir o problema do projeto de sistemas de controle por realimentação perante seus vários objetivos. Os conflitos resultantes conduzem à necessidade de soluções de compromisso. Será sugerida também uma sequência de decisões de projeto e de suas revisões que visa facilitar o desenvolvimento das soluções.

  É importante salientar, com relação aos projetos lineares, que

  • modelos lineares valem somente em faixas reduzidas dos sinais, fora das quais ocorrem alterações importantes;

  • o esforço de controle é limitado fisicamente em amplitude ou por questões econômicas, ou por alguma saturação;

  • a planta pode se alterar por condições ambientais e, a longo prazo, por desgaste.

  Apesar disso, é usualmente satisfatório projetar o controlador com base num dado modelo linear, válido nas condições usuais, e depois realizar estudos de robustez. Na prática atual esses estudos consistem em extensivas simulações em computador.

  É também intenção do capítulo estudar as limitações ao projeto que decorrem de plantas com fase não mínima, com atraso puro e, embora superficialmente, as que decorrem de plantas com não linearidades.

  

### 9.2 Critérios de qualidade

  A rigor, um projeto de controlador dependeria de considerar todos os possíveis sinais de referência e de perturbação previsíveis na vida do sistema. No entanto, para tornar o problema matematicamente definido adotam-se apenas alguns sinais simples, representativos dos reais: a constante, o degrau ou a rampa. Em teorias avançadas utilizam-se também representações estatísticas dos sinais.

  Para o projeto, um critério de qualidade de desempenho deve ser estabelecido. Pode ser um conjunto de exigências sobre erros estacionários, sobre amplitudes e durações dos erros transitórios, sobre faixas de passagem em frequência ou pode ser um índice chamado de "erro integral". Dentre estes, os principais referem-se à resposta ao degrau e são designados por siglas internacionais:

  • IAE : Integral do Erro Absoluto (Integral of Absolute Error) é definido como

   [img:Illustration] 

  • ISE : Integral do Erro Quadrático (Integral of Square Error) é definido como

   [img:Illustration] 

  • ITAE : Integral do Produto do Tempo pelo Erro Absoluto (Integral of Time Multiplied Absolute Error) é definido como

   [img:Illustration] 

  Um critério de qualidade mais realista, que leva em conta também o custo do esforço de controle (saída m(t) do controlador), foi proposto por N. Wiener e depois adotado em incontáveis estudos de controle ótimo. Esse critério integral compõe o quadrado do erro com o quadrado do esforço:

   [img:Illustration] 

  sendo λ uma constante positiva de ponderação ou de custo relativo. A preocupação com o esforço de controle m(t) é fundamental, pois de nada adianta projetar um sistema com resposta muito rápida ou com erro atuante muito pequeno se o correspondente valor de m(t) não pode ser atingido.

  

### 9.3 Controlabilidade

  Na concepção inicial de um sistema de controle é necessário verificar a viabilidade física do ato de controlar, isto é, verificar se existem cadeias de causa e efeito, internas ao processo, que viabilizem efeitos da variável manipulada m(t) (saída do controlador) sobre a saída do processo y(t).

  A seguir, a capacidade dos meios de controle deve ser examinada, usualmente expressa por meio de alguns conceitos de controlabilidade da literatura de controle de processo. São apresentadas duas definições de controlabilidade, ambas associadas à entrada e à saída do processo, que requerem um exame quantitativo dos recursos disponíveis. Esses conceitos são especialmente importantes no controle de sistemas multivariáveis, isto é, quando várias entradas e saídas interagem via dinâmica da planta (ver [3] e [54]).

  A condição de controlabilidade para sistemas dinâmicos SISO com n estados é apresentada no Capítulo 13.

  

### Controlabilidade estacionária

  Um sistema linear é controlável nesse sentido se a variável de saída pode ser mantida no seu valor desejado (set-point), em regime estacionário, a despeito das perturbações estacionárias previstas na especificação.

  Partindo das equações dinâmicas, a ferramenta natural para o teste dessa questão é, naturalmente, o Teorema do Valor Final.

  

### Janelas de operação

  A janela de operação no espaço das perturbações da saída é a região deste espaço cujo efeito é compensável pela variável de manipulação disponível, considerando o regime estacionário, as não linearidades e os limites da variável de manipulação ([37]).

  Por exemplo, considere um acionamento elétrico: normalmente a janela a ser considerada é bidimensional, dada pelo intervalo dos valores dos conjugados de carga no eixo, estacionários, e pelo intervalo das tensões da fonte de energia elétrica.

  Analogamente, define-se a janela de operação da entrada da planta como o intervalo necessário de valores da entrada para compensar as perturbações em regime estacionário.

  

### Controlabilidade de entrada-saída

  É a existência de pelo menos um controlador por realimentação que seja capaz de produzir desempenho estático e dinâmico aceitável para todas as perturbações esperadas na especificação (ver [54]).

  É uma qualidade da planta e da escolha das variáveis. Uma solução teórica ou analítica para este problema é difícil, e tem sido pouco estudada. A resposta prática fica por conta de tentativas de projeto e de simulações.

  

### 9.4 A complexidade dos objetivos do projeto

  Considere o diagrama de blocos de um sistema de controle por realimentação, SISO (Single Input Single Output), que está representado na Figura 9.1.

   [img:Illustration] 

  Figura 9.1 Diagrama de blocos de um sistema de controle por realimentação.

  Os principais sinais são:

  V(s): comando aplicado pelo operador para definir o sinal de referência R(s); Y(s): variável de saída que se deseja controlar;

  E(s) = R(s) − Y(s): erro;

  P(s): perturbação atuante sobre a planta;

  N(s): ruído do transdutor de medida;

  M(s): esforço de controle.

  As funções de transferência representam:

  Gp(s): processo controlado da variável de manipulação até a saída, junto com o amplificador de potência e o atuador principal;

  Gr(s): adaptador de comando, geralmente necessário por razões ergonômicas. Leva a variável

  V(s) de comando do operador à variável R(s) de referência;

  Gd(s): processo controlado, das perturbações de carga ou de energia até a saída;

  H(s): transdutor de medida da variável de saída;

  Gc(s): controlador de realimentação.

  A função de transferência do processo controlado, base para os métodos deste livro, se define após várias etapas de concepção e de construção do sistema técnico, como:

  • seleção da variável de manipulação externa m(t) que seja capaz de, por uma cadeia bem determinada de causas e efeitos, alterar o valor da variável y(t) que se deseja controlar. Em processos industriais complexos essa escolha pode não ser trivial;

  • seleção de um amplificador de potência e de um atuador que sejam fisicamente capazes de corrigir a variável y(t) frente às amplitudes das perturbações p(t) e dos comandos v(t) previstos na especificação do sistema de controle. Exemplos: para um dado acionamento mecânico, a seleção de um motor suficientemente forte e de um amplificador a tiristores; para um misturador, a seleção da bomba de um dos componentes. Esta seleção tem enorme efeito sobre os custos dos equipamentos;

  • estabelecimento da função de transferência desses componentes e da sua composição em cascata;

  • seleção de um transdutor de precisão e rapidez adequadas para medir a variável de saída.

  Exemplos: um tacogerador; um transdutor de pH; um sensor de posição linear, etc.

  

### Funções de transferência

  Para lidar com as especificações é preciso considerar simultaneamente várias funções de transferência como, por exemplo, de R(s) para Y(s), de P(s) para Y(s), de R(s) para E(s), etc. É curioso que em todas essas funções de transferência intervém a função chamada de diferença de retorno:

   [img:Illustration] 

  em que Gma(s) é a conhecida função de transferência de malha aberta.

  Foi H. Bode quem pela primeira vez observou a importância da diferença de retorno, tendo justificado este nome da seguinte forma: suponha a realimentação interrompida numa conexão qualquer entre dois blocos da malha fechada, assim criando um terminal de entrada e um de saída. Suponha um impulso unitário injetado no terminal de entrada e a medida do sinal retornado no terminal de saída. A diferença entre o sinal injetado e o retornado, levando em conta o sinal algébrico no somador, resulta igual a (9.5), pois

   [img:Illustration] 

  Do diagrama de blocos da Figura 9.1, várias funções de transferências podem ser calculadas. Desta figura tem-se que

   [img:Illustration] 

  Deduz-se facilmente que, se P(s) = N(s) = 0, a função de transferência da referência até a saída vale Y(s)

   [img:Illustration] 

  Se R(s) = P(s) = 0, a função de transferência do ruído do transdutor até a saída vale

   [img:Illustration] 

  Se R(s) = N(s) = 0, a função de transferência da perturbação de carga até a saída vale

   [img:Illustration] 

  Outras funções de transferências de interesse para os projetos são:

   [img:Illustration] 

  Uma regra mnemônica para gerar as fórmulas (9.9) a (9.17), a partir do diagrama de blocos da Figura 9.1, é a seguinte:

  
    o ganho de uma entrada (R(s), N(s) ou P(s)) até uma variável de saída (Y(s), E(s) ou M(s)) é o ganho dos blocos que se encontram no caminho, da entrada até a saída, como se não existisse realimentação, dividido pela diferença de retorno.

  

  

### 9.5 Estratégia de projeto

  Embora o problema de controle da Figura 9.1 seja usualmente considerado de uma entrada e uma saída (SISO - Single Input Single Output), há várias entradas (R(s), N(s) ou P(s)) e várias saídas (Y(s), E(s) ou M(s)) que devem ser consideradas ao mesmo tempo. O sistema usualmente chamado de SISO é na realidade multivariável (MIMO - Multi Input Multi Output).

  Usando a representação matricial e as funções de transferência (9.9) a (9.17), pode-se sintetizar matricialmente toda essa complexidade:

   [img:Illustration] 

  Apesar dos vários métodos já estudados para análise e projeto de sistemas de controle por realimentação, o projeto de um caso real é complexo e impõe uma sucessão de escolhas, análises e revisões. Nesta seção pretende-se indicar uma estratégia geral de projeto.

  Suponha que os sinais do ambiente do sistema tenham sido medidos e analisados, assim estabelecendo as faixas de frequência em que os seus conteúdos harmônicos são significativos. Sejam FR, FN e FP os extremos superiores das faixas de frequência da referência R(s), do ruído de medida N(s) e da perturbação P(s).

  Em essência, do ponto de vista frequencial o que se deseja no sistema é obter um conjunto de respostas em frequência relacionadas com esses extremos, conforme está representado nos gráﬁcos (a), (b) e (c) da Figura 9.2 e na Tabela 9.1.

   [img:Illustration] 

  Figura 9.2 Extremos superiores das faixas de frequência.

  Tabela 9.1 Objetivo geral de projeto das respostas frequenciais

  
    
      
        

        

        
      

      
        
          
            Função de transferência

          

          
            Objetivo geral

          

          
            Resposta frequencial

          
        

        
          
            E(s)/R(s)

          

          
            Reduzir erros de regime permanente

          

          
            —

          
        

        
          
            Y(s)/R(s)

          

          
            Verificar se y(t) reproduz r(t)

          

          
            Y(jω)/R(jω)|≈ 1 para 0 < ω < FR

          
        

        
          
            Y(s)/N(s)

          

          
            Reduzir efeitos de n(t) sobre y(t)

          

          
            Y(jω)/N(jω)| "pequeno" para ω > FN

          
        

        
          
            Y(s)/P(s)

          

          
            Reduzir efeitos de p(t) sobre y(t)

          

          
            Y(jω)/P(jω)| "pequeno" para 0 < ω < FP

          
        

      
    
  

  O gráﬁco (d) da Figura 9.2 destina-se a apontar que, em geral, a amplitude do esforço de controle cresce até uma frequência FE, maior que FR. Por isso, especial atenção deve ser dada à potência instantânea máxima do ampliﬁcador de potência e do atuador do sistema nas faixas dos sinais reais, isto é, de 0 a FR.

  Para conciliar todas as exigências frequenciais e temporais recomenda-se conduzir o processo de projeto de acordo com o ﬂuxograma da Figura 9.3.

   [img:Illustration] 

  Figura 9.3 Fluxograma de projeto.

  

### 9.6 Limitações por fase não mínima

  Esta característica na planta limita seriamente o desempenho atingível pelo sistema de controle por realimentação, atrasando as ações corretivas da variável manipulada, porque a variável de saída da planta reage inicialmente em sentido contrário ao esperado (ver Seções 3.8 e 5.4).

  Quanto à estabilidade, pelo lugar das raízes sabe-se que os zeros no semiplano direito do plano s, que caracterizam a fase não mínima, "atraem" as curvas para a região instável. Pelos gráﬁcos de Bode, zeros no semiplano direito produzem defasagens negativas anormalmente grandes e, portanto, instabilizantes.

  

### Exemplo 9.1

  Considere o diagrama de blocos da Figura 9.4. O processo é de fase não mínima, pois possui um zero no semiplano direito em s = 1.

   [img:Illustration] 

  Figura 9.4 Diagrama de blocos de um sistema em malha fechada.

  Na Figura 9.5 (a) e (b) são apresentados os gráﬁcos do lugar das raízes para Gc(s) = K (controlador proporcional) e  [img:Illustration]  (compensador por avanço de fase), respectivamente.

   [img:Illustration] 

  Figura 9.5 Lugar das raízes.  [img:Illustration] 

  • Para Gc(s) = K, a função de transferência de malha fechada é

   [img:Illustration] 

  Substituindo s por jω no denominador de (9.19), o polinômio característico ﬁca

   [img:Illustration] 

  Portanto, o lugar das raízes cruza o eixo imaginário em ±j para K = 1.

  • Para  [img:Illustration] , a função de transferência de malha fechada é

   [img:Illustration] 

  Substituindo s por jω no denominador de (9.21), o polinômio característico ﬁca

   [img:Illustration] 

  Portanto, o lugar das raízes cruza o eixo imaginário em  [img:Illustration] 

  Logo, com o controlador proporcional a frequência de corte é ω = 1 (rad/s), enquanto com o compensador por avanço de fase ocorre um aumento da frequência de corte para  [img:Illustration]  (rad/s). Isso também pode ser veriﬁcado nos diagramas de Bode da função de malha aberta da Figura 9.6.

   [img:Illustration] 

  Figura 9.6 Gráficos do módulo da função de malha aberta com o controlador proporcional e com o compensador por avanço de fase.

  Na Figura 9.7 são apresentadas as respostas ao degrau unitário do sistema em malha fechada com o compensador por avanço de fase. Observe que na medida em que o ganho aumenta o tempo de acomodação diminui, mas o sobressinal negativo (undershoot) aumenta.

   [img:Illustration] 

  Figura 9.7 Respostas ao degrau unitário do sistema em malha fechada com o compensador por avanço de fase.

  ■

  

### 9.7 Limitações por atraso puro

  

#### 9.7.1 Preditor de Smith

  O efeito instabilizante dos atrasos puros, que é muito presente em controle de processos industriais, foi visto nas Seções 3.9 e 5.5. Considere o sistema da Figura 9.8 em que o processo tem um atraso puro igual a α.

   [img:Illustration] 

  Figura 9.8 Sistema em malha fechada com processo com atraso puro.

  Em 1957 O. J. M. Smith propôs uma configuração de blocos para o controlador que, em teoria, sempre estabiliza a malha com atraso puro. A Figura 9.9 mostra o chamado "preditor de Smith", que consiste em uma realimentação negativa em torno do controlador Gc(s) com função de transferência (1 − e−αs)Gp(s), obtida a partir de um modelo do processo.

   [img:Illustration] 

  Figura 9.9 Sistema em malha fechada com preditor de Smith.

  Da Figura 9.9 tem-se que a função de transferência do preditor de Smith é

   [img:Illustration] 

  A função de transferência de malha fechada é

   [img:Illustration] 

  O resultado obtido em (9.24) permite rearranjar o sistema em malha fechada de acordo com o diagrama em blocos da Figura 9.10.

   [img:Illustration] 

  Figura 9.10 Diagrama de blocos equivalente ao sistema com preditor de Smith.

  Verifica-se no diagrama final da Figura 9.10 que a função de transferência de malha aberta, responsável pela estabilidade, não contém atraso. No entanto, note bem que a função de transferência de malha fechada Y(s)/R(s) mantém o efeito do atraso puro.

  Assim, basta projetar um controlador Gc(s) para o processo Gp(s) sem o atraso e, depois, implementar o preditor de Smith de acordo com a Figura 9.9. A resposta transitória y(t) é a mesma de x(t), porém com um atraso puro igual a α. Note que o preditor de Smith depende do modelo da planta. Portanto, sempre que a dinâmica da planta real se afastar do modelo a questão da estabilidade deve ser reexaminada.

  

### 9.8 Índice de desempenho ISE mínimo

  Há um resultado teórico muito eficaz que resume as limitações de desempenho devidas a zeros no semiplano direito e a atrasos puros e pode ser deduzido por meio da teoria da otimização de funcionais, aplicada ao controle de uma planta linear genérica com índice de desempenho ISE(Integral of Square Error),

   [img:Illustration] 

  sendo r(t) um degrau unitário.

  Este é um índice ideal, que supõe esforços de controle ilimitados, e sua minimização estabelece um limite que baliza os desempenhos reais possíveis.

  
    Para plantas estáveis com zeros no semiplano direito localizados em zi e um atraso puro α > 0 a função de transferência de malha fechada ótima ISE é

     [img:Illustration] 

    sendo z*i o complexo conjugado de zi e o valor ISEmin ótimo para r(t) degrau unitário (ver [41]) é

     [img:Illustration] 

  

  Note que não há realimentação capaz de produzir índice menor que α.

  Se α = 0 e há dois zeros complexos conjugados z1 = σ + jω e z2 = σ − jω, resulta o limite de desempenho

   [img:Illustration] 

  

### 9.9 Robustez perante incertezas estruturadas

  Todo projeto de sistemas de controle se apoia em modelos matemáticos da planta que nunca a representam com total fidelidade. Isso ocorre seja por dificuldades de medida, na fase de modelagem, seja por simplificações exigidas pelos métodos de projeto (linearidade e invariância no tempo, por exemplo). Deficiências dos modelos que se traduzem em valores de parâmetros são chamadas de incertezas estruturadas.

  Outro tipo de incertezas é o decorrente de uma total ausência de informação estrutural. São os componentes "parasitas" da planta e suas eventuais ressonâncias, localizadas em "altas" frequências, mas que acrescentam defasagem negativa na frequência crítica do projeto. A literatura designa essas deficiências como incertezas não estruturadas. São elas que em larga medida exigem do projetista, nos gráficos de Bode, as margens de segurança.

  Um projeto de sistema de controle dinâmico somente pode ser considerado completo quando sua robustez está comprovada, ou seja, quando estão garantidos os desempenhos especificados em presença das ﬂutuações previsíveis dos parâmetros do processo e das perturbações.

  A rigor é preciso verificar a robustez do desempenho para todos os valores possíveis dos parâmetros da planta, geralmente também associados às excursões dos sinais nas janelas de controlabilidade. Como esta é uma condição exigente, o melhor é embutir a preocupação em todo o processo de projeto. Esta ideia, que é central na experiência profissional apresentada em [31], é muito simples de realizar por meio de simulação computacional.

  

### Exemplo 9.2

  Considere o sistema da Figura 9.11, com os seguintes valores nominais para os parâmetros:

  k = 100, a = 1, b = 8 e c = 20.

   [img:Illustration] 

  Figura 9.11 Sistema em malha fechada.

  Deseja-se verificar a robustez do sistema em malha fechada quando os quatro parâmetros variam de −50% a +20%. A robustez da estabilidade deve ser avaliada perante quaisquer combinações de flutuações nos parâmetros. Portanto, devem ser feitas repetições dos gráficos utilizados no projeto e simulações de desempenho em todos os 24 = 16 vértices do paralelepípedo tetradimensional percorrido pelos parâmetros.

  Na Tabela 9.2 estão representadas todas as combinações dos parâmetros. Observe que as combinações 1 e 16 resultam em funções de transferência iguais.

  Tabela 9.2 Variações especificadas para os parâmetros no teste de robustez

  
    
      

      

      

      

      
    

    
      
        
          Casos

        

        
          1

        

        
          2

        

        
          3

        

        
          4

        

        
          5

        

        
          6

        

        
          7

        

        
          8

        

        
          9

        

        
          10

        

        
          11

        

        
          12

        

        
          13

        

        
          14

        

        
          15

        

        
          16

        
      

      
        
          k

        

        
          50

        

        
          50

        

        
          50

        

        
          50

        

        
          50

        

        
          50

        

        
          50

        

        
          50

        

        
          120

        

        
          120

        

        
          120

        

        
          120

        

        
          120

        

        
          120

        

        
          120

        

        
          120

        
      

      
        
          a

        

        
          0,5

        

        
          0,5

        

        
          0,5

        

        
          0,5

        

        
          1,2

        

        
          1,2

        

        
          1,2

        

        
          1,2

        

        
          0,5

        

        
          0,5

        

        
          0,5

        

        
          0,5

        

        
          1,2

        

        
          1,2

        

        
          1,2

        

        
          1,2

        
      

      
        
          b

        

        
          4

        

        
          4

        

        
          9,6

        

        
          9,6

        

        
          4

        

        
          4

        

        
          9,6

        

        
          9,6

        

        
          4

        

        
          4

        

        
          9,6

        

        
          9,6

        

        
          4

        

        
          4

        

        
          9,6

        

        
          9,6

        
      

      
        
          c

        

        
          10

        

        
          24

        

        
          10

        

        
          24

        

        
          10

        

        
          24

        

        
          10

        

        
          24

        

        
          10

        

        
          24

        

        
          10

        

        
          24

        

        
          10

        

        
          24

        

        
          10

        

        
          24

        
      

    
  

  Na Figura 9.12 é apresentada a Carta de Nichols1 para os sistemas com os parâmetros da Tabela 9.2. Note que o sistema em malha fechada é instável em cinco casos (5, 9, 13, 14 e 15), pois as margens de ganho e fase são negativas. Nas demais combinações o sistema em malha fechada é estável.

  Na Figura 9.13 são apresentadas as respostas ao degrau unitário dos casos em que o sistema em malha fechada é estável. Para facilitar a visualização e a análise, os gráficos foram divididos em dois grupos. As respostas mais amortecidas e com menor sobressinal ocorrem quando os parâmetros variam de acordo com os casos 2, 4, 6, 8, 10 e 12.

   [img:Illustration] 

  Figura 9.12 Carta de Nichols para os sistemas com os parâmetros da Tabela 9.2.

   [img:Illustration] 

  Figura 9.13 Respostas ao degrau unitário.

  ■

  

### 9.10 Não linearidades

  Os métodos de projeto linear sofrem da restrição de serem válidos unicamente para modelos lineares. Os sistemas reais sempre apresentam fenômenos não lineares, desde uma simples variação "suave" do ganho com a amplitude do sinal de entrada até efeitos radicais como a saturação, a "folga de engrenagens", a zona morta, o atrito seco ou de Coulomb, todos não exprimíveis por equações lineares.

  Na Seção 9.10.1 é exposto o método dos modelos incrementais para analisar sistemas contendo um bloco não linear "suave" nas vizinhanças de um ponto de trabalho.

  Nas Seções 9.10.2 a 9.10.5 descrevem-se algumas das outras não linearidades. Para estas existe a chamada linearização para grandes sinais senoidais e a chamada função descritiva, que se baseia em supor o componente sujeito a entradas senoidais e em reter apenas a primeira harmônica da transformada de Fourier da saída. A análise dos erros dessa aproximação deve ser feita por meio do cálculo das harmônicas de ordem superior. Uma óbvia aplicação das funções descritivas é o seu emprego como respostas em frequência nos critérios de estabilidade de Nyquist ou Bode, embora esses critérios passem a ser apenas uma condição necessária, mas não suficiente para a estabilidade. A instabilidade pode surgir via harmônicas de ordem superior ([11]).

  Na Seção 9.10.6 trata-se da simulação em computador, que é a solução prática para lidar com não linearidades nos projetos de controle dinâmico.

  

#### 9.10.1 Linearização para pequenos sinais

  Componentes estáticos não lineares podem ter sua descrição matemática linearizada, ou seja, substituída por uma aproximação linear, desde que os sinais excursionem pouco em torno de um dado ponto.

  Considere um elemento genérico com variável de excitação X e variável de resposta Y. Seja o seu modelo matemático Y = g(X), não linear, e seja um ponto de operação designado por (X0,Y0), perto do qual excursionam as variáveis X e Y. Se a função g(X) é contínua, ela pode ser desenvolvida em série de Taylor em (X0,Y0):

   [img:Illustration] 

  Sendo (X − X0) "pequeno", os termos de potência mais elevada influenciam menos. Uma aproximação razoável para Y(X) pode ser

   [img:Illustration] 

  A Equação 9.30 representa no plano (X, Y) uma reta pelo ponto de trabalho (X0,Y0), tangente à curva Y = g(X) em (X0,Y0). Embora seja uma reta do ponto de vista gráfico, se não passa pela origem do plano a função da aproximação é ainda uma função não linear. No entanto, se as variáveis originais são substituídas pelas seguintes variáveis incrementais, y = Y −Y0 e x = X −X0, a função representativa do componente passa a ser linear,2 ou seja,

   [img:Illustration] 

  Portanto, para obter um modelo incremental a partir de um não linear são necessários dois passos: calcular a derivada primeira da saída relativa à entrada, no ponto de trabalho, e trocar as variáveis originais pelas incrementais.

  

### Exemplo 9.3

  Considere um tanque industrial de líquido aberto, conforme mostrado na Figura 9.14. A variável de entrada é a vazão de entrada Qe (m3/min) e a variável de saída é o nível do líquido H (m) no tanque. A vazão de saída Qs (m3/min) depende não linearmente do nível H. A secção horizontal do reservatório é C (m2), constante. Deseja-se um modelo linear para a relação causal entre pequenos sinais de vazão de entrada Qe e de nível H.

   [img:Illustration] 

  Figura 9.14 Tanque industrial.

  Sabe-se que, em primeira aproximação, a vazão de saída é proporcional à raiz quadrada da altura da coluna do líquido, sendo que K é uma constante da válvula de saída:

   [img:Illustration] 

  Desenvolvendo g(H) em série de Taylor no ponto (Qs0,H0), conforme a Equação (9.30), obtém-se

   [img:Illustration] 

  Como g(H0) = Qs0 e

   [img:Illustration] 

  então,

   [img:Illustration] 

  Adotando as notações qs(t) para (Qs − Qs0) e h(t) para (H − H0), tem-se a função linear

   [img:Illustration] 

  Seja qe(t) uma pequena flutuação de Qe em torno de Qe0 e seja Cdh(t) o volume de líquido acumulado no tanque. Em um pequeno intervalo de tempo dt, por um balanço de volume,

   [img:Illustration] 

  Logo, a equação diferencial do processo é

   [img:Illustration] 

  Aplicando a transformada de Laplace, obtém-se a seguinte função de transferência

   [img:Illustration] 

  ■

  

#### 9.10.2 Saturação

  Um elemento de saturação deixa passar um sinal sem distorção se a amplitude do sinal de entrada estiver dentro de limites máximo E e mínimo −E. Se o sinal de entrada estiver fora desses limites, então o sinal de saída irá apresentar um valor fixo (KE ou −KE). A curva característica estática de uma saturação simétrica ideal é apresentada na Figura 9.15.

   [img:Illustration] 

  Figura 9.15 Curva característica estática de uma saturação simétrica ideal.

  Esta não linearidade é descrita por

   [img:Illustration] 

  A Figura 9.16 mostra o efeito da saturação sobre uma entrada x(t) senoidal com amplitude suficientemente grande para alcançar o nível E de saturação.

   [img:Illustration] 

  Figura 9.16 Saída de um elemento de saturação quando a entrada é um sinal senoidal para K > 1.

  Todo equipamento real apresenta saturação, pois a amplitude do sinal de saída deve ser finita. Equipamentos bem selecionados ou sistemas de controle bem projetados em geral evitam a entrada em saturação. Excetuam-se projetos em que deliberadamente o esforço de controle é chaveado entre dois valores extremos, como, por exemplo, na técnica de controle não linear no espaço de estados, chamada de sliding mode control (ver [27]).

  

#### 9.10.3 Relé

  É uma não linearidade de duas posições do tipo liga-desliga (on-off). A curva característica de um relé simétrico ideal é apresentada na Figura 9.17.

   [img:Illustration] 

  Figura 9.17 Curva característica de um relé simétrico ideal.

  Esta não linearidade é descrita por

   [img:Illustration] 

  A Figura 9.18 mostra a saída y(t) de um relé simétrico quando a entrada x(t) é um sinal senoidal.

   [img:Illustration] 

  Figura 9.18 Saída de um relé simétrico quando a entrada é um sinal senoidal.

  Um caso extremo de amplificador com saturação é o relé, cuja característica corresponde à da saturação quando o coeficiente K tende a infinito, pois neste caso a saída já salta para os valores extremos com entradas muito pequenas. Amplificadores com essa característica são muito frequentes em eletrônica de potência, nos amplificadores chaveados dos inversores e dos choppers.

  

#### 9.10.4 Zona morta

  A saída deste elemento não linear é nula dentro de uma região de –E a E, que é chamada de zona morta. Fora desta região a saída reproduz a entrada sem distorção. A curva característica de uma zona morta é apresentada na Figura 9.19.

   [img:Illustration] 

  Figura 9.19 Curva característica de uma zona morta ideal.

  Esta não linearidade é descrita por

   [img:Illustration] 

  A Figura 9.20 mostra a saída y(t) de uma zona morta ideal quando a entrada x(t) é um sinal senoidal.

   [img:Illustration] 

  Figura 9.20 Saída de uma zona morta ideal quando a entrada é um sinal senoidal de período T.

  

#### 9.10.5 Folga de engrenagens (backlash)

  Backlash é uma não linearidade característica das engrenagens que é muito importante em controle automático de posição. A Figura 9.21 (a) mostra o esquema de uma folga entre duas engrenagens (A e B), e a Figura 9.21 (b) mostra a curva característica estática da não linearidade.

   [img:Illustration] 

  Figura 9.21 (a) Folga entre engrenagens. (b) Curva característica estática.

  Suponha uma folga F entre os dentes de uma roda tracionadora A e os dentes de uma roda tracionada B. Quando a velocidade da roda A troca de sentido o contato entre dentes deixa de existir durante o percurso da folga. Nesta fase a roda tracionada B fica parada ou se move por inércia. Depois o contato volta a existir, mas a roda B se move "atrasada" em relação à roda A. Como todos os fenômenos ocorrem nos dois sentidos a curva característica é simétrica, gerando F/2 na velocidade positiva de A e F/2 na velocidade negativa de A.

  A simulação de um movimento senoidal das rodas é mostrado na Figura 9.22. Os pontos a, b, c e d indicam os momentos de começo e fim dos efeitos da folga. Em cada instante, a distância entre as posições x e y vale F/2, que corresponde à metade da folga física entre os dentes.

   [img:Illustration] 

  Figura 9.22 Simulação de um movimento senoidal com folga de engrenagens.

  

#### 9.10.6 Efeitos sobre a estabilidade

  Pensando na estabilidade dos sistemas com realimentação e blocos não lineares, em primeira aproximação ocorre considerar apenas as harmônicas fundamentais dos sinais e analisar a estabilidade pelos diagramas de Bode. Neste caso, as não linearidades que oferecem efeito instabilizante são as que produzem defasagem da harmônica fundamental. Das não linearidades anteriores é fácil apontar a folga de engrenagens como a mais propensa a esse efeito.

  Mas oscilações não lineares podem justificar-se fora do âmbito frequencial de Nyquist e Bode. No passado muitos desses fenômenos foram estudados em sistemas de até segunda ordem, empregando o chamado plano de fase (ver[11]).

  Atualmente, a melhor forma de analisar os sistemas de controle com não linearidades é por meio de simulações em computador, que são muito facilitadas pelo uso de programas como o Simulink do MATLAB. Nesse caso a programação é feita por meio de um diagrama de blocos, em que é possível selecionar cada bloco não linear a ser analisado.

  

### Exemplo 9.4

  Considere o diagrama de blocos da Figura 9.23, que representa um sistema de controle de posição de um servomecanismo com folga de engrenagens.

   [img:Illustration] 

  Figura 9.23 Sistema de controle de posição de um servomecanismo com folga de engrenagens.

  A Figura 9.24 mostra simulações das respostas ao degrau unitário do sistema em malha fechada com e sem a presença do backlash, com valor F = 0,1. Observe que na resposta em que a folga das engrenagens está presente ocorre uma oscilação permanente, com amplitude e frequência constantes, caracterizando assim, um fenômeno tipicamente não linear.

   [img:Illustration] 

  Figura 9.24 Respostas ao degrau unitário do sistema em malha fechada.

  ■

  

### 9.11 Estudo de caso: antena de radar

  Deseja-se projetar um sistema de controle de posição para uma antena de radar meteorológico, como ilustrado na Figura 9.25.

   [img:Illustration] 

  Figura 9.25 Antena de radar meteorológico. Cortesia da Atmos Sistemas Ltda. Ver [1].

  No diagrama esquemático da Figura 9.26 o ângulo θA indica a posição angular da torre em torno do eixo vertical e caracteriza a chamada posição azimutal que se deseja controlar com precisão. O ângulo θm indica a posição angular do eixo do motor de acionamento.

  Deseja-se projetar um compensador para a posição azimutal θA a partir da atuação do motor CC indicado na figura. Por razões práticas, especifica-se que a medida da posição θA seja feita indiretamente, por meio de um transdutor que meça a posição θm.

   [img:Illustration] 

  Figura 9.26 Esquema da antena de um radar meteorológico.

  As especificações dinâmicas do sistema de controle são as seguintes:

  i) Margem de ganho maior ou igual a 10 dB;

  ii) Margem de fase maior ou igual a 30o;

  iii) Atenuação de −30 dB para ruídos a partir de 490 (rad/s);

  iv) Ganho na frequência de ressonância inferior a −10 dB;

  v) Erro estacionário menor ou igual a 1% para sinal de referência do tipo rampa unitária.

  Os valores numéricos dos parâmetros indicados na Figura 9.26 são:

  JA = 770 (kg · m2): momento de inércia do sistema formado pelo eixo de azimute + antena;

  Jm = 0,0038 (kg · m2): momento de inércia do conjunto motor + engrenagens;

  N = 464: fator de redução de velocidade do motor para o eixo da antena;

  K = 38 · 106 (N · m/rad): coeficiente de rigidez do eixo de azimute + antena;

  B = 44 (N · m · s/rad): coeficiente de amortecimento do eixo de azimute + antena.

  Do lado do motor é considerada a sua inércia, desprezados a rigidez e o atrito. Os parâmetros elétricos do motor são:

  La = 0,0038 H: indutância de armadura;

  Ra = 0,56 Ω: resistência de armadura;

  Kt = 0,56 (N · m/A): constante de torque do motor;

  Kv = 0,45 (V · s/rad): constante da força contraeletromotriz.

  As variáveis dinâmicas importantes do motor são:

  τm: torque do motor;

  ea: tensão de armadura;

  ia: corrente de armadura;

  ev : força contraeletromotriz.

  Na Figura 9.27 é mostrado um diagrama esquemático da modelagem matemática do sistema mecânico formado pelo eixo do motor, engrenagens, eixo da antena e a antena propriamente dita. A modelagem da parte mecânica fica reduzida a uma mola de torção que conecta as duas inércias rotacionais JA e Jm.

   [img:Illustration] 

  Figura 9.27 Diagrama esquemático para o modelo da planta.

  As equações diferenciais do sistema mecânico são:

   [img:Illustration] 

  As equações diferenciais do motor CC são:

   [img:Illustration] 

  A força contraeletromotriz ev(t) interliga o sistema mecânico ao motor e aparece no motor devido à carga. Aplicando a transformada de Laplace nas Equações (9.43) e (9.44), com condições iniciais nulas, obtém-se:

   [img:Illustration] 

  Substituindo a Equação (9.49) na Equação (9.48), tem-se que

   [img:Illustration] 

  ou

   [img:Illustration] 

  Sabendo-se que a velocidade angular Ωm(s) do motor é Ωm(s) sΘm(s), obtém-se a função de transferência

   [img:Illustration] 

  Substituindo a corrente de armadura da Equação (9.46) na Equação (9.45) e aplicando a transformada de Laplace, com condições iniciais nulas, obtém-se a função de transferência

   [img:Illustration] 

  Da Equação (9.49) obtém-se a função de transferência

   [img:Illustration] 

  O diagrama de blocos da planta completa (antena+motor) é mostrado na Figura 9.28, sendo explicitada a realimentação interna do motor devida à força contraeletromotriz Ev(s) e à velocidade angular do motor Ωm(s).

   [img:Illustration] 

  Figura 9.28 Diagrama de blocos da planta completa (antena+motor).

  É interessante observar que no estado estacionário, isto é, com velocidades e acelerações nulas, a Equação (9.44) resulta θA(t) = θm(t)/N. Assim, como o radar meteorológico opera com velocidades e acelerações muito baixas pode-se considerar que a posição θA(t) é medida pelo transdutor localizado em θm(t).

  A função de transferência, tendo como entrada a tensão de armadura Ea(s) e como saída a velocidade angular Ωm(s), é dada por

   [img:Illustration] 

  sendo

   [img:Illustration] 

   [img:Illustration] 

  Assim, a planta Gp(s) possui dois zeros complexos conjugados z1 e z2, localizados em

   [img:Illustration] 

  e cinco polos p1, p2, p3, p4 e p5, localizados em

   [img:Illustration] 

  Se for empregado um controlador proporcional Kc para controlar a saída Θm(s) da planta Gp(s), o lugar das raízes tem o aspecto da Figura 9.29.

   [img:Illustration] 

  Figura 9.29 Lugar das raízes de KcGp(s).

  Analisando a Figura 9.29 pode-se verificar que o sistema em malha fechada apresenta polos complexos conjugados muito pouco amortecidos, mesmo para pequenos valores de ganho. Assim, conclui-se que o compensador para atender às especificações de projeto não pode ser apenas um controlador do tipo proporcional.

  

### Controle com realimentação auxiliar de velocidade

  Servomecanismos com ressonância na carga são um problema de controle difícil. Daí a adoção tradicional da realimentação auxiliar da velocidade Ωm(s), além da realimentação da posição Θm(s), conforme é mostrado na Figura 9.30. Deve-se destacar que um tacogerador tem custo adicional, mas é normalmente muito eficaz.

   [img:Illustration] 

  Figura 9.30 Sistema de controle com realimentação da velocidade Ωm(s) e da posição Θm(s).

  Do diagrama da Figura 9.30 tem-se a seguinte função de transferência:

   [img:Illustration] 

  Supondo que o ganho da realimentação auxiliar de velocidade seja unitário (Ka = 1), então

   [img:Illustration] 

  Assim, a função de transferência (9.63) possui os mesmos zeros da planta Gp(s) e cinco polos:

   [img:Illustration] 

  Na Figura 9.31 é mostrado o lugar das raízes de

   [img:Illustration] 

  Nota-se agora que, para valores pequenos do ganho Kc, os polos de malha fechada se tornaram um pouco mais amortecidos.

   [img:Illustration] 

  Figura 9.31 Lugar das raízes de Gma(s).

  Para atender à especificação de erro estacionário para entrada rampa unitária (R(s) = 1/s2) menor ou igual a 1% tem-se, pelo teorema do valor final,

   [img:Illustration] 

  Logo, Kc ≥ 145. Na Figura 9.32 são apresentados os gráficos de Bode para o sistema em malha aberta Gma(s), com Kc = 145.

   [img:Illustration] 

  Figura 9.32 Diagramas de Bode de Gma(jω) para Kc = 145.

  Analisando a Figura 9.32 verifica-se que o gráfico da fase cruza a linha de −180o em três frequências: 146, 222 e 362 (rad/s). A frequência de 222 (rad/s) corresponde à frequência dos zeros de Gma(s), ou seja, é a frequência em que Gma(s) se anula. Nas frequências de 146 e 362 (rad/s) o valor de | Gma(jω)| (dB) é aproximadamente o mesmo. Com isso, a margem de ganho vale MG ≅ 3,5 dB, que é inferior aos 10 dB especificados.

  A margem de fase MF ≅ 29o é medida na frequência em que o ganho cruza a linha de 0 dB, ou seja, em 120 (rad/s). Logo, a margem de fase está próxima dos 30o especificados.

  O ganho na frequência de 490 (rad/s) vale aproximadamente −21 dB, sendo portanto insuficiente para a atenuação de ruídos, especificada como −30 dB.

  A frequência de ressonância corresponde ao pico máximo do gráfico do módulo e ocorre aproximadamente em 353 (rad/s). Nesta frequência o ganho é de −3 dB, que é superior aos −10 dB da especificação.

  Na Figura 9.33 é mostrada a resposta de θm(t) para um degrau unitário na referência. Constatase forte oscilação no período do transitório e um sobressinal máximo elevado (Mp ≅ 40%).

   [img:Illustration] 

  Figura 9.33 Resposta θm(t) para um degrau unitário na referência.

  Para que as especificações de atenuação de ganho na frequência de ressonância e de ruídos sejam satisfeitas é necessário reduzir o ganho em altas frequências. Algumas soluções podem ser consideradas a partir desse ponto:

  • usar como controlador um filtro passa-baixas com função de transferência

   [img:Illustration] 

  para frequências acima de, por exemplo, 10 (rad/s). Ao mesmo tempo em que esse filtro produz uma redução de ganho nas frequências superiores a 10 (rad/s) também produz um atraso de fase e, portanto, deve ser avaliado com cuidado;

  • projetar um compensador por atraso de fase

   [img:Illustration] 

  de forma a produzir uma redução de ganho. É preciso ficar atento ao fato de que tal compensador produz um pequeno atraso de fase em frequências próximas da frequência crítica 0 dB e, portanto, pode afetar a margem de fase.

  

### Controle por meio de filtro passa-baixas

  O diagrama de blocos do sistema de controle com um filtro passa-baixas é apresentado na Figura 9.34.

   [img:Illustration] 

  Figura 9.34 Sistema de controle por meio de filtro passa-baixas.

  Definindo a função de malha aberta

   [img:Illustration] 

  o erro estacionário para R(s) = 1/s2 é dado por

   [img:Illustration] 

  Sendo Θm(s)/Rm(s) dada pela Equação (9.63) e adotando Kc = 145, a especificação de erro estacionário é satisfeita, pois e(∞) = 0,01.

   [img:Illustration] 

  Figura 9.35 Diagramas de Bode de Gma(jω) para Kc = 145 e pc = 10 no filtro passa-baixas.

  A constante pc do filtro passa-baixas Gc(s) corresponde à frequência a partir da qual ocorrerá uma atenuação de ganho e um atraso de fase. Na Figura 9.35 são mostrados os gráficos de Bode de Gma(s) para pc = 10. Verifica-se que tanto a margem de ganho de 5 dB como a margem de fase de 8o são inadequadas.

  Se for adotado um valor maior para a constante pc, como, por exemplo, entre 10 e 100, a margem de ganho será menor que os 5 dB obtidos. Conclui-se, portanto, que o filtro passa-baixas é inadequado para satisfazer a todas as especificações de projeto.

  

### Compensador por atraso de fase

  O diagrama de blocos do sistema de controle com um compensador por atraso de fase é apresentado na Figura 9.36.

   [img:Illustration] 

  Figura 9.36 Sistema de controle com compensador por atraso de fase.

  Adotando Kc = 145, o erro estacionário é e(∞) = 0,01 para R(s) = 1/s2. Logo,

   [img:Illustration] 

  Com o controlador Kc verifica-se na Figura 9.32 que o ganho vale −21 dB na frequência de 490 (rad/s). Para que a atenuação de ruídos seja de −30 dB o ganho deve cair 9 dB. Esta redução faz com que o ganho na frequência de ressonância diminua para −3 − 9 = −12 dB, satisfazendo à especificação de −10 dB. Além disso, a redução de ganho faz com que a especificação da margem de ganho seja também satisfeita, aumentando aproximadamente 9 dB.

  Logo,

   [img:Illustration] 

  Em altas frequências

   [img:Illustration] 

  Na Figura 9.37 são apresentados os diagramas de Bode de  [img:Illustration]  para Kc = 145. Verifica-se que o ganho vale 9 dB na frequência de aproximadamente 37 (rad/s). Nesta frequência a fase vale −100o. Escolhendo o zero do compensador uma década abaixo dessa frequência, obtém-se T = 1/3,7 ≅ 0,27. Portanto, a função de transferência do compensador resulta como

   [img:Illustration] 

  Na Figura 9.38 são mostrados os diagramas de Bode de  [img:Illustration] . Nota-se que a margem de ganho vale 12 dB e a margem de fase é de 75o. Observe que mesmo com o atraso de fase introduzido pelo compensador a margem de fase aumentou. Isso se justifica devido à redução de ganho que o compensador produziu. Além disso, verifica-se que o ganho no pico de ressonância é de −12 dB e que nas frequências acima de 490 (rad/s) a atenuação é de pelo menos −30 dB. Resulta, assim, que o compensador (9.76) atende a todas as especificações.

   [img:Illustration] 

  Figura 9.37 Diagramas de Bode de  [img:Illustration]  para Kc = 145.

   [img:Illustration] 

  Figura 9.38 Diagramas de Bode de  [img:Illustration] .

  Na Figura 9.39 é mostrada a resposta de θm(t) para um degrau unitário na referência. Comparando-se com a Figura 9.33, constata-se melhora significativa no período de transitório.

   [img:Illustration] 

  Figura 9.39 Resposta θm(t) para um degrau unitário na referência.

  

### Avaliação de robustez do compensador por atraso de fase

  Para avaliação de robustez do compensador por atraso de fase são mostrados, na Figura 9.40, os gráficos de Bode resultantes para diversas combinações de valores de parâmetros da antena. Foram consideradas oito combinações possíveis para variações de ±10% em torno dos valores nominais dos parâmetros Ra, Kt e B. Medidas precisas a partir desses gráficos indicam variações de 11,3 dB a 13,1 dB para as margens de ganho e variações de 72,6o a 77,1o para as margens de fase, as quais se mantêm, portanto, em valores aceitáveis para as especificações de projeto.

   [img:Illustration] 

  Figura 9.40 Diagramas de Bode de  [img:Illustration]  para variações de ±10% em torno dos valores nominais dos parâmetros Ra, Kt e B.

  

### 9.12 Exercícios resolvidos

  

### Exercício 9.1

  O diagrama de blocos da Figura 9.41 representa um servomecanismo com realimentação unitária e amplificador chaveado a relé. Utilizando um programa computacional, simule o sistema em malha fechada com e sem a presença do relé.

   [img:Illustration] 

  Figura 9.41 Servomecanismo com realimentação unitária e amplificador chaveado a relé.

  Solução

  Aplicando um degrau unitário na referência e simulando o sistema por meio do Simulink do MATLAB são obtidos os gráficos da Figura 9.42. Observe a oscilação frequente da saída quando o bloco do relé está presente.

   [img:Illustration] 

  Figura 9.42 Respostas ao degrau unitário do sistema em malha fechada.

  Para eliminar as oscilações da saída uma solução é implementar um compensador por avanço de fase com função de transferência

   [img:Illustration] 

  Simulando o sistema não linear em malha fechada com e sem o compensador obtêm-se os gráficos da Figura 9.43.

   [img:Illustration] 

  Figura 9.43 Respostas ao degrau unitário do sistema em malha fechada com relé.

  

### Exercício 9.2

  O esquema de um sistema de levitação eletromagnética é apresentado na Figura 9.44. O sistema consiste em um eletroímã que suspende uma massa m de material magnético. A levitação da massa é obtida por meio do controle da distância X do entreferro existente entre a massa e o eletroímã.

   [img:Illustration] 

  Figura 9.44 Sistema de levitação eletromagnética.

  Sabe-se que a força produzida pelo eletroímã é dada por

   [img:Illustration] 

  sendo I a corrente elétrica que circula pela bobina, e K uma constante que depende do número de espiras e da área da seção transversal do eletroímã. Deseja-se determinar a função de transferência do sistema que tem como entrada a corrente I e como saída a distância X.

  Solução

  Sendo g a aceleração da gravidade, a força resultante FR(X, I) na massa m é

   [img:Illustration] 

  Expandindo a força FR(X, I) na série de Taylor de ordem 1, no ponto de equilíbrio (X0, I0), obtém-se

   [img:Illustration] 

  Adotando as notações fR(t) = FR(X, I) − FR(X0, I0), x(t) = X − X0 e i(t) = I − I0, tem-se a função linear

   [img:Illustration] 

  No ponto de equilíbrio de forças tem-se da Equação (9.79) que

   [img:Illustration] 

  Da Equação (9.81) obtém-se

   [img:Illustration] 

  Portanto, a função de transferência é dada por

   [img:Illustration] 

  

### Exercício 9.3

  Considere um processo de produção de barras de alumínio em que o alumínio líquido escorre de um forno basculante para um molde resfriado a água. O forno é lentamente girado por meio de um pistão hidráulico e a base do molde é lentamente abaixada por meio de outro pistão hidráulico, conforme é esquematizado na Figura 9.45.

   [img:Illustration] 

  Figura 9.45 Processo de produção de barras de alumínio.

  É fundamental que a temperatura do alumínio esteja adequada ao chegar ao molde. Um transdutor de temperatura é instalado nesse ponto e serve de base para um controle a realimentação, cuja atuação se faz por meio de um queimador de óleo ou gás. Entre o transdutor e o forno há um atraso de transporte que não pode ser negligenciado na questão da estabilidade da malha.

  Supõe-se que a massa M no forno seja constante, isto é, que a quantidade de alumínio que forma a barra é pequena, relativamente a M. Supõe-se ainda que o forno seja termicamente isolado e que a temperatura do alumínio no seu interior seja constante.

  Sejam:

  θi(t) (oC): temperatura do alumínio no interior do forno;

  θo(t) (oC): temperatura do alumínio no molde;

  h(t) (cal/s): taxa de aquecimento de calor no forno;

  M (kg): massa do alumínio contido no forno;

  q = 0,005 (kg/s): vazão de alumínio pela calha;

  c = 200 [cal/(kg oC)]: calor específico do alumínio;

  C = 1000 (cal/oC): capacitância térmica da massa M de alumínio no forno;

  d = 5 (m): distância entre o forno e o molde;

  v = 0,05 (m/s): velocidade de escoamento na calha.

  a) Determine a função de transferência Θo(s)/H(s) do processo.

  b) Projete um controlador de modo que a resposta transitória da malha fechada seja mais rápida que a da malha aberta e que o erro estacionário seja nulo para referência do tipo degrau.

  c) Analise a robustez do sistema em malha fechada, quando a constante de tempo e o atraso puro da planta variam de −20% a +20%.

  Solução

  

### a) Função de transferência do processo.

  A equação de balanço energético no forno é dada por

   [img:Illustration] 

  Aplicando a transformada de Laplace, com condições iniciais nulas, obtém-se

   [img:Illustration] 

  cuja função de transferência é

   [img:Illustration] 

  Admitindo-se que não há perdas ao longo da calha, tem-se que

   [img:Illustration] 

  Logo, a função de transferência do processo com entrada H(s) e saída Θo(s) é

   [img:Illustration] 

  O processo é relativamente lento por natureza e o problema principal de controle é o atraso puro.

  

### b) Projeto do controlador

  Para atender às especificações de projeto, pode-se sintonizar um controlador PI por meio da regra SIMC 1. Desse modo, a função de transferência da planta pode ser escrita como

   [img:Illustration] 

  Sendo K = 1, τ = 1000, α = 100 e supondo τc = 2α, as constantes do controlador PI são

   [img:Illustration] 

  Portanto, a função de transferência do controlador PI é

   [img:Illustration] 

   [img:Illustration] 

  Figura 9.46 Respostas ao degrau unitário.

  Na Figura 9.46 são apresentadas as respostas ao degrau unitário na referência com o controlador PI e a resposta ao degrau unitário do sistema em malha aberta sem controlador. Comparando os gráficos, observa-se que ambas as respostas possuem erro estacionário nulo. Porém, o transitório com controlador é bem mais rápido que o transitório sem controlador.

  

### c) Análise da robustez

  Na Tabela 9.3 estão representadas as combinações de flutuações da constante de tempo τ e do atraso puro α da planta, quando esses parâmetros variam de −20% a +20%.

  Tabela 9.3 Variações especificadas para os parâmetros da planta

  
    
      
        

        

        

        

        
      

      
        
          
            Casos

          

          
            1

          

          
            2

          

          
            3

          

          
            4

          
        

        
          
            α

          

          
            80

          

          
            120

          

          
            80

          

          
            120

          
        

        
          
            τ

          

          
            800

          

          
            800

          

          
            1200

          

          
            1200

          
        

      
    
  

  Na Figura 9.47 são apresentadas as Cartas de Nichols3 obtidas a partir da malha aberta formada pelo controlador (9.93) e pela planta com os parâmetros da Tabela 9.3. Observe que a malha fechada é estável em todas as possibilidades, pois as margens de ganho e fase são positivas. Com exceção do caso 1 as respostas ao degrau unitário na referência apresentam um pequeno sobressinal, conforme pode-se observar na Figura 9.48.

   [img:Illustration] 

  Figura 9.47 Cartas de Nichols desenhadas por meio dos parâmetros da planta da Tabela 9.3.

   [img:Illustration] 

  Figura 9.48 Respostas ao degrau unitário nas referências dos sistemas em malha fechada.

  

### Exercício 9.4

  Projete um preditor de Smith para o processo de fundição do Exercício 9.3, de modo que a constante de tempo da malha fechada seja 10 vezes menor que a constante de tempo do processo e que o erro estacionário seja nulo para entrada de referência do tipo degrau.

  Solução

  Inicialmente, projeta-se um controlador Gc(s) para o sistema sem atraso  [img:Illustration]  conforme é mostrado na Figura 9.49.

   [img:Illustration] 

  Figura 9.49 Diagrama de blocos do sistema com o atraso fora da malha fechada.

  Para satisfazer as especificações de projeto pode-se utilizar um controlador PI. Adotando o parâmetro TI = 1000, de modo que o zero do controlador cancele o polo de Gp(s), a função de transferência do controlador resulta como

   [img:Illustration] 

  A função de transferência da malha fechada é dada por

   [img:Illustration] 

  Para que a constante de tempo da malha fechada seja 10 vezes menor que a constante de tempo do processo, basta adotar Kc = 10. O preditor de Smith deve ser implementado de acordo com a Figura 9.9, cuja função de transferência é

   [img:Illustration] 

  Na Figura 9.50 são apresentadas as respostas ao degrau unitário na referência com o preditor de Smith e a resposta ao degrau unitário da malha aberta sem o preditor. Comparando os gráficos observa-se que ambas as respostas possuem erro estacionário nulo. Porém, o transitório com o preditor é bem mais rápido que o transitório sem o preditor.

   [img:Illustration] 

  Figura 9.50 Respostas ao degrau unitário.

  

### 9.13 Exercícios propostos

  

### Exercício 9.5

  O pêndulo da Figura 9.51 está sujeito à gravidade g, sem atrito, e obedece ao equilíbrio de forças

   [img:Illustration] 

  sendo θ(t) a posição angular do pêndulo, em radianos. Calcular o seu modelo incremental em Θ0 = 0 e em Θ0 = π/4.

   [img:Illustration] 

  Figura 9.51 Pêndulo simples.

  

### Exercício 9.6

  O servomecanismo da Figura 9.52 tem saturação no amplificador de potência. Usando um programa computacional, compare a resposta y(t) ao degrau unitário com a do sistema sem saturação. Observe que a resposta do sistema não linear é similar a do linear, porém mais lenta.

   [img:Illustration] 

  Figura 9.52 Servomecanismo com realimentação unitária e saturação.

  

### Exercício 9.7

  Considere o caso da antena de radar da Seção 9.11 com um transdutor de posição medindo diretamente o ângulo θA(t). Admitindo as mesmas especificações dinâmicas, projete um compensador Gc(s) por avanço e atraso de fase de acordo com a Figura 9.53. Observe que o produto G3(s)G4(s)/s produz um modelo simplificado para a planta.

   [img:Illustration] 

  Figura 9.53 Diagrama de blocos do sistema em malha fechada.

  

  __________

  1As simulações computacionais das Figuras 9.12 e 9.13 foram obtidas por meio do programa MATLAB.

  2Uma função y(x) é linear se y(a1x1 + a2x2) = a1y(x1) + a2y(x2), com a1 e a2 constantes.

  3As simulações computacionais das Figuras 9.47 e 9.48 foram obtidas por meio do programa MATLAB.

<!-- Text/chapter10.xhtml -->

  
  Controle Automático, 2ª edição
  
  

  

## 10

  

## Sistemas de Tempo Discreto

  

### 10.1 Introdução

  Os sinais eletrônicos podem ser divididos em dois grupos:

  • sinais de tempo contínuo ou analógicos: definidos em qualquer instante pertencente ao intervalo de observação; representam-se matematicamente por funções f(t), t ∊ R;

  • sinais de tempo discreto ou amostrados: definidos apenas em determinados instantes do intervalo de observação; matematicamente, se os instantes são periódicos com período de amostragem T tais sinais se representam por sequências f(kT), k = 0, 1, 2, 3, . . . , k ∊ N.

  Os sinais de tempo discreto podem ser originalmente discretos ou resultantes da amostragem de sinais analógicos. Considere, por exemplo, o registro das variações da temperatura atmosférica ao longo de um dia. No gráfico da Figura 10.1 (a) pode-se notar que a temperatura f(t) assume valores em qualquer instante ao longo das 24 horas de um dia, formando um gráfico de linha contínua ao longo do tempo t. Por outro lado, se a temperatura for anotada de hora em hora, em um processo de amostragem, o sinal f(t) converte-se no sinal discreto f(kT) mostrado na Figura 10.1 (b).

   [img:Illustration] 

  Figura 10.1 Registro de temperaturas em um dia. (a) Tempo contínuo. (b) Tempo discreto.

  O sinal discreto da Figura 10.1 (b) pode, por sua vez, ser convertido num sinal digital. Os sinais digitais são resultantes da conversão da amplitude dos sinais de tempo discreto por meio de algum tipo de código binário, ou seja, usando apenas elementos 0 e 1.

  

### 10.2 Transformada Z

  A transformada Z é uma aplicação que faz corresponder uma função da variável complexa z a uma sequência de números. A transformada Z corresponde, no caso discreto, à transformada de Laplace no caso contínuo. A definição da transformada Z é a seguinte:

  Definição 10.1 Dada uma função f(t), t ≥ 0, amostrada com período T, ou uma sequência infinita de números f (0), f(T), f (2T), f (3T), . . . , f(kT), . . . , a transformada Z é a série de potências1

   [img:Illustration] 

  sendo z uma variável complexa e k ∊ N.

  Interessa saber em que condições a série (10.1) converge. Prova-se que se | f(kT) |≤ ck para alguma constante c > 0, isto é, se a sequência f(kT) cresce no máximo geometricamente, então a série converge para | z |> c. Para | z |> c, F(z) é então uma função analítica de z, isto é, tem derivadas de qualquer ordem. Usando o princípio da continuação analítica, F(z) é definível mesmo nos pontos z tais que | z |< c. Sempre que possível, a transformada Z será considerada estendida a todo o plano z.

  

#### 10.2.1 Transformada Z de algumas funções

  

### Impulso unitário

  A sequência impulso unitário ou δ(kT) de Kronecker é definida como

   [img:Illustration] 

  O gráfico desta sequência é apresentado na Figura 10.2.

   [img:Illustration] 

  Figura 10.2 Impulso unitário.

  Aplicando a definição (10.1) para k ≥ 0, obtém-se

   [img:Illustration] 

  

### Degrau unitário

  A sequência degrau unitário é definida como

   [img:Illustration] 

  O gráfico desta sequência é apresentado na Figura 10.3.

   [img:Illustration] 

  Figura 10.3 Degrau unitário.

  Aplicando a definição (10.1) para k ≥ 0, obtém-se

   [img:Illustration] 

  Para | z |> 1, a série (10.5) representa a soma dos termos de uma progressão geométrica com razão z−1 e primeiro termo igual a 1. Logo,

   [img:Illustration] 

  

### Rampa unitária

  A função rampa unitária é definida como

   [img:Illustration] 

  O gráfico desta sequência é apresentado na Figura 10.4.

   [img:Illustration] 

  Figura 10.4 Rampa unitária.

  Aplicando a definição (10.1) para k ≥ 0, obtém-se

   [img:Illustration] 

  A expressão (10.8) pode ser escrita como

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  

### Função exponencial

  A função exponencial é dada por

   [img:Illustration] 

  Para t = kT e k ≥ 0,

   [img:Illustration] 

  

### Sequência ak

  A sequência ak é dada por

   [img:Illustration] 

   [img:Illustration] 

  

### Função seno

  A função seno é dada por

   [img:Illustration] 

  Para t = kT e k ≥ 0, de (10.12) tem-se que

   [img:Illustration] 

  

### Função cosseno

  A função cosseno é dada por

   [img:Illustration] 

  Para t = kT e k ≥ 0, de (10.12) tem-se que

   [img:Illustration] 

  

### Exemplo 10.1

  Deseja-se obter a transformada Z da função cuja transformada de Laplace é

   [img:Illustration] 

  Expandindo a Equação (10.21) em frações parciais, obtém-se

   [img:Illustration] 

  cuja transformada inversa é dada por

   [img:Illustration] 

  Logo, a transformada Z de f(t), amostrada com período T, é dada por

   [img:Illustration] 

  ■

  

#### 10.2.2 Algumas propriedades e teoremas da transformada Z

  

### Propriedade 10.1 Linearidade

  A transformada Z é uma aplicação linear. De fato, sendo f(k) e g(k) duas sequências e α e β dois números reais, tem-se que

   [img:Illustration] 

  

### Propriedade 10.2 Atraso

  Dadas as sequências f(k) e g(k), sendo a última obtida por translação da primeira para depois (Figura 10.5 (a) e 10.5 (b)), isto é,

   [img:Illustration] 

  Então,

   [img:Illustration] 

  Definindo m = k − n e dado que g(k) = 0 para k < n, obtém-se

   [img:Illustration] 

  Portanto,

   [img:Illustration] 

  A propriedade (10.29) permite considerar a variável complexa z−n como um operador de atraso n, aplicável às sequências temporais, que será muito útil na representação de sistemas dinâmicos.

  

### Exemplo 10.2

  Considere a sequência

   [img:Illustration] 

  e a sequência g(k) atrasada de duas unidades de tempo, isto é,

   [img:Illustration] 

  Então,

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  ■

  

### Propriedade 10.3 Avanço

  Dada a sequência f(k) e seja ĥ(k) obtida por translação de f(k) para antes (Figura 10.5 (a) e

   [img:Illustration] 

  Como a definição da transformada Z não admite termos da sequência com índice k < 0, é necessário truncar ĥ(k), obtendo-se a sequência truncada h(k) da Figura 10.5 (d), dada por

   [img:Illustration] 

  Assim,

   [img:Illustration] 

  Definindo m = k + n, então

   [img:Illustration] 

  Portanto,

   [img:Illustration] 

  A propriedade (10.37) permite considerar a variável complexa zn como um operador de avanço n, aplicável às sequências temporais com a devida atenção ao truncamento.

   [img:Illustration] 

  Figura 10.5 (a) Sequência f(k). (b) Sequência g(k) = f(k − 2) com atraso de duas unidades de tempo. (c) Sequência ĥ(k) = f(k + 2) com avanço de duas unidades de tempo. (d) Sequência h(k) = ĥ(k) para k ≥ 0.

  

### Exemplo 10.3

  Considere as sequências h(k) = k +2 e f(k) = k. Então,

   [img:Illustration] 

  Loga,

   [img:Illustration] 

  ■

  

#### 10.2.3 Teorema do valor inicial

  Seja F(z) a transformada Z de uma função f(t), então o valor inicial f (0) de f(t) é dado por

   [img:Illustration] 

  De fato,

   [img:Illustration] 

  Fazendo z →∞ na Equação (10.41), obtém-se o valor inicial f (0).

  

### Exemplo 10.4

  Determine o valor inicial de uma função f(k), cuja transformada Z é dada por

   [img:Illustration] 

  Pelo teorema do valor inicial

   [img:Illustration] 

  De fato,

   [img:Illustration] 

  ■

  

#### 10.2.4 Teorema do valor final

  Supondo que f(k) = 0 para k < 0 e que existe

   [img:Illustration] 

  então o valor final de f(k) é dado por

   [img:Illustration] 

  Para mostrar este teorema, basta considerar que

   [img:Illustration] 

  Subtraindo a Equação (10.46) da (10.47) e calculando o limz→1(1 − z−1)F(z), obtém-se

   [img:Illustration] 

  

### Exemplo 10.5

  Determine o valor final de uma função f(k) cuja transformada Z é dada por

   [img:Illustration] 

  Pelo teorema do valor final

   [img:Illustration] 

  De fato,

   [img:Illustration] 

  ■

  

### 10.3 Função de transferência

  Num sistema discreto no tempo a entrada u(k) e a saída y(k) são sequências de números, sendo portanto suscetíveis de representação por transformadas Z. A descrição matemática fundamental de um sistema dinâmico discreto no tempo é uma equação de diferenças. No caso de ser linear e invariante no tempo ela é do tipo

   [img:Illustration] 

  sendo n a ordem do sistema, e ai (i = 0, . . . , n − 1) e bj (j = 0, . . . , m − 1) constantes, com m ≤ n.

  Aplicando a propriedade (10.3) do avanço na Equação (10.52), obtém-se

   [img:Illustration] 

  Supondo condições iniciais nulas

   [img:Illustration] 

  obtém-se

   [img:Illustration] 

  
    A função de transferência G(z) é definida como a razão das transformadas Z da saída Y(z) e da entrada U(z) do sistema supondo condições iniciais nulas (c.i. = 0), ou seja,

     [img:Illustration] 

  

  Logo, a função de transferência é dada por

   [img:Illustration] 

  Note que G(z) independe dos sinais de entrada e saída, desde que haja condições iniciais nulas. G(z) depende apenas dos parâmetros ai (i = 0, . . . , n − 1), bj (j = 0, . . . , m) e das ordens n e m. Um sistema discreto, linear e invariante no tempo G(z), com entrada U(z) e saída Y(z), é apresentado na Figura 10.6.

   [img:Illustration] 

  Figura 10.6 Sistema G(z) com entrada U(z) e saída Y(z).

  Assim como no caso dos sistemas contínuos, os pontos do plano z em que a função G(z) ou suas derivadas tendem ao infinito são os polos de G(z). Já os pontos em que a função G(z) se anula são os zeros de G(z). No caso de G(z) ser racional, como na Equação (10.57), tem-se que

  
    • os polos são as raízes do polinômio do denominador de G(z), e

    • os zeros são as raízes do polinômio do numerador de G(z).

  

  Uma outra forma equivalente de expressar a função de transferência (10.57) é através de potências negativas de z. Para isso basta multiplicar o numerador e o denominador da Equação (10.57) por z−n, ou seja,

   [img:Illustration] 

  

#### 10.3.1 Álgebra de blocos

  É fácil verificar que valem para as funções de transferência em z as mesmas regras de álgebra de blocos que as das funções de transferência em s.

  

### 10.4 Resposta impulsiva

  Supondo que a entrada U(z) do sistema da Figura 10.6 seja um impulso unitário no instante zero, então U(z) = 1. Da Equação (10.58) resulta que Y(z) = G(z), ou seja, a função de transferência do sistema é igual à transformada Z da saída.

  Dividindo-se o numerador pelo denominador na Equação (10.58), obtém-se

   [img:Illustration] 

  Diz-se que um sistema é causal quando as suas respostas sempre ocorrem após ou simultaneamente com as entradas. Uma função de transferência é dita realizável fisicamente quando corresponde a um sistema causal.

  Assim, aplicando a propriedade do atraso (10.29) na Equação (10.59), obtém-se a sequência y(k), dada por

   [img:Illustration] 

  Para que a função de transferência G(z) das Equações (10.57) ou (10.58) seja fisicamente realizável, é necessário que δ[k − (n − m)] ocorra em n − m ≥ 0, ou seja, n ≥ m. Logo, o grau do denominador de G(z) deve ser maior ou igual ao grau do seu numerador, ou o número n de polos de G(z) deve ser maior ou igual ao seu número m de zeros.

  

### 10.5 Transformada Z inversa

  Deseja-se determinar a sequência f(k), cuja transformada Z é uma dada função F(z). A sequência f(k) é dita transformada Z inversa e pode ser obtida através dos seguintes métodos:

  • expansão em série por divisão contínua;

  • programa de computador;

  • expansão em frações parciais.

  

#### 10.5.1 Expansão em série por divisão contínua

  A expansão em série de potências da função F(z) consiste na simples divisão contínua do polinômio do numerador pelo polinômio do denominador.

  

### Exemplo 10.6

  Determine f(k) para k = 0, 1, 2, 3, 4, 5 quando F(z) é dada por

   [img:Illustration] 

  Escrevendo F(z) com potências negativas de z, obtém-se

   [img:Illustration] 

  Dividindo o numerador pelo denominador da Equação (10.62), obtém-se

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  Conforme se pode notar, este método fornece diretamente os elementos da série e não uma expressão geral para a sequência f(k).

  ■

  

#### 10.5.2 Programa de computador

  Consiste em determinar numericamente a sequência f(k) a partir de uma equação de diferenças implementada dentro de um laço de repetição de um programa de computador. Para obter a equação de diferenças supõe-se que F(z) seja uma função de transferência com entrada impulsiva e condições iniciais nulas.

  

### Exemplo 10.7

  Determine f(k) para k = 0, 1, 2, 3, 4, 5 quando F(z) é dada por

   [img:Illustration] 

  Supondo que F(z) é a saída de um sistema com entrada impulsiva (U(z) = 1) e com condições iniciais nulas, então

   [img:Illustration] 

  Escrevendo F(z) em termos de potências negativas de z, obtém-se

   [img:Illustration] 

  Aplicando a transformada inversa e a propriedade (10.29) do atraso, obtém-se a equação de diferenças

   [img:Illustration] 

  Sabendo-se que f(−1) = f(−2) = f(−3) = 0 e que u(k) é um impulso, ou seja,

   [img:Illustration] 

  os valores de f(k) (k = 0, 1, 2, 3, . . .) podem ser calculados por meio de uma implementação da Equação (10.67) num programa de computador.

  A seguir é apresentado o trecho de um programa escrito na linguagem C.

  Tabela 10.1 Programa e coeficientes para k = 0, 1, 2, . . . , 10

   [img:Illustration] 

  

#### 10.5.3 Expansão em frações parciais

  Considere a função

   [img:Illustration] 

  O método da expansão em frações parciais consiste em expandir a função da Equação (10.69) em frações que podem ser facilmente identificáveis na tabela de transformadas Z (10.2). A diferença deste método com relação aos dois anteriores é que o resultado da transformação inversa da função F(z) é uma função f(k).

  

### Polos distintos

  Se F(z) possuir pelo menos um zero na origem (b0 = 0) e apenas polos distintos, então pode-se realizar a seguinte expansão:

   [img:Illustration] 

  onde cada coeficiente ai (i = 1, 2, . . . , n) pode ser calculado como

   [img:Illustration] 

  Após a expansão F(z) pode ser escrita como

   [img:Illustration] 

  A inversa de F(z) é a soma das inversas

   [img:Illustration] 

  A expansão de F(z)/z visa apenas facilitar a identificação das frações expandidas na tabela de transformadas Z. Caso F(z) não possua pelo menos um zero na origem o método também pode ser aplicado, ou seja,

   [img:Illustration] 

  Pela propriedade do atraso (10.29) tem-se que

   [img:Illustration] 

  Se F(z) possuir polos complexos conjugados, então cada polo complexo também pode ser manipulado como sendo uma raiz distinta.

  

### Polos múltiplos

  Se F(z) possui um polo p com multiplicidade m, então devem ser desenvolvidas m frações associadas a p, ou seja,

   [img:Illustration] 

  Prova-se que cada constante bj (j = 1, 2, . . . , m) pode ser calculada como

   [img:Illustration] 

  A Equação (10.76) também se aplica no caso de F(z) possuir polos complexos conjugados múltiplos.

  

### Exemplo 10.8

  Determine a transformada Z inversa de

   [img:Illustration] 

  Note que F(z) possui um zero na origem e um polo múltiplo em z = 1 com multiplicidade m = 2.

  a) F(z)/z pode ser expandida em frações parciais do seguinte modo:

   [img:Illustration] 

  sendo

   [img:Illustration] 

  Portanto,

   [img:Illustration] 

  Da tabela de transformadas Z obtém-se

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  b) Outro modo de obter os coeficientes da expansão F(z)/z é através de uma identificação dos coeficientes do polinômio do numerador antes e depois da expansão em frações parciais. Assim,

   [img:Illustration] 

  Identificando

   [img:Illustration] 

  ou seja,

   [img:Illustration] 

  A Equação (10.86) tem solução quando

   [img:Illustration] 

  Resolvendo o sistema (10.87) obtêm-se os mesmos resultados que em (10.79), (10.80) e (10.81), ou seja,

   [img:Illustration] 

  c) Em vez de expandir a função F(z)/z pode-se também expandir F(z), isto é,

   [img:Illustration] 

  sendo

   [img:Illustration] 

  Portanto,

   [img:Illustration] 

  Aplicando a propriedade do atraso (10.29) na Equação (10.92), obtém-se a seguinte transformada Z inversa

   [img:Illustration] 

  A Equação (10.93) também pode ser escrita como

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  que é igual à f(k) da Equação (10.83).

  ■

  Tabela 10.2 Tabela de transformadas Z e de Laplace

   [img:Illustration] 

  Tabela 10.3 Teoremas e propriedades da transformada Z

   [img:Illustration] 

  

### 10.6 Exercícios resolvidos

  

### Exercício 10.1

  Determine a transformada Z da sequência f(k) da Tabela 10.4.

  Tabela 10.4 Sequência f(k)

  
    
      
        

        

        

        

        

        

        

        

        

        

        
      

      
        
          
            k

          

          
            0

          

          
            1

          

          
            2

          

          
            3

          

          
            4

          

          
            5

          

          
            6

          

          
            •

          

          
            •

          

          
            •

          
        

        
          
            f(k)

          

          
            0

          

          
            1

          

          
            2

          

          
            3

          

          
            0

          

          
            0

          

          
            0

          

          
            •

          

          
            •

          

          
            •

          
        

      
    
  

  Solução

  Aplicando a definição de transformada Z,

   [img:Illustration] 

  

### Exercício 10.2

  A resposta y(k) de um sistema para uma entrada u(k) do tipo impulso unitário está apresentada na Tabela 10.5. Determine a função de transferência G(z) = Y(z)/U(z) e uma expressão para y(k).

  Tabela 10.5 Resposta y(k)

  
    
      
        

        

        

        

        

        

        

        

        
      

      
        
          
            k

          

          
            0

          

          
            1

          

          
            2

          

          
            3

          

          
            4

          

          
            •

          

          
            •

          

          
            •

          
        

        
          
            y(k)

          

          
            2

          

          
            1

          

          
            0,5

          

          
            0,25

          

          
            0,125

          

          
            •

          

          
            •

          

          
            •

          
        

      
    
  

  Solução

  Aplicando a definição de transformada Z,

   [img:Illustration] 

  A Equação (10.97) representa a soma dos termos de uma progressão geométrica com razão 0,5z−1 e primeiro termo igual a 2. Para | z |> 1, há convergência. Assim,

   [img:Illustration] 

  Como a entrada u(k) é um impulso unitário, então U(z) = 1. Logo,

   [img:Illustration] 

  Da tabela de transformadas Z (10.2) obtém-se

   [img:Illustration] 

  

### Exercício 10.3

  Um sistema dinâmico é descrito pela equação de diferenças

   [img:Illustration] 

  Supondo que u(k) é um degrau unitário determine:

  a) a transformada Z da sequência y(k);

   [img:Illustration] 

  Solução

  a) Aplicando a propriedade (10.37) do avanço na Equação (10.101), obtém-se

   [img:Illustration] 

  Como y(0) = y(1) = 0, então

   [img:Illustration] 

  Como u(k) é um degrau unitário, então Z[u(k)] = z/(z − 1). Logo,

   [img:Illustration] 

  b) Aplicando o teorema do valor final na Equação (10.104), obtém-se

   [img:Illustration] 

  

### Exercício 10.4

  Dado

   [img:Illustration] 

  determine a transformada Z inversa.

  Solução

  • Por meio de expansão em série por divisão contínua

  Escrevendo F(z) com potências negativas de z, obtém-se

   [img:Illustration] 

  Dividindo o numerador pelo denominador, tem-se que

   [img:Illustration] 

  Logo, f(0) = 0, f(1) = 1, f(2) = 7, f(3) = 17, f(4) = 25, f(5) = 21, . . .

  • Por meio de programa de computador

  Supondo que F(z) é a função de transferência de um sistema e que sua entrada é o impulso U(z) = 1, então

   [img:Illustration] 

  Aplicando a propriedade (10.29) do atraso, obtém-se

   [img:Illustration] 

  Sabendo-se que f(−1) = f(−2) = f(−3) = 0 e que u(k) é um impulso, então a Equação (10.110) pode ser implementada num programa de computador.

  A seguir é apresentado o trecho de um programa, escrito na linguagem C, que calcula os valores da sequência f(k) para k = 0, 1, 2, . . . , 10.

  Tabela 10.6 Programa e coeficientes para k = 0, 1, 2, . . . , 10

   [img:Illustration] 

  • Por meio de expansão em frações parciais

  F(z)/z pode ser expandida em frações parciais do seguinte modo

   [img:Illustration] 

  sendo a*2 o complexo conjugado de a2.

   [img:Illustration] 

  Portanto,

   [img:Illustration] 

  Da tabela de transformadas Z obtém-se

   [img:Illustration] 

  Como

   [img:Illustration] 

  então,

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  Assim,

   [img:Illustration] 

  Quando a função F(z) possui polos complexos conjugados pode-se realizar a expansão de acordo com termos tabelados, ou seja,

   [img:Illustration] 

  Necessariamente,

   [img:Illustration] 

  ou

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  Da tabela de transformadas Z (10.57) obtém-se

   [img:Illustration] 

  Escrevendo a Equação (10.123) de modo a utilizar as funções tabeladas (10.124) e (10.125), obtém-se

   [img:Illustration] 

  Comparando as Equações (10.124), (10.125) e (10.126), tem-se que

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  Portanto, a transformada Z inversa de F(z) é dada por

   [img:Illustration] 

  

### 10.7 Exercícios propostos

  

### Exercício 10.5

  Determine a transformada Z das funções seno e cosseno amortecido, definidos por

   [img:Illustration] 

  

### Exercício 10.6

  Supondo um período de amostragem T = 1s, determine a transformada Z da função f(t) da Figura 10.7.

   [img:Illustration] 

  Figura 10.7 Função f(t).

  

### Exercício 10.7

  Considere um sistema com entrada u(k) e saída y(k). Quando a entrada é um impulso unitário a saída é o sinal apresentado na Figura 10.8.

   [img:Illustration] 

  Figura 10.8 Saída y(k) para entrada impulso unitário.

  a) Determine a função de transferência G(z) = Y(z)/U(z).

  b) Quais são os polos de G(z)?

  c) Supondo que a entrada u(k) é um degrau unitário, calcule o valor estacionário da saída pelo teorema do valor final.

  d) Determine a resposta y(k) da saída quando a entrada u(k) for um degrau unitário.

  e) Desenhe o gráfico da sequência y(k) correspondente.

  

### Exercício 10.8

  Um sistema discreto com entrada u e saída y é representado pela equação de diferenças

  y(k) = 1,3y(k − 1) − 0,4y(k − 2) + u(k − 2).

  a) Calcule y(0), y(1), y(2), y(3), y(4) e y(5), quando a entrada é um degrau unitário.

  b) Determine a função de transferência G(z) = Y(z)/U(z).

  c) Quais são os polos de G(z)?

  d) Supondo que a entrada é um degrau unitário, calcule o valor estacionário da saída pelo teorema do valor final.

  e) Determine a resposta analítica y(k) para a saída, quando a entrada é um degrau unitário.

  

### Exercício 10.9

  Dado

   [img:Illustration] 

  determine a transformada Z inversa por meio de

  • expansão em série por divisão contínua;

  • programa de computador;

  • expansão em frações parciais.

  

### Exercício 10.10

  Dada a função de transferência

   [img:Illustration] 

  sabendo-se que a entrada U(z) é do tipo degrau unitário, determine a transformada Z inversa da saída Y(z) por meio de

  • expansão em série por divisão contínua;

  • programa de computador;

  • expansão em frações parciais.

  

### Exercício 10.11

  Determine a solução f(k) da seguinte equação de diferenças

  f(k + 2) + 3f(k + 1) + 2f(k) = 0, com f(0) = 0, f(1) = 1.

  Verifique o resultado obtido, calculando f(k) para k = 0, . . . , 5 por meio dos métodos da divisão contínua e por meio de um programa de computador.

  

### Exercício 10.12

  Dado um sistema dinâmico descrito pela equação de diferenças

  y(k + 2) + 2y(k + 1) + y(k) = u(k), com y(0) = y(1) = 0 ,

  sabendo-se que u(k) = k, determine a solução y(k).

  Verifique o resultado obtido calculando y(k) para k = 0, . . . , 5 por meio dos métodos da divisão contínua e por meio de um programa de computador.

  

  __________

  1A rigor esta é a transformada Z unilateral, que só se aplica a sequências f(t) para t ≥ 0. Ver [29].

<!-- Text/chapter11.xhtml -->





  
  Controle Automático, 2ª edição
  



  

## 11


  

## Sistemas de Controle Digital


  

### 11.1 Introdução


  A Figura 11.1 apresenta o diagrama de blocos de um sistema de controle digital com realimentação. A planta é o sistema dinâmico a ser controlado. O atuador é o dispositivo de potência, através do qual o controlador consegue atuar na planta. O sensor é o elemento de medição, que converte uma grandeza física da saída da planta num sinal eletrônico. O sinal proveniente da saída do sensor é um sinal analógico que é convertido para digital por meio de um conversor A/D. Da mesma forma, o sinal digital proveniente da saída do controlador é convertido para analógico por meio de um conversor D/A. O sincronismo de conversão dos sinais é realizado por um relógio. A referência, ou set-point, é ajustada internamente ao "computador"1.


   [img:Illustration] 


  Figura 11.1 Diagrama de blocos de um sistema de controle digital.


  Uma configuração alternativa para o sistema de controle digital é apresentada na Figura 11.2, onde a referência é ajustada externamente ao "computador" e as dinâmicas do atuador, da planta e do sensor são representadas por meio de um único bloco, denominado processo.


   [img:Illustration] 


  Figura 11.2 Diagrama de blocos de um sistema de controle digital.


  Os sistemas de controle digital são portanto híbridos, no sentido de que neles comparecem tanto sinais discretos quanto contínuos no tempo. O analista tem obviamente duas opções para descrever a dinâmica do sistema em malha fechada: totalmente por transformada de Laplace ou totalmente por transformada Z. Neste capítulo mostra-se que a primeira opção não é viável, apesar de que em alguns blocos a análise espectral de Fourier dê informações importantes. Já a segunda opção é viável com algumas aproximações.


  

### 11.2 Conversor A/D


  O conversor A/D tem a função de converter um sinal analógico y(t) num sinal y(kT) discreto no tempo e discreto em amplitude, conforme representado na Figura 11.3. O sinal y(kT) é discreto em amplitude porque é expresso em código binário, em número finito de dígitos. Esse fato significa que em geral y(kT) representa o sinal no instante kT com algum erro ou incerteza.


   [img:Illustration] 


  Figura 11.3 Conversor A/D.


  Um amostrador também pode ser representado simplificadamente por uma chave que amostra um sinal contínuo y(t) a cada T períodos de amostragem, conforme a Figura 11.4.


   [img:Illustration] 


  Figura 11.4 Representação simplificada de um amostrador.


  Assim, o conversor A/D consiste em duas etapas subsequentes: a amostragem, que converte um sinal analógico y(t) numa sequência de pulsos y(kT), e a conversão das amplitudes desses pulsos num sinal digital.


  

### 11.3 Conversor D/A


  O conversor D/A, representado na Figura 11.5, é um dispositivo eletrônico que tem a função de converter uma sequência de entrada u(kT) num sinal de tempo contínuo u(t), isto é, que assume valores em qualquer instante t.


   [img:Illustration] 


  Figura 11.5 Representação de um conversor D/A.


  Há vários métodos de conversão de um sinal digital em analógico, sendo que o mais usual recebe o nome de segurador de ordem zero. Dada uma sequência de entrada u(kT), o conversor D/A ou segurador de ordem zero gera na sua saída um sinal u(t), conforme indicado na Figura 11.6. O termo "ordem zero" decorre do fato de a função u(t) ser aproximada em cada intervalo [kT, (k + 1)T] por um valor constante, ou seja, por um polinômio de ordem zero.


   [img:Illustration] 


  Figura 11.6 Entrada u(kT) e saída u(t) de um conversor D/A de ordem zero.


  Analiticamente, define-se


   [img:Illustration] 


  ou seja, u(t) é uma função constante por trechos e contínua à direita.


  Na prática, não é comum o emprego de conversores de ordem maior que zero devido às dificuldades que surgem no sistema de controle devido à geração de ruídos de alta frequência.


  

### 11.4 Análise frequencial da amostragem e da recuperação


  Matematicamente é conveniente representar o processo de amostragem em duas partes, conforme é mostrado na Figura 11.7. O sinal analógico f(t) é modulado (multiplicado) por um trem de impulsos s(t) produzindo o sinal amostrado f*(t), que depois é convertido para o código digital, resultando em f(kT).


   [img:Illustration] 


  Figura 11.7 Conversor A/D ideal.


  O sinal s(t) é o trem de impulsos dado por


   [img:Illustration] 


  sendo δ(t − kT) a função delta de Dirac, que é igual a zero, exceto em t = kT .


  Sendo o sinal s(t) periódico, este pode ser representado através da série de Fourier


   [img:Illustration] 


  Os coeficientes ck da série de Fourier são dados por


   [img:Illustration] 


  sendo ωA = 2π/T a frequência de amostragem.


  Das expressões (11.2) e (11.4), obtém-se


   [img:Illustration] 


  Como no intervalo de integração da Equação (11.5), o impulso ocorre apenas em k = 0, então


   [img:Illustration] 


  Introduzindo o resultado (11.6) na Equação (11.3), obtém-se


   [img:Illustration] 


  De acordo com a Figura 11.7, o sinal amostrado f*(t) é dado por


   [img:Illustration] 


  Da Equação (11.7) tem-se que


   [img:Illustration] 


  Aplicando a transformada de Laplace na Equação (11.9), obtém-se


   [img:Illustration] 


  Fazendo s = jw na Equação (11.10), obtém-se


   [img:Illustration] 


  Este resultado mostra que o espectro de frequência de um sinal amostrado f*(t) consiste em repetidas cópias do espectro de frequência de f(t), deslocadas de múltiplos inteiros da frequência de amostragem ωA.


   [img:Illustration] 


  Figura 11.8 (a) Espectro de frequência do sinal original. (b) Espectro de frequência do sinal amostrado quando ωA > 2ωN. (c) Espectro de frequência do filtro passa-baixas ideal. (d) Reconstrução do sinal original a partir do sinal amostrado quando ωA > 2ωN. (e) Espectro de frequência do sinal amostrado quando ωA ≤ 2ωN, mostrando a sobreposição de bandas.


  Na Figura 11.8 (a) é apresentado o espectro de frequência |F(jω)| do sinal original, suposto com banda limitada, onde a componente não nula de maior frequência ocorre na frequência2 ωN. A Figura 11.8 (b) apresenta o espectro de frequência |F*(jω)| do sinal amostrado quando


   [img:Illustration] 


  Para ωA > 2ωN não ocorre sobreposição de bandas quando as cópias de F(jω) são adicionadas. Consequentemente o sinal f(t) pode ser recuperado a partir do sinal amostrado f*(t) através de um filtro passa-baixas ideal com o espectro de frequência Gi(jω)| da Figura 11.8 (c).


  Da Figura 11.9 tem-se que


   [img:Illustration] 


   [img:Illustration] 


  Figura 11.9 Recuperação de um sinal contínuo através de um filtro ideal.


  Se o filtro passa-baixas ideal Gi(jω) possui ganho T e frequência de corte ωC tal que


   [img:Illustration] 


  então,


   [img:Illustration] 


  Se a desigualdade (11.12) não for válida, ou seja, se ωA ≤ 2ωN, então irá ocorrer uma sobreposição de bandas, conforme mostrado na Figura 11.8 (e). Neste caso o sinal u(t) não irá representar o sinal de entrada original, apresentando uma distorção denominada aliasing.


  
    Teorema 11.1 Teorema de amostragem de Shannon.


    Seja f(t) um sinal de banda limitada tal que F(jω) = 0 para ω > ωN. Então, o sinal f(t) pode ser determinado a partir de suas amostras f(kT), se


     [img:Illustration] 


    sendo ωA = 2π/T.

  


  Portanto, para recuperar o sinal original sem distorção a partir do sinal amostrado com frequência ωA é necessário que ωA/2 seja maior que todas as frequências presentes no sinal original. Na prática recomenda-se um amplo coeficiente de segurança na escolha da frequência de amostragem, como, por exemplo, ωA ≥ 10ωN.


  

### Exemplo 11.1


  No processo de amostragem da função f(t) = sen(t), que possui frequência de 1 (rad/s), se a frequência de amostragem for ωA = 4/3 (rad/s), o sinal amostrado f(kT) resulta com frequência de 1/3 (rad/s), que é diferente do sinal original, conforme é mostrado na Figura 11.10 (a).


  Se a frequência de amostragem ωA for igual ao dobro da frequência de f(t), o sinal amostrado f(kT) pode ser sempre nulo e não representar sinal algum, conforme se vê na Figura 11.10 (b).


   [img:Illustration] 


  Figura 11.10 (a) Amostragem com ωA = 4/3 (rad/s). (b) Amostragem com ωA = 2 (rad/s).


  ■


  

### 11.5 Subsistema A/D + controlador + D/A


  Considere o subsistema da Figura 11.11, formado pelo conjunto A/D + controlador + D/A. Conforme mencionado anteriormente, o conversor A/D possui a função de amostrador e o conversor D/A possui usualmente a função de segurador de ordem zero.


   [img:Illustration] 


  Figura 11.11 Subsistema A/D + controlador + D/A.


  Não é possível descrever este subsistema por meio da transformada de Laplace, pois os sinais envolvidos nesses blocos são analógicos e digitais. Porém, supondo que o controlador apenas transfere a saída do conversor A/D para o conversor D/A, sem efetuar cálculo algum, ou seja, f(kT) = u(kT), pode-se representar o subsistema por um amostrador e por um segurador de ordem zero conforme a Figura 11.12.


   [img:Illustration] 


  Figura 11.12 Representação de um amostrador e segurador de ordem zero sem controlador.


  

#### 11.5.1 Função de transferência do segurador de ordem zero


  Da Figura 11.12 tem-se que a função de transferência do segurador de ordem zero é dada por


   [img:Illustration] 


  Quando a entrada f*(t) é um impulso, a saída u(t) é um pulso que corresponde a um degrau unitário d(t) no instante zero menos um degrau unitário d(t − T) no instante T, conforme mostrado na Figura 11.13.


   [img:Illustration] 


  Figura 11.13 Pulso de saída u(t).


  Logo, a transformada de Laplace de u(t) é dada por


   [img:Illustration] 


  Como F*(s) = 1, então a função de transferência do segurador de ordem zero é dada por


   [img:Illustration] 


  

### 11.6 Filtro ideal e segurador de ordem zero


  Conforme apresentado na Seção (11.4), o processo de amostragem introduz no domínio da frequência um número infinito de componentes, além da componente principal. Para filtrar essas componentes excedentes em altas frequências seria necessária a implementação de um filtro passabaixas ideal com o espectro de frequência da Figura 11.14.


   [img:Illustration] 


  Figura 11.14 Espectro de frequência de um filtro passa-baixas ideal.


  A Figura 11.15 apresenta o espectro de frequência de um sinal antes e depois da filtragem.


   [img:Illustration] 


  Figura 11.15 Filtragem de um sinal através de um filtro ideal.


  O espectro de frequência de um filtro passa-baixas ideal é dado por


   [img:Illustration] 


  Aplicando a transformada inversa de Fourier em (11.20), obtém-se


   [img:Illustration] 


  A função (11.21) representa a resposta impulsiva gi(t) do filtro ideal, cujo gráfico está desenhado na Figura 11.16.


   [img:Illustration] 


  Figura 11.16 Resposta impulsiva de um filtro ideal.


  O filtro ideal é um sistema não causal, ou seja, a entrada impulsiva aplicada em t = 0 fornece uma resposta que começa em t < 0. Por esta razão o filtro ideal não pode ser implementado na prática. A não causalidade pode ser amenizada adicionando-se um atraso ao filtro, porém esta prática deve ser evitada em sistemas de controle, pois o atraso usualmente reduz a estabilidade relativa do sistema.


  Para resolver esse problema utiliza-se no lugar do filtro ideal o segurador de ordem zero. Fazendo s = jω na função de transferência do segurador de ordem zero da Equação (11.19), obtém-se


   [img:Illustration] 


  A expressão (11.22) também pode ser escrita como


   [img:Illustration] 


  Da expressão (11.23) tem-se que o módulo e a fase de Gso(jω) são dados, respectivamente, por


   [img:Illustration] 


  Analisando-se a Equação (11.24) verifica-se que o módulo de Gso(jω) é nulo nas frequências múltiplas da frequência de amostragem ωA = 2π/T. Na Figura 11.17 são apresentados os gráficos do módulo em função da frequência do filtro ideal e do segurador de ordem zero.


   [img:Illustration] 


  Figura 11.17 Comparação entre os módulos Gi(jω)| do filtro ideal e |Gso(jω)| do segurador de ordem zero .


  Conforme se pode perceber na Figura 11.17 o segurador de ordem zero não remove as componentes de frequência maiores que ωA/2, introduzindo assim algum aliasing. Quanto maior for a frequência de amostragem ωA menor será a superposição de harmônicas que geram o aliasing. Na maioria dos casos práticos a resposta do segurador de ordem zero é considerada satisfatória quando a frequência de amostragem é adotada como sendo pelo menos 10 vezes maior que a componente de maior frequência presente no sinal contínuo (ωA ≥ 10ωN).


  

### 11.7 Mapeamento do plano s no plano z


  Considere o processo de amostragem de um conversor A/D ideal, conforme representado na Figura 11.7. O sinal contínuo f(t) é modulado por um trem de impulsos s(t), produzindo o sinal amostrado f*(t), que depois é convertido para a sequência discreta f(kT). Da Figura 11.7 tem-se que


   [img:Illustration] 


  sendo δ(t − kT) a função delta de Dirac.


  O sinal amostrado f*(t) é definido para todo t ≥ 0, sendo igual a zero para kT < t < (k + 1)T e diferente de zero nos instantes de amostragem t = kT. Já o sinal discreto f(kT) assume valor apenas em t = kT, pois não é definido em t ≠ kT.


  A transformada de Laplace de f*(t) é dada por


   [img:Illustration] 


  Definindo z = eTs, a Equação (11.27) resulta na definição de transformada Z, ou seja,


   [img:Illustration] 


  Da Equação (11.28) conclui-se que a mudança de variável z = eTs representa um procedimento alternativo para a definição da transformada Z. Além disso, essa mudança estabelece relações geométricas interessantes entre o plano s e o plano z.


  Supondo s = σ + jω, com σ e ω reais, então


   [img:Illustration] 


  Logo,


   [img:Illustration] 


  Das Equações (11.30) e (11.31) conclui-se que:


  
    • o eixo imaginário jω do plano s (σ = 0) corresponde à circunferência de raio unitário do plano z (|z| = 1);


    • o semiplano esquerdo do plano s (σ < 0) corresponde ao círculo de raio unitário com centro na origem do plano z (|z| < 1).

  


  Na Figura 11.18 é apresentado o mapeamento do plano s no plano z.


   [img:Illustration] 


  Figura 11.18 Mapeamento do plano s no plano z.


  À medida que um ponto do eixo jω do plano s (σ = 0) se move de −π/T a +π/T, a fase ∠z varia de −π a +π no sentido anti-horário. Quando o ponto se move de π/T a 3π/T a circunferência de raio unitário é percorrida mais uma vez. Para ω variando de −∞ a +∞, a circunferência de raio unitário é percorrida um número infinito de vezes.


  Portanto, um só ponto do plano z é mapeado no plano s em uma infinidade de pontos do tipo


   [img:Illustration] 


  

### 11.8 Subsistema D/A + processo + A/D


  No projeto de sistemas de controle digital é conveniente representar o subsistema D/A + processo + A/D por meio da transformada Z. Note que não é possível descrever separadamente, por meio da transformada Z, blocos como o conversor D/A, o processo e o conversor A/D, já que os sinais envolvidos no processo são analógicos e, no caso dos conversores, os sinais são analógicos e digitais. No entanto, o conjunto desses três blocos tem entrada e saída discretas (Figura 11.19) e pode, portanto, ser tratado como um único sistema discreto pela transformada Z (Figura 11.20). Deve-se observar que para valer a representação da Figura 11.20 é necessário considerar que o processo e as operações de conversão são lineares.


   [img:Illustration] 


  Figura 11.19 Subsistema D/A + processo + A/D.


   [img:Illustration] 


  Figura 11.20 Representação simplificada.


  A ideia é calcular a função de transferência H(z) do subsistema por meio da sua resposta impulsiva. Sendo u(kT) um impulso unitário, a saída u(t) do conversor D/A de ordem zero é um pulso, conforme representado na Figura 11.21.


   [img:Illustration] 


  Figura 11.21 Impulso u(kT) e saída pulso u(t).


  Conforme visto na Equação (11.18), a transformada de Laplace de u(t) é dada por


   [img:Illustration] 


  A saída do processo é, portanto,


   [img:Illustration] 


  A transformada Z de y(kT) é


   [img:Illustration] 


  Lembrando que Z[e−sT] = z−1 e que a transformada Z é uma operação linear, obtém-se


   [img:Illustration] 


  Como u(kT) é um impulso unitário (U(z) = 1), então


   [img:Illustration] 


  
    Concluindo, para determinar a função de transferência H(z) do subsistema D/A + processo + A/D basta calcular:


     


    • Z[G(s)/s], onde G(s) é a função de transferência do processo dinâmico;


    • H(z) = (1 − z−1)Z[G(s)/s].

  


  

### Exemplo 11.2


  Considere o subsistema da Figura 11.22.


   [img:Illustration] 


  Figura 11.22 Subsistema D/A + processo + A/D.


   [img:Illustration] 


  ■


  

### 11.9 Análise da malha fechada


  O diagrama de blocos de um sistema em malha fechada com realimentação unitária e controle discreto é apresentado na Figura 11.23.


   [img:Illustration] 


  Figura 11.23 Diagrama de blocos de um sistema em malha fechada com controle discreto.


  Conforme foi visto na seção anterior o subsistema D/A + processo + A/D pode ser representado pela função de transferência discreta H(z) dada pela Equação (11.35). Assim, o diagrama de blocos simplificado do sistema discreto em malha fechada pode ser representado através da Figura 11.24.


   [img:Illustration] 


  Figura 11.24 Diagrama de blocos simplificado do sistema discreto em malha fechada.


  Sendo R(z) = Z[r(kT)] e Y(z) = Z[y(kT)], a função de transferência de malha fechada é dada por


   [img:Illustration] 


  A função de transferência Gc(z) do controlador pode ser genericamente representada por


   [img:Illustration] 


  sendo b0, b1, . . . , bp e a0, . . . , aq−1 constantes, com p ≤ q.


  Dado o sinal de referência r(kT), os cálculos dos sinais de erro e(kT) e da ação de controle u(kT) podem ser implementados num algoritmo de "computador" por meio das seguintes equações de diferenças:


   [img:Illustration] 


   [img:Illustration] 


  

### 11.10 Estabilidade de sistemas de tempo discreto


  Nesta seção é considerado o conceito de estabilidade de entrada e saída, ou estabilidade externa, dos sistemas dinâmicos de tempo discreto.


  Definição 11.1 Um sistema possui a propriedade de estabilidade externa se toda sequência de entrada de amplitude limitada produz uma sequência de saída de amplitude limitada.


  Este tipo de estabilidade é referido como estabilidade BIBO.3 No caso de sistemas lineares e invariantes no tempo a estabilidade BIBO pode ser caracterizada pela resposta impulsiva do sistema, conforme o seguinte lema.


  Lema 11.1 Um sistema linear, discreto e invariante no tempo, com resposta impulsiva g(k) é BIBO estável se e somente se


   [img:Illustration] 


  Prova da suficiência


  Seja u(k) uma sequência de entrada de amplitude limitada ao número M e seja y(j) a saída correspondente. Expressando y(j) pela convolução e considerando módulos, tem-se que


   [img:Illustration] 


  De (11.41), segue-se a tese.


  Prova da necessidade


  Suponha que a condição (11.41) não é válida, isto é,


   [img:Illustration] 


  e considere uma entrada limitada definida por


   [img:Illustration] 


  Sendo y(j) a saída correspondente, então


   [img:Illustration] 


  Logo, da Equação (11.43)


   [img:Illustration] 


  o que conclui a prova.


  

### Exemplo 11.3


  O sistema


   [img:Illustration] 


  tem como resposta impulsiva o degrau unitário que é mostrado na Figura 11.25.


   [img:Illustration] 


  Figura 11.25 Sequência degrau unitário.


  A transformada inversa de G(z) é dada por


   [img:Illustration] 


  Logo,


   [img:Illustration] 


  Do Lema (11.1) conclui-se que o sistema G(z) é instável. De fato, considerando que G(z) representa um integrador, aplicando uma entrada de amplitude limitada, por exemplo do tipo degrau, a saída será uma rampa, que não é limitada.


  ■


  Outro teste para a estabilidade BIBO, normalmente mais útil nas aplicações, é expresso em termos da função de transferência em estudo, apresentado no teorema a seguir.


  
    Teorema 11.2 Um sistema linear, discreto e invariante no tempo, com função de transferência G(z), é BIBO estável se e somente se todos os polos de G(z) têm módulo menor que 1, ou seja, estão localizados estritamente dentro do círculo de raio unitário.

  


  Prova da suficiência


  Sendo os polos de G(z) interiores ao círculo de raio unitário e em número finito, basta expandir G(z) em frações parciais e verificar que a contribuição de cada parcela para a resposta impulsiva de G(z) é de amplitude limitada.


  Prova da necessidade


  Suponha que nem todos os polos de G(z) estão localizados estritamente dentro do círculo de raio unitário, isto é, um número finito de polos tem módulo maior ou igual a 1. É preciso mostrar que o sistema não é BIBO estável. Por simplicidade, suponha que G(z) possui dois polos reais, simples e diferentes (z = a e z = b), então a função G(z) pode ser expandida em frações parciais do seguinte modo


   [img:Illustration]  termos correspondentes aos polos no interior do círculo unitário.


  Como a contribuição dos polos do interior do círculo unitário para a resposta impulsiva de G(z) é de amplitude limitada, pelo lema basta mostrar que


   [img:Illustration] 


  De fato,


   [img:Illustration] 


  Supondo sem perda de generalidade que |a| > |b|, ou seja,


   [img:Illustration] 


  Então,


   [img:Illustration] 


  ou seja, a série diverge pois o polo em z = a está localizado, por hipótese, fora do círculo unitário.


  

### Exemplo 11.4


  O sistema


   [img:Illustration] 


  é instável, pois possui um polo em z = 1 que não está localizado estritamente dentro do círculo de raio unitário.


  ■


  

### Exemplo 11.5


  Dado o sistema


   [img:Illustration] 


  Os polos de G(z) são as raízes do polinômio do denominador


   [img:Illustration] 


  Logo,


   [img:Illustration] 


  Conforme mostrado na Figura 11.26, os polos de G(z) estão localizados fora do círculo unitário,4 poins  [img:Illustration]  Portanto, o sistema G(z) é instável.


   [img:Illustration] 


  Figura 11.26 Posição dos polos de G(z).


  ■


  

#### 11.10.1 Critério de Routh


  O critério de Routh, visto anteriormente para analisar a estabilidade de sistemas contínuos no plano s, também pode ser utilizado para analisar a estabilidade de sistemas discretos no plano z. Para isso basta realizar uma transformação bilinear, que consiste em substituir a variável complexa z por uma expressão na variável v, dada por


   [img:Illustration] 


  Escrevendo v na forma cartesiana σ + jω, tem-se que


   [img:Illustration] 


  Portanto, por meio da transformação bilinear (11.58) consegue-se mapear o interior do círculo unitário (|z| < 1) no semiplano esquerdo aberto (σ < 0) da variável complexa v, conforme é mostrado na Figura 11.27.


   [img:Illustration] 


  Figura 11.27 Mapeamento do plano z no plano v.


  Assim, para determinar a estabilidade de sistemas discretos basta aplicar a transformação bilinear (11.58) no denominador da função de transferência na variável complexa z e depois aplicar o critério de Routh na variável complexa v.


  

#### 11.10.2 Critério de Jury


  Considere o sistema da Figura 11.28.


   [img:Illustration] 


  Figura 11.28 Função de transferência G(z) de um sistema discreto.


  Suponha que a função de transferência G(z) seja dada por


   [img:Illustration] 


  O critério de estabilidade de Jury é aplicado para sistemas discretos, e permite determinar se um sistema G(z) é estável ou não sem precisar calcular as raízes do polinômio do denominador D(z) da função de transferência G(z).


  Suponha que o polinômio D(z) seja dado por


   [img:Illustration] 


  A seguir deve-se construir a tabela de estabilidade de Jury de acordo com a Tabela 11.1.


  Tabela 11.1 Tabela de estabilidade de Jury


   [img:Illustration] 


  De acordo com a Tabela 11.1 a primeira linha é composta pelos coeficientes do polinômio D(z), alinhados em potências ascendentes de z. Os elementos da segunda linha são alinhados de maneira inversa à da primeira. Os elementos de qualquer linha par são alinhados de maneira inversa à de qualquer linha ímpar imediatamente anterior. A última linha da tabela é composta por apenas três elementos (q2, q1 e q0). Os elementos da linha 3 até a linha 2n − 3 são calculados através dos seguintes determinantes:


   [img:Illustration] 


  
    Critério de Jury: um sistema com equação característica D(z) = 0 é estável se todas as condições a seguir são satisfeitas.


     


     [img:Illustration] 

  


  

### 11.11 Exercícios resolvidos


  

### Exercício 11.1


  Considere o sistema da Figura 11.29.


   [img:Illustration] 


  Figura 11.29 Diagrama de blocos do sistema em malha fechada.


  Supondo um período de amostragem T = 0,1 s, determine:


  a) a equação de diferenças do controlador;


  b) a função de transferência de malha fechada Y(z)/R(z);


  c) a resposta y(0), y(0, 1), y(0, 2), . . . , y(1, 0) quando a entrada r(kT) for um degrau unitário;


  d) o erro de regime estacionário quando r(kT) for um degrau unitário.


  Solução


  a) A função de transferência do controlador é dada por:


   [img:Illustration] 


  Aplicando a propriedade do atraso Z{u[(k − 1)T]} = z − 1U(z), obtém-se a equação de diferenças do controlador:


  u(kT) = u[(k − 1)T] + e(kT).


  b) Conforme calculado no Exemplo (11.2), a função de transferência H(z) é dada por


   [img:Illustration] 


  A função de transferência do sistema em malha fechada é dada por


   [img:Illustration] 


  Como T = 0,1 s, então


   [img:Illustration] 


  c) Aplicando a transformada Z inversa e a propriedade do atraso, obtém-se a seguinte equação de diferenças:


   [img:Illustration] 


  Sabendo-se que y(−0,1) = y(−0,2) = 0 e que r(kT) é um degrau unitário, ou seja,


   [img:Illustration] 


  a sequência y(kT) pode ser obtida por meio de uma implementação da Equação (11.64) num programa de computador.


  A seguir é apresentado o trecho de um programa, escrito na linguagem C, que calcula os valores da sequência y(kT) para k = 0, 1, 2, . . . , 10.


  Tabela 11.2 Programa e coeficientes para k = 0, 1, 2, . . . , 10


   [img:Illustration] 


  d) O valor da resposta no estado estacionário pode ser obtido por meio do teorema do valor final, ou seja,


   [img:Illustration] 


  Como r(kT) é um degrau unitário, então R(z) = z/(z − 1). Logo,


   [img:Illustration] 


  Com isso, o erro de regime no estado estácionário é nulo, isto é,


   [img:Illustration] 


  Este resultado está de acordo com o esperado, pois o controlador Gc(z) é um integrador.


  

### Exercício 11.2


  Usando a transformação bilinear e o critério de Routh, determine se o sistema


   [img:Illustration] 


  é estável ou instável.


  Solução


  A equação característica da função de transferência (11.69) é


   [img:Illustration] 


  Aplicando a transformação bilinear (11.58),


   [img:Illustration] 


  Multiplicando a Equação (11.71) por (v − 1)3,


   [img:Illustration] 


  Expandindo a Equação (11.72), obtém-se


   [img:Illustration] 


  Como todos os coeficientes do polinômio (11.73) estão presentes e têm o mesmo sinal, é necessário montar a seguinte tabela de Routh:


   [img:Illustration] 


  Como b1 < 0, há duas mudanças de sinal na 1 a coluna de coeficientes da tabela de Routh. Logo, o polinômio na variável v possui duas raízes no semiplano direito. Com isso o polinômio (11.70) na variável z possui duas raízes fora do círculo unitário. Portanto, o sistema (11.69) é instável.


  De fato, os polos de G(z) são


  z1 = −0,8 + 0,8j, z2 = −0,8 − 0,8j e z3 = −0,5


   [img:Illustration] 


  

### Exercício 11.3


  Usando o critério de Jury, determine se o sistema (11.69) é estável ou instável.


  Solução


  O polinômio D(z) é dado por


   [img:Illustration] 


  Os coeficientes de D(z) são


  a0 = 1, a1 = 2,1, a2 = 2,08 e a3 = 0,64 .


  A primeira condição é satisfeita, pois


   [img:Illustration] 


  A segunda condição também é satisfeita, pois


   [img:Illustration] 


  Sendo ímpar o grau de D(z), pois n = 3, então da terceira condição tem-se que


   [img:Illustration] 


  ou seja, a terceira condição é verdadeira.


  Na Tabela 11.3 é construída a tabela de estabilidade de Jury.


  Tabela 11.3 Tabela de estabilidade de Jury


   [img:Illustration] 


  Da Tabela 11.3 verifica-se que a quarta condição é falsa, pois


   [img:Illustration] 


  Como nem todas as condições do critério de Jury são satisfeitas, então o sistema (11.69) é instável.


  

### Exercício 11.4


  Determine a faixa de valores do ganho K para que o sistema em malha fechada da Figura 11.30 seja estável. Suponha um período de amostragem T = 1s.


   [img:Illustration] 


  Figura 11.30 Diagrama de blocos de um sistema em malha fechada.


  Solução


  A função de transferência H(z) do subsistema D/A + processo + A/D é


   [img:Illustration] 


  A função de transferência de malha fechada é


   [img:Illustration] 


  A equação característica deste sistema é dada por


   [img:Illustration] 


  Os coeficientes de D(z) são


  a0 = 1, a1 = 0,2838K − 1,1353 e a2 = 0,1353 + 0,1485K .


  Da primeira condição do critério de Jury tem-se que


   [img:Illustration] 


  Da segunda condição do critério de Jury tem-se que


   [img:Illustration] 


  Sendo par, o grau de D(z), pois n = 2, então, da terceira condição do critério de Jury tem-se que


   [img:Illustration] 


  Fazendo a intersecção das condições (11.82), (11.83) e (11.84), conclui-se que o sistema em malha fechada é estável para


   [img:Illustration] 


  

### Exercício 11.5


  Determine se um sistema com a equação característica


   [img:Illustration] 


  é estável ou instável.


  Solução


  Os coeficientes de D(z) são


  a0 = 1, a1 = 1,8, a2 = 0,47, a3 = −0,45 e a4 = −0,18 .


  A primeira condição é satisfeita, pois


   [img:Illustration] 


  A segunda condição também é satisfeita, pois


   [img:Illustration] 


  Sendo par, o grau de D(z), pois n = 4, então da terceira condição tem-se que


   [img:Illustration] 


  ou seja, a terceira condição é falsa.


  Como nem todas as condições do critério de Jury são satisfeitas, então o sistema é instável. De fato, o polinômio D(z) pode ser fatorado como


   [img:Illustration] 


  ou seja, D(z) possui uma raiz fora do círculo unitário em z = −1,2 .


  

### 11.12 Exercícios propostos


  

### Exercício 11.6


  Supondo um período de amostragem T, determine o subsistema H(z) = Y(z)/U(z) da Figura 11.31.


   [img:Illustration] 


  Figura 11.31 Subsistema D/A + processo + A/D.


  

### Exercício 11.7


  Considere o sistema da Figura 11.32.


   [img:Illustration] 


  Figura 11.32 Diagrama de blocos do sistema em malha fechada.


  Supondo um controlador proporcional K = 1 e um período de amostragem T = 1s, calcule:


  a) a função de transferência de malha fechada Y(z)/R(z);


  b) a resposta y(0), y(1), y(2), . . . , y(10), quando a entrada r(kT) for um degrau unitário;


  c) o erro de regime no estado estacionário quando r(kT) for um degrau unitário.


  

### Exercício 11.8


  Considere o sistema da Figura 11.33.


   [img:Illustration] 


  Figura 11.33 Diagrama de blocos do sistema em malha fechada.


  Supondo um período de amostragem T = 1s e sendo a função de transferência do controlador dada por


   [img:Illustration] 


  a) a equação de diferenças do controlador;


  b) a função de transferência de malha fechada Y(z)/R(z);


  c) a resposta y(0), y(1), y(2), . . . , y(10) quando a entrada r(kT) for um degrau unitário;


  d) o erro de regime no estado estacionário quando r(kT) for um degrau unitário.


  

### Exercício 11.9


  Determine se as seguintes equações características têm todas as suas raízes no interior do círculo unitário.


  a) z2 + 1,5z + 1,125 = 0 .


  b) z2 − 2z +1 = 0 .


  c) z3 − 0,2z2 − 0,3z + 0,4 = 0 .


  d) z3 − 1,3z2 − 0,08z + 0,24 = 0 .


  e) z4 + 0,4z3 − 0,57z2 − 0,1z + 0,08 = 0 .


  

### Exercício 11.10


  Usando o critério de Jury ou Routh, determine se o sistema com função de transferência


   [img:Illustration] 


  é estável ou instável.


  

### Exercício 11.11


  O sistema da Figura 11.34 é representado pela seguinte equação de diferenças:


   [img:Illustration] 


  Determine para quais valores de α o sistema G(z) é estável.


   [img:Illustration] 


  Figura 11.34 Sistema G(z).


  

### Exercício 11.12


  Determine a faixa de valores do ganho K para que o sistema em malha fechada da Figura 11.35 seja estável. Suponha um período de amostragem T = 1s.


   [img:Illustration] 


  Figura 11.35 Diagrama de blocos do sistema em malha fechada.


  

### Exercício 11.13


  Um sistema discreto com entrada u e saída y é representado pela equação de diferenças


  y(k) = 0,5y(k − 1) + u(k) − 0,1u(k − 1) .


  a) Determine a função de transferência G(z) = Y(z)/U(z).


  b) Obtenha o valor do polo e do zero de G(z).


  c) Determine se o sistema G(z) é estável ou instável.


  

### Exercício 11.14


  Um sistema discreto é representado simplificadamente pelo diagrama de blocos da Figura 11.36.


   [img:Illustration] 


  Figura 11.36 Diagrama de blocos de um sistema discreto.


  a) Determine se o sistema em malha aberta é estável ou instável.


  b) Determine se o sistema em malha fechada é estável ou instável.


  

### Exercício 11.15


  Considere o sistema de controle da Figura 11.37. O ganho K do controlador e o parâmetro p do processo são números reais maiores que zero. T é o período de amostragem.


   [img:Illustration] 


  Figura 11.37 Diagrama de blocos de um sistema em malha fechada.


  a) Determine a função de transferência discreta H(z) = Y(z)/U(z) do subsistema D/A + processo + A/D.


  b) Para quais valores de p e T o sistema discreto H(z) é estável?


  c) Obtenha a função de transferência discreta da malha fechada Y(z)/R(z).


  d) Supondo p = 1 e T = 0,1s, determine para quais valores de K o sistema em malha fechada é estável.


  e) Supondo p = 1 e T = 0,1s, determine, se existir, o valor estacionário y(∞) da saída quando é aplicado um degrau unitário na referência.


  

### Exercício 11.16


  Determine a faixa de valores do ganho K para que o sistema em malha fechada da Figura 11.38 seja estável. Suponha um período de amostragem T = 1s.


   [img:Illustration] 


  Figura 11.38 Diagrama de blocos do sistema em malha fechada.


  

### Exercício 11.17


  Determine a faixa de valores do ganho K para que o sistema em malha fechada da Figura 11.39 seja estável. Suponha um período de amostragem T = 0,5 s.


   [img:Illustration] 


  Figura 11.39 Diagrama de blocos do sistema em malha fechada.


  

### Exercício 11.18


  Considere o sistema da Figura 11.40.


   [img:Illustration] 


  Figura 11.40 Diagrama de blocos do sistema em malha fechada.


  a) Supondo Gc(z) = 1, determine se o sistema em malha fechada é estável para T = 0,1 s.


  b) Supondo Gc(z) = z/(z − 1), determine se o sistema em malha fechada é estável para T = 2s.


  c) Supondo Gc(z) = z/(z − 1) e T = 0,1s, determine os erros de regime para entrada r(t) rampa e degrau unitário.


  


  __________


  1 Esta denominação é usada para designar qualquer processador eletrônico capaz de realizar cálculos digitalmente.


  2 A frequência ωN é chamada de frequência de Nyquist.


  3 Abreviação do inglês Bounded Input Bounded Output, ou seja, "Entrada Limitada Saída Limitada".


  4 Círculo unitário é o círculo aberto de raio 1 e centro na origem do plano complexo z.



<!-- Text/chapter12.xhtml -->

  
  Controle Automático, 2ª edição
  
  

  

## 12

  

## Projeto de Controladores Digitais

  

### 12.1 Introdução

  A principal vantagem do controlador digital sobre o controlador contínuo é a flexibilidade de implementação. Como os controladores contínuos são implementados por meio de componentes eletrônicos, a complexidade desses controladores depende da complexidade e da precisão dos componentes. Já os controladores digitais são implementados na forma de programas, sendo portanto igualmente fácil implementar controladores simples ou complexos, além do que mudanças nas leis de controle também são muito mais simples de serem realizadas.

  Os controladores digitais são modeláveis, a menos de pequenas imprecisões nas amplitudes dos sinais, por meio de sistemas de tempo discreto e suas funções de transferência em z.

  Basicamente, o projeto de controladores de tempo discreto pode ser realizado de duas formas: i) por aproximações discretas do projeto realizado no domínio contínuo por meio da transformada de Laplace; ii) diretamente no domínio discreto por meio da transformada Z.

  A primeira forma implica obter funções de transferência em z, aproximadas a partir de funções de transferência em s. Neste caso serão apresentados os métodos: aproximação retangular para a frente e para trás, transformação bilinear ou de Tustin e mapeamento polo-zero. Na segunda forma funcionam bem o método do lugar das raízes e o método algébrico na variável z.

  Neste capítulo são ainda apresentados projetos de controladores no domínio da frequência, de controladores PID discretos e de controladores do tipo dead beat.

  

### 12.2 Aproximações de tempo discreto

  Deseja-se obter um sistema discreto que represente aproximadamente um sistema contínuo. Considere, por simplicidade, a função de transferência de um integrador:

   [img:Illustration] 

  A equação diferencial que representa a função de transferência (12.1) é

   [img:Illustration] 

  Integrando ambos os membros da Equação (12.2) num período de amostragem T qualquer, ou seja, de (k − 1)T a kT, obtém-se

   [img:Illustration] 

  Há vários métodos numéricos para integrar o segundo membro da Equação (12.3). Alguns deles são mostrados nas Figuras 12.1 (a), (b) e (c).

   [img:Illustration] 

  Figura 12.1 Métodos numéricos de integração. (a) Retangular para a frente. (b) Retangular para trás. (c) Trapézio.

  

#### 12.2.1 Retangular para a frente

  Neste método o cálculo da integral é aproximado pela área de um retângulo, cujo comprimento de um dos lados é igual ao período de amostragem T e o comprimento do outro é igual ao valor da função no instante (k − 1)T, conforme mostrado na Figura 12.1 (a). Fazendo esta aproximação na Equação (12.3), obtém-se

   [img:Illustration] 

  Aplicando a transformada Z na Equação (12.4), obtém-se

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  Portanto, a função de transferência do sistema discreto (12.6) se obtém da função de transferência do sistema contínuo (12.1) simplesmente fazendo a troca de variável1

   [img:Illustration] 

  Para um sistema qualquer ser estável, seus polos devem estar localizados no semiplano esquerdo aberto do plano s. Este semiplano se caracteriza por

   [img:Illustration] 

  Como T > 0, então

   [img:Illustration] 

  Portanto, a transformação (12.7) pode fazer com que polos localizados no semiplano esquerdo do plano s sejam mapeados fora do círculo unitário, fazendo com que o sistema discreto resultante seja instável (Figura 12.2).

   [img:Illustration] 

  Figura 12.2 Mapeamento do plano s no plano z com a aproximação retangular para a frente.

  

#### 12.2.2 Retangular para trás

  Neste método o cálculo da integral é aproximado pela área de um retângulo, cujo comprimento de um dos lados é igual ao período T e o comprimento do outro é igual ao valor da função no instante kT, conforme mostrado na Figura 12.1 (b). Fazendo esta aproximação na Equação (12.3), obtém-se

   [img:Illustration] 

  Aplicando a transformada Z na Equação (12.10), obtém-se

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  As Equações (12.1) e (12.12) são equivalentes se

   [img:Illustration] 

  Se um sistema qualquer é estável seus polos devem estar localizados no semiplano esquerdo aberto do plano s. Da Equação (12.13) tem-se que

   [img:Illustration] 

  Escrevendo z em coordenadas retangulares, isto é, z = σ + jω e como T > 0, então

   [img:Illustration] 

  ou

   [img:Illustration] 

  Portanto, a transformação (12.13) mapeia o semiplano esquerdo do plano s num círculo com centro em z = 0,5 e raio igual a 0,5. Conforme é mostrado na Figura 12.3, a integração retangular para trás não oferece perigo de instabilizar indevidamente um sistema estável.

   [img:Illustration] 

  Figura 12.3 Mapeamento do plano s no plano z com a aproximação retangular para trás.

  

#### 12.2.3 Transformação bilinear ou método de Tustin

  Neste método o cálculo da integral é aproximado pela área de um trapézio, cuja altura é igual ao período T e cujas bases correspondem aos valores da função nos instantes kT e (k − 1)T, conforme mostrado na Figura 12.1 (c). Fazendo esta aproximação na Equação (12.3), obtém-se

   [img:Illustration] 

  Aplicando a transformada Z na Equação (12.17), obtém-se

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  As Equações (12.1) e (12.19) são equivalentes se

   [img:Illustration] 

  Se um sistema qualquer é estável seus polos devem estar localizados no semiplano esquerdo aberto do plano s. Da Equação (12.20) tem-se que

   [img:Illustration] 

  Escrevendo z em coordenadas retangulares, isto é, z = σ + jω e como T > 0, então

   [img:Illustration] 

  ou

   [img:Illustration] 

  Portanto, a transformação (12.20) mapeia no plano z um círculo com centro na origem e raio igual a 1, conforme mostrado na Figura 12.4. Embora nesta transformação o semiplano esquerdo de s seja mapeado exatamente no círculo unitário do plano z, a mesma pode ocasionar uma distorção na resposta em frequência quando comparada ao sistema contínuo. Para compensar esta distorção (prewarping) pode-se usar a transformação bilinear da seção seguinte.

   [img:Illustration] 

  Figura 12.4 Mapeamento do plano s no plano z com a aproximação de Tustin.

  

#### 12.2.4 Transformação bilinear com compensação de prewarping

  Fazendo s = jωs e z = ejωT, a transformação (12.20) no domínio da frequência fica expressa por

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  ou seja, a frequência do sistema contínuo ωs é mapeada em  [img:Illustration]  no sistema discreto. Esta distorção em frequência é denominada prewarping.

  Note que em baixas frequências, ou para ωT pequeno, as frequências dos sistemas contínuo e discreto são próximas, pois

   [img:Illustration] 

  Como não é possível compensar essa distorção em todas as frequências costuma-se ajustar apenas a frequência crítica do sistema, como, por exemplo, no limite superior da faixa de passagem.

  Considere, por simplicidade, a função de transferência de primeira ordem

   [img:Illustration] 

  Se, por exemplo, a frequência crítica da função (12.27) for a frequência do polo (ωs = a), então a função de transferência é ajustada para

   [img:Illustration] 

  Note que o numerador da Equação (12.28) também foi ajustado para que o ganho em baixas frequências permaneça o mesmo. Aplicando-se a transformação bilinear (12.20) em (12.28), obtémse o sistema discreto com compensação de distorção em frequência

   [img:Illustration] 

  Pode-se mostrar que na frequência crítica adotada (ωs = ω = a) os módulos dos sistemas contínuo e discreto são iguais, ou seja,

   [img:Illustration] 

  e

   [img:Illustration] 

  

### Exemplo 12.1

  Dada a função de transferência do sistema contínuo

   [img:Illustration] 

  determine a função de transferência do sistema discreto usando a transformação bilinear com e sem compensação de distorção em frequência. No caso da transformação com compensação deseja-se que o sistema discreto tenha o mesmo módulo que o sistema contínuo na frequência ω = 2 rad/s. Suponha um período de amostragem T = 1s.

  No caso da transformação bilinear sem compensação basta substituir diretamente a aproximação (12.20) em G(s), obtendo

   [img:Illustration] 

  No caso da transformação bilinear com compensação, a função G(s) deve ser modificada para

   [img:Illustration] 

  Aplicando a transformação bilinear (12.20) na Equação (12.34), obtém-se

   [img:Illustration] 

  Na Figura 12.5 é apresentada a resposta em frequência do sistema contínuo (12.32) e dos sistemas discretos (12.33) e (12.35). Note que o sistema discreto com compensação possui o mesmo módulo que o sistema contínuo na frequência ω = 2 rad/s.

   [img:Illustration] 

  Figura 12.5 |G(jω)| do sistema contínuo (12.32) e |G(ejωT)| dos sistemas discretos (12.33) e (12.35).

  ■

  

#### 12.2.5 Mapeamento polo-zero

  O método consiste em mapear os polos e zeros da função de transferência G(s) no plano z, através da relação z = esT. Inicialmente deve-se fatorar G(s) na forma de polos e zeros, ou seja,

   [img:Illustration] 

  sendo n o número de polos, e m o número de zeros.

  Um polo de G(s) em s = pn é mapeado no plano z em z = epnT, e um zero finito de G(s) em s = zm é mapeado no plano z em z = ezmT .

  Quando o número de zeros de G(s) é menor que o número de polos (m < n), G(s) possui zeros no infinito, que são mapeados em z = −1. A explicação para este fato é que conforme um ponto do eixo jω varia de 0 a π/T no plano s o mesmo varia de (z = ej0 = 1) até (z = ejπ = −1) no plano z, ou seja, o ponto z = −1 representa a maior frequência possível da função de transferência discreta. Para compensar este efeito acrescentam-se (n − m − 1) fatores de (z + 1) no numerador da função transferência discreta G(z).

  Por último, deve-se ajustar o ganho de G(z). Este ajuste pode ser feito para qualquer frequência crítica de G(s). Normalmente o ganho é ajustado para que em baixas frequências o ganho do sistema contínuo seja igual ao do sistema discreto, ou seja,

   [img:Illustration] 

  

### Exemplo 12.2

  Dada a função de transferência do sistema contínuo

   [img:Illustration] 

  determine a função de transferência do sistema discreto usando o método do mapeamento polo-zero. Suponha um período de amostragem T = 1s.

  O polo em s = −2 é mapeado em z = e−2T. O sistema G(s) possui um polo (n = 1) e nenhum zero finito (m = 0). Como n − m − 1 = 0, então não é necessário acrescentar fatores de (z + 1) no numerador do sistema discreto.

  Logo, a função de transferência do sistema discreto é dada por

   [img:Illustration] 

  O ganho K é ajustado para que em baixas frequências o ganho do sistema contínuo G(s) seja igual ao do sistema discreto G(z), ou seja,

   [img:Illustration] 

  Portanto,

   [img:Illustration] 

  ■

  

### Exemplo 12.3

  Dada a função de transferência do sistema contínuo

   [img:Illustration] 

  determine a função de transferência do sistema discreto usando o método do mapeamento polo-zero. Suponha um período de amostragem T = 1s.

  O zero em s = −1 é mapeado em z = e−T. Os polos em s = −2, s = −3 e s = −4 são mapeados, respectivamente, em z = e−2T, z = e−3T e z = e−4T.

  O sistema G(s) possui três polos (n = 3) e um zero finito (m = 1). Como n − m − 1 = 1, então é necessário acrescentar um fator de (z + 1) no numerador do sistema discreto.

  Logo, a função de transferência do sistema discreto é dada por

   [img:Illustration] 

  O ganho K é ajustado para que em baixas frequências o ganho do sistema contínuo G(s) seja igual ao do sistema discreto G(z), ou seja,

   [img:Illustration] 

  Portanto,

   [img:Illustration] 

  ■

  

### 12.3 Projeto de controlador discreto a partir de projeto de controlador contínuo

  Suponha o sistema de tempo contínuo e o projeto do controlador realizado inteiramente no plano s de Laplace. A questão é obter um controlador discreto por meio de uma das aproximações analisadas anteriormente. Considere o sistema de controle contínuo da Figura 12.6.

   [img:Illustration] 

  Figura 12.6 Sistema de controle contínuo.

  Para trocar o controlador contínuo por um discreto é preciso adicionar os blocos de conversores A/D (analógico/digital) e D/A (digital/analógico), conforme representado na Figura 12.7.

   [img:Illustration] 

  Figura 12.7 Sistema de controle discreto.

  O processo de amostragem e o circuito segurador, representados pelos conversores A/D e D/A, introduzem na malha um atraso de tempo que reduz a estabilidade do sistema, fato que deve de antemão ser considerado no projeto do controlador contínuo. Caso contrário, quando o controlador discreto for implementado o sistema resultante poderá ser instável em malha fechada. Conforme visto anteriormente, a função de transferência do segurador de ordem zero é dada por

   [img:Illustration] 

  Em uma primeira aproximação, a exponencial e−sT pode ser representada na forma racional através da aproximação de Padé2 de ordem 1, ou seja,

   [img:Illustration] 

  Substituindo a Equação (12.47) na Equação (12.46), obtém-se

   [img:Illustration] 

  Note que os ganhos em baixas frequências das Equações (12.46) e (12.48) não são unitários. O interesse na Equação (12.48) é determinar uma função de transferência racional que represente apenas o atraso de fase ocasionado pelo segurador de ordem zero e que não afete o ganho da malha fechada, já que o mesmo será determinado no projeto do controlador.

  Corrigindo o ganho da Equação (12.48), de modo que em baixas frequências (s = jω = 0) o mesmo seja unitário, obtém-se uma função de transferência racional aproximada para o segurador de ordem zero, dada por

   [img:Illustration] 

  Assim, o controlador contínuo deve ser projetado com base no diagrama de blocos da Figura 12.8, isto é, prevendo a função de transferência do segurador de ordem zero aproximada.3

  Quanto menor for o período de amostragem T, menor a influência na estabilidade do sistema. Por esta razão este deve ser escolhido suficientemente "pequeno", como aliás indica o teorema da amostragem.

   [img:Illustration] 

  Figura 12.8 Sistema de controle contínuo com segurador.

  Finalmente, o controlador discreto é obtido por meio de uma aproximação do controlador contínuo Gc(s) por um dos métodos analisados anteriormente (Tustin, mapeamento polo-zero, etc.).

  Como se sabe, as especificações de projeto do controlador costumam ser realizadas em termos dos parâmetros da resposta temporal, como, por exemplo: sobressinal Mp, tempo de subida tr, tempo de pico tp ou tempo de acomodação ts. Estes parâmetros estão indicados na Figura 12.9, que representa a resposta temporal típica de um sistema de segunda ordem subamortecido (0 < ξ < 1).

   [img:Illustration] 

  Figura 12.9 Resposta temporal de um sistema de segunda ordem para 0 < ξ < 1.

  Conforme analisado anteriormente para sistemas subamortecidos (0 < ξ < 1), os parâmetros da resposta temporal da Figura 12.9 valem:

   [img:Illustration] 

  sendo ξ o coeficiente de amortecimento, ωn a frequência natural não amortecida e ωd a frequência natural amortecida.

  

### Exemplo 12.4

  Deseja-se projetar um controlador discreto para um processo com função de transferência

   [img:Illustration] 

  de modo que a resposta para um degrau aplicado na referência tenha um sobressinal máximo Mp = 16,3% e um tempo de pico tp = 1s.

  Solução

  O controlador discreto pode ser obtido por meio de uma aproximação do controlador contínuo. Considerando-se o efeito do segurador de ordem zero, o controlador contínuo deve ser projetado para o diagrama de blocos da Figura 12.10.

   [img:Illustration] 

  Figura 12.10 Diagrama de blocos do sistema contínuo com segurador.

  Supondo que o sistema em malha fechada tenha dinâmica dominada por um par de polos complexos,4 o coeficiente de amortecimento ξ é obtido a partir do sobressinal Mp, ou seja,

   [img:Illustration] 

  O tempo de pico tp é dado por

   [img:Illustration] 

  sendo ωd a frequência natural amortecida dada por  [img:Illustration] 

  Assim, a frequência natural não amortecida ωn vale

   [img:Illustration] 

  A resposta temporal da saída, para uma entrada do tipo degrau na referência, irá apresentar oscilações durante o transitório, com período Td, dado por

   [img:Illustration] 

  Na prática o período de amostragem T é escolhido como sendo pelo menos 10 vezes menor que o período das oscilações, ou seja,

   [img:Illustration] 

  Logo, a função de transferência aproximada do segurador de ordem zero é dada por

   [img:Illustration] 

  A função de transferência genérica de um sistema de segunda ordem é dada por

   [img:Illustration] 

  cujos polos de malha fechada são

   [img:Illustration] 

  Para que o sistema em malha fechada satisfaça às especificações de projeto (Mp = 16,3% e tp = 1s), os polos de malha fechada devem estar localizados em

   [img:Illustration] 

  

### Projeto por meio do lugar das raízes

  Nesta técnica de projeto calcula-se uma função de transferência para o controlador Gc(s), de modo que o lugar das raízes passe pelos polos de malha fechada desejados (12.65).

  As especificações de projeto podem ser satisfeitas através de um controlador de primeira ordem, com função de transferência

   [img:Illustration] 

  A função de transferência de malha aberta é dada por

   [img:Illustration] 

  Existem infinitos valores para K, C1 e C2 que satisfazem às especificações de projeto. Uma solução é cancelar5 o zero do controlador com o polo estável da planta. Com isso os valores de C2 e K podem ser calculados por meio das condições de fase e módulo, respectivamente.

  Assim, adotando C1 = 1, obtém-se

   [img:Illustration] 

  Da condição de fase tem-se que

   [img:Illustration] 

  ou seja,

   [img:Illustration] 

  O valor de C2 deve ser calculado num dos polos complexos de malha fechada s1,2 ≅ −1,81 ± πj. Da expressão (12.70) obtém-se

   [img:Illustration] 

  Na Figura 12.11 é apresentado o gráfico do lugar das raízes.

   [img:Illustration] 

  Figura 12.11 Lugar das raízes.

  O valor de K pode ser calculado através da condição de módulo, ou seja,

   [img:Illustration] 

  Substituindo um dos polos complexos de malha fechada s1,2 ≅ −1,81±πj em (12.72), obtém-se

   [img:Illustration] 

  Portanto, a função de transferência do controlador contínuo é dada por

   [img:Illustration] 

  Com isso, a função de transferência de malha fechada é dada por

   [img:Illustration] 

  Os polos de malha fechada da Equação (12.75) são s1,2 ≅ −1,81 ± 3,14j, s3 = −12,06. Como os polos complexos estão bem mais próximos do eixo imaginário que o polo real estes são chamados de polos dominantes, ou seja, são os polos complexos que irão determinar a característica da resposta transitória. Por esta razão o sistema de terceira ordem terá comportamento próximo daquele do sistema de segunda ordem.

  

### Projeto por meio de imposição algébrica de polos

  Nesta técnica de projeto a função de transferência do controlador Gc(s) é calculada por meio de uma imposição algébrica de polos.

  A função de transferência do processo mais o segurador tem grau n = 3. O controlador Gc(s) deve ter grau m ≥ n − 1. Assim, assumindo m = 2 a função de transferência do controlador é do tipo

   [img:Illustration] 

  A função de transferência de malha aberta é dada por

   [img:Illustration] 

  Supondo que os zeros do controlador cancelam os polos estáveis (C1 = 1 e C2 = 10), então

   [img:Illustration] 

  A função de transferência de malha fechada é dada por

   [img:Illustration] 

  cujo polinômio característico é

   [img:Illustration] 

  Os polos de malha fechada dominantes são s1,2 ≅ −1,81 ± πj. Para que o polinômio característico tenha grau 3 adota-se o terceiro polo6 em s3 = −12,06, que é a mesma posição obtida pelo método do lugar das raízes. Então,

   [img:Illustration] 

  Comparando os polinômios (12.80) e (12.81), obtém-se K = 15,88, D1 = 5,69 e D2 = 10. Portanto, a função de transferência do controlador é dada por

   [img:Illustration] 

  Os compensadores (12.74) e (12.82) resultaram iguais, pois no projeto algébrico foi adotado como polinômio característico o mesmo denominador da função de transferência de malha fechada (12.75) obtida pelo método do lugar das raízes.

  

### Função de transferência do controlador discreto

  A função de transferência do controlador discreto pode ser obtida por meio do método do mapeamento polo-zero. O zero em s = −1 é mapeado em z = e−T, e o polo em s = −5,69 é mapeado em z = e−5,69T. Como Gc(s) possui um polo (n = 1) e um zero finito (m = 1), então não é necessário acrescentar fatores de (z + 1) no numerador do controlador discreto, ou seja,

   [img:Illustration] 

  O ganho Kz é ajustado para que em baixas frequências o ganho do controlador contínuo Gc(s) seja igual ao do controlador discreto Gc(z), ou seja,

   [img:Illustration] 

  Portanto,

   [img:Illustration] 

  Aplicando a propriedade do atraso, obtém-se a seguinte equação de diferenças:

   [img:Illustration] 

  Sabendo-se que u(−0,2) = e(−0,2) = 0 e que r(kT) é um degrau unitário, ou seja,

   [img:Illustration] 

  então a Equação (12.86) pode ser implementada num programa de computador. Na Figura 12.12 é apresentado o trecho de um programa, escrito na linguagem C, que exemplifica a realização do controlador para k = 0, 1, 2, . . . , 100.

   [img:Illustration] 

  Figura 12.12 Realização do controlador discreto na linguagem C.

  

### Resposta ao degrau

  Aplicando-se um degrau unitário na entrada R(s) da função de transferência de malha fechada (12.75), obtém-se a resposta ao degrau do sistema contínuo, dada por

   [img:Illustration] 

  Para verificar se o controlador discreto Gc(z) da Equação (12.85) satisfaz às especificações de projeto pode-se comparar a resposta (12.88) com a resposta ao degrau do sistema da Figura 12.13.

   [img:Illustration] 

  Figura 12.13 Diagrama de blocos do sistema em malha fechada com controlador discreto.

  Da Figura 12.13 tem-se que

   [img:Illustration] 

  A função de transferência de malha aberta é dada por

   [img:Illustration] 

  A função de transferência de malha fechada é dada por

   [img:Illustration] 

  Aplicando a propriedade do atraso, obtém-se a seguinte equação de diferenças:

   [img:Illustration] 

  Sabendo-se que y(−0,2) = y(−0,4) = 0 e que r(kT) é um degrau unitário, então os valores de y(kT) podem ser calculados por meio da implementação da Equação (12.92) num programa de computador. A seguir é apresentado o trecho de um programa, escrito na linguagem C, que calcula os valores da sequência y(kT) para k = 0, 1, 2, . . . , 15.

  Tabela 12.1 Programa e coeficientes para k = 0, 1, 2, . . . , 15

   [img:Illustration] 

  Na Figura 12.14 são apresentados os gráficos da resposta ao degrau unitário do sistema em malha fechada contínuo (12.88) e discreto (12.92). Note que as respostas estão próximas das especificações de projeto e que a curva y(t) possui um atraso devido à aproximação do segurador de ordem zero.

   [img:Illustration] 

  Figura 12.14 Resposta ao degrau unitário.

  ■

  

### 12.4 Erro estacionário ou permanente

  No projeto de sistemas de controle também é comum adotar como especificação de desempenho o erro estacionário ou erro em regime permanente.

  Considere o sistema discreto em malha fechada da Figura 12.15.

   [img:Illustration] 

  Figura 12.15 Sistema discreto em malha fechada.

  Da Figura 12.15 tem-se que

   [img:Illustration] 

  

#### 12.4.1 Degrau na referência

  Se o sistema for estável, isto é, se os polos de 1 + G(z)H(z) estiverem localizados dentro do círculo de raio unitário (|z| < 1), então o erro estacionário e(∞) pode ser calculado por meio do teorema do valor final, ou seja,

   [img:Illustration] 

  Supondo que um degrau de amplitude A é aplicado na referência (R(z) = A/(1 − z−1)), então

   [img:Illustration] 

  Genericamente, a função de transferência de malha aberta G(z)H(z) pode ser escrita como

   [img:Illustration] 

  sendo que N(z)/D(z) não contém polos ou zeros em z = 1 e L indica a quantidade de integradores ou polos em z = 1 de G(z)H(z).

  Usualmente um sistema é chamado de tipo (0, 1, 2, . . .) de acordo com a sua quantidade (L = 0, 1, 2, . . .) de polos em z = 1.

  Substituindo (12.96) em (12.95), tem-se que

   [img:Illustration] 

  Definindo

   [img:Illustration] 

  obtém-se

   [img:Illustration] 

  

#### 12.4.2 Rampa na referência

  Supondo que uma rampa é aplicada na referência, isto é, R(z) = ATz−1/(1 − z−1)2, pelo teorema do valor final tem-se que

   [img:Illustration] 

  Substituindo (12.96) em (12.100), tem-se que

   [img:Illustration] 

  Definindo

   [img:Illustration] 

  obtém-se

   [img:Illustration] 

  Note que para L = 1 o período de amostragem T afeta diretamente o valor do erro estacionário. Na Tabela 12.2 estão resumidos os erros estacionários para sistemas tipo 0, 1 e 2 (L = 0, 1 e 2) para entrada degrau e rampa na referência.

  Tabela 12.2 Erros estacionários para sistemas tipo 0, 1 e 2

   [img:Illustration] 

  

### 12.5 Polos no plano s e no plano z

  Considere um sistema de segunda ordem padrão com função de transferência

   [img:Illustration] 

  Supondo um coeficiente de amortecimento 0 < ξ < 1, os polos s1,2 da Equação (12.104) são complexos conjugados e dados por

   [img:Illustration] 

  Sendo T o período de amostragem, os polos no plano s podem ser mapeados no plano z por meio da relação z = eTs, ou seja,

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  e

   [img:Illustration] 

  No plano s o coeficiente de amortecimento ξ = cos β está localizado em uma linha radial, enquanto no plano z esta linha é representada por uma espiral, conforme é mostrado na Figura 12.16. Note que os polos no plano z dependem do período de amostragem T.

   [img:Illustration] 

  Figura 12.16 Gráficos com coeficiente de amortecimento ξ constante no plano s e no plano z.

  Na Figura 12.17 são apresentadas diversas curvas no plano z para 0 ≤ ωn ≤ π/T, mostrando os lugares em que o coeficiente de amortecimento ξ e a frequência ωn são constantes. Para ξ = 0 o gráfico é a circunferência de raio unitário, e para ξ = 1 o gráfico é uma linha horizontal ligando os pontos z = 0 a z = 1.

   [img:Illustration] 

  Figura 12.17 Curvas com coeficiente de amortecimento ξ e frequência ωn constantes no plano z para 0 ≤ ωn ≤ π/T.

  

### 12.6 Influência do período de amostragem em transitórios

  A resposta transitória de um sistema de tempo discreto depende do período de amostragem T, pois este afeta a posição dos polos no plano z. Para que um sistema seja estável os polos devem estar localizados estritamente dentro do círculo de raio unitário, ou seja, o período T deve ser tal que

   [img:Illustration] 

  Na prática o período de amostragem T é escolhido como pelo menos 10 vezes menor que o período das oscilações da saída, se a resposta transitória for subamortecida, ou 10 vezes menor que o tempo de subida, se a resposta for amortecida.

  

### Exemplo 12.5

  Considere o sistema da Figura 12.18.

   [img:Illustration] 

  Figura 12.18 Diagrama de blocos de um sistema em malha fechada.

  A função de transferência Gp(z) do subsistema D/A + processo + A/D é

   [img:Illustration] 

  Supondo que o processo tenha um polo em s = −a = −1, tem-se que

   [img:Illustration] 

  A função de transferência de malha fechada é

   [img:Illustration] 

  A equação característica é dada por

   [img:Illustration] 

  Pelo critério de Jury os coeficientes de D(z) são

  a0 = 1, a1 = T − 2 e a2 = 1 − Te−T.

  Da primeira condição do critério de Jury tem-se que

   [img:Illustration] 

  Da segunda condição do critério de Jury tem-se que

   [img:Illustration] 

  Como T > 0, a condição (12.115) é sempre satisfeita.

  Sendo par o grau de D(z), pois n = 2, então, da terceira condição do critério de Jury tem-se que

   [img:Illustration] 

  Na Figura 12.19 são apresentados os gráficos das funções Te−T e 4 − T em função de T. Conforme se pode perceber por meio desta figura, a condição (12.114) é sempre satisfeita. Já a condição (12.116) é satisfeita apenas para T ≤ 3,9223 aproximadamente.

   [img:Illustration] 

  Figura 12.19 Intersecção das funções Te−T e 4 − T .

  Para T = 0,5 s os polos de malha fechada são z1,2 = 0,7500 ± 0,3664j. Logo,

   [img:Illustration] 

  e

   [img:Illustration] 

  Assim,

   [img:Illustration] 

  Portanto, o sobressinal vale

   [img:Illustration] 

  Para T = 2s os polos de malha fechada são z1,2 = ±0,8540j. Logo,

   [img:Illustration] 

  e

   [img:Illustration] 

  Assim,

   [img:Illustration] 

  Portanto, o sobressinal vale

   [img:Illustration] 

  

### Resposta ao degrau

  A Equação (12.110) também pode ser escrita com potências negativas em z, ou seja,

   [img:Illustration] 

  Aplicando a transformada Z inversa e a propriedade do atraso, obtém-se a seguinte equação de diferenças:

   [img:Illustration] 

  Na Figura 12.20 são apresentados os gráficos da resposta ao degrau unitário y(kT) para T = 0,5 s e T = 2s. Note que para T = 0,5 s a resposta é mais amortecida e com sobressinal menor (Mp ≅ 28,6%) que a resposta para T = 2s (Mp ≅ 72,9%).

   [img:Illustration] 

  Figura 12.20 Resposta ao degrau unitário.

  

### 12.7 Projeto de controlador no plano z

  A principal dificuldade dos projetos em z é a escolha dos polos de malha fechada, ou da região em que eles devem estar, para que resultem transientes aceitáveis com razoável robustez frente às variações da planta. Como as especificações de projeto são usualmente baseadas em índices de desempenho de respostas transitórias que possuem uma correspondência com os polos do plano s, os polos do plano z podem ser obtidos por meio de um mapeamento dos polos em s.

  Dado um desejado amortecimento para um par de polos, no plano s os polos estão sobre retas bem conhecidas, enquanto no plano z estão sobre curvas que se amontoam no ponto z = 1, conforme é mostrado nas Figuras 12.16 e 12.17. Portanto, a sensibilidade do sobressinal com relação à variação de parâmetros é muito grande.

  

### Exemplo 12.6

  Considere o sistema da Figura 12.21.

   [img:Illustration] 

  Figura 12.21 Diagrama de blocos de um sistema em malha fechada.

  Deseja-se projetar um controlador Gc(z) de modo que a resposta y(kT) para um degrau unitário na referência r(kT) tenha um sobressinal máximo Mp = 16,3% e um tempo de pico tp = 1s.

  Solução

  O primeiro passo consiste em converter as especificações de projeto, baseadas em índices de desempenho da resposta temporal (sobressinal e tempo de pico), nos correspondentes polos de malha fechada do plano s. A seguir, os polos do plano s são mapeados no plano z.

  A função de transferência de um sistema de segunda ordem padrão é dada por

   [img:Illustration] 

  cujos polos de malha fechada são

   [img:Illustration] 

  Para que os polos de malha fechada possam ser determinados basta calcular os valores do coeficiente de amortecimento ξ e da frequência natural não amortecida ωn, que podem ser obtidos a partir do sobressinal Mp e do tempo de pico tp, respectivamente. Assim,

   [img:Illustration] 

  O tempo de pico tp é dado por

   [img:Illustration] 

  Assim, a frequência natural não amortecida ωn vale

   [img:Illustration] 

  O período Td das oscilações do sinal de saída durante o transitório é dado por

   [img:Illustration] 

  Na prática o período de amostragem T é escolhido como sendo pelo menos 10 vezes menor que o período das oscilações, ou seja,

   [img:Illustration] 

  Para que o sistema em malha fechada satisfaça às especificações de projeto (Mp = 16,3% e

   [img:Illustration] 

  No plano z os polos correspondentes são mapeados em

   [img:Illustration] 

  A função de transferência Gp(z) do subsistema D/A + processo + A/D é dada por

   [img:Illustration] 

  Da Equação (12.111) obtém-se

   [img:Illustration] 

  O diagrama de blocos do sistema discreto equivalente ao da Figura 12.21 é apresentado na Figura 12.22.

   [img:Illustration] 

  Figura 12.22 Diagrama de blocos do sistema discreto.

  Para o projeto do controlador Gc(z) podem ser utilizados os métodos do lugar das raízes ou da imposição algébrica de polos, que são idênticos aos do plano s, exceção feita ao limite da estabilidade, que no plano s é o eixo jω, e no plano z é a circunferência de raio unitário.

  

### Projeto por meio do lugar das raízes

  Nesta técnica de projeto calcula-se uma função de transferência para o controlador Gc(z) de modo que o lugar das raízes passe pelos polos de malha fechada desejados (12.135). Uma vez que isso ocorra o sistema em malha fechada irá apresentar o comportamento transitório desejado.

  As especificações de projeto podem ser satisfeitas por meio de um controlador de primeira ordem, com função de transferência

   [img:Illustration] 

  A função de transferência de malha aberta é dada por

   [img:Illustration] 

  Existem infinitos valores para K, C1 e C2 que satisfazem às especificações de projeto. Uma solução é cancelar o zero do controlador com o polo estável da planta. Com isso os valores de C2 e K podem ser calculados por meio das condições de fase e módulo, respectivamente.

  Assim, adotando C1 = −0,8187, obtém-se

   [img:Illustration] 

  Da condição de fase, tem-se que

   [img:Illustration] 

  ou seja,

   [img:Illustration] 

  O valor de C2 deve ser calculado num dos polos de malha fechada z1,2 ≅ 0,5629 ± 0,4090j. Da Equação (12.142) obtém-se

   [img:Illustration] 

  Na Figura 12.23 é apresentado o gráfico do lugar das raízes.

   [img:Illustration] 

  Figura 12.23 Lugar das raízes.

  O valor de K pode ser calculado por meio da condição de módulo, ou seja,

   [img:Illustration] 

  Substituindo um dos polos complexos de malha fechada z1,2 ≅ 0,5629 ± 0,4090j na Equação (12.144), obtém-se

   [img:Illustration] 

  Portanto, a função de transferência do controlador é dada por

   [img:Illustration] 

  

### Projeto por meio de imposição algébrica de polos

  Nesta técnica de projeto a função de transferência do controlador Gc(z) é calculada por meio de uma imposição algébrica de polos semelhante ao caso dos sistemas de tempo contínuo.

  Os polos de malha fechada desejados (12.135) produzem o polinômio característico

   [img:Illustration] 

  A função de transferência do processo Gp(z) tem grau n = 2. O controlador Gc(z) deve ter grau m ≥ n − 1. Assim, assumindo m = 1, a função de transferência do controlador é do tipo

   [img:Illustration] 

  A função de transferência de malha aberta é dada por

   [img:Illustration] 

  Supondo que o zero do controlador cancela o polo estável da planta, então

   [img:Illustration] 

  A função de transferência de malha fechada é dada por

   [img:Illustration] 

  cujo polinômio característico é

   [img:Illustration] 

  Comparando os polinômios (12.147) e (12.152), tem-se o seguinte sistema:

   [img:Illustration] 

  Resolvendo o sistema, obtém-se C2 ≅ −0,3109 e K ≅ 9,9. Portanto, a função de transferência do controlador é dada por

   [img:Illustration] 

  que é a mesma obtida pelo método do lugar das raízes.

  

### Resposta ao degrau

  Substituindo os valores de K e C2 na Equação (12.151) a função de transferência de malha fechada resulta

   [img:Illustration] 

  Aplicando a transformada Z inversa e a propriedade do atraso, obtém-se a seguinte equação de diferenças

   [img:Illustration] 

  Sabendo-se que y(−0,2) = y(−0,4) = 0 e que r(kT) é um degrau unitário, então os valores de y(kT) podem ser calculados por meio da implementação da Equação (12.156) num programa de computador. A seguir é apresentado o trecho de um programa, escrito na linguagem C, que calcula os valores da sequência y(kT) para k = 0, 1, 2, . . . , 10.

  Tabela 12.3 Programa e coeficientes para k = 0, 1, 2, . . . , 10

   [img:Illustration] 

  Na Figura 12.24 é apresentado o gráfico da resposta ao degrau unitário y(kT) com o efeito de um segurador. Note que a resposta apresenta o sobressinal (Mp ≅ 16,3%) e o tempo de pico (tp = 1s) de acordo com as especificações de projeto do controlador. Além disso, com o controlador Gc(z) foi possível reduzir o sobressinal e acelerar as respostas do sistema sem controlador apresentadas na Figura 12.20.

   [img:Illustration] 

  Figura 12.24 Resposta ao degrau unitário.

  ■

  

### 12.8 Controlador PID discreto

  O digrama de blocos de um sistema em malha fechada com o controlador PID(z) é apresentado na Figura 12.25.

   [img:Illustration] 

  Figura 12.25 Diagrama de blocos de um sistema em malha fechada com o controlador PID(z).

  Conforme foi visto no Capítulo 6, a função de transferência do controlador PID de tempo contínuo tem três partes (Proporcional+Integral+Derivativa):

   [img:Illustration] 

  Diversas aproximações podem ser empregadas para obter uma função de transferência em z a partir da função de transferência em s (12.157). A melhor aproximação para a parte integral é obtida com o método de Tustin, e a melhor aproximação para a parte derivativa é obtida com o método retangular para trás. Assim,

   [img:Illustration] 

  A Equação (12.158) também pode ser escrita como

   [img:Illustration] 

  cuja equação de diferenças a ser implementada num programa de computador é

   [img:Illustration] 

  Por ser imprópria7 e pelo fato de a parte derivativa possuir um ganho que cresce com o aumento da frequência, amplificando ruídos de alta frequência, a função de transferência (12.157) não é implementada na prática. Então a função de transferência (12.157) é substituída por

   [img:Illustration] 

  sendo N um parâmetro tipicamente adotado entre 0,05 e 0,17.

  Usando a aproximação de Tustin para a parte integral e o método do mapeamento polo-zero para a parte derivativa na Equação (12.161), a função de transferência do controlador PID(z) pode ser escrita como

   [img:Illustration] 

  Para evitar que o controlador forneça na sua saída sinais com amplitude elevada, se ocorrerem variações do tipo degrau na referência, a parte derivativa pode ser implementada como realimentação da saída. Nesse caso a estrutura do controlador é dada por

   [img:Illustration] 

  Uma outra forma de evitar que o controlador forneça na sua saída sinais com amplitude elevada é implementar também a parte proporcional como realimentação da saída, ou seja,

   [img:Illustration] 

  

### Exemplo 12.7

  Deseja-se projetar um controlador Gc(z) para o sistema da Figura 12.26 de modo que:

  • o erro estacionário seja nulo para entrada r(kT) do tipo degrau unitário e

  • os polos de malha fechada dominantes tenham coeficiente de amortecimento ξ = 0,5 e frequencia natural ωn = 2 (rad/s).

   [img:Illustration] 

  Figura 12.26 Diagrama de blocos de um sistema em malha fechada.

  Solução

  Os polos de malha fechada dominantes devem estar localizados em

   [img:Illustration] 

  Se os polos dominantes tiverem influência predominante na dinâmica do sistema a resposta ao degrau deve apresentar um sobressinal próximo de Mp ≅ 16,3% e um tempo de acomodação próximo de ts ≅ 4 s (critério de 2%).

  O período Td das oscilações do sinal de saída durante o transitório é dado por

   [img:Illustration] 

  O período de amostragem T é escolhido como sendo pelo menos 10 vezes menor que o período das oscilações. Adotando T = 0,4, no plano z os polos correspondentes são mapeados em

   [img:Illustration] 

  A função de transferência Gp(z) do subsistema D/A + processo + A/D é dada por

   [img:Illustration] 

  

### Projeto por meio do lugar das raízes

  Para que o sistema em malha fechada apresente o comportamento transitório desejado a função de transferência do controlador Gc(z) deve ser calculada de modo que o lugar das raízes passe pelos polos de malha fechada desejados (12.168). Além disso, como a planta não possui integrador, para que o erro estacionário seja nulo para degrau em r(kT) o controlador deve possuir um polo em z = 1. Essas especificações podem ser satisfeitas com o controlador PID:

   [img:Illustration] 

  A função de transferência de malha aberta é dada por

   [img:Illustration] 

  Cancelando um dos polos estáveis da planta (C2 = −0,6703) as constantes C1 e K podem ser calculadas por meio das condições de fase e módulo, respectivamente. Da condição de fase tem-se que

   [img:Illustration] 

  Assim,

   [img:Illustration] 

  A constante C1 deve ser calculada num dos polos desejados z1,2 ≅ 0,5158 ± 0,4281j, ou seja,

   [img:Illustration] 

  Na Figura 12.27 é apresentado o gráfico do lugar das raízes. O valor de K em qualquer ponto do lugar das raízes pode ser calculado por meio da condição de módulo, ou seja,

   [img:Illustration] 

  Substituindo um dos polos complexos de malha fechada z1,2 ≅ 0,5158 ± 0,4281j na Equação (12.174), obtém-se

   [img:Illustration] 

  Portanto, a função de transferência do controlador PID é dada por

   [img:Illustration] 

  A função de transferência de malha fechada é dada por

   [img:Illustration] 

  cujos polos de malha fechada são z1,2 ≅ 0,5158 ± 0,4281j e z3 ≅ 0,1181.

   [img:Illustration] 

  Figura 12.27 Lugar das raízes.

  

### Projeto por meio de imposição algébrica de polos

  Supondo que um zero do controlador PID cancela o polo em z = 0,6703 da planta (C2 = −0,6703), a função de transferência de malha aberta resulta

   [img:Illustration] 

  A função de transferência de malha fechada é dada por

   [img:Illustration] 

  cujo polinômio característico é

   [img:Illustration] 

  Como o polinômio característico é de terceira ordem, as suas raízes são formadas pelos polos de malha fechada desejados (12.167) e por um terceiro polo em z = p, ou seja,

   [img:Illustration] 

  Comparando os polinômios (12.180) e (12.181), obtém-se um sistema cuja solução é C1 ≅ −0,2640, K ≅ 5,5153 e p = 0,1181. Logo, a função de transferência do controlador PID é a mesma obtida pelo método do lugar das raízes.

  

### Resposta ao degrau

  Escrevendo a Equação (12.177) com potências negativas de z, a função de transferência de malha fechada resulta como

   [img:Illustration] 

  Aplicando a transformada Z inversa e a propriedade do atraso, obtém-se

   [img:Illustration] 

  Na Tabela 12.4 é apresentada a resposta y(kT) quando r(kT) é um degrau unitário. Note que o tempo de acomodação obtido está de acordo com o especificado (ts = 4 s para o critério de 2%), e o sobressinal obtido (Mp ≅ 18,61%) também está próximo do especificado (Mp ≅ 16,3%).

  Tabela 12.4 Resposta ao degrau y(kT) para kT = 0 ; 0,4 ; 0,8 ; 1,2 ; . . . ; 4

  
    
      

      
    

    
      
        
          kT

        

        
          0,0

        

        
          0,4

        

        
          0,8

        

        
          1,2

        

        
          1,6

        

        
          2,0

        

        
          2,4

        

        
          2,8

        

        
          3,2

        

        
          3,6

        

        
          4,0

        
      

      
        
          y(kT)

        

        
          0

        

        
          0,2997

        

        
          0,7660

        

        
          1,0780

        

        
          1,1861

        

        
          1,1571

        

        
          1,0784

        

        
          1,0103

        

        
          0,9754

        

        
          0,9700

        

        
          0,9801

        
      

    
  

  Na Figura 12.28 é apresentado o gráfico da resposta ao degrau y(kT). Note que o erro estacionário é nulo, pois e(∞) = r(∞) − y(∞) = 0.

   [img:Illustration] 

  Figura 12.28 Resposta ao degrau unitário.

  ■

  

### 12.9 Controlador PID com ganho variável (adaptativo)

  Na forma digital o controlador PID pode ser facilmente implementado com ganhos variáveis, o que tem utilidade principalmente no controle de plantas não lineares ou lineares com variações lentas. A seguir são apresentadas algumas regras empíricas, utilizadas na prática, que podem ser adotadas em alguns casos específicos.

  • Ganho variável com o erro.

  Um ajuste de ganho "baixo" aumenta o erro estacionário, inibe oscilações e o windup8;

  Um ajuste de ganho "alto" reduz o erro estacionário, melhora a regulação e o desempenho.

  • Ganho variável com a saída da planta.

  Para sistemas que respondem rapidamente quando a saída da planta possui um valor "baixo" e lentamente quando a saída da planta possui um valor "alto", como, por exemplo, motores a combustão e turbinas, podem-se adotar as seguintes regras:

  Se a saída da planta possui um valor "baixo" ajusta-se um ganho "baixo";

  Se a saída da planta possui um valor "alto" ajusta-se um ganho "alto".

  • Ganho variável com o sinal algébrico do erro.

  Para alguns sistemas não lineares, se o erro for positivo ajusta-se um ganho Kc e se o erro for negativo ajusta-se um ganho diferente Kc.

  • Ganho variável com a carga ou com a entrada da planta.

  Para sistemas em que o sinal de entrada da planta varia de acordo com a carga aplicada, como, por exemplo, motores a combustão, podem-se adotar as seguintes regras:

  Se a carga ou a entrada da planta tiver um valor "baixo" ajusta-se um ganho "baixo";

  Se a carga ou a entrada da planta tiver um valor "alto" ajusta-se um ganho "alto".

  

### 12.10 Projeto no domínio da frequência

  Conforme já foi analisado anteriormente para sistemas de tempo contínuo, o plano s pode ser associado ao domínio da frequência pela relação s = jω. Assim, a resposta em frequência de uma função G(jω) é dada por

   [img:Illustration] 

  No caso de sistemas de tempo discreto o plano z também pode ser associado ao domínio da frequência, mas pela relação z = esT = ejωT, de modo que a resposta em frequência seja

   [img:Illustration] 

  Porém, os diagramas de Bode, que representam a resposta em frequência dada por (12.185), não podem ser desenhados por meio de assíntotas. Nesse caso os gráficos de Bode podem ser obtidos se seus pontos forem calculados numericamente por meio de recursos computacionais. Para isso basta variar a frequência ω e realizar o mapeamento z = ejωT.

  

#### 12.10.1 Formas de mapeamento

  Para utilizar as mesmas regras de aproximações assintóticas dos diagramas de Bode de sistemas de tempo contínuo e, com isso, ganhar uma maior visão nos procedimentos de projeto pode-se realizar uma transformação bilinear num plano u, dada por

   [img:Illustration] 

  ou

   [img:Illustration] 

  Na Figura 12.29 são apresentados os mapeamentos nos planos s, z e u. No domínio da frequência o plano u é representado por uma frequência fictícia v, de modo que u = jv.

   [img:Illustration] 

  Figura 12.29 Mapeamentos nos planos s, z e u.

  Note que quando ω varia de 0 a +π/T no eixo jω do plano s, z varia de +1 a –1 na circunferência de raio unitário e v varia de 0 a +∞ no eixo jv do plano u. A diferença entre os planos s e u é que enquanto no plano s a frequência ω está na faixa de –π/T ≤ ω ≤ +π/T, no plano u a frequência v está na faixa de –∞ < v < +∞

  A relação entre a frequência v do plano u com a frequência ω do plano s é dada por

   [img:Illustration] 

  ou

   [img:Illustration] 

  A Equação (12.189) mostra que há uma distorção na escala de frequências entre os planos s e u. Porém, para ωT/2 "pequeno"

   [img:Illustration] 

  ou seja, neste caso o comportamento das funções nos planos s e u é semelhante.

  Na Figura 12.30 é apresentado um gráfico mostrando a relação entre as frequências v e ω.

   [img:Illustration] 

  Figura 12.30 Relação entre as frequências v e ω.

  

#### 12.10.2 Diagramas de Bode

  As regras para o traçado dos diagramas de Bode de uma função G(jv) são as mesmas que foram estudadas no Capítulo 5 para a função G(jω). Os diagramas de Bode consistem em dois gráficos que conjuntamente representam a resposta em frequência:

  
    • módulo de G(jv) versus frequência v, ambos em escala logarítmica;

    • fase de G(jv) versus frequência v, esta última em escala logarítmica.

  

  Para traçar os diagramas de Bode de uma planta discreta também é necessário considerar o atraso de fase adicional proveniente do segurador de ordem zero, que é inexistente nas plantas contínuas.

  

### Exemplo 12.8

  Considere o sistema da Figura 12.31.

   [img:Illustration] 

  Figura 12.31 Subsistema D/A + processo + A/D.

  A função de transferência Gp(z) do subsistema D/A + processo + A/D é dada por

   [img:Illustration] 

  Da Equação (12.137) obtém-se

   [img:Illustration] 

  Usando a transformação bilinear (12.187), com T = 0,2 , tem-se que

   [img:Illustration] 

  Assim,

   [img:Illustration] 

  Note que o processo Gp(s) possui dois polos em s = 0 e s = –1 e que os polos de Gp(u) também são u = 0 e u = –1. Em baixas frequências, sem considerar o integrador, os ganhos também são iguais. Porém, Gp(u) tem dois zeros em u = –300 e u = 10, enquanto Gp(s) não possui nenhum zero. Como Gp(u) tem um zero no semiplano direito do plano u, então G(u) é um sistema de fase não mínima.

  Na Figura 12.32 são apresentados os diagramas de Bode de Gp(jω) e Gp(jv). Multiplicando por 20 o logaritmo dos termos fatorados de |Gp(jω)| e |Gp(jv)| os gráficos do módulo podem ser obtidos por meio da soma de assíntotas, com unidade resultante em decibel (dB). Os gráficos da fase de ∠Gp(jω) e ∠Gp(jv) são obtidos por meio da soma das fases de cada um dos termos fatorados.

  Em baixas frequências os gráficos de Bode de Gp(jω) e Gp(jv) são semelhantes. A principal diferença ocorre em altas frequências. Note que

   [img:Illustration] 

   [img:Illustration] 

  Figura 12.32 Gráficos de Bode de Gp(jω) e Gp(jv).

  enquanto

   [img:Illustration] 

  ou

   [img:Illustration] 

  Essa diferença pode ser explicada pelo fato de que a região de interesse da transformação bilinear está na faixa de 0 ≤ ω ≤ π/T.

  Devido ao zero de fase não mínima em u = 10 de Gp(u), a fase de Gp(jv) apresenta uma distorção quando comparada à fase de Gp(jω). Porém, em altas frequências para ambos os gráficos tem-se que

   [img:Illustration] 

  ■

  

#### 12.10.3 Projeto do controlador

  O projeto no domínio da frequência é indicado quando as especificações da resposta do sistema são fornecidas em termos do erro estacionário e das margens de ganho e de fase. Conforme estudado anteriormente, diversos tipos de controladores podem ser utilizados, como os compensadores por avanço e atraso de fase ou os controladores PID.

  A compensação por avanço de fase melhora as margens de estabilidade e aumenta a banda passante, fazendo com que a resposta transitória do sistema se torne mais rápida. Porém, a resposta pode apresentar mais ruído devido ao aumento do ganho em altas frequências.

  Já a compensação por atraso de fase é utilizada para melhorar a margem de fase por meio de uma redução do ganho em altas frequências. Como a banda passante é reduzida a resposta transitória do sistema se torna mais lenta. Por outro lado, essa compensação também pode ser utilizada para manter a margem de fase e aumentar o ganho em baixas frequências, reduzindo com isso o erro estacionário.

  O controlador PID é um tipo de compensador por avanço e atraso de fase. A ação de controle PD se comporta como um compensador por avanço de fase, enquanto a ação de controle PI se comporta como um compensador por atraso de fase. O controlador PID consiste na combinação dos efeitos dos controles PD e PI.

  

### Exemplo 12.9

  Considere o sistema da Figura 12.33.

   [img:Illustration] 

  Figura 12.33 Diagrama de blocos de um sistema em malha fechada.

  Deseja-se projetar um controlador Gc(z) de modo a satisfazer às seguintes especificações:

  • erro estacionário e(∞) = 0,3 para entrada de referência do tipo rampa unitária;

  • margem de fase MF ≅ 50°.

  A função de transferência Gp(u) do subsistema D/A + processo + A/D, deduzida no exemplo anterior, é dada por

   [img:Illustration] 

  Um compensador por avanço de fase pode resolver o problema. Caso contrário, deve-se refazer o projeto com um outro tipo de compensador. A função de transferência de um compensador por avanço de fase é dada por

   [img:Illustration] 

  O diagrama de blocos do sistema simplificado é apresentado na Figura 12.34.

   [img:Illustration] 

  Figura 12.34 Diagrama de blocos do sistema simplificado.

  A função de transferência de malha aberta Gma(u) é dada por

   [img:Illustration] 

  A constante K do compensador Gc(u) pode ser obtida a partir da especificação do erro estacionário, ou seja,

   [img:Illustration] 

  Sabendo-se que R(u) = 1/u2, então

   [img:Illustration] 

  Portanto, K = 3,3333 ou, em decibéis, K ≅ 10,5 dB.

  Os gráficos de Bode de KGp(jv) são apresentados na Figura 12.35. Comparando os gráficos desta figura com os gráficos da Figura 12.32 verifica-se que o ganho K desloca o gráfico do módulo na direção vertical de K ≅ 10,5 dB. Logo, o ponto de cruzamento da curva de módulo em 0 dB (ganho 1) se desloca para a direita, ocorrendo numa frequência mais alta, ou seja, em v ≅ 1,7 (rad/s). Com isso, a margem de fase é MF ≅ 21°.

   [img:Illustration] 

  Figura 12.35 Gráficos de Bode de KGp(jv).

  A margem de fase é determinada pela frequência de cruzamento em que o ganho do sistema em malha aberta vale 1 ou 0 dB. Para que a margem de fase seja 50° o compensador deve fornecer uma fase de pelo menos 50° – 21° = 29°. Porém, como o ganho do compensador cresce a partir da frequência 1/τ a frequência de cruzamento de ganho 1 do sistema em malha aberta é deslocada para a direita. Logo, o avanço de fase máximo ϕm, a ser fornecido pelo compensador, deve ser na realidade maior que 29o. Adotando uma parcela de correção9 de 17° a mais o avanço de fase máximo a ser fornecido pelo compensador é ϕm ≅ 50° – 21° + 17° ≅ 46°.

  Conforme foi visto no Capítulo 5,

   [img:Illustration] 

  e

   [img:Illustration] 

  Na frequência vm o ganho de malha aberta deve ser igual a 1 ou 0 dB, ou seja,

   [img:Illustration] 

  Logo, o módulo do sistema não compensado deve valer na frequência vm

   [img:Illustration] 

  O valor de τ é obtido da relação

   [img:Illustration] 

  Portanto, a função de transferência do compensador é dada por

   [img:Illustration] 

  Os gráficos de Bode do sistema em malha aberta Gma(jv), do controlador Gc(jv) e da planta Gp(jv) são apresentados na Figura 12.36.

  Note que MF = 180° + ∠Gma(j2,84) = 180° + ϕm + ∠Gp(j2,84) = 180° + 46° – 176° = 50°.

   [img:Illustration] 

  Figura 12.36 Gráficos de Bode de Gma(jv), Gc(jv) e Gp(jv).

  Usando a transformação bilinear (12.186) para T = 0,2 , obtém-se

   [img:Illustration] 

  Assim,

   [img:Illustration] 

  A função de transferência de malha aberta discreta é dada por

   [img:Illustration] 

  O erro estacionário para entrada do tipo rampa unitária vale

   [img:Illustration] 

  que está de acordo com o especificado no projeto.

  A função de transferência de malha fechada resulta como

   [img:Illustration] 

  Aplicando a transformada Z inversa e a propriedade do atraso, obtém-se

   [img:Illustration] 

  Na Figura 12.37 é apresentado o gráfico da resposta y(kT), quando r(kT) é uma rampa unitária. Note que o erro estacionário é e(∞) = r(∞) – y(∞) = 0,3.

   [img:Illustration] 

  Figura 12.37 Resposta à rampa unitária.

  

### 12.11 Controlador dead beat

  A resposta transitória de um sistema em malha fechada para uma entrada degrau é definida como dead beat quando o tempo de acomodação é mínimo, o erro estacionário é nulo e não há oscilações entre os instantes de amostragem.

  Considere o sistema em malha fechada da Figura 12.38.

   [img:Illustration] 

  Figura 12.38 Diagrama de blocos de um sistema em malha fechada.

  A função de transferência de malha fechada é dada por

   [img:Illustration] 

  Isolando a função de transferência Gc(z) do controlador na Equação (12.216), obtém-se

   [img:Illustration] 

  Conforme se pode perceber na Equação (12.217), o controlador Gc(z) inverte a planta Gp(z) de modo a produzir os resultados desejados. É necessário investigar em que situações isso é possível.

  

#### 12.11.1 Causalidade

  • O controlador Gc(z) deve ser causal, isto é, o grau do seu numerador deve ser menor ou igual ao grau do seu denominador. Caso contrário, o controlador necessitaria de entradas futuras para produzir uma saída atual.

  • Para que a resposta ocorra num tempo de acomodação finito e para que o sistema em malha fechada seja causal, a função de transferência de malha fechada deve ser do tipo

   [img:Illustration] 

  com p ≥ n, sendo n a ordem da planta.

  • A planta não pode responder de forma instantânea quando um sinal de controle de amplitude finita é aplicado na sua entrada. Se a planta tiver um atraso de um período de amostragem a função de transferência de malha fechada Gmf(z) deve ter no mínimo o mesmo tempo de atraso pois, caso contrário, o sistema em malha fechada teria que responder antes que uma entrada fosse aplicada nele. Assim, se por exemplo a expansão em série de Gp(z) começar em z–2, então a expansão em série (12.219) deve começar no mínimo também em z–2, ou seja,

   [img:Illustration] 

  

#### 12.11.2 Erro estacionário

  Da Figura 12.38 tem-se que

   [img:Illustration] 

  O erro estacionário é dado por

   [img:Illustration] 

  • Quando R(z) é um degrau de amplitude A ≠ 0 tem-se que

   [img:Illustration] 

  Se a planta Gp(z) tiver um ou mais polos em z = 1, então e(∞) = 0. Portanto,

   [img:Illustration] 

  • Quando R(z) é uma rampa com coeficiente A ≠ 0 tem-se que

   [img:Illustration] 

  Usando a regra de L’Hospital

   [img:Illustration] 

  Se a planta Gp(z) tiver um polo em z = 1, então  [img:Illustration]  com K constante. Portanto,

   [img:Illustration] 

  Se a planta Gp(z) tiver dois ou mais polos em z = 1, então e(∞) = 0. Portanto,

   [img:Illustration] 

  Na Tabela 12.5 são apresentadas as restrições para a função de transferência de malha fechada Gmf(z) em função da entrada de referência R(z) e da quantidade de polos da planta em z = 1.

  Tabela 12.5 Restrições para a função de transferência de malha fechada Gmf(z)

   [img:Illustration] 

  

### Exemplo 12.10

  Deseja-se projetar um controlador dead beat para o sistema da Figura 12.39, de modo que o tempo de acomodação seja mínimo, o erro estacionário para referência do tipo degrau seja nulo e que não haja oscilações da saída entre os instantes de amostragem. Suponha um período de amostragem T = 1s.

   [img:Illustration] 

  Figura 12.39 Diagrama de blocos de um sistema em malha fechada.

  A função de transferência Gp(z) do subsistema D/A + processo + A/D é dada por

   [img:Illustration] 

  Como a planta Gp(z) é de ordem 3, da Equação (12.219) tem-se que a função de transferência de malha fechada é do tipo

   [img:Illustration] 

  Fazendo a divisão na Equação (12.229), Gp(z) pode ser escrita como soma de potências, ou seja,

   [img:Illustration] 

  Como o primeiro termo de Gp(z) começa com z–3, ou seja, há um atraso de três períodos de amostragem, então Gmf(z) também deve começar com um termo em z–3. Logo, g0 = g1 = g2 = 0 e

   [img:Illustration] 

  Aplicando um degrau na referência, o erro estacionário deve ser nulo. Para que isso ocorra é necessário que Gmf(1) seja igual a 1. Logo, g3 = 1 e

   [img:Illustration] 

  O controlador dead beat é calculado por meio da Equação (12.217), ou seja,

   [img:Illustration] 

  Aplicando a transformada Z inversa e a propriedade do atraso nas Equações (12.233) e (12.234), obtém-se

   [img:Illustration] 

  Na Figura 12.40 é apresentado o gráfico da resposta y(kT) quando r(kT) é um degrau unitário. Note neste gráfico que a resposta possui um atraso de três períodos de amostragem e erro estacionário nulo.

   [img:Illustration] 

  Figura 12.40 Respostas ao degrau unitário.

  Na Figura 12.41 é apresentado o gráfico da saída do controlador u(kT) quando r(kT) é um degrau unitário. Como a saída do controlador é constante para kT ≥ 1, então a saída contínua da planta y(t) também é constante e não apresenta oscilações entre os instantes de amostragem.

   [img:Illustration] 

  Figura 12.41 Saída do controlador u(kT).

  O projeto do controlador dead beat independe da escolha do período de amostragem T. Todavia, se o período de amostragem for escolhido muito "pequeno" a amplitude do sinal de controle u(t) pode ser muito elevada, podendo causar sua saturação. Por outro lado, se o período de amostragem for escolhido muito "grande" o sistema em malha fechada pode se tornar até mesmo instável. Na prática utiliza-se um período de amostragem que seja suficientemente "pequeno" para não ocorrer saturação do sinal de controle.

  ■

  

#### 12.11.3 Polos e zeros fora ou sobre a circunferência de raio unitário

  Polos da planta Gp(z) fora ou sobre a circunferência de raio unitário (|z| ≥ 1) não devem ser cancelados por zeros do controlador Gc(z), pois na prática este cancelamento nunca é perfeito e, consequentemente, o sistema em malha fechada resulta instável.

  Da mesma forma, o controlador não deve possuir polos instáveis que cancelem zeros da planta fora ou sobre a circunferência de raio unitário.

  Suponha, por simplicidade, que a planta possua um zero em z = –a e um polo em z = –b, ambos fora ou sobre a circunferência de raio unitário (|z| ≥ 1).

  Definindo

   [img:Illustration] 

  Assim, a função de transferência de malha fechada é dada por

   [img:Illustration] 

  e

   [img:Illustration] 

  Da Equação (12.217) obtém-se

   [img:Illustration] 

  Das Equações (12.238) e (12.239) tem-se que

  
    • Um zero da planta Gp(z) fora ou sobre a circunferência de raio unitário (|z| = |a| ≥ 1) deve ser zero da função Gmf(z), ou seja, Gmf(a) = 0.

    • Um polo da planta Gp(z) fora ou sobre a circunferência de raio unitário (|z| = |b| ≥ 1) deve ser zero da função 1 – Gmf(z), ou seja, 1 – Gmf(b) = 0.

  

  

### Exemplo 12.11

  Deseja-se projetar um controlador para o sistema da Figura 12.42 de modo que o tempo de acomodação seja mínimo, o erro estacionário para referência do tipo degrau seja nulo e sem que haja preocupações com oscilações da saída entre os instantes de amostragem. Suponha um período de amostragem T = 1s.

   [img:Illustration] 

  Figura 12.42 Diagrama de blocos de um sistema em malha fechada.

  A função de transferência Gp(z) do subsistema D/A + processo + A/D é dada por

   [img:Illustration] 

  Como a planta Gp(z) é de ordem 2, da Equação (12.219) tem-se que a função de transferência de malha fechada é do tipo

   [img:Illustration] 

  Fazendo a divisão na Equação (12.242), o primeiro termo de Gp(z) começa com z–1. Logo, para que o sistema em malha fechada seja causal Gmf(z) também deve começar com um termo em z–1. Assim, g0 = 0 e

   [img:Illustration] 

  Aplicando um degrau na referência o erro estacionário deve ser nulo. Para que isso ocorra é necessário que Gmf(1) seja igual a 1, isto é,

   [img:Illustration] 

  A planta Gp(z) possui um polo fora da circunferência de raio unitário em z = 1,6487. Assim, este polo deve ser zero da função 1 – Gmf(z), ou seja,

   [img:Illustration] 

  Das Equações (12.245) e (12.246) tem-se o seguinte sistema

   [img:Illustration] 

  cuja solução é g1 = 2,6487 e g2 = –1,6487.

  Portanto,

   [img:Illustration] 

  O controlador é calculado por meio da Equação (12.217), ou seja,

   [img:Illustration] 

  Aplicando a transformada Z inversa e a propriedade do atraso nas Equações (12.248) e (12.250), obtém-se

   [img:Illustration] 

  Na Figura 12.43 são apresentados os gráficos da resposta discreta y(kT) e da resposta contínua y(t) quando r(kT) é um degrau unitário. Note que em kT = 2s a resposta y(kT) já atingiu o estado estacionário, porém com um sobressinal elevado.

   [img:Illustration] 

  Figura 12.43 Respostas ao degrau unitário.

  Um inconveniente observado na Figura 12.43 é que a saída real da planta y(t) apresenta oscilações indesejáveis entre os períodos de amostragem. Este problema ocorre porque o controlador Gc(z) possui um polo próximo da circunferência de raio unitário em z = –0,8490. Este polo causa uma oscilação no sinal de controle u(kT) que causa, por sua vez, a oscilação da saída da planta y(t). A resposta discreta y(kT) não apresenta oscilação porque o polo do controlador em z = –0,8490 é cancelado com um zero da mesma posição da planta Gp(z).

  Na Figura 12.44 é mostrada a oscilação do sinal de controle u(kT). Embora o controlador dead beat forneça uma resposta rápida e com erro estacionário nulo a amplitude do sinal de controle pode ser muito elevada, o que pode causar sua saturação e excessivo desgaste de atuadores, que não suportam mudanças repentinas em suas entradas.

   [img:Illustration] 

  Figura 12.44 Saída do controlador u(kT).

  ■

  

#### 12.11.4 Eliminação de oscilações entre os instantes de amostragem

  Quando a entrada de referência é do tipo degrau, para que a saída da planta não apresente oscilações entre os períodos de amostragem é necessário que y(t) seja constante após o tempo de acomodação ser alcançado. Para que isso ocorra basta que a entrada da planta u(t) também seja constante após esse período.

  Do sistema da Figura 12.38 tem-se que

   [img:Illustration] 

  Definindo Gp(z) = N(z)/D(z), da Equação (12.218) tem-se que

   [img:Illustration] 

  Sendo r(kT) uma entrada do tipo degrau, para que u(kT) seja constante após um tempo de acomodação os polos da função de transferência (12.254) devem estar longe da circunferência de raio unitário. Como a função (12.254) possui p polos em z = 0, então os zeros da planta Gp(z) próximos da circunferência de raio unitário é que causam as oscilações entre os períodos de amostragem.

  Assim, para que u(kT) seja constante após um tempo de acomodação basta cancelar os zeros indesejáveis de N(z) com zeros de Gmf(z). Para isso basta acrescentar restrições no projeto do controlador de que zeros da planta Gp(z), próximos da cincunferência de raio unitário, também são zeros de Gmf(z).

  

### Exemplo 12.12

  Deseja-se projetar um controlador dead beat para o exemplo anterior, de modo que a saída não apresente oscilações entre os instantes de amostragem. Suponha um período de amostragem T = 1s.

  A planta Gp(z) em (12.241) possui um zero indesejável próximo da circunferência de raio unitário em z = –0,8490. Dessa maneira, deve ser incluída no projeto uma restrição de que Gmf(–0,8490) = 0. Por essa razão a função de transferência de malha fechada deve possuir um termo a mais, ou seja,

   [img:Illustration] 

  sendo

   [img:Illustration] 

  Para que o erro estacionário seja nulo, então

   [img:Illustration] 

  Para que o polo fora da circunferência de raio unitário em z = 1,6487 seja zero da função 1 – Gmf(z), então

   [img:Illustration] 

  Das Equações (12.256), (12.257) e (12.258) tem-se o seguinte sistema:

   [img:Illustration] 

  cuja solução é g1 = 1,9322, g2 = 0,2491 e g3 = –1,1813.

  Portanto,

   [img:Illustration] 

  O controlador é calculado por meio da Equação (12.217), ou seja,

   [img:Illustration] 

  Aplicando a transformada Z inversa e a propriedade do atraso nas Equações (12.260) e (12.262), obtém-se

   [img:Illustration] 

  Na Figura 12.45 é apresentado o gráfico da resposta discreta y(kT) e da resposta contínua y(t), quando r(kT) é um degrau unitário. A resposta y(kT) atingiu o estado estacionário em kT = 3s, porém com um sobressinal elevado. Como se pode perceber, as oscilações entre os períodos de amostragem da resposta contínua y(t) foram eliminadas.

   [img:Illustration] 

  Figura 12.45 Respostas ao degrau unitário.

  Na Figura 12.46 é apresentado o gráfico do sinal de controle u(kT). Note que este sinal é constante para kT ≥ 3 s, o que possibilita que a saída y(t) também seja constante a partir desse instante.

   [img:Illustration] 

  Figura 12.46 Saída do controlador u(kT).

  

### 12.12 Exercícios resolvidos

  

### Exercício 12.1

  Obtenha aproximações discretas para o sistema contínuo da Figura 12.47 através dos seguintes métodos: retangular para trás, mapeamento polo-zero, bilinear sem compensação e com compensação de distorção na frequência ωs = 1 rad/s. Para cada método, calcule a resposta analítica da saída y(k) para k = 0, . . . , 5, quando a entrada u(k) for um degrau unitário. Suponha T = 1s.

   [img:Illustration] 

  Figura 12.47 Sistema contínuo.

  Solução

  

### Método retangular para trás

  Da expressão (12.13) tem-se que

   [img:Illustration] 

  Para U(z) degrau unitário obtém-se

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  

### Transformação bilinear ou de Tustin

  Da expressão (12.20) tem-se que

   [img:Illustration] 

  Para U(z) degrau unitário obtém-se

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  

### Transformação bilinear com compensação de distorção em frequência

  A função de transferência contínua deve ser modificada para

   [img:Illustration] 

  Aplicando a transformação bilinear (12.20) na Equação (12.271), obtém-se

   [img:Illustration] 

  Para U(z) degrau unitário obtém-se

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  

### Método do mapeamento polo-zero

  A função de transferência do sistema discreto é dada por

   [img:Illustration] 

  O ganho K é ajustado para que em baixas frequências o ganho do sistema contínuo seja igual ao do sistema discreto, ou seja,

   [img:Illustration] 

  Portanto,

   [img:Illustration] 

  Para U(z) degrau unitário obtém-se

   [img:Illustration] 

  Logo,

   [img:Illustration] 

  Na Tabela 12.6 são apresentados os valores da saída contínua y(t) e discreta y(k) (k = 0, . . . , 5) quando a entrada é um degrau unitário.

  Tabela 12.6 Saída contínua y(t) e discreta y(k)

   [img:Illustration] 

  Na Figura 12.48 são apresentados os gráficos da resposta ao degrau para os métodos analisados.

   [img:Illustration] 

  Figura 12.48 Respostas ao degrau.

  

### Exercício 12.2

  Considere o sistema discreto da Figura 12.49.

   [img:Illustration] 

  Figura 12.49 Sistema discreto.

  Desenhe o lugar das raízes e determine a faixa de valores do ganho K de modo que o sistema seja estável em malha fechada.

  Solução

  Os polos do sistema em malha aberta estão localizados em z1,2 = 0,4±0,2j. O lugar das raízes começa nos polos complexos de malha aberta, seguindo assíntotas verticais na medida em que o ganho K aumenta, conforme representado na Figura 12.50.

   [img:Illustration] 

  Figura 12.50 Lugar das raízes.

  O máximo valor de K que estabiliza o sistema em malha fechada pode ser determinado pelo cruzamento do lugar das raízes com a circunferência de raio unitário, que ocorre nos pontos z1,2 = 0,4 ± 0,9165j. O valor de K num destes pontos pode ser calculado pela condição de módulo

   [img:Illustration] 

  Portanto, o sistema em malha fechada é estável para 0 < K < 0,8.

  

### Exercício 12.3

  Considere o sistema da Figura 12.51.

   [img:Illustration] 

  Figura 12.51 Diagrama de blocos de um sistema em malha fechada.

  Projete um controlador Gc(z) de modo que as seguintes especificações sejam satisfeitas:

  • erro estacionário nulo para entrada r(kT) do tipo degrau unitário e

  • polos de malha fechada dominantes com coeficiente de amortecimento ξ = 0,6 e frequência natural ωn = 1 (rad/s).

  Suponha que o período de amostragem seja T = 1s.

  Solução

  Os polos de malha fechada dominantes devem estar localizados em

   [img:Illustration] 

  Se os polos dominantes tiverem influência predominante na dinâmica do sistema então a resposta ao degrau deve apresentar um sobressinal próximo de Mp ≅ 9,5%. Como este sistema possui um atraso de transporte de 1 s, o tempo de pico máximo está próximo de tp ≅ 4,9 s.

  No plano z os polos são mapeados em

   [img:Illustration] 

  A função de transferência Gp(z) do subsistema D/A + processo + A/D é dada por

   [img:Illustration] 

  

### Projeto por meio do lugar das raízes

  Como a planta não possui integrador, para que o erro estacionário seja nulo para a entrada degrau o controlador deve possuir um polo em z = 1. Esta especificação pode ser satisfeita com um controlador PI ou PID.

  Para que o sistema em malha fechada apresente o comportamento transitório desejado a função de transferência do controlador Gc(z) deve ser calculada de modo que o lugar das raízes passe pelos polos de malha fechada desejados (12.282). Para isso será utilizado um controlador PI, que tem uma função de transferência mais simples que a de um PID, ou seja,

   [img:Illustration] 

  A função de transferência de malha aberta é dada por

   [img:Illustration] 

  As constantes C e K podem ser determinadas pelas condições de fase e módulo, respectivamente. Da condição de fase tem-se que

   [img:Illustration] 

  Assim,

   [img:Illustration] 

  A constante C deve ser calculada num dos polos desejados z1,2 ≅ 0,3824 ± 0,3937j , ou seja,

   [img:Illustration] 

  O valor de K pode ser calculado por meio da condição de módulo, ou seja,

   [img:Illustration] 

  Portanto, a função de transferência do controlador PI é dada por

   [img:Illustration] 

  Na Figura 12.52 é apresentado o gráfico do lugar das raízes.

   [img:Illustration] 

  Figura 12.52 Lugar das raízes.

  A função de transferência de malha fechada é dada por

   [img:Illustration] 

  com polos complexos conjugados de acordo com a especificação.

  

### Projeto por meio de imposição algébrica de polos

  A função de transferência de malha fechada com o controlador PI é dada por

   [img:Illustration] 

  cujo polinômio característico é

   [img:Illustration] 

  Como o polinômio característico é de terceira ordem, suas raízes são formadas pelos polos de malha fechada desejados (12.282) e por um terceiro polo em z = p, ou seja,

   [img:Illustration] 

  Comparando os polinômios (12.294) e (12.295), obtém-se um sistema cuja solução é C ≅ –0,2485, K ≅ 1,0392 e p = 0,3706. Logo, a função de transferência do controlador PI é a mesma obtida pelo método do lugar das raízes.

  

### Resposta ao degrau

  Aplicando a transformada Z inversa na função de transferência de malha fechada, obtém-se

   [img:Illustration] 

  Na Tabela 12.7 é apresentada a resposta y(kT) quando r(kT) é um degrau unitário. Note que o sobressinal máximo obtido é Mp ≅ 7,01%, com tempo de pico máximo tp = 5s. O sobressinal obtido é um pouco menor que o previsto (Mp = 9,5%) devido ao fato de o polo real também influenciar na resposta.

  Tabela 12.7 Resposta ao degrau y(kT) para kT = 0, 1, 2, . . . , 10

   [img:Illustration] 

  Na Figura 12.53 é apresentado o gráfico da resposta ao degrau y(kT). Note que o erro estacionário é nulo, pois e(∞) = r(∞) – y(∞) = 0. Além disso, devido ao atraso de transporte da planta de 1 s a resposta do sistema somente ocorre a partir de kT > 1.

   [img:Illustration] 

  Figura 12.53 Resposta ao degrau unitário.

  

### Exercício 12.4

  Projete um controlador dead beat para o sistema da Figura 12.54 de modo que o tempo de acomodação seja mínimo, o erro estacionário para referência do tipo degrau unitário seja nulo e sem que a saída apresente oscilações entre os instantes de amostragem. Suponha também que o erro estacionário para referência do tipo rampa unitária é igual a 0,2 e que o período de amostragem é T = 1s.

   [img:Illustration] 

  Figura 12.54 Diagrama de blocos de um sistema em malha fechada.

  Solução

  A função de transferência Gp(z) do subsistema D/A + processo + A/D é dada por

   [img:Illustration] 

  
    Restrições de projeto

    i) Fazendo a divisão na Equação (12.297), o primeiro termo de Gp(z) irá começar com z–1. Para a função Gmf(z) ser causal o primeiro coeficiente é nulo, ou seja, g0 = 0.

    ii) O erro estacionário deve ser nulo para referência do tipo degrau unitário. Assim,

     [img:Illustration] 

    iii) A planta possui um polo sobre a circunferência de raio unitário em z = 1. Este polo deve ser zero da função 1 – Gmf(z), ou seja,

     [img:Illustration] 

    iv) O erro estacionário deve ser igual a 0,2 para referência do tipo rampa unitária. Da Equação (12.226) tem-se que

     [img:Illustration] 

    v) A planta possui um zero próximo da circunferência de raio unitário em z = –0,9672. Para evitar oscilações da saída

     [img:Illustration] 

  

  Como g0 é igual a 0 na restrição i) e como a restrição ii) é igual a iii), então a função de transferência de malha fechada tem apenas três termos, ou seja,

   [img:Illustration] 

  Da restrição ii) ou iii) obtém-se

   [img:Illustration] 

  Da restrição iv) tem-se que

   [img:Illustration] 

  Da restrição v) obtém-se

   [img:Illustration] 

  Das Equações (12.303), (12.304) e (12.305) tem-se o seguinte sistema:

   [img:Illustration] 

  A solução do sistema (12.306) é g1 = 1,1649, g2 = 0,4701 e g3 = –0,6351. Logo,

   [img:Illustration] 

  O controlador é calculado por meio da Equação (12.217), ou seja,

   [img:Illustration] 

  Aplicando a transformada Z inversa e a propriedade do atraso nas Equações (12.307) e (12.309), obtém-se

   [img:Illustration] 

  Na Figura 12.55 é apresentado o gráfico da resposta discreta y(kT) e da resposta contínua y(t) quando r(kT) é um degrau unitário. A resposta y(kT) atingiu o estado estacionário em kT = 3s, porém com um sobressinal elevado.

   [img:Illustration] 

  Figura 12.55 Respostas ao degrau unitário.

  Na Figura 12.56 é apresentado o gráfico do sinal de controle u(kT) quando r(kT) é um degrau unitário. Note que este sinal é constante para kT ≥ 3 s, o que possibilita que a saída y(t) também seja constante a partir desse instante.

   [img:Illustration] 

  Figura 12.56 Saída do controlador u(kT) para r(kT) do tipo degrau unitário.

  O erro estacionário para referência do tipo rampa unitária é dado por

   [img:Illustration] 

  Na Figura 12.57 é apresentado o gráfico da resposta y(kT) para entrada de referência do tipo rampa unitária. Observe que e(∞) = 0,2.

   [img:Illustration] 

  Figura 12.57 Resposta à rampa unitária.

  O valor de u(∞) para referência do tipo rampa unitária é dado por

   [img:Illustration] 

  Na Figura 12.58 é apresentado o gráfico do sinal de controle u(kT) quando r(kT) é uma rampa unitária. Note que este sinal é constante (u(∞) ≅ 0,1) para kT ≥ 3 s.

   [img:Illustration] 

  Figura 12.58 Saída do controlador u(kT) para r(kT) do tipo rampa unitária.

  

### 12.13 Exercícios propostos

  

### Exercício 12.5

  Obtenha aproximações discretas para a função de transferência

   [img:Illustration] 

  Aplique os seguintes métodos: retangular para trás, mapeamento polo-zero, bilinear sem compensação e com compensação de distorção na frequência ωs = 1rad/s. Para cada método calcule a resposta analítica da saída y(k) para k = 0, . . . , 5 quando a entrada u(k) for um degrau unitário. Suponha T = 1s.

  

### Exercício 12.6

  Desenhe o lugar das raízes para o sistema da Figura 12.59 e determine a faixa de valores do período de amostragem T que estabiliza o sistema em malha fechada.

   [img:Illustration] 

  Figura 12.59 Sistema discreto.

  

### Exercício 12.7

  Projete um controlador discreto para o sistema da Figura 12.60 de modo que a resposta para um degrau aplicado na referência tenha um sobressinal máximo de 16,3% e um tempo de acomodação de 2s segundo o critério de 2%.

   [img:Illustration] 

  Figura 12.60 Diagrama de blocos de um sistema em malha fechada.

  

### Exercício 12.8

  Projete um controle discreto para o sistema da Figura 12.61 de modo que a resposta para um degrau aplicado na referência tenha um sobressinal máximo de 20% e um tempo de subida de 1 s.

   [img:Illustration] 

  Figura 12.61 Diagrama de blocos de um sistema em malha fechada.

  

### Exercício 12.9

  O esquema de um sistema de levitação magnética é apresentado na Figura 12.62. O sistema consiste em um eletroímã que suspende uma massa de material magnético. A levitação da massa é conseguida através do controle da distância x(t) existente entre a massa e a bobina do eletroímã. Na bobina é instalado um sensor que mede a posição x(t) da massa. A partir dessa medida um sistema de controle discreto calcula uma tensão u(t) a ser aplicada na entrada de um circuito de potência que, por sua vez, gera uma corrente i(t) a ser aplicada na bobina. A função de transferência linear do sistema é dada por

   [img:Illustration] 

  Supondo Kp = 0,1 (A/V) e Ks = 0,25 (V/mm), projete um controlador discreto de modo que a resposta para um degrau aplicado na referência tenha um sobressinal máximo de 20% e um tempo de pico de 0,1 s.

   [img:Illustration] 

  Figura 12.62 Sistema de levitação magnética.

  

### Exercício 12.10

  Considere o sistema da Figura 12.63.

   [img:Illustration] 

  Figura 12.63 Diagrama de blocos de um sistema em malha fechada.

  Deseja-se projetar um controlador Gc(z) de modo a satisfazer às seguintes especificações:

  • erro estacionário nulo para entrada de referência do tipo degrau unitário;

  • margem de fase MF ≅ 30°.

  

### Exercício 12.11

  Projete um controlador dead beat para os sistemas das Figuras 12.60 e 12.61 de modo que o tempo de acomodação seja mínimo, o erro estacionário seja nulo e não haja oscilações da saída entre os instantes de amostragem. Suponha um período de amostragem T = 1s.

  

  __________

  1Prova-se que esta transformação também é válida para sistemas de ordem superior.

  2As aproximações de Padé de ordem superior são muito mais precisas, porém aumentam a ordem da função de transferência e a complexidade do projeto do controlador. Neste caso é fundamental o emprego de ferramentas computacionais, como, por exemplo, o MATLAB.

  3Em algumas aplicações pode-se desprezar o bloco do segurador sem degradação significativa do desempenho. Esses casos podem ser verificados por simulação computacional.

  4Caso esta suposição não seja razoável, os polos de malha fechada devem ser escolhidos por meio de tentativas de Gc(s) buscando a estabilidade e o sobressinal desejado.

  5Cancelamentos entre polos e zeros instáveis não devem ser realizados. Na prática, caso esses cancelamentos não sejam perfeitos o sistema resultante será instável.

  6Para que os comportamentos dos sistemas de segunda e terceira ordens sejam próximos deve-se adotar o terceiro polo em s = −p pelo menos cinco constantes de tempo mais à esquerda dos polos complexos conjugados dominantes, isto é, para p ≥ 5ξωn. Ver Seção 3.7.

  7Uma função de transferência é imprópria se o grau do seu numerador é maior que o grau do seu denominador.

  8Ver Capítulo 6.

  9Caso esta correção não produza um resultado satisfatório, o projeto do controlador deve ser refeito.

<!-- Text/chapter13.xhtml -->





  
  Controle Automático, 2ª edição
  
  



  

## 13


  

## Projeto de Controladores no Espaço de Estados


  

### 13.1 Introdução


  Nas décadas de 1940 a 1960, grandes progressos na engenharia de controle automático foram conquistados a partir da abordagem apresentada nos capítulos anteriores, baseada na descrição de sistemas dinâmicos por meio de funções de transferência, que associa diretamente as variáveis de entrada e saída do sistema. Por serem as funções de transferência intimamente relacionadas às características de resposta em frequência dos sistemas dinâmicos, diz-se que essa é uma abordagem no domínio da frequência.


  A partir da década de 1960, com a motivação principal dos sistemas aeroespaciais, novos avanços foram obtidos com o desenvolvimento da chamada teoria de variáveis de estado, na qual os sistemas dinâmicos são descritos por meio de equações diferenciais. Como estas equações diferenciais têm a variável tempo como variável independente, diz-se que essa é uma abordagem no domínio do tempo.


  A análise no espaço de estados baseia-se na utilização das chamadas variáveis de estado, as quais estão associadas à energia interna armazenada nos componentes físicos de um sistema, tais como energia cinética e magnética. Explicitar estas grandezas durante o processo de análise e projeto foi um grande avanço para se atender às especificações de desempenho mais exigentes, características dos sistemas de controle modernos. Outra característica fundamental da abordagem no espaço de estados é a possibilidade de ser aplicada igualmente para sistemas com apenas uma entrada e uma saída - SISO (Single Input Single Output), com múltiplas entradas e múltiplas saídas - MIMO (Multi Input Multi Output), não lineares e variantes no tempo.


  Historicamente, a abordagem inicial no domínio da frequência é chamada de teoria de controle clássico e a abordagem no espaço de estados é chamada de teoria de controle moderno.


  Seguindo o mesmo contexto da abordagem no domínio da frequência dos capítulos anteriores, neste capítulo a teoria de espaço de estados é aplicada a sistemas SISO, lineares e invariantes no tempo.


  

### 13.2 Modelo de sistemas dinâmicos no espaço de estados


  Nesta seção são considerados sistemas dinâmicos lineares SISO e invariantes no tempo, descritos pelo sistema (13.1) de equações diferenciais de primeira ordem,


   [img:Illustration] 


  As variáveis envolvidas no sistema de Equações (13.1) recebem as seguintes denominações:


  x1(t), x2(t),. . .,xn(t) : variáveis de estado;


  u(t) : variável de entrada;


  y(t) : variável de saída;


  t : variável independente tempo1.


  As equações do sistema (13.1) também podem ser escritas no formato matricial (13.2), cuja representação geral no espaço de estados é composta por duas equações:


   [img:Illustration] 


  No caso de sistemas SISO:


   [img:Illustration] 


  sendo x(t)n×1 o vetor de estados, x(0)n×1 = x0 o vetor com as condições iniciais, An×n a matriz do sistema, Bn×1 a matriz da entrada, C1×n a matriz da saída e D1×1 o ganho de transmissão direta da entrada para a saída.


  Na Figura 13.1 é mostrado o diagrama de blocos do sistema de Equações (13.2), em que as setas finas denotam um único sinal e as setas grossas denotam dois ou mais sinais.


   [img:Illustration] 


  Figura 13.1 Diagrama de blocos de um sistema representado por equações de estados.


  

### Exemplo 13.1


  Considere o circuito RLC paralelo com resistor, indutor e capacitor da Figura 13.2 em que a entrada do circuito é o gerador i(t) e a saída é a corrente iL(t) no indutor.


   [img:Illustration] 


  Figura 13.2 Circuito RLC paralelo.


  Pela lei de Kirchhoff das correntes tem-se que


   [img:Illustration] 


  Sabendo-se que  [img:Illustration]  obtém-se


   [img:Illustration] 


  Isolando o termo com derivada de maior ordem na Equação (13.4), tem-se que


   [img:Illustration] 


  Definindo as variáveis de estado  [img:Illustration]  obtém-se


   [img:Illustration] 


  Logo, as equações de estados na forma matricial são


   [img:Illustration] 


  ■


  

### Exemplo 13.2


  Considere o deslocamento y(t) de saída decorrente da força f(t) de entrada, aplicada no sistema mecânico com massa M, mola com constante k e atrito viscoso com constante b da Figura 13.3.


   [img:Illustration] 


  Figura 13.3 Sistema massa-mola numa superfície com atrito.


  Aplicando a segunda lei de Newton ao corpo de massa M, obtém-se a equação diferencial que representa a dinâmica do sistema, ou seja,


   [img:Illustration] 


  Isolando o termo com derivada de maior ordem na Equação (13.9), tem-se que


   [img:Illustration] 


  Definindo as variáveis de estado  [img:Illustration]  obtém-se


   [img:Illustration] 


  Logo, as equações de estados na forma matricial são


   [img:Illustration] 


  ■


  É importante observar que as definições feitas para as variáveis de estado nos exemplos (13.1) e (13.2) não são únicas. Conforme será mostrado na seção (13.10), por meio de transformações de similaridade, infinitas representações diferentes podem ser obtidas, chamadas de realizações para os modelos de variáveis de estado.


  

### 13.3 Forma canônica controlável


  Sistemas lineares descritos na forma de função de transferência podem ser representados na forma de variáveis de estado. Nesta seção é desenvolvida uma representação chamada de forma canônica controlável. A justificativa deste nome encontra-se na Seção 13.9.


  Considere um sistema linear, descrito pela equação diferencial de ordem n, entrada u(t) e saída y(t) dado por


   [img:Illustration] 


  Aplicando a transformada de Laplace em ambos os lados da Equação (13.14) e supondo condições iniciais nulas, resulta a função de transferência


   [img:Illustration] 


  Introduzindo a variável auxiliar W(s) na Equação (13.15) e definindo


   [img:Illustration] 


  e


   [img:Illustration] 


  o numerador e o denominador da função de transferência (13.15) podem ser separados conforme representado no diagrama de blocos da Figura 13.4.


   [img:Illustration] 


  Figura 13.4 Diagrama de blocos das funções de transferência (13.16) e (13.17).


  Das Equações (13.16) e (13.17) têm-se que


   [img:Illustration] 


  Aplicando a transformada inversa de Laplace nas Equações (13.18), (13.19) e isolando a derivada de maior ordem de w(t), resulta


   [img:Illustration] 


  Substituindo a Equação (13.20) na Equação (13.21), resulta


   [img:Illustration] 


  Definindo as variáveis de estado


   [img:Illustration] 


  das Equações (13.20) e (13.22) resulta o sistema de equações


   [img:Illustration] 


  As equações de estados na forma matricial


   [img:Illustration] 


  são portanto


   [img:Illustration] 


   [img:Illustration] 


  Note que a representação na forma de estados transforma a equação diferencial de ordem n (13.14), associada à função de transferência da Equação (13.15), em um sistema de n equações diferenciais de ordem 1, como no sistema (13.23).


  

### Exemplo 13.3


  Um processo com entrada u(t) e saída y(t) é representado pela função de transferência


   [img:Illustration] 


  Como o numerador da função de transferência G(s) é um polinômio em s, separa-se o numerador do denominador de G(s) em dois blocos, como na Figura 13.5.


   [img:Illustration] 


  Figura 13.5 Diagrama de blocos da função de transferência (13.27).


  Da Figura 13.5 tem-se que


   [img:Illustration] 


  Aplicando a transformada inversa de Laplace e isolando a derivada de maior ordem na Equação (13.28), resulta


   [img:Illustration] 


  Substituindo a Equação (13.30) na Equação (13.31), resulta


   [img:Illustration] 


  Definindo as variáveis de estado


   [img:Illustration] 


  resulta o sistema de equações


   [img:Illustration] 


  Portanto, as equações de estados na forma matricial são dadas por


   [img:Illustration] 


  ■


  

### 13.4 Forma canônica observável


  Nesta seção é desenvolvida uma representação na forma de variáveis de estado de um sistema linear, que recebe a denominação de forma canônica observável. A justificativa deste nome encontra-se na Seção 13.9.


  Considere um sistema linear, descrito pela equação diferencial de ordem n, entrada u(t) e saída y(t) dado por


   [img:Illustration] 


  Definindo


   [img:Illustration] 


  resulta


   [img:Illustration] 


  Integrando a Equação (13.39) com condições iniciais nulas, obtém-se


   [img:Illustration] 


  Definindo


   [img:Illustration] 


  resulta


   [img:Illustration] 


  Integrando a Equação (13.42) com condições iniciais nulas, obtém-se


   [img:Illustration] 


  Seguindo este procedimento, obtém-se


   [img:Illustration] 


  e


   [img:Illustration] 


  Integrando a Equação (13.45) com condições iniciais nulas, obtém-se


   [img:Illustration] 


  Definindo


   [img:Illustration] 


  resulta


   [img:Illustration] 


  Integrando a Equação (13.48) com condições iniciais nulas, obtém-se


   [img:Illustration] 


  e com isso resulta o sistema de equações


   [img:Illustration] 


  As equações de estados na forma matricial


   [img:Illustration] 


  são dadas por


   [img:Illustration] 


  Comparando as equações de estados (13.25) e (13.26) da forma canônica controlável com as equações de estados (13.52) e (13.53) da forma canônica observável, podem-se verificar as correspondências entre as matrizes da Tabela 13.1.


  Tabela 13.1 Correspondências entre as matrizes das formas canônicas controlável e observável


   [img:Illustration] 


  

### Exemplo 13.4


  Um processo com entrada u(t) e saída y(t) é representado pela função de transferência


   [img:Illustration] 


  Aplicando a transformada inversa de Laplace na Equação (13.54), resulta


   [img:Illustration] 


  Definindo


   [img:Illustration] 


  resulta


   [img:Illustration] 


  Integrando a Equação (13.57) com condições iniciais nulas, obtém-se


   [img:Illustration] 


  Definindo


   [img:Illustration] 


  resulta


   [img:Illustration] 


  Integrando a Equação (13.60) com condições iniciais nulas, obtém-se


   [img:Illustration] 


  Definindo


   [img:Illustration] 


  resulta


   [img:Illustration] 


  Integrando a Equação (13.63) com condições iniciais nulas, obtém-se


   [img:Illustration] 


  Substituindo a Equação (13.64) nas Equações (13.56), (13.59) e (13.62), resulta o sistema


   [img:Illustration] 


  Portanto, as equações de estados na forma matricial são dadas por


   [img:Illustration] 


  Comparando as matrizes das Equações (13.66) e (13.67) da forma canônica observável com as matrizes das Equações (13.35) e (13.36) da forma canônica controlável, podem-se verificar as correspondências da Tabela 13.1.


  ■


  

### 13.5 Conversão de estados para função de transferência


  Considere um sistema com entrada u(t) e saída y(t) descrito pelas equações de estados (13.2). Aplicando a transformada de Laplace com condições iniciais nulas, obtém-se


   [img:Illustration] 


  Isolando a transformada de Laplace do vetor de estados X(s), tem-se que


   [img:Illustration] 


  Substituindo a Equação (13.70) em (13.69), obtém-se


   [img:Illustration] 


  Portanto, a função de transferência G(s) é dada por


   [img:Illustration] 


  

### Exemplo 13.5


  Considere o circuito RLC paralelo da Figura 13.2, cujas equações de estados são


   [img:Illustration] 


  A matriz (sI – A) é dada por


   [img:Illustration] 


  cuja inversa é


   [img:Illustration] 


  Logo


   [img:Illustration] 


  Da Equação (13.72) tem-se que


   [img:Illustration] 


  Portanto, a função de transferência G(s) do circuito com entrada i(t) e saída iL(t) é


   [img:Illustration] 


  ■


  

### 13.6 Autovalores de uma matriz


  Definição 13.1 Seja a matriz A, n × n. Os autovalores da matriz A, representados pela variável s, são as raízes da equação


   [img:Illustration] 


  na qual s é uma variável complexa, det(.) e | . | denotam a função determinante e I é a matriz identidade.


  A Equação (13.80) é chamada equação característica e os autovalores são também chamados raízes características.


  

### 13.7 Estabilidade


  No Capítulo 3 o conceito de estabilidade BIBO foi estudado para sistemas lineares descritos na forma de função de transferência. Nesta seção é mostrado como as condições de estabilidade BIBO se refletem para um sistema linear descrito na forma de variáveis de estado.


  Conforme mostrado na Seção 13.5, uma realização para a função de transferência G(s) é uma representação na forma de variáveis de estado, dada pelas matrizes (A, B, C, D), tal que


   [img:Illustration] 


  Por outro lado, um sistema linear invariante no tempo é BIBO estável se e somente se todos os polos de sua função de transferência estão localizados no semiplano esquerdo aberto do plano s, excluído o eixo imaginário.


  Sendo cof(sI – A) a matriz dos cofatores da matriz (sI – A), a função de transferência G(s) pode ser escrita como


   [img:Illustration] 


  Logo, os polos da função de transferência da Equação (13.82) são as raízes da equação característica da matriz A, ou seja, os autovalores calculados por meio da Equação (13.80).


  
    Portanto, um sistema linear invariante no tempo, dado pelas matrizes (A, B, C, D), é BIBO estável se e somente se todos os autovalores da matriz A estão localizados no semiplano esquerdo aberto do plano s, excluído o eixo imaginário.

  


  

### Exemplo 13.6


  Seja a matriz


   [img:Illustration] 


  Os autovalores da matriz A são as raízes da equação


   [img:Illustration] 


  ou seja,


   [img:Illustration] 


  Logo, os autovalores da matriz A são s = –1 e s = –2.


  Portanto, o sistema é BIBO estável, pois todos os autovalores da matriz A (s = –1 e s = –2) estão localizados no semiplano esquerdo aberto do plano s, excluído o eixo imaginário.


  ■


  

### Exemplo 13.7


  Seja a matriz


   [img:Illustration] 


  Os autovalores da matriz A são as raízes da equação


   [img:Illustration] 


  ou seja,


   [img:Illustration] 


  Logo, os autovalores da matriz A são s = 0, s = –1 e s = –2.


  Portanto, o sistema não é BIBO estável, pois um dos autovalores da matriz A (s = 0) está localizado sobre o eixo imaginário do plano s.


  ■


  

### 13.8 Posto de uma matriz


  Definição 13.2 Seja a matriz A, n × m, e sejam p ≤ n o número máximo de linhas linearmente independentes e q ≤ m o número máximo de colunas linearmente independentes. Nessas condições, diz-se que o posto da matriz A é dado por


   [img:Illustration] 


  Obviamente, se n = m então o máximo posto da matriz A é n = m.


  Se n > m, então o máximo posto de A é m e, se n < m, o máximo posto de A é n.


  A partir da definição, para determinar o posto de uma matriz basta encontrar uma submatriz quadrada de maior ordem possível, cujo determinante é diferente de zero.


  

### Exemplo 13.8


  Seja a matriz quadrada, com dimensão n = m = 2,


   [img:Illustration] 


  Como det(A) = 1 · 4 – 2 · 2 = 0, pode-se afirmar que as duas linhas e as duas colunas da matriz A não são linearmente independentes. Logo, posto(A) < 2.


  Como cada um dos elementos da matriz A constitui uma submatriz de ordem 1 e pelo menos um deles não é nulo, existe uma submatriz de ordem p = q = 1, com determinante diferente de zero. Portanto, posto(A) = 1. Isto somente não ocorreria se todos os elementos da matriz A fossem nulos, caso em que o posto(A) seria igual a zero.


  ■


  

### Exemplo 13.9


  Seja a matriz retangular


   [img:Illustration] 


  Como a matriz A possui n = 2 linhas e m = 3 colunas, n < m e o posto da matriz A pode valer no máximo n = 2. Para que isso ocorra, é necessário que A possua uma submatriz de ordem 2 × 2, com determinante diferente de zero.


  A submatriz A1 formada pelas 2 primeiras colunas é


   [img:Illustration] 


  cujo determinante é igual a zero.


  Por outro lado, as duas submatrizes


   [img:Illustration] 


  possuem determinantes não nulos e, assim, resulta posto(A) = 2.


  ■


  

### 13.9 Controlabilidade e observabilidade


  A propriedade de um sistema dinâmico ser controlável, denominada de controlabilidade, está associada à existência de um sinal de controle capaz de conduzir o vetor de estados de um ponto inicial qualquer x(t0) para um ponto final qualquer x(tf), em um intervalo de tempo arbitrário tf – t0 > 0.


  A propriedade de um sistema dinâmico ser observável, denominada de observabilidade, está associada à possibilidade de se determinar a trajetória de todo o vetor de estados x(t) em um intervalo de tempo arbitrário tf – t0 > 0, a partir do conhecimento da função de saída y(t) do sistema nesse intervalo.


  As duas condições apresentadas a seguir permitem verificar se um sistema dinâmico dado pelas matrizes (A, B, C, D) é controlável ou é observável2.


  

#### 13.9.1 Condição de controlabilidade


  O sistema dinâmico SISO de ordem n, dado pelas Equações (13.2), é controlável se e somente se a matriz


   [img:Illustration] 


  tem posto pleno, ou seja, posto(M) = n.


  Para que a matriz M tenha posto pleno deve-se ter det(M) ≠ 0.


  

#### 13.9.2 Condição de observabilidade


  O sistema dinâmico SISO de ordem n, dado pelas Equações (13.2), é observável se e somente se a matriz


   [img:Illustration] 


  tem posto pleno, ou seja, posto(N) = n.


  Para que a matriz N tenha posto pleno deve-se ter det(N) ≠ 0.


  

### Exemplo 13.10


  As equações de estados de um sistema são dadas por


   [img:Illustration] 


  Como o sistema possui n = 2 estados, a matriz M2×2 de controlabilidade é dada por


   [img:Illustration] 


  Como det(M) ≠ 0, a matriz M tem posto pleno n = 2. Logo, o sistema é controlável.


  Como o sistema possui n = 2 estados, a matriz N2×2 de observabilidade é dada por


   [img:Illustration] 


  Como det(N) = 0, a matriz N não tem posto pleno. Logo, o sistema não é observável.


  ■


  

### 13.10 Transformação de similaridade


  As transformações de similaridade são de grande utilidade no estudo de sistemas dinâmicos descritos por variáveis de estado, tanto para fins de análise quanto de projeto de compensadores.


  Se os estados reais medidos no processo não forem exatamente os estados do modelo, então o controlador será projetado para um modelo com estados fictícios, diferentes dos estados reais. Após o projeto deve-se, então, usar uma transformação de similaridade que leve o controlador para a base dos estados reais.


  Considere um sistema dinâmico descrito por n variáveis de estado


   [img:Illustration] 


  Então, dada uma matriz Pn×n, não singular, pode-se escrever


   [img:Illustration] 


  Definindo  [img:Illustration]  Logo, as equações do sistema (13.100) resultam como


   [img:Illustration] 


  Definição 13.3 Sejam as matrizes An×n, An×n e a matriz Pn×n, não singular, tal que


   [img:Illustration] 


  Nessas condições, as matrizes A e A são similares e P é uma transformação de similaridade.


  Definindo ainda B = PB, C = CP–1 e D = D, do sistema (13.102), obtém-se


   [img:Illustration] 


  A transformação de similaridade não altera os autovalores das matrizes A e A, ou seja,


   [img:Illustration] 


  As funções de transferência dos sistemas (13.100) e (13.104) também não se alteram com a transformação de similaridade, ou seja,


   [img:Illustration] 


  

#### 13.10.1 Transformação para a forma canônica controlável


  Essa transformação permite representar um sistema na forma canônica controlável, a partir de uma realização qualquer com estados controláveis.


  Considere um sistema dinâmico controlável qualquer descrito pela realização de estados


   [img:Illustration] 


  cuja matriz M de controlabilidade é dada por


   [img:Illustration] 


  A função de transferência associada ao sistema dinâmico da Equação (13.107) é dada por


   [img:Illustration] 


  Considere agora o sistema (13.107) escrito na forma canônica controlável


   [img:Illustration] 


  sendo


   [img:Illustration] 


  A matriz M de controlabilidade do sistema (13.110) é


   [img:Illustration] 


  Obviamente, como o sistema (13.107) é assumido controlável, a matriz de transformação de similaridade P e as matrizes de controlabilidade M e M resultam não singulares.


  Da Equação (13.111) resulta


   [img:Illustration] 


  com


   [img:Illustration] 


   [img:Illustration] 


   [img:Illustration] 


  

### Exemplo 13.11


  Considere o sistema dinâmico representado pelas equações de estados


   [img:Illustration] 


  A função de transferência associada a esse sistema é dada por


   [img:Illustration] 


  A matriz (sI – A) é dada por


   [img:Illustration] 


  cuja inversa é


   [img:Illustration] 


  Logo


   [img:Illustration] 


  Comparando os coeficientes de G(s) com a Equação (13.109), obtém-se para n = 2 o coeficiente a1 = 0.


  Das Equações (13.108), (13.112) e (13.114) obtêm-se


   [img:Illustration] 


  ou


   [img:Illustration] 


  Sabendo-se que A = P AP–1, B = PB e C = CP–1, as equações de estados na forma canônica controlável são dadas por


   [img:Illustration] 


  ■


  

### 13.11 Controle por realimentação de estados contínuos


  O projeto de compensadores a partir do modelo de variáveis de estado pode ser tratado por diversas técnicas. Nesta seção, este problema é abordado pela técnica de alocação ou imposição de polos para o sistema em malha fechada. Com esta técnica, o compensador é projetado de forma que o sistema em malha fechada possua os polos especificados pelo projetista.


  A escolha da posição dos polos de malha fechada pode ser realizada com base em especificações da resposta transitória temporal da saída do sistema, como por exemplo, sobressinal máximo e tempo de resposta.


  A abordagem de alocação de polos considera que todos os estados do sistema controlado são disponíveis para realimentação, ou seja, existem sensores que medem cada uma das variáveis de estado. De fato, esta não é uma situação que ocorre em todas as aplicações da engenharia de controle. Conforme é mostrado na Seção 13.13, sob certas condições, o problema de os estados não serem todos disponíveis pode ser contornado utilizando-se o chamado observador ou estimador de estados.


  Um ponto a ser destacado é que a alocação arbitrária de todos os polos do sistema só será possível se o sistema for controlável. Nos casos em que isto não ocorre, para garantir que o sistema em malha fechada seja estável é necessário que os polos do sistema controlado, associados às variáveis de estado não controláveis, estejam situados no semiplano esquerdo aberto do plano s, ou seja, possuam parte real negativa.


  Considerando a realimentação de estados, o diagrama de blocos correspondente para o controlador por realimentação de estados é mostrado na Figura 13.6, em que as setas finas indicam sinais escalares e as setas grossas indicam sinais vetoriais.


   [img:Illustration] 


  Figura 13.6 Controle por realimentação de estados.


  Na Figura 13.6 o ganho D de transmissão direta da entrada para a saída é suposto nulo por simplicidade e o sistema controlado com uma entrada e uma saída é dado por


   [img:Illustration] 


  com função de transferência G(s) = C(sI – A)–1B.


  A realimentação de estados é chamada de realimentação estática, uma vez que o vetor


   [img:Illustration] 


  que produz a realimentação de estados é um vetor de ganhos com constantes k1, k2, k3, . . . , kn.


  O sinal de controle u(t) é dado por


   [img:Illustration] 


  sendo r(t) o sinal de referência.


  Das Equações (13.125) e (13.127) têm-se que ẋ (t) = Ax(t) + Bu(t) = Ax(t) + B[r(t) – Kx(t)].


  Logo, o sistema em malha fechada resulta como


   [img:Illustration] 


  cujos polos de malha fechada são os autovalores da matriz A – BK, que são as raízes da equação característica


   [img:Illustration] 


  

### Exemplo 13.12


  Considere o sistema dinâmico representado pelas equações de estados


   [img:Illustration] 


  Os polos do sistema em malha aberta são os autovalores de


   [img:Illustration] 


  ou seja, s = –1 e s = 1. Portanto, o sistema em malha aberta é instável.


  Supondo um vetor de realimentação de estados


   [img:Illustration] 


  os polos do sistema em malha fechada são as raízes de


   [img:Illustration] 


  ou seja, s = –0,5 e s = –2. Nota-se, assim, que a realimentação de estados estabilizou o sistema em malha fechada.


  ■


  

#### 13.11.1 Alocação de polos de malha fechada


  Nesta seção é mostrado como projetar o vetor de realimentação estática K dos estados, tal que os polos de malha fechada resultem em posições especificadas, que podem ser baseadas em parâmetros da resposta transitória temporal da saída, como por exemplo, sobressinal máximo e tempo de resposta.


  Supõe-se ainda que o sistema em malha aberta é controlável. Do ponto de vista das aplicações, deve-se destacar que, se um sistema não é controlável, é necessário que os estados não controláveis estejam associados a polos estáveis. Caso contrário, pode-se dizer que o sistema não tem utilidade prática, já que será sempre instável em malha fechada.


  Considere a função de transferência (13.109) representada pelas equações de estados


   [img:Illustration] 


  Se o par [A, B] é controlável, então o sistema (13.135) pode ser escrito na forma canônica controlável por meio da transformação de similaridade P e das relações x(t) = Px(t), A = P AP–1, B = PB, C = CP–1 e D = D, ou seja,


   [img:Illustration] 


  sendo


   [img:Illustration] 


  Para o sistema na forma canônica controlável (13.136), a realimentação de estados é dada por


   [img:Illustration] 


  Sabendo-se que os estados originais x(t) e os estados na forma canônica x(t) estão relacionados por x(t) = Px(t), então


   [img:Illustration] 


  Logo, para o sistema original (13.135) o vetor de realimentação de estados vale


   [img:Illustration] 


  com


   [img:Illustration] 


  A matriz da forma canônica de malha fechada com o controlador K é


   [img:Illustration] 


  Os polos de malha fechada são as raízes da equação característica


   [img:Illustration] 


  Se os polos de malha fechada desejados forem especificados como p1, p2, . . ., pn, então


   [img:Illustration] 


  Comparando os coeficientes dos polinômios (13.142) e (13.143), tem-se o sistema de n equações


   [img:Illustration] 


  Do sistema (13.144) obtém-se o controlador K = [k1 ... kn–1 kn] para realimentação dos estados x(t) da forma canônica (13.136). Uma consequência da representação do sistema na forma canônica é que os ganhos do controlador são determinados facilmente, pois são calculados de forma isolada.


  Já os ganhos do controlador K para realimentação dos estados originais x(t) do sistema (13.135) são obtidos da Equação (13.139).


  

### Exemplo 13.13


  Considere o sistema dinâmico do Exemplo 13.11, representado pelas equações de estados


   [img:Illustration] 


  Para escrever o sistema de Equações (13.145) e (13.146) na forma canônica controlável é necessário determinar a matriz de transformação de similaridade P, que é a matriz inversa da Equação (13.112), ou seja,


   [img:Illustration] 


  Sabendo-se que A = P AP–1, B = PB e C = CP–1, as equações de estados na forma canônica controlável são dadas por


   [img:Illustration] 


  A matriz da forma canônica de malha fechada com o controlador K é


   [img:Illustration] 


  Os polos de malha fechada são as raízes da equação característica


   [img:Illustration] 


  Especificando os polos de malha fechada em s = –0,5 e s = –2, como no Exemplo 13.12, obtém-se o polinômio característico


   [img:Illustration] 


  Comparando os coeficientes dos polinômios (13.151) e (13.152), obtém-se os ganhos do controlador K para o sistema na forma canônica controlável, ou seja,


   [img:Illustration] 


  Para o sistema original de Equações (13.145) e (13.146), o controlador K vale


   [img:Illustration] 


  que corresponde aos mesmos ganhos adotados para o controlador no Exemplo 13.12.


  ■


  

### 13.12 Regulador Linear Quadrático - RLQ


  Nesta seção é apresentado um sistema de controle, denominado de Regulador Linear Quadrático - RLQ, projetado a partir da realimentação de estados do sistema a ser controlado. Seu projeto decorre da teoria de controle ótimo, que por sua vez resulta da minimização de um índice de desempenho.


  Um grande diferencial em relação à teoria de projeto por alocação de polos de malha fechada é que o Regulador Linear Quadrático produz sistemas de controle robustos estáveis, podendo a margem de ganho variar na faixa de meio a infinito e a margem de fase variar na faixa de –60° a +60° (ver [35]).


  Outra característica importante do Regulador Linear Quadrático é que no seu procedimento de projeto são utilizados, de forma explícita, parâmetros que permitem limitar amplitudes "excessivas" durante transitórios, tanto para as variáveis de estado quanto para a variável de controle.


  

#### 13.12.1 Formulação do problema


  Considere um sistema dinâmico com entrada u(t), estados x(t) e condição inicial não nula x(0), representado por


   [img:Illustration] 


  com An×n, Bn×1 e x(t)n×1.


  Supondo que as variáveis de estado são todas disponíveis, o sinal de controle u(t) é dado por


   [img:Illustration] 


  sendo K = [k1 k2 ... kn] um vetor de ganhos constantes.


  O sistema em malha fechada pode ser representado pelo diagrama de blocos da Figura 13.7.


   [img:Illustration] 


  Figura 13.7 Sistema com controlador por realimentação de estados.


  Das Equações (13.155) e (13.156) resulta o sistema com realimentação de estados


   [img:Illustration] 


  cujos polos do sistema em malha fechada são dados pelos autovalores da matriz A – BK.


  Diferentemente do problema estudado na Seção 13.11 de alocação de polos de malha fechada, no regulador linear quadrático o sinal de referência r(t) é assumido como sendo igual a zero. Nesta condição, se todos os polos de malha fechada tiverem parte real negativa, então para qualquer condição inicial x(0), a entrada de controle u(t) leva o vetor de estados x(t) para zero quando t tende a infinito.


  Para o projeto do regulador linear quadrático, o vetor de ganhos K é calculado de forma a minimizar um índice de desempenho quadrático J dado por


   [img:Illustration] 


  sendo Q uma matriz simétrica semidefinida positiva3 e R uma constante escalar positiva, ambas escolhidas como parâmetros de projeto.


  No índice de desempenho J da Equação (13.158), os termos xT (t)Qx(t) e Ru2(t) estão relacionados com a energia das variáveis de estado e do sinal de controle, respectivamente. Dessa forma, a escolha apropriada de Q e R permite uma ponderação das energias desses dois sinais durante o transitório das variáveis de estado desde o valor inicial até zero. Como exemplo, supondo a matriz Q diagonal, quanto maiores forem os valores escolhidos para os seus elementos, relativamente ao valor de R, menor será a energia dos estados e maior será a energia dispendida pelo controle.


  Se a matriz Qn×n é semidefinida positiva, então ela pode ser fatorada como Q = CTqCq, sendo Cq uma matriz m × n, com 0 < m < n (ver [14]).


  Considere as seguintes hipóteses:


  i) todos os estados do vetor x(t) são disponíveis para realimentação;


  ii) o par (A, B) é estabilizável4 e o par (A, Cq) é detectável5;


  iii) R > 0.


  Nessas condições, o vetor K que minimiza o índice de desempenho J é dado por


   [img:Illustration] 


  sendo F a única matriz simétrica semidefinida positiva, solução da equação


   [img:Illustration] 


  chamada de equação algébrica de Riccati. Além disso, o sistema com realimentação da Equação (13.157) é sempre assintoticamente estável, ou seja, todos os autovalores da matriz de malha fechada A – BK estão no semiplano esquerdo aberto do plano s.


  A Equação (13.160) pode ter mais de uma matriz F como solução, mas somente uma é simétrica semidefinida positiva. A demonstração das Equações (13.159) e (13.160) pode ser encontrada na referência [33].


  

#### 13.12.2 Procedimento de projeto para o Regulador Linear Quadrático


  i) Adotar valores para a matriz Q e para o escalar R.


  ii) Resolver a equação algébrica de Riccati (13.160), determinando a matriz F.


  iii) Calcular o vetor de realimentação de estados K pela Equação (13.159).


  iv) Simular o sistema em malha fechada e avaliar as amplitudes máximas e demais características de transitório.


  v) Se as especificações de projeto não forem satisfeitas, voltar para i) e refazer o projeto.


  

### Exemplo 13.14


  Considere o mesmo sistema dinâmico dos Exemplos 13.12 e 13.13, representado pelas equações de estados


   [img:Illustration] 


  Conforme verificado no Exemplo 13.12, o sistema em malha aberta é instável. Para o projeto do regulador linear quadrático, inicialmente deve-se adotar valores para a matriz Q e para o escalar R. Como há infinitos valores que podem ser adotados para Q e R, se ao final do cálculo do vetor K o controlador não atender às especificações, então o projeto deve ser refeito.


  Após algumas tentativas são adotados R = 1 e


   [img:Illustration] 


  Como o sistema tem n = 2 estados, então a matriz simétrica F = FT, solução da equação algébrica de Riccati, tem dimensão 2 × 2, ou seja,


   [img:Illustration] 


  Da equação algébrica de Riccati6 (13.160) tem-se que


   [img:Illustration] 


  Simplificando a Equação (13.165), obtém-se o sistema de equações


   [img:Illustration] 


  Da Equação (13.168) tem-se que


   [img:Illustration] 


  Substituindo a Equação (13.169) na Equação (13.167), obtém-se


   [img:Illustration] 


  Substituindo a Equação (13.170) na Equação (13.166), obtém-se


   [img:Illustration] 


  cujas raízes são f2 = –0,2361 e f2 = 4,2361.


  Para f2 = 4,2361 obtém-se


   [img:Illustration] 


  cujos autovalores são –0,0942 e –10,6141. Como estes autovalores são negativos, a matriz F não é semidefinida positiva. Logo, esta solução deve ser descartada.


  Para f2 = –0,2361 obtém-se


   [img:Illustration] 


  cujos autovalores são 0,4411 e 2,2671. Como estes autovalores são positivos, a matriz F é definida positiva. Logo, esta solução deve ser utilizada no cálculo do vetor K.


  Portanto, da Equação (13.159) obtém-se o vetor K para realimentação dos estados


   [img:Illustration] 


  Supondo que a entrada de referência r(t) é zero, então as equações de estados do sistema em malha fechada resultam como


   [img:Illustration] 


  Aplicando a transformada de Laplace na Equação (13.175), tem-se que


   [img:Illustration] 


  Logo, a transformada de Laplace da saída Y (s) é


   [img:Illustration] 


  Supondo condição inicial


   [img:Illustration] 


  então


   [img:Illustration] 


  Aplicando a transformada inversa de Laplace na Equação (13.183), obtém-se a resposta transitória da saída y(t) para a condição inicial (13.182), dada por


   [img:Illustration] 


  O gráfico da resposta transitória (13.184) é apresentado na Figura 13.8. Observe que o controlador estabilizou o sistema em malha fechada. Porém, se a resposta transitória não satisfizer às especificações de projeto, como por exemplo o tempo de resposta e a amplitude máxima do sinal de controle, o cálculo do controlador K deve ser refeito, escolhendo-se outros valores para Q e R.


   [img:Illustration] 


  Figura 13.8 Resposta transitória da saída y(t) para a condição inicial (13.182).


  ■


  

### 13.13 Observador ou estimador de estados contínuos


  Em ambos os métodos de projeto vistos anteriormente, de alocação de polos de malha fechada e do regulador linear quadrático, foi suposto que os estados da planta eram disponíveis para realimentação. Porém, esta situação não ocorre com frequência na prática. Como exemplo, no caso da realimentação auxiliar de velocidade do servomecanismo estudado na Seção 4.6.4, as duas variáveis de estado realimentadas são a posição e a velocidade. Para que ambas sejam disponíveis para realimentação, é necessária a utilização de um potenciômetro para a medida da posição angular e um tacômetro para a medida da velocidade. No entanto, por razões econômicas ou tecnológicas, em diversas aplicações nem sempre estes sensores podem ser instalados. Nesses casos, na hipótese de o sistema ser observável, é possível projetar um estimador ou observador de estados usando apenas os sinais de entrada e saída da planta. Obviamente, estes sinais estão sempre disponíveis, pois o sinal de entrada da planta nada mais é do que a saída do controlador e o sinal de saída da planta é sempre medido.


  Os termos observador ou estimador de estados são comumente empregados na literatura. Neste texto será utilizado o termo observador de estados.


  

#### 13.13.1 Formulação do problema


  Considere um sistema dinâmico observável com entrada u(t), saída y(t) e condição inicial não nula x(0), representado por


   [img:Illustration] 


  sendo An×n, Bn×1, C1×n e x(t)n×1.


  O projeto de um observador de estados visa obter uma estimativa  [img:Illustration] (t) para o vetor de variáveis de estado  [img:Illustration] (t), tal que o erro de observação  [img:Illustration] (t) satisfaça


   [img:Illustration] 


  

#### 13.13.2 Estrutura do observador de estados


  A estrutura do observador de estados baseia-se no modelo de variáveis de estado da planta. Na prática, sempre existem erros de modelagem e, portanto, após o projeto do observador, seu desempenho deve ser avaliado por meio de simulações que consideram esses erros. Na Figura 13.9 é apresentado o diagrama de blocos contendo a planta e o observador de estados.


   [img:Illustration] 


  Figura 13.9 Diagrama de blocos contendo planta e observador de estados.


  Da Figura 13.9 tem-se que o bloco correspondente ao observador é dado por


   [img:Illustration] 


  com condição inicial  [img:Illustration] (0).


  Pode-se notar que o sistema (13.187) tem a mesma estrutura do sistema (13.185), porém, com o termo adicional L[ y(t) –  [img:Illustration] (t) ]. Na condição ideal em que as matrizes e as condições iniciais da planta e do observador são idênticas, esse termo adicional não precisaria ser incluído. De fato, neste caso o observador seria idêntico à planta e teria a estrutura do chamado observador de malha aberta, com  [img:Illustration]  para todo t ≥ 0.


  Suponha agora, que as condições iniciais x(0) e  [img:Illustration] (0) = 0 são diferentes. Subtraindo a derivada dos estados  [img:Illustration] (t) da derivada dos estados estimados  [img:Illustration] (t), obtém-se


   [img:Illustration] 


  Substituindo y(t) e  [img:Illustration] (t) na Equação (13.188), resulta


   [img:Illustration] 


  Supondo que os erros entre as matrizes da planta (A,B,C) e do modelo  [img:Illustration]  são suficientemente pequenos, da Equação (13.189) tem-se que


   [img:Illustration] 


  Portanto, a dinâmica do sinal de erro de observação  [img:Illustration] (t) fica determinada, aproximadamente, pela matriz A — LC. Assim, o procedimento de projeto do observador de estados consiste, essencialmente, em obter um vetor de ganhos L tal que a matriz A — LC seja estável, o que resultará em  [img:Illustration] (t) → 0 quando t → ∞.


  Um procedimento bastante comum para a determinação do vetor L considera a similaridade com o problema do regulador linear quadrático. Conforme mostrado na Seção 13.12, sendo o par (A, B) estabilizável, obtém-se a partir da equação algébrica de Riccati um vetor K tal que a matriz de malha fechada A – BK minimiza o índice de desempenho J da Equação (13.158). Além disso, o método garante a estabilidade do sistema em malha fechada.


  Para o projeto do vetor L do observador de estados, nota-se que as matrizes A – BK e AT – CT LT têm exatamente a mesma estrutura. Com isso pode-se estabelecer analogias entre as matrizes do regulador e do observador de estados que estão apresentadas na Tabela 13.2.


  Tabela 13.2 Analogias entre regulador linear quadrático e observador de estados.


   [img:Illustration] 


  Sabendo-se que os autovalores da matriz A – LC são os mesmos da matriz AT – CT LT e que o par (A,C) detectável corresponde ao par (AT , CT) estabilizável, o procedimento para cálculo do vetor de ganhos L pode ser o mesmo que foi utilizado no projeto do regulador linear quadrático, isto é, por meio de uma equação algébrica de Riccati.


  Utilizando as analogias da Tabela 13.2 na Equação (13.159), tem-se que


   [img:Illustration] 


  sendo que F é uma matriz simétrica semidefinida positiva, que é solução da equação algébrica de Riccati


   [img:Illustration] 


  Conforme mencionado no projeto do regulador, a Equação (13.192) pode ter mais de uma matriz F como solução, mas somente uma é simétrica semidefinida positiva.


  Da mesma forma que no projeto do regulador linear quadrático, o observador de estados deve ter o seu desempenho avaliado por meio de simulações. Os autovalores da matriz de malha fechada A – LC também devem ser avaliados. Na prática, é recomendável escolher matrizes Q e R, que resultem numa matriz A – LC com autovalores mais rápidos, localizados mais à esquerda no plano s, que os autovalores da matriz A – BK do projeto do regulador linear quadrático.


  

#### 13.13.3 Procedimento de projeto do observador de estados


  i) Adotar valores para a matriz Q e para o escalar R.


  ii) Resolver a equação algébrica de Riccati (13.192), determinando a matriz F.


  iii) Calcular o vetor de ganhos L pela Equação (13.191).


  iv) Simular o sistema em malha fechada e avaliar a resposta transitória.


  v) Se as especificações de projeto não forem satisfeitas, voltar para i) e refazer o projeto.


  

### Exemplo 13.15


  Considere o mesmo sistema dinâmico dos Exemplos 13.12, 13.13 e 13.14. Para o projeto do observador, inicialmente deve-se adotar valores para a matriz Q e para o escalar R. Como há infinitos valores que podem ser adotados para Q e R, se ao final do projeto as especificações não forem satisfeitas, então os cálculos devem ser refeitos. Após algumas tentativas são adotados R = 0,1 e


   [img:Illustration] 


  Como o sistema tem n = 2 estados, então a matriz simétrica F = FT, solução da equação algébrica de Riccati, tem dimensão 2 × 2, ou seja,


   [img:Illustration] 


  Da equação algébrica de Riccati (13.192) tem-se que


   [img:Illustration] 


  Simplificando a Equação (13.195), obtém-se o sistema de equações


   [img:Illustration] 


  Substituindo a Equação (13.198) na Equação (13.197), com f2 ≠ 0, obtém-se


   [img:Illustration] 


  Da Equação (13.196) tem-se que


   [img:Illustration] 


  cujas raízes são f1 = –0,8 e f1 = 1.


  Para f1 = –0,8 obtém-se


   [img:Illustration] 


  cujos autovalores são –0,9857 e 12,9857. Como um dos autovalores é negativo, a matriz F não é semidefinida positiva. Logo, esta solução deve ser descartada.


  Para f1 = 1 obtém-se


   [img:Illustration] 


  cujos autovalores são 0,7918 e 20,2082. Como estes autovalores são positivos, a matriz F é definida positiva. Logo, esta solução deve ser utilizada no cálculo do vetor L. Da Equação (13.191) tem-se


   [img:Illustration] 


  A matriz de malha fechada é


   [img:Illustration] 


  cujos autovalores são –1 e –9, que são mais rápidos que os autovalores da matriz A – BK (–0,618 e –1,618).


  ■


  

#### 13.13.4 Conexão entre controlador e observador de estados


  Conforme já comentado na seção anterior, em muitas situações os estados da planta podem não estar todos disponíveis para realimentação. Este fato pode ocorrer tanto por razões tecnológicas, devido à dificuldade de certos estados serem medidos, quanto por razões econômicas, em que o custo de sensores pode ser muito elevado.


  Porém, na hipótese de o sistema ser observável, é possível obter estimativas dos estados e utilizar estas estimativas no lugar dos estados medidos. Esta é a ideia da conexão de um controlador por realimentação de estados com observador. Na Figura 13.10 é apresentado o diagrama de blocos do sistema em malha fechada completo.


   [img:Illustration] 


  Figura 13.10 Malha fechada com controlador por realimentação de estados e observador.


  Na configuração da Figura 13.10, o controlador pode ser obtido tanto pelo método de alocação de polos de malha fechada, quanto pelo método do regulador linear quadrático. É importante destacar que, no caso do regulador linear quadrático, quando se utiliza o observador no lugar da medida dos estados, as propriedades de margem de ganho infinita e margem de fase de pelo menos 60° não são mais garantidas, o que ocasiona uma perda de robustez da malha fechada. Como regra geral, qualquer que seja o método de projeto do controlador, é sempre necessário que seja feita, por meio de simulações, uma avaliação da robustez do sistema em malha fechada, relativamente a erros de modelagem.


  O sistema completo em malha fechada com controlador por realimentação de estados e observador pode ser equacionado a partir da Figura 13.10.


  • Planta ou sistema controlado com condição inicial x(0):


   [img:Illustration] 


  • Observador de estados com condição inicial  [img:Illustration] (0):


   [img:Illustration] 


  • Controlador por realimentação de estados:


   [img:Illustration] 


  • Erro do estimador de estados:


   [img:Illustration] 


  • Sinal de entrada da planta:


   [img:Illustration] 


  Da equação de estados da planta tem-se que


   [img:Illustration] 


  Da Equação (13.190) tem-se que


   [img:Illustration] 


  Das Equações (13.210) e (13.211) resultam as equações dinâmicas do sistema em malha fechada com realimentação de estados observados da Figura 13.10, ou seja,


   [img:Illustration] 


  Como Amf é uma matriz triangular, os seus autovalores são os autovalores da matriz A – BK, decorrentes do projeto de alocação de polos ou do regulador linear quadrático, mais os autovalores da matriz A – LC, decorrentes do projeto do observador de estados, ou seja,


   [img:Illustration] 


  

#### 13.13.5 Função de transferência do bloco controlador+observador


  Supondo que os erros entre as matrizes (A, B, C) e  [img:Illustration]  são suficientemente pequenos, das equações do observador tem-se que


   [img:Illustration] 


  Da Equação (13.209) tem-se que


   [img:Illustration] 


  cuja transformada de Laplace, considerando condições iniciais nulas é


   [img:Illustration] 


  Substituindo a Equação (13.217) na transformada de Laplace na Equação (13.209), obtém-se


   [img:Illustration] 


  Na Equação (13.218) fica evidente que o conjunto controlador+observador produz o sinal de controle U (s) a partir do sinal de saída da planta Y (s). Rearranjando os blocos da Figura 13.10, de forma a explicitar a realimentação da saída, resulta o diagrama de blocos de malha fechada da Figura 13.11, que é muito útil na análise e no projeto de sistemas de controle que visam a regulação do sinal de saída da planta.


   [img:Illustration] 


  Figura 13.11 Diagrama de blocos de malha fechada com controlador e observador de estados.


  Da Figura 13.11, a transformada de Laplace do sinal de erro, para R(s) = 0, é


   [img:Illustration] 


  Das Equações (13.218) e (13.219) resulta a função de transferência do conjunto controlador + observador


   [img:Illustration] 


  Deve-se notar que no caso em que a planta possui uma entrada e uma saída, os sinais r(t), e(t), u(t) e y(t) são escalares e a função de transferência do conjunto controlador+observador também é escalar.


  

### Exemplo 13.16


  Considerando os vetores K e L, calculados nos Exemplos 13.14 e 13.15, tem-se que


   [img:Illustration] 


  cuja matriz inversa é


   [img:Illustration] 


  Logo, a função de transferência do controlador+observador é


   [img:Illustration] 


  Considerando a planta com a função de transferência (13.120) do Exemplo 13.11, tem-se que


   [img:Illustration] 


  Logo, a função de transferência de malha aberta é


   [img:Illustration] 


  Portanto, a função de transferência de malha fechada resulta como


   [img:Illustration] 


  Supondo que a entrada de referência seja um degrau unitário (R(s) = 1/s), então


   [img:Illustration] 


  Aplicando a transformada inversa de Laplace na Equação (13.229), obtém-se a resposta transitória da saída y(t), dada por


   [img:Illustration] 


  O gráfico da resposta transitória (13.230) é apresentado na Figura 13.12. Observe que o sistema de controle com observador estabilizou o sistema em malha fechada. Porém, se a resposta transitória não satisfizer às especificações de projeto, como por exemplo, tempo de resposta, sobressinal ou erro estacionário, o cálculo dos vetores K e L deve ser refeito.


   [img:Illustration] 


  Figura 13.12 Resposta transitória da saída y(t) para um degrau unitário aplicado na referência.


  ■


  

### 13.14 Inclusão de integrador contínuo na malha de controle


  Embora o regulador linear quadrático seja projetado para levar o sistema controlado de um estado inicial qualquer para zero, são comuns aplicações em que, após o cálculo e implementação do vetor de realimentação de estados K e do observador de estados, o sistema em malha fechada seja submetido a sinais de referência diferentes de zero. Além disso, sendo o sistema em malha fechada estável, frequentemente faz-se a exigência de erro de regime nulo quando o sinal de referência r(t) é um degrau, mesmo na presença de perturbações d(t) na entrada da planta, conforme é representado na Figura 13.13.


   [img:Illustration] 


  Figura 13.13 Diagrama de blocos do sistema em malha fechada com entrada de referência r(t) e de perturbação d(t).


  O objetivo é atender à especificação de erro de regime permanente nulo, considerando-se sinais do tipo degrau em r(t) e em d(t). Nesta condição, a saída y(t) deve acompanhar o sinal de referência r(t) mesmo na presença de um degrau de perturbação d(t). No contexto da teoria de controle clássico, a solução mais comum consiste em incluir um integrador no bloco de controle, tornando o sistema7 do tipo 1. O emprego do controlador PID é uma solução típica para este problema, já que o mesmo possui o elemento integrador em sua estrutura.


  No entanto, no caso do controlador por realimentação de estados+observador das seções anteriores não foi utilizado nenhum mecanismo que garantisse a presença de um integrador (polo na origem) em sua estrutura. O procedimento, que soluciona este problema, consiste em acrescentar um bloco integrador na entrada da planta, como na Figura 13.14.


   [img:Illustration] 


  Figura 13.14 Diagrama de blocos mostrando a inclusão do integrador na entrada da planta.


  De acordo com a Figura 13.14, o bloco do controlador+observador deve ser projetado pelos mesmos procedimentos das seções anteriores, porém assumindo-se o conjunto planta+integrador como modelo para o sistema controlado, o qual é denominado planta estendida. Após o projeto, o integrador deve ser implementado juntamente com o bloco do controlador+observador. O modelo para a chamada planta estendida é obtido a partir do modelo da planta juntamente com o modelo de variável de estado para o integrador. Da Figura 13.14 tem-se que


   [img:Illustration] 


  Aplicando a transformada inversa de Laplace na Equação (13.231), tem-se que


   [img:Illustration] 


  Definindo a variável de estado xi(t) = u(t), resulta a equação de estado do integrador


   [img:Illustration] 


  A Equação (13.233) em conjunto com o modelo da planta (13.2) produz o modelo de variáveis de estado para a planta estendida, dado por


   [img:Illustration] 


  As matrizes (Ae, Be, Ce) representam o modelo da planta estendida e são as matrizes que devem ser usadas nos projetos do vetor K de realimentação de estados e do vetor L do observador.


  

### 13.15 Espaço de estados discretos


  Na abordagem de variáveis de estado apresentada anteriormente os sistemas dinâmicos foram tratados no espaço de estados contínuo. Nesta seção, são apresentados desenvolvimentos análogos, aplicados às etapas de modelagem, análise e projeto, porém considerando-se uma versão discreta para os modelos de variáveis de estado. Devido à analogia entre os resultados dos casos contínuo e discreto, muitos dos desenvolvimentos nesta seção serão omitidos ou apresentados de forma breve.


  

#### 13.15.1 Modelos no espaço de estados discretos


  Considere um sistema contínuo linear e invariante no tempo, descrito na forma de espaço de estados, dado por


   [img:Illustration] 


  sendo que t é o tempo contínuo, u(t) é a variável de entrada, y(t) é a variável de saída, x(t)n×1 é o vetor de estados, x(0)n×1 = x0 é o vetor com as condições iniciais, An×n é a matriz do sistema, Bn×1 é a matriz da entrada, C1×n é a matriz da saída e D1×1 é a matriz de transmissão direta da entrada para a saída.


  Da teoria de equações lineares, sabe-se que a solução analítica fechada para o vetor de estados x(t) é dada por


   [img:Illustration] 


  Conforme é mostrado a seguir, o sistema contínuo representado pela Equação (13.236) pode ser aproximado por um sistema discreto com comportamento similar. Neste texto, é considerada apenas uma dentre as várias aproximações possíveis. Supondo que T é o período de amostragem ou de discretização, t0 = kT e t = kT + T, com k = 0, 1, 2, 3,. . ., então


   [img:Illustration] 


  Considerando a aproximação


   [img:Illustration] 


  que equivale a passar u(t) por um segurador de ordem zero, então, da Equação (13.238) tem-se que


   [img:Illustration] 


  Fazendo a mudança de variável λ = kT + T – τ, obtém-se


   [img:Illustration] 


  A exponencial eAT pode ser escrita numa expansão em série, ou seja,


   [img:Illustration] 


  Definindo a variável Ad = eAT, então


   [img:Illustration] 


  com


   [img:Illustration] 


  Definindo


   [img:Illustration] 


  então, a Equação (13.241) resulta como


   [img:Illustration] 


  
    Por simplicidade de notação, a partir deste ponto o sinal de aproximação na Equação (13.246) é substituído pelo sinal de igualdade e, sempre que possível, o período T é omitido.

  


  Assim,


   [img:Illustration] 


  Note que os vetores x(k) e x(t) representam as mesmas quantidades medidas, nas mesmas unidades. Assim, a equação da saída pode ser escrita como


   [img:Illustration] 


  sendo as matrizes C e D do sistema discreto as mesmas do sistema contínuo.


  Das Equações (13.247) e (13.248) resultam as equações de estados do sistema discreto equivalente ao sistema contínuo da Equação (13.236), ou seja,


   [img:Illustration] 


  

### Exemplo 13.17


  Seja o sistema dinâmico contínuo com função de transferência


   [img:Illustration] 


  A equação diferencial associada a este sistema é


   [img:Illustration] 


  Definindo as variáveis de estado  [img:Illustration]  obtém-se


   [img:Illustration] 


  Logo, as equações de estados na forma matricial são


   [img:Illustration] 


  Considerando um período de discretização T = 0,1s na Equação (13.244), tem-se que


   [img:Illustration] 


  Substituindo a Equação (13.255) nas Equações (13.243) e (13.245), obtém-se


   [img:Illustration] 


  Portanto, as equações de estados do sistema discreto para T = 0,1s resultam como


   [img:Illustration] 


  ■


  

#### 13.15.2 Conversão de estados para função de transferência


  Considere um sistema discreto com entrada u(k) e saída y(k) descrito pelas equações de estados (13.249). Aplicando a transformada Z com condições iniciais nulas, obtém-se


   [img:Illustration] 


  Isolando a transformada Z do vetor de estados X(z), tem-se que


   [img:Illustration] 


  Logo


   [img:Illustration] 


  Portanto, a função de transferência G(z) é dada por


   [img:Illustration] 


  

### Exemplo 13.18


  Considere o sistema discreto representado pelas equações de estados (13.258) e (13.259).


  A matriz (zI – Ad) é dada por


   [img:Illustration] 


  cuja inversa é


   [img:Illustration] 


  Logo


   [img:Illustration] 


  As respostas dos sistemas contínuo e discreto podem ser comparadas por meio de uma entrada do tipo impulso unitário. Se os sistemas contínuo e discreto são equivalentes, as respostas nos instantes de amostragem devem ser iguais. Expandindo em frações parciais a Equação (13.250) e supondo que a entrada é um impulso de Dirac (U (s) = 1), então


   [img:Illustration] 


  cuja transformada de Laplace inversa é


   [img:Illustration] 


  No sinal do tipo impulso de Dirac a "área" sob a função é igual a 1. Um sinal discreto u(kT), que produz efeito equivalente na saída de um sistema discreto, é a sequência {1/T, 0, 0, 0,...}, cuja transformada Z é U (z) = 1/T.


  Expandindo em frações parciais a Equação (13.267), tem-se para T = 0,1 que


   [img:Illustration] 


  cuja transformada Z inversa é


   [img:Illustration] 


  Os gráficos da resposta discreta (13.271) e contínua (13.269) são apresentados na Figura 13.15.


   [img:Illustration] 


  Figura 13.15 Respostas ao impulso.


  ■


  

#### 13.15.3 Autovalores


  Definição 13.4 Seja a matriz Ad, n × n. Os autovalores da matriz Ad, representados pela variável z, são as raízes da equação


   [img:Illustration] 


  na qual z é uma variável complexa, det(.) e | . | denotam a função determinante e I é a matriz identidade.


  

#### 13.15.4 Estabilidade


  Conforme mostrado na Seção 13.15.2, uma realização para a função de transferência G(z) é uma representação na forma de variáveis de estado, dada pelas matrizes (Ad, Bd, C, D), tal que


   [img:Illustration] 


  Um sistema linear, discreto e invariante no tempo, com função de transferência G(z), é BIBO estável se e somente se todos os polos de G(z) têm módulo menor que 1, ou seja, estão localizados estritamente dentro do círculo de raio unitário.


  Sendo cof(zI – Ad) a matriz dos cofatores da matriz (zI – Ad), a função de transferência G(z) pode ser escrita como


   [img:Illustration] 


  Logo, os polos da função de transferência da Equação (13.274) são as raízes da equação característica da matriz Ad, ou seja, os autovalores calculados por meio da Equação (13.272).


  
    Portanto, um sistema linear invariante no tempo, dado pelas matrizes (Ad, Bd, C, D), é BIBO estável se e somente se todos os autovalores da matriz Ad têm módulo menor que 1, ou seja, estão localizados estritamente dentro do círculo de raio unitário.

  


  

### Exemplo 13.19


  No sistema discreto da Equação (13.258), os autovalores da matriz Ad são as raízes da equação


   [img:Illustration] 


  ou seja, z = 1 e z = 0,9048. Logo, o sistema é BIBO instável, pois a matriz Ad possui um autovalor em z = 1, que está sobre a circunferência de raio unitário.


  ■


  

### 13.16 Controle por realimentação de estados discretos


  O esquema de controle por realimentação de estados num sistema discreto é análogo ao do caso contínuo e está representado no diagrama de blocos da Figura 13.16.


   [img:Illustration] 


  Figura 13.16 Sistema discreto com controlador por realimentação de estados.


  Na Figura 13.16 e nos cálculos seguintes, a matriz D1×1 de transmissão direta da entrada para a saída é omitida, pois na maioria das plantas ela é frequentemente nula. Assim, o sistema discreto é dado por


   [img:Illustration] 


  com função de transferência


   [img:Illustration] 


  Na Figura 13.16 o operador z–1 corresponde ao operador atraso unitário, ou seja,


   [img:Illustration] 


  com condições iniciais nulas.


  A realimentação de estados é realizada por meio do vetor de ganhos K, dado por


   [img:Illustration] 


  com constantes k1, k2, k3, ... , kn.


  O sinal de controle u(k) é dado por


   [img:Illustration] 


  sendo r(k) o sinal de referência.


  Das Equações (13.276) e (13.280) têm-se que


   [img:Illustration] 


  Assim, o sistema em malha fechada resulta como


   [img:Illustration] 


  cujos polos de malha fechada são os autovalores da matriz Ad – BdK, que são as raízes da equação característica


   [img:Illustration] 


  Portanto, a dinâmica do sistema em malha fechada é dada pelos autovalores da matriz Ad – BdK. Como no caso contínuo, uma escolha adequada do vetor K pode estabilizar um sistema instável em malha aberta, reduzir ou eliminar um eventual sobressinal da saída ou também aumentar a velocidade da resposta transitória da malha fechada, se a resposta do sistema sem controlador for lenta. Esses objetivos de controle são resumidos nas Tabela 13.3.


  Tabela 13.3 Objetivos de um sistema de controle


   [img:Illustration] 


  Sendo dadas as matrizes Ad e Bd do sistema discreto, deve-se verificar em que condições é possível impor arbitrariamente os autovalores da matriz Ad – BdK, por meio de uma escolha adequada do vetor K. Como no caso contínuo, a condição para que isto seja possível está associada à propriedade de controlabilidade do par (Ad, Bd), cujos conceitos são análogos aos dos sistemas contínuos.


  

#### 13.16.1 Alocação de polos de malha fechada


  Pode-se mostrar que as seguintes afirmações são equivalentes:


  i) existe um vetor de ganhos K tal que os autovalores de Ad – BdK podem ser alocados em qualquer posição desejada do plano z;


  ii) existe uma sequência de entrada {u(0), u(1), u(2) ,..., u(r – 1)} capaz de transferir um estado qualquer x(0) para um estado desejado x(r);


  iii) a matriz de controlabilidade


   [img:Illustration] 


  tem posto pleno, ou seja, posto(M) = n;


  iv) o par (Ad , Bd) é controlável.


  Supondo que o sistema seja controlável, um primeiro procedimento para projeto do vetor de ganhos K de realimentação de estados, consiste em determinar o polinômio característico de malha fechada


   [img:Illustration] 


  Igualando a Equação (13.285) ao polinômio formado pelos polos de malha fechada desejados, obtém-se um sistema de equações nas variáveis k1, k2 ,..., kn, cuja solução fornece o vetor de ganhos de realimentação K.


  Este procedimento pode levar a um sistema de equações não lineares e, salvo nos casos mais simples, deve ser resolvido computacionalmente devido à grande quantidade de cálculos envolvidos.


  

### Exemplo 13.20


  Considere o sistema discreto instável do Exemplo 13.17, com as seguintes equações de estados para T = 0,1s


   [img:Illustration] 


  Deseja-se projetar um controlador por realimentação de estados discretos, tal que o sistema em malha fechada apresente polos com coeficiente de amortecimento ξ = 0,456, correspondente a um sobressinal Mp ≅ 20% para uma resposta a degrau, com frequência natural ωn = 2 rad/s, correspondente a um tempo de pico tp ≅ 1,8s. Nestas condições, os polos de malha fechada no plano s, são dados por


   [img:Illustration] 


  No plano z, os polos de malha fechada são mapeados em


   [img:Illustration] 


  Assim, o polinômio característico desejado para o sistema em malha fechada é dado por


   [img:Illustration] 


  Sendo K = [k1 k2], o polinômio característico em função dos ganhos k1 e k2 é dado por


   [img:Illustration] 


  Igualando os coeficientes dos polinômios (13.290) e (13.291), obtém-se um sistema de duas equações nas incógnitas k1 e k2, ou seja,


   [img:Illustration] 


  cuja solução é


   [img:Illustration] 


  As equações de estados do sistema em malha fechada resultam como


   [img:Illustration] 


  A partir das equações de estados (13.294) e (13.295) do sistema em malha fechada pode-se obter a resposta transitória da saída y(kT), quando é aplicado um degrau unitário na referência r(kT), que é apresentada na Figura 13.17.


   [img:Illustration] 


  Figura 13.17 Resposta da saída y(kT) quando é aplicado um degrau unitário na referência r(kT).


  Note que o sistema em malha fechada se tornou estável, com a saída estabilizada no valor estacionário y(∞) ≅ 0,26. Além disso, a resposta transitória apresenta um sobressinal Mp ≅ 20% e um tempo de pico ts ≅ 1,8s, de acordo com a especificação de projeto.


  Porém, a resposta transitória apresenta um erro estacionário e(∞) = r(∞) – y(∞) ≅ 1 – 0,26 ≅ 0,74. Para eliminar esse erro, basta incluir um bloco integrador na entrada da planta, conforme é apresentado no final deste capítulo.


  ■


  

#### 13.16.2 Regulador Linear Quadrático - RLQ


  De modo análogo ao caso contínuo, nesta seção é apresentado o projeto do controlador por realimentação de estados pela técnica do chamado Regulador Linear Quadrático - RLQ.


  Considere o sistema discreto


   [img:Illustration] 


  O problema do Regulador Linear Quadrático consiste em determinar o vetor de ganhos de realimentação de estados K, tal que


   [img:Illustration] 


  que minimize o índice de desempenho


   [img:Illustration] 


  sendo que a matriz Q = QT ≥ 0 é uma matriz simétrica semidefinida positiva de ponderação das variáveis de estado e R > 0 é uma constante positiva de ponderação do esforço de controle.


  O termo xT (k)Qx(k) penaliza o desvio do vetor de estados x(k) em relação à origem e o termo Ru2(k), que é uma medida da energia do sinal u(k), penaliza esforços de controle excessivos.


  Para o escalar R deve-se escolher qualquer constante positiva. Já para a matriz Q, embora seja possível adotar qualquer matriz simétrica semidefinida positiva, são comuns escolhas de matrizes diagonais.


  
    Pode-se mostrar que a solução do problema do Regulador Linear Quadrático é dada por


     [img:Illustration] 


    sendo F a solução estabilizante da seguinte equação algébrica discreta de Riccati


     [img:Illustration] 


    com


     [img:Illustration] 

  


  A equação de Riccati (13.300) pode ter várias soluções8, mas somente uma delas estabiliza o sistema em malha fechada. Como esta equação é não linear em F, para resolvê-la pode-se utilizar um algoritmo recursivo com N passos de repetição. A quantidade de passos N deve ser suficientemente "grande" para que ocorra a convergência da solução F da equação de Riccati e do controlador K, dado por


   [img:Illustration] 


  com constantes k1, k2, k3, ... , kn.


  O algoritmo resultante para a solução F da equação algébrica discreta de Riccati e cálculo do vetor K é apresentado na Tabela 13.4.


  Tabela 13.4 Algoritmo para cálculo da solução F da equação de Riccati e do controlador K.


   [img:Illustration] 


  

### Exemplo 13.21


  Considere o sistema discreto instável do Exemplo 13.17, com as seguintes equações de estados para T = 0,1s


   [img:Illustration] 


  Para o projeto do regulador linear quadrático, inicialmente deve-se adotar valores para a matriz Q e para o escalar R. Como há infinitos valores que podem ser adotados para Q e R, se ao final do cálculo do vetor K o controlador não atender às especificações, então o projeto deve ser refeito.


  Adotando R = 1,


   [img:Illustration] 


  e executando o algoritmo da Tabela 13.4 para N = 100 repetições, obtém-se a solução da equação algébrica discreta de Riccati


   [img:Illustration] 


  e o controlador


   [img:Illustration] 


  As equações de estados do sistema em malha fechada resultam como


   [img:Illustration] 


  Os autovalores do sistema em malha fechada são as raízes de


   [img:Illustration] 


  ou seja,


   [img:Illustration] 


  Como |z1,2| ≅ 0,917 < 1, o sistema em malha fechada é estável.


  Supondo que a entrada de referência r(kT) é zero, a partir das equações de estados (13.308) e (13.309) do sistema em malha fechada pode-se obter a resposta transitória de x1(kT) e x2(kT) para a condição inicial


   [img:Illustration] 


  Na Figura 13.18 são apresentados os gráficos da resposta transitória dos estados, mostrando que estes partem da condição inicial e convergem para zero.


   [img:Illustration] 


  Figura 13.18 Resposta transitória dos estados para o sistema em malha fechada com o controlador RLQ.


  ■


  

### 13.17 Observador ou estimador de estados discretos


  O desenvolvimento do observador ou estimador de estados discretos é análogo ao caso contínuo. O diagrama de blocos da planta com o observador de estados é mostrado na Figura 13.19.


  As equações de estados estimados do observador são dadas por


   [img:Illustration] 


  com condição inicial  [img:Illustration] (0).


  O bloco correspondente à planta é dado por


   [img:Illustration] 


  Subtraindo os estados da planta x(k + 1) dos estados estimados  [img:Illustration] (k + 1), obtém-se


   [img:Illustration] 


  Supondo que os erros entre as matrizes da planta (A, B, C) e do modelo  [img:Illustration]  são suficientemente pequenos, então


   [img:Illustration] 


   [img:Illustration] 


  Figura 13.19 Diagrama de blocos contendo planta e observador de estados discretos.


  Portanto, a dinâmica do sinal de erro de observação  [img:Illustration] (k) = x(k) –  [img:Illustration] (k) fica determinada, aproximadamente, pela matriz Ad – LC.


  • Se a planta é instável, basta escolher L de maneira adequada para que a matriz Ad – LC tenha autovalores estáveis e, consequentemente,  [img:Illustration] (k) → x(k).


  • Escolhendo L de maneira adequada é possível fazer os autovalores de Ad – LC muito mais rápidos que os da matriz Ad e, consequentemente,  [img:Illustration] (k) → x(k).


  Como no caso contínuo pode-se estabelecer analogias entre as matrizes do regulador linear quadrático e do observador de estados que estão apresentadas na Tabela 13.5. Para calcular o vetor L, basta resolver a equação de Riccati, substituindo as matrizes do regulador pelas matrizes análogas correspondentes ao observador.


  Tabela 13.5 Analogias entre regulador linear quadrático e observador de estados discretos.


   [img:Illustration] 


  O algoritmo resultante para a solução F da equação algébrica discreta de Riccati e cálculo do vetor L é apresentado na Tabela 13.6. A quantidade de passos N deve ser suficientemente "grande" para que ocorra a convergência da solução F da equação de Riccati e do vetor L, dado por


   [img:Illustration] 


  com constantes l1, l2, l3, ... , ln.


  Tabela 13.6 Algoritmo para cálculo da solução F da equação de Riccati e do vetor L.


   [img:Illustration] 


  

### Exemplo 13.22


  Considere o sistema discreto instável do Exemplo 13.21, com as equações de estados (13.303) e (13.304). Para o cálculo do vetor L do observador de estados, inicialmente deve-se adotar valores para a matriz Q e para o escalar R. Como há infinitos valores que podem ser adotados para Q e R, se ao final do cálculo do vetor L, as especificações de projeto da resposta transitória da malha fechada não forem satisfeitas, então, o projeto deve ser refeito.


  Adotando R = 1,


   [img:Illustration] 


  e executando o algoritmo da Tabela 13.6 para N = 100 repetições, obtém-se a solução da equação algébrica discreta de Riccati


   [img:Illustration] 


  e o vetor


   [img:Illustration] 


  Os autovalores de malha fechada são as raízes de


   [img:Illustration] 


  Portanto, a malha fechada com observador é estável.


  ■


  

#### 13.17.1 Alocação de polos de malha fechada no observador


  É importante investigar em que condições é possível impor os autovalores de Ad – LC apenas manipulando os termos de L. Pode-se mostrar que estas condições estão associadas à propriedade de observabilidade do par (C,Ad).


  Mais uma vez, considerando a analogia do conceito de observabilidade com o caso contínuo, pode-se mostrar que as seguintes afirmações são equivalentes:


  i) existe um vetor L tal que os autovalores de Ad – LC podem ser alocados em qualquer valor desejado;


  ii) para qualquer estado inicial x(0), existe um número r finito tal que x(0) pode ser calculado a partir da sequência de saída {y(0), y(1) ,..., y(r – 1)} ;


  iii) a matriz de observabilidade


   [img:Illustration] 


  tem posto pleno, ou seja, posto(N) = n ;


  iv) o par (C,Ad) é observável.


  Supondo que o sistema seja observável, para calcular o vetor de ganhos L do observador de estados, inicialmente deve-se determinar o polinômio característico de malha fechada


   [img:Illustration] 


  Igualando a Equação (13.323) ao polinômio formado pelos polos de malha fechada desejados, obtém-se um sistema de equações nas variáveis l1, l2, l3 ,..., ln, cuja solução fornece o vetor de ganhos L. É recomendável adotar os polos de malha fechada de |zI – (Ad – LC)| = 0 mais rápidos que os polos de malha fechada de |zI – (Ad – BdK)| = 0.


  

### Exemplo 13.23


  Considere o sistema discreto instável do Exemplo 13.20, com as equações de estados (13.286) e (13.287). Os polos de malha fechada do controlador foram adotados de tal forma a fornecer uma resposta transitória com coeficiente de amortecimento ξ = 0,456, com frequência natural ωn = 2 rad/s. Para o projeto do observador, os polos de malha fechada devem ser mais rápidos que os polos adotados no projeto do controlador. Supondo um mesmo coeficiente de amortecimento ξ = 0,456, mas com uma frequência natural 5 vezes maior, isto é, ωn = 10 rad/s, no plano s tem-se que


   [img:Illustration] 


  No plano z os polos de malha fechada são mapeados para T = 0,1s em


   [img:Illustration] 


  O polinômio característico desejado para o sistema em malha fechada é dado por


   [img:Illustration] 


  O polinômio característico em função dos ganhos l1 e l2 do vetor L é dado por


   [img:Illustration] 


  Igualando os coeficientes dos polinômios (13.326) e (13.327), obtém-se um sistema de duas equações, nas incógnitas l1 e l2, ou seja,


   [img:Illustration] 


  cuja solução é


   [img:Illustration] 


  ■


  

#### 13.17.2 Conexão entre controlador e observador de estados discretos


  De forma análoga ao estudado no caso de sistemas contínuos, a realimentação das variáveis de estado é substituída pela realimentação das variáveis de estado estimadas. O diagrama de blocos completo do sistema em malha fechada é apresentado na Figura 13.20.


   [img:Illustration] 


  Figura 13.20 Malha fechada com controlador e observador de estados.


  O erro do estimador de estados  [img:Illustration] (k) é dado por


   [img:Illustration] 


  Logo, os estados estimados  [img:Illustration] (k) valem


   [img:Illustration] 


  O sinal u(k) na entrada da planta é dado por


   [img:Illustration] 


  Da equação de estados da planta tem-se que


   [img:Illustration] 


  Da Equação (13.316) tem-se que


   [img:Illustration] 


  Das Equações (13.333) e (13.334) resultam as equações dinâmicas do sistema em malha fechada da Figura 13.20, ou seja,


   [img:Illustration] 


  Como Admf é uma matriz triangular, os seus autovalores são os autovalores da matriz Ad – BdK, decorrentes do projeto do controlador, mais os autovalores da matriz Ad – LC, decorrentes do projeto do observador de estados, ou seja,


   [img:Illustration] 


  Pelo Princípio da Separação, para se fazer realimentação de estados com os estados estimados pode-se projetar o controlador (como se não houvesse observador) e o observador (como se não houvesse controlador), fazendo depois a conexão de ambos.


  

### Exemplo 13.24


  Considere os projetos do controlador do Exemplo 13.20 e do observador de estados do Exemplo 13.23, ambos calculados pelo método de alocação de polos de malha fechada. Da equação de estados (13.335) do sistema em malha fechada resulta


   [img:Illustration] 


  Da Equação (13.331) o vetor  [img:Illustration] (kT) dos estados estimados é dado por


   [img:Illustration] 


  Implementando as equações de diferenças (13.337), e (13.338) num programa de computador podem ser obtidos os gráficos do comportamento transitório dos estados x1(kT), x2(kT),  [img:Illustration] 1(kT) e  [img:Illustration] 2(kT), que são apresentados na Figura 13.21. Nesta simulação foi considerado um erro inicial entre os estados x(0) e a sua estimativa  [img:Illustration] (0), ou seja,


   [img:Illustration] 


   [img:Illustration] 


  Figura 13.21 Resposta transitória da malha fechada com controlador e observador projetados pelo método de alocação de polos.


  O efeito do erro na estimativa inicial dos estados pode ser observado no primeiro segundo da simulação. De fato, após o transitório os estados estimados convergem para os estados da planta, isto é,  [img:Illustration] 1(kT) → x1(kT) e  [img:Illustration] 2(kT) → x2(kT), o que mostra a eficiência do observador.


  Resultado semelhante também ocorre quando são considerados os projetos do controlador do Exemplo 13.21 e do observador de estados do Exemplo 13.22, ambos calculados por meio da solução de uma equação algébrica discreta de Riccati. Da equação de estados (13.335), resulta


   [img:Illustration] 


  Implementando as equações de diferenças (13.338) e (13.340) num programa de computador podem ser obtidos os gráficos do comportamento transitório dos estados x1(kT), x2(kT),  [img:Illustration] 1(kT) e  [img:Illustration] 2(kT), que são apresentados na Figura 13.22. Como no Exemplo 13.24 foi considerado um erro inicial entre os estados x(0) e a sua estimativa  [img:Illustration] (0), ou seja,


   [img:Illustration] 


  Assim como no projeto por alocação de polos, os estados estimados convergem para os estados da planta, o que mostra a eficiência do observador.


   [img:Illustration] 


  Figura 13.22 Resposta transitória da malha fechada com controlador e observador projetados por meio da solução das equações algébricas discretas de Riccati.


  ■


  

#### 13.17.3 Função de transferência do bloco controlador+observador


  Supondo que os erros entre as matrizes (Ad, Bd, C) e  [img:Illustration]  são suficientemente pequenos, da Equação (13.313) do observador, tem-se que


   [img:Illustration] 


  Da Equação (13.332) tem-se que


   [img:Illustration] 


  cuja transformada Z, considerando condições iniciais nulas, é


   [img:Illustration] 


  Isolando  [img:Illustration]  (z), obtém-se


   [img:Illustration] 


  A transformada Z da Equação (13.332) resulta como


   [img:Illustration] 


  Rearranjando os blocos da Figura 13.20, de forma a explicitar a realimentação da saída, resulta o diagrama de blocos de malha fechada da Figura 13.23.


   [img:Illustration] 


  Figura 13.23 Sistema em malha fechada com controlador e observador de estados discretos.


  A transformada Z do sinal de erro, para R(z) = 0, é


   [img:Illustration] 


  Portanto, a função de transferência do conjunto controlador + observador resulta como


   [img:Illustration] 


  Definindo xc(k) como sendo os estados do conjunto controlador + observador, as equações de estados são dadas por


   [img:Illustration] 


  Sendo as equações de estados da planta dadas por


   [img:Illustration] 


  então, as equações de estados do sistema em malha fechada resultam como


   [img:Illustration] 


  

### Exemplo 13.25


  Considere os projetos do controlador do Exemplo 13.20 e do observador de estados do Exemplo 13.23, ambos calculados pelo método de alocação de polos de malha fechada. Das equações de estados (13.351) e (13.352) resultam


   [img:Illustration] 


   [img:Illustration] 


  Da matriz Admf na Equação (13.353) tem-se que os polos de malha fechada são as raízes de


   [img:Illustration] 


  ou seja, 0,8984 + 0,1618j e 0,3989 ± 0,4925j.


  Considere agora os projetos do controlador do Exemplo 13.21 e do observador de estados do Exemplo 13.22, ambos calculados por meio da solução de uma equação algébrica discreta de Riccati. Das equações de estados (13.351) e (13.352) resultam


   [img:Illustration] 


  Da matriz Admf na Equação (13.356) tem-se que os polos de malha fechada são as raízes de


   [img:Illustration] 


  ou seja, 0,9159 ± 0,0459j, 0,3837 e 0,8675.


  Na Figura 13.24 são apresentados os gráficos da resposta transitória da saída y(kT) quando é aplicado um degrau unitário na referência r(kT). Nesta figura são considerados o sistema em malha fechada dado pelas Equações (13.353) e (13.354), obtido pelo método de alocação de polos e o sistema em malha fechada dado pelas Equações (13.356) e (13.357), obtido por meio da solução das equações de Riccati.


   [img:Illustration] 


  Figura 13.24 Resposta da saída y(kT) quando é aplicado um degrau unitário na referência r(kT).


  Comparando os gráficos da Figura 13.24 verifica-se que as respostas transitórias são diferentes. No método de alocação de polos, a resposta transitória da saída é mais rápida e apresenta sobressinal próximo ao especificado em projeto. Porém, a resposta transitória obtida por meio da solução das equações de Riccati é mais lenta e sem sobressinal. Isso se deve às diferentes posições dos polos de malha fechada.


  ■


  

### 13.18 Inclusão de integrador discreto na malha de controle


  Assim como no caso contínuo, são comuns aplicações em que o sistema em malha fechada é submetido a um sinal de referência diferente de zero. Neste caso, para obter erro estacionário nulo quando o sinal de referência r(k) é do tipo degrau, basta incluir um integrador discreto na entrada da planta, de acordo com o diagrama de blocos da Figura 13.25.


   [img:Illustration] 


  Figura 13.25 Diagrama de blocos mostrando a inclusão do integrador na entrada da planta.


  De acordo com a Figura 13.25, o bloco do controlador+observador deve ser projetado para o conjunto planta+integrador, denominado planta estendida. Após o projeto, o integrador deve ser implementado juntamente com o bloco do controlador+observador. O modelo para a planta estendida é obtido a partir do modelo da planta juntamente com o modelo de variável de estado para o integrador.


  Há diversas aproximações que podem ser usadas para representar o bloco de um integrador discreto. No caso contínuo, a transformada de Laplace de um bloco integrador é 1/s. Adotando a aproximação retangular para trás da Seção 12.2.2, obtém-se a função de transferência do integrador discreto, dada por


   [img:Illustration] 


  Assim, a equação de diferenças do integrador resulta como


   [img:Illustration] 


  Definindo a variável de estado xi(kT) = u [(k–1)T], obtém-se a equação de estado do integrador


   [img:Illustration] 


  A Equação (13.361) em conjunto com o modelo da planta (13.249) produz o modelo de variáveis de estado para a planta estendida, dado por


   [img:Illustration] 


  As matrizes (Ae, Be, Ce, D) representam o modelo da planta estendida e são as matrizes que devem ser usadas nos projetos do vetor K de realimentação de estados e do vetor L do observador.


  

### 13.19 Exercícios resolvidos


  

### Exercício 13.1


  Determine as equações de estados que representam o circuito elétrico RLC série da Figura 13.26. Suponha que a entrada do circuito é a tensão v(t) e que a saída é a tensão vc(t) no capacitor.


   [img:Illustration] 


  Figura 13.26 Circuito elétrico RLC série.


  Solução


  Aplicando a lei de Kirchhoff das tensões, obtém-se


   [img:Illustration] 


  Sabendo-se que  [img:Illustration]  então


   [img:Illustration] 


  Isolando o termo com derivada de maior ordem na Equação (13.365), tem-se que


   [img:Illustration] 


  Definindo as variáveis de estado  [img:Illustration]  obtém-se


   [img:Illustration] 


  Logo, as equações de estados na forma matricial são


   [img:Illustration] 


  

### Exercício 13.2


  Determine a função de transferência do circuito RLC série da Figura 13.26 a partir das equações de estados (13.368) e (13.369).


  Solução


  Da Equação (13.72) tem-se que a função de transferência do circuito é dada por


   [img:Illustration] 


  A matriz (sI – A) é dada por


   [img:Illustration] 


  cuja inversa é


   [img:Illustration] 


  Da Equação (13.370) tem-se que


   [img:Illustration] 


  Portanto, a função de transferência G(s) do circuito com entrada v(t) e saída vc(t) é


   [img:Illustration] 


  que também pode ser obtida por meio da transformada de Laplace da Equação (13.365).


  

### Exercício 13.3


  Considere o sistema de inércia e atrito rotacional da Figura 13.27, em que J representa a inércia rotacional, B representa o coeficiente de atrito rotacional, τ (t) é o torque de entrada e θ(t) é o deslocamento angular de saída. Determine as equações de estados que representam esse sistema.


   [img:Illustration] 


  Figura 13.27 Sistema de inércia e atrito rotacional.


  Solução


  A equação diferencial que representa a dinâmica do sistema é dada por


   [img:Illustration] 


  Isolando o termo com derivada de maior ordem na Equação (13.375), tem-se que


   [img:Illustration] 


  Definindo as variáveis de estado  [img:Illustration]  obtém-se


   [img:Illustration] 


  Logo, as equações de estados na forma matricial são


   [img:Illustration] 


  

### Exercício 13.4


  Determine a função de transferência do sistema de inércia e atrito rotacional da Figura 13.27 a partir das equações de estados (13.378) e (13.379).


  Solução


  Da Equação (13.72) tem-se que a função de transferência do sistema é dada por


   [img:Illustration] 


  A matriz (sI – A) é dada por


   [img:Illustration] 


  cuja inversa é


   [img:Illustration] 


  Da Equação (13.380) tem-se que


   [img:Illustration] 


  Portanto, a função de transferência G(s) do sistema com entrada τ (t) e saída θ(t) é


   [img:Illustration] 


  que também pode ser obtida por meio da transformada de Laplace da Equação (13.375).


  

### Exercício 13.5


  Considere um sistema com a função de transferência


   [img:Illustration] 


  Represente o sistema na forma canônica controlável e verifique as condições de controlabilidade e de observabilidade.


  Solução


  Separar o numerador do denominador da função de transferência G(s) em dois blocos, como na Figura 13.28.


   [img:Illustration] 


  Figura 13.28 Diagrama de blocos da função de transferência (13.385).


  Da Figura 13.28 tem-se que


   [img:Illustration] 


  Aplicando a transformada inversa de Laplace e isolando a derivada de maior ordem na Equação (13.386) resulta


   [img:Illustration] 


  Definindo as variáveis de estado  [img:Illustration]  resulta o sistema de equações


   [img:Illustration] 


  Portanto, as equações de estados na forma matricial são dadas por


   [img:Illustration] 


  Como o sistema possui n = 2 estados, a matriz M2×2 de controlabilidade é dada por


   [img:Illustration] 


  Como det(M) ≠ 0, a matriz M tem posto pleno n = 2.


  Logo, o sistema é controlável. Como era de se esperar, já que o sistema está representado na forma canônica controlável.


  Como o sistema possui n = 2 estados, a matriz N2×2 de observabilidade é dada por


   [img:Illustration] 


  Como det(N) = 0, a matriz N não tem posto pleno.


  Logo, o sistema não é observável.


  

### Exercício 13.6


  Considere um sistema com a função de transferência


   [img:Illustration] 


  Represente o sistema na forma canônica observável e verifique as condições de controlabilidade e de observabilidade.


  Solução


  Aplicando a transformada inversa de Laplace na Equação (13.395) resulta


   [img:Illustration] 


  Definindo


   [img:Illustration] 


  resulta


   [img:Illustration] 


  Integrando a Equação (13.398) com condições iniciais nulas, obtém-se


   [img:Illustration] 


  Definindo


   [img:Illustration] 


  resulta


   [img:Illustration] 


  Integrando a Equação (13.401) com condições iniciais nulas, obtém-se


   [img:Illustration] 


  Substituindo a Equação (13.402) nas Equações (13.397) e (13.400), resulta o sistema


   [img:Illustration] 


  Portanto, as equações de estados na forma matricial são dadas por


   [img:Illustration] 


  A matriz M2×2 de controlabilidade é dada por


   [img:Illustration] 


  Como det(M) = 0, a matriz M não tem posto pleno.


  Logo, o sistema não é controlável.


  A matriz N2×2 de observabilidade é dada por


   [img:Illustration] 


  Como det(N) ≠ 0, a matriz N tem posto pleno n = 2.


  Logo, o sistema é observável. Como era de se esperar, já que o sistema está representado na forma canônica observável.


  
    Observações:


    • as Equações (13.391) e (13.392) na forma canônica controlável e as Equações (13.404) e (13.405) na forma canônica observável satisfazem as correspondências da Tabela 13.1.


    • quando ocorrer cancelamento de polos e zeros na função de transferência, o sistema não pode ser simultaneamente controlável e observável, independentemente das equações de estados adotadas.

  


  

### Exercício 13.7


  Um processo industrial com entrada u(t) e saída y(t) é representado pelas equações de estados


   [img:Illustration] 


  Determine a função de transferência G(s) = Y(s)/U(s) do processo.


  Solução


  A função de transferência do sistema é dada por


   [img:Illustration] 


  A matriz (sI – A) é dada por


   [img:Illustration] 


  cuja inversa é


   [img:Illustration] 


  Multiplicando a Equação (13.412) à esquerda pelo vetor C e à direita pelo vetor B, obtém-se


   [img:Illustration] 


  Da Equação (13.410) tem-se que


   [img:Illustration] 


  

### Exercício 13.8


  Determine se o sistema representado pelas Equações (13.408) e (13.409) é estável ou instável.


  Solução


  Os autovalores da matriz A são as raízes da equação


   [img:Illustration] 


  ou seja,


   [img:Illustration] 


  Logo, os autovalores da matriz A são s = –1, s = –2 e s = –3, que corresponde aos polos da função de transferência (13.414).


  Portanto, o sistema é BIBO estável, pois todos os autovalores da matriz A estão localizados no semiplano esquerdo aberto do plano s, excluído o eixo imaginário.


  

### Exercício 13.9


  Considere a função de transferência do processo industrial do Exercício (13.7).


   [img:Illustration] 


  Represente o sistema por equações de estados nas formas canônicas controlável e observável.


  Solução


  Separar o numerador do denominador da função de transferência G(s) em dois blocos, como na Figura 13.29.


   [img:Illustration] 


  Figura 13.29 Diagrama de blocos da função de transferência (13.417).


  Da Figura 13.29 tem-se que


   [img:Illustration] 


  Aplicando a transformada inversa de Laplace e isolando a derivada de maior ordem na Equação (13.418), resulta


   [img:Illustration] 


  Substituindo a Equação (13.420) na Equação (13.421), resulta


   [img:Illustration] 


  Definindo as variáveis de estado


   [img:Illustration] 


  resulta o sistema de equações


   [img:Illustration] 


  Portanto, as equações de estados na forma canônica controlável são


   [img:Illustration] 


  Uma vez obtidas as Equações (13.425) e (13.426) da forma canônica controlável, as equações de estados da forma canônica observável podem ser obtidas por meio das correspondências da Tabela 13.1, ou seja,


   [img:Illustration] 


  

### Exercício 13.10


  Represente o sistema do Exercício (13.7) na forma canônica controlável por meio de uma transformação de similaridade.


  Solução


  Da Equação (13.112) tem-se que a matriz inversa da transformação de similaridade é dada por


   [img:Illustration] 


  Para o sistema de Equações (13.408) e (13.409), a matriz de controlabilidade é dada por


   [img:Illustration] 


  A matriz inversa de controlabilidade do sistema na forma canônica controlável é dada pela Equação (13.114). Como a ordem do sistema é n = 3, então


   [img:Illustration] 


  Os coeficientes a1 e a2 são determinados a partir da função de transferência do processo. Das Equações (13.109) e (13.414) têm-se que


   [img:Illustration] 


  Comparando os coeficientes, obtém-se a1 = 11 e a2 = 6.


  Da Equação (13.429) tem-se que


   [img:Illustration] 


  Logo, a matriz de transformação de similaridade é dada por


   [img:Illustration] 


  Sabendo-se que A = P AP–1, B = PB, C = CP–1 e D = D, as equações de estados na forma canônica controlável são dadas por


   [img:Illustration] 


  Observe que as Equações (13.435) e (13.436) correspondem às mesmas Equações (13.425) e (13.426) obtidas pela metodologia do Exercício (13.9).


  

### Exercício 13.11


  A função de transferência de um processo industrial é dada por


   [img:Illustration] 


  Projete um controlador K = [k1 k2 k3] por realimentação de estados de modo que os polos de malha fechada estejam localizados em s = –1 + j, s = –1 – j e s = –10.


  Solução


  O processo industrial é BIBO instável, pois possui um polo na origem do plano s e dois polos sobre o eixo imaginário em s = ±j. Logo, necessita de um controlador para estabilizá-lo.


  Para escrever as equações de estados na forma canônica controlável das Equações (13.25) e (13.26), separar o numerador do denominador da função de transferência G(s) em dois blocos, como na Figura 13.30.


   [img:Illustration] 


  Figura 13.30 Diagrama de blocos da função de transferência (13.437).


  Da Figura 13.30 tem-se que


   [img:Illustration] 


  Aplicando a transformada inversa de Laplace e isolando a derivada de maior ordem na Equação (13.438), resulta


   [img:Illustration] 


  Definindo as variáveis de estado


   [img:Illustration] 


  resulta o sistema de equações


   [img:Illustration] 


  Portanto, as equações de estados na forma canônica controlável são


   [img:Illustration] 


  A matriz de malha fechada com o controlador K é


   [img:Illustration] 


  Os polos de malha fechada são as raízes da equação característica


   [img:Illustration] 


  A partir dos polos de malha fechada desejados obtém-se o polinômio característico


   [img:Illustration] 


  Comparando os coeficientes dos polinômios (13.447) e (13.448), obtém-se os ganhos do controlador K de realimentação de estados, ou seja,


   [img:Illustration] 


  Sabendo-se que u(t) = r(t) – Kx(t) pode-se representar o sistema em malha fechada pelo diagrama de blocos da Figura 13.31. O fato das realimentações possuirem apenas ganhos constantes não aumenta o número de polos do sistema em malha fechada. As realimentações apenas deslocam os polos da planta para as posições escolhidas no plano s.


   [img:Illustration] 


  Figura 13.31 Diagrama de blocos com controlador por realimentação de estados.


  

### Exercício 13.12


  Um motor de corrente contínua, utilizado para realizar acionamentos mecânicos, tem como entrada a tensão u(t) aplicada em seus terminais e como saída a posição angular y(t) do seu eixo. A função de transferência do motor é dada por


   [img:Illustration] 


  Projete um controlador K = [k1 k2] por alocação de polos de malha fechada de modo que a resposta transitória da posição angular y(t), quando é aplicado um degrau unitário na referência r(t), satisfaça às seguintes especificações:


  • sobressinal máximo Mp = 4% ;


  • tempo de pico da resposta tp = 1s ;


  • erro estacionário nulo entre a referência e a saída.


  Solução


  Inicialmente é preciso determinar os polos de malha fechada correspondentes às especificações da resposta transitória desejada. Como a função de transferência do motor é a de um sistema de segunda ordem, o coeficiente de amortecimento ξ e a frequência natural ωn podem ser determinados a partir das expressões do sobressinal e do tempo de pico da resposta, ou seja,


   [img:Illustration] 


  Os polos de malha fechada de sistemas de segunda ordem podem ser determinados a partir do coeficiente de amortecimento ξ e da frequência natural ωn, ou seja,


   [img:Illustration] 


  Em seguida é necessário determinar as equações de estados na forma canônica controlável do motor. Como o numerador da função de transferência é uma constante igual a 1, não é necessário separá-la em dois blocos, podendo-se escrever diretamente que


   [img:Illustration] 


  Aplicando a transformada inversa de Laplace e isolando a derivada de maior ordem na Equação (13.454), resulta


   [img:Illustration] 


  Definindo as variáveis de estado


   [img:Illustration] 


  resulta o sistema de equações


   [img:Illustration] 


  Portanto, as equações de estados na forma canônica controlável são


   [img:Illustration] 


  A matriz de malha fechada com o controlador K é


   [img:Illustration] 


  Os polos de malha fechada são as raízes da equação característica


   [img:Illustration] 


  A partir dos polos de malha fechada desejados obtém-se o polinômio característico


   [img:Illustration] 


  Comparando os coeficientes dos polinômios (13.461) e (13.462), obtém-se os ganhos do controlador K de realimentação de estados, ou seja,


   [img:Illustration] 


  A função de transferência de malha fechada é dada por


   [img:Illustration] 


  Sabendo-se que u(t) = r'(t) – Kx(t) = r'(t) – k1x1(t) – k2x2(t) pode-se representar o sistema em malha fechada pelo diagrama de blocos da Figura 13.32.


   [img:Illustration] 


  Figura 13.32 Diagrama de blocos com controlador por realimentação de estados.


  A diferença entre a referência r(t) e a saída y(t) somente representa um sinal de erro e(t) quando a realimentação externa é unitária, pois neste caso é realizada uma comparação da referência com a saída da planta.


  Quando a realimentação externa não é unitária, a diferença r(t) – k1y(t) não tem significado de erro, pois não há uma comparação direta entre os sinais r(t) e y(t). Para que essa comparação seja possível, é necessário fazer uma correção de ganho, acrescentando um bloco com ganho k1 entre r(t) e r'(t), conforme é mostrado na Figura 13.32. Desta forma tem-se que


   [img:Illustration] 


  Adotando esse procedimento, da Equação (13.464), obtém-se


   [img:Illustration] 


  Quando a referência r(t) for um degrau unitário (R(s) = 1/s), a saída estacionária y(∞) pode ser determinada pelo teorema do valor final, ou seja,


   [img:Illustration] 


  Logo, o erro estacionário é nulo, pois


   [img:Illustration] 


  O gráfico da resposta transitória é apresentado na Figura 13.33. Observe que todas as especificações de projeto são satisfeitas.


   [img:Illustration] 


  Figura 13.33 Resposta transitória da saída y(t) para um degrau unitário aplicado em r(t).


  

### Exercício 13.13


  Projete um regulador linear quadrático para o motor de corrente contínua do Exercício 13.12, cujas equações de estados na forma canônica controlável são


   [img:Illustration] 


  Adotar as mesmas especificações para a resposta transitória:


  • sobressinal máximo Mp = 4% ;


  • tempo de pico da resposta tp = 1s ;


  • erro estacionário nulo entre a referência e a saída.


  Solução


  Para o projeto do regulador, inicialmente deve-se adotar valores para a matriz Q e para o escalar R. Como há infinitos valores que podem ser adotados para Q e R, se após o cálculo do controlador K, as especificações não forem satisfeitas, então o projeto deve ser refeito.


  Após algumas tentativas os valores de Q e R adotados no projeto são R = 0,244 e


   [img:Illustration] 


  Como o sistema tem n = 2 estados, então a matriz simétrica F = FT, solução da equação algébrica de Riccati, tem dimensão 2 × 2, ou seja,


   [img:Illustration] 


  Da equação algébrica de Riccati9 (13.160) tem-se que


   [img:Illustration] 


  ou seja,


   [img:Illustration] 


  Simplificando a Equação (13.474), obtém-se


   [img:Illustration] 


  Resolvendo o sistema (13.475), a única solução definida positiva da equação de Riccati é


   [img:Illustration] 


  cujos autovalores positivos são 0,5473 e 32,5974.


  Portanto, da Equação (13.159) obtém-se o vetor K para realimentação dos estados, ou seja,


   [img:Illustration] 


  Note que para a matriz Q e o escalar R adotados, o vetor K obtido em (13.477) é o mesmo obtido em (13.463) no Exercício 13.12 pelo método de alocação de polos de malha fechada.


  Consequentemente, o gráfico da resposta transitória também é o mesmo da Figura 13.33. É importante lembrar a inclusão do ganho k1, no diagrama de blocos da Figura 13.32, para se obter erro estacionário nulo entre a referência r(t) e a saída y(t).


  Apesar do projeto do regulador ser aparentemente trabalhoso, por resultar de um processo iterativo de escolha das matrizes Q e R, uma grande vantagem com relação ao projeto por alocação de polos de malha fechada é que o projeto do regulador possui a propriedade de robutez, que resulta num sistema com margem de ganho infinita e margem de fase de pelo menos 60°.


  

### Exercício 13.14


  Supondo que a medida da velocidade angular do eixo do motor não está disponível para realimentação, projetar um observador ou estimador de estados para o sistema do exercício 13.13 e analisar a resposta transitória da saída y(t).


  Solução


  Para o projeto do observador, inicialmente deve-se adotar valores para a matriz Q e para o escalar R. Como há infinitos valores que podem ser adotados para Q e R, se após o cálculo do observador, as especificações não forem satisfeitas, então o projeto deve ser refeito.


  Após algumas tentativas os valores de Q e R adotados no projeto são R = 0,01 e


   [img:Illustration] 


  Como o sistema tem n = 2 estados, então a matriz simétrica F = FT , solução da equação algébrica de Riccati, tem dimensão 2 × 2, ou seja,


   [img:Illustration] 


  Da equação algébrica de Riccati (13.192) tem-se que


   [img:Illustration] 


  ou seja,


   [img:Illustration] 


  Simplificando a Equação (13.481), obtém-se


   [img:Illustration] 


  Resolvendo o sistema (13.482), a única solução definida positiva da equação de Riccati é


   [img:Illustration] 


  cujos autovalores positivos são 1,0001 e 0,4987.


  Portanto, da Equação (13.191) obtém-se o vetor L, ou seja,


   [img:Illustration] 


  Na Figura 13.34 é apresentado o diagrama de blocos do sistema em malha fechada, considerando o conjunto controlador+observador e a planta.


   [img:Illustration] 


  Figura 13.34 Diagrama de blocos do sistema em malha fechada.


  A função de transferência do conjunto controlador+observador é dada pela Equação (13.220), ou seja,


   [img:Illustration] 


  Considerando as matrizes A, B, C e o vetor K do Exercício 13.13, tem-se que


   [img:Illustration] 


  cuja matriz inversa é


   [img:Illustration] 


  Logo, a função de transferência do conjunto controlador+observador é


   [img:Illustration] 


  A função de transferência do motor é


   [img:Illustration] 


  Logo, a função de transferência de malha aberta é


   [img:Illustration] 


  Portanto, a função de transferência de malha fechada resulta como


   [img:Illustration] 


  Observe que a função de transferência (13.491) possui um polo em s ≅ –100 que está bem distante dos polos complexos conjugados e que dessa forma tem pouca influência na resposta transitória. Por esta razão, apenas os polos complexos conjugados dominantes influenciam significativamente na resposta, fazendo com que o transitório tenha um comportamento muito próximo da resposta de um sistema de segunda ordem. Como os polos complexos conjugados dominantes são os mesmos que foram especificados no projeto por alocação de polos do Exercício 13.12, a resposta transitória da saída y(t) deve ter um sobressinal Mp ≅ 4% e um tempo de pico tp = 1s, quando for aplicado um degrau unitário na referência r(t), conforme é mostrado na Figura 13.35.


   [img:Illustration] 


  Figura 13.35 Resposta transitória da saída y(t) para um degrau unitário aplicado na referência.


  Note que na Figura 13.35 a resposta transitória do sistema controlado com observador é muito próxima da resposta do sistema controlado sem observador. É importante destacar que isso somente foi possível após um procedimento de tentativa e erro na atribuição de valores para Q e R no cálculo do vetor K e para Q e R no cálculo do vetor L. Por outro lado, a inclusão do observador normalmente produz uma degradação no desempenho, como por exemplo, aumento do sobressinal e do tempo de acomodação.


  

### Exercício 13.15


  O esquema de um sistema de levitação eletromagnética é apresentado na Figura 13.36. O sistema consiste em um eletroímã que suspende uma massa de material magnético. A levitação da massa é conseguida através do controle da distância y(t) existente entre a massa e a bobina do eletroímã. Na bobina é instalado um sensor que mede a posição y(t) da massa. A partir dessa medida um sistema de controle calcula uma tensão u(t) a ser aplicada na entrada de um circuito de potência que, por sua vez, gera uma corrente i(t) a ser aplicada na bobina. A função de transferência linear do sistema é dada por


   [img:Illustration] 


  com Kp = 10(A/V) e Ks = 0,1 (V/mm).


  Supondo que a medida da velocidade da massa não está disponível para realimentação, projete um controlador RLQ com observador de estados tal que:


  • o erro de regime permanente e(t) seja nulo quando é aplicado um degrau na referência r(t);


  • o sobressinal da resposta transitória da saída y(t) seja menor que 30%.


   [img:Illustration] 


  Figura 13.36 Sistema de levitação eletromagnética.


  Solução


  O projeto do controlador RLQ é desenvolvido a partir de um modelo de variáveis de estado. Assim, o primeiro passo é obter uma realização de estados na forma canônica controlável para a função de transferência (13.492). Como o numerador da função de transferência é KpKs = 1, não é necessário separá-la em dois blocos, podendo-se escrever diretamente que


   [img:Illustration] 


  Aplicando a transformada inversa de Laplace e isolando a derivada de maior ordem na Equação (13.493), resulta


   [img:Illustration] 


  Definindo as variáveis de estado


   [img:Illustration] 


  resulta o sistema de equações


   [img:Illustration] 


  Portanto, as equações de estados na forma canônica controlável são


   [img:Illustration] 


  Como a planta não possui integrador (polo em s = 0) e considerando a especificação de erro de regime permanente nulo para sinal de referência do tipo degrau, deve-se forçar que o controlador possua um integrador. Para isso devem ser utilizadas nos projetos do controlador e do observador as matrizes da planta estendida, dadas por


   [img:Illustration] 


  Substituindo as matrizes A, B e C nas Equações (13.499) e (13.500), obtém-se


   [img:Illustration] 


  A nova variável de estado xi(t) das Equações (13.501) e (13.502) representa a saída u(t) do integrador acrescentado na malha de controle, que fica com a configuração da Figura 13.37.


   [img:Illustration] 


  Figura 13.37 Diagrama de blocos mostrando a inclusão do integrador na entrada do levitador eletromagnético.


  A partir das matrizes Ae, Be e Ce da planta estendida, o próximo passo é determinar o vetor de ganhos K do regulador linear quadrático. Para determinar o vetor de ganhos K deve-se seguir o procedimento da Seção 13.12.2, resolvendo a equação de Riccati10


   [img:Illustration] 


  Após algumas tentativas os valores de Q e R adotados no projeto RLQ são R = 1 e


   [img:Illustration] 


  cuja solução da equação de Riccati (13.503) é


   [img:Illustration] 


  Da Equação (13.159) obtém-se o vetor K, ou seja,


   [img:Illustration] 


  Como a medida da velocidade x2(t) da massa não está disponível para realimentação, é necessário projetar um observador ou estimador de estados. Para determinar o vetor de ganhos L do observador deve-se seguir o procedimento da Seção 13.13.3, resolvendo a equação de Riccati


   [img:Illustration] 


  Após algumas tentativas os valores de Q e R adotados no projeto observador são R = 0,001 e


   [img:Illustration] 


  cuja solução da equação de Riccati (13.507) é


   [img:Illustration] 


  Da Equação (13.191) obtém-se o vetor L, ou seja,


   [img:Illustration] 


  Conforme a Seção 13.14, a função de transferência correspondente ao controlador RLQ com observador é dada por


   [img:Illustration] 


  Assim, a função de transferência final para implementação do controlador, incluindo o integrador, é


   [img:Illustration] 


  É interessante notar neste exemplo, que o conjunto controlador+observador resultou com um zero em s = –1 que cancela o polo estável da planta. Com isso, a função de transferência de malha aberta pode ser simplificada para


   [img:Illustration] 


  A resposta transitória da saída y(t) para um degrau unitário aplicado na referência r(t) com o sistema em malha fechada é mostrada na Figura 13.38. Conforme especificado, essa resposta apresenta um sobressinal menor que 30% e erro de regime nulo.


   [img:Illustration] 


  Figura 13.38 Resposta transitória da saída y(t) para um degrau unitário aplicado na referência.


  

### Exercício 13.16


  Considere o mesmo sistema de levitação eletromagnética do Exercício 13.15. Projete um controlador RLQ com observador de estados supondo que o modelo do sistema é representado por variáveis discretas de estado. Adote as mesmas especificações de projeto e um período de amostragem T = 0,01 s.


  Solução


  O modelo do sistema, representado por variáveis discretas de estado, pode ser obtido a partir das equações de estados (13.497) e (13.498) do sistema contínuo. As matrizes Ad e Bd são calculadas a partir das Equações (13.243), (13.244) e (13.245).


  Considerando um período de amostragem T = 0,01 s na Equação (13.244), tem-se que


   [img:Illustration] 


  Substituindo a Equação (13.515) nas Equações (13.243) e (13.245), obtém-se


   [img:Illustration] 


  Portanto, as equações de estados do sistema discreto para T = 0,01 s resultam como


   [img:Illustration] 


  Como a planta não possui integrador e considerando a especificação de erro de regime permanente nulo para sinal de referência do tipo degrau, devem ser utilizadas nos projetos do controlador e do observador as matrizes da planta estendida. Das Equações (13.362) e (13.363) têm-se que


   [img:Illustration] 


  ou seja,


   [img:Illustration] 


  A nova variável de estado xi[(k+1)T] representa a saída u(kT) do integrador incluído na malha de controle, conforme é representado na Figura 13.39.


   [img:Illustration] 


  Figura 13.39 Diagrama de blocos mostrando a inclusão do integrador na entrada do levitador eletromagnético.


  A partir das matrizes Ae, Be e Ce da planta estendida, o próximo passo é determinar o vetor de ganhos K do regulador linear quadrático. Para isso, deve-se adotar valores para a matriz Q e para o escalar R. Como há infinitos valores que podem ser adotados para Q e R, se ao final do cálculo do vetor K o controlador não atender às especificações, então o projeto deve ser refeito. Após algumas tentativas são adotados R = 0,0001 e


   [img:Illustration] 


  Executando o algoritmo da Tabela 13.4 para N = 1000 repetições, obtém-se a solução da equação algébrica discreta de Riccati


   [img:Illustration] 


  e o vetor de ganhos


   [img:Illustration] 


  Para o cálculo do vetor L do observador de estados, devem-se adotar valores para a matriz Q e para o escalar R. Como no projeto do regulador, há infinitos valores que podem ser adotados para Q e R. Também neste caso, se as especificações não forem satisfeitas após o cálculo do vetor L, o projeto deve ser refeito. Após algumas tentativas são adotados R = 1 e


   [img:Illustration] 


  Executando o algoritmo da Tabela 13.6 para N = 1000 repetições, obtém-se a solução da equação algébrica discreta de Riccati


   [img:Illustration] 


  e o vetor de ganhos


   [img:Illustration] 


  Das Equações (13.351) e (13.352) obtêm-se as equações de estados da malha fechada


   [img:Illustration] 


  ou seja,


   [img:Illustration] 


  Na Figura 13.40 é apresentado o gráfico da resposta transitória da saída y(kT) quando é aplicado um degrau unitário na referência r(kT) do sistema em malha fechada formado pelas Equações (13.532) e (13.533). Conforme especificado, essa resposta apresenta um sobressinal menor que 30% e erro de regime nulo.


   [img:Illustration] 


  Figura 13.40 Resposta transitória da saída y(kT) para um degrau unitário aplicado na referência.


  Comparando o gráfico da Figura 13.40, obtido a partir do projeto do modelo discreto, com o gráfico da Figura 13.38, obtido a partir do projeto do modelo contínuo, verifica-se que os resultados são semelhantes, embora outras escolhas para as matrizes Q e Q e para os escalares R e R possam produzir resultados muito distintos.


  

### 13.20 Exercícios propostos


  

### Exercício 13.17


  Determine as equações de estados que representam o circuito elétrico RC da Figura 13.41. Suponha que a entrada do circuito é a tensão ve(t) e que a saída é a tensão vs(t). São dados: R1 = 1000Ω, R2 = 250Ω, C1 = 1mF e C2 = 2mF.


   [img:Illustration] 


  Figura 13.41 Circuito elétrico RC.


  

### Exercício 13.18


  Determine as equações de estados que representam um motor de corrente contínua controlado pela armadura, esquematizado na Figura 13.42. Suponha que a entrada é a tensão de armadura ea(t) e que a saída é a posição angular do eixo θ(t).


   [img:Illustration] 


  Figura 13.42 Esquema de um motor de corrente contínua controlado por armadura.


  As variáveis e constantes indicadas na Figura 13.42 são:


  ea(t): tensão de armadura;


  ia(t): corrente de armadura;


  Ra: resistência de armadura;


  La: indutância de armadura;


  ic(t): corrente de campo do motor;


  τ (t): torque do motor;


  θ(t): posição angular do eixo;


  B: coeficiente de atrito;


  J: inércia do conjunto formado pelo rotor do motor e pela carga mecânica;


  Kt: constante de proporcionalidade entre o conjugado motor e a corrente de armadura;


  Kv : constante de proporcionalidade entre a força contraeletromotriz gerada pela armadura em rotação e a velocidade angular do eixo.


  

### Exercício 13.19


  Determine as equações de estados que representam o circuito elétrico da Figura 13.43. Suponha que a entrada do circuito é a tensão v(t) e que a saída é a corrente iR(t) no resistor.


   [img:Illustration] 


  Figura 13.43 Circuito elétrico.


  

### Exercício 13.20


  Determine as equações de estados que representam o circuito eletrônico com amplificadores operacionais da Figura 13.44. Suponha que a entrada do circuito é a tensão u(t) e que a saída é a tensão y(t). São dados: R1 = 1000Ω, R2 = 250Ω, C1 = 1mF e C2 = 2mF.


   [img:Illustration] 


  Figura 13.44 Circuito eletrônico com amplificadores operacionais.


  

### Exercício 13.21


  Um sistema é representado pelas equações de estados


   [img:Illustration] 


  a) Verifique se o sistema é estável ou instável.


  b) Verifique se o sistema é controlável e observável.


  c) Determine a função de transferência do sistema.


  

### Exercício 13.22


  Determine as equações de estados que representam o circuito eletrônico com amplificadores operacionais da Figura 13.45. Suponha que a entrada do circuito é a tensão u(t) e que a saída é a tensão y(t). São dados: R = 1000Ω, R1 = 100Ω, R2 = 20Ω, R3 = 2,5Ω e C = 1mF.


   [img:Illustration] 


  Figura 13.45 Circuito eletrônico com amplificadores operacionais.


  

### Exercício 13.23


  Um processo com entrada u(t) e saída y(t) é representado pela função de transferência


   [img:Illustration] 


  Represente o sistema nas formas canônicas controlável e observável.


  

### Exercício 13.24


  Um processo é representado pelas equações de estados


   [img:Illustration] 


  a) Verifique se o sistema é estável ou instável.


  b) Verifique se o sistema é controlável e observável.


  c) Determine a função de transferência do sistema.


  d) Represente o sistema na forma canônica controlável por meio de uma transformação de similaridade.


  

### Exercício 13.25


  Um sistema é representado pelas equações de estados


   [img:Illustration] 


  Projete um controlador K = [ k1 k2 k3 ] por realimentação de estados de modo que os polos de malha fechada estejam localizados em s = –1 + j, s = –1 –j e s = –10.


  

### Exercício 13.26


  Um sistema é representado pelas equações de estados


   [img:Illustration] 


  Projete um controlador K = [ k1 k2 ] por realimentação de estados de modo que os polos de malha fechada tenham frequência natural ωn =  [img:Illustration]  (rad/s) e coeficiente de amortecimento  [img:Illustration] 


  

### Exercício 13.27


  Considere um oscilador não amortecido, composto pelo sistema massa-mola da Figura 13.46, na qual a saída y(t) indica a posição da massa M, km é a constante da mola e f(t) representa a força externa aplicada à massa.


   [img:Illustration] 


  Figura 13.46 Sistema massa-mola.


  Supondo M = 1kg e km = 1N/m, projete um controlador K = [ k1 k2 ] por realimentação de estados de modo que os polos de malha fechada estejam localizados em s = –1 + j e s = –1 – j.


  

### Exercício 13.28


  Considere o levitador eletromagnético da Figura 13.36, cuja função de transferência linear é dada por


   [img:Illustration] 


  Supondo que os estados estão disponíveis e que podem ser medidos para realimentação, projete um controlador K = [ k1 k2 ] por alocação de polos de malha fechada, de modo que a resposta transitória da saída y(t), quando é aplicado um degrau na referência, apresente:


  • sobressinal máximo Mp = 16,3% e


  • tempo de acomodação ts = 1s pelo critério de 5%.


  

### Exercício 13.29


  Considere uma planta composta de um duplo integrador com função de transferência dada por


   [img:Illustration] 


  Supondo que os estados estão disponíveis e que podem ser medidos para realimentação, projete um controlador K = [ k1 k2 ] por alocação de polos de malha fechada, de modo que a resposta transitória da saída y(t), quando é aplicado um degrau na referência, apresente:


  • coeficiente de amortecimento ξ = 0,5 ;


  • frequência natural ωn = 4 (rad/s) ;


  • erro estacionário nulo entre a referência e a saída.


  

### Exercício 13.30


  Refaça o Exercício 13.29, projetando um controlador do tipo RLQ.


  Suponha que os estados estão disponíveis e que podem ser medidos para realimentação.


  

### Exercício 13.31


  Refaça o Exercício 13.29, projetando um controlador do tipo RLQ com observador de estados.


  Suponha que os estados não estão disponíveis para realimentação.


  

### Exercício 13.32


  Considere uma planta, cuja função de transferência é dada por


   [img:Illustration] 


  Projete um controlador RLQ com observador de estados de modo que a resposta transitória da saída y(t), quando é aplicado um degrau na referência, apresente:


  • sobressinal máximo menor que 20%;


  • erro estacionário nulo entre a referência e a saída.


  

### Exercício 13.33


  Supondo um periodo de amostragem T = 0,1s, obtenha uma representação no espaço de estados discretos para as plantas com as seguintes funções de transferência:


   [img:Illustration] 


  

### Exercício 13.34


  Determine se o sistema discreto, representado pelas equações de estados (13.546) e (13.547), é estável ou instável.


   [img:Illustration] 


  

### Exercício 13.35


  Determine a função de transferência discreta G(z) = Y(z)/U(z), correspondente às equações de estados (13.546) e (13.547).


  

### Exercício 13.36


  Considere o sistema discreto do Exercício 13.34 com um período de amostragem T = 0,1 s. Supondo que os estados estão disponíveis para realimentação, projete um controlador K = [ k1 k2 ] por alocação de polos de malha fechada no plano z, de modo que a resposta transitória da saída, quando é aplicado um degrau na referência, apresente:


  • sobressinal máximo Mp ≅ 16,3%, isto é, com coeficiente de amortecimento ξ = 0,5;


  • tempo de pico tp ≅ 0,9 s, ou seja, com frequência natural ωn = 4 (rad/s);


  • erro estacionário nulo entre a referência e a saída.


  

### Exercício 13.37


  Refaça o Exercício 13.36, projetando um controlador do tipo RLQ.


  Suponha que os estados estão disponíveis para realimentação.


  

### Exercício 13.38


  Refaça o Exercício 13.36, projetando um controlador do tipo RLQ com observador de estados.


  Suponha que os estados não estão disponíveis para realimentação.


  

### Exercício 13.39


  Considere o sistema discreto representado pelas equações de estados (13.548) e (13.549).


   [img:Illustration] 


  Supondo um período de amostragem T = 0,1 s, projete um controlador RLQ com observador de estados, de modo que a resposta transitória da saída quando é aplicado um degrau na referência apresente:


  • sobressinal máximo Mp ≤ 20%;


  • erro estacionário nulo entre a referência e a saída.


  


  __________


  1Para maior simplicidade de notação, em algumas equações a variável tempo não será explicitada em alguns pontos do capítulo.


  2Para demonstração destas condições ver [35].


  3A matriz Q é simétrica quando ela é igual à sua transposta, isto é, Q = QT. Todos os autovalores de matrizes reais simétricas são reais. Q é semidefinida positiva quando todos os seus autovalores são maiores ou iguais a zero.


  4Um sistema é estabilizável se e somente se os modos não controláveis são estáveis.


  5Um sistema é detectável se e somente se os modos não observáveis são estáveis.


  6Para resolver a equação algébrica de Riccati é recomendável a utilização de programas computacionais como os aplicativos MATLAB ou OCTAVE.


  7Um sistema é chamado do tipo n quando possui n polos na origem.


  8A solução do problema do Regulador Linear Quadrático é um tópico complexo, que foge ao escopo deste texto. Para maiores detalhes ver [26].


  9Para resolver a equação algébrica de Riccati é recomendável a utilização de programas computacionais como os aplicativos MATLAB ou OCTAVE.


  10Para resolver a equação algébrica de Riccati é recomendável a utilização de programas computacionais como os aplicativos MATLAB ou OCTAVE.



<!-- Text/bm01.xhtml -->





  Controle Automático, 2ª edição
  
  
  



  

## Bibliografia


  [1] ARMELLINI, F. Projeto e implementação do controle de posição de uma antena de radar meteorológico através de servomecanismos. 2006. 123f. Dissertação (Mestrado em Engenharia Mecânica). Escola Politécnica da Universidade de São Paulo, São Paulo.


  [2] ASTROM, K. J.; WITTENMARK, B. Computter controlled systems: theory and design. New Jersey: Prentice-Hall, 1984.


  [3] BEQUETTE, B. W. Process control: modeling, design and simulation. New Jersey: Prentice-Hall, 2003.


  [4] BITTAR, A.; SALES, R. M. H2 and H∞ control for maglev vehicles. IEEE Control Systems Magazine, 1998, v. 18, pp. 18-25.


  [5] BODE, H. W. Network analysis and feedback amplifier design. New York: D. Van Nostrand, 1945.


  [6] BUCKLEY, P. S. et al. Design of distillation column control systems. New York: ISA, 1985.


  [7] CAMPOS, M. C. M. M.; TEIXEIRA, H. C. G. Controles típicos de equipamentos e processos industriais. São Paulo: Edgard Blücher, 2006.


  [8] CANNON Jr, R. H. Dynamics of physical systems. New York: McGraw-Hill, 1967.


  [9] CASTRUCCI, P. B. L. Controle automático: teoria e projeto. São Paulo: Edgard Blücher, 1969.


  [10] CASTRUCCI, P. B. L.; BATISTA, L. Controle linear: método básico. São Paulo: Edgard Blücher, 1980.


  [11] CASTRUCCI, P. B. L.; CURTI, R. Sistemas não-lineares. São Paulo: Edgard Blücher, 1981.


  [12] CASTRUCCI, P. B. L.; SALES, R. M. Controle digital. São Paulo: Edgard Blücher, 1990.


  [13] CHEN, C. T. Analog and digital control system design: transfer-function, state-space and algebraic methods. New York: Saunders College Publishing, 1993.


  [14] CHEN, C. T. Linear system theory and design. New York: Rinehart and Winston, 1984.


  [15] CHEN, C. T.; SEO, B. The inward approach in the design of control systems. IEEE Transactions on Education, 1990, v. 33, pp. 270-278.


  [16] CHESTNUT, H.; MAYER, R. W. Servomechanisms and regulating systems design. New York: John Wiley, 1951, v. 1.


  [17] COUGHANOWR, D. R.; KOPPEL, L. B. Análise e controle de processos. Rio de Janeiro: Guanabara Dois, 1978.


  [18] CRUZ, J. J. Controle robusto multivariável. São Paulo: EDUSP, 1996.


  [19] D’AZZO, J. J.; HOUPIS, C. H. Análise e projeto de sistemas de controle lineares. Rio de Janeiro: Guanabara Dois, 1984.


  [20] DISTEFANO, J. J. et al. Sistemas de retroação e controle, com aplicações para engenharia, física e biologia. São Paulo: McGraw-Hill, 1972.


  [21] DORF, R. C.; BISHOP, R. H. Sistemas de controle modernos. Rio de Janeiro: LTC, 2001.


  [22] EVANS, W. R. Graphical analysis of control systems. AIEE Transactions, 1948, v. 67, pp. 547-551.


  [23] EVANS, W. R. Control system synthesis by root locus method. AIEE Transactions, 1950, v. 69, pp. 66-69.


  [24] EVANS, W. R. Control system dynamics. New York: McGraw-Hill, 1954.


  [25] FOULARD, C. et al. Commande et régulation par calculateur numérique. 4. ed. Paris: Eyrolles, 1984.


  [26] FRANKLIN, G. F. et al. Digital control of dynamic systems. 3. ed. California: Addison Wesley, 1998.


  [27] FRIEDLAND, B. Advanced control system design. New Jersey: Prentice Hall, 1996.


  [28] GARCIA, C. Modelagem e simulação de processos industriais e de sistemas eletromecânicos. 2. ed. São Paulo: EDUSP, 2005.


  [29] GEROMEL, J. C.; PALHARES, A. G. B. Análise linear de sistemas dinâmicos. São Paulo: Edgard Blücher, 2005.


  [30] GOODWIN, G. C. et al. Control system design. New Delhi: Prentice-Hall, 2006.


  [31] HOUPIS, C. H. et al. Quantitative feedback theory: fundamentals and applications. 2. ed. New York: Marcel Dekker, 2006.


  [32] JAMES, H. M. et al. Theory of servomechanisms. New York: McGraw-Hill, 1947.


  [33] KWAKERNAAK, H. ; SIVAN, R. Linear optimal control systems. New York: John Wiley and Sons, 1972.


  [34] KUO, B. C. Automatic control systems. 7. ed. New Jersey: Prentice Hall, 1995.


  [35] LEVINE, W. S. (Ed.). The control handbook. Florida: CRC Press, 1996.


  [36] LUYBEN, W. L. Process modeling, simulation and control for chemical engineers. 2. ed. New York: McGraw-Hill, 1990.


  [37] MARLIN, T. E. Process control: designing processes and control systems for dynamic performance. New York: McGraw-Hill, 1995.


  [38] MAYR, O. Origins of feedback control. Massachusetts: MIT Press, 1971.


  [39] MICHEL, G. Programmable logic controllers: architecture and application. Chichester: John Wiley, 1990.


  [40] MORAES, C. C.; CASTRUCCI, P. B. L. Engenharia de automação industrial. 2. ed. Rio de Janeiro: LTC, 2007.


  [41] MORARI, M.; ZAFIRIOU, E. Robust process control. New Jersey: Prentice Hall, 1989.


  [42] MORRISS, S. B. Programmable logic controllers. New Jersey: Prentice Hall, 1999.


  [43] NISE, N. S. Engenharia de sistemas de controle. 3. ed. Rio de Janeiro: LTC, 2002.


  [44] NOVAES, G. O. Modelagem e controle de velocidade e tensão de um laminador de encruamento. 2009. 203f. Dissertação (Mestrado em Engenharia Elétrica). Escola Politécnica da Universidade de São Paulo, São Paulo.


  [45] NYQUIST, H. Regeneration theory. Bell System Technical Journal, 1932, v. 11, pp. 126-147.


  [46] OGATA, K. Discrete-time control systems. 2. ed. New Jersey: Prentice Hall, 2003.


  [47] OGATA, K. Engenharia de controle moderno. 4. ed. São Paulo: Pearson, 2003.


  [48] OGATA, K. MATLAB for control engineers. New Jersey: Pearson, 2008.


  [49] OPPENHEIM, A. V.; SHAFER, R. W. Discrete-time signal processing. New Jersey: Prentice Hall, 1989.


  [50] ORSINI, L. Q.; CONSONNI, D. Curso de circuitos elétricos. São Paulo: Edgard Blücher, 2002.


  [51] PIRES, P. S. M. Introdução ao SCILAB-versão 3.0. Natal: Universidade Federal do Rio Grande do Norte, 2004.


  [52] SHINSKEY, F. G. Process control systems: application, design, adjustment. 2. ed. New York: McGraw-Hill, 1979.


  [53] SKOGESTAD, S. Simple analytic rules for model reduction and PID controller tuning. Journal of Process Control, 2003, v. 13, pp. 291-309.


  [54] SKOGESTAD, S.; POSTLETHWAITE, I. Multivariable feedback control: analysis and design. 2. ed. Chichester: John Wiley, 2005.


  [55] SMITH, C. A.; CORRIPIO, A. B. Principles and practice of automatic process control. 3. ed. New York: John Wiley, 2005.


  [56] ZIEGLER, J. G.; NICHOLS, N. B. Optimum settings for automatic controllers. ASME, 1942, v. 64, pp 759-768.



<!-- Text/fm03.xhtml -->





  Controle Automático, 2ª edição
  
  
  



  

## Material Suplementar


  Este livro conta com o seguinte material suplementar:


  
    ■ Ilustrações da obra em formato de apresentação (restrito a docentes).

  


  O acesso ao material suplementar é gratuito. Basta que o leitor se cadastre em nosso site (www.grupogen.com.br), faça seu login e clique em GEN-IO, no menu superior do lado direito. É rápido e fácil.


  Caso haja alguma mudança no sistema ou dificuldade de acesso, entre em contato conosco (gendigital@grupogen.com.br).


   


   


   [img:Illustration] 


