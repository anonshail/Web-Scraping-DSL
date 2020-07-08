# Syntax:
1) let command

The purpose of the let command is to create a new variable and store it in the variable tree

Syntax: 

let <var_name> equals <url_value>

Here variable name can be any name apart from a reserved keyword. One variable will hold only one value

2) list command

The purpose of the list command is to create a new list which stores multiple url values. A list in the DSL is very similar to an array in other langauges, and it’s merely a collection of multiple url values.

Syntax

list <list_name> equals <url_value1> <url_value2> <url_value3> . . .

Here, the list name can be any name apart from a reserved keyword. One list can hold any number of url values.

3) freevar command

The purpose of the freevar command is to delete one or more variables from the variables table.

Syntax:

freevar <var_name1> <var_name2> . . .

The freevar command will find the variable names in the variables table and delete the entry. Multiple variables can be deleted using the freevar command as shown above.

4) freelist command

The purpose of the freelist command is to delete one or more lists from the lists table.

Syntax:

freelist <list_name1> <list_name2> . . .

The freelist command will find the list names in the list table and delete the entry. Multiple lists can be deleted using the freevar command as shown above.

5) mem command

The mem command is incharge of displaying the status of the memory to the user based on the options that the user provides. It displays the details of all the active variables and lists based on the user’s preference.

Syntax:

mem <modeOfOption?> <verbose?>

Mode of option indicates what data the user wants to obtain. It’s an optional token, and if absent the mode of options is taken to be normal. In this case, the user will be displayed with all the details of all the variables and list.

Optionally, mode of option can be set to ‘vars’ where it will display details of only variables or ‘list’ where it will display details on only lists.

Another optional token here is the ‘verbose’ token. The verbose option will decide how the memory state is presented to the user. If verbose is present, the user will obtain a list of all identifiers requested (based on mode of operation) along with all the values they store in a neat systematic order. If the verbose option is absent, the identifiers are merely listed(based on the mode of operation) one after the other to indicate the list of active identifiers in the memory.

6) get command

The purpose of the get command is to obtain information or resources from a url or a webpage.

Syntax:

get <resource_type> <resource_identifier> from <url_identifier> write? <location> store? location

The resource_type indicates what type of resources the user wants to obtain. This can be text, images, videos, audios, files, urls, ids and class.

Resource_identifier refers to what particular resource the user wants to obtain. If they wish to obtain all resources, it must be denoted as ‘all’.

Url_identifier can either be a url, a variable or a list. In case of a variable, the variable value is the url that is targeted. Incase of a list a loop is executed. In this case, the command will be looped over all the values present in the list.

Write is an optional command which can divert the output to a file specified in the location.

Store is an optional command which specifies which location the resources obtained should be stored.


7) view command

The purpose of the view command is to obtain details of a webpage or a url and details about associated resources.and information.

Syntax:

view <resource_type> <resource_identifier> from <url_identifier> write? <location>

The resource_type indicates what type of resources the user wants to obtain information about. This can be text, images, videos and audios.

Resource_identifier refers to what particular resource the user wants to obtain information about. If they wish to obtain information about all resources, it must be denoted as ‘all’.

Url_identifier can either be a url, a variable or a list. In case of a variable, the variable value is the url that is targeted. Incase of a list a loop is executed. In this case, the command will be looped over all the values present in the list.

Write is an optional command which can divert the output to a file specified in the location.

8) help command

The help command displays the help string to the user. It displays the purpose, functioning and syntax of all commands and gives the user an understanding of how the DSL works.

Syntax:

help
