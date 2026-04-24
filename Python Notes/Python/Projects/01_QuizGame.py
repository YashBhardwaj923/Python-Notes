# yah sabse pahle display hone vala text hai screen par:
print("Welcome to my computer quiz!")

# yahan par yah check kiya gya hai ki user game khelna chahta hai ya nahi!:
playing = input("Do you want to play? : ")
if playing.lower() != "yes":
    quit()

# agar user game khelna chahta hai to use yah display show hoga:
print("OK!, Let's Play : :)")

# ye basically score calculate karne ke liye ek variable declare kiya gya hai:
score = 0

# ye hamne ek question define kiya hai, jisme user se ham answer le rahe hain aur answer ko ".lower()" function ka use kare, user input ko lower case me change kar diya hai:
answer = input("What does HTML stands for? => ")
if answer.lower() == "hyper text markup language":
    print("Correct")
    score += 1 # yadi answer correct hota hai to user ka ek score add ho jata hai.
else:
    print("Incorrect")

answer = input("What does CSS stands for? => ")
if answer.lower() == "cascading style sheet":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does MERN stands for? => ")
if answer.lower() == "mongodb expressjs reactjs nodejs":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does VS stands for? => ")
if answer.lower() == "visual studio code editor":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does JS stands for? => ")
if answer.lower() == "javascript":
    print("Correct")
    score += 1
else:
    print("Incorrect")

# ye lines user ka total score dikhane ka kaam karti hain aur questions ke hisab se percentage bhi show karega.
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")