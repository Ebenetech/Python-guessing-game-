print("Welcome to my Hub")

request_play = input("Do you want to play? : ")


text = "Nice one! "
print(text.lower())

if request_play != "yes":
    exit()
    
print("Okay! Let's 🎮 ")
score = 0

answer = input("what is the full meaning of btc?: ")
if answer.lower() == "Bitcoin":
    print("Correct ✔")
    score += 2
else:
    print("Incorrect 👎")

answer = input("What is the full meaning of GPU?: ")
if answer.lower() == "graphics processing unit":
    print("Correct ✔")
    score += 2
else:
    print("Incorrect 👎")
    
answer = input("is blockchain and cryptocurrency the same?:  ")
if answer.lower() == "no":
    print("Correct ✔")
    score += 2
else:
    print("Incorrect 👎")
    
answer = input("which is most popular smart contract programming language?  ")
if answer.lower() == "solidity":
    print("Correct ✔")
    score += 2
else:
    print("Incorrect 👎")

answer = input("which year was the internet given birth to?  ")
if answer.lower() == "1960":
    print("Correct ✔")
    score += 2
else:
    print("Incorrect 👎")


print("You got ", str(score), " questions correct")
print("You got ", str((score /5) * 100), "%")