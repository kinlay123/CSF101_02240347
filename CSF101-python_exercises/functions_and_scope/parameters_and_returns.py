def greet_with_default(name="Guest"):
    print(f"hello, {name}!")

greet_with_default()
greet_with_default("Bob")

def calculate_rectangle_area(width, height):
    return width * height

area = calculate_rectangle_area(5, 3)
print(f"the area of the rectanglr is: {area}")

def print_info(**kwrags):
    for key, value in kwrags.items():
        print(f"{key}: {value}")
print_info(name="alice", age=30, city="new york")

def min_max(numbers):
    return min(numbers), max(numbers)

result = min_max([5, 2, 8, 1, 9])
print(f"min: {result[0]}, max: {result[1]}")

def safe_divide(a, b):
    if b == 0:
        return"cannot divide by 0"
    return a / b
print(safe_divide(10, 2))
print(safe_divide(5, 0))



