#This is the help file. It contains all the details of the interpreter
#It's sole purpose is to display the help string.
#The help string contains all the information about the syntax and parameter/option usage.

helpString = '''
Welcome to Web Scraping DSL! This contains all the information regarding the syntax and options usage!

'''

def main(tokList, lineNo):
    #tokList should be only of lenght 1(help)
    #if there is more than one item, help is used incorrectly

    if len(tokList) > 1:
        print("Incorrect usage of the help command. Simply type help. Error on line no: " + str(lineNo))
        print(helpString)
        return -1
        
    print(helpString)