def comparar_llistes(llista1,llista2):
    l=[]
    for p,e in enumerate(llista1):
        if e in llista2:
            if e==llista2[p]:
                l.append(2)
            else:
                l.append(1)
        else:
            l.append(0)
    return l