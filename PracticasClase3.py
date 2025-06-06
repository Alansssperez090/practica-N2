import math

# Ingresar número 

numero = int(input("Ingresa un número entero distinto de 0: "))

if numero == 0:
    print("El número que ingresaste es 0. Saliste del programa.")
    quit()

if numero > 0:
    print("Bien ahí, pudiste entrar.")
    print("Ahora ingresa una palabra para que yo pueda contar las letras.")

   
    # Contar letras 
    
    palabra = input("Ingresa tu palabra: ")
    print("La palabra tiene", len(palabra), "letras.")
else:
    print("Ingresaste un número negativo. El programa ha terminado.")