#Itzel Campos
#16/09/2019

Numero = input("Dame un numero del 1 al 9\t")
Numero = int(Numero)
#for ejecuta un bloque de codigo un numero determinado de veces y este recorre un rango de valores 
for i in range (1,11):
    #i va variando cada que se ejecuta el for
    salida = "{} x {} = {}"
    print (salida.format(Numero,i,i*Numero))
