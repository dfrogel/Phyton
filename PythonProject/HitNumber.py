#Algorithm that generates a random value and the user tries to guess
import random

class HitNumber: #Create a class
    def __init__(self):
        self.random_value = 0 #Number starts at zero
        self.min_value = 1 #lower value
        self.max_value = 100 #maximum value
        self.TryAgain = True
    
    def Start(self):
        self.GenerateValue() #Create a random value
        self.RequestValue() #Create a request 

        try:
            while self.TryAgain == True: 
                if int(self.response_value) > self.random_value:
                    print('Try a lower value!')
                    self.RequestValue()
                elif int(self.response_value) < self.random_value:
                    print('Try a higher value!')
                    self.RequestValue()
                if int(self.response_value) == self.random_value:
                    self.TryAgain = False
                    print('Congratulations!! This is the number :)')
        except:
            print('Please try a number from 1 to 100')
            self.Start()
                
    def RequestValue(self): 
        self.response_value = input('What is the number? ')    

    def GenerateValue(self):
        self.random_value = random.randint(self.min_value, self.max_value)
    
Hit = HitNumber()
Hit.Start()