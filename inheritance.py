class pet:
    def __init__(self,name,age ):
        self.name=name 
        self.age =age 


    def show(self):
        print(f"I am {self.name} and I am {self.age} years old ")

class CAt(pet):  # inheritance.......

    def __init__(self,name,age):
        self.name =name
        self.age=age


    def speak(self):
        print("Meow")



class DOg(pet):


    
    def speak(self):
        print("bark")



p = pet("Tim", 19)
p.speak()

c=CAt("Bill" , 34)
c.show()
c.speak()



