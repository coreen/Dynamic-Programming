# Coreen Yuen
# global constant
SCALE_FACTOR = 3

# outputs a triangle
def triangle():
    for row in range(1,(2 * SCALE_FACTOR)):
        for spaces in range((2 * SCALE_FACTOR), row, -1):
            print(" ", end = "")
        for FrontSlashes in range(0, row):
            print("/", end = "")
        print("**", end = "")
        for backslashes in range(0, row):
            print("\\", end = "")
        print()

# outputs a line
def line():
    print("+", end = "")
    for line in range(0,(2 * SCALE_FACTOR)):
        print("=*", end = "")
    print("+", end = "")
    print()

# outputs top of square1/bottom of square2
def top():
    for row1 in range(1, (SCALE_FACTOR + 1)):
        print("|", end = "")
        for dots1 in range(0, (SCALE_FACTOR - row1)):
            print(".", end = "")
        for slashes1 in range(0, row1):
            print("/\\", end = "")
        for dots2 in range(0, (-2 * row1 + 2 * SCALE_FACTOR)):
            print(".", end = "")
        for slashes2 in range(0, row1):
            print("/\\", end = "")
        for dots3 in range(0, (SCALE_FACTOR - row1)):
            print(".", end = "")
        print("|", end = "")
        print()

# outputs bottom of square1/top of square2
def bottom():
    for row2 in range(SCALE_FACTOR, 0, -1):
        print("|", end = "")
        for dots4 in range(0, (SCALE_FACTOR - row2)):
            print(".", end = "")
        for slashes3 in range(0, row2):
            print("\\/", end = "")
        for dots5 in range(0, (-2 * row2 + 2 * SCALE_FACTOR)):
            print(".", end = "")
        for slashes4 in range(0, row2):
            print("\\/", end = "")
        for dots6 in range(0, (SCALE_FACTOR - row2)):
            print(".", end = "")
        print("|", end = "")
        print()

# outputs first square of the rocket
def square1():
    top()
    bottom()

# outputs second square of the rocket
def square2():
    bottom()
    top()

# main
triangle()
line()
square1()
line()
square2()
line()
triangle()
