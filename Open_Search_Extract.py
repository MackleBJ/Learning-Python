#Open file, count lines, search for data, extract data, average data, and output average

file_name = input('Enter file name: ')   #Prompting user for file name
file_handle = open(file_name)            #Opening file name entered

line_counter = 0
total_count = 0

for line in file_handle:                                     #Loop that reads each line of the file
    if line.startswith('X-DSPAM-Confidence:'):               #Looking for specific info within lines
        line_counter = line_counter + 1                      #Counts number of lines  found
        float_start = line.find('.') - 1                     #Determines position the float starts
        float_whole = line[float_start:]                     #Extracts the whole float from the line
        total_count = total_count + float(float_whole)       #Totals all the floats extracted
print('Average spam confidence:',total_count/line_counter)   #Prints average float value
