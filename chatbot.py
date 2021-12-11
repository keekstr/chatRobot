# a readable note
# Print introduction to the chatbot
# Get name from user
# Print hello name
    # chatbot introduction
print('Hello! I am Zygo 64. I am a chatbot')
print('I Like animals and I love to talk about food')
name = input('What is your name?: ')
print('Hello' , name, ', Nice to meet you')
# Get current year from user
# Get chatbot age from user
# Print guess is correct
# Convert chatbot age to integer
# Set years to 100 - chatbot age
# Print I will be 100 in years
# Convert current year to integers
# Print That will be current year + years
     # get year inormation
year = input('I am not very good at dates. What is the year?: ')
print('Yes, I think that is correct. Thanks! ')
    # ask user to guess age
myage = input('Can you guess my age? - enter a number: ')
print('Yes you are right. I am ', myage)
    # do math to calculate when chatbot will be 100
myage = int(myage)
nyears = 100 - myage
print('I will be 100 in', nyears, 'years')
print('That will be the year', int(year) +
nyears)
    # food conversation
print('I love ramen and I also like trying out new kinds of food')
food = input('How about you? What is your favorite food?: ')
print('I like', food, 'too.')
question = 'How often do you eat ' + food + '?: '
howoften = input(question)
print('Interesting. I wonder if that is good for your health')
    # animal conversation
animal = input('My favorite animal is a tiger. What is yours?: ')
print(animal,'! I do not like them.')
print('I wonder if a', animal, 'likes to eat', food,'?')
    # a conversation about feelings
feeling = input('How are you feeling today?: ')
print('Why are you feeling', feeling, 'now?')
reason = input('Please tell me: ')
print('I understand. Thanks for sharing')
    # goodbye
print('It has been a long day')
print('I have some bitcoin to mine. We can chat again tomorrow.')
print('Goodbye', name, 'I liked chatting with you')
