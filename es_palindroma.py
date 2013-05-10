def es_palindroma(palabra):
    lista_palabra=list(palabra)
    lista_palabra_alreves=lista_palabra[-1::-1]
    if lista_palabra==lista_palabra_alreves:
        return True
    else:
        return False
