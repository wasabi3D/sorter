hexadecimals = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
                10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}


def decimal_hexadecimal(num):
    b = num
    q = b // 16
    r = b % 16
    return hexadecimals[q]+hexadecimals[r]


