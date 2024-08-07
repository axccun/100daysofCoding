#flippin coin
# import random
# coin=random.randint(0,1)
# if coin==1:
#     print("heads")
# else:
#     print("tails")
import random

#who ll pay the bill
# import random
# names=["Akash" ,"Nico","Poli","Akku","kalyani"]
# lenofnames=len(names)
# randomnumber=random.randint(0,lenofnames-1)
# print(f"{names[randomnumber]} will pay the bill today !!")

#treasure map
# line1=["[]","[]","[]"]
# line2=["[]","[]","[]"]
# line3=["[]","[]","[]"]
# mapa=[line1,line2,line3]
# position=input().lower()
# letterposi=position[0]
# abc=['a','b','c']
# mapa[int(position[1])-1][abc.index(letterposi)]='X'
# print(f"{line1}\n{line2}\n{line3}")


#Rock paper scissors
import random
Rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choice = int(input("Enter your choice 0 for rock,1 for paper and 2 for scissors : "))
computer=random.randint(0,2)
if choice==0 and computer==1:
    print(f"you : \n{Rock}\n bot : \n{Paper}\n You Loose !!")
elif choice==0 and computer==2:
    print(f"you : \n{Rock}\n bot : \n{Scissors}\n You Win !!")
elif choice==0 and computer==0:
    print(f"you : \n{Rock}\n bot : \n{Rock}\n Draw !!")
elif choice==1 and computer==1:
    print(f"you : \n{Paper}\n bot : \n{Paper}\n Draw !!")
elif choice==1 and computer==2:
    print(f"you : \n{Paper}\n bot : \n{Scissors}\n You Loose !!")
elif choice==1 and computer==0:
    print(f"you : \n{Paper}\n bot : \n{Rock}\n You Win !!")
elif choice==2 and computer==1:
    print(f"you : \n{Scissors}\n bot : \n{Paper}\n You Win !!")
elif choice==2 and computer==2:
    print(f"you : \n{Scissors}\n bot : \n{Scissors}\n Draw !!")
else:
    print(f"you : \n{Scissors}\n bot : \n{Rock}\n You Loose !!")
