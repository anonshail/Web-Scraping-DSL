#DSL v1.0
#Author: Shail K Shah
#Purpose of this file
#---------------------
#This file is responsible of reading the input from the script file and converting the commands into tokens

#the command line arguments are assumed to be the files that need to be executed
import sys

def main():
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
