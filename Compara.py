#Itzel Campos
#16/09/2019

numero1 = input("Dame el primer numero  ")
numero2 = input("Dame el segundo numero  ")
salida = "Numeros proporcionados : {} y {} .{}."
if (numero1 == numero2):
    #Verifica si los numeros son iguales 
    print(salida.format(numero1,numero2,"Los numeros son iguales"))
else:
    # Si los numeros no son iguales se pone un if dentro de otro if para hacer las debidas comparaciones 
    if numero1 > numero2:
        print(salida.format(numero1,numero2,"El primer numero es el mayor"))
    else:
        print(salida.format(numero1,numero2,"El segundo numero es el mayor"))
