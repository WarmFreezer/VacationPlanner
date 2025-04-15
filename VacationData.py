#By: Thomas Eubank
#Designed to store data for a vacation, not the travel costs
class VacationData: #Objects of this type store the data for a vacation object
    percentBudget = 0 #Stores the percentage of the budget allocated to housing
    
    def __init__(self, housing, housingCost, eventCost, foodCost, additionalCosts, itineraryDescription):
        #Below this line are housing info
        self.housing = housing #Stores the name and the address of the housing option
        self.housingCost = housingCost #Stores the cost of the housing
        #Below this line are other costs
        self.eventCost = eventCost
        self.foodCost = foodCost
        self.additionalCosts = additionalCosts
        self.itineraryDescription = itineraryDescription
        
    def __init__(self, housing, housingCost, eventCost, foodCost, additionalCosts, itineraryDescription, services, images): #Alternate constructor for when we add service and image support
        #Below this line are housing info
        self.housing = housing #Stores the name and the address of the housing option
        self.housingCost = housingCost #Stores the cost of the housing
        #Below this line are other costs
        self.eventCost = eventCost
        self.foodCost = foodCost
        self.additionalCosts = additionalCosts
        self.itineraryDescription = itineraryDescription
        self.services = services
        self.images = images

    def CalcPercentBudget(budget):
        percentBudget = housingCost/budget