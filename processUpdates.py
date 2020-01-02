"""
Sonya Cao
COMPSCI 1026
BAUER
12/04/19
Process Updates program: uses the information from an update file to change the information of specified countries in the country catalogue
"""

from CountryCatalogue import CountryCatalogue
from Country import Country

def processUpdates(cntryFileName, updateFileName):
    cExists = False
    while cExists == False: #will continue to prompt user for name of data file until it exists or they choose to quit
        try:
            countriesFile = open(cntryFileName, "r")
            cExists = True
        except IOError:
            answer = input("Country file does not exist. Do you want to quit? (Y or N)")
            if answer == "Y":
                countriesFile.close()
                return False
            else:
                cntryFileName = input("Enter the countries file name")
        except:
            print("An issue has occurred! The program will now exit!")
            return False

    cat = CountryCatalogue(cntryFileName) #creates a country catalogue object using the data file
    countriesFile.close()

    uExists = False
    while uExists == False: #will continue to prompt user for name of updates file until it exists or they choose t
        try:
            updates = open(updateFileName, "r")
            uExists = True
        except IOError:
            answer = input("Updates file does not exist. Do you want to quit? (Y or N)")
            if answer == "Y":
                outputFile = open("output.txt", "w")
                outputFile.write("Update Unsuccessful\n")
                countriesFile.close()
                return False
            else:
                updateFileName = input("Enter the update file name")
        except:
            print("An issue has occurred! The program will now exit!")
            return False

    line = updates.readline()

    while line != "": #loops through the entire updates file
        countryExists = False
        updateFields = line.split(";") #seperates the information in the update file
        updateName = updateFields[0].strip()

        for element in cat._countryCat: #if the country in the update file does not exist, a new country object is created
            if element._name == updateName:
                updateCountry = cat.findCountry(element)
                countryExists = True
        if countryExists == False:
            cat.addCountry(updateName,"","","")
            updateCountry = cat.findCountry(Country(updateName,"","",""))

        for i in range(1, len(updateFields)):
            if updateType(updateFields[i]) == 'P':
                update = updateFields[i].strip()
                update = update.strip("P=")
                cat.setPopulationOfCountry(updateCountry, update) #updates the population of the country
            elif updateType(updateFields[i]) == 'A':
                update = updateFields[i].strip()
                update = update.strip("A=")
                cat.setAreaOfCountry(updateCountry, update)  #updates the area of the country
            elif updateType(updateFields[i]) == 'C':
                update = updateFields[i].strip()
                update = update.strip("C=")
                cat.setContinentOfCountry(updateCountry, update)  #updates the continent of the country
            elif updateType(updateFields[i])== None: #if the file is in the wrong format will open an output fil that just has Update Unsuccessful
                outputFile = open("output.txt", "w")
                outputFile.write("Update Unsuccessful\n")
                return False

            if i == 3: #if there are more than 3 updates, stop at the third one
                break

        line = updates.readline()

    updates.close()
    CountryCatalogue.saveCountryCatalogue(cat, "output.txt") #writes the updated country catalogue to an output file
    return True


def updateType(updateFields): #returns P, A or C depending on what information is being updated

    updateFields = updateFields.strip(" ")
    try:
        if updateFields[1] == '=':
            if updateFields[0] == 'P':
                return 'P'
            elif updateFields[0] == 'A':
                return 'A'
            elif updateFields[0] == 'C':
                return 'C'
        else:
            print("Error: update file in wrong format")
    except IndexError: #Exception for when the update file is in the wrong format
        print("Error: update file in wrong format")
        return None
    except:
        print("An issue has occurred! The program will now exit!")
        return False
