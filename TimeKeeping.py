# Sean Mayers
# 11/8/2020
# Week3 Inheritance 

"""
For this exercise, we want you to code a generic superclass and at least three
subclasses of that superclass, each class needs to have at least 2 attributes and 2 methods.
It’s easiest to simply describe a real-world object in this manner.
You need to provide a test method that shows your classes in operation.

"""

# Superclass
class Payroll:
    
    def __init__(self, wages, taxes):
        self.wages = wages
        self.taxes = taxes
        
    def isBasePay(self):
        return False
    
    def isOverTimePay(self):
        return False
    
    def isVactionPay(self):
        return False
    
    
# SubClass       
class BasePay(Payroll):
   
    def __init__(self, wages, taxes, hours):
        Payroll.__init__(wages, taxes)
        self.hours = hours
        
    def isBasePay(self):
        return True
        
# SubClass        
class OverTimePay(Payroll):
    
    def __init__(self, wages, taxes, hours):
        Payroll.__init__(wages, taxes)
        self.hours = hours
    
    def isOverTimePay(self):
        return True
        
        
# SubClass 
class VacationPay(Payroll):
    def __init__(self, wages, taxes, hours):
        Payroll.__init__(wages, taxes)
        self.hours = hours
        
    def isVactionPay(self):
        return True
    
# total payroll (wages and taxes)   
pay1 = Payroll(20000, 4500)    # Object of payroll
print(pay1.wages, pay1.taxes)

print("\n")


    
    

 
 
 

    
    
        
        