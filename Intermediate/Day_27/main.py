from tkinter import *

window = Tk()
window.title('First GUI Program!!')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = Label(text='I Am a Label', font=('Arial', 24, 'italic bold'))
my_label.config(pady=50, padx=50)
my_label.grid(row=0, column=0)


def button_clicked():
    my_label.config(text=user_input.get())


my_button = Button(text='Click Me', command=button_clicked)
my_button.grid(row=1, column=1)

new_button = Button(text='New Button', command=button_clicked)
new_button.grid(row=0, column=2)

user_input = Entry(width=10)
user_input.grid(row=2, column=3)

window.mainloop()
