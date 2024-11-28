# imports
from tkinter import *
from api.send_prompt import send_prompt
from helper import read_response

# creating root window
root = Tk()
root.title("Code of Studies Info")
root.geometry('500x500')

# info label
info_label = Label(root, text='Enter question index:')
info_label.grid(row=0, sticky="w")

# index entry for user input
index_entry = Entry(root)
index_entry.grid(row=1, sticky="w")

# response label
response_label = Label(root, wraplength=500)
response_label.grid(row=3)

# method to handle button click
def clicked():
    user_input = index_entry.get()
    try:
        send_prompt(user_input)
    except Exception as ex:
        response_label.configure(text = "There is no question with the given index!")
    response = read_response(user_input)
    response_label.configure(text = " ".join(response))

# ok button
ok_button = Button(root, text = "OK" , command=clicked)
ok_button.grid(row=2, sticky="w")

root.mainloop()