# Task 1

def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

length = float(input("Enter length of rectangle:"))
width = float(input("Enter width of rectangle:"))

X, Y = calc_rectangle(length, width)

print(f"Area:{X}, Perimeter:{Y}")

# Task 2




