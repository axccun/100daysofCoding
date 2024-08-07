# summing the height of students
# heights=input().split()
# sumofheights=0
# numofstudents=0
# for height in range(0,len(heights)):
#     heights[height]=int(heights[height])
#     sumofheights+=heights[height]
#     numofstudents+=1
# print(f"The number of students are {numofstudents} and sum the heights are {sumofheights}")

#finiding the highest score
# scores=input().split()
# for i in range(0,len(scores)):
#     scores[i]=int(scores[i])
# maxScore=0
# for score in scores:
#     if score>maxScore:
#         maxScore=score
# print(f"MAx score is {maxScore}")

#summing the even number upto n
# number=int(input("enter the range of the number : "))
# total=0
# for i in range(0,number+1): #or for i in range(2,number+1,2):
#     if i%2==0: #skipthis
#         total+=i #indent it properly
# print(f"The sum of all the even numbers is range {number} is {total}")

#fizzbuzz
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print("fizz Buzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)

#password generator
import random
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
digit=['0','1','2','3','4','5','6','7','8','9']
symbols=['~','!','@','#','$','%','^','&','(',')']
alphabets=int(input("Enter the number of letters you want in ur password : "))
digits=int(input("Enter the number of digits you want : "))
symbolss=int(input("Enter the number of symbols you want in ur passoword : "))
password=''
for i in range(1,alphabets+1):
    password+=random.choice(alpha)
for i in range(1,digits+1):
    password+=random.choice(digit)
for i in range(1,symbolss+1):
    password+=random.choice(symbols)
l = list(password)
random.shuffle(l)
result = ''.join(l)
print(f"You password is {result}")