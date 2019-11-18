
from FakeData import *
import random

allData = {'ru_RU': [RUFirstNames, RULastNames, RUPhoneCodes, RUStreets, RUPatronitycs], 
           'by_BY': [BYFirstNames, BYLastNames, BYPhoneCodes, BYStreets, BYPatronitycs],
           'en_US': [USFirstNames, USLastNames, USPhoneCodes, USStreets]}        

def GeneratePerson(language):    
    data = allData[language]
    firstName = random.choice(data[0])
    lastName = random.choice(data[1])
    phoneNumber = GeneratePhoneNumber(data[2], language)
    adress = GenerateAdress(data[3], language)    
    fio = firstName + ' ' + lastName
    if language != 'en_US':        
        patronityc = random.choice(data[4])    
        fio += ' ' + patronityc            
    return [fio, phoneNumber, adress]     

def GeneratePhoneNumber(codes, language):    
    phoneCode = random.choice(codes)
    number = str(random.randint(1000000, 9999999))
    if language == 'by_BY':        
        return '+375' + phoneCode + number
    elif language == 'ru_RU':        
        return '8' + phoneCode + number
    else:
        return phoneCode + number

def GenerateAdress(streets, language):    
    street = random.choice(streets)
    houseNumber = str(random.randint(1, 100))
    if language != 'en_US':                
        houseNumber += random.choices(['', 'A', 'Б'], weights=[70, 15, 15])[0]        
        return street + ' ' + houseNumber
    else:
        return houseNumber + ' ' + street

    