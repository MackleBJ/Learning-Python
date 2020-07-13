#Open file, .split() lines into words, .append() to another list, then check for any duplicates.

file_name = input("Enter file name: ")       #Requests what file to open
file_handle = open(file_name)
line_split = []
bank = []

for line in file_handle:                     #Splits each word, in the line, into individual indexies of a list
    line_split = line_split + line.split()

for x in line_split:                         #Adds words to another list
    if bank.count(x) == 0:                   #Check that no word is in the list more than once
        bank.append(x)

bank.sort()                                  #Permanently, alphabetically sorts the list
print(bank)
