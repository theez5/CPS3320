import random
# Hangman game!
# Assume the answer is "hangman"

#randomly selects a word from the list
def getWord():
    words = ['hello', 'goodbye', 'testing', 'bourbon', 'apple']
    return random.choice(words)

#A = ['h','a','n','g','m','a','n']
#L = ['_','_','_','_','_','_','_']
A=[]
L= []
word = getWord()
dashCount = len(word)
pos = 0
for char in word:
    A.append(word[pos].upper())
    L.append('_')
    pos = pos + 1

play = True
maxGuess = 0
print(' '.join(str(n) for n in L))
while play == True:
#Ask the user to guess a letter
    letter = str(input("Guess a letter: "))
    if letter == ' ' or letter == '':
        print('You cannot give a blank letter, enter a letter.')
        continue

# Check to see if that letter is in the Answer
    i = 0
    x = 0
    for char in word:

        if letter == char:
            L[i] = letter.upper()
            x = 1
            #print(i)
            #print(letter)

# Display what the player has thus far (L) with a space
# separating each letter

        i = i + 1
# Test to see if the word has been successfully completed,
# and if so, end the loop
    if x == 1:
        print(' '.join(str(n) for n in L))
    else:
        print("Bad guess!")
        maxGuess = maxGuess + 1
    if A == L:
        play = False
        print("GREAT JOB!")
    if maxGuess > 5:
        play = False
        print("GAME OVER")