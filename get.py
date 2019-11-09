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


    if (("from" not in tokList) and ("file" not in tokList)):   #file will not have from attribute
        print("Invalid syntax, no from found on line no: " + str(lineNo))
        return -1

    #url comes after from keyword
    if("file" not in tokList):
        urlIndex = tokList.index("from") + 1
        html_doc = requests.get(tokList[urlIndex])
        soup = BeautifulSoup(html_doc.content, 'html.parser')



    #if else ladder of all the get options


    #FOR TEXT
    if(tokList[1] == "text"):
        #cases for text scraping

        #error checking, making sure that all the parameters are correct
        for i in range(len(tokList)):
            if tokList[i] == 'get' or tokList[i] == 'text' or tokList[i] == 'write' or tokList[i] == 'from':
                continue
            elif tokList[i-1] == 'write' or tokList[i-1] == 'from':
                continue
            elif tokList[i][0] == '#':  #skip the remaining, since it's a comment
                break
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




    #FOR IMAGES
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
            elif tokList[i][0] == '#':  #skip the remaining, since it's a comment
                break
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





    #FOR URLS
    elif(tokList[1] == 'urls'):
        #error checking, making sure that all the parameters are correct
        for i in range(len(tokList)):
            if tokList[i] == 'get' or tokList[i] == 'urls' or tokList[i] == 'write' or tokList[i] == 'from':
                continue
            elif tokList[i-1] == 'write' or tokList[i-1] == 'from':
                continue
            elif tokList[i][0] == '#':  #skip the remaining, since it's a comment
                break
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




    #FOR ID
    elif(tokList[1] == 'id'):
        #Error checking
        for i in range(len(tokList)):
            if tokList[i] == 'get' or tokList[i] == 'id' or tokList[i] == 'write' or tokList[i] == 'from':
                continue
            elif tokList[i-1] == 'write' or tokList[i-1] == 'from' or tokList[i-1] == 'id':
                continue
            elif tokList[i][0] == '#':  #skip the remaining, since it's a comment
                break
            else:
                print("Incorrect token: " + tokList[i] + " on line no: " + str(lineNo) + ". Execute help for information.")
                return -1

        currentId = tokList[2]

        if  "write" in tokList:
            #write to a text file
            fileName = tokList[tokList.index("write") + 1]
            file = open(fileName, "a")
            file.write(str(soup.find(id=tokList[tokList.index('id')+1])))               
            file.close()


        else:
            #print on terminal
            print(soup.find(id=tokList[tokList.index('id')+1]))





    #FOR CLASS
    elif(tokList[1] == 'class'):
        #Error checking
        for i in range(len(tokList)):
            if tokList[i] == 'get' or tokList[i] == 'class' or tokList[i] == 'write' or tokList[i] == 'from':
                continue
            elif tokList[i-1] == 'write' or tokList[i-1] == 'from' or tokList[i-1] == 'class':
                continue
            elif tokList[i][0] == '#':  #skip the remaining, since it's a comment
                break
            else:
                print("Incorrect token: " + tokList[i] + " on line no: " + str(lineNo) + ". Execute help for information.")
                return -1

        
        currentClass = tokList[2]

        if  "write" in tokList:
            #write to a text file
            fileName = tokList[tokList.index("write") + 1]
            file = open(fileName, "a")
            for tag in soup.find_all(class_=tokList[2]):
                file.write(str(tag)+"\n")
            file.close()

        else:
            #print on terminal
            for tag in soup.find_all(class_=tokList[2]):
                print(str(tag)+"\n")





    #FOR FILE
    elif(tokList[1]=="file"):
        storeFlag = False
        storeLocation = ''   #location to store the file into, if storeFlat is set to true
        

        #error checking, making sure that all the parameters are correct
        for i in range(len(tokList)):
            if tokList[i] == 'get' or tokList[i] == 'file' or tokList[i] == 'store':
                continue
            elif tokList[i-1] == 'file':
                continue
            elif tokList[i][0] == '#':  #skip the remaining, since it's a comment
                break
            elif tokList[i-1] == 'store':   #if you want to store into a folder
                storeFlag = True            #enabling store
                storeLocation = tokList[i]   #location to store is set

                #check if storeLocation exists, or else create it
                if(os.path.exists(storeLocation)==False):
                    os.mkdir(storeLocation) 


        #obtaining file url
        fileUrl = tokList[2]
        
        r = requests.get(fileUrl, stream = True)
        filename = fileUrl.split('/')[-1].split('#')[0].split('?')[0]
        with open(storeLocation+filename,"wb") as file:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)





    #FOR VIDEO
    elif(tokList[1]=="videos"):
        #case for videos
        storeFlag = False
        storeLocation = ''   #location to store videos into, if storeFlat is set to true
        

        #error checking, making sure that all the parameters are correct
        for i in range(len(tokList)):
            if tokList[i] == 'get' or tokList[i] == 'videos' or tokList[i] == 'from' or tokList[i] == 'store':
                continue
            elif tokList[i-1] == 'videos' or tokList[i-1] == 'from':
                continue
            elif tokList[i][0] == '#':  #skip the remaining, since it's a comment
                break
            elif tokList[i-1] == 'store':   #if you want to store into a folder
                storeFlag = True            #enabling store
                storeLocation = tokList[i]   #location to store is set

                #check if storeLocation exists, or else create it
                if(os.path.exists(storeLocation)==False):
                    os.mkdir(storeLocation)


            else:
                print("Incorrect token: " + tokList[i] + " on line no: " + str(lineNo) + ". Execute help for information.")
                return -1

        #check which videos to get, i.e., all or some specific videos
        #here, tokList[2] must contain all, or a particular video to download

        if(tokList[2] == 'all'):
            #download all videos
            video_tags = soup.find_all('video')
            urls = [video.source['src'] for video in video_tags]

            for url in urls:
                #filename = re.search(r'/([\w_-]+[.](mp4|ogg|webm))$', url)
                filename = url.split('/')[-1].split('#')[0].split('?')[0]
                with open(storeLocation+filename, 'wb') as f:
                    if 'http' not in url:
                        # sometimes an video source can be relative 
                        # if it is provide the base url which also happens 
                        # to be the site variable atm. 
                        url = '{}{}'.format(tokList[urlIndex], url)
                    response = requests.get(url)
                    f.write(response.content)

        else:
            #download a particular video
            if(tokList[2]=='from'):
                #no video has been mentioned, hence, throw error, while checking for store
                print("No video mentioned on line no: " + str(lineNo) + ". Execute help for information.")
                return -1
            
            #now, download video stored in tokList[2] or throw an error, while checking for store
            urlOfFile = tokList[2]
            filename = urlOfFile.split('/')[-1].split('#')[0].split('?')[0]
            with open(storeLocation+filename, 'wb') as f:
                if 'http' not in urlOfFile:
                    # sometimes an video source can be relative 
                    # if it is provide the base urlOfFile which also happens 
                    # to be the site variable atm. 
                    urlOfFile = '{}{}'.format(tokList[urlIndex], urlOfFile)
                response = requests.get(urlOfFile)
                f.write(response.content)


    
    #UNKNOWN COMMAND ERROR
    else:
        print("Unkown parameter: " + tokList[1] + " on line no: " + str(lineNo))
        return -1
