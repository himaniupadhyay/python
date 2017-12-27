class Employee:
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name,", Salary: ", self.salary
        return

emp1 = Employee("luv", 2000)
emp2 = Employee("kush", 5000)
emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee %d" % Employee.empCount