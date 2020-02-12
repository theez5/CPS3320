#this program is based off of the popular game Scrabble and contains two functions:
#letterScore, which allows a user to determine the point value of a letter
#wordScore, which allows a user to determine the point value of a word

letters = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,'J':8,'K':5,
           'L':1,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1,'S':1,'T':1,'U':1,'V':4,'W':4,
           'X':8,'Y':4,'Z':10}
letterscor = str(input("Enter a letter, A-Z: ")) #need to convert input to uppercase if user enters lowercase letter

def letterScore(letterscor):
    letterscor = letterscor.upper()
    if letterscor in letters:
        return (letters[letterscor])
    else:
        return  (0)
print("The point value of the letter ",letterscor," is: ")
print (letterScore(letterscor))
#the function below calculates the point amount of the word the user enters
word = str(input("Enter a word: "))
def wordScore(word):
    i = 0
    for char in word:
        i = i + letterScore(char)
    return i
print("Your word ",word, " contains this many points: ")
print(wordScore(word))
