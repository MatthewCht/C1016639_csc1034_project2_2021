# CSC1034_Assessment_2


## Project Overview:
This application allows the user to access a contacts list to view or edit it.
A contact can be found individually or in groups based on contact information, or it can show the entire list at once.
The contact information can be edited by adding new contacts, editing existing contacts or deleting contacts.
Each of these can be done as many as wanted but once you no longer want to do it you will have to restart the program to do it again.

##Assumptions Made:
* The user will only use valid inputs
* The user will only want to use the operations in the order they are in 
* When editing a contact the user will change it all and re-write what they want to keep the same
* If they want to say yes they type exactly 'Y' and not 'y' or 'yes' to make the while loops work
* They know all the information of the contact they are adding and not just some

## How To Run:
Once this application is run it will ask what the user wants to do via a series of questions and if you want to the user must enter 'Y'.
Once the user has selected the process desired they must input the indicated information then the process will be carried out and the information will be displayed if necessary.

## Use Case:
When asked for a choice between Y or N such as in this line:

    ContactList = input('Do you want view the contacts list? (Y/N):')
 
if you input 'Y' it will allow you to carry out that function but if you input anything else it won't be carried out and it will carry on to the next function until there are none left then the file will close.




When asked to input details for the contact such as in these lines:

    con = Contact(input("Enter name: "),
                      input("Enter date of birth(dd/mm/yyyy): "),
                      input("Enter address: "),
                      input("Enter phone number: "))

You should input name, the date of birth, address then phone number, as indicated.
The phone number must be 11 characters long, or you will have to put it in again until it is.