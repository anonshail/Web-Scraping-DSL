#List command in web scraping dsl
#This file is for creating lists, and it will return a name/list pair to get

#Synatx: list listName equals URL1 URL2 URL3

keywords = [
    'let',
    'list',
    'freevar',
    'freelist',
    'mem',
    'verbose',
    'get',
    'view',
    'help',
    'images',
    'text',
    'audios',
    'videos',
    'all',
    'from',
    'urls',
    'id',
    'write',
    'class',
    'store',
    'file',
    'vars'
]

def doesExist(listName, varTable, listTable):
    #The purpose of this function is to ensure that the list name does not already exist
    #If it does, it returns 1
    #Else it returns 0

    #checking if the list name is there in the variableTable
    if listName in varTable:
        return 1

    #checking if the list name is there in the listTale
    if listName in listTable:
        return 1

    #all ok, return 0
    else:
        return 0
    
def startsWithHttp(listName):
    #The purpose of this function is to ensure that the list name does not start with http
    #listName cannot start with http, or else the code will break

    #If incorrect variable is used, it should return 0
    if listName.startswith('http'):
        return 1

    #All okay, return 0
    else:
        return 0

def main(tokList, lineNo, varTable, listTable):

    #check if tokList has equals, if not throw error
    if('equals' not in tokList):
        print("Invalid syntax, no equals found on line no: " + str(lineNo))
        return -1

    
    #error checking, making sure that all the parameters are correct
    for i in range(len(tokList)):
        if tokList[i] == 'list':
            continue
        elif tokList[i+1] == 'equals':
            continue
        elif tokList[i][0] == '#' or tokList[i] == 'equals':  #skip the remaining, since it's a comment or urls
            break
        else:
            print("Incorrect token: " + tokList[i] + " on line no: " + str(lineNo) + ". Execute help for information.")
            return -1

    #creating name/value pair
    listName = tokList[tokList.index("equals") - 1]

    #Further error checking

    #Checking to ensure that the variable name does not already exist
    if doesExist(listName, varTable, listTable) == 1:
        #Error has occoured

        print("List name: " + listName + " already exists. Error on line: " + str(lineNo))
        return -1

    #Checking to ensure variable name does not start with http
    if startsWithHttp(listName) == 1:
        #Error has occoured

        print("Incorrect list name: " + listName + ". It cannot start with https. Error on line: " + str(lineNo))
        return -1 

    #error checking
    #if list name is a reserved keyword, throw error
    if listName in keywords:
        print("Error on line: " + str(lineNo) + " List name cannot be a keyword: " + listName)
        return -1

    listValues = tokList[tokList.index("equals") + 1 : ] # contains all url values

    #trimming the listValues of comment tokens
    for token in listValues:
        if token[0] == '#':
            commentBeginIndex = listValues.index(token)
            listValues = listValues[:commentBeginIndex]
            break

    return [listName, listValues]
