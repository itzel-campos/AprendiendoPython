#Itzel Campos
#16/09/2019

#Se decaran las variables con las uqe vamos a trabajar
acumulado = int(0)
numero = str("")
#Cuando se coloca el valor de true a un while este no para a menos que haya una instruccion break que rompa
#Con este ciclo al darle una comparacion para que vaya al break

while True:
    numero = input("Dame un numero entero ")
    if numero=="":
        #Si se da enter si ningun numero se terminara el programa
        print("Vacio. Salio del programa")
        break
    else:
        #Se utiliza la suma incluyente (+=) para que al acumulado se le sume el nuevo numero ingresado
        acumulado+=int(numero)
        salida = "El monto acumulado es {}"
        print(salida.format(acumulado))
