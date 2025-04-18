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
    def SearchFlights(self, departure: str, destination: list[str], d_date: str, r_date: str) -> list[FlightData]:
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

        input_element = driver.find_element(By.XPATH, "//*[@id="i23"]/div[6]/div[2]/div[2]/div[1]/div/input")


        time.sleep(10)

        driver.quit()





