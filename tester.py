from Country import Country
from CountryCatalogue import CountryCatalogue
from processUpdates import processUpdates


catalogue1 = CountryCatalogue("data2.txt")
CountryCatalogue.printCountryCatalogue(catalogue1)
print(CountryCatalogue.saveCountryCatalogue(catalogue1,"test1"))
processUpdates("data23.txt", "upd.txt")
#do we assume data is in right format, right order?
#exceptions
