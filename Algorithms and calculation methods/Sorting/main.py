from tkinter import *
from functions import *


class Lab_two:
    def begin(self):
        def first_window():

            self.root1 = Toplevel(self.root)
            self.root1.title("Array Sorting")
            self.root.geometry("450x300")
            Label(self.root1, font="Arial 12", text="Enter the array").grid(
                row=0, column=1, columnspan=3)

            entC = Entry(self.root1, font="Arial 11", width=20)
            entC.grid(row=4, column=1)
            self.root1.mainloop()

        def second_window():

            self.root2 = Toplevel(self.root)
            self.root2.title("Sorting 10 Arrays")
            self.root2.geometry("300x200")
            Label(self.root2, font="Arial 12", text="If b/z>d then y=sin(w*f)\nOtherwise y=cos(w*f)").grid(
                row=0, column=1)

            self.root2.mainloop()

        self.root = Tk()
        self.root.title("Lab Work 2")
        self.root.geometry("225x200")
        Label(self.root, font="Arial 13",
              text="Selection Sort").grid(row=0, column=1)
        Button(self.root, font="Arial 11", text="Array Sorting",
               command=first_window, width=23).grid(row=1, column=1)
        Button(self.root, font="Arial 11", text="Sorting 10 Arrays",
               command=second_window, width=23).grid(row=2, column=1)
        self.root.mainloop()


Lab_two().begin()
