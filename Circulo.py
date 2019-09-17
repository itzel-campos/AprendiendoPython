def AreaCirculo(Radio):
    area = 3.1416 * Radio 
    return area 

radioDado = int( input("¿Cual es el radio del circulo?"))
area = AreaCirculo(radioDado)


print("El area del circulo de {} de radio es de:{}" .format(radioDado, area))
