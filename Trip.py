class Trip:
    def __init__(self, destination, housing, housingCost, ticketCost, eventCost, foodCost, additionalCosts, percentBudget, services, images):
        self.destination = destination #Stores the name of the city 
        self.housing = housing #Stores the name of the housing 
        self.housingCost = housingCost #Stores the cost of the housing (double)
        self.ticketCost = ticketCost #Stores the cost of the plane ticket
        self.eventCost = eventCost #Stores the cost of the main event on the itenerary
        self.foodCost = foodCost #Stores the cost of food for the trip
        self.additionalCosts = additionalCosts #Stores additional costs
        self.percentBudget = percentBudget #Stores the percentage of budget used for housing
        
