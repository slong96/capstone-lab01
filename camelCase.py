"""
Write a program that turns a sentence into camel case. 
The first word is lowercase, the rest of the words have their initial letter 
capitalized, and all of the words are joined together. 
For example, with the input "fOnt proCESSOR and ParsER", 
your program will output "fontProcessorAndParser". 

Optional extra question: 
print a warning message if the input will not produce a valid variable name. 
You don't need to be exhaustive in checking, but test for a few common issues, 
such as starting with a number, or containing invalid characters such as 
# or + or ".  Or, would it be easier to check that the name only contains 
# valid characters?
"""

# Had to search the web for this one.
# This post explained it well and walked me through on how to do it.
# https://www.educative.io/answers/how-do-you-convert-a-string-to-camelcase-format


def banner():
  """ Display program name """
  message = "Awesome camel case program!!"
  stars = '*' * len(message)
  print(f'\n{stars}\n{message} \n{stars}\n')

def main():
  banner()
  sentence = input('Enter a short sentence: ')
  i = sentence.title().replace(' ', '')
  print(''.join( [ i[0].lower(), i[1:] ] ))

main()