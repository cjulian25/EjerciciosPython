#1) El almacen Gran Distribuidos vende camisas al por mayor y hace descuentos segun la cantidad facturada: en cantidades superiores o iguales a 1000 unidades hace el 10%
#de descuento; entre 500 y 999 el 8%, entre 200 y 499 el 5%, y en menos de 200 no hay descuento. Dada la cantidad facturada y el precio unitario, se requiere calcular el
#descuento que se le hace a un cliente y el valor a pagar.

'''unidades = int(input("Cuantas unidades facturo?: "))
precioUnitario = int(input("Cual el precio untiario del producto?: "))
cont = 0
totalFacturado = unidades * precioUnitario 

if unidades >= 1000:
    descuento = 10
    cont = 10
elif unidades >= 500 and unidades <= 999:
    descuento = 8
    cont = 8
elif unidades >= 200 and unidades <= 499:
    descuento = 5
    cont = 5
elif unidades < 200:
    cont = 0

if cont > 1:
    print(f'Para un total de {unidades} unidades, se le aplica un descuento del {descuento}%, total a pagar {totalFacturado-(totalFacturado*descuento/100)}')
else:
    print("No aplica descuento")'''

#2) El banco Buena Paga ofrece diferentes tasas de interes anual para depositos a termino dependiendo del tiempó por el que se hagan. Si el deposito es por un preiodo
#menor o igual a 6 meses la tasa es del 8% anual, entre siete y 12 meses del 10%, entre 13 y 18 meses del 12%, entre 19 y 24 meses del 15%, y para peoriodos superiores
#a 24 meses del 18%. Se requiere un algoritmo para determinar cuanto recibira un cliente por un deposito tanto por concepto de interes como en total.

'''prestamo = int(input("Digite la cantidad del monto total del prestamo: "))
cuotas = int(input("Escoge la cantidad de cuotas mensuales para pagar el prestamo: "))

if cuotas > 24:
    intereses = 0.18/12
elif cuotas >= 19:
    intereses = 0.15/12
elif cuotas >= 13:
    intereses = 1/12
elif cuotas >= 7 and cuotas <= 12:
    intereses = 0.1/12
elif cuotas > 0 and cuotas <= 6:
    intereses = 0.08/12

totalPagar = round((prestamo +((prestamo*cuotas)*intereses)),3)

print(f'para un monto total de {prestamo} a un total de {cuotas} meses, el valor total mensual a pagar es de {totalPagar}')'''

#3) Una empresa editorial tiene tres grupos de empleados: vendedores, diseñadores y administrativos. Se requiere calcular el nuevo sueldo para los empleados
#teniendo en cuenta que se incrementaran sus salarios asi: administrativos 5%, diagramadores 10% y vendedores 12%, mostrar el nuevo sueldo y cual fue su incremento.

'''sueldo = int(input("Ingrese el sueldo actual del empleado:"))
tipoEmpleado = int(input(''A que categoria pertenece?
1. Administrativos       
2. Diseñadores 
3. Vendedores
Escoge una opcion: '')) 

#opcion1
match tipoEmpleado:
    case 1:
        print(f'Usted tiene un aumento del 5%, su nuevo sueldo es de ${(sueldo*0.05) + sueldo}')
    case 2:
        print(f'Usted tiene un aumento del 10%, su nuevo sueldo es de ${(sueldo*0.10) + sueldo}')
    case 3:
        print(f'Usted tiene un aumento del 12%, su nuevo sueldo es de ${(sueldo*0.12) + sueldo}')
    case _:
        print("Error: opcion no valida")

#opcion2
match tipoEmpleado:
    case 1:
        porcentaje = 5
    case 2:
        porcentaje = 10
    case 3:
        porcentaje = 12
    case _:
        porcentaje = 0
if porcentaje >1:
    print(f'Usted tiene un aumento del {porcentaje}% equivalente a {sueldo *0.05}, su nuevo sueldo es de ${(sueldo *0.05) + sueldo}')
else:
    print("Error: opcion no valida")'''

#4) Un vendedor recibe una comision sobre las ventas efectuadas en el mes, siempre que estas sean mayores a 1000000. Los porcentajs de bonificacion son :
#ventas mayores a 1000000 y hasta 2000000 = 3%
#ventas mayores a 2000000 y hasta 5000000 = 5%
#ventas mayores a 5000000 = 8%
#Se desea saber cuanto corresponde al vendedor por comision y cuanto recibira en total en el mes.

sueldo = float(input("Ingrese el valor de su sueldo actual: "))
ventas = float(input("Ingrese el valor total de las ventas efectuadas: "))

if ventas > 5000000:
    comision = ventas*0.08
elif ventas > 2000000:
    comision = ventas*0.05
elif ventas >= 1000000:
    comision = ventas*0.03

if ventas >= 1000000:
    print(f'El valor total de la comision sobre las ventas del mes son {comision}, por lo tanto el sueldo total para este mes es {sueldo+comision}')
else:
    print("Lo siento no recibes comision sobre las ventas")
        
