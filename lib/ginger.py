import json
import os

class Contact:
    def __init__(self,firstname,lastname,email,phone,group,address):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.address = address
        self.phone=phone
        self.group=group
        
    def __str__(self):
        return "FirstName:{0}\nLastname:{1}\nEmail address:{2}\nPhone:{3}\nGroup:{4}\naddress:{5}".format(self.firstname,self.lastname,self.email,self.phone,self.group,self.address)
  
class Group:
    def __init__(self,name):
        self.name=name
        
    def __str__(self):
        return "Group Name :{0}".format(self.name)

        
def add_contact():
    address_book_file=open("./data/address_book_file.json","r")
    is_file_empty=os.path.getsize("./data/address_book_file.json")==0
    if not is_file_empty:
        list_contacts=json.load(address_book_file)
    else:
        list_contacts={}
        list_contacts["users"] = {}
        list_contacts["group"] = []

    if len(list_contacts["users"]) == 0:
        id_max = 1
    else:
        id_max = int(max(list_contacts["users"])) + 1

    try:
        contact=get_contact_info_from_user()
        address_book_file=open("./data/address_book_file.json","w")
        list_contacts["users"][id_max] = contact.__dict__
        json.dump(list_contacts,address_book_file,indent=4, sort_keys=True)
        print "Contact added"
    except KeyboardInterrupt:
        print "Contact not added"
    except EOFError:
        print "Contact not added"
    finally:
        address_book_file.close()
    
def get_contact_info_from_user():
    try:
        first_name=raw_input("Enter contact firstname\n")
        last_name=raw_input("Enter contact lastname\n")
        #Initializing for mail 
        nbr_email = 0
        mail_address = []
        #Initializing for location
        nbr_street = 0
        location = []
        #Initializing for phone
        nbr_phone = 0
        phone_num = []
        #Initializing for groups
        nbr_group = 0
        name_group = []

        # Getting number of mails
        while(int(nbr_email)<1):
        	nbr_email=raw_input("Enter number of email addresses\n")
		
		#Generating a string concatening all mail addresses of user
		for i in xrange(0,int(nbr_email)):
			mail = raw_input("Enter contact email address\n")
			mail_address.append(mail)

		# Getting number of location addresses
		while(int(nbr_street)<1):
			nbr_street=raw_input("Enter number of location addresses\n")
		#Generating a string concatening all mail addresses of user
		for i in xrange(0,int(nbr_street)):
			adrs = raw_input("Enter contact location address\n")
			location.append(adrs)

		# Getting number of mails
		
		while(int(nbr_phone)<1):
			nbr_phone=raw_input("Enter number of phone numbers\n")
		#Generating a string concatening all mail addresses of user
		for i in xrange(0,int(nbr_phone)):
			phone = raw_input("Enter contact phone numbers\n")
			phone_num.append(phone)

		# Getting number of mails
		while(int(nbr_group)<1):
			nbr_group=raw_input("Enter number of groups\n")
		#Generating a string concatening all mail addresses of user
		for i in xrange(0,int(nbr_group)):
			group = raw_input("Enter group name\n")
			name_group.append(group.lower())

        contact=Contact(first_name.lower(),last_name.lower(), mail_address, phone_num,name_group,location )
        return contact
    except EOFError as e:
        #print "You entered end of file. Contact not added"
        raise e
    except KeyboardInterrupt as e:
        #print "Keyboard interrupt. Contact not added"
        raise e

def say_hello():
    name = raw_input("What is your name? ")
    return "Hello " + name

def add_group():
    group_file=open("./data/address_book_file.json","r")
    is_file_empty=os.path.getsize("./data/address_book_file.json")==0
    if not is_file_empty:
        list_contacts=json.load(group_file)
    else:
        list_contacts={}
        list_contacts["users"] = {}
        list_contacts["group"] = []
    try:
        group=get_group_info(list_contacts["group"])
        if group.name in list_contacts["group"]:
            print "Group {0} already in list".format(group.name)
        else:
            group_file=open("./data/address_book_file.json","w")
            list_contacts["group"].append(group.name)
            json.dump(list_contacts,group_file,indent=4, sort_keys=True)
            print "Group added"
    except KeyboardInterrupt:
        print "Group not added"
    except EOFError:
        print "Group not added"
    finally:
        group_file.close()
    
def get_group_info(list_group):
    try:
        group = raw_input("Enter a group name\n")
        group=Group(group.lower() )
        return group
    except EOFError as e:
        #print "You entered end of file. Contact not added"
        raise e
    except KeyboardInterrupt as e:
        #print "Keyboard interrupt. Contact not added"
        raise e


def display_group():
    address_book_file=open("./data/address_book_file.json","r")
    is_file_empty=os.path.getsize("./data/address_book_file.json")==0
    if not is_file_empty:
        list_contacts=json.load(address_book_file)
        if len(list_contacts["group"])>0: 
            if len(list_contacts["users"])>0:
                group = raw_input("Enter a group available in our list\n")
                if group not in list_contacts["group"]:
                    print "This group is not in our list\n"
                else:
                    i = 0
                    for contact in list_contacts["users"]:
                        if group in list_contacts["users"][contact]["group"]:
                            print "User : {0} {1}\n".format(list_contacts["users"][contact]["firstname"],list_contacts["users"][contact]["lastname"])
                            i += 1
                    if (i == 0):
                        print "No user with this group\n"
            else:
                print "no contacts in contact book\n"
        else:
            print "No Groups added\n"
    else:
        print "No data in address book\n"
        return
    address_book_file.close()
    
def display_user_groups():
    address_book_file=open("./data/address_book_file.json","r")
    is_file_empty=os.path.getsize("./data/address_book_file.json")==0
    if not is_file_empty:
        list_contacts=json.load(address_book_file)
        if len(list_contacts["users"])>0:
            user = raw_input("Enter a user firstname\n")
            i = 0
            for users in list_contacts["users"]:
                if user.lower() == list_contacts["users"][users]["firstname"]:
                    loc = ', '.join(list_contacts["users"][users]["group"])
                    print "User {0} belongs to groups {1}".format(user,loc)
                    i += 1
            if i == 0:
                print "No user with this firstname"
        else:
            print "no contacts in contact book\n"
    else:
        print "No data in address book\n"
        return
    address_book_file.close()
    
def find_user():
    address_book_file=open("./data/address_book_file.json","r")
    is_file_empty=os.path.getsize("./data/address_book_file.json")==0
    if not is_file_empty:
        list_contacts=json.load(address_book_file)
        if len(list_contacts["users"])>0:
            user = raw_input("Enter a keyword to find users\n")
            i = 0
            for users in list_contacts["users"]:
                if (user.lower() == list_contacts["users"][users]["firstname"] or user.lower() == list_contacts["users"][users]["lastname"]):
                    print "User found:  firstname {0} , lastname {1}".format(list_contacts["users"][users]["firstname"],list_contacts["users"][users]["lastname"])
                    i += 1
            if i == 0:
                print "No user with this firstname"
        else:
            print "no contacts in contact book\n"
    else:
        print "No data in address book\n"
        return
    address_book_file.close()

def find_user_mail():
    address_book_file=open("./data/address_book_file.json","r")
    is_file_empty=os.path.getsize("./data/address_book_file.json")==0
    if not is_file_empty:
        list_contacts=json.load(address_book_file)
        if len(list_contacts["users"])>0:
            mail = raw_input("Enter a keyword to find users\n")
            i = 0
            for users in list_contacts["users"]:
                mail_adress = ', '.join(list_contacts["users"][users]["email"])
                if (mail.lower() in mail_adress):
                    print "User found:  firstname {0} , lastname {1}, mail {2}".format(list_contacts["users"][users]["firstname"],list_contacts["users"][users]["lastname"],mail_adress)
                    i += 1
            if i == 0:
                print "No user with this mail"
        else:
            print "no contacts in contact book\n"
    else:
        print "No data in address book\n"
        return
    address_book_file.close()

    
