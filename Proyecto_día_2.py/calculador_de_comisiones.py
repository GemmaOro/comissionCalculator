nombre = input("¿Cuál es tu nombre? ")
numero_ventas = int(input("Número total de ventas este mes: "))
comisiones = round(numero_ventas*13/100,2)


print(f"Felicitaciones {nombre}, tus comisiones para este mes son de {comisiones} euros!")