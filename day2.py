# weight=float(input())
# height=float(input())
# bmi=weight/(height**2)
# print(int(bmi))

# weeks left calculator
# age=int(input("Enter age :"))
# yearsleft=90-age
# print(round((yearsleft*365)/7))

#day2 project
print("Welcome to the tip calculator !")
bill=float(input("Enter the bill amount :\n"))
tip=int(input("Enter the amount of tip you want to give 10,12 or 15 ?\n"))
percent=(bill*tip)/100+bill
People=int(input("Enter the number of people you want to split the bill ?\n"))
splitamount=round(percent/People,2)
print(f"Your total bill was {percent} and each person has to pay {splitamount}")