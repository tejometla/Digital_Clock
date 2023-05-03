from tkinter import Tk, Label


window = Tk()
window.title("Digital Clock")
window.geometry("600x300")

Label = Label(window, font=("Arial Black",78,"bold"), bg="steelblue", fg="white")
Label.pack(pady=100)

window.mainloop()