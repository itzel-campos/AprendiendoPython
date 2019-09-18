#Itzel Campos
#16/09/2019
#Python tiene librerias las cuales se pueden utilizar importandolas con la instrucccion import
import random
Numero1 = float(10.5)
#En python una funcion es un bloque de codigo que hace una tarea especifica tomando en cuenta lo que este alineado
#a la derecha de la funcion que este se tiene cuando se escribe def
def Mifuncion ():
  #Se cambia a float el numero que es dado por random(esto solo es posible si se importa random)
  Numero2 = float(random.randrange(1,10))
  Mensaje = "La suma de {} y de {} es de {}"
  print(Mensaje.format (Numero1,Numero2,Numero1+Numero2))
Mifuncion()
