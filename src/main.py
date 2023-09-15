fin = False #Almacena el valor de False
print("""=== CALCULADORA ===
      \nMenu Principal -> Elija Una opcion: 
      \n1 Sumar
      \n2 Restar
      \n3 Multiplicar
      \n4 Dividir
      \n5 Salir
      """)
while not fin:
            opc = int(input("Opcion: "))#declaramos una variable Opc que contiene una entrada de datos
            #la cual mostrara un Opcion: donde el usuario puede digitar un numero que hara referencia a la 
            #operacion a realizar
            if(opc == 1):
                #Al principio validamos si la opcion ingresada es igual a 1
                sum1 = int(input("Ingrese el primer numero: ")) 
                sum2 = int(input("Ingrese el segundo numero: ")) 
                print("La suma es de: ",sum1 + sum2)
            elif(opc == 2):
              rest1 = int(input("Ingrese el primer nunero: "))
              rest2 = int(input("Ingrese el segundo numero: "))
              print("La Resta es de: ",rest1-rest2)
            elif(opc == 3):
              product1 = int(input("Ingrese el primer numero: "))
              product2 = int(input("Ingrese el segundo numero: "))
              print("El producto es de: ",product1 * product2)
            elif(opc == 4):
              dividir1 = int(input("Ingrese el primer numero: "))
              dividir2 = int(input("Ingrese el segundo numero: "))
              print("La division es de: ",dividir1/dividir2)
            elif(opc == 5):
              fin = True