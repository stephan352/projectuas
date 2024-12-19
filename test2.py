import tkinter
import tkinter.ttk

root = tkinter.Tk()

cat = tkinter.PhotoImage(file="catpng.png")
cat.zoom(25)
cat.subsample(32)

table = tkinter.ttk.Treeview(root, columns=(1,2,3), show="tree")
table.pack()


table.insert(parent="", index=tkinter.END, values=(67,56,23))
table.insert(parent="", index=tkinter.END, image=cat)

root.mainloop()