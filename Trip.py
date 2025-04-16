#By: Thomas Eubank
#Stores trip information including vacation plan and flights
from VacationData import VacationData
from FlightData import FlightData

class Trip:
    def __init__(self, vacation, flightData1, flightData2, eventCost, foodCost, additionalCosts, percentBudget, services, images):
        self.vacationData = vacation
        self.flightData1 = flightData1
        self.flightData2 = flightData2
        rating = services.__sizeof__()

    def __init__(self, vacationData, flightData1, flightData2, eventCost, foodCost, additionalCosts):
        self.vacationData = vacationData
        self.flightData1 = flightData1
        self.flightData2 = flightData2
