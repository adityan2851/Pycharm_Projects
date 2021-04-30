import tkinter

window = tkinter.Tk()
window.title("Mile to km Convertor")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

def button_clicked():
    mile = float(input.get())
    Km = mile * 1.609
    number.config(text=f"{Km}")


label = tkinter.Label(text="Miles", font=("Arial", 10, "bold"))
label.grid(row=0, column=2)

new_label = tkinter.Label(text="is equal to",font=("Arial", 10, "bold"))
new_label.grid(row=1, column=0)

number = tkinter.Label(text="0", font=("Arial", 10, "bold"))
number.grid(row=1, column=1)

km = tkinter.Label(text="km", font=("Arial", 10, "bold"))
km.grid(row=1, column=2)

button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)

input = tkinter.Entry(width=10)
input.grid(row=0, column=1)




window.mainloop()