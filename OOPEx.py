# Difference between procedural programming and OOP: 

# Procedural 
# baseSalary = 30000
# overtime = 10
# rate = 20 

# def getWage(baseSalary, overtime,rate):
# 	return baseSalary + (overtime * rate)


# OOP 

class employee:
  
  #data members of class
  baseSalary = 30000  #attribute 1
  overtime = 10
  rate = 20
  #class default constructor

  def __init__(self,baseSalary,overtime, rate): 
          self.baseSalary = baseSalary
          self.overtime = overtime
          self.rate = rate
  
  def getWage(self):
  		return self.baseSalary + (self.overtime * self.rate)

Employee1 = employee(30000, 10, 20)

wage = Employee1.getWage()

print(f'total wage: {wage}')