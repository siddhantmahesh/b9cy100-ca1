import unittest

######################################## GITHUB REPO ################################################

#       repo link : https://github.com/siddhantmahesh/b9cy100-ca1.git

######################################## GITHUB REPO ################################################


######################################### EMPLOYEE CLASS ######################################################
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

        # check for negative values
        if regHours < 0 or \
        hourlyRate < 0 or \
            otMultiple < 0 or \
                taxCredit < 0 or \
                    standardBand < 0 :
                    #if negative values found, notify
            raise ValueError("\nInvalid value check : Employee " + empID + "\n")


    def computePayment(self, hoursWorked:float, dateWorked:str):

        regularHrsWorked = 0
        regularPay = 0
        otHrsWorked = 0
        otRate = self.hourlyRate * self.otMultiple
        otPay = 0

        if hoursWorked > self.regHours:
            
            regularHrsWorked = self.regHours #regular hours worked cannot be greater than regular hours
            otHrsWorked = hoursWorked - self.regHours #overtime hours = total hours worked - regular hours
            otPay = otHrsWorked * otRate #calc ovetime pay
            regularPay = regularHrsWorked * self.hourlyRate #calc regular pay
        
        else:

            regularHrsWorked = hoursWorked #hours worked <= reg. hours worked, then hours worked = regular hours
            regularPay = hoursWorked * self.hourlyRate #calc regular pay

        grossPay = regularPay + otPay
        higherRatePay = grossPay - self.standardBand if grossPay > self.standardBand else 0
        # if gross pay > standard band, higher pay rate = earnings above gross pay else higher rate earnings

        standardTax = 0.2 * (self.standardBand if higherRatePay != 0 else grossPay)
        # if gross pay < standard band, tax applicable only on amount below standard band
        # else tax applicable on full band amount

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
########################################### EMPLOYEE CLASS ######################################################


def computeAllPayments(employeeFile:str, hoursFile:str):

    empObjectDict = {} #all emp objects read from file stored here
    hrsObjectDict = {} #all hours data read from file stored here

    ############################## READ FROM EMPLOYEE AND HOURS FILE ######################################################
    try:
        with open(employeeFile, "r") as emp:
            empList = [] #store lines read from emp file here

            for item in emp: #line in employees.txt
                empList.append(item)

            for item in empList: #field line in above array

                empDetails = [] #convert each line read into a list, store here
                empDetails = item.split() 

                try:
                    empObject = Employee(empDetails[0],empDetails[1],empDetails[2]
                        ,float(empDetails[3]),float(empDetails[4]),float(empDetails[5])
                        ,float(empDetails[6]),float(empDetails[7]))
                #Employee object CTR:
                #Employee(empID: str, lName: str, fName: str, regHours: float, 
                        #hourlyRate: float, otMultiple: float, taxCredit: float, standardBand: float)

                except TypeError as e : #catch alphabets/alphanumeric conversion errors
                    print(e)
                    # print(1)
                    continue #or quit()
                except ValueError as e : #catch errors generated by negative input values
                    print(e)
                    # print(2)
                    continue #or quit()
                except Exception as e:
                    print(e)
                    # print(3)
                    quit()

                empObjectDict[empDetails[0]] = empObject #add employee object to emp object dictionary {empid : empobject}

        with open(hoursFile, "r") as hrs:
            hoursList = [] #store hours data here

            for item in hrs: #line in hours.txt
                lis = item.split() #convert line to a list
                hoursList.append(lis)

            for item in hoursList:
                empID = item[0]

                if empID not in hrsObjectDict.keys():
                    hrsObjectDict[empID] = [] # create empty list for first occurance of the empid, 
                                                #or else the append function below doesnt work

                hrsObjectDict[empID].append(item) # map hours data with its empid {empid1 : [[h1],[h2],[h3]]},
                                                                                # {empid2 : [[h1],[h2],[h3]]}

    except FileNotFoundError as e:
        print(e)
        # print(4)
        quit()
    except Exception as e:
        print(e)
        # print(45)
        quit()
    ############################## READ FROM EMPLOYEE AND HOURS FILE ######################################################


    ############################## GENERATE EMPLOYEE PAYMENT DETAILS FROM DICITONARIES ########################################

    computedWages = [] #store all the computed wages in this list

    for k, v in hrsObjectDict.items(): #compute wages by looping through the hours dictionary
        empID = k #emp id
        empHrs = v #list of hours worked wrt date

        if empID not in empObjectDict.keys(): #check for data entered for invalid employee id
            print("\nInvalid employee ID in hours file : " + str(empID) + "\n")
            continue
        
        for item in empHrs:
            try:
                if float(item[2]) < 0: #check for negative hours input, notify in case
                    print("\nInvalid hours worked for : " + str(item) + "\n")
                    continue

                computedWages.append(empObjectDict[empID].computePayment(float(item[2]), item[1])) #append successful computation here

            except TypeError as e : #catch alphabets/alphanumeric conversion errors
                print(e)
                # print(11)
                continue #or quit()
            except ValueError as e : #catch errors generated by negative input values
                print(e)
                # print(22)
                continue #or quit()
            except Exception as e:
                print(e)
                # print(33)
                quit()

    print("\nComputed Wages : \n" + str(computedWages)) #print consolidated computation
    
    ############################## GENERATE EMPLOYEE PAYMENT DETAILS FROM DICITONARIES ########################################
    

####################################### TEST CASES ##########################################################
class ComputeTestCases(unittest.TestCase):

    # TC #1 Net pay cannot exceed gross pay 
    def testGrossAndNetPay(self):
        e = Employee("G10", "jackson", "michael", 40, 55, 1.5, 100, 2000)
        computeData = e.computePayment(60, "1/1/2020")
        netPay = computeData["net pay"]
        grossPay = computeData["gross pay"]
        self.assertGreaterEqual(grossPay, netPay)

    # TC #2 Overtime hours cannot be negative 
    def testOverTimePay(self):
        e = Employee("G10", "jackson", "michael", 40, 55, 1.5, 100, 2000)
        computeData = e.computePayment(100, "1/1/2020")
        overTimePay = computeData["ot pay"]
        self.assertGreaterEqual(overTimePay, 0)

    # TC #3 Overtime hours cannot be negative
    def testOverTimeHrs(self):
        e = Employee("G10", "jackson", "michael", 40, 55, 1.5, 100, 2000)
        computeData = e.computePayment(50, "1/1/2020")
        overTimeHrs = computeData["ot hrs worked"]
        self.assertGreaterEqual(overTimeHrs, 0)

    #TC #4 Regular Hours Worked cannot exceed hours worked
    def testRegularHours(self):
        e = Employee("G10", "jackson", "michael", 40, 55, 1.5, 100, 2000)
        hrsWorked = 60 #declared as a variable since emp object doesnt have this property, neither computed by it
        computeData = e.computePayment(hrsWorked, "1/1/2020")
        regHrsWorked = computeData["regular hrs worked"]
        self.assertLessEqual(regHrsWorked, hrsWorked) #variable required for comparison

    #TC #5 Higher Tax cannot be negative.
    def testHigherTax(self):
        e = Employee("G10", "jackson", "michael", 40, 55, 1.5, 100, 2000)
        computeData = e.computePayment(50, "1/1/2020")
        higherTax = computeData["higher tax"]
        self.assertGreaterEqual(higherTax, 0)

    #TC #6 Net Pay cannot be negative.
    def testNetPay(self):
        e = Employee("G10", "jackson", "michael", 40, 55, 1.5, 100, 2000)
        computeData = e.computePayment(50, "1/1/2020")
        netPay = computeData["net pay"]
        self.assertGreaterEqual(netPay, 0)

unittest.main(argv=['ignored'], exit=False)

####################################### TEST CASES ##########################################################

# RUN CODE
computeAllPayments("./employees.txt", "./hours.txt")