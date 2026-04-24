file = open("sample.txt", "w")
file.write("Hello, this is the first line in the file.\n")
file.write("File handling in Python is easy to learn.\n")
file.close() # Closing the file
print("Data written successfully.\n")

file = open("sample.txt", "r")
print("Reading file contents:")
content = file.read()
print(content)
file.close()

file = open("sample.txt", "a")
file.write("This line is added using append mode.\n")
file.close()
print("\nData appended successfully.\n")

file = open("sample.txt", "r")
print("Updated file contents:")
print(file.read())
file.close()
