list = []

for i in range(5):
    num = int(input("Enter a number: "))
    list.append(num)


even = []

for i in list:
    if i%2 == 0:
        even.append(i)

print(f"The even numbers are: {even}")