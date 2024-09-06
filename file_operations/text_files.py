def crete_and_write_file(filename):
    with open(filename, 'w') as file:
        file.write("This is the first line.\n")
        file.write("This is the second line.\n")
        file.write("This is the thitd line.\n")

crete_and_write_file('sample.txt')
print("file created and written successfully.")


def read_and_print_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
read_and_print_file('sample.txt')


def append_to_file(filename, new_line):
    with open(filename, 'a') as file:
        file.write(new_line + "\n")

append_to_file('sample.txt' , "this is appended line.")
print("line appended successfully")
read_and_print_file('sample.txt')

def count_words(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)
    
word_count = count_words('sample.txt')
print(f"the file containns {word_count} words.")

