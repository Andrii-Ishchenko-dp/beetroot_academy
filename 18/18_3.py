#Write a program that counts lines and characters in a file (similar to `wc` Unix-utility, for additional info about it follow the link: https://www.geeksforgeeks.org/wc-command-linux-examples/ or in case you have macOS or Linux - just call manual for this utility via command: `man wc`).

 #Create a Python module called `mymod.py`, which has three functions:

#count_lines(name) function that reads an input file and counts the number of lines in it (hint: file.readlines() does most of the work for you, and `len` does the rest) 
#count_chars(name) function that reads an input file and counts the number of characters in it (hint: file.read() returns a single string)
#test(name) function that calls both counting functions with a given input file­name. Such a filename generally might be passed-in, hard-coded, input with raw_input, or pulled from a command-line via the sys.argv list; for now, assume it’s a passed-in function argument.



def count_lines(filename):
    with open(filename) as file:
        sim = [row.rstrip() for row in file]
        print('Количество строк: {}'.format(len(sim)))

def count_chars(filename):
    with open(filename) as file:
        s = file.read()
        print('Количество символов:' + ' ' + str(len(s)))

def test(filename):
    count_lines(filename)
    count_chars(filename)

test('file1')
