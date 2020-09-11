#Exercise 1

animal = 'dog'
vegetable = 'carrot'
mineral = 'salt'

print('Here is an animal, a vegetable, and a mineral.')
print(animal)
print(vegetable)
print(mineral)


#Exercise 2

name = input('What is your name? ')
print('You entered: ', name)


#Exercise 3

cat_speak = input('What does a cat say? ')
speech_length = len(cat_speak)

print('   {}'.format('_' * speech_length))
print(' < {}! > ' .format(cat_speak))
print('   {}'.format('-' * speech_length))

print('{0:>9}'.format('/'))
print(' /\_/\ ''{0:1}'.format('/'))
print('( o.o )')
print(' > ^ < ')
