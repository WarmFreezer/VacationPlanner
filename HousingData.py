class HousingData: #Objects of this type store the data for a housing object
    percentBudget = 0 #Stores the percentage of the budget allocated to housing
    
    def __init__(self, housing, housingCost):
        self.housing = housing #Stores the name and the address of the housing option
        self.housingCost = housingCost #Stores the cost of the housing

    def CalcPercentBudget(budget):
        percentBudget = housingCost/budget