from tkinter import *

window = Tk()
window.title('First GUI Program!!')
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

def calculate():
    miles = float(mile_entry.get())
    km = miles * 1.609344
    km_value.config(text=f"{km}")


mile_entry = Entry(width=10, justify='left')
mile_entry.insert(END, string="0")
mile_entry.grid(row=0, column=1)

miles_label = Label(text='Miles', font=('Arial', 10, 'normal'))
miles_label.config(padx=5, pady=5)
miles_label.grid(row=0, column=2)

is_equal_to_label = Label(text='is equal to', font=('Arial', 10, 'normal'))
is_equal_to_label.config(padx=5, pady=5)
is_equal_to_label.grid(row=1, column=0)

km_value = Label(text='0', font=('Arial', 10, 'normal'))
km_value.config(padx=5, pady=5)
km_value.grid(row=1, column=1)

km_label = Label(text='Km', font=('Arial', 10, 'normal'))
km_label.config(padx=5, pady=5)
km_label.grid(row=1, column=2)

calculate_button = Button(text='Calculate', command=calculate)
calculate_button.grid(row=2, column=1)

window.mainloop()