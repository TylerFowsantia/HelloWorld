from tkinter import *

root = Tk()
root.title("BMI Calculator -TF")
root.geometry("300x150")


def calculate_bmi():
    float_w = float(enter_weight.get())
    float_h = float(enter_height.get())
    bmi = float_w / float_h ** 2
    bmi = round(bmi, 2)
    if bmi < 18.5:
        end_result1.set(bmi)
        end_result2.set("You are underweight! Go eat food.")
    elif 18.5 <= bmi <= 24.9:
        end_result1.set(bmi)
        end_result2.set("You are normal! Keep it up!")
    elif 25 <= bmi <= 29.9:
        end_result1.set(bmi)
        end_result2.set("You are overweight! Exercise more!")
    elif bmi >= 30:
        end_result1.set(bmi)
        end_result2.set("You are obese! Go see a doctor.")


# Widgets
w = Label(text="Weight(kg):", fg="blue")
h = Label(text="Height(m):", fg="blue")
enter_weight = Entry(root)
enter_height = Entry(root)
button1 = Button(text="Calculate", fg="blue", command=calculate_bmi)
end_result1 = StringVar()
end_result1.set('')
end_result2 = StringVar()
end_result2.set('')
result1 = Label(root, textvariable=end_result1)
result2 = Label(root, textvariable=end_result2)
# Grid Assignment
w.grid(row=0, sticky=E)
h.grid(row=1, sticky=E)
enter_weight.grid(row=0, column=1)
enter_height.grid(row=1, column=1)
button1.grid(row=2, column=1)
result1.grid(row=3, column=1)
result2.grid(row=4, column=1)
root.mainloop()
