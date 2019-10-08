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

def callModule(tokList, lineNo):
    #this function will be incharge of analyzing the token list, and calling the relative call_module

    #incase the line is a comment, that is it starts with a hash, no processing needed
    if(tokList[0][0] == '#'):
        return

    #the command to execute will be the first word, hence, look up the commands
    command = tokList[0]

    #if else ladder of the commands
    if command == "get":
        #get command is used to get the details of the page
        get.main(tokList, lineNo)

    else:
        print("Unkown command: " + command + " on line no: " + lineNo)
        return

def main():
    #This is the main function, it is in charge of splitting tokens

    #if no arguments present
    if(len(sys.argv) <= 1):
        print("Please enter the location of the script to execute")

    else:
        # try:
        #Reading the files
        for file_name in sys.argv:
            if(file_name == "main.py"):
                continue

            file = open(file_name, "r")

            #reading the contents of current files
            lines = file.readlines();
            for i in range(len(lines)):
                lines[i] = lines[i].split()
                callModule(lines[i], i+1)

            file.close()

        # except:
        #     print("Error in reading the file(s)")

main()
