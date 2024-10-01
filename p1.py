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