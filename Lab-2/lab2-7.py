def writeToFile(filename,content):
    with open(filename,'w') as file:
        file.write(content)
    print(f"Content written to {filename}")

def readFromFile(filename):
    with open(filename,'r') as file:
        content = file.read()
    return content

content="Hello This is test file.\nWelcome to the file operation in Python!"
filename="example.txt"

writeToFile(filename,content)
file_content=readFromFile(filename)
print(f"Content read from {filename}:\n{file_content}")