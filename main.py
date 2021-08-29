import tkinter as tk

root = tk.Tk()
root.title("Python GUI Calculator")

text = tk.Entry(root)
text.delete(0, "end")
text.grid(row = 0, column = 0, columnspan = 5, sticky = "nsew")

def print_num(num):
	index = len(text.get())
	text.insert(index, num)

def compute():
	val = text.get()
	if "\u221A" in val:
		val = val.replace("\u221A", "")
		val += "**.5"
	if "^2" in val:
		val = val.replace("^2", "**2")
	text.delete(0,"end")
	try:
		text.insert(0, eval(val))
	except:
		text.insert(0, "ERROR")

def clear():
	text.delete(0,"end")

def delete():
	index = len(text.get())
	text.delete(index - 1)

keys = [
	["7", "8", "9", "*", "/"],
	["4", "5", "6", "-"],
	["1", "2", "3", "+"], 
	["0", ".", "^2", "\u221A"]
]

row_count = 1
col_count = 0
for row in keys:
	for col in row:
		button = tk.Button(root, text = col, width = 3, height = 3, command = lambda col = col: print_num(col))
		button.grid(row = row_count, column = col_count, sticky = "nsew")
		col_count += 1
	col_count = 0
	row_count += 1

equal = tk.Button(root, text = "=", width = 3, height = 3, command = compute)
equal.grid(row = 4, column = 4)

clear = tk.Button(root, text = "CLEAR", width = 3, height = 3, command = clear)
clear.grid(row = 3, column = 4)

delete = tk.Button(root, text = "DELETE", width = 3, height = 3, command = delete)
delete.grid(row = 2, column = 4)

root.mainloop()