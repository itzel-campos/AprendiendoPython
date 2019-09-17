#Itzel Campos
#16/09/2019
Entrada = input()
print (type(Entrada))
#La variable booleana contienen el resultado de verificar si lo capturado es un digito, y si no se encuentra
#un punto en lo capturado, lo que indicaria que se trata de un numero con decimales. si find retorna -1 quiere 
#decir que lo buscado, en este caso el punto decimal, no se encontro. si esentero es TRue, lo capturado es entero
esEntero = (Entrada.isdigit() and Entrada.find(".") == -1)

if (esEntero):
  #Lineas que se ejecutan si la condicion es verdadera
  print("Dato entero ¡Muy bien!")
else:
    print("Dato no es entero. Intentar nuevamente")