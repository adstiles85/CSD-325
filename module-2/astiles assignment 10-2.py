"""
Name: Andrew Stiles
Date: 12-15-2024 (Updated 1-19-2025)
Assignment: Module 10-2 Assignment
Purpose: This program defines Employee and ProductionWorker classes with attribute managers.
Note: This program is being used for an assignment in Advanced Python to debug. Assignment 2.2
Citation: N/A
"""

# Create Employee class
class Employee:
    def __init__(self):
        self.__name = ""
        self.__gender = ""
        self.__hourlyPayRate = 0.0
        self.__employeeNumber = 0

    # The Setters
    def setName(self, name):
        self.__name = name

    def setGender(self, gender):
        self.__gender = gender

    def setHourlyPayRate(self, hourlyPayRate):
        self.__hourlyPayRate = hourlyPayRate

    def setEmployeeNumber(self, employeeNumber):
        self.__employeeNumber = employeeNumber

    def setDepartment(self, department):  # New setter for department
        self.__department = department

    # The Getters
    def getName(self):
        return self.__name

    def getGender(self):
        return self.__gender

    def getHourlyPayRate(self):
        return self.__hourlyPayRate

    def getEmployeeNumber(self):
        return self.__employeeNumber
    
    def getDepartment(self):  # New getter for department
        return self.__department

# Create ProductionWorker Subclass
class ProductionWorker(Employee):
    def __init__(self):
        super().__init__()
        self.__shiftNumber = 0

    # Setter for shiftNumber
    def setShiftNumber(self, shiftNumber):
        self.__shiftNumber = shiftNumber

    # Getter for shiftNumber
    def getShiftNumber(self):
        return self.__shiftNumber

# Main class to show the Employee and ProductionWorker classes
class Main:
    @staticmethod
    def run():
        # Create two Employee instances
        employee1 = Employee()
        employee1.setName("Harry Potter")
        employee1.setGender("Male")
        employee1.setHourlyPayRate(27.00)
        employee1.setEmployeeNumber(101)
        employee1.setDepartment("Magic Department")  # Intentional typo: 'setDepatment' instead of 'setDepartment'

        employee2 = Employee()
        employee2.setName("Hermione Granger")
        employee2.setGender("Female")
        employee2.setHourlyPayRate(26.50)
        employee2.setEmployeeNumber(102)
        employee2.setDepartment("Research Department")

        # Create two ProductionWorker instances
        worker1 = ProductionWorker()
        worker1.setName("Luna Lovegood")
        worker1.setGender("Female")
        worker1.setHourlyPayRate(26.75)
        worker1.setEmployeeNumber(201)
        worker1.setDepartment("Customer Service Department")
        worker1.setShiftNumber(1)

        worker2 = ProductionWorker()
        worker2.setName("Ronald Weasley")
        worker2.setGender("Male")
        worker2.setHourlyPayRate(29.75)
        worker2.setEmployeeNumber(202)
        worker1.setDepartment("Manufacturing")
        worker2.setShiftNumber(3)

        # Display details for Employees
        print("\nEmployee Details:\n")
        print(f"Name: {employee1.getName()}")
        print(f"Gender: {employee1.getGender()}")
        print(f"Hourly Pay: ${employee1.getHourlyPayRate():.2f}")
        print(f"Employee Number: {employee1.getEmployeeNumber()}\n")
        print(f"Department: {employee1.getDepartment()}\n")  # Display department

        print(f"Name: {employee2.getName()}")
        print(f"Gender: {employee2.getGender()}")
        print(f"Hourly Pay: ${employee2.getHourlyPayRate():.2f}")
        print(f"Employee Number: {employee2.getEmployeeNumber()}\n")
        print(f"Department: {employee2.getDepartment()}\n")  # Display department

        # Display details for ProductionWorkers
        print("Production Worker Details:\n")
        shiftNames = {1: "Morning", 2: "Evening", 3: "Night"}
        print(f"Name: {worker1.getName()}")
        print(f"Gender: {worker1.getGender()}")
        print(f"Hourly Pay: ${worker1.getHourlyPayRate():.2f}")
        print(f"Employee Number: {worker1.getEmployeeNumber()}")
        print(f"Department: {worker1.getDepartment()}\n")  # Display department
        print(f"Shift: {shiftNames.get(worker1.getShiftNumber(), 'Unknown')}\n")

        print(f"Name: {worker2.getName()}")
        print(f"Gender: {worker2.getGender()}")
        print(f"Hourly Pay: ${worker2.getHourlyPayRate():.2f}")
        print(f"Employee Number: {worker2.getEmployeeNumber()}")
        print(f"Department: {worker2.getDepartment()}\n")  # Display department
        print(f"Shift: {shiftNames.get(worker2.getShiftNumber(), 'Unknown')}\n")

# Run Main
if __name__ == "__main__":
    Main.run()


