def calcular_frete(valor_carrinho, regiao):

    if valor_carrinho <= 0:
        raise ValueError("Valor de carrinho inválido")

    if regiao == "Norte":
        limite_frete_gratis = 300.0
    else:
        limite_frete_gratis = 200.0

    if valor_carrinho >= limite_frete_gratis:
        return 0.0

    return 20.0