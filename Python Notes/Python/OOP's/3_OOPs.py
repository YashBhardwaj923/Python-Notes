class Person:
    # this is the constructor function:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def test(self):
        print(f"Name : {self.name}. Age : {self.age}. Gender : {self.gender}. Address : {self.address}")

user1 = Person("Vineet Bhardwaj", 23, "Male", "New Delhi")
user1.test()

user2 = Person("Anamika", 28, "Female", "Noida")
user2.test()

user3 = Person("Mohan Kumar Mishra", 25, "Male", "Bhopal")
user3.test()