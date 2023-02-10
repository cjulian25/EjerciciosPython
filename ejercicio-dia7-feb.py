#1. Un profesor de matematica de un establecimiento educativo registra de cada alumno codigo estudiante, nombre y promedio. Segun el promedio desea saber cuantos alumnos aprobaron
#(promedio mayor o igual a 7), cuantos habilitan en diciembre(primedio menor a 7 y mayor o igual a 4) y cuantos habilitan examen en marzo( promedio menor a 4). Ademas
#desea concoer el codigo y nombre de los alumnos con mejor promedio. Realizar un programa atraves de un menu que permita realizar dichas acciones.

'''bandera, bandera1 = True, False
registroAlumnos = []

while bandera == True:
    opcion = int(input(''
1. Ingresar el registro de cada alumno
2. Mostrar cuantos alumnos aprobaron
3. Mostrar estudiantes con mejor promedio
4. Mostrar cuales estudiantes habilitan en diciembre
5. Mostrar cuales estudiantes habilitan en marzo 
6. Salir

Escoge una opcion: ''))

    match opcion:

        case 1:
            numAlumnos = int(input("\n\tDigita el numero de estudiantes que vas a ingresar: "))
            for i in range(numAlumnos):
                registroAlumnos.append({})
                registroAlumnos[i]["nombre"] = input(f'\n\tDigita el nombre del estudiante #{i+1}: ')
                registroAlumnos[i]["codigo"] = int(input(f'\tDigita el CODIGO del estudiante: '))
                registroAlumnos[i]["promedio"] = float(input(f'\tDigita el PROMEDIO del estudiante: '))
            bandera1 = True
        
        case 2:
            if bandera1 == True:
                print(f'\t\t Estudiante(s) que aprobaron')
                for i in registroAlumnos:
                    if i["promedio"] >= 7:
                        print(f'\t{i["nombre"]} con promedio de {i["promedio"]}')
            elif bandera1 == False:
                print("\n\tPrimero debes realizar la opcion 1")

        case 3:
            if bandera1 == True:
                print(f'\t\t Alumno(s) con el mejor promedio')
                listaPromedio = []
                for i in registroAlumnos:
                    listaPromedio.append(i["promedio"])
                max = max(listaPromedio)
                for i in registroAlumnos:
                    if max == i["promedio"]:
                        print(f'\n\t\t\t{i["nombre"]} con promedio de {i["promedio"]}')
            elif bandera1 == False:
                print("\n\tPrimero debes realizar la opcion 1")
        
        case 4:
            if bandera1 == True:
                print(f'\t\t Estudiante(s) que debe(n) habilitar en diciembre')
                for i in registroAlumnos:
                    if i["promedio"] >= 4 and i["promedio"] < 7:
                        print(f'\n\t\t {i["nombre"]} con promedio de {i["promedio"]}')
            elif bandera1 == False:
                print("\n\tPrimero debes realizar la opcion 1")
        
        case 5:
            if bandera1 == True:
                print(f'\t\t Estudiante(s) que debe(n) habilitar en marzo')
                for i in registroAlumnos:
                    if i["promedio"] < 4:
                        print(f'\n\t\t {i["nombre"]} con promedio de {i["promedio"]}')
            elif bandera1 == False:
                print("\n\tPrimero debes realizar la opcion 1")
        
        case 6:
            print("\n\tCerrando...\n")
            bandera = False

        case _:
            print("\t\tError: Opcion no valida")'''
    
#2. En el instituto TURBOCOEX, se tiene una cantidad N de estudiantes, de los cuales se desea registrar el nombre, codigo y nivel(Beginner, junior, senior), se debe
#averiguar quen no se creen codigos duplicados para los estudiantes que se registren. Ademas de los datos solicitados se requiere registrar 3 notas para cada estudiante.
# Se debe calcular y mostrar el promedio de las notas por cada estudiante junto con un mensaje de "aprobo" ó "reprobo" y el promedio general del grupo de estudiantes.
# Para saber si aprobo, su promedio debe ser superior o igual a 3.5 (validar las notas en un rango de 0 a 5). Se ha solicitado que usted cree un algoritmo expresado
# en pseudocodigo que cumpla con los requerimientos indicados creando un menu que permita realizar las siguientes acciones:
#1. Definir cantidad de estudiantes.
#2. Registrar datos del estudiante.
#3. Mostrar listado de estudiantes.
#4. Registrar notas de cada estudiante.
#5. Mostrar notas de cada estudiante.
#6. Acerca del Autor.
#7. Salir.

bandera = True
bandera1, bandera2, bandera3, bandera4 = False, False, False, False
registroEstudiantes = []

while bandera == True:
    
    opcion = int(input('''
1. Definir cantidad de estudiantes.
2. Registrar datos del estudiante.
3. Mostrar listado de estudiantes.
4. Registrar notas de cada estudiante.
5. Mostrar notas de cada estudiante.
6. Acerca del Autor.
7. Salir.

Escoge una opcion: '''))
    
    match opcion:

        case 1:
            numEstudiantes = int(input("\n\tDigita la cantidad de estudiantes que vas a ingresar: "))
            bandera1 = True
        
        case 2:
            if bandera1 == True:
                for i in range(numEstudiantes):
                    registroEstudiantes.append({})
                    registroEstudiantes[i]["codigo"] = int(input(f'\tDigita el CODIGO del estudiante #{i+1}: '))   
                    registroEstudiantes[i]["nombre"] = input(f'\tDigita el Nombre del estudiante #{i+1}: ')                 
                    while bandera == True:
                        registroEstudiantes[i]["nivel"] = int(input('''\tNivel:\n\t1. Beginner\n\t2. Junior\n\t3. Senior\n\tEscoge una opcion: '''))
                        if registroEstudiantes[i]["nivel"] <= 0 or registroEstudiantes[i]["nivel"] > 3:
                            print("Error: opcion invalida")
                        if registroEstudiantes[i]["nivel"] == 1:
                            registroEstudiantes[i]["nivel"] = "Beginner"
                            break
                        if registroEstudiantes[i]["nivel"] == 2:
                            registroEstudiantes[i]["nivel"] = "Junior"
                            break
                        if registroEstudiantes[i]["nivel"] == 3:
                            registroEstudiantes[i]["nivel"] = "Senior"
                            break
                    bandera2 = True
            elif bandera1 == False:
                print("\n\tPrimero debes realizar la opcion 1")

        case 3:
            if bandera1 == True and bandera2 == True:
                print("\n\tCogido \tNombre \tNivel")
                for i in registroEstudiantes:
                    print(f'\t{i["codigo"]} \t{i["nombre"]} \t{i["nivel"]}')
                bandera3 = True
            elif bandera1 == False and bandera2 == False:
                print("Primero debes realizar la opcion 1 y la opcion 2")
                    
        case 4:
            if bandera1 == True and bandera2 == True:
                for i in registroEstudiantes:
                    i["notas"] = []
                    for j in range(3):
                        while bandera == True:
                            notas = float(input(f'\tDigita la calificacion de la nota #{j+1}: '))
                            if notas <= 0 or notas > 5:
                                print("\t\t Error: la nota ingresada no esta en el rango de 0.0 a 5.0")   
                            elif notas > 0 and notas <=5:
                                i["notas"].append(notas)
                                break
                for k in registroEstudiantes:
                    sumatoria = 0
                    promedio = 0
                    for n in k["notas"]:
                        sumatoria += n
                    promedio = round((sumatoria/3),2)
                    k["promedio"] = promedio
                    if promedio >= 3.5:
                        k["estado"] = "APROBADO"
                    elif promedio < 3.5:
                        k["estado"] = "REPROBADO"        
                bandera4 = True
            elif bandera1 == False and bandera2 == False:
                print("Primero debes realizar la opcion 1 y la opcion 2")

        case 5:
            if bandera1 == True and bandera2 == True and bandera4 == True:
                print("\n\tCogido \tNombre \tNivel \tNotas \t\tPromedio \tEstado")
                for i in registroEstudiantes:
                    print(f'\t{i["codigo"]} \t{i["nombre"]} \t{i["nivel"]} \t{i["notas"]} \t{i["promedio"]} \t\t{i["estado"]}')
            elif bandera1 == False and bandera2 == False and bandera3 == False and bandera4 == False:
                print("Primero debes realizar la opcion 1, la opcion 2 y la opcion 4")

        case 6:
            print("\n\tAutor:\n\t\t Julian Carrillo")
        
        case 7:
            print("\n\t Cerrando...")
            bandera = False
        
        case _:
            print("Error: opcion no valida")




 