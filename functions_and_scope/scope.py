x = 10

def print_x():
    x =20
    print(f"Local c: {x}")

print_x()
print(f"global x: {x}")

def increment():
    global count
    count += 1
    print(f"Count: {count}")

increment()
increment()
print(f"final count: {count}")

def outer():
    x = "outer"

    def inner():
        nonlocal x 
        x = "inner"
        print(f"inner x: {x}")

    inner()
    print(f"outer x: {x}")

outer()        





    