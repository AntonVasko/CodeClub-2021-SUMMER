#Secret Messages. New character

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = int(input('Please input key '))
character = input('Please enter a character ')
position = alphabet.find(character)
print('Position of a character ', character, ' is ', position)
newPosition = (position + key) % 26
print('New position of a character ', character, ' is ', newPosition)
newCharacter = alphabet[newPosition]
print('New character of a new position of ', newPosition, ' is ', newCharacter)
