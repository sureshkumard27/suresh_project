#Types of Properties
class Employee:
     def __init__(self,first,last,sal):
          self.first=first
          self.last=last
          self.sal=sal
     @property
     def email(self):
          return '{}.{}@email.com'.format(self.first,self.last)
     @property
     def fullname(self):
          return '{}{}'.format(self. first,self.last)
     @fullname.setter
     def fullname(self,name):
          first,last=name.split(' ')
          self.first=first
          self.last=last
     @fullname.deleter
     def fullname(self):
          self.first=None
          self.last=None
          print('Property Deleted')
     def __repr__(self):
          return 'Employee {}'.format(self.first)
     def __str__(self):
          return '{}'.format(self.fullname)

e=Employee('john','smith',500)
print(e.fullname)
print(e.email)
e.fullname='suresh kumar'
print(e.fullname)
print(e.email)
print(repr(e))
print(str(e))
del e.fullname
print(repr(e))