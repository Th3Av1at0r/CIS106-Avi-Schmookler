# This program takes information from a file containing a catalog of CDs 
# and prints the menu, number of items and average price
# tips on ElementTree given by Jess Elis

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
        print("Error 1: Missing or bad data.")
        exit()


def get_processed_list(catalog, find_object):
    try:
        information_file = ET.fromstring(catalog)
        processed_list = [element.text for element in 
        information_file.findall(find_object)]
    except:
        print("Error 2: Missing or bad data.")
        exit()
        
    return processed_list


def get_average_price(price_list):
    try:
    price_sum = 0
    for element in list(price_list):
        price_sum = price_sum + float(element)
    average_price = (price_sum / len(price_list))
    average_price = format(average_price, '.2f')
    except:
        print("Error 3: Missing or bad data.")
        exit()
        
    return average_price


def display_results(title_list, artist_list, country_list, 
year_list, price_list, average_price):
    try:
        counter = 0
        while (counter < len(title_list)):
            print(title_list[counter] + " - " + 
            artist_list[counter] + " - " + country_list[counter] + " - " + 
            price_list[counter] + " - " + year_list[counter])
            counter += 1
        print("There were " + str(len(title_list)) + 
        " CDs and the average price is $" + average_price)
    except:
        print("Error 4: Missing or bad data.")
        exit()
    
    
def main():
    file_name = "cd_catalog.xml"
    catalog = get_catalog(file_name)
    title_list = get_processed_list(catalog, "CD/TITLE")
    artist_list = get_processed_list(catalog, "CD/ARTIST")
    country_list = get_processed_list(catalog, "CD/COUNTRY")
    price_list = get_processed_list(catalog, "CD/PRICE")
    year_list = get_processed_list(catalog, "CD/YEAR")
    average_price = get_average_price(price_list)
    display_results(title_list, artist_list, country_list, 
    year_list, price_list, average_price)
    
    
main()
