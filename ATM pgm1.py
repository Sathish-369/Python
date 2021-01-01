import getpass
import string
import os

# creating user and pin and statement
users=["sathish","abbi","mano"]
pins=["12","123","1234"]
amount=[1000,2000,3000]
count=0

#while loop checking existance of the entered username

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("^^                             ^^")
print("welcome to source-code ATM system")
print("^^                             ^^")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

while  True:
    user = input('\nenter user name:  ')
    user= user.lower()
    if user in users:
        if user == users[0]:
            n=0
        elif user == users[1]:
            n=1
        else:
            n=2
        break

    else:
        print("-------------")
        print("invalid  user name")
        print("---------")

## comparing pin

while count <3:
    print("---------")
    pin=input("enter the pin:  ")
    print("--------")

    if pin.isdigit():
     if user=="sathish":
        if pin == pins[0]:
            break
        else:
             count+=1
             print("--------")
             print("invalid pin")
             print("---------")
             print()

    if user=="abbi":
        if pin==pins[1]:
            break

        else:
             count+=1
             print("--------")
             print("invalid pin")
             print("--------")
             print()

    if user=="mano":
        if pin==pins[2]:
            break

        else:
            count+=1
            print('-------')
            print("invalid pin")
            print("------")
            print()

else:
    print("----")
    print("pin consists of 4 digit")
    print("------")
    count+=1


## in case of valid pin-continuing or exiting

if count==3:
    print("--------")
    print("3 unsuccessful pin attempt, exiting")
    print("your card has been locked")
    print("---------")
    exit()

print("------")
print("login success so you continue")
print("---------")
print(str.capitalize(users[n]), "welcome to ATM")
print("-----------")
print("^^^^^^^^^ ATM SYSTEM^^^^^^^^^^^")

### Mani Menu

while True:
    #os.system('clear)

    print("------")
    print("------")
    response=input("SELECT FROM FOLLOWING OPTIONS: \nStatement__(s) \nWithdraw___(w) \nlodgement__(l) \nChangepin__(p) \nQuit__(q) "
                   "\ntype the letter of your choices:") .lower()

    print("------")
    print("------")
    valid_responses =['s','w','p','q']
    response=response.lower()
    if response=='s':
        print("------")
        print("------")
        print(str.capitalize(users[n]), "you have", amount[n],"euro on your account")
        print("------")
        print("------")
    elif response=='w':
        print("------")
        print("------")
        cash_out=int(input("enter amount you would like to withdraw"))
        print("------")
        print("------")
        if cash_out%10 !=0:
            print("------")
            print("------")
            print("amount you want to withdraw must to match 10 euro note ")
            print("------")
            print("------")
        elif cash_out>amount[n]:
            print("------")
            print("------")
            print("you have insufficient balance")
            print("------")
            print("------")
        else:
            amount[n] =amount[n]-cash_out
            print("------")
            print("------")
            print("your new balance is:  ",amount[n],'euro')
            print("------")
            print("------")
    elif response =='1':
        print()
        print("------")
        print("------")
        cash_in =int(input("enter amount you want to lodge"))
        print("------")
        print("------")
        print()
        if cash_in%10 !=0:
            print("------")
            print("------")
            print("amount you want to lodge must to match with 10 euro notes")
            print("------")
            print("------")
        else:
            amount[n] = amount[n]+cash_in
            print("------")
            print("------")
            print("your new balance is:",amount[n],'euro')
            print("------")
            print("------")
    elif response=='p':
        print("------")
        print("------")
        new_pin =str(getpass.getpass("enter a new pin"))
        print("------")
        print("------")
        if new_pin.isdigit()and new_pin !=pin[n] and len(new_pin) ==4:
            print("------")
            print("------")
            new_pin=str(getpass.getpass("confirm new pin"))
            print("------")
            print("------")
            if new_pin !=new_pin:
                print("------")
                print("------")
                print("pin mismatch")
                print("------")
                print("------")
            else:
                pins[n]=new_pin
                print("New pin saved")
        else:
            print("------")
            print("------")
            print("new pin consist of 4 digit \n and must be different to previous pin")
            print("------")
            print("------")
    elif response =='q':
        exit()
    else:
        print("------")
        print("------")
        print("response not valid")
        print("------")
        print("------")






