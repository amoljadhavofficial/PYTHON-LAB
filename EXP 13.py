# Step 1: Open file in write mode and write data
file_w = open("FileHandling.txt", "w")
file_w.write("Welcome to Python File Handling Session.\n")
file_w.write("This file demonstrates write operation in File Handling Session.\n")
file_w.close()

print("Write Operation is completed.\n")


# Step 2: Open file in read mode and read data
file_o = open("FileHandling.txt", "r")
content = file_o.read()

print("Reading a content from file(FileHandling.txt):")
print(content)

file_o.close()
print("The open operation is completed.\n")


# Step 3: Open file in append mode and add new data
file_a = open("FileHandling.txt", "a")
file_a.write("\nThis concept is applicable to FYMCA students\n")
file_a.close()

print("The append operation is completed.\n")


# Step 4: Read updated file content
file = open("FileHandling.txt", "r")
updated_content = file.read()

print("The updated file content")
print(updated_content)

file.close()