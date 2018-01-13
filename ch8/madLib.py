#Read madLibText.txt and show corresponding prompt and let user enter word.
#Replace corresponding word in the text and save the result.

with open('madLibText.txt') as source:
    text = source.read()

while 'ADJECTIVE' in text:
    adj = input('Enter an adjective. ')
    text = text.replace('ADJECTIVE', adj, 1)
    
while 'NOUN' in text:
    noun = input('Enter a noun. ')
    text = text.replace('NOUN', noun, 1)
    
while 'VERB' in text:
    verb = input('Enter a verb. ')
    text = text.replace('VERB', verb, 1)
    
print(text)

with open('madLibResult.txt', 'w') as result:
    result.write(text)
