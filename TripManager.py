#Internal libraries here
from WebSearch import WebSearch
from FlightScraper import FlightScraper
from Trip import Trip, VacationData
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
        #https://www.eventbrite.com/d/united-states--florida/all-events/
        eventsUrl = "https://www.eventbrite.com/d/united-states--" + self.destinationState +"/all-events/" #Current Eventbrite URL

        search = WebSearch() #New webSearch obj
        search.GetHousing(housingUrl) #Search this url for housing
        search.GetEvents(eventsUrl) #Search this url for events
        self.vacationData = search.GetVacationData() #Get vacationData objects in a list from the search obj

        #Iterates through the price and names list to create VacationData objects
        index = 0 
        while(index < len(self.vacationData)): 
            self.flightData.append(FlightData("Spirit", self.destinationState, "05-16-2025", 100)) #remove
            self.flightData.append(FlightData("Spirit", self.destinationState, "05-23-2025", 100)) #remove
            index += 1

        #Iterates through the vacationData and flight lists to create Trip objects
        index = 0
        while (index < len(self.vacationData)): #Parse through vacationData
            trip = Trip(self.vacationData[index], self.flightData[2 * index], self.flightData[2 * index + 1]) #Define a trip object to be tested
            housingCost = float(trip.ToString()[0][1])
            eventCost = float(trip.ToString()[0][3])
            if (housingCost + eventCost * int(self.vacationers) < int(self.budget)): #if housingCost + eventCost * vacationers < budget    
                self.tripList.append(trip) #Add to trip list
            index += 1 #Goto next item in list

        if (len(self.tripList) == 0): #If no trips fit in budget
            self.tripList.append(Trip(VacationData(), FlightData(), FlightData())) #Add default trip to represent a search error

        return self.tripList



