import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import time, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import pandas as pd
import numpy as np
import re

"""
Functions for web scraping with selenium
1. Google speaker
2. Google institute
3. Google institute on Google Map

"""


chromedriver = "/Applications/chromedriver" # path to the chromedriver executable
os.environ["webdriver.chrome.driver"] = chromedriver

# Open automated Chrome with fictionDB webpage
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.google.com")


def google_speaker(speaker):
    
    keyword = speaker
    speaker_dict={}
    headers = ["speaker","profession","birth","born","age","origin"]

    # Selenium begins
    driver.get("https://www.google.com")
    search_bar = driver.find_element_by_xpath("//input[@name='q'][@type='text']")
    search_bar.clear()
    search_bar.send_keys(keyword)
    #     print(speaker)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(2)

    # Set default value of result
    profession, birth, born, age, origin = np.nan, np.nan, np.nan, np.nan, np.nan

    # Find profession
    try:
        profession = driver.find_element_by_xpath("//div[@data-attrid='subtitle']").text
    except:
        pass

    if profession is np.nan:
        try:
            description = driver.find_element_by_xpath("//div[@data-attrid='description']").text
            profession = re.findall("(?<=was )(.*)(?= who)", description)[0]
        except:
            pass

    # Find birth info    
    try:
        birth = driver.find_element_by_xpath("//div[@class='rVusze']").text
    except:
        pass

    # Extract age and birth blace from birth info
    # Age
    try:
        age = re.findall("age \d+", birth)[0].split(' ')[-1]
    except:
        pass

    # Year born
    try:
        born = re.findall("Born: .* \d+", birth)[0].split(', ')[-1]
    except:
        pass

    # Birth place
    try:
        origin = " ".join(birth.split(', ')[-2:])
    except:
        pass

    speak_dict = dict(zip(headers,
                [speaker,profession,birth,born,age,origin]))

    return speak_dict





def google_school(school):
    
    school = school
    keyword = school + ' coordinate dd'
    school_dict={}
    headers = ["school","coord","latitude","longitude"]

    # Selenium begins
    driver.get("https://www.google.com")
    search_bar = driver.find_element_by_xpath("//input[@name='q'][@type='text']")
    search_bar.clear()
    search_bar.send_keys(keyword)
    #     print(speaker)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(2)

    # Set default value of result
    coord,latitude,longitude = np.nan,np.nan,np.nan

    # Find coordinate decimal degrees
    try:
        coord = driver.find_element_by_xpath("//span[@class='hgKElc']").text
    except:
        pass
    
    
    # Extract latitude and longitude
    try:
        latitude = re.findall('[-+]?\d*\.?[-+]?\d+', coord)[0]
        longitude = re.findall('[-+]?\d*\.?[-+]?\d+', coord)[1]
    except:
        pass

    school_dict = dict(zip(headers,
                [school,coord,latitude,longitude]))

    return school_dict



def google_school_2(school):
    """Get coordinates from google map url"""
    
    keyword = school
    school_dict={}
    headers = ["school","coord","latitude","longitude"]

    # Scrape google map for dd coord
    driver.get("https://www.google.com/maps")
    search_bar = driver.find_element_by_xpath("//input[@name='q'][@id='searchboxinput']")
    search_bar.clear()
    search_bar.send_keys(keyword)
    #     print(speaker)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(5)

    coord,latitude,longitude = np.nan,np.nan,np.nan
    try:
        url = driver.current_url
        coord = re.findall('@[-+]?\d+\.?\d+,[-+]?\d+\.?\d+',url)
        latitude = coord[0].split(',')[0].lstrip('@')
        longitude = coord[0].split(',')[1]
    except:
        pass

    school_dict = dict(zip(headers,
                           [school,coord,latitude,longitude]))

    return school_dict