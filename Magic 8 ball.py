import sys
import random

ans = True

while ans:
    question = input("Ask the magic 8 ball a question: (press enter to quit) ")
    answers = random.randint(1,8)

    if question =="":
        sys.exit()
    elif answers==1:
        print("It's certain")
    elif answers ==2:
        print("Good")
    elif answers==3:
        print("On the way bro")
    elif answers==4:
        print("Ask again later")
    elif answers==5:
        print("Focus and ask again")
    elif answers==6:
        print("Reply and ask dude")
    elif answers==7:
        print("My answer is no")
    elif answers==8:
        print("my sources say no")
    else:
        print("Shutdown")