import re
Document = "CAP1/dictionary.txt"
with open (Document, "r",encoding="utf-8") as file:
    Dict = file.read ()

eliminated_dict = re.sub (r'[a-zA-Z-0-9]+|[^\w\s]', '', dict)

with open (Document, "w",encoding="utf-8") as file:
    file.write (eliminated_dict)

print ("Eliminated")