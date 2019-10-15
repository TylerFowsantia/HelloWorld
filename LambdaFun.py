square = lambda x: x * x
def square():
    x * x
print(square(5))
print("------------------------------")
# ----------------------------------------
add = lambda a, b: a + b

print(add(2, 7))
print("-----------------------------")
# ----------------------------------------
area = lambda b, h: (b * h) / 2

print(area(5, 2))
print("------------------------------")
# -----------------------------------------
slicer = lambda l, i: l[0:i]

print(slicer("Take one down and pass it around, 1 bottle of Pepsi on the wall.", 19))
print("-----------------------------")
# -----------------------------------------
bmi_calc = lambda w, he: w / he ** 2
bmi = bmi_calc(120, 1.6)
if bmi < 18.5:
    print(bmi)
    print("You are underweight! Go eat food.")
elif 18.5 <= bmi <= 24.9:
    print(bmi)
    print("You are normal! Keep it up!")
elif 25 <= bmi <= 29.9:
    print(bmi)
    print("You are overweight! Exercise more!")
elif bmi >= 30:
    print(bmi)
    print("You are obese! Go see a doctor.")
