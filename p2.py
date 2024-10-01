class Calculator:
  def add(self,x,y):
    return x+y
  def subtract(self,x,y):
    return x-y
  def multiply(self,x,y):
    return x*y
  def divide(self,x,y):
    if y == 0:
      return "Error! Division by zero."
    return x/y
  
  cal=Calculator()
print("Addition:",cal.add(10,5))
print("Subtraction:",cal.subtract(10,5))
print("Multiplication:",cal.multiply(10,5))
print("Division:",cal.divide(10,5))
print("Division by zero:",cal.divide(10,5))