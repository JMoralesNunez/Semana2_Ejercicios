licencia = input("tienes licencia? (Y/N) ")
casco = input("tienes casco? (Y/N) ")

if licencia  != "Y" or casco != "Y":
    print("No puedes conducir")
else:
    print("Puedes conducir")