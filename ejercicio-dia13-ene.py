#1)Desarrolle un algoritmo que permita leer tres valores y almacenarlos en las variables num1, num2, num3 respectivamente. El algoritmo debe imprimir cual es el mayor
#Recuerde constatar que los tres valores introducidos por el teclado seam valores distintos.

'''print("Recuerda que los tres valores introducidos deben ser diferentes")
num1 = float(input("Digite el primer valor: "))
num2 = float(input("Digite el segundo valor: "))

if num1 != num2:
    num3 = float(input("Digite el tercer valor: "))
    if num3 != num1 and num3 != num2:
        if num1 > num2 and num1 > num3:
            print(f'El numero mayor es el primer numero {num1}')
        elif num2 > num1 and num2 > num3:
            print(f'El numero mayor es el segundo numero {num2}')
        elif num3 > num1 and num3 > num2:
            print(f'El numero mayor es el tercer numero {num3}')
else:
    print("El numero introducido debe ser diferente")'''

#2) Se pide leer tres notas del estudiante y calcular su definitiva en un rango de 0-5 y mostrar un mensaje donde diga su el estudiante aprobo o reprobo. Para que un
#estudiante apruebe debe haber obtenido un promedio de 3.0 en adelante. Si alguna nota esta fuera del rango indicar que hay un error.

'''nota1 = float(input("Digite la primer nota: "))
nota2 = float(input("Digite la segunda nota: "))
nota3 = float(input("Digite la tercer nota: "))

if nota1<=5.0 and nota1>0 and nota2<=5.0 and nota2>0 and nota3<=5.0 and nota3>0:    
    definitiva = (nota1 + nota2 + nota3)/3
    if definitiva >= 3:
        print("El estudiante APROBO")
    elif definitiva < 3:
        print("El estudiando REPROBO")
else:
    print("La calificacion no esta en el rango de 0 a 5")'''

#3) Dados dos numeros enteros, se desea saber su alguno de ellos es multiplo del otro.

'''num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))

#Solucion1
if num1 > num2:
    division1 = num1%num2
    if division1 == 0:
        print(f'El numero {num1} es multiplo de {num2}')
    elif division1 != 0:
        print("Los numeros no son multiplos")
elif num2 > num1:
    division2 = num2%num1
    if division2 == 0:
        print(f'El numero {num2} es multiplo de {num1}')
    elif division2 != 0:
        print("Los numeros no son multiplos")'''

'''#solucion2
if num1%num2 or num2%num1:
    print("Los numeros son multiplos")
else:
    print(f'el numero {num1} y {num2} no son multiplos')'''

#4) En la universidad Buena Nota se requiere un algoritmo para calcular la nota definitiva y decidir si el estudiante aprueba o reprueba la asignatura. 
# La nota final se obtiene a partir de dos notas parciales y un examen final, donde el primer parcial equivale al 30%, el segundo parcial al 30% y el 
# examen final al 40%, y la nota mínima aprobatoria es 3.0.
#Si el promedio de los dos parciales es menor a 2.0, el estudiante no puede presentar examen final y pierde la materia por bajo promedio, en este caso 
# la nota definitiva es el promedio de los parciales, si el promedio es igual o superior a 2.0 puede presentar el examen final.
#Si la nota del examen final es inferior a 2.0, se desconoce (no se toma en cuenta) las notas de los parciales y la nota definitiva es la obtenida 
# en el examen final. Si la nota es igual o superior a 2.0 se calcula la nota definitiva aplicando los porcentajes mencionados a los parciales y al final.
#Si la nota definitiva es igual o superior a 3.0 el estudiante aprueba la asignatura; si es inferior a 3.0 pierde la materia; sin embargo, puede habilitarla, 
# siempre y cuando en el examen final obtenga nota mayor o igual a 2.0, en este caso la nota definitiva será la que obtenga en la habilitación.

'''parcial1 = float(input("Digite la nota del primer parcial: "))
parcial2 = float(input("Digite la nota del segundo parcial: "))

sumaParcial = (parcial1 + parcial2)/2
if sumaParcial < 2.0:
    print(f'La nota definitiva es {round((sumaParcial),2)}, REPROBO')
elif sumaParcial >= 2.0:
    examenFinal = float(input("Digite la nota del examen final: "))
    if examenFinal < 2.0:
        print(f'La nota definitiva es {round((examenFinal),2)}, REPROBO')
    elif examenFinal >= 2.0:
        definivita = (parcial1*0.30)+(parcial2*0.30)+(examenFinal*0.40)
        print(f'La nota definitiva es {round((definivita),2)}')
        if definivita < 3.0:
            habilitacion = float(input("Digite la nota de la habilitacion: "))
            print(f'La nota definitiva es {round((habilitacion),2)}')'''

#5) Leer 3 numeros enteros diferentes y ordenarlos de menor a mayor

num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el tercer numero: "))

#opcion 1
if num1 < num2 and num1 < num3:
    if num2 > num1 and num2 < num3:
        print(f'{num1}, {num2}, {num3}')
    elif num2 > num1 and num2 > num3:
        print(f'{num1}, {num3}, {num2}')
elif num1 > num2 and num1 > num3:
    if num2 < num1 and num2 < num3:
        print(f'{num2}, {num3}, {num1}')
    elif num2 < num1 and num2 > num3:
        print(f'{num3}, {num2}, {num1}')    
elif num3 < num1 and num3 < num2:
    if num1 < num2:
        print(f'{num3}, {num1}, {num2}')
elif num2 < num1 and num1 < num3:
        print(f'{num2}, {num1}, {num3}')



