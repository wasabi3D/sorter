# from main import *
from time import sleep


def sort_lst(lst):
    for i in range(len(lst)):
        lv = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[lv]:
                lv = j

        lst[i], lst[lv] = lst[lv], lst[i]


def long_sort(lst):
    for i in range(len(lst)):
        lv = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[lv]:
                lv = j

        lst[i], lst[lv] = lst[lv], lst[i]


def add_to_values(val, lst1, lst2, cv):
    try:
        lst1.append(int(val))
        lst2.append(int(val))
        sort_lst()
        d = lst2[len(lst2) - 1] / 255
        rw = cv / (len(lst) + 10)
    except ValueError:
        e1.insert(10, "Not a valid num")
        sleep(2)
        e1.delete(0, END)
