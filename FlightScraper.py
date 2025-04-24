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
    def SearchFlights(self, departure: str, destination: list[str], d_date: str, r_date: str, flier_count: int) -> list[FlightData]:
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

        if (len(destination) != 0):
            #Inputs the first entry, the XPATH's change after the first entry
            driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/div/div/input').send_keys(departure)
            driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[2]/div[2]/div[1]/div/input').send_keys(destination[0])
            driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input').send_keys(d_date)
            driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/input').send_keys(r_date)
            
            #Sets the number of fliers
            #Opens the flier count popup
            driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[1]/div/button').click()
            #Wait for the popup to load
            time.sleep(1)
            #Adds a flier for each additional person on the trip above 1 (1 is default)
            add_flier = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/ul/li[1]/div/div/span[3]/button').click()
            for i in range(self.fliers - 1):
                add_flier.click()
            #Closes the flier count popup
            driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/button[1]').click()

            #Sets the flight filter to show only continuous flights
            #Clicks search
            driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/button').click()
            #Clicks all filters to open the popup
            driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[4]/div/div/div[1]/div/button').click()
            #Clicks the "hide separate and self-transfer tickets"
            driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[4]/div/div[2]/div[3]/div/div[2]/div/div[1]/section[9]/div/div[1]/div/div/div/div[2]/div/div/input').click()
            #closes the all filters popup
            driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[4]/div/div[2]/div[3]/div/div[1]/div[2]/span/button').click()
            #Waits for the flights to load
            time.sleep(5)



            if (len(destination) > 1):
                for i in range(len(destination - 2)):

            

        driver.quit()





