def hello():
    print("Hello")

def read_file():
    file = open('test/test.txt','r')
    contents=file.read()
    return contents

def append_file():
    file = open('test/test.txt','a+')
    file.write("Hello\n")
    file.close()

def erase_file():
    f = open('test/test.txt', 'r+')
    f.truncate(0)  # need '0' when using r+


