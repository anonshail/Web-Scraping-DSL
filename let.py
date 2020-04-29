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

def main(tokList, lineNo):

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

    #error checking
    #if list name is a reserved keyword, throw error
    if varName in keywords:
        print("Error on line: " + str(lineNo) + " Variable name cannot be a keyword: " + varName)
        return -1

    varValue = tokList[tokList.index("equals") + 1]

    return [varName, varValue]