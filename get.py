#get command in Web Scrapping DSL
#The purpose of this command is to get details of the particular url, and display it to the user
#Similar to "ls" command in shell

from bs4 import BeautifulSoup
import scrapy
import requests

def main(tokList, lineNo):

    if "from" not in tokList:
        print("Invalid syntax, no from found on line no: " + str(lineNo))
        return -1

    #url comes after from keyword
    urlIndex = tokList.index("from") + 1

    html_doc = requests.get(tokList[urlIndex])
    soup = BeautifulSoup(html_doc.content, 'html.parser')

    #if else ladder of all the get options
    if(tokList[1] == "text"):

	#error checking should happen here! check all the parameters and make sure that they are valid! WIP

        contents = soup.get_text() #conatians the contents of what the user wnats
        #check for "write" to write into file
        if  "write" in tokList:
            #write contents into the file after write keyword
            fileName = tokList[tokList.index("write") + 1]
            file = open(fileName, "a")
            file.write(contents)
            file.close()
            
        else:
            #display all the text of the page on the terminal
            print(contents)

    else:
        print("Unkown parameter: " + tokList[1] + " on line no: " + str(lineNo))
        return -1