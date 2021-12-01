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


    def computePayment(self, hoursWorked:float, dateWorked:str):
        regularHrsWorked = 0
        regularPay = 0
        otHrsWorked = 0
        otRate = self.hourlyRate * self.otMultiple
        otPay = 0

        if hoursWorked > self.regHours:
            
            regularHrsWorked = self.regHours
            otHrsWorked = hoursWorked - self.regHours
            otPay = otHrsWorked * otRate
            regularPay = regularHrsWorked * self.hourlyRate
        
        else:

            regularHrsWorked = hoursWorked
            regularPay = hoursWorked * self.hourlyRate

        grossPay = regularPay + otPay
        higherRatePay = grossPay - self.standardBand if grossPay > self.standardBand else 0
        # if gross pay > standard band, higher pay rate = earnings above gross pay else higher rate earnings

        standardTax = 0.2 * (self.standardBand if higherRatePay != 0 else grossPay)
        # if gross pay < standard band, tax applicable only on amount below standard band else tax applicable on full band amount

        higherTax = 0.4 * (higherRatePay if higherRatePay != 0 else 0)
        # if higher pay == 0, no higher tax applicable

        netDeductions = standardTax + higherTax - self.taxCredit if standardTax + higherTax >= self.taxCredit else standardTax + higherTax
        # if total taxes >= tax credits, deductions = total taxes - tax credits;
        # else deductions = total taxes 

        return dict({
            "name" : self.fName + " " + self.lName,
            "date" : dateWorked,
            "regular hrs worked" : regularHrsWorked,
            "ot hrs worked" : otHrsWorked,
            "regular rate" : self.hourlyRate,
            "ot rate" : otRate,
            "regular pay" : regularPay,
            "ot pay" : otPay,
            "gross pay" : grossPay,
            "std rate pay" : self.standardBand,
            "higher rate pay" : higherRatePay,
            "standard tax" : standardTax,
            "higher tax" : higherTax,
            "total tax" : standardTax + higherTax,
            "tax credit" : self.taxCredit,
            "net deductions" : netDeductions,
            "net pay" : grossPay - netDeductions
        })


# e = Employee("123", "doe", "john", 40, 45, 1.5, 80, 1900)
# print (str(e.computePayment(43, "10/10/2021")))

############################## READ FROM EMPLOYEE AND HOURS FILE ########################################













########################################################################################################