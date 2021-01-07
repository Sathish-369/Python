

user=["sathish","sreenivasan","abbi","mano","satabbi"]
print(user)

while True:
    print("***********************")
    print("****               ****")
    print("Welcome to AlienTek")
    print("****               ****")
    print("***********************")

    name = (input("Enter your employee name: ")).strip()

    if name in user:
      print("Welcome Mr.{}".format(name))

      remove=(input("Would you like to remove above name (y/n)?:  "))
      if(remove == "y"):
          user.remove(name)
      else:
          print("No problem I didn't want you to leave")
      print(user)
    else:
      print("Not valid name")
      add=input("Would you like to add your name in the system (y/n)?:  ")

      if(add =="y"):
          user.append(name)
          print(user)
      else:
          print("See you later")
