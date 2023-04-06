#This is a die simulator, serves to simulate the use of a die, generating a number from 1 to 6.

import random
import PySimpleGUI as sg #For interface

class DiceSimulator:
    def __init__(self):
        self.min_value = 1
        self.max_value = 6
    
        #Layout 
        self.layout = [
            [sg.Text('Roll the dice?')],
            [sg.Button('Yes'), sg.Button('No')]
    ]

    def Start(self):

        #Create a window
        self.window = sg.Window('Dice Simulator', layout=self.layout)

        #Read a value in the window
        self.events, self.values = self.window.Read()

        if self.events == 'Yes' or self.events == 'y':
             self.GenerateValue()
        elif self.events == 'No' or self.events == 'n':
            print('Alright, come back anytime!')
        else:
                print('Please enter a valid answer')

    def GenerateValue(self):
        print(random.randint(self.min_value, self.max_value))

simulator = DiceSimulator()
simulator.Start()
    
