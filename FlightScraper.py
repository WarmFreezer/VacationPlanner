#This program searches for available flights off of Google Flights using a Chrome Web Browser
from re import L
from FlightData import FlightData
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import bs4
import time
import os



class FlightScraper:
    airline = ""
    dest = ""
    dt = ""
    rt = ""
    price = 0.0
    
    def __init__(self, url: str):
        #Setup headless Chrome
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        base_dir = os.path.dirname(os.path.abspath(__file__))
        chromedriver_path = os.path.join(base_dir, "chromedriver-win64", "chromedriver.exe")
        service = Service(executable_path=chromedriver_path)
        driver = webdriver.Chrome(options=chrome_options)
        #print(url)
        driver.get(url) 

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        print(driver.current_url)

        elem = driver.find_element(By.CLASS_NAME, 'infinite-trip-list')
        html = elem.get_attribute('outerHTML')
        soup = bs4.BeautifulSoup(html, 'html.parser')

        print(soup.prettify())

        driver.quit()

        if "We couldn't display your results" in soup.text:
            print("No flight results found. Page returned an error message.")
        else:
            flight = soup.select_one('')
            if flight:
                self.airline = str(flight.find('span').text_strip())
                path = flight.find('div', class_='span9 trip-path')
                self.dt = str(path.find('div', class_='trip-path-point trip-path-point-first').find('div', class_='trip-path-point-time ').text_strip())
                self.rt = str(path.find('div', class_='trip-path-point trip-path-point-last').find('div', class_='trip-path-point-time ').text_strip())
                self.price = float(flight.find('div', class_='span2 trip-cost').find('p').find('span').text_strip())
            else:
                print("There are no available flights")

    def getFlight(self) -> FlightData:
        return FlightData(self.airline, self.dt, self.rt, self.price)