import requests
from bs4 import BeautifulSoup


def obter_tarifa(classe: str, bandeira: str) -> float:
    url = "https://www.cemig.com.br/atendimento/valores-de-tarifas-e-servicos/"  

  
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Erro ao acessar o site da CEMIG: {response.status_code}")


    soup = BeautifulSoup(response.text, "html.parser")

    # Encontrando a tabela com as tarifas
    tabela = soup.find("table", {"class": "table table-bordered"}) 
    if not tabela:
        raise Exception("Tabela de tarifas não encontrada.")

    # Encontrando as linhas da tabela
    linhas = tabela.find_all("tr")
    if not linhas:
        raise Exception("Linhas da tabela não foram encontradas.")

    # Obtendo os cabeçalhos da tabela
    cabecalhos = linhas[0].find_all("th")
    colunas_bandeiras = [cabeçalho.text.strip() for cabeçalho in cabecalhos]

    # Verificando se a bandeira está entre os cabeçalhos
    if bandeira not in colunas_bandeiras:
        raise Exception(f"Bandeira {bandeira} não encontrada entre os cabeçalhos.")

    # Encontrando o índice da coluna correspondente à bandeira
    indice_bandeira = colunas_bandeiras.index(bandeira)  # Pega o índice da coluna que corresponde à bandeira

    # Mapeando as colunas da tabela (ignorando cabeçalhos)
    for linha in linhas[1:]: 
        colunas = linha.find_all("td")
        if len(colunas) > 0:
            # Verificar o nome da classe na primeira coluna
            nome_classe = colunas[0].text.strip()

            # Se a classe corresponder, pegar o valor da tarifa na coluna correspondente
            if nome_classe == classe:
                tarifa = colunas[indice_bandeira].text.strip()

                # Convertendo o valor da tarifa para float
                try:
                    return float(tarifa.replace(",", "."))
                except ValueError:
                    raise Exception(f"Erro ao converter tarifa para número: {tarifa}")

    raise Exception(f"Classe {classe} com {bandeira} não encontrada.")

# Função principal da calculadora
def calculadora(consumo: list, classe: str, bandeira: str) -> tuple:
    """
    Retorna uma tupla de floats contendo economia anual, economia mensal, desconto aplicado e cobertura.
    """
    # Obtendo a tarifa com base na classe e bandeira
    tarifa = obter_tarifa(classe, bandeira)

    # Calculando o consumo médio
    consumo_medio = sum(consumo) / len(consumo)

    # Determinando o desconto aplicado com base na classe e consumo
    if classe == "Residencial":
        if consumo_medio < 10000:
            desconto_aplicado = 0.18
        elif consumo_medio <= 20000:
            desconto_aplicado = 0.22
        else:
            desconto_aplicado = 0.25
    elif classe == "Comercial":
        if consumo_medio < 10000:
            desconto_aplicado = 0.16
        elif consumo_medio <= 20000:
            desconto_aplicado = 0.18
        else:
            desconto_aplicado = 0.22
    elif classe == "Industrial":
        if consumo_medio < 10000:
            desconto_aplicado = 0.12
        elif consumo_medio <= 20000:
            desconto_aplicado = 0.15
        else:
            desconto_aplicado = 0.18

    # Determinando a cobertura com base no consumo
    if consumo_medio < 10000:
        cobertura = 0.90
    elif consumo_medio <= 20000:
        cobertura = 0.95
    else:
        cobertura = 0.99

    # Calculando o consumo total e valores
    consumo_total_sem_desconto = consumo_medio * tarifa
    valor_pago = consumo_total_sem_desconto * (1 - desconto_aplicado)
    economia_mensal = consumo_total_sem_desconto - valor_pago
    economia_anual = economia_mensal * 12

    return (
        round(economia_anual, 2),
        round(economia_mensal, 2),
        round(desconto_aplicado, 2),
        round(cobertura, 2),
    )



if __name__ == "__main__":
    print("Testando...")

    
    assert calculadora([1518, 1071, 968], "Industrial", "BANDEIRA VERMELHA 2") == (
        1349.86,
        112.49,
        0.12,
        0.90,
    )

    assert calculadora([1000, 1054, 1100], "Residencial", "BANDEIRA VERMELHA 1") == (
        1725.61,
        143.8,
        0.18,
        0.90,
    )

    assert calculadora([973, 629, 726], "Comercial", "BANDEIRA AMARELA") == (
        1097.6,
        91.47,
        0.16,
        0.90,
    )

    assert calculadora([15000, 14000, 16000], "Industrial", "BANDEIRA VERMELHA 1") == (
        21656.81,
        1804.73,
        0.15,
        0.95,
    )

    assert calculadora([12000, 11000, 11400], "Residencial", "BANDEIRA VERDE") == (
        22997.8,
        1916.48,
        0.22,
        0.95,
    )

    assert calculadora([17500, 16000, 16400], "Comercial", "BANDEIRA AMARELA") == (
        27938.08,
        2328.17,
        0.18,
        0.95,
    )

    assert calculadora([30000, 29000, 29500], "Industrial", "BANDEIRA VERMELHA 1") == (
        53262.07,
        4438.51,
        0.18,
        0.99,
    )

    assert calculadora([22000, 21000, 21400], "Residencial", "BANDEIRA AMARELA") == (
        52186.84,
        4348.9,
        0.25,
        0.99,
    )

    assert calculadora([25500, 23000, 21400], "Comercial", "BANDEIRA VERDE") == (
        48697.35,
        4058.11,
        0.22,
        0.99,
    )

    print("Todos os testes passaram!")
