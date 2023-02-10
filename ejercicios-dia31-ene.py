#1. Sumar los valores del siguiente arreglo numeros = [33,55,77,81,48] mostrar al final del programa los numeros en forma de lista y el resultado de la suma.

'''numeros = [33,55,77,81,48]
suma = 0

for i in range(len(numeros)):
    suma += numeros[i]
    print(f'\t\t {numeros[i]}')
    if i/2 == 1:
        print(f'\t\t {numeros[i]}  +') 

print(f'\t____________\n\t\t{suma}')'''

#2. Un usuario desea ingresar al sistema y se solicita los datos de usuario y contraseña. Los datos de usuario y contraseña se encuentran almacenados en dos arreglos
#respectivamente. Verificar si el usuario y la contraseña coinciden con los que se encuentran almacenados (un usuarion tiene una contraseña que se corresponde respectivamente).
#Si ambos son correctos (La coincidencia debe ser exacta), mostrar el mensaje bienvenido. De lo contrario mostrar un mensaje indicando que hay un error.
#Dar un maximo de 3 oportunidades.

'''usuarios = ["pepito89","supermongoi", "espernancacion"]
contrasenias = ["123456", "password", "qwerty123"]
listadoDatos = list(zip(usuarios, contrasenias))

contador1, contador2 = 0, 3
bandera = True


while bandera == True:

    datoUsuario = input("\nDigita su usuario: ")
    datoUsuario.lower()
    datoContrasenia = input("Digita la contraseña: ")    
    
    for i in listadoDatos:

        if i[0] in datoUsuario and i[1] in datoContrasenia:
            print(f'\n\t\t Bienvenido {i[0]}\n')    
            bandera = False
        elif i[0] not in datoUsuario or i[1] not in datoContrasenia:
            contador1 += 1
    
    if contador1 == 3 or contador1 == 6:
        contador2 -=1
        print(f'\n\t\t Error en la validacion de los datos, te quedan {contador2} intentos\n')

    elif contador1 == 9:
        print("\n\t\t Alcanzaste el maximo de intentos\n")
        bandera = False'''

#3. Llenar una matriz de tamalo 5 filas x 10 columnas con los numeros de 1 hasta el 50 en forma automatica.

matriz = []
contador = 0

for i in range(5):    
    matriz.append([])

    for j in range(10):
        matriz[i].append(contador+j+1)
    contador += j + 1

print(f'{matriz}')





    


        

    