#By: Thomas Eubank
#Designed to store data for a vacation, not the travel costs
class VacationData: #Objects of this type store the data for a vacation object
    percentBudget = 0 #Stores the percentage of the budget allocated to housing
  
    def __init__(self, housing = "Sorry, there was no housing available meeting this criteria. ", housingCost = -1, itineraryDescription = "", eventCost = -1):
        #Below this line are housing info
        self.housing = housing #Stores the name and/or the address of the housing option
        self.housingCost = housingCost #Stores the cost of the housing
        #Below this line are event costs
        self.eventCost = eventCost
        self.itineraryDescription = itineraryDescription

    def CalcPercentBudget(self, budget): #Percent of budget used for housing
        percentBudget = self.housingCost/budget

    def ToString(self):
        string = []
        string.append(self.housing)
        string.append(self.housingCost)
        string.append(self.itineraryDescription)
        string.append(self.eventCost)
        return string