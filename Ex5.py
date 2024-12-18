def llegir_llista_paraules():
    l=[]
    while True:
        p=input("Introdueix una paraula: ")
        if p==".":
            break
        else:
            l.append(p)
    return l