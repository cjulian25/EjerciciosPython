#1) Una empresa esta pagando una bonificacion a sus empleados dependiendo del tiempo de servicio y del estado civil, asi : para empleados solteros: Si llevan hasta 5 años,
#el 2% del sueldo; entre 6 y 10 años el 5%; mas de 10 años el 10%. Para empelados casados: si llevan hasta 5 años, 5% del sueldo, entre 6 y 10 años el 10%,
# mas de 10 años el 15%.

'''servicio = int(input("Cuantos años lleva laborando en la empresa?: "))
sueldo = int(input("Digite su sueldo mensual: "))
estadoCivil = int(input(''Es usted casado o soltero?
1) Casado
2) Soletro
Escoge una opcion:  ''))

match estadoCivil:
    case 1:
        if servicio > 10:
            bonificacion = 15
        elif servicio > 6:
            bonificacion = 10
        elif servicio > 0:
            bonificacion = 5
    case 2:
        if servicio > 10:
            bonificacion = 10
        elif servicio > 6:
            bonificacion = 5
        elif servicio >0:
            bonificacion = 2
    case _:
        print("Error")
print(f'Su bonificacion corresponde al {bonificacion}% para un total de {sueldo*bonificacion/100}, su sueldo quedaria en {(sueldo*bonificacion/100)+sueldo}')'''

#2) Una empresa desea contratar un profesional para cubrir una vacante, los requisitos para ser considera elegible son: ser profesional y tener entre 25 y 35 años
#inclusive, o contar con formacionm academica de especialista o superior en cuyo caso no se tiene en cuenta la edad. Se requiere un algoritmo que evalue los datos de
#cada candidado e informe si es apto o no apto.

'''formacion = int(input(''Cual es su nivel de formacion?
1) Tecnico o Tecnologo
2) Profesional, especialista, Magister o Doctorado
Escoge una opcion:  ''))
edad = int(input("Digite su edad: "))

if edad >= 18:
    match formacion:
        case 1:
            if edad >= 25 and edad <= 35:
                print("No Apto")
            elif edad < 25 and edad > 35:
                print("No cumple con el requisito de ser profesional, ni el de edad")
        case 2:
            if edad >= 25 and edad <= 35:
                print("Apto")
            else:
                print("No cumple con el requisito de edad pero si cumple con el requisito de ser profesional")
        case _:
            print("Error: opcion no validad")
else:
    print("Error: Edad no valida")'''
        
