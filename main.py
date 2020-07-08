    #WebScraping DSL v0.1
#Author: Shail K Shah
#Purpose of this file
#---------------------
#This file is responsible of reading the input from the script file and converting the commands into tokens

#the command line arguments are assumed to be the files that need to be executed
import sys
import os
import re
import get
import help
import view
import let
import list as listCmd
import mem

#initializing variables table
varTable = {}

#initializing lists table
listTable = {}

def preprocess(tokList, lineNo):
    #this function will take the token list, preprocess it for variables and lists

    if "from" not in tokList:   #from must be there, since there has to be a url
        print("Invalid syntax, no from found on line no: " + str(lineNo))
        return -1

    nameOfId = tokList[tokList.index('from')+1] #name of identifier (var or list)

    #if name of id is a valid url, then no preprocessing required, return same tokList
    if(nameOfId.startswith("http")):
        #valid url, return tokList as is
        return [tokList]
    
    #some preprocessing required

    #first check if nameOfId exists in varTable
    if nameOfId in varTable.keys():
        #replacing url with correct url value
        urlIndex = tokList.index('from')+1
        tokList[urlIndex] = varTable[nameOfId]
        return [tokList]

    #now check if nameOfId exists in listTable
    elif nameOfId in listTable.keys():
        #creating all possible lists

        tokLL = [] #tokListLists
        for url in listTable[nameOfId]:
            urlIndex = tokList.index('from')+1
            newList = tokList.copy()
            newList[urlIndex] = url
            tokLL.append(newList)
        
        return tokLL
    
    else:
        print("Unknown identifier: " + nameOfId + "on line number: " + str(lineNo))
        return -1 #error status


def callModule(tokList, lineNo):
    #this function will be incharge of analyzing the token list, and calling the relative call_module

    #incase the line is a comment, that is it starts with a hash, no processing needed
    if(tokList[0][0] == '#'):
        return

    #the command to execute will be the first word, hence, look up the commands
    command = tokList[0]

    #if else ladder of the commands
    if command == "get":
        tokListLists = preprocess(tokList, lineNo)

        if tokListLists == -1: #identifier not found
            return -1

        for tokenList in tokListLists:
            status = get.main(tokenList, lineNo)
            if(status == -1):
                return status
    
    
    elif command == "help":
        status = help.main(tokList, lineNo)
        return status


    elif command == "view":
        tokListLists = preprocess(tokList, lineNo)

        if tokListLists == -1: #identifier not found
            return -1

        for tokenList in tokListLists:
            status = view.main(tokenList, lineNo)
            if(status == -1):
                return status


    elif command == "let":
        status = let.main(tokList, lineNo, varTable, listTable)

        #if status is -1, error has occoured, or else, add variable to the table
        if status != -1:
            varTable[status[0]] = status[1]

        return status
    

    elif command == "list":
        status = listCmd.main(tokList, lineNo, varTable, listTable)

        #if status is -1, error has occoured, or else, add list to the table
        if status != -1:
            listTable[status[0]] = status[1]
        
        return status

    elif command == "freevar":
        #this block of code is to remove all the variables that user wants to delete

        varToDelete = tokList[1:]

        #error checking to ensure all the variables do infact exist
        flag=1
        for var in varToDelete:
            if var in varTable:
                continue
            else:
                print("Error on line " + str(lineNo) + " no variable: " + var + " found")
                flag=0

        if(flag==0):
            #if flag is 0, the command is incorrect
            return -1
        
        #now to go about and deleting all the variables from the varTable

        for var in varToDelete:
            del varTable[var]
    
    elif command == "freelist":
        #this block of code is to remove all the lists that the user wants to delete

        listsToDelete = tokList[1:]

        #error checking to ensure all the lists do infact exist
        flag=1
        for list_ in listsToDelete:
            if list_ in listTable:
                continue
            else:
                print("Error on line " + str(lineNo) + " no list: " + list_ + " found")
                flag=0

        if(flag==0):
            #if flag is 0, the command is incorrect
            return -1
        
        #now to go about and deleting all the variables from the varTable

        for list_ in listsToDelete:
            del listTable[list_]
    
    elif command == "mem":
        status = mem.main(tokList, lineNo, varTable, listTable)

        #if an error is there in the command
        if(status == -1):
            return status


    else:
        print("Unkown command: " + command + " on line no: " + str(lineNo))
        return -1

def main():
    #This is the main function, it is in charge of splitting tokens

    #if no arguments present
    if(len(sys.argv) <= 1):
        #Starting commmand line
        
        print("WEB SCRAPING DSL COMMAND LINE: ")
        print("Version: v1.4")
        print("Type 'exit' to exit the command line")
        
        
        #Starting infinite loop of commandline, will exit on 'exit' command
        while(True):
            print("> ", end="")
            command = input() #entering the command

            #if command is exit, break the loop
            if(command == 'exit' or command == 'Exit'):
                break

            #else execute the command
            status = callModule(command.split(), 1)
            
            # #if status is -1, error has occoured, so the execution is halted

            # if(status == -1): 
            #     break




    else:
        #Executing script(s)


        #WIP REMOVE TRY COMMENTS IN THE END WIP!!!
        # try:
        #Reading the files
        for file_name in sys.argv:
            if(file_name == "main.py"):
                continue

            file = open(file_name, "r")

            #reading the contents of current files
            lines = file.readlines()
            for i in range(len(lines)):
                lines[i] = lines[i].split()
                status = callModule(lines[i], i+1)

                if(status == -1):
                    break


            file.close()

        # except:
        #     print("Error in reading the file(s)")

main()
