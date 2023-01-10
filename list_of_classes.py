"""
• Write a program that asks for the names of all
the classes you are taking this semester
• Save these class names in a list
• How will you know when the last class has
been entered?
• Print all the items in the list, one per line

"""

classes = []
class_amount = int(input('How many classes are you taking? '))

for amount in range(class_amount):
  class_name = input(f'Enter the name for class {amount+1}: ')
  classes.append(class_name)

print('\nHere are your classes:')
for index, c in enumerate(classes):
  print(f'{index+1}: {c}')