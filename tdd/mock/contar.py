def contar_arquivo():
    arquivo = open('teste.txt')

    tamanho = len(arquivo.read())

    return tamanho