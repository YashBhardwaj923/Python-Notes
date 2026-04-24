class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"name is {self.name} and age is {self.age}.")

# user1 = Parent("Rahul Sharma", 34)
# user1.info()

class Child(Parent):
    def __init__(self, name, age, gender, address): 
        Parent.__init__(self, name, age)

        self.gender = gender
        self.address = address 

    def data(self):
        print(f"name is {self.name} and age is {self.age}. Gender is {self.gender}. Address is {self.address}.")

child_user = Child("Ayushi Jain", 34, "Female", "Delhi")
child_user.data()
child_user.info()
