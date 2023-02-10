# # Calcular el perímetro y área de un rectángulo dada su base y su altura.
# base=float(input('Digita la base del rectángulo'))
# altura=float(input('Digita la altura del rectángulo'))
# area=base*altura
# perimetro=2*base+2*altura
# print(f'El área es {area} y el perímetro es {perimetro}')

# # Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:
# # C = (F-32)*5/9
# f=float(input('Digita la temperatura en Farenheit'))
# c=(f-32)*5/9
# print(f'La temperatura en Celsius es {round(c,2)}°')

# # Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.
# precio=float(input('Digita el precio de la compra'))
# pago=precio-(precio*0.15) #También podemos usar 0.85 que sería el equivalente al precio a pagar o también 15/100
# print(f'El precio a pagar será {pago}')

# # Un estudiante desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
# # 55% del promedio de sus tres calificaciones parciales.
# # 30% de la calificación del examen final.
# # 15% de la calificación de un trabajo final.
# p1=float(input('Digita nota parcial 1'))
# p2=float(input('Digita nota parcial 2'))
# p3=float(input('Digita nota parcial 3'))
# ef=float(input('Digita nota Examen Final'))
# tf=float(input('Digita nota trabajo Final'))
# promParc=(p1+p2+p3)/3*0.55
# promEf=ef*0.3
# promTf=tf*0.15
# definitiva=promParc+promEf+promTf
# print(f'La nota definitiva es {definitiva}')



# # 4.	Una persona recibe un préstamo de  10,000.00 de un banco y desea saber cuánto pagará de interés, si el banco le cobra una tasa del 27% anual.
prestamo=10000
interesMensual=27/12/100
pagoInt=prestamo*interesMensual
print(f'El valor a pagar por interes en un mes será de {pagoInt}')


# # Calcular el porcentaje de niños y niñas en un aula
# ninos=int(input('Digita la cantidad de niños'))
# ninas=int(input('Digita la cantidad de niñas'))
# total=ninos+ninas
# porcNinos=ninos*100/total
# porcNinas=ninas*100/total
# print(f'El porcenta de niños es {porcNinos}\nEl porcentaje de niñas es {porcNinas}')


# # Calcular el monto a pagar en una cabina de Internet si el costo por hora es de 1500 y por cada 5 horas te dan una hora de promoción gratis, sabiendo que la permanencia en la cabina  fueron  de 12 horas.
# cantHoras=float(input('Digita el tiempo en horas'))
# precio=1500
# horasGratis=cantHoras//5
# pago=(cantHoras-horasGratis)*precio
# print(f'El valor a pagar es {pago}')