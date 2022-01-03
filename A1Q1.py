

class Bank:
    
    def __init__(self,principal,years,rate):
        self.principal= principal
        self.years = years
        self.rate = rate
        
    def SInterest(self):
        total = self.principal * self.years * self.rate/100
        print(total)
        
    def CInterest(self):
        total = self.principal*(1+(self.rate/100))**self.years
        print(total)


b = Bank(2000,1.5,2)
b.SInterest()
b.CInterest()