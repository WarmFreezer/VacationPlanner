class FlightData: #Objects of this type contain flight information for other classes
    airline: str
    destination: str
    d_time: str
    price: float

    def __init__(self, airline = "", d_time = "", r_time = "", price = 0.0):
        self.airline = airline #Stores the airline of the flight
        self.d_time = d_time #Stores the departure date/time
        self.r_time = r_time
        self.price = price #Stores the price of the flight

    #This is just to display the results. Appends each entry into an array and returns the array.
    def ToString(self):
        string = []
        string.append(self.airline)
        string.append(self.d_time)
        string.append(self.r_time)
        string.append("$" + str(self.price))
        return string




