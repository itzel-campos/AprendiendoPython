import sys

listaNumeros = [1,2,3,4,5,6,7,8,9,10]
tuplaNumeros = 1,2,3,4,5,6,7,8,9,10

consumoRAMLista = sys.getsizeof (listaNumeros)
consumoRAMTupla = sys.getsizeof (tuplaNumeros)

print("Lista de 10 elementos: %d Bytes en RAM" %consumoRAMLista)
print("Tupla de 10 nelementos %d Bytes en RAM" %consumoRAMTupla)
