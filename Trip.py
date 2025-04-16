#Internal libraries here
from VacationData import VacationData
from FlightData import FlightData

#By: Thomas Eubank
#Stores trip information including vacation plan and flights
class Trip:
    def __init__(self, vacationData, flightData1, flightData2, eventCost, foodCost, additionalCosts, percentBudget, services, images):
        self.vacationData = vacationData
        self.flightData1 = flightData1
        self.flightData2 = flightData2
        self.eventCost = eventCost
        self.foodCost = foodCost
        self.additionalCosts = additionalCosts
        self.percentBudget = percentBudget
        self.services = services
        self.images = images
        rating = services.__sizeof__()

    def __init__(self, vacationData, flightData1, flightData2, eventCost, foodCost, additionalCosts):
        self.vacationData = vacationData
        self.flightData1 = flightData1
        self.flightData2 = flightData2
        self.eventCost = eventCost
        self.foodCost = foodCost
        self.additionalCosts = additionalCosts

    def __init__(self, vacationData, flightData1, flightData2): #Simplified constructor since we are running out of time
        self.vacationData = vacationData
        self.flightData1 = flightData1
        self.flightData2 = flightData2

    def __init__(self, vacationData):
        self.vacationData = vacationData
        self.flightData1 = FlightData()
        self.flightData2 = FlightData()
    
    def ToString(self):
        string = []
        string.append(self.vacationData.ToString())
        string.append(self.flightData1.ToString())
        string.append(self.flightData2.ToString())
        return string
        