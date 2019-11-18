import sys
from ShowData import *
from decimal import Decimal

language = sys.argv[1]
personCount = int(sys.argv[2])
errorCount = Decimal(sys.argv[3])

if errorCount == 0:
    ShowPersonsWithoutError(personCount, language)                      
elif errorCount < 1:
    ShowPersonsWithErrorInSome(personCount, errorCount, language)                       
else:
    ShowPersonsWithErrorInEach(personCount, errorCount, language)        

