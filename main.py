from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

# Website URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Start webdriver
browser = webdriver.Edge("msedgedriver.exe")
# browser = webdriver.Edge()
browser.get(START_URL)

time.sleep(10)
# Array to store scraped data
scraped_data = []

soup = BeautifulSoup(browser.page_source, 'html.parser')

# Defining the Scraping method
def scrape():
    # Find Table
    bstar_table = soup.find("table", attrs={"class": "wikitable"})
    
    # Find body
    bstar_body = bstar_table.find('tbody')
    
    # Find tr
    table_rows = bstar_body.find_all('tr')
    
    # Get data from td
    for row in table_rows:
        table_cols = row.find_all('td')
        print(table_cols)
        
        temp_list = []
        
        for col_data in table_cols:
            # Printing only columns textual data using .text property
            # print(col_data.text)
            
            # Removing extra white spaces using white spaces
            data = col_data.text.strip()
            print(data)
            
            temp_list.append(data)
        
        scraped_data.append(temp_list)
        
        stars_data = []
        
        for i in range(0,len(scraped_data)):
            
            Star_names = scraped_data[i][1]
            Distance = scraped_data[i][3]
            Mass = scraped_data[i][5]
            Radius = scraped_data[i][6]
            Lum = scraped_data[i][7]
            required_data = [Star_names, Distance, Mass, Radius, Lum]
            stars_data.append(required_data)

# Calling the function
scrape()

# Define header
header = ['Star_names', 'Distance', 'Mass', 'Radius', 'Luminousity']

# Define Pandas dataframe
star_df_1 = pd.DataFrame(stars_data, columns=header)

# Convert to CSV
star_df_1.to_CSV('scraped_data.csv', index=True, index_label="id")