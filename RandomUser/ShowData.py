from AddError import AddError
from GeneratePerson import GeneratePerson

def CreatePersonWithError(errorCount, language):
    generatedPerson = GeneratePerson(language)
    return AddError(generatedPerson, errorCount, language)

def ShowPersonsWithErrorInSome(personCount, errorChance, language):                
    errorCount = 1    
    personCountWithError = int(personCount) * errorChance
    for i in range(0, personCount):                                                         
        if i > personCountWithError:
            person = GeneratePerson(language)                            
            print(*person, sep="; ")                
        else:
            person = CreatePersonWithError(errorCount, language)                          
            print(*person, sep="; ")            
                        
def ShowPersonsWithErrorInEach(personCount, errorCount, language):
    errorCount = int(errorCount)
    for i in range(0, personCount):  
        person = CreatePersonWithError(errorCount, language)            
        print(*person, sep="; ")

def ShowPersonsWithoutError(personCount, language):
    for i in range(0, personCount):
        person = GeneratePerson(language)        
        print(*person, sep="; ")
