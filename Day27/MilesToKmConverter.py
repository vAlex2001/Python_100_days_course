from tkinter import *

MULTIPLIER = 1.6

def button_clicked():
    new_text = miles_input.get()
    miles = int(new_text)
    kilometres = miles * MULTIPLIER
    kilometer_result.config(text=f"{kilometres}")

# Window
window = Tk()
window.title("Miles to kilometres converter.")
window.config(padx=20, pady=20)

# Input
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)


# Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Label
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

# Label
kilometer_result = Label(text="0")
kilometer_result.grid(column=1, row=1)

# Label
kilometer_label = Label(text="KM")
kilometer_label.grid(column=2, row=1)

# Button
calculate_button = Button(text="Convert", command=button_clicked)
calculate_button.grid(column=1, row=2)

window.mainloop()