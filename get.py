#get command in Web Scrapping DSL

from bs4 import BeautifulSoup
import scrapy
import requests
import sys
import shutil
import re
import os.path
import os

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
        #cases for text scraping

        #error checking, making sure that all the parameters are correct
        for i in range(len(tokList)):
            if tokList[i] == 'get' or tokList[i] == 'text' or tokList[i] == 'write' or tokList[i] == 'from':
                continue
            elif tokList[i-1] == 'write' or tokList[i-1] == 'from':
                continue
            else:
                print("Incorrect token: " + tokList[i] + " on line no: " + str(lineNo) + ". Execute help for information.")
                return -1   

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

    elif(tokList[1]=="images"):
        #case for images
        storeFlag = False
        storeLocation = ''   #location to store images into, if storeFlat is set to true
        

        #error checking, making sure that all the parameters are correct
        for i in range(len(tokList)):
            if tokList[i] == 'get' or tokList[i] == 'images' or tokList[i] == 'from' or tokList[i] == 'store':
                continue
            elif tokList[i-1] == 'images' or tokList[i-1] == 'from':
                continue
            elif tokList[i-1] == 'store':   #if you want to store into a folder
                storeFlag = True            #enabling store
                storeLocation = tokList[i]   #location to store is set

                #check if storeLocation exists, or else create it
                if(os.path.exists(storeLocation)==False):
                    os.mkdir(storeLocation)


            else:
                print("Incorrect token: " + tokList[i] + " on line no: " + str(lineNo) + ". Execute help for information.")
                return -1

        #check which images to get, i.e., all or some specific images
        #here, tokList[2] must contain all, or a particular image to download

        if(tokList[2] == 'all'):
            #download all images
            img_tags = soup.find_all('img')
            urls = [img['src'] for img in img_tags]

            for url in urls:
                #filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
                filename = url.split('/')[-1].split('#')[0].split('?')[0]
                with open(storeLocation+filename, 'wb') as f:
                    if 'http' not in url:
                        # sometimes an image source can be relative 
                        # if it is provide the base url which also happens 
                        # to be the site variable atm. 
                        url = '{}{}'.format(tokList[urlIndex], url)
                    response = requests.get(url)
                    f.write(response.content)

        else:
            #download a particular image
            if(tokList[2]=='from'):
                #no image has been mentioned, hence, throw error, while checking for store
                print("No image mentioned on line no: " + str(lineNo) + ". Execute help for information.")
                return -1
            
            #now, download image stored in tokList[2] or throw an error, while checking for store
            urlOfFile = tokList[2]
            filename = urlOfFile.split('/')[-1].split('#')[0].split('?')[0]
            with open(storeLocation+filename, 'wb') as f:
                if 'http' not in urlOfFile:
                    # sometimes an image source can be relative 
                    # if it is provide the base urlOfFile which also happens 
                    # to be the site variable atm. 
                    urlOfFile = '{}{}'.format(tokList[urlIndex], urlOfFile)
                response = requests.get(urlOfFile)
                f.write(response.content)

    elif(tokList[1] == 'urls'):
        #error checking, making sure that all the parameters are correct
        for i in range(len(tokList)):
            if tokList[i] == 'get' or tokList[i] == 'urls' or tokList[i] == 'write' or tokList[i] == 'from':
                continue
            elif tokList[i-1] == 'write' or tokList[i-1] == 'from':
                continue
            else:
                print("Incorrect token: " + tokList[i] + " on line no: " + str(lineNo) + ". Execute help for information.")
                return -1
        
        #either print the links, or write it to a file, if write is present
        if  "write" in tokList:
            #write contents into the file after write keyword
            fileName = tokList[tokList.index("write") + 1]
            file = open(fileName, "a")
            curLink=""
            for link in soup.find_all('a', href=True):
                if(link.get('href').startswith('http')):
                    curLink=link.get('href')
                file.write(curLink+"\n")               
            file.close()
            
        else:
            #display all the text of the page on the terminal
            curLink=""
            for link in soup.find_all('a', href=True):
                if(link.get('href').startswith('http')):
                    curLink=link.get('href')
                print(curLink)



    else:
        print("Unkown parameter: " + tokList[1] + " on line no: " + str(lineNo))
        return -1
