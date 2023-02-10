#1. Se desea llenar una lista con 10 animales, y le han pedido a usted que sabe programar que les ayude para solicitar esos 10 nombres, mostrarlos ordenados alfabeticamente
#luego solicitar al usuario un numero entre 1 y el 10 y que le permita ver cuales animales se encuentra entre el numero dicho y el final de la lista. Tambien cree una
#opcion que permita al usuario ingresar el nombre de un animal y verificar si ese animal se encuentra en la lista.

'''bandera = True
bandera1, bandera2, bandera3 = False, False, False
listaAnimales = []

while bandera == True:
    opcion = int(input(''
    1. Ingresar nombre de especie del animal
    2. Mostrar listado de animales
    3. Mostrar listado de nombre de animales apartir de un número
    4. Mostrar si existe un animal en especifico dentro de la lista
    5. Salir
    
    Escoge una opcion: ''))

    match opcion:

        case 1:
            for i in range(1,11):
                nombreAnim = input(f'\t\t Digita nombre de especial del animal #{i}: ')
                nombreAnim.lower()
                listaAnimales.append(nombreAnim)
            bandera1 = True

        case 2:
            if bandera1 == True:            
                listaAnimales.sort()
                for i in listaAnimales:
                    if i == listaAnimales[0]:
                        print(f'\t\t {i}', end=", ")
                    elif i > listaAnimales[0] and i < listaAnimales[9]:
                        print(f'{i}', end = ", ")
                    elif i >= listaAnimales[9]:
                        print(f'{i}', end = ". ")
                print(" ")
                bandera2 = True
            if bandera1 != True:
                print("\t\t Realiza primero la opcion 1")

        case 3:
            if bandera1 == True and bandera2 == True:

                while bandera == True:
                    num = int(input("\t\t Digita un numero: "))
                    if num <= 0:
                        print("\t\t Error: numero ingresado igual o inferior a 0")   
                    elif num > 10:
                        print("\t\t Error: el numero ingresado es mayor a 10")                 
                    elif num > 0 and num <=10:
                        break

                for i in range(num,11):
                    if i < 9:
                        print(f'{listaAnimales[i-1]}', end= ", ")
                    elif i > 9:
                        print(f'{listaAnimales[i-1]}', end= ". ")
                bandera3 = True
            if bandera1 != True or bandera2 != True or bandera3 != True:
                print("\t\t Realiza primero la opcion 1 y despues la opcion 2")
        
        case 4:
            nomb = input("\t\t Digita la especial del animal a buscar: ")
            nomb.lower()

            for i in listaAnimales:
                if nomb == i:
                    print(f'\t\t El animal {nomb} si existe en la lista de animales')
                    break
                elif nomb != i:
                    continue

        case 5:
            print("\t\t Saliendo... Que tengas un lindo día")
            bandera = False

        case _:
            print("\t\t Error: opcion no valida")'''

#2. Dado el siguiente arreglo = [1,0,2,4,8,5,7,6,8,7,5,6,4,3,1,9,2], dar la opcion al usuario de indicar uin numero a buscar y mostrar la posicion en que se encuentra
# un numero por primera vez y por ultima vez dentro del arreglo.

'''arreglo = [1,0,2,4,8,5,7,6,8,7,5,6,4,3,1,9,2]
bandera = True

max = max(arreglo)
min = min(arreglo)

while bandera == True:
    num = int(input("Digita un numero: "))
    if num < min or num > max:
        print(f'\t Error: el valor ingresa no esta en los rangos de {min} a {max}')  

    elif num >= min and num <= max:
        bandera = False

for i in range(0, len(arreglo)):
    if num == arreglo[i]:
        print(f'\t El numero {num} se encuentra por primera vez en la posicion {i}')

for i in range(len(arreglo)-1, -1, -1):
    if num == arreglo[i]:
        print(f'\t El numero {num} se encuentra por ultima vez en la posicion {i}')'''
        

    


    




