from tkinter import*

tester = Tk()


def close_window():
    exit()


button = Button(tester, text="Close", command=close_window)

button.pack()

mainloop()
