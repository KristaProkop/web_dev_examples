import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
from bs4 import BeautifulSoup, SoupStrainer
import pprint

url = urllib2.urlopen("http://www.codingdojo.com/").read()
soup = BeautifulSoup(url, "html.parser")

mylist = []
for line in soup.find_all('a'):
    mylist.append((line.get('href')))

# print mylist
dictionary = dict()
for i in range(len(mylist)):
    dictionary[mylist[i]] = mylist.count(mylist[i])

for key in dictionary:
    print key, ":", dictionary[key]

# myset = set(mylist)
# print list(myset)

#print soup.prettify()
## links = SoupStrainer('a')
# print links

# print soup.title
# link_list = soup.find_all('a')

# myset = set(link_list)
# print myset