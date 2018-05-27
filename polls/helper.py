import csv
import matplotlib.pyplot as plt
from sortedcontainers import SortedList, SortedDict, SortedSet


# function to read the csv file and return the dict reader object


def dictFileReader(file):
    return csv.DictReader(open(file, newline=''), delimiter=',', quotechar='|')




#id of matches which played in x year
def idOfMatch(year,matchReader):
    idOfMatchInYear=SortedSet() 
    #initializationn of id list
    for match in matchReader:
        if int(match['season'])==int(year):
            idOfMatchInYear.add(int(match['id']))
    return idOfMatchInYear

    