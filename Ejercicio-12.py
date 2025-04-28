frutas = ["mango", "manzana", "aguacate"]
print(frutas)

delete = input("Enter the name of the fruit you want to delete: ")

if delete in frutas:
    frutas.remove(delete)
    print(frutas)
else:
    print("item no encontrado")