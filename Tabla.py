#Itzel Campos
#16/09/2019

Numero = input("Dame un numero del 1 al 9\t")
Numero = int(Numero)
#for ejecuta un bloque de codigo un numero determinado de veces, cuando se pide que recorra un rango de valores
#El segundo parametro de range no se incluye en la serie de valores
for i in range (1,11):
    #i va variando a cada iteracion
    salida = "{} x {} = {}"
    print (salida.format(Numero,i,i*Numero))