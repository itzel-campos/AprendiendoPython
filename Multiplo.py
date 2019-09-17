#Itzel Campos
#16/09/2019

#Se captura un numero y se almacena una vez que es cambiado a int
numero = int(input("Dame un numero entero: "))
#Se almacena en valores booleanos la evaluacion de residuales. Si el residal es cero quiere decir que es multiplo
esMultiplode3=((numero%3)==0)
esMultiplode5=((numero%5)==0)
esMultiplode7=((numero%7)==0)
#Cuando se usa and, se resuelve por verdadero si todas las condiciones son verdaderas. Cuando se usa or
#Se resuelve verdadero si al menos una codicion es verdadera
#Los parentesis le dicen a python que las primeras dos condicione son juntas y la tercera es independiente
if ((esMultiplode3 and esMultiplode5) or esMultiplode7):
    print("Es correcto")
else:
    print("Es incorrecto")