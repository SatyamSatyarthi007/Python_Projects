from tkinter import *
import wikipedia

def on_press():
    q=get_q.get()
    text.insert(INSERT,wikipedia.summary(q))

root = Tk()
root.title("Wikipedia Search App")
question = Label(root, text="Wikipedia Search Result", font=("Helvetica", 16))
question.pack(pady=10)
get_q = Entry(root,bd = 5)
get_q.pack(pady=10)
submit = Button(root, text="search", command=on_press)
submit.pack(pady=10)
text=Text(root)
text.pack()

root.mainloop()

