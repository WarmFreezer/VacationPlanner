#Internal libraries here
from VacationData import VacationData

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
class WebSearch:
    def __init__(self):
        self.listings = [] #Will return a listing in html format from Vacasa
        self.eventListings = [] #Will return a listing in html format from Eventsbrite
        self.names = [] #Holds the names of the housing scraped
        self.prices = [] #Holds the prices of the housing scraped
        self.eventNames = [] #Holds the names of events scraped AKA itineraryDescription
        self.eventPrices = [] #Holds the prices of events scraped 

    def GetHousing(self, housingUrl):
        #Setup headless Chrome
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        #Path to chromedriver
        base_dir = os.path.dirname(os.path.abspath(__file__))
        chromedriver_path = os.path.join(base_dir, "chromedriver-win64", "chromedriver.exe")
        service = Service(executable_path=chromedriver_path)

        #Scrapes the entire HTML for the given URL
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(housingUrl)
        print(housingUrl)
    
        #Scroll down to load more listings
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        #Create object to hold html data from url passed
        searchResults = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[1]")
        html = searchResults.get_attribute('outerHTML')
        soup = bs4.BeautifulSoup(html, 'html.parser')
        driver.quit()

        if "We couldn't display your results" in soup.text:
            print("No housing results found. Page returned an error message.")
        else:
            housingList = soup.select_one('div.row.mt-16.mb-8.px-16')
            if housingList:
                for card in housingList.select('div.px-8.my-8.unit-result-list'):
                    self.listings.append(card)
            else:
                print("housingList found, but no listings inside.")

    def GetEvents(self, eventUrl):
        #Setup headless Chrome
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        #Path to chromedriver
        base_dir = os.path.dirname(os.path.abspath(__file__)) 
        chromedriver_path = os.path.join(base_dir, "chromedriver-win64", "chromedriver.exe")
        service = Service(executable_path=chromedriver_path)

        #Scrapes the entire HTML from the given URL
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(eventUrl)
        print(eventUrl)
        
        #Scroll down to load more listings
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        
        #Create object to hold html data from url passed
        searchResults = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div/div[1]/div/main/div/div/div/section[1]/div/section/div/div/section/ul")
        html = searchResults.get_attribute('outerHTML')
        soup = bs4.BeautifulSoup(html, 'html.parser')
        driver.quit()
        
        #Below is the common tree for event price and names per event listing
        #/html/body/div[3]/div/div[2]/div/div/div/div[1]/div/main/div/div/div/section[1]/div/section/div/div/section/ul

        if "We couldn't display your results" in soup.text:
            print("No event results found. Page returned an error message.")
        else:
            eventList = soup.select_one('ul')
            if eventList:
                for card in eventList.select('li'): #Adds contents of all "li" tags to the list
                    self.eventListings.append(card)
            else:
                print("eventList found, but no listings inside.")
        
    def GetPrices(self):
        prices = []
        for card in self.listings:
            try:
                #Locates the text containing the price of the housing listing
                price = str(card.find('div').find('div').find('span').find('a').text.strip())
                prices.append(price)
            except Exception as e:
                print (e)
                print ("Something went wrong while fetching housing prices...")
        
        index = 0
        while(index < len(prices)): #Parses through prices and removes "$" from the beginning of each price in list
            prices[index] = prices[index][1:]
            index+=1

        return prices

    def GetNames(self):
        names = []
        for card in self.listings: 
            try:
                #Locates the text containing the name of the housing option
                option = str(card.find('h2').find('a').text.strip())
                names.append(option) #Stores the name of a housing option
            except Exception as e:
                print (e)
                print ("Something went wrong while fetching housing names...")

        return names

    def GetVacationData(self):
        index = 0
        while (index < len(self.listings)): #Travels down a common tree for each price and name in HTML
            self.listings[index] = self.listings[index].find('div').find('div').find('div')
            index+=1

        names = self.GetNames() #Stores housing names
        prices = self.GetPrices() #Stores housing prices

        index = 0
        while (index < len(self.eventListings)): #Travels down a common tree for each eventPrice and eventName in HTML
            #/li[1]/div/div/div[2]/section/div/section[2]/div    
            self.eventListings[index] = self.eventListings[index].find('div').find('div').find('div', class_='discover-search-desktop-card discover-search-desktop-card--hiddeable').find('section').find('div').find('section', class_='event-card-details').find('div')
            index+=1

        eventNames = self.GetEventNames().copy() #Stores the eventNames 
        eventPrices = self.GetEventPrices().copy() #Stores the eventPrices
        vacationData = []

        index = 0
        while (index < len(names)): #Creates a VacationData object for each index of the names list
            try:
                #Create a VacationData object for each item in the 4 lists
                vacationData.append(VacationData(names[index], prices[index], eventNames[index], eventPrices[index]))
            except Exception:
                print("No results for event lists")
            index += 1

        return vacationData

    def GetEventNames(self):
        eventNames = []
        for card in self.eventListings:
            try:
                #Try to find the name wrapper
                aTag = card.find('a')
                if aTag: #If aTag is not empty
                    h3Tag = aTag.find('h3') #Locate h3Tag
                    if h3Tag: #If h3Tag is not empty
                        name = h3Tag.text.strip() #Gather event name
                        eventNames.append(name) #Store in eventNames
                    else:
                        eventNames.append("No event name found")

                else:
                    eventNames.append("No link found")

            except Exception as e:
                print("Something went wrong while fetching event names...")
                print(e) #Prints error
                print(card.prettify()) #Prints HTML causing error
                eventNames.append("Error") #Stores error result

        return eventNames


    def GetEventPrices(self):
        eventPrices = []
        for card in self.eventListings:
            try:
                #Try to find the price wrapper
                priceWrapper = card.find('div', class_='DiscoverHorizontalEventCard-module__priceWrapper___3rOUY') 
                if priceWrapper: #If priceWrapper is not empty
                    priceTag = priceWrapper.find('p') #Locate price tag
                    if priceTag: #If price tag is not empty
                        price = priceTag.text.strip() #Gather price in string format
                        eventPrices.append(price) #Store in eventPrices
                    else:
                        eventPrices.append("No price tag found")

                else:
                    eventPrices.append("Free or no price listed") 

            except Exception as e:
                print("Something went wrong while fetching event prices...")
                print(e) #Prints error (without traceback)
                print(card.prettify()) #Prints HTML that caused error
                eventPrices.append("Error") #Stores an error result

        index = 0
        while (index < len(eventPrices)): #Parses through eventPrices and removes "from $" from the beginning of each price in list
            eventPrices[index] = eventPrices[index][6:]
            index+=1

        return eventPrices
