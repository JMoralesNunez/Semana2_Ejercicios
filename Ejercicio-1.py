password = "1234"

while True:
    guess = input("Please enter your password: ")
    if guess == password:
        print("Correct password")
        break
    else:
        print("wrong password, try again")
