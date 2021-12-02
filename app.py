class Hours:

    def __init__(self, empID:str, dateWorked:str, hoursWorked:float):

        self.empID = empID
        self.dateWorked = dateWorked
        self.hoursWorked = hoursWorked

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

empObjectDict = {}
hrsObjectDict = {}

with open("employees.txt", "r") as emp:

    empList = []

    for item in emp: #line in employees.txt

        empList.append(item)
        #print(str(empList))  ['BAT1536 WAYNE BRUCE 40 25 1.5 80 750\n', 'MAN1331 MAN BAT 35 45 1.5 80 700']

    for item in empList: #field line in above array

        empDetails = item.split() 
        #print(str(empDetails)) [BAT1536, WAYNE, BRUCE, 40, 25, 1.5, 80, 750\n]

        empObject = Employee(empDetails[0],empDetails[1],empDetails[2]
            ,empDetails[3],empDetails[4],empDetails[5],empDetails[6],empDetails[7])
        #Employee object CTR:
        #Employee(empID: str, lName: str, fName: str, regHours: float, 
                #hourlyRate: float, otMultiple: float, taxCredit: float, standardBand: float)

        empObjectDict[empDetails[0]] = empObject #add employee object to emp object list

    for k, v in empObjectDict.items():
        print(k + " : " + str(v.fName))
    

with open("hours.txt", "r") as hrs:
    
    hoursList = []

    for item in hrs: #line in hours.txt
        lis = item.split()
        hoursList.append(lis)
        # print(item) => BAT1536 01/01/2021 40

    for item in hoursList:
        empID = item[0]
        if empID not in hrsObjectDict.keys():
            hrsObjectDict[empID] = []
        else:
            hrsObjectDict[empID].append(item)


    print(str(hrsObjectDict))
    # print(str(hoursList)) => [['BAT1536', '01/01/2021', '40'], ['BAT1536', '08/01/2021', '35'],...]
            
        # print(str(item))


        
        # empID = item.split(" ")[0]
        # # print(empID)
        # # print("empID")

        # if empID not in hrsObjectDict.keys():
        #     print(str(lis))
        #     print("here")
        #     val = []
        #     hrsObjectDict[empID] = val.append(item.split())
        
        # else:
        #     print(str(lis))
        #     print("there")
        #     val = []
        #     hrsObjectDict[empID] = val.append(item.split())













########################################################################################################