#1) Realizar un programa que acumule (sume) valores ingresados por teclado hasta ingresar el 9999 (no sumar dicho valor, solamente indica que ha finalizado la carga)
# Imprimir el valor acumulado e informar si dicho valor es cero, mayor a cero o menor a cero.

'''num = 0
suma = 0

while num != 9999:
    num = int(input("Digite un numero: "))
    if num != 9999:
        suma = num+suma
if suma == 0:
    print(f'El valor acumulado es {suma}')
elif suma > 0:
    print(f'El valor acumulado es mayor a cero: {suma}')
elif suma < 0:
    print(f'El valor acumulado es menor a cero: {suma}')'''

#2) Algoritmo que lea numeros enteros hasta teclear 0, y nos muestre el maximo, el minimo y la media (promedio) de todos ellos.

'''num = ""
num2 = 0
suma = 0
contador = 0
mayor = -9999999999999
menor = 9999999999999

if num != 0:
    while num != 0:
        num = int(input("Digita un numero: "))
        if num != 0:
            suma += num
            contador +=1
            num2 = num
            if num2 > mayor:
                mayor = num2
            elif num2 < menor and num2 != 0:
                menor = num2            
if num == 0:
    print(f'El numero mayor es: {mayor}, el numero menor es : {menor}, el promedio es {round((suma/contador),2)}')
    print(f'contador: {contador}')'''

#3) Mostrar los numeros del 1 al 100 (ambos incluidos) divisibles entre 2 y 3.

'''for i in range(1,101,1):
    if i%2 == 0 and i%3 == 0:
        print(i, end=", ")'''

#4) Se desea validar una clave que sea 123456 hasta en tres oportunidades, debe indicar cuantos intentos lleva y cuantos le restan.

'''contadorR = 3
contadorS = 0

for i in range(1,4,1):
        num = str(input("Digita la clave: "))
        if i < 4:
            contadorS += 1
            contadorR -= 1
            if num == "123456":
                print("Login...")  
                break
            if num != "123456":
                print(f'Intentos realizados: {contadorS}, le quedan {contadorR} intentos')'''
        