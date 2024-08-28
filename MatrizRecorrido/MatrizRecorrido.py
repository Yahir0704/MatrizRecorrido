print("Este programa es capaz de leer y mostrar una matriz.")

maxf = 3  
maxc = 5  


a = [[0.0 for _ in range(maxc)] for _ in range(maxf)]


for f in range(maxf):
    for c in range(maxc):
        a[f][c] = float(input(f"Ingrese el valor para la posición [{f + 1}][{c + 1}]: "))



print("La matriz ingresada es:")
for f in range(maxf):
    for c in range(maxc):
        print(f"{a[f][c]:.2f}", end=" ")
    print()  
