#Itzel Campos
#16/09/2019
#Python pose muchas librerias listas para usarse.
#A dicahs librerias se les da el nombre de modulos.
#Para que se puedan usar se debe importar con la instruccion import.
import random
Numero1 = float(10.5)
#En python una funcio es un conjunto de instrucciones que procesan una tarea especifica, como unidad de ejecucion
#Se declara con def el codigo que este posicionado a la derecha de la definicion, forma parte de la funcion
def Mifuncion ():
  #Se convierte a float el umero aleatorio generado por random(esto solo es posible si se importa random)
  Numero2 = float(random.randrange(1,10))
  Mensaje = "La suma de {} y de {} es de {}"
  print(Mensaje.format (Numero1,Numero2,Numero1+Numero2))
Mifuncion()