#get command in Web Scrapping DSL
#The purpose of this command is to get details of the particular url, and display it to the user
#Similar to "ls" command in shell



# View Options:
# 1. View Text
# 2. View Images
# 3. View Urls
# 4. View Videos
# 5. View Files
# 6. View Id
# 7. View Class



#modules to be imported
from bs4 import BeautifulSoup
import scrapy
import requests
import sys
import shutil
import re
import os.path
import os




def main(tokList, lineNo):
    #view immplementation WIP!

    if "from" not in tokList:   #from must be there, since there has to be a url
        print("Invalid syntax, no from found on line no: " + str(lineNo))
        return -1
    
    
    #obtaining that url and creating soup
    urlIndex = tokList.index("from") + 1
    html_doc = requests.get(tokList[urlIndex])
    soup = BeautifulSoup(html_doc.content, 'html.parser')


    #if else ladder of all the get options

    
    #FOR TEXT
    if(tokList[1] == 'text'):
        #error checking, making sure that all the parameters are correct
        for i in range(len(tokList)):
            if tokList[i] == 'view' or tokList[i] == 'text' or tokList[i] == 'write' or tokList[i] == 'from':
                continue
            elif tokList[i-1] == 'write' or tokList[i-1] == 'from':
                continue
            elif tokList[i][0] == '#':  #skip the remaining, since it's a comment
                break
            else:
                print("Incorrect token: " + tokList[i] + " on line no: " + str(lineNo) + ". Execute help for information.")
                return -1


        #obtaining data, and calculating varios metrics
        contents = soup.get_text() #conatians the contents of what the user wnats
        stringContent = str(contents) #contains string of all the information
        lengthOfText = len(stringContent) #length of the text
        noOfWords = len(stringContent.split()) #number of words


        #Final Report String
        reportString = "The responce contains " + str(noOfWords) +" word(s) and " + str(lengthOfText) + " character(s)" 


        #now, either display the report string on the terminal, or write it into a text file
        #if the 'write' keyword is present


        if  "write" in tokList:
            #write contents into the file after write keyword
            fileName = tokList[tokList.index("write") + 1]
            file = open(fileName, "a")
            file.write(reportString)
            file.close()
            
        else:
            #display all the text of the page on the terminal
            print(reportString)