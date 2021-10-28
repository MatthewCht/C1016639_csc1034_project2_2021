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

    AddContact = input('Do you want to add a new input? (Y/N):')
    while AddContact == ('Y'):

        #create a contact through accepting inputs
        con1 = Contact(input("Enter name: "), input("Enter date of birth: "), input("Enter address: "), input("Enter phone number: "))

        #prints the contents of contact 1
        print('\nName: ' + con1.name,
                '  Date of Birth: ' + con1.dob,
                '  Address: ' + con1.address,
                '  Phone Number: ' + con1.phone_num)

        contactp1 = ('Name: ' +con1.name, '  Date of Birth: ' + con1.dob)
        contactp2 = ('  Address: ' + con1.address, '  Phone Number: ' + con1.phone_num)
        contact1 = str(contactp1 + contactp2)


        file = open('Contacts.txt', 'a')
        file.write('\n' + contact1)
        file.close()
        AddContact = input('Do you want to add a new input? (Y/N)')

    else:

        print('All processes complete')

