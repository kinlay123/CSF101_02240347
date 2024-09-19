def create_binary_file(filename):
    data = bytes([0, 1, 2, 3, 4, 5])
    with open(filename, 'wb') as file:
        file.write(data)
create_binary_file('bimary_sample.bin')
print("binary file created successfully")


def read_binary_file(filename):
    with open(filename, 'rb') as file:
        content = file.read()
        print("binary content:", content)

    read_binary_file('binary_sample,bin')

def append_to_binary_file(filename, data):
    with open(filename, 'ab') as file:
        file.write(data)

append_to_binary_file('binary_sample.bin', bytes([6, 7, 8, 9]))
print("Bytes appended to binary file.")
read_binary_file('binary_sample.bin') 

