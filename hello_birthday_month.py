name = input('What is your name? ')
birth_month = input('What month were you born in? ')

print(f'Hello, {name}!')

if birth_month.lower() == 'january':
  print('Happy birthday month!')

print(f'There are {len(name)} letters in your name.')