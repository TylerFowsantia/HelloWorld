from tkinter import *
import random

answer_choices = ["Yes", "Probably not", "Maybe", "Absolutely", "Nope", "Ask me tomorrow"]

root = Tk()
root.title("Magic 8Ball -TF")
root.geometry("300x150")


def eight_ball_reply():
    ran_ans = random.choice(answer_choices)
    x = question.get()
    if "?" in x:
        answer.set(ran_ans)
    else:
        answer.set("Please provide a question")


# Widgets
question_label = Label(text="Ask a question:")
question = Entry(root, width=30)
ask_button = Button(text="Ask Question", command=eight_ball_reply)
answer = StringVar()
answer.set('')
box = Label(root, textvariable=answer)
# Grid Assignment
question_label.grid(row=0, sticky=E)
question.grid(row=0, column=1, ipadx=10)
ask_button.grid(row=1)
box.grid(row=2)
root.mainloop()
