
def write_file(data,f):
    try:
        with open(f,"wt") as f1:
            f1.write(f"{data}\n")
    except Exception as e:
        print("Error, cannot write into the file")

def append_file(data,f):
    try:
        with open(f,"at") as f1:
            f1.write(f"{data}\n")
    except FileExistsError as e:
        print("Error, File not found")

def read_file(f):
    try:
        with open("output.txt","rt") as f3:
            print(f3.read())
    except FileExistsError as e:
        print("Error, File not found")


if __name__ == "__main__":
    f = "output.txt"
    #Write data
    data = input("Enter text to write in a file: ")
    write_file(data,f)

    #append data
    data2 = input("Enter text to write in a file: ")
    append_file(data2,f)

    #read file
    read_file(f)
