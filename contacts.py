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

    #create a contact
    con1 = Contact(input("Enter name: "), input("Enter date of birth: "), input("Enter address: "), input("Enter phone number: "))

    print('Name: ' + con1.name,
          '\nDate of Birth: ' + con1.dob,
          '\nAddress: ' + con1.address,
          '\nPhone Number: ' + con1.phone_num)
