# Ginger Payments test

## Architecture of the project
The project contains 3 folders:
* data
this folder contains address_book_file JSON file containing the collection
* lib
This folder contains ginger Python file. It represents the requested lib
* test
This folder contains unittest 

## Library
The library is available in lib folder
* add_contact
permits to add a contact with its different attributes
* add_group
permits to add a group to list
* display_group
permits to get users that belong to an input group
* display_users_group
permits to get group list of a specific user
* find_user
permits to find a user with its firstname or lastname 
* find_user_mail
permits to find users with the mail

## Case study
To find a user with a keyword that can be foundin his mail, we should clean its mails and concat it to a string
```
list = [email.replace('@',' ').replace('.',' ').replace('-',' ').replace('_',' ').split() for email in emails] 
mails_string = ''.join(list)
if keyword in mails_string:
	do stuff
```

## Running the script
simply download the repository, and launch ``` python script.py ``` available in base folder
it would call the library and let you choose what task you would like to do

## Thank you for this assignement, shall I expect a positive reply from your part
