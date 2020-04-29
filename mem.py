#this command is in charge of displaying the status of the memory 
#this command has many options:
#   1. verbose = which will display the memory with details
#   2. vars = which will display only variable details
#   3. list = which will display only list details

def main(tokList, lineNo, varTable, listTable):

    #error checking

    #checking if all tokens are consisten
    #loop over all tokens to ensure they are correct

    for tok in tokList:
        if(tok == 'mem' or tok == 'verbose' or tok == 'vars' or tok == 'list'):
            continue
        else:
            print("Incorrect token: " + tok + " on line no: " + str(lineNo) + ". Execute help for information.")
            return -1
    
    #now to check if both list and vars is present in the same command

    #errorFlag indicates if an error has occoured
    #if vars is present add 1, if list is present add 1
    #if value is 2, error has occoured

    errorFlag = 0 
    for tok in tokList:

        if tok == 'vars':
            errorFlag+=1

        if tok == 'list':
            errorFlag+=1
    

    if(errorFlag == 2):
        print ("Incorrect usage of mem command on line: " + str(lineNo) + ". Please execute help for more information.")
        return -1

    #execution of the mem command begins now

    #verboseFlag indicates weather the command is being executed in normal mode or verbose mode
    verboseFlag = 0

    for tok in tokList:
        if tok=='verbose':
            verboseFlag = 1

    #now, to set the mode of operation of mem
    #if mode of op is 0, it is normal mode of operation
    #if mode of op is 1, only vars
    #if mode of op is 2, only list
    modeOfOp = 0

    if(errorFlag==0):
        modeOfOp = 0
    
    #looping over tok to determine mode of op
    else:
        for tok in tokList:
            
            if tok == 'vars':
                modeOfOp = 1
            
            if tok == 'list':
                modeOfOp = 2
    
    #now, we have determined modeOfOp for the mem command, as well as the verbose flag

    #execution of the mem command

    #switch case ladder for verbose flag
    
    # print("Mode= " + str(modeOfOp))

    if(verboseFlag == 0):
        #verbose off
        if modeOfOp == 0:
            #normal

            #vars

            print("Currently active variables in the memory: ")
            listOfVars = varTable.keys()

            for var in listOfVars:
                print (var, end='\t')
            
            print()
            print()

            #lists 

            print("Currently active lists in the memory: ")
            listOfLists = listTable.keys()

            for list_ in listOfLists:
                print (list_, end='\t')
            
            print()

        elif modeOfOp == 1:
            #vars

            print("Currently active variables in the memory: ")
            listOfVars = varTable.keys()

            for var in listOfVars:
                print (var, end='\t')
            
            print()

        elif modeOfOp == 2:
            #lists 

            print("Currently active lists in the memory: ")
            listOfLists = listTable.keys()

            for list_ in listOfLists:
                print (list_, end='\t')
            
            print()
        
        else:
            print("Fatal error has occoured, this should not be happening")
            return -1
    
    else:
        #verbose on
        if modeOfOp == 0:
            #normal

            #vars

            print("Currently active variables in the memory:")
            listOfVars = varTable.keys()

            for var in listOfVars:
                print("Name: " + var + "\t" + "Value: " + varTable[var])
            
            print()
            print()

            #lists

            print("Currently active lists in the memory:")
            listOfLists = listTable.keys()

            for list_ in listOfLists:
                print("Name: " + list_)
                #obtaining serial numbers
                slNoList = range(len(listTable[list_]))

                # #correcting serial numbers
                # for i in range(len(slNoList)):
                #     slNoList[i]+=1

                counter = 0

                #now to print the lists 
                for val in listTable[list_]:
                    print(str(slNoList[counter]+1) + ". " + val)
                    counter += 1
            
                print()

            print()



        elif modeOfOp == 1:
            #vars

            print("Currently active variables in the memory:")
            listOfVars = varTable.keys()

            for var in listOfVars:
                print("Name: " + var + "\t" + "Value: " + varTable[var])
            
            print()
            

        elif modeOfOp == 2:
            #lists

            print("Currently active lists in the memory:")
            listOfLists = listTable.keys()

            for list_ in listOfLists:

                print("Name: " + list_)

                #obtaining serial numbers
                slNoList = range(len(listTable[list_]))

                #correcting serial numbers
                # for i in range(len(slNoList)):
                #     slNoList[i]+=1

                counter = 0

                #now to print the lists 
                for val in listTable[list_]:
                    print(str(slNoList[counter]+1) + ". " + val)
                    counter += 1
            
                print()

            print()

        else:
            print("Fatal error has occoured, this should not be happening")
            return -1