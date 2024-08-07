#hangman game
import random
import stagesofhangman
import words
import hangmanlogo
print(hangmanlogo.logo)
word = random.choice(words.randomwords)
print("Fill up the empty spaces by guessing the correct letters...")
lengthofword = len(word)
lives = 6
guesser = []
index = 0
result = False
for letter in range(lengthofword):
    guesser.append('_')
print(''.join(guesser))
while not result:
    letterguess = input("Enter a letter of the word : ").lower()
    if letterguess in guesser:
        print(f"\nYou already guessed that letter '{letterguess}'")
    for position in range(lengthofword):
        if word[position] == letterguess:
            guesser[position] = word[position]
    print(''.join(guesser))
    if letterguess not in word:
        lives-=1
        print(f"\nIt does not have letter '{letterguess}',You lost a life.....")
        print(f"\nTotal lives remaining out of 6 are : {lives}")
        if lives==0:
           result=True
           print("\nYou Lost................................"
                 f"\nThe correct word was {word}")

    if "_" not in guesser:
        result = True
        print("\nYou Won.................................")
    print(stagesofhangman.stages[lives])
print("\nThank You...")