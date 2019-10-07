#WebScraping DSL v0.1
#Author: Shail K Shah
#Purpose of this file
#---------------------
#This file is responsible of reading the input from the script file and converting the commands into tokens

#the command line arguments are assumed to be the files that need to be executed
import sys
import os
import re

def call_module(tok_list):
    #this function will be incharge of analyzing the token list, and calling the relative call_module

    #incase the line is a comment, that is it starts with a hash, no processing needed
    if(tok_list[0][0] == '#'):
        return

    #the command to execute will be the first word, hence, look up the commands
    command = tok_list[0]

    #if else ladder of the commands
    if true:
        #do stuff
        x=1

    else:
        print("Unkown command: " + command)
        return

def main():
    #This is the main function, it is in charge of splitting tokens

    #if no arguments present
    if(len(sys.argv) <= 1):
        print("Please enter the location of the script to execute")

    else:
        try:
            #Reading the files
            for file_name in sys.argv:

                if(file_name == "main.py"):
                    continue

                file = open(file_name, "r")

                #reading the contents of current files
                lines = file.readlines();
                for i in range(len(lines)):
                    lines[i] = lines[i].split()

                #do stuff with readlines
                print(lines)

                file.close()

        except:
            print("Error in reading the file(s)")

main()
