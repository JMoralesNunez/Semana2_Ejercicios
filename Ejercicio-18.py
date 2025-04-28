list = [1,3,5,6,8,3,2,5]
print(list)

num = int(input("Enter the number you would like to add: "))

position = int(input("Enter the position you would like to the number to be: "))
position = position - 1  #Para que usuario ingrese la posición sin contar el 0

list.insert(position, num)

print(list)