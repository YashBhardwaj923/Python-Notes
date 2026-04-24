class Person:
    name = "ayushi jain"
    age = 23
    email = "ayushi@gmail.com"
    address = "delhi"

    def info(self, skills, qualifications):
        print(f"Name : {self.name}. Age : {self.age}. Email : {self.email}. Address : {self.address}. Skills : {skills}. Qualifications : {qualifications}")

user1 = Person()
user1.info("Football", "B.Tech")

user2 = Person()
user2.name = "Mohan Kumar Mishra"
user2.age = 25
user2.email = "mohan@gmail.com"
user2.address = "Bhopal"
user2.info("Cricket", "M.Tech")
