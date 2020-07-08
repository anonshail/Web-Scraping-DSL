#Let command in web scraping DSL
#This file is for creating of Variables and returning the name/value pair to main for storage in local variables table

#Synatx: let varName equals URL

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

def doesExist(varName, varTable, listTable):
    #The purpose of this function is to ensure that the variable name does not already exist
    #If it does, it returns 1
    #Else it returns 0

    #checking if the variable name is there in the variableTable
    if varName in varTable:
        return 1

    #checking if the variable name is there in the listTale
    if varName in listTable:
        return 1

    #all ok, return 0
    else:
        return 0
    
def startsWithHttp(varName):
    #The purpose of this function is to ensure that the vairable name does not start with http
    #varName cannot start with http, or else the code will break

    #If incorrect variable is used, it should return 0
    if varName.startswith("http"):
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
        if tokList[i] == 'let' or tokList[i] == 'equals':
            continue
        elif tokList[i-1] == 'equals' or tokList[i+1] == 'equals':
            continue
        elif tokList[i][0] == '#':  #skip the remaining, since it's a comment
            break
        else:
            print("Incorrect token: " + tokList[i] + " on line no: " + str(lineNo) + ". Execute help for information.")
            return -1
    

    #creating name/value pair
    varName = tokList[tokList.index("equals") - 1]

    #Further error checking

    #Checking to ensure that the variable name does not already exist
    if doesExist(varName, varTable, listTable) == 1:
        #Error has occoured

        print("Variable name: " + varName + " already exists. Error on line: " + str(lineNo))
        return -1

    #Checking to ensure variable name does not start with http
    if startsWithHttp(varName) == 1:
        #Error has occoured
        print("Incorrect variable name: " + varName + ". It cannot start with https. Error on line: " + str(lineNo))
        return -1              
                 

    #error checking
    #if list name is a reserved keyword, throw error
    if varName in keywords:
        print("Error on line: " + str(lineNo) + " Variable name cannot be a keyword: " + varName)
        return -1

    varValue = tokList[tokList.index("equals") + 1]

    return [varName, varValue]
