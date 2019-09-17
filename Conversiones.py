#Itzel Campos
#16/09/2019
#Se declara una variable str, con una cadena de digitos
Numero = "1234"
#Se muestra el tipo de que tiene la variable.
print (type(Numero))
#Se convierte a entero
Numero = int (Numero)
#Se muestra como el tipo de variable cambia aunque se use la misma variable
print (type(Numero))
#Se declara un str con meta de sustitucion usando format
salida = ("El numero utilizado es {}")
print (salida .format (Numero))
