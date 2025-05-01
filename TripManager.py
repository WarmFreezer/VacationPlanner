#Internal libraries here
from WebSearch import WebSearch
from FlightScraper import FlightScraper
from Trip import Trip, VacationData
from FlightData import FlightData

#External Libraries Here
import streamlit as st
from datetime import date

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
        #Sets a month variable to the first 2 characters of the departure date
        dMonth = self.departureDate[0:2]
        dDay = self.departureDate[3:5] #Same for day
        dYear = self.departureDate[6:10] #Same for year

        rMonth = self.returnDate[0:2] #...
        rDay = self.returnDate[3:5] #...
        rYear = self.returnDate[6:10] #...

        self.destinationState = self.destinationState.replace(' ', '-')
        self.destinationCity = self.destinationCity.replace(' ', '-')

        #Example housing URL
        #https://www.vacasa.com/search?adults=2&arrival=04%2F20%2F2025&departure=04%2F26%2F2025&place=/usa/Florida/Miami/
        housingUrl = "https://www.vacasa.com/search?adults=" + str(self.vacationers) + "&arrival=" + dMonth + "%2F"+ dDay + "%2F" + dYear + "&departure=" + rMonth + "%2F" + rDay + "%2F" + rYear + "&place=/usa/" + self.destinationState + "/" + self.destinationCity + "/" #Current Vacasa URL

        #Example events URL
        #https://www.eventbrite.com/d/united-states--florida/all-events/?page=1&start_date=2025-04-27&end_date=2025-05-03
        eventsUrl = "https://www.eventbrite.com/d/united-states--" + self.destinationState +"/all-events/?page=1&start_date=" + dYear + "-" + dMonth + "-" + dDay + "&end_date=" + rYear + "-" + rMonth + "-" + rDay #Current Eventbrite URL

        #Example flights URL
        #https://skiplagged.com/flights/louisville/new-york/2025-05-16/2025-05-18
        flightsUrl = "https://skiplagged.com/flights/" + self.departure.lower() + "/" + self.destinationCity.lower() + "/" + dYear + "-" + dMonth + "-" + dDay + "/" + rYear + "-" + rMonth + "-" + rDay

        search = WebSearch() #New webSearch obj
        search.GetHousing(housingUrl) #Search this url for housing
        search.GetEvents(eventsUrl) #Search this url for events
        self.vacationData = search.GetVacationData() #Get vacationData objects in a list from the search obj

        flightsSearch = FlightScraper(flightsUrl)
        self.flightData = flightsSearch.getFlight();

        #Iterates through the vacationData and flight lists to create Trip objects
        index = 0
        self.tripList.clear()
        while (index < len(self.vacationData)): #Parse through vacationData
            trip = Trip(self.vacationData[index], self.flightData) #Define a trip object to be tested
            
            dateOfDeparture = date(int(dYear), int(dMonth), int(dDay))
            dateOfReturn = date(int(rYear), int(rMonth), int(rDay))

            housingCost = float(trip.ToString()[0][1]) * abs((dateOfReturn - dateOfDeparture).days)
            eventCost = float(trip.ToString()[0][3])
            if (housingCost + eventCost * int(self.vacationers) < int(self.budget) / 2): #if housingCost + eventCost * vacationers < budget    
                self.tripList.append(trip) #Add to trip list
            index += 1 #Goto next item in list

        if (len(self.tripList) == 0): #If no trips fit in budget
            self.tripList.append(Trip(VacationData(), FlightData())) #Add default trip to represent a search error

        return self.tripList



