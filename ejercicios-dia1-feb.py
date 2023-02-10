#1. Dada una matriz de m*n diseñar un algoritmo para sumar cada una de las filas y guardar los resultados en un ventor llamado sumafila, sumar cada una de las
# ccolumnas y guardar los resultados en el vector sumacol, finalmente mostrar los dos vectores.

matriz, sumaFila, sumaColumna, extra  = [], [], [], []
contador, contador2 = 0,0

#fila = int(input(""))

for i in range(4):
    matriz.append([])
    for j in range(6):
        matriz[i].append(contador+j+1)
    contador += j+ 1

for i in matriz:
    sumaFila.append(sum(i))

for columna in range(6):
    sumaColumna.append([])
    for fila in range(4):
        sumaColumna[columna].append(matriz[fila][columna])
        #extra.append(sum(sumaColumna[columna]))
#print(extra)  
    
suma = sum(sumaColumna[columna])
sumaColumna.insert(columna,suma)
   
#print(matriz)
#print(sumaFila)