def calculadora(consumo: list, tarifa: float, classe: str) -> tuple:
    """
    Retorna uma tupla de floats contendo economia anual, economia mensal, desconto aplicado e cobertura.
    """
    economia_anual = 0
    economia_mensal = 0
    desconto_aplicado = 0
    cobertura = 0
    
    consumo_medio = sum(consumo) / len(consumo)  # Média do consumo
    
    # Definindo o desconto de acordo com a classe e o consumo médio
    if classe == "Residencial":
        if consumo_medio < 10000:
            desconto_aplicado = 0.18  # 18% de desconto para consumo < 10.000 kWh
        elif 10000 <= consumo_medio <= 20000:
            desconto_aplicado = 0.22  # 22% de desconto para consumo entre 10.000 e 20.000 kWh
        else:
            desconto_aplicado = 0.25  # 25% de desconto para consumo > 20.000 kWh
    elif classe == "Comercial":
        if consumo_medio < 10000:
            desconto_aplicado = 0.16  # 16% de desconto para consumo < 10.000 kWh
        elif 10000 <= consumo_medio <= 20000:
            desconto_aplicado = 0.18  # 18% de desconto para consumo entre 10.000 e 20.000 kWh
        else:
            desconto_aplicado = 0.22  # 22% de desconto para consumo > 20.000 kWh
    elif classe == "Industrial":
        if consumo_medio < 10000:
            desconto_aplicado = 0.12  # 12% de desconto para consumo < 10.000 kWh
        elif 10000 <= consumo_medio <= 20000:
            desconto_aplicado = 0.15  # 15% de desconto para consumo entre 10.000 e 20.000 kWh
        else:
            desconto_aplicado = 0.18  # 18% de desconto para consumo > 20.000 kWh
    
    # Calculando a cobertura com base no consumo médio
    if consumo_medio < 10000:
        cobertura = 0.90  # Cobertura de 90% para consumo < 10.000 kWh
    elif 10000 <= consumo_medio <= 20000:
        cobertura = 0.95  # Cobertura de 95% para consumo entre 10.000 e 20.000 kWh
    else:
        cobertura = 0.99  # Cobertura de 99% para consumo > 20.000 kWh
    
    # Calculando o valor total de consumo sem desconto
    consumo_total_sem_desconto = consumo_medio * tarifa
    
    # Aplicando o desconto para calcular o valor pago
    valor_pago = consumo_total_sem_desconto * (1 - desconto_aplicado)
    
    # A economia mensal é a diferença entre o valor total e o valor pago
    economia_mensal = consumo_total_sem_desconto - valor_pago
    
    # A economia anual é 12 vezes a economia mensal
    economia_anual = economia_mensal * 12

    # Arredondando os valores para 2 casas decimais
    return (
        round(economia_anual, 2),
        round(economia_mensal, 2),
        round(desconto_aplicado, 2),
        round(cobertura, 2),
    )

# Teste
if __name__ == "__main__":
    print("Testando...")

    resultado = calculadora([1518, 1071, 968], 0.878460, "Industrial")
    print(f"Resultado calculado: {resultado}")
    assert resultado == (
        1349.86,  # Economia Anual
        112.49,   # Economia Mensal
        0.12,     # Desconto aplicado
        0.90      # Cobertura
    )  # BANDEIRA VERMELHA 2

    assert calculadora([1000, 1054, 1100], 0.84432, "Residencial") == (
        1725.61,
        143.8,
        0.18,
        0.90
    )  # BANDEIRA VERMELHA 1

    assert calculadora([973, 629, 726], 0.818540, "Comercial") == (
        1097.6,
        91.47,
        0.16,
        0.90
    )  # BANDEIRA AMARELA

    assert calculadora([15000, 14000, 16000], 0.844320, "Industrial") == (
        21656.81,
        1804.73,
        0.15,
        0.95
    )  # BANDEIRA VERMELHA 1

    assert calculadora([12000, 11000, 11400], 0.79969, "Residencial") == (
        22997.8,
        1916.48,
        0.22,
        0.95
    )  # BANDEIRA VERDE

    assert calculadora([17500, 16000, 16400], 0.818540, "Comercial") == (
        27938.08,
        2328.17,
        0.18,
        0.95
    )  # BANDEIRA AMARELA

    assert calculadora([30000, 29000, 29500], 0.844320, "Industrial") == (
        53262.07,
        4438.51,
        0.18,
        0.99
    )  # BANDEIRA VERMELHA 1

    assert calculadora([22000, 21000, 21400], 0.81854, "Residencial") == (
        52186.84,
        4348.9,
        0.25,
        0.99
    )  # BANDEIRA AMARELA

    assert calculadora([25500, 23000, 21400], 0.799669, "Comercial") == (
        48697.35,
        4058.11,
        0.22,
        0.99
    )  # BANDEIRA VERDE

    print("Todos os testes passaram!")
    