def lista_foi_preenchida():
    lista = ["web-map1", "web-map1", "web-map1", "web-map1", "web-map1", "web-map1", "web-map1"] 
    
    if len(lista) > 0:
        return True
    return False

def lista_e_valida():
    lista = ["web", None, None, "web", "web", 3]
    return False

def lista_foi_filtrada():
    lista = ["web-map1", "web-map1", "web-map1", "web-map1", "web-map1", "web-map1", "web-map1"] 
    lista = lista[:5]
    return len(lista)