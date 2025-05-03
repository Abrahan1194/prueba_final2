print("-"*50)
print("\n Menu Programa Gestion de Datos:")
print("\n Escoge una accion a realizar :")
print("1. Determinar estado de aprobacion.")
print("2. Calcular promedio de notas ingresadas.")
print("3. Contar cuantas calificaciones son mayores a un valor especifico Ingresado.")
print("4. Contar cuantas veces se repite una calificacion es espesifica ingresada por el usuario.")
print("5. Salir")   
print("-"*50)

while  True:# Bucle principal del programa
    opcion = input("\nIngrese una opcion del 1 al 5 : ")
    if opcion == '1' :
        while True:# Bucle para asegurar una entrada válida
            nota_final_letras = input("Ingrese calificacion del estudiante para determinar si aprobo o no aprobo:")#se ingresa en str despues se convierte
            try :
                nota_final =int(nota_final_letras)# Convertir a número entero
                if 0 <= nota_final<=100:
                    break
                else:
                    print("Ingrese una calificacion valida entre 0 y 100:")
            
            except ValueError :
                print("Valor Invalido ingrese una calificacion :")
        if nota_final >= 70  :
             print("\nAprobado")

        else :
             print("\nReprobado")

    elif opcion == '2': 
        print("\nCalcular Promedio : ")

        while True :# Bucle para ingresar las notas
            nota_final_letras = input("Ingrese las notas separas por (,) : ")
            lista_notas_letras = nota_final_letras.split(',')# Separar las notas en una lista de strings
            lista_notas_sum = [] # Lista para almacenar las notas convertidas a números
            valida = True # Variable para controlar si todas las entradas son válidas
            for calif_letra in lista_notas_letras:
                try:
                    calif = int(calif_letra.strip())# Iterar sobre cada nota en string
                    if 0 <= calif <= 100:
                        lista_notas_sum.append(calif)
                    else:
                        print("Una de las calificaciones ingresadas no esta entre 0 y 100")
                        valida = False
                        break
                except ValueError:
                    print("Entrada invalida en la lista de calificaciones ingresa numeros separados por comas")
                    valida = False
                    break
            if valida and lista_notas_sum:
                nota_final = lista_notas_sum # Actualizamos la lista principal
                suma_calificaciones = 0
                for calif in nota_final:
                   suma_calificaciones += calif
                promedio = suma_calificaciones  / len(nota_final)
                print(f"El promedio de las calificaciones es: {promedio:.2f}")
                break
            elif valida and not lista_notas_sum:
                 print("No ingresaste ninguna calificacion")

    elif opcion == '3':
        
        print("\nContar cantidad de calificaciones mayores")
        if not nota_final:# Comprobar si ya hay una lista de notas
            print("Primero debes ingresar una lista de calificaciones (opción 2)")
        else:
            while True:# Bucle para obtener el valor de comparación
                valor_comparacion_letras = input("Ingresa un valor para comparar las calificaciones: ")
                try:
                    valor_comparacion = int(valor_comparacion_letras)
                    break
                except ValueError:
                    print("Entrada invalida. Por favor, ingresa un número")

            contador_mayores = 0
            i = 0
            while i < len(nota_final):# Iterar sobre la lista de notas
                if nota_final[i] > valor_comparacion:
                    contador_mayores += 1
                i += 1
        print(f"Hay {contador_mayores} calificaciones mayores que {valor_comparacion}.")

    elif opcion == '4':
       
          print("\nVerificar y contar calificaciones especificas")
          if not nota_final:# Comprobar si ya hay una lista de notas
            print("Primero debes ingresar una lista de calificaciones")
          else:
            while True:
                calificacion_especifica_letra = input("Ingresa una calificacion especifica para contar: ")
                try:
                    calificacion_especifica = int(calificacion_especifica_letra)
                    if 0 <= calificacion_especifica <= 100:# Validar el rango
                        break
                    else:
                        print("Ingresa una calificacion entre 0 y 100.")
                except ValueError:
                    print("Entrada invalida. Ingresa un numero")

            contador_especifica = 0
            encontrada = False #Variable para saber si se encontró la calificación
            for calif in nota_final:
                if calif == calificacion_especifica:
                    contador_especifica += 1
                    encontrada = True
                    continue# Continuar a la siguiente iteración
                
            if encontrada:
                print(f"La calificacion {calificacion_especifica} aparece {contador_especifica} veces en la lista.")
            else:
                print(f"La calificacion {calificacion_especifica} no se encontró en la lista.")

    elif opcion == '5':
          print("Saliendo del programa")
          break

    else:
          print("Opción inválida, imgrese numero entre 1 y 5")
 
