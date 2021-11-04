#class definition
class Contact:

    #constructor
    def __init__(self, name, dob, address, phone_num):
        self.name = name
        self.dob = dob
        self.address = address
        self.phone_num = phone_num



#main
if __name__=="__main__":

    #starts a while loop so until the user enters something other than 'Y' it keeps adding new contacts
    AddContact = input('Do you want to add a new input? (Y/N):')
    while AddContact == ('Y'):

        #create a contact through accepting inputs
        con = Contact(input("Enter name: "),
                      input("Enter date of birth: "),
                      input("Enter address: "),
                      input("Enter phone number: "))

        #prints the contents of the contact
        print('\nName: ' + con.name,
                '  Date of Birth: ' + con.dob,
                '  Address: ' + con.address,
                '  Phone Number: ' + con.phone_num)

        #takes the first and second half of the contact then concatonates them so it can be written to the file
        contactp1 = ('Name: ' +con.name, '  Date of Birth: ' + con.dob)
        contactp2 = ('  Address: ' + con.address, '  Phone Number: ' + con.phone_num)
        contact1 = str(contactp1 + contactp2)


        #writes the contact to the text file
        file = open('Contacts.txt', 'a')
        file.write('\n' + contact1)
        file.close()
        AddContact = input('Do you want to add a new input? (Y/N)')

    #asks user for input to feed into while loop
    else:
        findcontact = input('Do you want to search for a contact? (Y/N)')

    #creates a while loop for finding a contact
    while findcontact == ('Y'):

        contactkey = input('What is the Contacts name (case sensitive):')
        contactfile = open("Contacts.txt")

        # reference from 'https://www.kite.com/python/answers/how-to-search-for-text-in-a-file-in-python'
        for line in contactfile:
            if contactkey in line:
                print(line)
        findcontact = input('Do you want to search for a contact? (Y/N)')

    else:
        editcontact = input('Do you want to edit a contact? (Y/N)')

    while editcontact == ('Y'):
        contactfile = open("Contacts.txt")
        contactkey = input('What is the Contacts name (case sensitive):')
        for line in contactfile:
            if contactkey in line:
                contactkey = line

        with open('Contacts.txt', 'r') as file:
            lines = file.readlines()

        with open('Contacts.txt', 'w') as file:
            for line in lines:
                if line.strip('\n') != contactkey:
                    file.write(line)

        con = Contact(input("Enter name: "),
                      input("Enter date of birth: "),
                      input("Enter address: "),
                      input("Enter phone number: "))

        # prints the contents of the contact
        print('\nName: ' + con.name,
              '  Date of Birth: ' + con.dob,
              '  Address: ' + con.address,
              '  Phone Number: ' + con.phone_num)

        # takes the first and second half of the contact then concatonates them so it can be written to the file
        contactp1 = ('Name: ' + con.name, '  Date of Birth: ' + con.dob)
        contactp2 = ('  Address: ' + con.address, '  Phone Number: ' + con.phone_num)
        contact1 = str(contactp1 + contactp2)

        # writes the contact to the text file
        file = open('Contacts.txt', 'a')
        file.write('\n' + contact1)
        file.close()

        editcontact = input('Do you want to edit a contact? (Y/N)')

else:
    print('All operations complete')






