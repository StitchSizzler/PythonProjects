from d_linked_node import d_linked_node

class d_linked_list:
    
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0        

            
    def search(self, item):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
        return found
        
    def index(self, item):
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
                index = -1
        return index        
         
    def add(self, item):
        # add item to beginning of list (index 0)
        temp = d_linked_node(item, self.__head, None)
        if self.__head != None: # if list is not empty
            self.__head.setPrevious(temp)   # add temp to front
        else:   # if list is empty, head is also the tail
            self.__tail = temp
        self.__head = temp  # new item is head cuz we're adding to front
        self.__size += 1
        
    def remove(self, item):
        # searches item and removes it
        current = self.__head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if found:
            if previous == None:    # if the index is 0, set a new head
                self.__head = current.getNext()
            else:
                previous.setNext(current.getNext()) # previous points to item after current (so current can be ignored and removed)
            if (current.getNext() != None): # if NOT removing the last item
                current.getNext().setPrevious(previous) # remove node from current so it can be ignored and deleted
            else:
                self.__tail = previous    # if nothing after current (current is last item) and current gets removed, the previous one will be last item
            self.__size -= 1
        
    def append(self, item):
        # adds item to the end of list
        temp = d_linked_node(item, None, None)
        if (self.__head == None):
            self.__head = temp
        else:
            self.__tail.setNext(temp)
            temp.setPrevious(self.__tail)
        self.__tail = temp
        self.__size += 1
        
    def insert(self, pos, item):
        assert pos <= self.get_size(), "Error in insert: position exceed limit"
        current = self.__head
        previous = None
        temp = d_linked_node(item, None, None)
        if (self.__head == None):
            self.__head = temp
            self.__tail = temp
        else:   # find position to add item
            i = 0
            while i != pos:
                previous = current
                current = current.getNext()
                i += 1
            if previous == None:
                self.__head = temp
            else:
                previous.setNext(temp)
                temp.setPrevious(previous)
            if current == None:
                self.__tail = temp
            else:
                temp.setNext(current)
                current.setPrevious(temp)
        self.__size += 1
  
    def pop1(self):
        # removes and returns the last item in the list
        temp = self.__tail
        previous = temp.getPrevious()
        self.__tail = previous
        if previous != None:
            previous.setNext(None)
        temp.setPrevious(None)
        self.__size -= 1
        return temp.getData()
        
    def pop(self, pos):
        assert pos < self.get_size(), "Error in pop: position exceed limit"
        assert self.get_size() != 0, "Error in pop: list is empty"
        current = self.__head
        previous = None
        i = 0
        while i != pos:    # find position to pop item
            previous = current
            current = current.getNext()
            i += 1
        if current == None:
            after = None
        else:
            after = current.getNext()
        if previous == None:
            self.__head = after
            after.setPrevious(None)
        else:
            if after == None:
                self.__tail = previous
                previous.setNext(None)
            else:
                previous.setNext(after)
                after.setPrevious(previous) 
        if current != None:
            current.setNext(None)
            current.setPrevious(None)
        self.__size -= 1
        return current.getData()
        
        
        
    def search_larger(self, item):
        current = self.__head
        found = False
        pos = 0
        while current != None and not found:
            if current.getData() > item:
                found= True
            else:
                current = current.getNext()
                pos += 1
        if not found:
                pos = -1
        return pos               
        
    def get_size(self):
        return self.__size    
    
    def get_item(self, pos):
        if pos>=0:
            assert pos<self.get_size(), "IndexError: position does not exist" 
            current = self.__head
            i = 0
            while i != pos:    # find position
                current = current.getNext()
                i += 1  
        else:
            pos = pos*-1
            assert pos<=self.get_size(), "IndexError: position does not exist" 
            current = self.__tail
            i = 1
            while i!= pos:
                current = current.getPrevious()
                i += 1
        return current.getData()
        
    def __str__(self):
        s= ""
        i=0
        current=self.__head
        while current != None:
            if i>0:
                s = s + ' '
            dataObject = current.getData()
            if dataObject != None:
                s = s + "%s" % dataObject
                i = i + 1
            current = current.getNext()
        return s         
        

def test():
                  
    linked_list = d_linked_list()
                    
    is_pass = (linked_list.get_size() == 0)
    assert is_pass == True, "fail the test"
            
    linked_list.add("World")
    linked_list.add("Hello")    
        
    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"    
              
    is_pass = (linked_list.get_size() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.get_item(0) == "Hello")
    assert is_pass == True, "fail the test"
        
        
    is_pass = (linked_list.get_item(1) == "World")
    assert is_pass == True, "fail the test"    
            
    is_pass = (linked_list.get_item(0) == "Hello" and linked_list.get_size() == 2)
    assert is_pass == True, "fail the test"
    
    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.pop1() == "Hello")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.get_size() == 0)
    assert is_pass == True, "fail the test" 
                    
    int_list2 = d_linked_list()
                    
    for i in range(0, 10):
        int_list2.add(i)      
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"
                
    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    for i in range(21, 23):
        int_list2.insert(0,i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    is_pass = (int_list2.get_size() == 10)
    assert is_pass == True, "fail the test"    
                    
    int_list = d_linked_list()
                    
    is_pass = (int_list.get_size() == 0)
    assert is_pass == True, "fail the test"
                    
        
                    
    for i in range(0, 1000):
        int_list.append(i)      
    correctOrder = True
            
    is_pass = (int_list.get_size() == 1000)
    assert is_pass == True, "fail the test"            
            
        
    for i in range(0, 200):
        if int_list.pop1() != 999 - i:
            correctOrder = False
                            
    is_pass = correctOrder
    assert is_pass == True, "fail the test" 
            
    is_pass = (int_list.search_larger(200) == 201)
    assert is_pass == True, "fail the test" 
            
    int_list.insert(7,801)   
        
    is_pass = (int_list.search_larger(800) == 7)
    assert is_pass == True, "fail the test"
            
            
    is_pass = (int_list.get_item(-1) == 799)
    assert is_pass == True, "fail the test"
            
    is_pass = (int_list.get_item(-4) == 796)
    assert is_pass == True, "fail the test"
                    
    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 1! ============")
                
if __name__ == '__main__':
    test()