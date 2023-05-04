from tkinter import *
window = Tk()

print("a\ta^2\ta^3")
for i in range(1,5):
    square = i ** 2
    cube = i ** 3
    print(i, "\a", square, "\a", cube)
