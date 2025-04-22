class FlightData: #Objects of this type contain flight information for other classes
    airline: str
    destination: str
    d_time: str
    price: float

    def __init__(self, airline = "", destination = "", d_time = "", price = ""):
        self.airline = airline #Stores the airline of the flight
        self.destination = destination #Stores the destination of the flight
        self.d_time = d_time #Stores the departure date/time
        self.price = price #Stores the price of the flight

    def ToString(self):
        string = []
        string.append(self.airline)
        string.append(self.d_time)
        string.append(str(self.price))
        return string




