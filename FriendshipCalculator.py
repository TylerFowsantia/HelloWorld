from tkinter import *
import random

root = Tk()
root.title("Friendship Calculator -TF")
root.geometry("425x250")


def reply():
    percentage = random.randrange(0, 100)
    x = person1_name.get()
    y = person2_name.get()
    if len(x.split()) == 0 and len(y.split()) == 0:
        answer.set("Please provide two names.")
    elif len(x.split()) == 0 or len(y.split()) == 0:
        answer.set("Please provide another person's name.")
    else:
        if percentage <= 25:
            answer.set("These two people are {}% compatible and they aren't coo.".format(percentage))
            answer_box.config(fg="red")
        elif percentage <= 50:
            answer.set("These two people are {}% compatible and they coo.".format(percentage))
            answer_box.config(fg="orange")
        elif percentage <= 75:
            answer.set("These two people are {}% compatible and they fren.".format(percentage))
            answer_box.config(fg="green")
        elif percentage <= 100:
            answer.set("These two people are {}% compatible and they super fren.".format(percentage))
            answer_box.config(fg="darkgreen")


# Widgets
person1_label = Label(text="Person 1:", fg="red")
person1_name = Entry(root, width=30)
person2_label = Label(text="Person 2:", fg="blue")
person2_name = Entry(root, width=30)
test_button = Button(text="Test Friendship", bg="green", fg="white", command=reply)
answer = StringVar()
answer.set('')
answer_box = Label(root, textvariable=answer)
# Grid Assignment
person1_label.grid(row=0, sticky=E)
person1_name.grid(row=0, column=1, ipadx=10)
person2_label.grid(row=1, sticky=E)
person2_name.grid(row=1, column=1, ipadx=10)
test_button.grid(row=2)
answer_box.grid(rowspan=2, column=1)
root.mainloop()
