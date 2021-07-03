#Secret Messages. New with if and new character

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = int(input('Please input key '))
newMessage = ''

message = (input('Please enter a message: '))

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    #print('Position of a character ', character, ' is ', position)
    newPosition = (position + key) % 26
    #print('New position of a character ', character, ' is ', newPosition)
    newCharacter = alphabet[newPosition]
    #print('New character of a new position of ', newPosition, ' is ', newCharacter)
    newMessage += newCharacter
  else:
    newMessage += character
  
print('New message is ', newMessage)
