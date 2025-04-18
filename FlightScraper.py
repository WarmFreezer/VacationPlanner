#This program searches for available flights off of Google Flights using a Chrome Web Browser
from FlightData import FlightData
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import bs4
import time
import os

class FlightScraper:
    def SearchFlights(departure: str, destination: list[str], d_date: str, r_date: str) -> list[FlightData]:
        service = Service(executable_path="chromedriver-win64/chromedriver.exe")
        driver = webdriver.Chrome(service=service)

        driver.get("https://google.com")

        time.sleep(10)

        driver.quit()





