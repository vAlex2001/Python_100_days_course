import tkinter

# window  = tkinter.Tk()
# window.title("First GUI")
# window.minsize(width=500, height=500)

# # Label
# my_label = tkinter.Label(text = "Label", font=("Arial", 24, "bold"))
# my_label.pack()

# window.mainloop()

# Unlimited positional arugments *args
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,2,3,34,2,5,2))

def calculate(n, **kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)
        n += kwargs["add"]
        n += kwargs["multiply"]
        print(n)

calculate(2, add=3, multiply=5)