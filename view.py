#View command in Web Scrapping DSL
#The purpose of this command is to get details of the particular url, and display it to the user
#Similar to "ls" command in shell

from bs4 import BeautifulSoup
import scrapy
import requests

def main(tokList, lineNo):
    #assume the url is stored in the last token

    html_doc = requests.get(tokList[-1])
    soup = BeautifulSoup(html_doc.content, 'html.parser')

    #if else ladder of all the view options
    if(tokList[1] == "text"):
        #display all the text of the page on the terminal
        print(soup.get_text())

    else:
        print("Unkown parameter: " + tokList[1] + " on line no: " + lineNo)
