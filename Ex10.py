def menu():
    print("1- llegir llista de enters")
    print("2- llista de senars")
    print("3- sumar llista de parells")
    print("4- cercar numero de la llista")
    print("5- llegir llista de paraules")
    print("6- crear paraula de la llista")
    print("7- crear llista de numeros aletoris")
    print("8- comparar llistes")
    print("9- majors d'edat")
    print("10-sortir")
    while True:
    
        o=int(input("Introdueix una opció: "))
        match o:
            case 1:
                llegir_llista_enters()
            case 2:
                print(senars_llista([1,2,3,4,5,6,7,8,9]))
            case 3:
                print(sumar_parells_llista([1,2,3,4,5,6,7,8,9]))
            case 4:
                print(cercar_numero_llista([1,2,3,4,5,6,7,8,9],5))
            case 5:
                llegir_llista_paraules()
            case 6:
                print(crear_paraula_llista(["hola","adios","fea","pablo","juan"]))
            case 7:
                print(crear_llista_num_aletoris())
            case 8:
                print(comparar_llistes([1,6,3,7,8],[9,4,3,1,8]))
            case 9:
                print(majors_edat(15,21))
            case 10:
                break

menu()