#get command in Web Scrapping DSL
#The purpose of this command is to get details of the particular url, and display it to the user
#Similar to "ls" command in shell



# View Options:
# 1. View Text - done
# 2. View Images - done
# 3. View Urls - done
# 4. View Videos - done
# 5. View Files
# 6. View Audios - done



#modules to be imported
from bs4 import BeautifulSoup
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
        reportString = "Text report for the page : " + tokList[urlIndex] + "\n\n"
        reportString += "The responce contains " + str(noOfWords) +" word(s) and " + str(lengthOfText) + " character(s)" 
        reportString += "\n\n"
        

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
    



    #FOR IMAGES
    if(tokList[1] == 'images'):
        #error checking, making sure that all the parameters are correct
        for i in range(len(tokList)):
            if tokList[i] == 'view' or tokList[i] == 'images' or tokList[i] == 'write' or tokList[i] == 'from':
                continue
            elif tokList[i-1] == 'write' or tokList[i-1] == 'from':
                continue
            elif tokList[i][0] == '#':  #skip the remaining, since it's a comment
                break
            else:
                print("Incorrect token: " + tokList[i] + " on line no: " + str(lineNo) + ". Execute help for information.")
                return -1
        


        #now, to obtain a list of titles of the images, and the image urls
        #and to display to the user, or to write the results into a file


        #obtaining all image tags
        img_tags = soup.find_all('img')

        #obtraining src url form the image tags
        urls = [img['src'] for img in img_tags]

        #attempting to fix urls
        for i in range(len(urls)):
            if urls[i].startswith('http'):
                continue
            elif urls[i].startswith('//'):
                urls[i]="http:"+urls[i]
            elif urls[i].startswith('/'):
                baseUrl =  os.path.dirname(tokList[urlIndex])
                urls[i] = baseUrl + urls[i]
            else:
                baseUrl =  os.path.dirname(tokList[urlIndex])
                urls[i] = baseUrl + '/' + urls[i]

        #obtaining filename list, from the urls
        filenames = [url.split('/')[-1].split('#')[0].split('?')[0] for url in urls]

        #creating a report string
        reportString = "Images report for the page : " + tokList[urlIndex] + "\n"
        reportString += "Number of images: " + str(len(urls)) + "\n\n"
        reportString += "Filename: Url"

        for i in range(len(urls)):
            reportString += "\n" + filenames[i] + ": " + urls[i]
        
        reportString+="\n\n"
        
        
        #now, to either write the report string into a file or print it
        if  "write" in tokList:
            #write contents into the file after write keyword
            fileName = tokList[tokList.index("write") + 1]
            file = open(fileName, "a")
            file.write(reportString)
            file.close()
            
        else:
            #display all the text of the page on the terminal
            print(reportString)
    






    #FOR VIDEO
    elif(tokList[1] == 'videos'):
        #error checking, making sure that all the parameters are correct
        for i in range(len(tokList)):
            if tokList[i] == 'view' or tokList[i] == 'videos' or tokList[i] == 'write' or tokList[i] == 'from':
                continue
            elif tokList[i-1] == 'write' or tokList[i-1] == 'from':
                continue
            elif tokList[i][0] == '#':  #skip the remaining, since it's a comment
                break
            else:
                print("Incorrect token: " + tokList[i] + " on line no: " + str(lineNo) + ". Execute help for information.")
                return -1

        
        #obtaining all video tags
        video_tags = soup.find_all('video')

        #obtaining urls of the video tags
        urls = [video.source['src'] for video in video_tags]

        #attempting to fix urls
        for i in range(len(urls)):
            if urls[i].startswith('http'):
                continue
            elif urls[i].startswith('//'):
                urls[i]="http:"+urls[i]
            elif urls[i].startswith('/'):
                baseUrl =  os.path.dirname(tokList[urlIndex])
                urls[i] = baseUrl + urls[i]
            else:
                baseUrl =  os.path.dirname(tokList[urlIndex])
                urls[i] = baseUrl + '/' + urls[i]

        #obtaining filename list, from the urls
        filenames = [url.split('/')[-1].split('#')[0].split('?')[0] for url in urls]

        #creating a report string
        reportString = "Videos report for the page : " + tokList[urlIndex] + "\n"
        reportString += "Number of videos: " + str(len(urls)) + "\n\n"
        reportString += "Filename: Url"

        for i in range(len(urls)):
            reportString += "\n" + filenames[i] + ": " + urls[i]
        
        reportString+="\n\n"
        
        
        #now, to either write the report string into a file or print it
        if  "write" in tokList:
            #write contents into the file after write keyword
            fileName = tokList[tokList.index("write") + 1]
            file = open(fileName, "a")
            file.write(reportString)
            file.close()
            
        else:
            #display all the text of the page on the terminal
            print(reportString)

    


    #FOR AUDIO
    elif(tokList[1] == 'audios'):
        #error checking, making sure that all the parameters are correct
        for i in range(len(tokList)):
            if tokList[i] == 'view' or tokList[i] == 'audios' or tokList[i] == 'write' or tokList[i] == 'from':
                continue
            elif tokList[i-1] == 'write' or tokList[i-1] == 'from':
                continue
            elif tokList[i][0] == '#':  #skip the remaining, since it's a comment
                break
            else:
                print("Incorrect token: " + tokList[i] + " on line no: " + str(lineNo) + ". Execute help for information.")
                return -1

        
        #obtaining all audio tags
        audio_tags = soup.find_all('audio')

        #obtaining urls of the audio tags
        urls = [audio.source['src'] for audio in audio_tags]

        #attempting to fix urls
        for i in range(len(urls)):
            if urls[i].startswith('http'):
                continue
            elif urls[i].startswith('//'):
                urls[i]="http:"+urls[i]
            elif urls[i].startswith('/'):
                baseUrl =  os.path.dirname(tokList[urlIndex])
                urls[i] = baseUrl + urls[i]
            else:
                baseUrl =  os.path.dirname(tokList[urlIndex])
                urls[i] = baseUrl + '/' + urls[i]

        #obtaining filename list, from the urls
        filenames = [url.split('/')[-1].split('#')[0].split('?')[0] for url in urls]

        #creating a report string
        reportString = "Audios report for the page : " + tokList[urlIndex] + "\n"
        reportString += "Number of audios: " + str(len(urls)) + "\n\n"
        reportString += "Filename: Url"

        for i in range(len(urls)):
            reportString += "\n" + filenames[i] + ": " + urls[i]
        
        reportString+="\n\n"
        
        
        #now, to either write the report string into a file or print it
        if  "write" in tokList:
            #write contents into the file after write keyword
            fileName = tokList[tokList.index("write") + 1]
            file = open(fileName, "a")
            file.write(reportString)
            file.close()
            
        else:
            #display all the text of the page on the terminal
            print(reportString)

    


    #FOR URLS
    elif(tokList[1] == 'urls'):
        #error checking, making sure that all the parameters are correct
        for i in range(len(tokList)):
            if tokList[i] == 'view' or tokList[i] == 'urls' or tokList[i] == 'write' or tokList[i] == 'from':
                continue
            elif tokList[i-1] == 'write' or tokList[i-1] == 'from':
                continue
            elif tokList[i][0] == '#':  #skip the remaining, since it's a comment
                break
            else:
                print("Incorrect token: " + tokList[i] + " on line no: " + str(lineNo) + ". Execute help for information.")
                return -1
        

        links = soup.find_all('a', href=True)

        #Creating the report string
        reportString = "URLS report for the page : " + tokList[urlIndex] + "\n"
        reportString += "Number of URLs: " + str(len(links)) + "\n\n"
        

        #now, to either write the report string into a file or print it
        if  "write" in tokList:
            #write contents into the file after write keyword
            fileName = tokList[tokList.index("write") + 1]
            file = open(fileName, "a")
            file.write(reportString)
            file.close()
            
        else:
            #display all the text of the page on the terminal
            print(reportString)




    #FOR FILES
    elif(tokList[1] == 'file'):


        #error checking, making sure that all the parameters are correct
        for i in range(len(tokList)):
            if tokList[i] == 'view' or tokList[i] == 'file' or tokList[i] == 'write' or tokList[i] == 'from':
                continue
            elif tokList[i-1] == 'write' or tokList[i-1] == 'from':
                continue
            elif tokList[i][0] == '#':  #skip the remaining, since it's a comment
                break
            else:
                print("Incorrect token: " + tokList[i] + " on line no: " + str(lineNo) + ". Execute help for information.")
                return -1


        #Creating list of all URLs
        allUrls=[] #will contain all urls

        for link in soup.find_all('a', href=True):
            if link.get('href').startswith('http'):
                curLink=link.get('href')
            elif link.get('href').startswith('//'):
                curLink="http:"+link.get('href')
            elif link.get('href').startswith('/'):
                baseUrl =  os.path.dirname(tokList[urlIndex])
                curLink = baseUrl + link.get('href')
            else:
                baseUrl =  os.path.dirname(tokList[urlIndex])
                curLink = baseUrl + '/' + link.get('href')
            
            allUrls.append(curLink)


        #if a url is a file, select it as fileUrl
        fileUrl = []


        #creating a blacklist of extensions:
        blacklist = ['asp', 'aspx', 'axd', 'asx', 'asmx', 'ashx', 'css', 'cfm', 'yaws', 'swf', 'html', 'htm', 'xhtml', 'jhtml', 'jsp', 'jspx', 'wss', 'do', 'action', 'js', 'php', 'pl', 'php4', 'php3', 'phtml', 'py', 'rb', 'rhtml', 'shtml', 'xml', 'rss', 'svg', 'cgi', 'dll', 'com', 'in', 'org', 'edu']
        blacklist2 = ['.abbott', '.abogado', '.ac', '.academy', '.accountant', '.accountants', '.active', '.actor', '.ad', '.ads', '.adult', '.ae', '.aero', '.af', '.afl', '.ag', '.agency', '.ai', '.airforce', '.al', '.allfinanz', '.alsace', '.am', '.amsterdam', '.an', '.android', '.ao', '.apartments', '.aq', '.aquarelle', '.ar', '.archi', '.army', '.arpa', '.as', '.asia', '.associates', '.at', '.attorney', '.au', '.auction', '.audio', '.autos', '.aw', '.ax', '.axa', '.az', '.ba', '.band', '.bank', '.bar', '.barclaycard', '.barclays', '.bargains', '.bauhaus', '.bayern', '.bb', '.bbc', '.bd', '.be', '.beer', '.berlin', '.best', '.bf', '.bg', '.bh', '.bi', '.bid', '.bike', '.bingo', '.bio', '.biz', '.bj', '.bl', '.black', '.blackfriday', '.bloomberg', '.blue', '.bm', '.bmw', '.bn', '.bnpparibas', '.bo', '.boats', '.bond', '.boo', '.boutique', '.bq', '.br', '.brussels', '.bs', '.bt', '.budapest', '.build', '.builders', '.business', '.buzz', '.bv', '.bw', '.by', '.bz', '.bzh', '.ca', '.cab', '.cafe', '.cal', '.camera', '.camp', '.cancerresearch', '.canon', '.capetown', '.capital', '.caravan', '.cards', '.care', '.career', '.careers', '.cartier', '.casa', '.cash', '.casino', '.cat', '.catering', '.cbn', '.cc', '.cd', '.center', '.ceo', '.cern', '.cf', '.cfd', '.cg', '.ch', '.channel', '.chat', '.cheap', '.chloe', '.christmas', '.chrome', '.church', '.ci', '.citic', '.city', '.ck', '.cl', '.claims', '.cleaning', '.click', '.clinic', '.clothing', '.club', '.cm', '.cn', '.co', '.coach', '.codes', '.coffee', '.college', '.cologne', '.com', '.community', '.company', '.computer', '.condos', '.construction', '.consulting', '.contractors', '.cooking', '.cool', '.coop', '.country', '.courses', '.cr', '.credit', '.creditcard', '.cricket', '.crs', '.cruises', '.cu', '.cuisinella', '.cv', '.cw', '.cx', '.cy', '.cymru', '.cyou', '.cz', '.dabur', '.dad', '.dance', '.date', '.dating', '.datsun', '.day', '.dclk', '.de', '.deals', '.degree', '.delivery', '.democrat', '.dental', '.dentist', '.desi', '.design', '.dev', '.diamonds', '.diet', '.digital', '.direct', '.directory', '.discount', '.dj', '.dk', '.dm', '.dnp', '.do', '.docs', '.doha', '.domains', '.doosan', '.download', '.durban', '.dvag', '.dz', '.eat', '.ec', '.edu', '.education', '.ee', '.eg', '.eh', '.email', '.emerck', '.energy', '.engineer', '.engineering', '.enterprises', '.epson', '.equipment', '.er', '.erni', '.es', '.esq', '.estate', '.et', '.eu', '.eurovision', '.eus', '.events', '.everbank', '.exchange', '.expert', '.exposed', '.express', '.fail', '.faith', '.fan', '.fans', '.farm', '.fashion', '.feedback', '.fi', '.film', '.finance', '.financial', '.firmdale', '.fish', '.fishing', '.fit', '.fitness', '.fj', '.fk', '.flights', '.florist', '.flowers', '.flsmidth', '.fly', '.fm', '.fo', '.foo', '.football', '.forex', '.forsale', '.foundation', '.fr', '.frl', '.frogans', '.fund', '.furniture', '.futbol', '.ga', '.gal', '.gallery', '.garden', '.gb', '.gbiz', '.gd', '.gdn', '.ge', '.gent', '.gf', '.gg', '.ggee', '.gh', '.gi', '.gift', '.gifts', '.gives', '.gl', '.glass', '.gle', '.global', '.globo', '.gm', '.gmail', '.gmo', '.gmx', '.gn', '.gold', '.goldpoint', '.golf', '.goo', '.goog', '.google', '.gop', '.gov', '.gp', '.gq', '.gr', '.graphics', '.gratis', '.green', '.gripe', '.gs', '.gt', '.gu', '.guge', '.guide', '.guitars', '.guru', '.gw', '.gy', '.hamburg', '.hangout', '.haus', '.healthcare', '.help', '.here', '.hermes', '.hiphop', '.hiv', '.hk', '.hm', '.hn', '.holdings', '.holiday', '.homes', '.horse', '.host', '.hosting', '.house', '.how', '.hr', '.ht', '.hu', '.ibm', '.id', '.ie', '.ifm', '.il', '.im', '.immo', '.immobilien', '.in', '.industries', '.infiniti', '.info', '.ing', '.ink', '.institute', '.insure', '.int', '.international', '.investments', '.io', '.iq', '.ir', '.irish', '.is', '.it', '.iwc', '.java', '.jcb', '.je', '.jetzt', '.jm', '.jo', '.jobs', '.joburg', '.jp', '.juegos', '.kaufen', '.kddi', '.ke', '.kg', '.kh', '.ki', '.kim', '.kitchen', '.kiwi', '.km', '.kn', '.koeln', '.komatsu', '.kp', '.kr', '.krd', '.kred', '.kw', '.ky', '.kyoto', '.kz', '.la', '.lacaixa', '.land', '.lat', '.latrobe', '.lawyer', '.lb', '.lc', '.lds', '.lease', '.leclerc', '.legal', '.lgbt', '.li', '.lidl', '.life', '.lighting', '.limited', '.limo', '.link', '.lk', '.loan', '.loans', '.london', '.lotte', '.lotto', '.love', '.lr', '.ls', '.lt', '.ltda', '.lu', '.luxe', '.luxury', '.lv', '.ly', '.ma', '.madrid', '.maif', '.maison', '.management', '.mango', '.market', '.marketing', '.markets', '.marriott', '.mc', '.md', '.me', '.media', '.meet', '.melbourne', '.meme', '.memorial', '.menu', '.mf', '.mg', '.mh', '.miami', '.mil', '.mini', '.mk', '.ml', '.mm', '.mma', '.mn', '.mo', '.mobi', '.moda', '.moe', '.monash', '.money', '.mormon', '.mortgage', '.moscow', '.motorcycles', '.mov', '.movie', '.mp', '.mq', '.mr', '.ms', '.mt', '.mtn', '.mtpc', '.mu', '.museum', '.mv', '.mw', '.mx', '.my', '.mz', '.na', '.nagoya', '.name', '.navy', '.nc', '.ne', '.net', '.network', '.neustar', '.new', '.news', '.nexus', '.nf', '.ng', '.ngo', '.nhk', '.ni', '.nico', '.ninja', '.nissan', '.nl', '.no', '.np', '.nr', '.nra', '.nrw', '.ntt', '.nu', '.nyc', '.nz', '.okinawa', '.om', '.one', '.ong', '.onl', '.online', '.ooo', '.org', '.organic', '.osaka', '.otsuka', '.ovh', '.pa', '.page', '.panerai', '.paris', '.partners', '.parts', '.party', '.pe', '.pf', '.pg', '.ph', '.pharmacy', '.photo', '.photography', '.photos', '.physio', '.piaget', '.pics', '.pictet', '.pictures', '.pink', '.pizza', '.pk', '.pl', '.place', '.plumbing', '.plus', '.pm', '.pn', '.pohl', '.poker', '.porn', '.post', '.pr', '.praxi', '.press', '.pro', '.prod', '.productions', '.prof', '.properties', '.property', '.ps', '.pt', '.pub', '.pw', '.py', '.qa', '.qpon', '.quebec', '.racing', '.re', '.realtor', '.recipes', '.red', '.redstone', '.rehab', '.reise', '.reisen', '.reit', '.ren', '.rentals', '.repair', '.report', '.republican', '.rest', '.restaurant', '.review', '.reviews', '.rich', '.rio', '.rip', '.ro', '.rocks', '.rodeo', '.rs', '.rsvp', '.ru', '.ruhr', '.rw', '.ryukyu', '.sa', '.saarland', '.sale', '.samsung', '.sap', '.sarl', '.saxo', '.sb', '.sc', '.sca', '.scb', '.schmidt', '.scholarships', '.school', '.schule', '.schwarz', '.science', '.scot', '.sd', '.se', '.services', '.sew', '.sexy', '.sg', '.sh', '.shiksha', '.shoes', '.shriram', '.si', '.singles', '.site', '.sj', '.sk', '.sky', '.sl', '.sm', '.sn', '.so', '.social', '.software', '.sohu', '.solar', '.solutions', '.soy', '.space', '.spiegel', '.spreadbetting', '.sr', '.ss', '.st', '.study', '.style', '.su', '.sucks', '.supplies', '.supply', '.support', '.surf', '.surgery', '.suzuki', '.sv', '.sx', '.sy', '.sydney', '.systems', '.sz', '.taipei', '.tatar', '.tattoo', '.tax', '.tc', '.td', '.tech', '.technology', '.tel', '.temasek', '.tennis', '.tf', '.tg', '.th', '.tickets', '.tienda', '.tips', '.tires', '.tirol', '.tj', '.tk', '.tl, National Division of Information and Technolog', '.tm', '.tn', '.to', '.today', '.tokyo', '.tools', '.top', '.toshiba', '.tours', '.town', '.toys', '.tp', '.tr', '.trade', '.trading', '.training', '.travel', '.trust', '.tt', '.tui', '.tv', '.tw', '.tz', '.ua', '.ug', '.uk', '.um', '.university', '.uno', '.uol', '.us', '.uy', '.uz', '.va', '.vacations', '.vc', '.ve', '.vegas', '.ventures', '.versicherung', '.vet', '.vg', '.vi', '.viajes', '.video', '.villas', '.vision', '.vlaanderen', '.vn', '.vodka', '.vote', '.voting', '.voto', '.voyage', '.vu', '.wales', '.wang', '.watch', '.webcam', '.website', '.wed', '.wedding', '.wf', '.whoswho', '.wien', '.wiki', '.williamhill', '.win', '.wme', '.work', '.works', '.world', '.ws', '.wtc', '.wtf', '.xin', '.测试', '.परीक्षा', '.佛山', '.慈善', '.集团', '.在线', '.한국', '.ভারত', '.八卦', '.موقع', '.বাংলা', '.公益', '.公司', '.移动', '.我爱你', '.москва', '.испытание', '.қаз', '.онлайн', '.сайт', '.срб', '.бел', '.时尚', '.테스트', '.淡马锡', '.орг', '.삼성', '.சிங்கப்பூர்', '.商标', '.商店', '.商城', '.дети', '.мкд', '.טעסט', '.中文网', '.中信', '.中国', '.中國', '.谷歌', '.భారత్', '.ලංකා', '.測試', '.ભારત', '.भारत', '.آزمایشی', '.பரிட்சை', '.网店', '.संगठन', '.网络', '.укр', '.香港', '.δοκιμή', '.飞利浦', '.إختبار', '.台湾', '.台灣', '.手机', '.мон', '.الجزائر', '.عمان', '.ایران', '.امارات', '.بازار', '.پاکستان', '.الاردن', '.بھارت', '.المغرب', '.السعودية', '.سودان', '.عراق', '.مليسيا', '.政府', '.شبكة', '.გე', '.机构', '.组织机构', '.健康', '.ไทย', '.سورية', '.рус', '.рф', '.تونس', '.みんな', '.グーグル', '.世界', '.ਭਾਰਤ', '.网址', '.游戏', '.vermögensberater', '.vermögensberatung', '.企业', '.信息', '.مصر', '.قطر', '.广东', '.இலங்கை', '.இந்தியா', '.հայ', '.新加坡', '.فلسطين', '.テスト', '.政务', '.xxx', '.xyz', '.yachts', '.yandex', '.ye', '.yodobashi', '.yoga', '.yokohama', '.youtube', '.yt', '.za', '.zip', '.zm', '.zone', '.zuerich', '.zw']

        #obtaining file extension and checking
        for url in allUrls:
            extension = os.path.splitext(url)[1]
            
            #if extensions is blank or in blacklist, ignore
            if extension == '' or extension in blacklist or extension in blacklist2:
                continue

            #else add it to the fileurl list
            else:
                fileUrl.append(url)

        
        #creating a report string
        reportString = "Files report for the page : " + tokList[urlIndex] + "\n"
        reportString += "Number of files: " + str(len(fileUrl)) + "\n\n"
        reportString += "Urls:"

        for link in fileUrl:
            reportString += "\n" + link 
        
        reportString+="\n\n"
           
        #now, to either write the report string into a file or print it
        if  "write" in tokList:
            #write contents into the file after write keyword
            fileName = tokList[tokList.index("write") + 1]
            file = open(fileName, "a")
            file.write(reportString)
            file.close()
            
        else:
            #display all the text of the page on the terminal
            print(reportString) 




    #UNKNOWN COMMAND ERROR
    else:
        print("Unkown parameter: " + tokList[1] + " on line no: " + str(lineNo))
        return -1

        


        




    
