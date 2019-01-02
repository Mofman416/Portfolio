import sys

################################################################################
def open_file(file_name, mode):
    #This opens the file
    try:
        file = open(file_name, mode)
    except IOError as e:
        print("Sorry, invalid operation.\n")
        input("Press enter to quit.")
        sys.exit()
    else:
        return file
################################################################################
def read_line(file):
    #Returns the next line from the trivia file, formatted
    line = file.readline()
    line = line.replace("/", "\n")
    return line

file = open_file("test_file.txt", "w")
file.write("this/is/a/Test")
file.close()
file = open_file("test_file.txt", "r")
line = read_line(file)
print(line)
