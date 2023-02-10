#1) Escribir un algoritmo que encuentre y despliegue los numeros primos entre uno y cien. Un numero primo es divisible entre si mismo y la unidad por lo tanto
# un numero primo no puede ser par excepto el dos

'''for i in range(1,101,1):
    contador = 0
    for j in range(1,i+1):
        if i%j == 0:
            contador +=1
    if contador == 2:
        print(i, end= ", ")'''

#2) Diseñar un programa que nos permita realizar las siguientes tareas:
#1. Ingresar el nombre del estudiante
#2. Ingresar las notas del estudiante (5 notas)
#3. Mostrar la nota definivita de un estudiante
#4. Mostrar si el estudiante aprueba o no la materia
#5. Mostrar el nombre del estudiante, la nota definitiva y si aprobo o no la materia.
#6. Salir

opcion = 0
bandera1 = False
bandera2 = False
bandera3 = False
bandera4 = False
acumulador = 0

while opcion != 6:
    opcion = int(input('''
    1. Ingresar el nombre del estudiante
    2. Ingresar las notas del estudiante (5 notas)
    3. Mostrar la nota definivita de un estudiante
    4. Mostrar si el estudiante aprueba o no la materia
    5. Mostrar el nombre del estudiante, la nota definitiva y si aprobo o no la materia.
    6. Salir

    Escoge una opcion: '''))
    print(" ")

    match opcion:
        case 1:
            nombre = input("Ingrese el nombre del estudiante: ")
            bandera1 = True
        case 2:
            if bandera1 == True:
                for i in range(5):
                    nota =-1
                    while nota<0 or nota>5:
                        nota = float(input(f'Digita la nota {i+1}: '))    
                    acumulador +=nota  
                bandera2 = True         
            else:
                print("Primero debes realizar el paso 1")
        case 3:
            if bandera1 == True and bandera2 == True: 
                definitiva = acumulador/5               
                print(f'La nota definivita del estudiante es: {definitiva}')
                bandera3 = True
            else:
                print("Primero debes realizar el paso 1 y el paso 2")
        case 4:
            if bandera1 == True and bandera2 == True and bandera3 == True:
                if definitiva >= 3.5:
                    print("Aprobo")
                    estado = "Aprobo"
                else:
                    print("Reprobo")
                    estado = "Reprobo"
                bandera4 == True
            else:
                print("Primero debes realizar el paso 1, el paso 2 y el paso 3")
        case 5:
            if bandera1 == True and bandera2 == True and bandera3 == True and bandera4 == True:
                print(f'Nombre {nombre}, Definitiva: {definitiva} y es Estado {estado}')
            else:
                print("Primero debes realizar el paso 1, el paso 2, el paso 3 y el paso 4")
        case 6:
            break
        case _:
            print("Error: La opcion no es valida")