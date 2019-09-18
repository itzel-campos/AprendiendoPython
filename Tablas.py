#Itzel Campos
#16/09/2019

for i in range (1,11):
    Encabezado = "Tabla del {}"
    print(Encabezado.format(i))
    #print solo es un salto de linea
    print()
    #dentro de un for se pone otro for
    for j in range(1,11):
        #Aqui i tiene el numero de la tabla y j el elemento de la tabla
        salida= "{} x {} es {}"
        print(salida.format(i,j,i*j))
    else:
        #Al concluir con las iteraciones indicadas se ejecuta este codigo, que es un salto de linea
            print()
