age = int(input("Enter your age: "))

if age >= 50:
    print("Anciano")
elif age <= 49 and age >= 18:
    print("Adulto")
elif age <= 17 and age >=12:
    print("Adolescente")
else:
    print("Niño")