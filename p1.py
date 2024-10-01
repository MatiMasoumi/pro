class Rectangle:
  def __init__(self,length,width):
    self.length=length
    self.width=width
  def area(self):
    return self.length * self.width
  def perimeter(self):
    return 2 * (self.length + self.width)
  def display(self):
    print(f'Length:{self.length},Width:{self.width}')
    rect1=Rectangle(10,5)
rect2=Rectangle(7,3)
rect1.display()
print("AREA:",rect1.area())
print("Perimeter:",rect1.perimeter())

rect2.display()
print("AREA:",rect2.area())
print("Perimeter:",rect2.perimeter())