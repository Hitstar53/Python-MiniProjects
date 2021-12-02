print("WELCOME TO MY QUIZ GAME!")
play = input("Do you want to play?(yes/no)\n")

if play.lower() != "yes":
    quit()

print("Let's Play!\n")
count = 0
ans = input("1] What does CPU stand for?\n")
if ans.lower() == "central processing unit":
    print("Correct!")
    count += 1
else:
    print("Wrong!")

ans = input("2] What does GPU stand for?\n")
if ans.lower() == "graphics processing unit":
    print("Correct!")
    count += 1
else:
    print("Wrong!")

ans = input("3] What does RAM stand for?\n")
if ans.lower() == "random access memory":
    print("Correct!")
    count += 1
else:
    print("Wrong!")

ans = input("1] What does PSU stand for?\n")
if ans.lower() == "power supply":
    print("Correct!")
    count += 1
else:
    print("Wrong!")

print(f"Your total score is: {count}/4!\nYou got",count*25,"%")