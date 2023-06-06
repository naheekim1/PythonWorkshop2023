#Constants for taxes and fees
STATETAX = 0.08
FEDERALTAX = 0.12
UNIONFEES = 0.02

def max(a, b):
    return a if a > b else b

class Employee:
    #sets the state tax owed by the employee
    #Returns: state taxes as a float
    def stateTax(self):
        return self.__gross * STATETAX
    
    #sets the federal tax owed by the employee
    #Returns: federal taxes as a float
    def federalTax(self):
        return self.__gross * FEDERALTAX

    #sets the unions fees owed by the employee
    #Returns: union fees as a float
    def unionFees(self):
        return self.__gross * UNIONFEES
    
    #sets the total income earned by the employee
    #Returns: gross income as a float
    def grossIncome(self):
        return self.__hours * self.__rate + max(0, self.__hours - 40) * self.__rate * 0.5 + max(0, self.__hours - 52) * self.__rate * 0.5

    #Computes the net income of the employee assuming fees, taxes, and gross income have all been computed first
    #Returns: net income as a float
    def netIncome(self):
        return self.__gross - (self.__state + self.__union + self.__fed)

    def __init__(self, nm, hrs, rte):
        self.__name = nm #Employee name
        self.__hours = hrs #Number of hours worked in a week
        self.__rate = rte #Pay per hour of work
        self.__gross = self.grossIncome() #gross income owed
        self.__state = self.stateTax() #state taxes owed
        self.__fed = self.federalTax() #federal taxes owed
        self.__union = self.unionFees() #union fees owed
        self.__netIncome = self.netIncome() #net income owed

   #Converts the employee into a string
    def __str__(self):
        return "----------------\nName: " + self.__name + "\nHours: " + str(self.__hours) + "\nRate: " + str(self.__rate) + "\n"

def main():
    output = ""
    run = True
    while run: #Run the following code block until the user says to stop
        #Get information on an employee
        print("------------------------")
        name = input("Enter employee name: ")
        hours = float(input("How many hours did this employee work? "))
        rate = float(input("How much is this employee paid? "))

        #Create an employee object just to convert it directly into a string. Add said string to the output
        output += str(Employee(name, hours, rate))

        #Ask the user if they want to put in another employee
        run = input("Is there another employee to enter data for? (type \"no\" to end the program) ") != "no"
    print(output)

main()

