class details():
    name="kaushiki"
    age=21
    def info(self):
        print(f"{self.name} age is {self.age}")
obj=details()
print(obj.name)
print(obj.age)

a=details()
b=details()
c=details()

a.name="oggy"
a.age=4
b.name="jack"
a.info()
b.info()
c.info()

####################
class Person:
  name = "Harry"
  occupation = "Software Developer"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()

a.name = "Shubham"
a.occupation = "Accountant"
b.name = "Nitika"
b.occupation = "HR"
# print(a.name, a.occupation)
a.info()
b.info()
c.info()
