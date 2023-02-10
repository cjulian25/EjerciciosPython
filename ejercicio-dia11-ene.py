#1) Pepe tiene dos hijos, uno tiene 20 años y el otro tiene 22. Si PepeJunior es 2 años mayor que Agripino entonces PepeJunior es el mayor,
#de lo contrario si Agripino tiene 2 años que PepeJunior Agripino es mayor, en caso que no se cumplan ninguna de las condiciones no son hijos de Pepe

'''pepeJunior = int(input("Cuantos años tiene PepeJunior?: "))
agripino = int(input("Cuantos años tiene Agripino?: "))

if pepeJunior > agripino and pepeJunior-agripino==2:
    print("PepeJunior es el mayor")
elif agripino > pepeJunior and agripino-pepeJunior==2:
    print("Agripino es el mayor")
else:
    print("No son los hijos de Pepe")'''

#2) La empresa La Generosa S.A desea aumentar el sueldo de sus empleados, para ello ha estrablecido las siguientes condiciones: 
#quienes ganan hasta 800mil tendran un incremento del 10%, quienes devengan mas de 800mil y hasta 1millon 200mil recibiran un aumento del 8% y los demas del 5%.
#Se requiere un algoritmo que calcule el valor del aumento y el nuevo salario para cada empleado.

'''salario= int(input("Ingrese el valor del sueldo del empleado: "))

if salario<= 800000 and salario > 0:
    print(f"El aumento del sueldo es del 10% para un total de {round((salario*1.10),2)}")
elif salario > 800000 and salario <= 1200000:
    print(f"El aumento del sueldo es del 8% para un total de {round((salario*1.08),2)}")
else:
    print(f"El aumento del sueldo es del 5% para un total de {round((salario*1.05),2)}")'''


#3) Se requiere un algoritmo que decida si un empleado tiene derecho al auxilio de transporte. Se conoce que todos los empleados que devengan un salario menor o igual
# a dos salarios minimos legales tienen derechgo a este rubro.

'''salario = int(input("Ingrese el sueldo correspondiente: "))

if salario > 2320000:
    print("No tienes derecho al auxilio de transporte")
else:
    print(f"Tiene derecho al auxilio de transporte por valor de $140.606 para un total de salario de {salario+140606} ")'''

#4) Realizar una calculadora de operaciones aritmetcias basicas (+,-,*,/) usando el match con dos valores

'''val1 = float(input("Digita el primer valor: "))
val2 = float(input("Digita el segundo valor: "))
operacion = int(input(''1. Suma         ##Agregarle una ' extra para que sean 3
2. Resta 
3. Multiplicacion 
4. Division
Escoge una opcion: ''))         ##Agregarle una ' extra para que sean 3

match operacion:
    case 1:
        print(val1+val2)
    case 2:
        print(val1-val2)
    case 3:
        print(val1*val2)
    case 4:
        if val1 == 0 or val2 ==0:
            print("No es posible dividir por 0")
        else:
            print(val1/val2)
    case _:
        print("La opcion no es valida")'''

#4) Se requiere aplicar un subsidio para el cobro del alumbrado publico en la factura de los clientes. El subsidio se aplicara segun el estrado.
#Para estrato 1; sera el 10%, para estrato 2 el 8%, para estrato 3 el 6%, para estrato 4 el 4%.
#Realice un algoritmo que segun el estrato determine el subsidio a aplicar y muestre el valor a pagar para el cliente.

consumoMes = int(input("Ingrese el valor de la factura del cliente: "))
operacion = int(input('''1. Estrato 1
2. Estrato 2
3. Estrato 3
4. Estrato 4
Selecciona el estrato al cual pertenece el cliente: '''))

match operacion:
    case 1:
        print(f'El valor total a pagar es {(consumoMes)-(consumoMes*0.10)}')
    case 2:
        print(f'El valor total a pagar es {(consumoMes)-(consumoMes*0.08)}')
    case 3:
        print(f'El valor total a pagar es {(consumoMes)-(consumoMes*0.06)}')
    case 4:
        print(f'El valor total a pagar es {(consumoMes)-(consumoMes*0.04)}')
    case _:
        print("No aplica para subsidio")