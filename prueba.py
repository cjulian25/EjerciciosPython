print("Bienvenido a la plataforma calificativa de coex :)")
print("")
n=0

#Almacen de datos en forma de matriz    
Coex =[]
Verificacion = []
Nota = []

menu = int(input('''------------   Bienvenido a la plataforma calificativa de coex :)   ---------
1. Ingreso de talentos en el grupó 
2. Informacion del talento 
3. Registro de notas del talento
4. ver nombre y nota del talento con las mejores notas de cada mision
5. Creditos
6. Salir
Elegir la opcion de operacion '''))
match menu:

    case '1':

        n = int(input("ingrese cuantos talentos conforman el grupo en coex : "))
        print("")

#Validacion para el ingreso de la cantidad en el grupo de coex
        while n < 0 :
            print("")
            n = int(input("Porfavor vuelva a ingresar un dato valido : "))
            print("")


    case '2':
    
        for i in range(n) :
            print("")#VALIDACION DEL NOMBRE DEL TALENTO
            Coex.append({})
            nombre = input(f'ingrese el nombre del talento ({i}) : ')
        while nombre == "" :
            nombre=input(f'ingrese correctamente un talento ({i}) : ')
            Coex[i]["Nombre"]=nombre
            print("")#VALIDACION DEL CODIGO Y QUE NO SE REPITA DEL TALENTO
            codigo = int(input(f'ingrese el codigo del talento ({i}) : '))
            if codigo not in Verificacion :
                Verificacion.append(codigo)
                Coex[i]["Codigo"] = codigo
        
            else :
                while codigo in Verificacion:
                    print("")
                    print("LO LAMENTAMOS ESE CODIGO YA FUE INGRESADO ANTERIORMENTE")
                codigo = int(input(f'vuelva a ingresar el codigo ({i}) : '))
                Verificacion.append(codigo)
                Coex[i]["Codigo"] = codigo
                print("")
        

    case '3':

        for i in range(n) :
            print("")#INGRESO DE CALIFICACIONES
            nota1 = float(input(f'ingrese la primera nota del talento {Coex[i]["Nombre"]} : '))
            while nota1 < 0 or nota1 >100:
                print("")
                nota1 = float(input("lo lamentamos vuelva a ingresar una nota calificable"))
            Coex[i]["Nota1"] = nota1
  

            nota2 = float(input(f'ingrese la segunda nota del talento {Coex[i]["Nombre"]} : '))
            while nota2 < 0 or nota2 >100:
                print("")
                nota2 = float(input("lo lamentamos vuelva a ingresar una nota calificable"))
            Coex[i]["Nota2"] = nota2
            
            nota3 = float(input(f'ingrese la tercera nota del talento {Coex[i]["Nombre"]} : '))
            while nota3 < 0 or nota3 >100:
                print("")
                nota3 = float(input("lo lamentamos vuelva a ingresar una nota calificable"))
            Coex[i]["Nota3"] = nota3
    nota4 = float(input(f'ingrese la ultima nota del talento {Coex[i]["Nombre"]} : '))
    while nota4 < 0 or nota4 >100:
        print("")
        nota4 = float(input("lo lamentamos vuelva a ingresar una nota calificable"))
    Coex[i]["Nota4"] = nota4

    Promedio = (nota4 + nota3 + nota2 + nota1)/4 #PROMEDIO DE NOTAS
    Coex[i]["Promedio"] = Promedio

for i in range(len(Coex)):
    print(f'el estudiante : {Coex[i]["Nombre"]} obtuvo un promedio  de : {Coex[i]["Promedio"]}')

   


               
        
    
    case '4':

for i in range(len(Coex)): #RESULTADOS COMPLETOS CON NOMBRE Y CODIGO
    print("")
    print(f'El estudiante : {Coex[i]["Nombre"]} , con el codigo  :{Coex[i]["Codigo"]} , obvtuvo en su primera mision una nota de : {Coex[i]["Nota1"]} ,en la segunda {Coex[i]["Nota2"]} , en la tercera {Coex[i]["Nota3"]} y en la final : {Coex[i]["Nota4"]} y su promedio fue de {Coex[i]["Promedio"]}')
    print("")


    case '5':
print("")  # DERECHOS RESERVADOS
print("@Todos los derechos reservados a coex y el programador christian naren sanchez cristancho (2023-2060)")

    case '6':

      print("Gracias por usar nuestro software,que tenga un buen dia")

    case _:

        print("ERROR")

case _: