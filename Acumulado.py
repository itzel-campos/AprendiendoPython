#Itzel Campos
#16/09/2019

#Se decaran las variables de trabajo con tipo explicito
acumulado = int(0)
numero = str("")
#Al colocar True como condicion de while, se forma un ciclo infinito que no se rompera hasta que de forma
#explicita se utilice la instruccion break
while True:
    numero = input("Dame un numero entero ")
    if numero=="":
        #Si el numero es vacio, reporta la situacion y sale
        print("Vacio. Salio del programa")
        break
    else:
        #Si proporciono valor, acumulado = acumulado + numero
        #Se realixa el calculo usando suma incluyente (+=)
        acumulado+=int(numero)
        salida = "El monto acumulado es {}"
        print(salida.format(acumulado))
