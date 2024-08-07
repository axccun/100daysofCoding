# greet function
# def greet():
#     print("hello")
#     print("good morning")
#     print("byebye")
# greet()
# weeks left
# def life_in_weeks(age1):
#     yearsleft = 90 - age1
#     weeksLeft = yearsleft * 52
#     print(f"You have {weeksLeft} weeks left.")
# age = int(input("Enter your age : "))
# life_in_weeks(age)

# def greet_with(name,location):
#     print(f"hello {name},from {location}")
# greet_with('Akash','Mumbai')

# love score calculator
# def lovescore(lover1,lover2):
#     combinedname=lover1+lover2
#     T=combinedname.lower().count('t')
#     R = combinedname.lower().count('r')
#     U=combinedname.lower().count('u')
#     E = combinedname.lower().count('e')
#     L = combinedname.lower().count('l')
#     O = combinedname.lower().count('o')
#     V = combinedname.lower().count('v')
#     E = combinedname.lower().count('e')
#     sum=str(T+R+U+E)
#     sum1=str(L+O+V+E)
#     final=sum+sum1
#     print(f"love score : {final}")
# name1=input("Enter the name of person 1 : ")
# name2=input("enter the name of the person 2 :")
# lovescore(name1,name2)

# ceaser cipher
# def encryption(msg, shift1):
#     list1 = list(msg)
#     for i in range(len(list1)):
#         letter = list1[i]
#         indeterminable = alphabets.index(letter) + shift1
#         indeterminable %= len(alphabets)
#         list1[i] = alphabets[indeterminable]
#     print(''.join(list1))
#     # cipher=""
#     # for letter in msg:
#     #     shiftposi=alphabets.index(letter)+shift1
#     #     shiftposi%=len(alphabets)
#     #     cipher+=alphabets[shiftposi]
#     # print(cipher)
#
#
# def decrytion(msg, shift1):
#     list1 = list(msg)
#     for i in range(len(list1)):
#         letter = list1[i]
#         indeterminable = alphabets.index(letter) - shift1
#         indeterminable %= len(alphabets)
#         list1[i] = alphabets[indeterminable]
#     print(''.join(list1))

def ceasercipher(msg, shiftamount, encode_or_decode):
    list1 = list(msg)

    if encode_or_decode == 'decrypt':
        shiftamount *= -1
    for i in range(len(list1)):
        letter = list1[i]
        if letter not in alphabets:
            list1[i]=letter
        else:
            indeterminable = alphabets.index(letter) + shiftamount
            indeterminable %= len(alphabets)
            list1[i] = alphabets[indeterminable]
    print(''.join(list1))
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("hello to ceaser cipher...")
Runagain=True
while Runagain:
    wannacontinue = input("Do you want to cipher or decipher something type 'Y' or 'N' : ")
    if wannacontinue=='Y' or wannacontinue=='y' :
        choice = input("What do you want to encrypt or decrypt :").lower()
        message = input(f"Enter the message you want to {choice} : ")
        shiftkey = int(input("Enter the shift key : "))
        ceasercipher(message, shiftkey, encode_or_decode=choice)
    else:
        Runagain=False
print("Thank you..")
