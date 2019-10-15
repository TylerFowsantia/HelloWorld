import random
a = (random.randrange(1, 50))
b = (random.randrange(1, 50))
attempts_left = 3
attempts = 1
print(a, b)
print("")
while True:
    print("I am thinking of 2 numbers between 1 and 50...")
    a2, b2 = int(input("a: ")), int(input("b: "))
    if a2 == a and b2 == b:
        print("Good Job!")
        print("You completed in {0} attempts!".format(attempts))
        break
    elif a2 == a and b2 < b:
        print(f"{a2} is correct, however {b2} is too low!")
        print("")
        print("Try again!")
        attempts += 1
        attempts_left -= 1
        print("Attempts left =", attempts_left)
    elif a2 == a and b2 > b:
        print(f"{a2} is correct, however {b2} is too high!")
        print("")
        print("Try again!")
        attempts += 1
        attempts_left -= 1
        print("Attempts left =", attempts_left)
    elif a2 < a and b2 == b:
        print(f"{a2} is too low, but {b2} is correct.")
        print("")
        print("Try again!")
        attempts += 1
        attempts_left -= 1
        print("Attempts left =", attempts_left)
    elif a2 > a and b2 == b:
        print(f"{a2} is too high, but {b2} is correct.")
        print("")
        print("Try again!")
        attempts += 1
        attempts_left -= 1
        print("Attempts left =", attempts_left)
    elif (a - 3) < a2 < (a + 3) and (b - 3) < b2 < (b + 3):
        print("Both a and b values are close!")
        attempts += 1
        attempts_left -= 1
        print("Attempts left =", attempts_left)
    elif (a - 3) < a2 < (a + 3):
        print("a value is close!")
        attempts += 1
        attempts_left -= 1
        print("Attempts left =", attempts_left)
    elif (b - 3) < b2 < (b + 3):
        print("b value is close!")
        attempts += 1
        attempts_left -= 1
        print("Attempts left =", attempts_left)
    else:
        print(f"Both a and b values are incorrect!")
        print("")
        print("Try again!")
        attempts += 1
        attempts_left -= 1
        print("Attempts left =", attempts_left)
    if attempts_left == 0:
        print("You lose :(")
        break
    else:
        continue
