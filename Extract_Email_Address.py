#Extract email addresses from email data

file_name = input('Enter file name: ')      #Requests file to open
file_handle = open(file_name)               #Opens file entered

address_count = 0                           #var to track number of lines with 'From'

for line in file_handle:
    if line.startswith('From:'):            #We don't want 'From:' lines, just 'From'
        continue
    elif line.startswith('From'):
        line_data = line.split()
        print(line_data[1])                 #Prints email address
        address_count = address_count + 1
print(f'There were {address_count} lines in the file with From as the first word')
