## Loading Ginger Lib
import imp
imp.load_source("ginger", "./lib/ginger.py")
import ginger 

print "Please Enter:\n'a' to add a contact\n'b' to add group\n'c' to browse users with group name\n'd' to browse groups with given user\n'e' to find users with keyword\n'f' to find user by email\n'q' to quit"
while True:
    choice=raw_input("Enter your choice\n")
    if choice == 'q':
        break
    elif(choice=='a'):
        ginger.add_contact()
    elif(choice=='b'):
        ginger.add_group()
    elif(choice=='c'):
        ginger.display_group()
    elif(choice=='d'):
        ginger.display_user_groups()
    elif(choice=='e'):
        ginger.find_user()
    elif(choice=='f'):
        ginger.find_user_mail()
    else:
        print "Incorrect choice. Need to enter the choice again"
        
