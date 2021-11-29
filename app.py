import datetime

class Employee:

    def __init__(self, empID:str, lName:str, fName:str, regHours:float, hourlyRate:float,
     otMultiple:float, taxCredit:float, standardBand:float):
        self.empID = empID
        self.lName = lName
        self.fName = fName
        self.regHours = regHours
        self.hourlyRate = hourlyRate
        self.otMultiple = otMultiple
        self.taxCredit = taxCredit
        self.standardBand = standardBand


    def computePayment(hoursWorked:float, dateWorked:datetime.date):

        pass