
from CircularQueue import CircularQueue

def main():
    # create queues
    regular_lineup = CircularQueue(3)
    vip_lineup = CircularQueue(3)
    action = ""
    while action.lower() != "exit":
        # get action
        action = input("Add, Serve, or Exit: ")
        # add customer to queue
        if action.lower() == "add":
            add(vip_lineup, regular_lineup)
        elif action.lower() == "serve":
            serve(vip_lineup, regular_lineup)
            
        print("people in the line: " + str(regular_lineup))
        print("VIP customers queue: " + str(vip_lineup) + "\n")
    
    print("Quitting")
            
            
def add(vip_lineup, regular_lineup):
    name = input("Enter the name of the person to add: ")
    vip = input("Is the customer VIP?(True/False): ")
    assert vip.lower()=="true" or vip.lower()=="false", ("Error: invalid input")
    if vip.lower() == "true":
        if not vip_lineup.isFull(): 
            vip_lineup.enqueue(name)
            print("add " + name + " to VIP line")
        else:
            print("Error: VIP lineup is full")                    
    else:
        if not regular_lineup.isFull():
            regular_lineup.enqueue(name)
            print("add " + name + " to the line")
        else:
            print("Error: normal customers' queue is full")   
            
def serve(vip_lineup, regular_lineup):
    if not vip_lineup.isEmpty():
        name = vip_lineup.dequeue()
        print(name + " has been served")
    elif not regular_lineup.isEmpty():
        name = regular_lineup.dequeue()
        print(name + " has been served")
    else:
        print("Error: queues are empty")

main()