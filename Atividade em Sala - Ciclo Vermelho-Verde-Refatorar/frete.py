def calcular_frete(modalidade, peso_kg):
    if peso_kg < 0:
        raise ValueError("peso não pode ser negativo")
    if modalidade == "padrao":
        return 10.00 + 2.00 * peso_kg
    elif modalidade == "expresso":
        return 20.00 + 3.50 * peso_kg
    elif modalidade == "retirada":
        return 0.00
    else:
        raise ValueError(f"modalidade desconhecida: {modalidade}")
