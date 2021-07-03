#Secret Messages. New position

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
character = input('Please enter a character ')
position = alphabet.find(character)
print('Position of a character ', character, ' is ', position)
newPosition = position + key
print('New position of a character ', character, ' is ', newPosition)
