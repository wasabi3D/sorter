from tkinter import *
from time import sleep
from convertisseur_en_hexadecimal import *
import threading


def sort_lst():
    for i in range(len(values2)):
        lv = i
        for j in range(i + 1, len(values2)):
            if values2[j] < values2[lv]:
                lv = j

        values2[i], values2[lv] = values2[lv], values2[i]
    print("val2 sorted")


def run():
    t1 = threading.Thread(target=long_sort)
    t1.start()


def long_sort():
    sort_lst()
    print(values2)
    decimals = 255 / values2[len(values2) - 1]
    line_space = canvas_width / len(values)
    height_multiplier = canvas_height / values2[len(values2) - 1]
    print(decimals, line_space, height_multiplier)
    for i in range(len(values)):
        lv = i
        for j in range(i + 1, len(values)):
            if values[j] < values[lv]:
                lv = j

        values[i], values[lv] = values[lv], values[i]
        print(values)
        x = 0
        lines.clear()
        c.delete("rec")
        for n in range(len(values)):
            hexa1 = decimal_hexadecimal(round(values[n] * decimals))
            color = "#" + hexa1 + "0000"
            canvas_append(x, line_space, height_multiplier, color, n)
            x += line_space
            sleep(0.01)
        if checkIfSorted(values):
            break
        sleep(0.5)
    clear_values()


def canvas_append(x, line_space, height_multiplier, color, n):
    lines.append(c.create_rectangle(x, 600-values[n] * height_multiplier, x + line_space, 600, fill=color, tag="rec"))


def canvas_delete():
    c.delete("rec")
    clear_values()

def checkIfSorted(args):
    for i in range(len(args)):
        if i!=0:
            if args[i] < args[i-1]:
                return False
    return True

def clear_values():
    values.clear()
    values2.clear()


def add_to_values():
    try:
        values.append(int(e1.get()))
        values2.append(int(e1.get()))
        e1.delete(0, END)
        print(values)
    except ValueError:
        e1.insert(10, "Not a valid num")
        sleep(1)
        e1.delete(0, END)


values = []
values2 = []
lines = []

hexadecimals = {"0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
                "10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}

window = Tk()
window.title("Sorter visualizer")
window.minsize(1080, 720)
l = Label(window)
canvas_width = 600
canvas_height = 600
c = Canvas(l, width=canvas_width, height=canvas_height, bg="#844A5E")
e1 = Entry(l)
l1 = Label(l, text="enter numbers")
b1 = Button(l, text="add number", command=add_to_values)
b2 = Button(l, text="start sorting", command=run)
resetCanvasBtn = Button(l, text="resetCanvas", command=canvas_delete)
c.grid(row=2, column=0)
e1.grid(row=0, column=1)
l1.grid(row=0, column=0)
b1.grid(row=0, column=2)
b2.grid(row=1, column=2)
resetCanvasBtn.grid(row=2, column=2)

l.pack(expand=YES)
window.mainloop()
