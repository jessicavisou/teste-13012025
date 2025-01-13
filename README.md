<p style="text-align:center" dir="auto">
  <a href="#desafio1">Desafio 1</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="#desafio2">Desafio 2</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>

<h2 id="desafio1" style="text-align:center;border-bottom:none">Desafio 1</h2>

Uma empresa de assinatura de energia deseja criar uma calculadora de economia para seu site e contratou você para desenvolver essa solução. Como requisito, foi estabelecido que a aplicação deve ser desenvolvida utilizando a linguagem Python.

### Sua aplicação receberá as seguintes entradas:

- Três valores representando o consumo de energia elétrica dos últimos 3 meses
- Valor da tarifa da distribuidora
- Tipo de tarifa (Comercial, Residencial e Industrial)

### Os resultados da sua aplicação serão:

- Economia Anual
- Economia Mensal
- Desconto Aplicado
- Cobertura

#### A empresa de assinatura de energia te forneceu as seguintes premissas para o desconto:

| Consumo (Média) | Desconto (Residencial) | Desconto (Comercial) | Desconto (Industrial) |
| --- | --- | --- | --- |
| < 10.000 kWh | 18% | 16% | 12% |
| >= 10.000 kWh e <= 20.000 kWh | 22% | 18% | 15% |
| > 20.000 kWh | 25% | 22% | 18% |

#### Alem disso, deve-se considerar os seguintes percentuais de cobertura baseado no consumo:

| Consumo (Média) - kWh | < 10.000 kWh | >= 10.000 kWh e <= 20.000 kWh | > 20.000 kWh |
| --- | --- | --- | --- |
| Cobertura*** | 90% | 95% | 99% |

*** Cobertura é o valor da energia que o consumidor irá receber da empresa de assinatura de energia em relação à energia consumida

<h2 id="desafio2" style="text-align:center;border-bottom:none">Desafio 2</h2>

Para tornar a aplicação mais versátil e de ampla aplicabilidade, foi solicitado que a tarifa não seja mais uma entrada fixa. Agora, a tarifa deve ser obtida automaticamente a partir do <a href="https://www.cemig.com.br/atendimento/valores-de-tarifas-e-servicos/" target="_blank">site da CEMIG</a>. Com base na classe de consumo e na bandeira tarifária, será possível determinar a tarifa que será utilizada pela calculadora.

Portanto, desenvolva um código de web scraping que obtenha a tarifa diretamente do site e integre essa funcionalidade à calculadora criada no Desafio 1. Certifique-se de que a tarifa capturada seja corretamente utilizada nos cálculos.

### Requisitos dos Desafios:
1. A linguagem Python deverá ser utilizada para o desenvolvimento das soluções;
2. A calculadora deve ser implementada nos arquivos calculadora_desafio1.py e calculadora_desafio2.py, especificamente dentro da função calculadora();
3. Todos os testes contidos nos dois arquivos devem ser executados sem apresentar erros;
4. No Desafio 2, a escolha de bibliotecas e ferramentas para web scraping é livre, contanto que sejam implementadas em Python;
5. Inclua neste mesmo README uma seção detalhada que explique claramente os passos necessários para executar o código. Certifique-se de que as instruções sejam precisas, organizadas e fáceis de entender, pois os avaliadores seguirão essa documentação;
6. A entrega deve ser realizada dentro do prazo estabelecido;
7. O candidato deve fazer um fork do repositório. A entrega pode ser realizada por meio de um pull request para o repositório original (o que será considerado um diferencial) ou enviando o link do seu repositório para o e-mail lucas@dg.energy.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Desafio 1:
Tecnologias Utilizadas
Python 3.x
Funções de Cálculo Matemático
Funcionalidade
A aplicação recebe como entradas:
O consumo médio dos últimos três meses (em kWh).
O valor da tarifa da distribuidora de energia.
A classe do consumidor (Residencial, Comercial ou Industrial).
Com essas entradas, o sistema calcula os seguintes resultados:
Economia Anual: Economia no valor total de energia anual (em R$).
Economia Mensal: Economia no valor total mensal (em R$).
Desconto Aplicado: O percentual de desconto aplicado com base na classe de consumo e faixa de consumo.
Cobertura: Percentual de cobertura, ou seja, a energia fornecida pela empresa em relação ao consumo.
Deu um erro, acredito que de arredondamento nos calculos, então não bateram conforme o esperado

Desafio 2:
Tecnologias Utilizadas
Python 3.x
Requests: Biblioteca para realizar requisições HTTP.
BeautifulSoup (bs4): Biblioteca para análise de HTML e extração de dados de páginas web.
Funcionalidade
A tarifa agora é obtida a partir do site da CEMIG, onde uma tabela contém as tarifas para diferentes classes de consumo e bandeiras tarifárias. A função realiza um web scraping para capturar esses valores e os utiliza nos cálculos da calculadora.

A aplicação acessa o site da CEMIG.
Faz a busca pela classe de consumo e pela bandeira tarifária.
A tarifa correspondente é extraída da tabela de preços.
Com a tarifa obtida, a calculadora do Desafio 1 é chamada para calcular os resultados.
Função para Obter a Tarifa:

def obter_tarifa(classe: str, bandeira: str) -> float:
  
Exemplos de Execução:
Primeiro, a função obter_tarifa() busca a tarifa da CEMIG com base na classe e bandeira:


tarifa = obter_tarifa("Industrial", "BANDEIRA VERMELHA 2")
Com a tarifa obtida, o código então pode chamar a função calculadora() para realizar os cálculos:


resultado = calculadora([1518, 1071, 968], "Industrial", tarifa)
print(resultado)
Como Executar
Desafio 1: O código funciona com entradas fixas de tarifa fornecidas pelo usuário.
Desafio 2: A tarifa é obtida automaticamente da página da CEMIG com base na classe e bandeira.
Passos para Execução
Instalar as dependências:
requests e beautifulsoup4
Rodar o script para calcular a economia. Ao rodar, os testes serão executados automaticamente e o resultado será exibido.
Não foi encontrado nas tabelas da cemig a tarifa para grupos especificados no exercicio