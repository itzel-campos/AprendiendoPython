def Sacareltiempo (Distancia, Velocidad):
    TiempoEstimado = Distancia / Velocidad
    return TiempoEstimado

DistanciaEstimada = int(input("Favor de ingresar la distancia \n"))
VelocidadEstimada = int(input("Favor de ingresar la velocidad \n"))
TiempoEstimado = Sacareltiempo (DistanciaEstimada, VelocidadEstimada)

print("El tiempo estimado es de: {}"  .format(TiempoEstimado))