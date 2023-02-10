#3. La escuela, PequeñosGamberros, quiere almacenar los datos de sus N estudiantes: Nombre, Curso, Genero. Quiere tambien registrar las notas de las 3 materias de 
#esos estudiantes. Luego imprimir el nombre de los estudiantes con el promedio de sus notas y mostrar quienes aprobaron y quenes no. Un estudiante aprueba, si el promedio
#de sus notas es >= 3.5. Debe tenerse en cuenta que las notas deben estar entre 0 y 5.

'''bandera = True
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
        print(f'El estudiante {i["Nombre"]} obtuvo un primedio de notas de {promedio}, NO APROBO')'''


#2. Por teclado se ingresa el valor hora de N cantidad de empleados. Posteriormente se ingresa el nombre del empleado, la antiguedad y la cantidad de horas trabajadas en el mes.
#Se pide calcular el importe a cobrar teniendo en cuenta que al total que resulta de multiplicar el valor hora por la cantidad de horas trabajadas, hay que sumarle la cantidad 
#de años trabajados multiplicados por $30 y al total de todas esas operaciones restarle el 13% en concepto de descuentos. 
#Imprimir el recibo correspondiente con el nombre, antiguedad, valor hora, total a cobrar en bruto, total de descuento y valor neto a cobrar.

'''bandera = True
valorHora = 4800
listado = []

NumEmpleados = int(input("Digita la cantidad de empleados: "))
print("")

for i in range(NumEmpleados):
    listado.append({})
    nombreEmpleado = input("Digita el nombre del empleado: ")
    listado[i]["nombre empleado"] = nombreEmpleado
    antiguedad = int(input(f'Digita el tiempo en años de antiguedad de {nombreEmpleado} en la empresa: '))
    while bandera == True:
        if antiguedad <= 0:
            print("\t\tError: El numero ingresado no es valido")
        elif antiguedad > 0:
            listado[i]["antiguedad"] = antiguedad
            break
    cantHoras = int(input(f'Digita la cantidad de horas mensuales trabadas de {nombreEmpleado}: '))
    while bandera == True:
        if cantHoras <= 0 or cantHoras > 300:
            print("\t\tError: no esta en el rango de la cantidad de horas establecidas")
        elif cantHoras > 0 and cantHoras <= 200:
            listado[i]["cantidad horas"] = cantHoras
            break
        
    valorHorasTrabajadas = cantHoras * valorHora
    valorAñosTrabajados = antiguedad * 30
    importe = valorHorasTrabajadas + valorAñosTrabajados
    descuento = round((importe * 0.13),2)
    listado[i]["valor horas trabajadas"] = valorHorasTrabajadas
    listado[i]["valor años trabajados"] = valorAñosTrabajados
    listado[i]["importe"] = importe
    listado[i]["descuento"] = descuento

print("")
print(f'Nombre \t\tAntiguedad \tValor Hora \tTotal bruto \tTotal descuento \tValor a cobrar')

for i in listado:
    print(f'{i["nombre empleado"]} \t\t{i["antiguedad"]} \t\t{valorHora} \t\t{i["importe"]} \t\t{i["descuento"]} \t\t{i["importe"]+ i["descuento"]}')'''
    
    

