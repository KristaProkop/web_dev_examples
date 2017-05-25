import csv     # imports the csv module
from collections import OrderedDict

with open("csvfile.csv", "r") as file_var:
    reader = csv.reader(file_var)
    my_list = []
    for row in reader:
        if (len(row)!=0):
            my_list = my_list + [row]

for i in range(1, len(my_list)):
    user = OrderedDict(zip(my_list[0], my_list[i]))
    print "----------------------"
    print user['first_name'], user['last_name']
    for key in user:
        print key + ":", user[key]
