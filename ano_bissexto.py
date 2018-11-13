def e_bissexto(valor):

    if valor is None:
        raise ValueError("Valor nao fornecido")
        
    if valor % 400 != 0 and valor % 100 == 0:
        return False
    elif valor % 4 != 0:
        return False

    return True