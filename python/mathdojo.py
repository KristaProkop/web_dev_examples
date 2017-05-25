class MathDojo(object):
  def __init__(self):
    self.result = 0

  def add(self, item1, *item2):
    if type(item1) == list or type(item1) == tuple:
      for num in item1:
        self.result += num
    else:
      self.result += item1
    if item2:
      for num in item2:
        if type(num) == list or type(num) == tuple:
          for subItem in num:
            self.result += subItem
        else:
          self.result += num
    return self

  def subtract(self, item1, *item2):
    if type(item1) == list or type(item1) == tuple:
      for var in item1:
        self.result -= var
    else:
      self.result -= item1
    if item2:
      for num in item2:
        if type(num) == list or type(num) == tuple:
          for var in num:
            self.result -= var
        else:
          self.result -= num
    return self

print MathDojo().add(2).add(2, 5).subtract(3, 2).result
print MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result
#print MathDojo().subtract(-2, [2,3], (1.1+2.3)).result

