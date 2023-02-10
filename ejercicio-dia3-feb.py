#1. Diseñar un algoritmo que almacene datos en dos vectores y luego identifique y muestre los elementos que estan en el primero y no estan en el segundo.

'''listaDatos1 = ["Julian", "Wilson", "Ronald", 6, 9, 7]
listaDatos2 = [1, 2, 3, 5, 6, 7, 8, 9, "Julian", "a", "b", "c"]
listaResultado = []

for datos1 in range(len(listaDatos1)):
    for datos2 in range(len(listaDatos2)):
        if listaDatos1[datos1] == listaDatos2[datos2]:              
            listaResultado.append(listaDatos1[datos1])

for i in listaDatos1:
    if  i in listaResultado:
        listaResultado.remove(i)
    else:
        listaResultado.append(i)

print(listaResultado)'''

#2. Dadas las siguientes ciudades y la temperatura de los proximos 5 dias. Realice un algoritmo que permita obtener la temperatura promedio, la mayor y menor de cada ciudad.
#Bogota = "19,19,17,18,20"
#Bucaramanga = "27,26,26,26,27"
#Medellin = "27,26,26,27,29"

'''Bogota = "19,19,17,18,20"
Bucaramanga = "27,26,26,26,27"
Medellin = "27,26,26,27,29"
listadoCompleto, bog, buca, mede = [], [], [], []
almacenar = ""

for temp in (Bogota, Bucaramanga, Medellin):
    for num in temp:
        if num != "," and almacenar != "":
            listadoCompleto.append(almacenar+num)
            almacenar = ""
        elif num != "," and almacenar == "":
            almacenar = num

for i in range(len(listadoCompleto)):
    if i >= 0 and i <=4:
        bog.append(listadoCompleto[i])
    elif i > 4 and i <= 9:
        buca.append(listadoCompleto[i])
    elif i > 9:
        mede.append(listadoCompleto[i])

print(listadoCompleto)
print(f'Bogota {bog} ----- la tempetaruta mayor es {max(bog)} --- la temperatura minima es {min(bog)}')
print(f'Bucaramanga {buca} ----- la tempetaruta mayor es {max(buca)} --- la temperatura minima es {min(buca)}')
print(f'Medellin {mede} ----- la temperatura mayor es {max(mede)} --- la temperatura minima es {min(mede)}')'''

#3. La escuela, PequeñosGamberros, quiere almacenar los datos de sus N estudiantes: Nombre, Curso, Genero. Quiere tambien registrar las notas de las 3 materias de 
#esos estudiantes. Luego imprimir el nombre de los estudiantes con el promedio de sus notas y mostrar quienes aprobaron y quenes no. Un estudiante aprueba, si el promedio
#de sus notas es >= 3.5. Debe tenerse en cuenta que las notas deben estar entre 0 y 5.

#Solucion #1
'''bandera = True
estudiantes = []
genero =""

numEstudent = int(input("Digita la cantidad de estudiantes: "))

for i in range(0,numEstudent):
    print("")
    estudiantes.append([])
    nombre = input(f'Ingresa el nombre del estudiante {i+1}: ')
    estudiantes[i].append(nombre)
    curso = input(f'Digita el curso al cual pertenece el estudiante {nombre}: ')
    estudiantes[i].append(curso)
    while bandera == True:
        genero = input("Ingresa F o M segun el genero del estudiante: ")
        genero.lower()
        if genero == "m" or genero == "f":            
            estudiantes[i].append(genero)
            break
        if genero != "m" or genero != "f":
            print("\t\t Debes ingresar F (femenino) o M (masculino) segun el genero del estudiante")        
    for j in range(4):
        while bandera == True:
            notas = float(input(f'Digita la calificacion de la nota #{j+1}: '))
            if notas <= 0 or notas > 5:
                print("\t\t Error: la nota ingresada no esta en el rango de 0.0 a 5.0")   
            elif notas > 0 and notas <=5:
                break
        estudiantes[i].append(notas)

for i in estudiantes:
    suma, promedio = 0, 0
    for j in range(len(i)):
        if j >= 3:
            suma = suma+i[j]
            promedio = suma/4
    if promedio >= 3.5:
        print(f'El estudiante {i[0]} obtuvo un promedio de notas de {promedio}, APROBO')
    elif promedio < 3.5:
        print(f'El estudiante {i[0]} obtuvo un primedio de notas de {promedio}, NO APROBO')'''
        
#Solucion #2 Diccionarios

bandera = True
estudiantes = []

numEstudent = int(input("Digita la cantidad de estudiantes: "))

for i in range(numEstudent):
    print("")
    estudiantes.append({})
    estudiantes[i]["Nombre"] = input(f'Ingresa el nombre del estudiante {i+1}: ')
    estudiantes[i]["Curso"] = input(f'\tDigita el curso al cual pertenece el estudiante {estudiantes[i]["Nombre"]}: ')
    while bandera == True:
        genero = input("\tIngresa F o M segun el genero del estudiante: ")
        genero.lower()
        if genero == "m" or genero == "f":            
            estudiantes[i]["Genero"] = genero
            break
        if genero != "m" or genero != "f":
            print("\t\t Debes ingresar F (femenino) o M (masculino) segun el genero del estudiante") 
    estudiantes[i]["Notas"] = []       
    for j in range(3):
         while bandera == True:
            notas = float(input(f'\tDigita la calificacion de la nota #{j+1}: '))
            if notas <= 0 or notas > 5:
                print("\t\t Error: la nota ingresada no esta en el rango de 0.0 a 5.0")   
            elif notas > 0 and notas <=5:
                estudiantes[i]["Notas"].append(notas)
                break
print(estudiantes)
print("")
for i in estudiantes:
    suma, promedio = 0, 0
    for j in i["Notas"]:
        suma = suma+j
        promedio = suma/3
    if promedio >= 3.5:
        print(f'El estudiante {i["Nombre"]} obtuvo un promedio de notas de {promedio}, APROBO')
    elif promedio < 3.5:
        print(f'El estudiante {i["Nombre"]} obtuvo un primedio de notas de {promedio}, NO APROBO')

