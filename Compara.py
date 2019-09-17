#Itzel Campos
#16/09/2019

numero1 = input("Dame el primer numero  ")
numero2 = input("Dame el segundo numero  ")
salida = "Numeros proporcionados : {} y {} .{}."
if (numero1 == numero2):
    #Entra aqui si los numeros son iguales
    print(salida.format(numero1,numero2,"Los numeros son iguales"))
else:
    #condicionales anidadas, if dentro de otro if. Si los numeros no son iguales
    if numero1 > numero2:
        #Reporta si el primer numero es mayor
        print(salida.format(numero1,numero2,"El primer numero es el mayor"))
    else:
        #O de lo contrario si el primero es menor
        print(salida.format(numero1,numero2,"El segundo numero es el mayor"))