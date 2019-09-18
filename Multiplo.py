#Itzel Campos
#16/09/2019

#Se pide el numero y se le da un valor entero
numero = int(input("Dame un numero entero: "))
#Se compara con el residuo de la divsion para saber si es cero y asi saber si es un multiplo
esMultiplode3=((numero%3)==0)
esMultiplode5=((numero%5)==0)
esMultiplode7=((numero%7)==0)
#Los parentesis se usan para indicar qeu las primeras dos comparaciones estan juntas y la tercera es una independiente
if ((esMultiplode3 and esMultiplode5) or esMultiplode7):
    print("Es correcto")
else:
    print("Es incorrecto")
