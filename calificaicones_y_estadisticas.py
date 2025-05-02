# Se establece una lista para almacenar las notas dadas por el Ususario.
notes = []
# Se establece una variable para almacenar la sumatoria de las notas dadas por el Usuario.
sum = 0

# Se le da la bienvenida al Usuario.
print("\nSea bienvenid@ al evaluador de notas.\n")

# Se pregunta la cantidad de notas que el Usuario desea evaluar, se valida que solo pueda ingresar caracteres de tipo "INT" 
# y se establece un tope máximo.
while True:
    try:
        amount = int(input("¿Cuántas notas desea evaluar?\n"))  
        if 1<= amount <=12:     
            break
        else:
            print("\n¡ERROR!, el numero minímo de notas a evaluar es 1. máximo 12.")
    except:
        print("\n¡ERROR!, ha isertado un caracter invalido.")

# Se establace un ciclo para que se repita en relación a la cantidad de notas que el Usuario desea evaluar.
for i in range(0,amount):
    # Se solicita al usuario ingresar una calificación numérica (de 0 a 100), se valida que solo pueda ingresar caracteres 
    # de tipo "FLOAT" y que la nota se encuentre dentro del rango establecido.
    while True:
        try:
            note = float(input("\nIndique la nota que desea evaluar (de 0 a 100): "))  
            if 0 <= note <= 100:     
                break
            else:
                print("\n¡ERROR!, la nota que evaluará debe estar entre 0 y 100.")
        except:
            print("\n¡ERROR!, ha isertado un caracter invalido.")

    # Se estabelce una sumatoria acumulada de las notas a evaluar.
    sum += note
    
    # Si la nota cumple con todas la validaciones se agrega a la lista "notes" establecida anteriormente.
    notes.append(note)

    # Se evalua si el estudiante ha aprobado o reprobado basándose en la calificación ingresada.
    if 0 <= note < 30:
        print("\nSu nota es INSUFICIENTE.\n¡¡REPROBADO!!")
    elif 30 <= note < 60:
        print("\nSu nota es DEFICIENTE.\n¡¡REPROBADO!!")
    elif 60 <= note < 80:
        print("\nSu nota es SATISFACTORIA.\n¡¡APROBADO!!")
    elif 80 <= note < 90:
        print("\nSu nota es SOBRESALIENTE.\n¡¡APROBADO!!")
    else:
        print("\nSu nota es EXCELENTE.\n¡¡APROVADO!!")

# Si el Usuario desea evaluar solo una nota, el programa terminará.
if amount == 1:
    print("\nHemos finalizado.\n")
    exit()
    
# Se calcua el promedio de las notas insertadas por el Usuario.
average = sum / amount

# Se le indica al Usuario que sus notas han sido almacenadas y 
# se calcula su promedio.
print("""\n!Sus notas han sido almacenadas de manera exitosa!""")
print(f"\nEl promedio de sus notas es {average}")
    
# Se le solicita la Usuario un valor para identificar cuántas de sus notas son mayores que este.
# Se valida que solo pueda ingresar caracteres de tipo "FLOAT" y que el valor se encuentre dentro del rango establecido.
while True:
    try:
        num_2 = float(input("\nAcontinuación indique un valor para contar cuántas de sus calificaciones\n"
                          "son mayores que este(de 0 a 100): "))  
        if 0 <= num_2 <= 100:     
            break
        else:
            print("\n¡ERROR!\El valor debe estar entre 0 y 100.")
    except:
        print("\n¡ERROR!, ha isertado un caracter invalido.")

# Se establece una variable para almacenar el conteo de los números mayores al indicado por el Usuario.
num_mayores = 0
# Se establece una lista para almacenar los números mayores al indicado por el Usuario.
mayores = []

# Se establece un contador para los números mayores al indicado por el Usuario.
for i in notes:
    while i > num_2:
        num_mayores += 1
        mayores.append(i)
        break
        
# Se combierte la lista "mayores" a caracter de tipo "STR" y se reemplazan "[]" por espacios en blanco.
mayores = str(mayores).replace("[","").replace("]","")

# Se tienen en cuenta diferentes repuestas dependiendo de si hay uno o varios números mayores e incluso si no hay.
if num_mayores == 0:
    print(f"\nNo hay numeros mayores que {num_2}")
elif num_mayores == 1:
    print(f"\nHay {num_mayores} número mayorque {num_2} dentro de sus calificaciones")
    print(f"El números mayor que {num_2} dentro de sus calificaciones es: {mayores}")
else: 
    print(f"\nHay {num_mayores} números mayores que {num_2} dentro de sus calificaciones")
    print(f"Los números mayores que {num_2} dentro de sus calificaciones son: {mayores}")
    
# Se le solicita la Usuario un valor para identificar cuántas de sus notas son iguales que este.
# Se valida que solo pueda ingresar caracteres de tipo "FLOAT" y que el valor se encuentre dentro del rango establecido.
while True:
    try:
        num_3 = float(input("\nAcontinuación indique qué calificación desea saber si está dentro de sus\n"
                            "calificaciones(de 0 a 100): "))  
        if 0 <= num_3 <= 100:     
            break
        else:
            print("\n¡ERROR!\El valor debe estar entre 0 y 100.")
    except:
        print("\n¡ERROR!, ha isertado un caracter invalido.")
            
# Se establece una variable para almacenar el conteo de los números iguales al indicado por el Usuario.
equals = 0

# Se establece un contador para los números iguales al indicado por el Usuario.
for i in notes:
    if num_3 == i:
        equals += 1

# Se tienen en cuenta diferentes repuestas dependiendo de si hay uno o varios números iguales e incluso si no hay .
if equals == 0:
    print(f"\nNo hay numeros iguales que {num_3}")
elif equals == 1:
    print(f"\nDentro de sus calificaciones existe {equals} número igual a {num_3}")
else: 
    print(f"\nDentro de sus calificaciones existen {equals} números iguales a {num_3}")