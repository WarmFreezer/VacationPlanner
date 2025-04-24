#This program searches for available flights off of Google Flights using a Chrome Web Browser
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
    def SearchFlights(self, departure: str, destination: str, d_date: str, r_date: str, flier_count: int):
        #Setup headless Chrome
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        #Path to chromedriver
        base_dir = os.path.dirname(os.path.abspath(__file__))
        chromedriver_path = os.path.join(base_dir, "chromedriver-win64", "chromedriver.exe")
        service = Service(executable_path=chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        #Google flights website
        driver.get("https://www.google.com/travel/flights?gl=US&hl=en-US")

        #Input search parameters
        driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/div/div/input').send_keys(departure)
        driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[2]/div[2]/div[1]/div/input').send_keys(destination)
        driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input').send_keys(d_date)
        driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/input').send_keys(r_date)

        #Open the flier count popup, set the number of fliers, then close the popup
        popup = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[1]/div/button')
        
        popup.click()
        time.sleep(1)
        add_flier = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/ul/li[1]/div/div/span[3]/button').click()
        for i in range(self.fliers - 1):
            add_flier.click()
        popup.click()

        #Opens the filters, hides separate and self-transfer flights, then closes the filters.
        driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/button').click()
        driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[4]/div/div/div[1]/div/button').click()
        driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[4]/div/div[2]/div[3]/div/div[2]/div/div[1]/section[9]/div/div[1]/div/div/div/div[2]/div/div/input').click()
        driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[4]/div/div[2]/div[3]/div/div[1]/div[2]/span/button').click()

        #Selects cheapest
        driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[2]/div/div[1]/div[2]').click()

        p1 = int(driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[2]/div/div[3]/div[2]/ul/li[1]/div/div[2]/div/div[2]/div/div[6]/div[1]/div[2]/span').getText()[1:])
        p2 = int(driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[2]/div/div[3]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div/div[6]/div[1]/div[2]/span').getText()[1:])

        airline = ""
        dest = ""
        dt = ""
        price = 0.0

        driver.find_element(By.XPATH, '').getText()

        if (p1 < p2):
            airline = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[2]/div/div[3]/div[2]/ul/li[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/span[1]').getText()
            dest = destination
            dt = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[2]/div/div[3]/div[2]/ul/li[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/span/span[1]/span/span/span').getText()
            price = p1
        else:
            airline = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[2]/div/div[3]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/span').getText()
            dest = destination
            dt = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[2]/div/div[3]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/span/span[1]/span/span/span').getText()
            price = p2

        driver.quit()

        flight = FlightData(airline, dest, dt, price)

        return flight





