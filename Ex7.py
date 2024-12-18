import random
def crear_llista_num_aletoris():
    l=[]
    for i in range(5):
        l.append(random.randint(1,100))
    return l