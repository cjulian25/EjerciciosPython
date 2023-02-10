'''edad = int(input("Ingrese la edad: "))
if edad>18 :
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
print("Se definio tu suerte")'''

'''nota = float(input("Ingrese la nota: "))
if nota>= 0 and nota<= 5.0:
    if nota>=3.0:
        print("Aprobo")
    else:
        print("No aprobo")
else: 
    print("La nota no es valida")'''

categoria = input("Digite la categoria: ")
#categoria = categoria.lower()
if categoria.lower() == "a":
    print("Paga $3000")
elif categoria.lower() == "b":
    print("Paga $7000")
elif categoria.lower() == "c":
    print("Paga $12000")
else:
    print("Paga $21000")

