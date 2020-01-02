"""
Sonya Cao
COMPSCI 1026
BAUER
12/04/19
Country program: stores information about a single country
"""
class Country:
    def __init__(self, name, pop, area, continent): #creating the Country object with the instance variables name, population, area and continent
        self._name = name
        self._pop = pop
        self._area = area
        self._continent = continent


    def getName(self): #getter method for name of country
        return self._name


    def getPopulation(self): #getter method for population of country
        return self._pop


    def setPopulation(self, newPop): #setter method to change/set population of country
        self._pop = newPop


    def setArea(self, newArea): #setter method to change/set area of country
        self._area = newArea


    def getArea(self): #getter method for area of country
        return self._area


    def setContinent(self, newContinent): #setter method to change/set continent of country
        self._continent = newContinent


    def getContinent(self): #getter method for continent of country
        return self._pop


    def __repr__(self): #generates a string representation for class objects
        return str(self._name) + "(pop: " + str(self._pop) + ", size: " + str(self._area) + ") in " + str(self._continent)


    def originalFormat(self): #returns the data of the country in the format it was originally in the data file
        str =""
        if self._name != "":
            str += self._name.strip() +"|"
        else:
            str += "|"
        if self._continent != "":
            str += self._continent.strip() +"|"
        else:
            str += "|"
        if self._pop != "":
            str += self._pop.strip() +"|"
        else:
            str += "|"
        if self._area != "":
            str += self._area.strip()

        return str
