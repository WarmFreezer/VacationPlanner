#External libraries here
from contextlib import nullcontext
from types import NoneType
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import bs4
import time
import os

#By: Thomas Eubank
#Designed to search different urls and return listings from Vacasa(for housing), eventually add support for additional costs.
class WebSearchAI:
    listings = [] #Will return a listing in html format from Vacasa
    driver = None

    def __init__(self, url):
        tempListings = [] 

        print(selenium.__version__)
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
        driver.get(url)
    
        #Scroll down to load more listings
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        #Create object to hold html data from url passed
        soup = bs4.BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()

        body = soup.body
        page = body.find('div', id='place-body', class_='view-list')
        main_column = page.find('div', id='place-page-left') if page else None
        table = main_column.find('div', id='search-results') if main_column else None
        housingList = table.select_one('div.row.mt-16.mb-8.px-16')

        if "We couldn't display your results" in table.text:
            print("No housing results found. Page returned an error message.")
        else:
            housingList = table.select_one('div.row.mt-16.mb-8.px-16')
            if housingList:
                for card in housingList.select('div.px-8.my-8.unit-result-list'):
                    #print(card)
                    tempListings.append(card)
            else:
                print("housingList found, but no listings inside.")

        listings = tempListings

    def getPrices(self):
        prices = []
        for card in self.listings:
            try:
                listingHeader = card.find('div').find('div').find('div')
                #Locates the text containing the price of the housing listing
                price = str(listingHeader.find('div').find('div').find('span').find('a').text.strip())
                prices.append(price)
                print (price)
            except nullcontext:
                print ("Something went wrong...")
        
        return prices

    def getNames(self):
        names = []
        for card in self.listings:
            try:
                listingHeader = card.find('div').find('div').find('div')
                #Locates the text containing the name of the housing option
                option = str(listingHeader.find('h2').find('a').text.strip())
                names.append(option)
                print (option)
            except nullcontext:
                print ("Something went wrong...")

        return names