# odd even program
# num = int(input())
# if num % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")

# bmi calculator 2.0
# height=float(input("Enter your height : "))
# weight=int(input("Enter your weight : "))
# bmi=weight/height**2
# if bmi<18.5:
#     print(f"bmi : {bmi} Eat more,You are underweight.")
# elif bmi<25:
#     print(f"bmi : {bmi} Your'e bmi is normal.")
# elif bmi<30:
#     print(f"bmi : {bmi} You are slightly overweight.")
# elif bmi<35:
#     print(f"bmi : {bmi} You are obese")
# else:
#     print(f"bmi : {bmi} You are clinically obese")

# leap year program
# year=int(input("Enter a year : "))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print(f"{year} is a leap year")
#     else:
#         print(f"{year} is a leap year")
# else:
#     print(f"{year}  is not lear year")

# pizza ordering
# print("Welcome to python pizzas")
# size = input("Enter the size of pizza S,M or L ? ")
# peporini = input("Do you want peporini ? y or N ? ")
# cheese = input("Do you want extra cheese ? Y or N ? ")
# bill = 0
# if size == 'S' or size == 's':
#     bill += 15
# elif size == 'M' or size == 'm':
#     bill += 20
# else:
#     bill += 25
# if peporini == 'Y' or peporini == 'y':
#     if size == 's' or size == 'S':
#         bill += 2
#     else:
#         bill += 3
# if cheese == 'Y' or cheese == 'y':
#     bill += 1
# print(f"Thank you for ordering your bill is {bill}")

#love calculator
# name1=input("Enter name 1 : ")
# name2=input("Enter name 2 : ")
# combined=name1+name2
# t=combined.lower().count('t')
# r=combined.lower().count('r')
# u=combined.lower().count('u')
# e=combined.lower().count('e')
# true=str(t+r+u+e)
# l=combined.lower().count('l')
# o=combined.lower().count('o')
# v=combined.lower().count('v')
# e=combined.lower().count('e')
# love=str(l+o+v+e)
# truelove=true+love
# if int(truelove)<10 or int(truelove)>90:
#     print(f"You are like coke and mentos {truelove}")
# elif int(truelove)>=40 or int(truelove)<=50:
#     print("You are alright")
# else:
#     print(f"Your score is {truelove}")

#final project
print("welcome to treasure hunt !!! ")
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************''')
road=input("You have two roads ahead of you where will you go right or left ? type your choice : ")
if road=='right' or road=='Right':
    choice=input("Now you have a river in front of you do you want to swim in the water or wait for the boat ? type swim or wait :")
    if choice=="wait" or choice=="Wait":
        door=input("You have 3 doors ahead of you red , blue and yellow type your choice to go in : red blue and yellow ?")
        if door=='red' or door=="Red":
            print("You died the door have demons in that.")
        elif door=="blue" or door=="Blue":
            print("You died as you fell in hole.")
        else:
            print("Congratulations , You found the treasure")
    else:
        print("You died the sharks ate you ")
else:
    print("Game over you died as you fell of the broken bridge")