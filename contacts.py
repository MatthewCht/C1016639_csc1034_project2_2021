#class definition
class Contact:

    #constructor
    def __init__(self, name, dob, phone_number):
        self.name == name
        self.dob == dob
        self.number == phone_number

    def display(self):
        return f"{self.name}{self.dob}{self.phone_number}"

#main
if __name__=="__main__":
    #create a contact
    con1 = Contact("Harry", "17 November", "0728327823")
