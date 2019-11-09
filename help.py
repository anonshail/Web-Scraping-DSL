#This is the help file. It contains all the details of the interpreter
#It's sole purpose is to display the help string.
#The help string contains all the information about the syntax and parameter/option usage.

helpString = '''
All the commands are to be in lower case. We are working only with single parameters for a particular key.

1. “Get” command:
Syntax: Get “<type_of_file>” from “<URL_NAME>” <optional_command>.
<type_of_file> would include 1) text, 2) URL 3) ‘img’ (for images) 4) ‘vid’ for videos 3) File-variations (.‘extension’) 4) Documents and Multimedia (.mp3, .mp4).  This command gets the contents of the URL for the type of file specified by the user.
Another variation of the command: 
get extension <Extension_type> from URL <optional_command>.

2. “View” command: Default syntax: view from <URL>
Syntax: view “<type_of_file>” from “<URL>”. 
Like the metadata operation, the view command is used to look at the contents of the given URL with the type of file to lookup as the parameter.

3. “Help” command: 
Syntax: Help. 
This command is used to give the entire documentation of our web-based domain specific language. This will include information on how to use the various command along with details of the parameters. 
The following commands are optional parameters.

4. “Where” command:
Syntax: get <command> from <URL> where <constraint1> <constraint2>.
Where command is used to list the various constraints while fetching the data. The constraints would be written in regex.

5. “Store” command:
Syntax: store <filename> <directory>.
This command is used to store the files fetched to a particular directory.
'''

def main(tokList, lineNo):
    #tokList should be only of lenght 1(help)
    #if there is more than one item, help is used incorrectly

    if len(tokList) > 1:
        print("Incorrect usage of the help command. Simply type help. Error on line no: " + str(lineNo))
        print(helpString)
        return -1
        
    print(helpString)
