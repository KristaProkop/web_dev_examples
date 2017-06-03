# helper = PaginationHelper(['a','b','c','d','e','f'], 4)
# helper.page_count # should == 2
# helper.item_count # should == 6
# helper.page_item_count(0)  # should == 4
# helper.page_item_count(1) # last page - should == 2
# helper.page_item_count(2) # should == -1 since the page is invalid

# # page_index takes an item index and returns the page that it belongs on
# helper.page_index(5) # should == 1 (zero based index)
# helper.page_index(2) # should == 0
# helper.page_index(20) # should == -1
# helper.page_index(-10) # should == -1 because negative indexes are invalid

class PaginationHelper:
  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
    self.collection = collection
    self.items_per_page = items_per_page
    
  # returns the number of items within the entire collection
  def item_count(self):
    return len(self.collection)
    
  
  # returns the number of pages
  def page_count(self):
    pages = divmod(self.item_count(), self.items_per_page)
    if pages[1] > 0:
      page_count = pages[0]+1
    else: 
      page_count = pages[0]
    return page_count

    
    
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self, page_index):
    page_item_count = -1 if page_index >= self.page_count() else len(self.page_dictionary()[page_index])
    return page_item_count

    # if page_index >= self.page_count():
    #   return -1
    # elif page_index == self.page_count() - 1:
    #   return len(self.collection) % self.items_per_page or self.items_per_page
    # else:
    #   return self.items_per_page
        
      
      
  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
    dictionary = self.page_dictionary()
    if item_index > -1 and item_index <= len(self.collection)-1:
      item = self.collection[item_index] 
      return [key for key, val in dictionary.iteritems() if item in val][0]
    else:
      return -1
      
  def page_dictionary(self):
    page_contents = [self.collection[x:x+self.items_per_page] for x in xrange(0, len(self.collection), self.items_per_page)]
    dictionary = dict(zip(range(0, self.page_count()), page_contents))
    return dictionary

collection = range(1,32)
helper = PaginationHelper(collection, 3)

print helper.page_count()
print helper.page_index(30)
print helper.item_count()