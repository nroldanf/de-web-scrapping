from selenium import webdriver # will open the webbrowser
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re
# from selenium.webdriver.common.keys import Keys
# import pandas as pd

# financials
# New-Tariffs
# filings
# Orders
# Tariffs
# 1. Go to body
# 2. Open pre
# 3. Get all <a>
# 4. Extract href from all (omit parent diretory one)
# 5. 

# XPath for finding hrefs: <a href="..."> >> //a[@href]

# driver.get(base_webpage)
# links = driver.find_elements(By.XPATH, "//a[@href]")
# print(links)
# links_list = []


def get_links(driver, base_webpage, pdfs_list):
    pattern = r'\.[^.\\/:*?"<>|\r\n]+$'
    driver.get(base_webpage)
    links = driver.find_elements(By.XPATH, "//a[@href]")
    for link in links:
        if link.accessible_name.find("Parent Directory") == -1:
            if re.search(pattern, link.accessible_name):
                if link.accessible_name.endswith(".pdf") or link.accessible_name.endswith(".PDF"):
                    pdfs_list.append(f"{link.parent.current_url}{link.accessible_name}")
                else:
                    continue
            else:
                # Continue clicking further
                url = f"{link.parent.current_url}{link.accessible_name}"
                get_links(driver, url, pdfs_list) 
    return pdfs_list
    

if __name__ == "__main__":
    
    chromedriver = "/chromedriver"
    option = webdriver.ChromeOptions()
    option.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
    s = Service(chromedriver)
    driver = webdriver.Chrome(service=s, options=option)
    base_webpage = "https://www.floridapsc.com/library/"    
    pdfs_list = get_links(driver, base_webpage, [])
    print()

