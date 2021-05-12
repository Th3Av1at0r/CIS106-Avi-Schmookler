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
        print("Error: Missing or bad data.")
        exit()


def get_title_list(catalog):
    try:
        information_file = ET.fromstring(catalog)
        title_list = [el.text for el in information_file.findall('CD/TITLE')]
    except:
        print("Error: Missing or bad data.")
        exit()
    
    return title_list
    

def get_artist_list(catalog):
    try:
        information_file = ET.fromstring(catalog)
        artist_list = [el.text for el in information_file.findall('CD/ARTIST')]
    except:
        print("Error: Missing or bad data.")
        exit()

    return artist_list


def get_country_list(catalog):
    try:
        information_file = ET.fromstring(catalog)
        country_list = [el.text for el in 
        information_file.findall('CD/COUNTRY')]
    except:
        print("Error: Missing or bad data.")
        exit()

    return country_list

    
def get_company_list(catalog):
    try:
        information_file = ET.fromstring(catalog)
        company_list = [el.text for el in 
        information_file.findall('CD/COMPANY')]
    except:
        print("Error: Missing or bad data.")
        exit()
    
    return company_list


def get_price_list(catalog):
    try:
        information_file = ET.fromstring(catalog)
        price_list = [el.text for el in information_file.findall('CD/PRICE')]
    except:
        print("Error: Missing or bad data.")
        exit()

    return price_list

    
def get_year_list(catalog):
    try:
        information_file = ET.fromstring(catalog)
        year_list = [element.text for element in 
        information_file.findall('CD/YEAR')]
    except:
        print("Error: Missing or bad data.")
        exit()
    
    return year_list


def get_average_price(price_list):
    try:
        price_list = [float(number) for number in price_list]
        average_price = (sum(price_list) / len(price_list))
        average_price = format(average_price, '.2f')
    except:
        print("Error: Missing or bad data.")
        exit()
        
    return average_price


def display_results(title_list, artist_list, country_list, company_list, 
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
        print("Error: Missing or bad data.")
        exit()
    
    
def main():
    file_name = "cd_catalog.xml"
    catalog = get_catalog(file_name)
    title_list = get_title_list(catalog)
    artist_list = get_artist_list(catalog)
    country_list = get_country_list(catalog)
    company_list = get_company_list(catalog)
    price_list = get_price_list(catalog)
    year_list = get_year_list(catalog)
    average_price = get_average_price(price_list)
    display_results(title_list, artist_list, country_list, company_list, 
    year_list, price_list, average_price)
    
    
main()
