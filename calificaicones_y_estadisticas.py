# Se establece una lista para almacenar las notas dadas por el Ususario.
notes = []
# Se establece una variable para almacenar la sumatoria de las notas dadas pro el Usuario.
sum = 0

# Se le da la bienvenida al Usuario.
print("\nSea bienvenid@ al evaluador de notas.\n")

# Se pregunta la cantidad de notas que el Usuario desea evaluar.
# Se valida que solo pueda ingresar caracteres de tipo INT.
while True:
    amount = input("¿Cuántas notas desea evaluar?\n")
    try:
        amount = int(amount)
        break
    except:
        print("\n¡ERROR!, ha isertado un caracter invalido.\n")

# Se establace un ciclo para que se repita en relación a la cantidad de notas que desea evaluar el Usuario.
for i in range(0,amount):
    # Se solicita al usuario ingresar una calificación numérica (de 0 a 100).
    # Se valida que solo pueda ingresar caracteres de tipo INT.
    while True:
        note = input("Indique la nota que desea evaluar (de 0 a 100): ")
        try:
            note = int(note)
            break
        except:
            print("\n¡ERROR!, ha insertado un caracter invalido.\n") 

    # Se valida que las notas que ingrese el usuario de encuentren dentro del rango permitido.        
    while note < 0 or note > 100:
        print("\n¡ERROR!, la nota que evaluará debe estar entre 0 y 100.\n")
        while True:
            note = input("Indique una nota valida: ")
            try:
                note = float(note)
                break 
            except:
                print("\n¡ERROR!, ha insertado un caracter invalido.\n")

    # Se estabelce una sumatoria acumulada de las notas a evaluar.
    sum += note
    
    # Si la nota cumple con todas la validaciones se agrega a la lista establecida anteriormente.
    notes.append(note)

    # Se evalua si el estudiante ha aprobado o reprobado basándose en la calificación ingresada.
    if note >= 0 and note < 25:
        print("\nSu nota es INSUFICIENTE.\n¡¡REPROBADO!!\n")
    elif note >= 25 and note < 50:
        print("\nSu nota es DEFICIENTE.\n¡¡REPROBADO!!\n")
    elif note >= 50 and note < 75:
        print("\nSu nota es SATISFACTORIA.\n¡¡APROBADO!!\n")
    elif note >= 75 and note < 90:
        print("\nSu nota es SOBRESALIENTE.\n¡¡APROBADO!!")
    else:
        print("\nSu nota es EXCELENTE.¡¡APROVADO!!")

# Se calcua el promedio de las notas insertadas por el Usuario.
average = sum / amount

# Se le indica al Usuario que sus notas han sido almacenadas y 
# se calcula su promedio.
print("""\n!Sus notas han sido almacenadas de manera exitosa!\n""")
print(f"El promedio de sus notas es {average}")

# Se le solicita la Usuario un valor para identificar cuántas de sus notas son mayores que este.
# Se valida que solo pueda ingresar caracteres de tipo INT
while True:
    num_2 = input("\nAcontinuación indique un valor para contar cuántas de sus calificaciones\n"
                  "son mayores que este(de 0 a 100): ")
    try:
        num_2 = int(num_2)
        break
    except:
        print("\n¡ERROR!, ha insertado un caracter invalido.\n")

# Se valida que el valor que ingrese el usuario de encuentren dentro del rango permitido.
while num_2 < 0 and num_2 > 100:
    print("\n¡ERROR!\El valor debe estar entre 0 y 100.\n")
    while True:
        num_2 = input("Indique una nota valida: ")
        try:
            num_2 = float(num_2)
            break 
        except:
            print("\n¡ERROR!, ha insertado un caracter invalido.\n")

# Se establece una variable para almacenar el conteo de los números mayores al indicado por el Usuario.
num_mayores = 0
# Se establece una lista para almacenar los números mayores al indicado por el Usuario.
mayores = []

# Se establece un contador para los números mayores al indicado por el Usuario.
for i in notes:
    if i > num_2:
        num_mayores += 1
        mayores.append(i)

mayores = str(mayores).replace("[","").replace("]","")

print(f"\nHay {num_mayores} números mayores que {num_2} dentro de sus calificaciones\n")
print(f"Los números mayores que {num_2} de sus calificaciones son: {mayores}\n")