# This program takes information from a file containing a catalog of CDs 
# and prints the menu, number of items and average price

import xml.etree.ElementTree as ET
import os


def get_catalog(file_name):
    try:
        with open(file_name, 'r') as open_file:
            catalog = open_file.read()
        filesize = os.path.getsize(file_name)
        if filesize == 0:
            print("The file is empty, exiting code")
            exit()
        else:
            
            return catalog
    except:
        print("There was an error reading the file.")

def get_title_list(catalog):
    title_list = []
    print(catalog)
    information_file = ET.fromstring(catalog)
    title_list = information_file.findall('CATALOG/CD/TITLE').text

    return title_list










def main():
    file_name = "cd_catalog.xml"
    catalog = get_catalog(file_name)
    title_list = get_title_list(catalog)
    
    
    
    
    
main()    
