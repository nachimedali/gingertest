import json

address_book_file=open("../data/address_book_file.json","r")
list_contacts=json.load(address_book_file)

k= mail_adress = ', '.join(list_contacts["users"]["1"]["email"])
# print k
if "sd" in k:
	print "yalla"

[m.replace('@',' ').replace('.',' ').replace('-',' ').split() for m in list_contacts["users"][users]["email"]][0]