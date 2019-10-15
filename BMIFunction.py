def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi < 18.5:
        print(bmi)
        return print("You are underweight! Go eat food.")
    elif 18.5 <= bmi <= 24.9:
        print(bmi)
        return print("You are normal! Keep it up!")
    elif 25 <= bmi <= 29.9:
        print(bmi)
        return print("You are overweight! Exercise more!")
    elif bmi >= 30:
        print(bmi)
        return print("You are obese! Go see a doctor.")


w = float(input("Weight: "))
h = float(input("Height: "))
bmi(w, h)
