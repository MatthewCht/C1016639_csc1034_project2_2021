# class definition
class Contact:

    # constructor
    def __init__(self, name, dob, address, phone_num):
        self.name = name
        self.dob = dob
        self.address = address
        self.phone_num = phone_num


# main
if __name__ == "__main__":

    # shows the entire contact list
    ContactList = input('Do you want view the contacts list? (Y/N):')
    if ContactList == 'Y':
        file = open('Contacts.txt')
        lines = file.readlines()
        for line in lines:
            print(line)
        file.close()

    # starts a while loop so until the user enters something other than 'Y' it keeps adding new contacts
    AddContact = input('Do you want to add a new input? (Y/N):')
    while AddContact == 'Y':

        # create a contact through accepting inputs
        con = Contact(input("Enter name: "),
                      input("Enter date of birth(dd/mm/yyyy): "),
                      input("Enter address: "),
                      input("Enter phone number: "))

        while len(con.phone_num) != 11:
            con.phone_num = input("Please enter a valid phone number: ")

        # prints the contents of the contact
        print('\nName: ' + con.name,
              '  Date of Birth: ' + con.dob,
              '  Address: ' + con.address,
              '  Phone Number: ' + con.phone_num)

        # takes the first and second half of the contact then concatenates them so it can be written to the file
        ContactP1 = ('Name: ' + con.name, '  Date of Birth: ' + con.dob)
        ContactP2 = ('  Address: ' + con.address, '  Phone Number: ' + con.phone_num)
        Contact1 = str(ContactP1 + ContactP2)

        # writes the contact to the text file
        file = open('Contacts.txt', 'a')
        file.write('\n' + Contact1)
        file.close()
        AddContact = input('Do you want to add a new input? (Y/N)')

    # asks user for input to feed into while loop
    else:
        FindContact = input('Do you want to search for a contact? (Y/N)')

    # creates a while loop for finding a contact
    while FindContact == 'Y':

        ContactKey = input('What is the Contacts name (case sensitive):')
        ContactFile = open("Contacts.txt")

        # reference from 'https://www.kite.com/python/answers/how-to-search-for-text-in-a-file-in-python'
        for line in ContactFile:
            if ContactKey in line:
                print(line)
        FindContact = input('Do you want to search for a contact? (Y/N)')

    else:
        EditContact = input('Do you want to edit a contact? (Y/N)')

    # allows for a contact to be edited by deleting it then replacing it with the desired information
    while EditContact == 'Y':
        ContactFile = open("Contacts.txt")
        ContactKey = input('What is the Contacts name (case sensitive):')

        # reference from 'https://www.pythonforbeginners.com/files/how-to-delete-a-specific-line-in-a-file'
        with open('Contacts.txt', 'r') as file:
            lines = file.readlines()

        with open('Contacts.txt', 'w') as file:
            for line in lines:
                if line.find(ContactKey) != -1:
                    pass
                else:
                    file.write(line)

        con = Contact(input("Enter name: "),
                      input("Enter date of birth(dd/mm/yyyy): "),
                      input("Enter address: "),
                      input("Enter phone number: "))

        while len(con.phone_num) != 11:
            con.phone_num = input("Please enter a valid phone number: ")

        # prints the contents of the contact
        print('\nName: ' + con.name,
              '  Date of Birth: ' + con.dob,
              '  Address: ' + con.address,
              '  Phone Number: ' + con.phone_num)

        while len(con.phone_num) != 11:
            con.phone_num = input("Please enter a valid phone number: ")

        # takes the first and second half of the contact then concatenates them so it can be written to the file
        ContactP1 = ('Name: ' + con.name, '  Date of Birth: ' + con.dob)
        ContactP2 = ('  Address: ' + con.address, '  Phone Number: ' + con.phone_num)
        Contact1 = str(ContactP1 + ContactP2)

        # writes the contact to the text file
        file = open('Contacts.txt', 'a')
        file.write('\n' + Contact1)
        file.close()

        EditContact = input('Do you want to edit a contact? (Y/N)')

    else:
        DeleteContact = input('Do you want to delete a contact? (Y/N)')

    while DeleteContact == 'Y':
        ContactFile = open("Contacts.txt")
        print('When entering the name please enter the full name as all which contain this will be deleted also')
        ContactKey = input('What is the Contacts name (case sensitive):')

        with open('Contacts.txt', 'r') as file:
            lines = file.readlines()

        with open('Contacts.txt', 'w') as file:
            for line in lines:
                if line.find(ContactKey) != -1:
                    pass
                else:
                    file.write(line)
        DeleteContact = input('Do you want to delete a contact? (Y/N)')

else:
    print('All operations complete')
