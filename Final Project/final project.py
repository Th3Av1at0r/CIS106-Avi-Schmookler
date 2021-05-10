# This program takes information from a file containing a catalogue of CDs 
# and prints the menu, number of items and average price

def get_catalogue(filename):
    try:
        import os
        catalogue = open(filename, "r")
        filesize = os.path.getsize(filename)
        if filesize == 0:
            print("The file is empty, exiting code")
            exit()
    
    return catalogue

def get_title_list(catalogue):
    title_list = []
    information_file = ET.fromstring(catalogue)
    title_list.append(catalogue.find('TITLE').text)
    

    return title_list










def main():
    filename = "cd_catalog.xml"
    import xml.etree.ElementTree as ET
    information_file = get_information_file(filename)
    title_list = get_title_list(information_file)
    print(title_list)
    
    
    
    
    
main()    
    
