#1)Calcular el perimetro y el area de un rectangulo dada su base y su altura

'''base = float(input("Digita la base del rectangulo: "))
altura = float(input("Digita la altura del rectangulo: "))

perimetro = 2*base + 2*altura
area = base * altura
print(" ")
print("El perimetro del rectangulo es :", perimetro)
print("El area del rectangulo es :", area)'''

#2) Escribir un programa que convierta un valor dado en grados Farenheit a grados celsius. Recordar que al formula para la concersion es:
# c = (F -32)*5 / 9

'''Farenheit = float(input("Digite el valor de los grados Farenheit: "))

c = (Farenheit-32)*5/9

print(" ")
print("El valor en Celsius es: ", round(c,2),"°")'''

#3) Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto debera pagar finalmente por su compra

'''vcompra = float(input("Ingrese el valor de la compra: "))

vdescuento = (vcompra * -0.15)
vtotal = (vcompra - vdescuento)

print (" ")
print (f'El valor a pagar es ${vtotal} y obtuvo un descuento de ${vdescuento}')'''

#4) Un estudiante desea saber cual será su calificación final en la materia de algoritmos. Dicha calificacion se compone de los siguientes porcentajes:
#55% del promedio de sus tres calificaciones parciales.
#30% de la calificacion del examen final
#15% de la calificaion de un trabajo final

'''nota1 = float(input("Ingrese la nota de la primera calificación parcial: "))
nota2 = float(input("Ingrese la nota de la segunda calificación parcial: "))
nota3 = float(input("Ingrese la nota de la tercera calificación parcial: "))
examenFinal = float(input("Ingrese la nota del examen final: "))
trabajoFinal = float(input("Ingrese la nota del trabajo final: "))

promedioNotas = (nota1 + nota2 + nota3) / 3 * 0.55
calificacionFinal = promedioNotas + (examenFinal*0.30) + (trabajoFinal*0.15)

print(" ")
print("La calificacion final del estudiante es: ", round(calificacionFinal,3))
print(" ")'''

#5) Una persona recibe un préstamo de U$10.000 de un banco y desea saber cuanto pagara de interes, en un mes si el banco le cobra una tasa del 27% anual.

'''valorPrestamo = float(input("Ingrese el valor del prestamo a recibir: "))

valorMes = (valorPrestamo * 0.27) / 12

print(" ")
print("El valor mensual a pagar por el prestamo es de: ", valorMes)
print(" ")'''

#6) Calcular el porcentaje de niños y niñas en un aula

'''Mujeres = int(input("Ingresar el valor de mujeres en el aula: "))
Hombres = int(input("Ingrese el valor de hombres en el aula: "))

sumatoria = Mujeres + Hombres
porcentajeMujeres = Mujeres*100/sumatoria
porcentajeHombres = Hombres*100/sumatoria

print("")
print(f'El porcentaje de mujeres es {round(porcentajeMujeres,2)}% y el porcentaje de hombres es {round(porcentajeHombres,2)}%')'''

#7) Calcular el monto a pagar en una cabina de internet si el costo por hora es de 1500 y por cada 5 horas te dan una hora de promocion gratis, sabiendo que la permanencia en la cabina fueron de 12 horas

permanencia = int(input("Ingrese la cantidad de horas que jugo: "))

descuento = permanencia//5
valorPagar = (permanencia - descuento) * 1500


print ("")
print("El valor total a pagar es de: ", valorPagar)