import json
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_password = {
        website: {
            'email': email,
            'password': password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title='Oops', message='Please don\'t leave any fields empty')
    else:
        try:
            with open('passwords.json', mode='r') as password_file:
                passwords = json.load(password_file)
        except FileNotFoundError:
            with open('passwords.json', mode='w') as password_file:
                json.dump(new_password, password_file, indent=4)
        else:
            passwords.update(new_password)
            with open('passwords.json', mode='w') as password_file:
                json.dump(passwords, password_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def search():
    website = website_entry.get()
    if len(website.rstrip(' ')) == 0:
        messagebox.showerror(title='Error', message='Please input a website to search.')
    else:
        try:
            with open('passwords.json', mode='r') as password_file:
                password_data = json.load(password_file)
        except FileNotFoundError:
            messagebox.showerror(title='Error', message='No data file found.')
        else:
            if website in password_data:
                email = password_data[website]['email']
                password = password_data[website]['password']
                messagebox.showinfo(title=website, message=f'Email: {email}\n'
                                                           f'Password: {password}')
            else:
                messagebox.showerror(title=website, message=f'No password found for {website}')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
my_pass_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=my_pass_image)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()
email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, 'zgjohnson94@gmail.com')
password_entry = Entry()
password_entry.grid(row=3, column=1, sticky='EW')

generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(row=3, column=2, sticky='EW')

add_button = Button(text='Add', command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky='EW')

search_button = Button(text='Search', command=search)
search_button.grid(row=1, column=2, sticky='EW')
window.mainloop()
