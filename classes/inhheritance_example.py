class BaseClassName():

  baseSharedData = 'base Shared Data'

  def __init__(self):
    self.baseData = 'base class data'

  def baseMethod(self):
    print('base method called from base class')

class DerivedClassName(BaseClassName):

  def __init__(self):
    self.derivedData = 'derived data'

  def baseMethod(self):
    BaseClassName.baseMethod(self) #call the base class' method
    print('base method called from derived class')

a = DerivedClassName()
a.baseMethod()
a.derivedData # outout = 'derived data'
a.baseSharedData # output = 'base shared data'
a.baseData # error