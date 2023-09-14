fin = False #Almacena el valor de False
print("""=== CALCULADORA ===
      \nMenu Principal -> Elija Una opcion: 
      \n1 Sumar
      \n2 Restar
      \n3 Multiplicar
      \n4 Dividir
      \n5 Salir
      """)#Agregamos un blucle while que se ejecutara multiples veces al menos que nosotros salgamos del
        #programa
        while not(fin):
            opc = int(input("Opcion: "))#declaramos una variable Opc que contiene una entrada de datos
            #la cual mostrara un Opcion: donde el usuario puede digitar un numero que hara referencia a la 
            #operacion a realizar
            if(opc == 1):
                #Al principio validamos si la opcion ingresada es igual a 1
                sum1 = int(input("Ingrese el primer numero: ")) 
                sum2 = int(input("Ingrese el segundo numero: ")) 
                print("La suma es de: ",sum1 + sum2)
