

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

      remove=(input("enter employee name who is not here (y/n)?:  "))
      if(remove == "y"):
          user.remove(name)
      else:
          print("no problem I didn't want you to leave")


      print(user)
    else:
      print("Not valid name")