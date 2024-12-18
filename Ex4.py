def cercar_numero_llista(llista,numero):
    if numero in llista:
        for p,e in enumerate(llista):
            if numero==e:
                return p
    else:
        return -1