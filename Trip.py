#Internal libraries here
from VacationData import VacationData
from FlightData import FlightData

#By: Thomas Eubank
#Stores trip information including vacation plan and flights
class Trip:
    def __init__(self, vacationData, flightData1, flightData2): 
        self.vacationData = vacationData
        self.flightData1 = flightData1
        self.flightData2 = flightData2
    
    def ToString(self):
        string = []
        string.append(self.vacationData.ToString())
        string.append(self.flightData1.ToString())
        string.append(self.flightData2.ToString())
        return string
        