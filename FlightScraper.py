#By: James Bandy
#Gets the cheapest flight option for our program

#This program searches for available flights off of Google Flights using a Chrome Web Browser
from re import L
from FlightData import FlightData
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import bs4
import time
import os



class FlightScraper:
    #These are the attributes used in the FlightData class
    airline = ""
    dt = ""
    rt = ""
    price = 0.0
    
    #This initializes a search and fills out the attributes
    def __init__(self, url: str):
        #This sets up a chrome browser to search for the information using SkipLagged.com
        chrome_options = Options()
        #chrome_options.add_argument("--headless") -- Headless mode is meant to hide the browser we open but unfortunately headless mode causes problems with javascript in web applications
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        #This launches a chromedriver using a url that is entered as input. The url is determined by the inputs which leads to a version of the website with the information needed
        base_dir = os.path.dirname(os.path.abspath(__file__))
        chromedriver_path = os.path.join(base_dir, "chromedriver-win64", "chromedriver.exe")
        service = Service(executable_path=chromedriver_path)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url) #This opens the webbrowser

        #This scrolls to the bottom to ensure the whole page is loaded. Our results are at the top so mostly not needed but it doesn't hurt to make sure
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3) #The program will wait for a few seconds to ensure everything loads
        
        #This parses most of the html document into a string.
        html = driver.find_element(By.XPATH, '/html/body/section').get_attribute("outerHTML")
        soup = bs4.BeautifulSoup(html, 'html.parser')

        #At this point, the information we need is in the parse html document so we close the browser
        driver.quit()

        #print(soup.prettify()) -- This was used for debugging purposes

        #This gets the airline and assigns it to the airline variable. It uses the top entry since by default the page sorts by cheapest at the top.
        #Since we're a budget planner its best to get the cheapest option for our planner.
        fl = soup.find('span', class_="airlines airlines-lg hide-small")
        if fl:
            self.airline = fl.text.strip()
            #print("Airline is: ", self.airline)

        #This gets the first price on the page and formats it to a float. The reason its not directly accessed like the others is because
        #it has a malformed identifier and as such couldn't be directly accessed.
        for span in soup.find_all('span'):
            text = span.text.strip()
            if "$" in text:
                print("Price found:", text)
                self.price = float(text[1:])
                break
        
        #This gets all the times on the page and parses the first two (the top results)
        times = soup.find_all('div', class_="trip-path-point-time")
        if len(times) >= 2:
            self.dt = times[0].text.strip()
            #print("Depart time: ", self.dt)
            self.rt = times[1].text.strip()
            #print("Return time: ", self.rt)
        #else:
            #print("There are no times")

    def getFlight(self) -> FlightData:
        return FlightData(self.airline, self.dt, self.rt, self.price)