def AreaTriangulo(Base, Altura):
    area = Base * Altura / 2  
    return area 

baseDada = int( input("¿Cual es la base del triangulo?"))
alturaDada = int( input("¿Cual es la altura del triangulo?"))
area = AreaTriangulo(baseDada, alturaDada)

print("El area del triangulo de {} X {} es de:{}" .format(baseDada, alturaDada, area))
