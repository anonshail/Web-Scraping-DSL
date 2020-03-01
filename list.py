#List command in web scraping dsl
#This file is for creating lists, and it will return a name/list pair to get

#Synatx: list listName equals URL1 URL2 URL3

def main(tokList, lineNo):

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
    listValues = tokList[tokList.index("equals") + 1 : ] # contains all url values

    #trimming the listValues of comment tokens
    for token in listValues:
        if token[0] == '#':
            commentBeginIndex = listValues.index(token)
            listValues = listValues[:commentBeginIndex]
            break

    return [listName, listValues]