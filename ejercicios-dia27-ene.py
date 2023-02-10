#1) Mostrar el valor mas grande y mas pequeño dentro de una lista sin usar metodos o funciones

'''lista = [10, 0, 3, 61, 9, 20, 17, 8, 2, 1]

mayor, menor = lista[0], lista[0]
lista.sort()
#max = max(lista)
#min = min(lista)
respuesta = lista.index(3)

for i in lista:
    if i > mayor:
        mayor = i
    elif i < menor:
        menor = i 
print(f'El numero mayor es: {mayor}\nEl numero menor es: {menor}')
print(lista)
print(max(lista))
print(min(lista))
print(respuesta)'''

#2) Crear un programa con un menú de opciones:
#1. Ingresar el nombre de 5 estudiantes
#2. Ingresar nota de cada estudiante
#3. Mostrar la mayor nota con el nombre del estudiante
#4. Mostrar todos los estudiantes y las notas
#5. Salir

listaNombres, listaNotas, notasMax = [], [], ""
bandera1, bandera2, bandera3 = False, False, False
bandera = True

while bandera == True:

    menu = int(input('''
1. Ingresar el nombre de 5 estudiantes
2. Ingresar nota de cada estudiante
3. Mostrar la mayor nota con el nombre del estudiante
4. Mostrar todos los estudiantes y las notas
5. Salir
       
Escoge una opcion: '''))
    print("")

    match menu:

        case 1:
            for i in range (1,6):
                nombre = input(f'\t\t Digita el nombre del estudiante #{i}: ')
                listaNombres.append(nombre)
            bandera1 = True  
        case 2:
            if bandera1 == True:
                for i in listaNombres:
                    while bandera == True:
                        nota = float(input(f'\t\t Digita la nota del estudiante {i}: '))                    
                        if nota > 0 and nota <=5:
                            listaNotas.append(nota)
                            notaMayor = nota
                            break                                                      
                        elif nota < 0 or nota > 5:
                            print("\t\t Error: la nota ingresada no esta en el rango de 0.0 a 5.0")
                            continue 
                bandera2 = True
            if bandera1 == False:
                print("\t\t Realiza la opcion 1 primero")                      
        case 3:
            if bandera1 == True and bandera2 == True:
                max = max(listaNotas)
                listadoNomNot = list(zip(listaNombres, listaNotas))
                for i in listadoNomNot:
                    if i[1] == max:
                        notasMax += f'Estudiante: {i[0]} - Nota {i[1]}\n'
                print(f'Estudiante(s) con las nota(s) mas alta(s):\n{notasMax}')
                bandera3 = True
            if bandera1 != True or bandera2 != True:
                print("\t\t Realiza primero la opcion 1 y despues opcion 2")    
        case 4:
            if bandera1 == True and bandera2 == True and bandera3 == True:
                for i in listadoNomNot:                
                    print(f'\t\t Estudiante {i[0]} - nota {i[1]}')
            if bandera1 != True or bandera2 != True or bandera3 != True:
                print("\t\t Realiza primero la opcion 1 y despues opcion 2 y despues la opcion 3")  
        case 5:  
            print("\t\t Saliendo... Que tengas un lindo día")      
            bandera = False
        case _:
            print("\t\t Error: opcion no valida")




        
                        
                



