#Internal libraries here
from WebSearchAI import WebSearchAI
from FlightScraper import FlightScraper
from Trip import Trip
from FlightData import FlightData

#External Libraries Here
import streamlit as st

#By: Thomas Eubank
#Designed to create trip objects from a combination of a vacationData object and 2 flightData objects
class TripManager:
    budget = None
    departure = None
    destinationState = None
    destinationCity = None
    departureDate = None
    returnDate = None
    vacationers = None

    flightData = [] #List for departing flights which need to be passed to WebSearchAI to find an itinerary on the destination city (Odd indexes should be departing flights)
    vacationData = [] #List for vacation info which will be combined with flightData to creat a list of trip objects
    tripList = [] #Will need to define a new object based on all departing flights and returning ones

    def __init__(self, budget, departure, destinationState, destinationCity, departureDate, returnDate, vacationers):
        self.budget = budget
        self.departure = departure
        self.destinationState = destinationState
        self.destinationCity = destinationCity
        self.departureDate = departureDate
        self.returnDate = returnDate
        self.vacationers = vacationers

    def MainSearch(self): 
        #dMonth = self.departureDate[0:1]
        #dDay = self.departure[3:4]
        #dYear = self.departure[6:9]

        #print (dMonth)
        #print (dDay)
        #print(dYear)

        #rMonth = self.returnDate[0:1]
        #rDay = self.departure[3:4]
        #rYear = self.departure[6:9]

        #Example URL
        #https://www.vacasa.com/search?adults=2&arrival=04%2F20%2F2025&departure=04%2F26%2F2025&place=/usa/Florida/Miami/
        housingUrl = "https://www.vacasa.com/search?adults=" + str(self.vacationers) + "&arrival=04%2F20%2F2025&departure=04%2F26%2F2025&place=/usa/" + self.destinationState + "/" + self.destinationCity + "/"

        search = WebSearchAI(housingUrl)
        vacationData = search.getVacationData()

        #Iterates through the price and names list to create VacationData objects
        index = 0
        while(index < len(vacationData)):
            self.flightData.append(FlightData("Spirit", self.destinationState, "05-16-2025", 100)) #remove
            self.flightData.append(FlightData("Spirit", self.destinationState, "05-16-2025", 100)) #remove
            index += 1

#        for i in prices:
 #           st.write(i)
  #      for i in names:
   #         st.write(i)

        #Iterates through the vacationData and flight lists to create Trip objects
        index = 0
        while (index < len(self.vacationData)):
            self.tripList.append(Trip(self.vacationData[index], self.flightData[2 * index], self.flightData[2 * index + 1]))
            index += 1

        return self.tripList



