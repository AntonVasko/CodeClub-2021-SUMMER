#Secret Messages. Decrypt message

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = int(input('Please input key '))
decMessage = ''

message = (input('Please enter a message: '))

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    #print('Position of a character ', character, ' is ', position)
    newPosition = (position - key) % 26
    #print('New position of a character ', character, ' is ', newPosition)
    newCharacter = alphabet[newPosition]
    #print('New character of a new position of ', newPosition, ' is ', newCharacter)
    decMessage += newCharacter
  else:
    decMessage += character
  
print('Your decrypt message of your ', message, ' is ', decMessage)
