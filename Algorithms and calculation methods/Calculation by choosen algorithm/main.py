from tkinter import *
from tkinter import messagebox
from algorithms import *
from pickle import load, dump


class Lab_one:
    def begin(self):
        def first_window():
            def from_file():
                upload(1, [entA, entB, entC])

            def calculation():
                a = float(entA.get())
                b = float(entB.get())
                c = float(entC. get())
                y = first_alg(a, b, c)
                messagebox.showinfo("Результат", y)
            self.root1 = Toplevel(self.root)
            self.root1.title("Перший алгоритм")
            self.root.geometry("450x300")
            Label(self.root1, font="Arial 12", text="Y = (a*c)^2+(b*c)^3+(с*с)^4").grid(
                row=0, column=1, columnspan=3)
            Label(self.root1, font="Arial 13", text="A:").grid(row=2, column=0)
            Label(self.root1, font="Arial 13", text="B:").grid(row=3, column=0)
            Label(self.root1, font="Arial 13", text="C:").grid(row=4, column=0)
            entA = Entry(self.root1, font="Arial 13", width=20)
            entB = Entry(self.root1, font="Arial 13", width=20)
            entC = Entry(self.root1, font="Arial 13", width=20)
            entA.grid(row=2, column=1)
            entB.grid(row=3, column=1)
            entC.grid(row=4, column=1)
            Button(self.root1, font="Arial 13",
                   text="Завантажити", command=from_file, width=15).grid(row=5, column=1)
            Button(self.root1, font="Arial 13",
                   text="Розрахувати", command=calculation, width=15).grid(row=6, column=1)
            self.root1.mainloop()

        def second_window():

            def from_file():
                upload(2, [entZ, entB, entD])

            def calculation():
                z = float(entZ.get())
                b = float(entB.get())
                d = float(entD. get())
                y = second_alg(b, z, d)
                messagebox.showinfo("Результат", y)

            self.root2 = Toplevel(self.root)
            self.root2.title("Другий алгоритм")
            self.root2.geometry("300x200")
            Label(self.root2, font="Arial 12", text="Якщо b/z>d то y=sin(w*f)\nВ іншому випадку y=cos(w*f)").grid(
                row=0, column=1)
            Label(self.root2, font="Arial 13", text="Z:").grid(row=2, column=0)
            Label(self.root2, font="Arial 13", text="B:").grid(row=3, column=0)
            Label(self.root2, font="Arial 13", text="D:").grid(row=4, column=0)
            entZ = Entry(self.root2, font="Arial 13", width=20)
            entB = Entry(self.root2, font="Arial 13", width=20)
            entD = Entry(self.root2, font="Arial 13", width=20)
            entZ.grid(row=2, column=1)
            entB.grid(row=3, column=1)
            entD.grid(row=4, column=1)
            Button(self.root2, font="Arial 13",
                   text="Завантажити", command=from_file, width=13).grid(row=5, column=1)
            Button(self.root2, font="Arial 13",
                   text="Розрахувати", command=calculation, width=13).grid(row=6, column=1)
            self.root2.mainloop()

        def third_window():
            def from_file():
                upload(3, [entA, entB])

            def calculation():
                a = int(entA.get())
                b = int(entB.get())
                y = third_alg(a, b)
                messagebox.showinfo("Результат", y)

            self.root3 = Toplevel(self.root)
            self.root3.title("Третій алгоритм")
            self.root3.geometry("300x200")
            Label(self.root3, font="Arial 12", text="f=a!*b/(a-b)!").grid(
                row=1, column=1)
            Label(self.root3, font="Arial 13", text="A:").grid(row=2, column=0)
            Label(self.root3, font="Arial 13", text="B:").grid(row=3, column=0)
            entA = Entry(self.root3, font="Arial 13", width=20)
            entB = Entry(self.root3, font="Arial 13", width=20)
            entA.grid(row=2, column=1)
            entB.grid(row=3, column=1)
            Button(self.root3, font="Arial 13",
                   text="Завантажити", command=from_file, width=13).grid(row=4, column=1)
            Button(self.root3, font="Arial 13",
                   text="Розрахувати", command=calculation, width=13).grid(row=5, column=1)
            self.root3.mainloop()

        def upload(number, space):
            with open(f"entries.txt", "rb") as f:
                entries = load(f)
                for i in range(len(space)):
                    space[i].delete(0, END)
                    space[i].insert(0, entries[f"{number}"][i])
                self.entries = entries

        self.root = Tk()
        self.root.title("Лабораторна робота 1")
        self.root.geometry("425x200")
        Label(self.root, font="Arial 13",
              text="Оберіть алгоритм").grid(row=0, column=1)
        Button(self.root, font="Arial 11", text="Перший",
               command=first_window, width=13).grid(row=1, column=0)
        Button(self.root, font="Arial 11", text="Другий",
               command=second_window, width=13).grid(row=1, column=1)
        Button(self.root, font="Arial 11", text="Третій",
               command=third_window, width=13).grid(row=1, column=2)
        self.root.mainloop()

        def save(number, value):
            with open(f"entries.txt", "wb") as f:
                self.entries[f"{number}"] = value
                dump(self.entries, f)

        save(1, ['1', '2', '3'])
        save(2, ['1', '2', '3'])
        save(3, ['1', '2'])
    entries = {}


Lab_one().begin()
