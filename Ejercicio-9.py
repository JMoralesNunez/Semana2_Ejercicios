nota = float(input("enter your grade (0-10): "))

if nota >= 7:
    print("Sobresaliente")
elif nota < 7 and nota >= 5:
    print("Aprobado")
elif nota < 5:
    print("Suspende")
else:
    print("Nota no válida")