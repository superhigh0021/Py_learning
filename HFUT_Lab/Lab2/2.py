class Employee:
    def __init__(self,name,ID,salary) -> None:
        self.name=name
        self.ID=ID
        self.salary=salary
    def pay(self):
        print(self.pay)
    def show(self):
        print('{} {} {}'.format(self.name,self.ID,self.salary))
class Manager(Employee):
    def pay(self):
        print(self.pay)
    def show(self):
        print('{} {} {}'.format(self.name,self.ID,self.salary))

class Salesman(Employee):
    def pay(self):
        print(self.pay)
    def show(self):
        print('{} {} {}'.format(self.name,self.ID,self.salary))

a=Employee('zhangsan',2020210574,10000)
b=Manager('lisi',2020210599,1000)
a.show()
b.show()