import provedor_conteudo

def contar_caracter():
    conteudo = provedor_conteudo.obter()   
     
    return len(conteudo)

"""def contar_arquivo():
    arquivo = open('teste.txt')

    tamanho = len(arquivo.read())

    return tamanho"""