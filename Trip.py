class Trip:
    def __init__(self, housingData, flightData1, flightData2, eventCost, foodCost, additionalCosts, services, images):
        self.housingData = housingData
        self.flightData1 = flightData1
        self.flightData2 = flightData2
        self.eventCost = eventCost #Stores the cost of the main event on the itenerary
        self.foodCost = foodCost #Stores the cost of food for the trip
        self.additionalCosts = additionalCosts #Stores additional costs
        self.percentBudget = percentBudget #Stores the percentage of budget used for housing
        self.services = services #Stores the services available
        rating = services.__sizeof__()
        self.images = images #Stores images for the trip object

    def __init__(self, housingData, flightData1, flightData2, eventCost, foodCost, additionalCosts):
        self.housingData = housingData
        self.flightData1 = flightData1
        self.flightData2 = flightData2
        self.eventCost = eventCost #Stores the cost of the main event on the itenerary
        self.foodCost = foodCost #Stores the cost of food for the trip
        self.additionalCosts = additionalCosts #Stores additional costs
        