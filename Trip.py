#Internal libraries here
from VacationData import VacationData
from FlightData import FlightData

#By: Thomas Eubank
#Stores trip information including vacation plan and flights
class Trip:
    def __init__(self, vacationData, flightData): 
        self.vacationData = vacationData
        self.flightData1 = flightData
    
    def ToString(self):
        string = []
        string.append(self.vacationData.ToString())
        string.append(self.flightData.ToString())
        return string
        