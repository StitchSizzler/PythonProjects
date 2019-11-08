'''
This program allows a user to "surf" the web.
= to enter address. > to go forward < to go back
same rules as Chrome/Firefox apply
'''
from Stack import Stack     # call Stack class from Stack.py

def main():
    first_stack = Stack()
    second_stack = Stack()
    home = "www.cs.ualberta.ca"
    first_stack.push(home)  # set home page
    #print(first_stack.peek())
    print("[%s]" % home)
    gone_back = False
    web_address = ""
    start = True
    while True:
        action = input()        
        # check action requested and if valid
        if action == "=":
            if not second_stack.is_empty():
                if gone_back == True:   
                    # bring last item (aka current page) 
                    # from second_stack to first_stack
                    # because don't want to delete current page
                    popped = second_stack.pop()
                    first_stack.push(popped)
                second_stack.make_empty()   # delete all 'forward' history
            web_address = input()
            print("[%s]" % web_address)
            first_stack.push(web_address)
            start = False
        elif action == "<" and not first_stack.is_empty():
            gone_back = True
            popped = first_stack.pop()
            second_stack.push(popped)            
            if popped == web_address and not first_stack.is_empty():   # don't print current page again
                popped = first_stack.pop()
                second_stack.push(popped)  
            web_address = popped
            if not start:  
                print("[%s]" % popped)
            else:
                print(action, "is an invalid action")      
        elif action == ">" and not second_stack.is_empty():
            gone_back = False
            popped = second_stack.pop()
            first_stack.push(popped)
            if popped == web_address and not second_stack.is_empty():   # don't print current page again
                popped = second_stack.pop()
                first_stack.push(popped)  
            web_address = popped 
            if popped != home:
                print("[%s]" % popped)
            else:
                print(action, "is an invalid action")                  
        else:
            print(action, "is an invalid action")  
        
        
        
main()



'''    WITHOUT STACKS
def main():
    history = ["www.cs.ualberta.ca"]
    current_index = 0   # index of current web address in list
    print(history[current_index])
    while True:
        action = input()
        history_length = len(history)        
        # check action requested and if valid
        if action == "=":
            web_address = input()
            if history_length>current_index+1:
                index_to_pop = history_length - current_index 
                for i in range(index_to_pop - 1):
                    history.pop()                
            history.append(web_address)
            current_index += 1   
            print("[%s]" % history[current_index])
        elif action == "<" and current_index>0:
            current_index -= 1
            print(history[current_index])
        elif action == ">" and current_index<history_length-1:
            current_index += 1
            print(history[current_index])
        else:
            print(action, "is an invalid action")
        
    
main()
'''