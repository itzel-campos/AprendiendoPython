#Itzel Campos
#16/09/2019
#Se le da un valor de cadena con una serie de numeros
Numero = "1234"
#Se muestra el tipo de que tiene la variable.
print (type(Numero))
#Se cambia el tipo a entero a entero
Numero = int (Numero)
#Se muestra el tipo de la variable ya cuando se a cambiado
print (type(Numero))
#Se da la salida del mensaje usando format 
salida = ("El numero utilizado es {}")
print (salida .format (Numero))
