# here, i am creating a "Students" name class.
class Students:
    # there are fields in the class.
    id = 1
    name = "Tushar Sharma"
    age = 28
    city = "Mathura"
    skill = "Full-Stack Developer"

# create a new object.
std1 = Students()
print(f"My id is {std1.id}. My name is {std1.name}. I am {std1.age} years old. I am living in {std1.city}. My skill is {std1.skill}.")

std2 = Students()
# modify std2 object with new data on old properties(keys).
std2.id = 2
std2.name = "Ayushi Sharma"
std2.age = 27
std2.city = "Delhi"
std2.skill = "Front-End Developer"
print(f"My id is {std2.id}. My name is {std2.name}. I am {std2.age} years old. I am living in {std2.city}. My skill is {std2.skill}.")