"""
Sonya Cao
COMPSCI 1026
BAUER
12/04/19
Country Catalogue program: stores a data structure that contains country objects
"""
from Country import Country
class CountryCatalogue:
    def __init__(self, countryFile): #creates objects of the country catalogue class
        self._countryCat = [] #instance variable for the list storing country objects
        data = open(countryFile, "r")
        data.readline()
        line = data.readline()

        try:
            while line != "": #looping through the entire data file
                line = line.strip()
                if line == "/n": #skips the line if it is blank
                    line = data.readline()
                line = self.correctFormat(line)
                cinfo = line.split("|") #seperating the information about the country
                self._countryCat.append(Country(cinfo[0], cinfo[2], cinfo[3], cinfo[1])) #creating a country object and adding it to the instance variable countryCat
                line = data.readline()
        except ValueError: #handles the error of an unreadable file
            print("Error: Country file in the incorrect format")
            outputFile = open("output.txt", "w")
            outputFile.write("Update Unsuccessful\n")
            outputFile.close()
        except IndexError: #handles the error of an unreadable file
            print("Error: Country file in the incorrect format")
            outputFile = open("output.txt", "w")
            outputFile.write("Update Unsuccessful\n")
            outputFile.close()
        except RuntimeError as error: #handles the error of the program crashing for any reason
            print("Error: ", str(error))
        except:
            print("An issue has occurred! The program will now exit!")
            return False

    def setPopulationOfCountry (self, country, newPop):
        if self.findCountry(country) != None: #if the country exists, the population will be changed
            self._countryCat.remove(self.findCountry(country)) #removes the original country object from the list
            country.setPopulation(newPop) #changes the population instance variable of the country object
            self._countryCat.append(country) #adds the new country object to the list
        else:
            print("country does not exist")

    def setAreaOfCountry(self, country, newArea):
        if self.findCountry(country) != None: #if the country exists, the area will be changed
            self._countryCat.remove(self.findCountry(country)) #removes the original country object from the list
            country.setArea(newArea) #changes the area instance variable of the country object
            self._countryCat.append(country) #adds the new country object to the list

    def setContinentOfCountry(self, country, newCont):
        if self.findCountry(country) != None: #if the country exists, the continent will be changed
            self._countryCat.remove(self.findCountry(country)) #removes the original country object from the list
            country.setContinent(newCont) #changes the continent instance variable of the country object
            self._countryCat.append(country) #adds the new country object to the list

    def findCountry(self, country):
        for element in self._countryCat: #loops through the country objects in the list and if the country matches with an element in the list will return the country object
            if element._name == country._name and element._pop == country._pop and element._area == country._area and element._continent == country._continent:
                country = element
                return country
        return None #returns None if the country does not match any elements in the list

    def addCountry(self, countryName, pop, area, cont):
        newCountry = Country(countryName, pop, area, cont) #creates a new country object with the given information
        if self.findCountry(newCountry) == None: #if the new country object does not exist within the list, the country object is added and the method returns True
            self._countryCat.append(Country(countryName, pop, area, cont))
            return True
        else:
            return False #if the country object already exists within the list, False is returned

    def printCountryCatalogue(self):
        if self == False: #if there are no countries in the list, an empty string is returned
            return ""

        self._countryCat.sort(key=lambda x: x._name) #the country catalogue (list of country objects) is sorted alphabetically based on the name of the country

        for country in self._countryCat: #prints every country object in the list
            print(country.__repr__())

    def saveCountryCatalogue(self, fname):
        self._countryCat.sort(key=lambda x: x._name) #sorts the country catalogue alphabetically by country name
        total = 0
        outputFile = open(fname, "w")
        outputFile.write("Country|Continent|Population|Area\n")
        for country in self._countryCat:
            outputFile.write(country.originalFormat()+"\n") #writes the countries and their corresponding data to an output file
            total += 1
        if total > 0: #returns the total amount of countries returned
            return total
        else:
            return -1

    def correctFormat(self, line):
        total = 0
        for i in range (0, len(line)): #counts how many vertical bars are in the line
            if line[i] == "|":
                total +=1

        if total == 0: #if the data file is missing vertical bars, they are added to the end
            return line + "|||"
        elif total == 1:
            return line + "||"
        elif total == 2:
            return line + "|"
        else:
            return line
