def llegir_llista_enters():
    l=[]
    while True:
        n=input("Introdueix un element: ")
        if n==".":
            break
        else:
            l.append(int(n))
    return l