#!/usr/bin/env python3
# Author ID: nrihani




def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
   
    f = open(file_name, 'r')               
    read_data = f.read()                   
    f.close()    
    return read_data

def read_file_list(file_name):
    
    f = open(file_name, 'r')               
    read_data = f.read()
    f.close()
    list_of_lines = read_data.split('\n')
    list_of_lines.remove('')    #I decided to add this because anything else would provide a blank space as the last list item, this way it removes any blank list items
    return list_of_lines

    
if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))