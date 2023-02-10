#1) Realizar un programa que lea los lados de triangulos, e informar:
#a) De cada uno de llos, que tipo de triangulo es: equilatero (tres lados inguales), isoceles (dos lados iguales, o escaleno (ningun lado igual)
#b) Cantidad de triangulos de cada tipo
#c) Tipo de truangulo del que hay menor cantidad

'''bandera = True
contEqui, contIsos, contEsc, contador = 0, 0, 0, 0

while bandera == True:
    cate1 = float(input("Ingrese el valor del primer lado del triangulo: "))
    cate2 = float(input("Ingrese el valor del segundo lado del triangulo: "))
    hipot = float(input("Ingrese el valor del tercer lado del triangulo: "))
    if cate1 == cate2 and cate2 == hipot:
        print("El tipo de triangulo es: Equilatero")
        contEqui +=1
    elif (cate1 == cate2 and cate1 != hipot) or (cate1 == hipot and cate1 != cate2) or (cate2 == hipot and hipot != cate1):
        print("El tipo de triangulo es: Isosceles")
        contIsos +=1
    elif cate1 != cate2 and cate1 != hipot and cate2 != hipot:
        print("El tipo de triangulo es: Escaleno")
        contEsc +=1
    contador +=1
    if contador == 4:
        break    
print(f'Hay una cantidad de {contEqui} triangulos Equilateros, {contEsc} triangulos Escalenos y {contIsos} triangulos Isosceles')
if contEqui > contEsc and contEqui > contIsos and contEsc > contIsos:
    print(f'Hay menos triangulos Isosceles con una cantidad de {contIsos}')
elif contEqui > contEsc and contEqui > contIsos and contIsos > contEsc:
    print(f'Hay menos triangulos Escalenos con una cantidad de {contEsc}')
elif contEqui < contEsc and contEqui < contIsos and contEsc < contIsos:
    print(f'Hay menos triangulos Equilateros con una cantidad de {contEqui}')
elif contEqui == contIsos:
    print(f'hay menos triangulos Equilateros y Isosceles con una cantidad de {contEqui}')
elif contEqui == contEsc:
    print(f'Hay menos triangulos Equilateros y Escalenos con una cantidad de {contEqui}')
elif contEsc == contIsos:
    print(f'Hay menos triangulos Escalenos y Isosceles con una cantidad de {contEsc}')'''

#2) Imprimir un triangulo de numeros

#solucion1
'''tri = ""
for i in range(1,6):  
    tri += str(i)
    print(tri)'''

'''#solucion2
for i in range(1,6):  
    print(i)
    for j in range(1, i+1):
        print(j , end= "")'''

#3) Imprimir un triangulo invertido de numeros

#solucion2
'''for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j , end= "")
    print("")'''

#4) hacer un algoritmo para calcular el residuo (modulo) y cociente (trunc o div o //) solo por medio de restas sucesivas

resta, conteo, residuo = 0, 0, 0
dividendo = int(input("Digita el numero del dividendo: "))
divisor = int(input("Digita el numero del divisor: "))



'''dividendo, divisor, resta, conteo, residuo = 0, 0, 0, 0, 0
bandera = True 
while bandera == True:
    if dividendo == 0:
        dividendo = int(input("Digita el numero del dividendo: "))
    elif divisor == 0:
        divisor = int(input("Digita el numero del divisor: "))
    while residuo > divisor:
        residuo -= divisor
        conteo +=1
        
    print(residuo)'''
               

