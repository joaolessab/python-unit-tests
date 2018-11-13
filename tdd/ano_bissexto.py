def e_bissexto(valor):
    return valor % 400 == 0 or (valor % 4 == 0 and valor % 100 != 0)