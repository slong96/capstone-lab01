# Had to search the web for this one.
# This post explained it well and walked me through on how to do it.
# https://www.educative.io/answers/how-do-you-convert-a-string-to-camelcase-format

sentence = input('Enter a short sentence: ')

i = sentence.title().replace(' ', '')

print(''.join( [ i[0].lower(), i[1:] ] ))