# 1. Evaluar las siguientes expresiones para A = 2, B = 5 y C=1:
'''a = 2
b = 5
c = 1
print("El valor de 3*A-4*B/A**2, es: ", 3*a-4*b/a**2)
print("El valor de (((B+C)/2*A+10)*3*B)-6, es: ", (((b+c)/2*a+10)*3*b)-6)'''

#2. Un individuo desea invertir su capital en un banco y desea saber cuánto dinero ganará después de un mes si el banco paga a razón de 1,2% mensual.
'''inversion = float(input("Ingrese el valor del capital: "))
mes = inversion * 1.012
print("El valor mensual a ganar seria: ", mes)'''

#3. Calcule el área de un triángulo y muestre su resultado.
'''base = float(input("Ingrese el valor de la base del triangulo: "))
altura = float(input("Ingrese el valor de la altura del triangulo: "))

area = base * altura / 2

print("El valor del area del triangulo es: ", area)'''

#4. Una agencia de venta de autos paga a su personal de ventas un salario de $980.000, más una comisión de $170.000 por auto vendido, más un 5% del valor de venta. Diseñar un algoritmo para calcular el salario de un vendedor en un determinado mes, conociendo el nº de automóviles vendidos y el total del monto de ventas.
'''autosVendidos = int(input("Ingrese el valor de los autos vendidos en el mes: "))
totalVentas = float(input("Ingrese el valor total de lo(s) auto(s) vendido(s): "))
salario = 980000
comision = 170000

comisionAuto = comision * autosVendidos
comisionVentas = totalVentas * 0.05
salarioVendedor = salario + comisionAuto + comisionVentas

print("El salario total del vendedor es: ", salarioVendedor)'''

#5. Hallar el promedio de calificaciones, teniendo en cuenta que el estudiante tiene 4 notas decimales; dos notas valen el 40% y las otras dos valen el 60%.
'''nota1 = int(input("Ingrese el valor de la primera nota equivalente al 40%: "))
nota2 = int(input("Ingrese el valor de la segunda nota equivalente al 40%: "))
nota3 = int(input("Ingrese el valor de la primera nota equivalente al 60%: "))
nota4 = int(input("Ingrese el valor de la segunda nota equivalente al 60%: "))

nota40 = (nota1 + nota2)/2 * 0.4
nota60 = (nota3 + nota4)/2 * 0.6
promedio = nota40 + nota60

print("El promedio de calificaciones del estudiante es: ", promedio)'''

#6. Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio, si la fórmula es: num. pulsaciones = (220 - edad)/10
'''edad = int(input("Ingrese la edad de la persona: "))

pulsaciones = (220-edad)/10

print("El numero de pulsaciones de la persona durante los 10 seg de ejercicio es: ", pulsaciones)'''

#7. Un vendedor recibe un sueldo base, más un 10% extra por comisión de sus ventas, el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres (3) ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
'''sueldoBase = float(input("Ingrese el valor del sueldo base del vendedor: "))
comisionVentas = float(input("Ingrese el valor total de las ventas del vendedor: "))

comisionTotal = comisionVentas * 0.10
sueldoTotal = sueldoBase + comisionTotal

print("El salario total del vendedor es: ", sueldoTotal)'''

#8. Un alumno desea saber cuál será su promedio general en las tres materias más difíciles que cursa y cuál será el promedio que obtendrá en cada una de ellas. Estas materias se evalúan como se muestra a continuación:
'''print("Calificacion de Matematicas")
sig1Nota1 = float(input("Ingrese la nota de la primer tarea: "))
sig1Nota2 = float(input("Ingrese la nota de la segunda tarea: "))
sig1Nota3 = float(input("Ingrese la nota de la tercer tarea: "))
sig1Examen = float(input("Ingrese la nota del examen: "))
promedioSig1 = (((sig1Nota1 + sig1Nota2 + sig1Nota3)/3)*0.10)+(sig1Examen * 0.9)
print("El primedio de la signatura de Matematicas es: ", round(promedioSig1,2))
print("")
print("Calificacion de Fisica")
sig2Nota1 = float(input("Ingrese la nota de la primer tarea: "))
sig2Nota2 = float(input("Ingrese la nota de la segunda tarea: "))
sig2Examen = float(input("Ingrese la nota del examen: "))
promedioSig2 = (((sig2Nota1 + sig2Nota2)/2)*0.20)+(sig2Examen * 0.80)
print("El promedio de la asignatura de Fisica es: ", round(promedioSig2,2))
print("")
print("Calificacion de Quimica")
sig3Nota1 = float(input("Ingrese la nota de la primer tarea: "))
sig3Nota2 = float(input("Ingrese la nota de la segunda tarea: "))
sig3Nota3 = float(input("Ingrese la nota de la tercer tarea: "))
sig3Examen = float(input("Ingrese la nota del examen: "))
promedioSig3 = (((sig3Nota1 + sig3Nota2 + sig3Nota3)/3)*0.15)+(sig3Examen * 0.85)
print("El promedio de la asignatura de Quimica es: ", round(promedioSig3,2)) 
print("")
promedioTotal = round((promedioSig1+promedioSig2+promedioSig3)/3,2)
print(f'El promedio total de las 3 asignaturas (Matematica, Fisica, Quimica) es: {round((promedioSig1+promedioSig2+promedioSig3)/3,2)}')'''