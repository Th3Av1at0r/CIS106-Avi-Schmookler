# This program takes information from a file containing a catalogue of CDs 
# and prints the menu, number of items and average price

import xml.etree.ElementTree as ET
import os


def get_catalogue(file_name):
    try:
        with open(file_name, 'r') as open_file:
            catalogue = open_file.read()
        filesize = os.path.getsize(file_name)
        if filesize == 0:
            print("The file is empty, exiting code")
            exit()
        else:
            
            return catalogue
    except:
        print("There was an error reading the file.")

def get_title_list(catalogue):
    title_list = []
    print(catalogue)
    information_file = ET.parse(catalogue)
    title_list = information_file.findall('CATALOGUE/CD/TITLE').text

    return title_list










def main():
    file_name = "cd_catalog.xml"
    catalogue = get_catalogue(file_name)
    title_list = get_title_list(catalogue)
    
    
    
    
    
main()    
