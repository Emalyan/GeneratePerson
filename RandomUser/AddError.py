import string
import random

def AddError(personData, errorCount, language):
    countElements = 2
    for i in range(0, int(errorCount)): 
        dataNumber = random.randint(0, countElements)
        data = personData[dataNumber]        
        replacedChar = random.randint(0, len(data))                        
        action = random.choice(actions)
        personData[dataNumber] = action(data, replacedChar)                        
    return personData
        
def ReplaceChar(data, index):
    return (data[:index] + randomChar() + data[index+1:])           

def DeleteChar(data, index):
    return (data[:index] + '' + data[index+1:])           

def AddChar(data, index):
    return (data[:index] + randomChar() + data[index:])           

actions = [AddChar, DeleteChar, ReplaceChar]

def randomChar(min_chars=1, max_chars=1, alphabet=string.ascii_lowercase):
    return ''.join(random.choices(alphabet, k=random.randint(1, 1)))
