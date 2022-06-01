import random
while True:
    print("1. roll the die\n 2. Exit")
    user = int(input("what you want to do \n"))
    if user <= 6:
        number = random.randint(1,6)
        print(number)
    else:
        break