# This program takes information from a file containing a catalogue of CDs 
# and prints the menu, number of items and average price

def get_information_file(filename):
    try:
        import os
        information_file = open(filename, "r")
        filesize = os.path.getsize(filename)
        if filesize == 0:
            print("The file is empty, exiting code")
            exit()
        else:
            next(information_file)
            next(information_file)
            
    except IOError:
        print("Error, file not accessible")
        exit()
    
    return information_file

def get_title_list(information_file):
    title_list = []
    for line in information_file:
        if line.find("<TITLE>") != -1:
            lne_strp_1 = line.strip("<TITLE>")
            lne_strp_2 = lne_strp_1.strip("\n")
            title_list.append(lne_strp_2)
        else:
            continue
        
    return title_list

def get_artist_list(information_file):
    artist_list = []
    for line in information_file:
        if line.find("<ARTIST>") != -1:
            lne_strp_1 = line.strip("<ARTIST>")
            lne_strp_2 = lne_strp_1.strip("\n")
            artist_list.append(lne_strp_2)
        else:
            continue
    return artist_list
    
def get_country_list(information_file):
    country_list = []
    for line in information_file:
        if line.find("<COUNTRY>") != -1:
            lne_strp_1 = line.strip("<COUNTRY>")
            lne_strp_2 = lne_strp_1.strip("\n")
            country_list.append(lne_strp_2)
        else:
            continue
        
    return country_list

def get_company_list(information_file):
    company_list = []
    for line in information_file:
        if line.find("<COMPANY>") != -1:
            lne_strp_1 = line.strip("<COMPANY>")
            lne_strp_2 = lne_strp_1.strip("\n")
            company_list.append(lne_strp_2)
        else:
            continue
        
    return company_list










def main():
    filename = "XmlTxtFile.xml"
    information_file = get_information_file(filename)
    title_list = get_title_list(information_file)
    artist_list = get_artist_list(information_file)
    country_list = get_country_list(information_file)
    company_list = get_company_list(information_file)
    print(title_list)
    
    
    
    
    
main()
