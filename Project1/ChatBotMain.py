#this program intends to assist students via a chatbot by referencing them with different resources for different subject areas

#importing the nltk library and associated functions
import sys

from nltk.chat.util import Chat, reflections

pairs = [
    #key value pairs to allow the chatbot to match custom inputs to desired outputs for the user
    ['(hi|hello|greetings|salutations)' , ['Hello friend!']],
    ['What is your name?', ['My name is Chatterboy, and yours?']],
    ['My name is (.*)' , ['Hi %1, nice to meet you!']],
    ['(.*)question(.*)', ['Ask away!']],
    ['(.*)math(.*)', ['Here is a good resource for Math questions: https://www.homeschoolmath.net/online/problem_solving.php']],
    ['(.*)science(.*)', ['Here is a good resource for Science questions: https://www.sciencebuddies.org/science-fair-projects/ask-an-expert-intro']],
    ['(.*)psychology(.*)', ['Here is a good resource for Psychology questions: https://www.apa.org/']],
    ['(.*)programming(.*)', ['Here is a good resource for comspci questions: https://www.w3schools.com/']],
    ['(quit|goodbye|thank you|farewell|done)' , ['Goodbye, feel free to ask more questions!']]

]
#welcome message
print("Welcome to Chatterboy, a chatbot that is here to help you with your studying needs! Try starting out by saying hi!")
chat = Chat(pairs, reflections)
chat.converse()

#if pairs[['(quit|goodbye|thank you|farewell)' , ['Goodbye, feel free to ask more questions!']]
#] == 'goodbye':
#   exit()
