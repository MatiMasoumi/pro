class Counter:
  def __init__(self):
    self.count=0
  def incerment(self):
    self.count += 1

  def decerment(self):
    if self.count > 0:
      self.count -= 1
  def reset(self):
    self.count = 0
  def get_count(self):
    return self.count
counter=Counter()

counter.incerment()
print("Count after incerment:",counter.get_count())

counter.decerment()
print("Count after decerment:",counter.get_count())

counter.incerment()
print("Count after another decerment:",counter.get_count())


counter.incerment()
counter.incerment()
print("Counter after two incerment:",counter.get_count())
counter.reset()
print("Counter after reset:",counter.get_count())


