Letra = input("Introduce una letra del abecedario \n")
Listadeletras = ["A", "B", "C"]
Letramay= Letra.upper()

while Letramay not in Listadeletras:
    Letra = input ("Dame otra opcion \n")
    if Letramay in Listadeletras:
            print("Esta opcion es valida")
        
