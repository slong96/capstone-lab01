"""
Write a program that asks for your name and the
month you were born in.

Your program should print
- A greeting to you, using your name
- A message with the number of letters in your name
- A 'Happy birthday month!' message if you were born in January

Bonus question can you detect if the month entered
is the same as the current month, no matter when you
run the program?

"""

name = input('What is your name? ')
birth_month = input('What month were you born in? ')

print(f'Hello, {name}!')

if birth_month.lower().strip() == 'january':
  print('Happy birthday month!')

print(f'There are {len(name)} letters in your name.')