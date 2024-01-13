class person:
    name='Sangeeta'
    age=25
    height=6
p1=person()
print(p1.name,p1.age,p1.height)
p2=person()
p2.name='Mona'
print(p2.name,p2.age,p2.height)

#Class declaration
class car:
    company='Honda'
    #constructor is created
    def __init__(self,price):
        self.price=34#if we are writing self.price=price than line 30 take argument of parameter in inside of class name
        #self.price=25 so here don't need to give argument inside class name
        self.price=price
    def priceofcar(self):
        # self.price=price
        print(self.price)
        
        #function defining here
    def details(self):
        print('car is white')
    def features(self,color):
        self.color=color
        print(self.color)
    
#object created and class call by obj        
obj=car('hi')# here u can give any type of argu if price is alredy defined in class but it is neccesary to give arg
obj=car(24)
obj.priceofcar()
# obj.details() 
# obj.features('red')
# obj.priceofcar()

#class declaration
class Person:
    #attribute of class
    name='abc'
    age=20
    height=5
#calling class by obj
p1=Person()
print(p1.name,p1.age,p1.height)

class Person:
    #attribute of class
    name='abc'
    age=20
    height=5
    def setage(self,newage):
        self.age=newage    
    def printAttributes(self):
        print(p1.name,p1.age,p1.height)
    
#calling class by obj
p1=Person()
print(p1.name,p1.age)
p2=Person()
p2.age=34
print(p2.age)
p2.setage(45)
p2.printAttributes()# why age did not chg


p2.setage(25)
print(p2.age)
p2.printAttributes()

class Person:
    #attribute of class
    name=''
    age=0
    height=0
    #constructor created
    def __init__(self,newname,newage,newheight):
        self.name=newname
        self.age=newage    
        self.height=newheight
        
    # def info(self,newage,newname,newheight):
    #     self.name=newname
    #     self.age=newage    
    #     self.height=newheight
    def Attributes(self):
        print(p1.name,p1.age,p1.height)
    
p1=Person('siya',25,2)
p1.Attributes()
# p1.info()
# p1.Attributes()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        