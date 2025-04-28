list = [5,4,3,2,1]
num = int(input("Enter  the number: "))

if num in list:
    pos = list.index(num)
    print(pos)
else:
    print("No está en la lista")