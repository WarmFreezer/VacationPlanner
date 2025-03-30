class FlightData: #Objects of this type contain flight data
    def __init__(self, airline, destination, d_time, price):
        self.airline = airline #Stores the airline of the flight
        self.destination = destination #Stores the destination of the flight
        self.d_time = d_time #Stores the departure date/time
        self.price = price #Stores the price of the flight