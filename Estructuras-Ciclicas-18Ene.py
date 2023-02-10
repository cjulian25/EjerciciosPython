# 1)Hacer un programa que conveirta un numero decimal a binario

'''num = 0
residuo = 0
binario = ""

num = int(input("Escribe un número: "))

while num > 0:
    residuo = num%2
    binario = str(residuo)+binario
    num = num//2
print(f'En binario es: {binario}')'''

# 2) Dado un numero n, entero positivo, calcular y mostrar la sumatoria de los numeros desde 1 hasta n.

'''num = 0
suma = 0

num = int(input("Digite un numero: "))

for i in range(num+1): #Se le agrega ese +1 para que llegue al numero al cual se digita ya que empieza desde 0
    suma = suma+i
print(f'La sumatoria es: {suma}')'''

# 3) PEdir al usuario un numero del 1 al 9 y mostrar la tabla de multiplicar de dicho numero.

'''num = 0

num = int(input("Digite un numero: "))
for i in range(num):
    if i <=num:
        multi = num*(i+1)
    print(f'{num} * {i+1} = {multi}')'''

# 4) Realizar un programa que imprima 25 terminos de la serie 11-22-33-44, etc. (No se ingresan valores por teclado)

'''num = 0

for i in range(25):
    num = num+11
    i = i+1
    print(f'Termino {i} = {num}')'''

# 5) Mostrar los multiplos de 8 hasta el valor de 500. debe aparecer en pantalla 8-16-24.

#solucion1
'''for i in range(8,500,8):
    print(i)
    i +=1'''

#solucion2
'''num = 0
while num <=500:
    print(num)
    num += 8'''

# 6) Realizar un programa que muestre los numeros del 1 al 10 en orden inverso (decendente).

#solucion1
'''for i in range(10,0,-1):
    print(i, end=", ")'''

#solucion2
'''num = 10
while num > 0:
    print(num, end=", ")
    num -=1'''

# 7) Dados dos numeros devolver los numeros pares que existen entre si.

'''num1 = int(input("Digite un numero: "))
num2 = int(input("Digite otro numero: "))

i= 0

#solucion1
if num1 < num2:
    for i in range(num1,num2+1):
        mod = i%2
        if mod == 0:
            print(i)
            i +=1
elif num2 < num1:
    for i in range(num2,num1+1):
        mod = i%2
        if mod == 0:
            print(i)
            i  +=1
elif num1 == num2:
    print("Los dos numeros son iguales")'''

'''num1 = int(input("Digite un numero: "))
num2 = int(input("Digite otro numero: "))

#solucion2
if num1 > num2:
    while num1 > num2:
        if num2%2 == 0:                     
            print(num2)
        num2 +=1  
elif num2 > num1:
    while num2 > num1:
        if num1%2 == 0:
            print(num1)
        num1 +=1 
elif num1 == num2:
    print("Los dos numeros son iguales")'''

# 8) Dados dos numeros, contar la cantidad de numeros pares que existen entre si.

'''num1 = int(input("Digite un numero: "))
num2 = int(input("Digite otro numero: "))
suma = 0
if num1 < num2:
    for i in range(num1,num2+1):
        mods = i%2
        if mods== 0:
            suma+=1
elif num2 < num1:
    for i in range(num2,num1+1):
        mods = i%2
        if mods == 0:
            suma+=1
elif num1 == num2:
    print("Los dos numeros son iguales")
print(f'Hay {suma} pares')'''

