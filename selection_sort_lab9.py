"""
This program runs two implementaion 
of selection sort, one with recursion
and another without, and compares their runtime 
"""
import time

def main():
    input_list = [300, 293, 286, 279, 272, 265, 258, 251, 244, 237, 230, 223, 216, 209, 202, 195, 188, 181, 174, 167, 160, 153, 146, 139, 132, 125, 118, 111, 104, 97, 90, 83, 76, 69, 62, 55, 48, 41, 34, 27, 20, 13, 6, 0]   
    
    # analyse time for recursion
    n = 1000
    totalTimeBounded = 0.0
    for i in range(20):
        start = time.time()
        for x in range(500):
            input_list1 = list(input_list)            
            recursion_sort(input_list1, len(input_list1) -1 )
        end = time.time()
        print("Recursive selection sort required %10.7f seconds"%(end-start))
        totalTimeBounded=totalTimeBounded+end-start
    print("the average time for recursive selection sort was %10.7f for n=%d"%(totalTimeBounded/20,n))   
    
    # analyse time for non-recursive
    n = 1000
    totalTimeBounded = 0.0
    for i in range(20):
        start = time.time()
        for x in range(500):
            input_list2 = list(input_list)            
            textbook_sort(input_list2, len(input_list2) -1 )
        end = time.time()
        print("Non-recursive selection sort required %10.7f seconds"%(end-start))
        totalTimeBounded=totalTimeBounded+end-start
    print("the average time for non-recursive selection sort was %10.7f for n=%d"%(totalTimeBounded/20,n))      
            

def recursion_sort(input_list, current_index): # sorting backward
    if (current_index == 0):  # return if reached the first position 
        return
    else:
        largest = max(input_list[:current_index + 1])   # ingore last elements that are already sorted
        index_largest = input_list.index(largest)
        if largest == input_list[current_index]:    # pass if element already in right position 
            pass
        else:   # switch elements
            temp = input_list[current_index]
            input_list[current_index] = largest
            input_list[index_largest] = temp            
        current_index -= 1
        recursion_sort(input_list, current_index)   # repeat until reach first index (backward)
        
def textbook_sort(input_list, current_index):
    # implementation from the textbook 
    for fillslot in range(len(input_list)-1,0,-1):
        if (current_index == 0):  # return if reached the first position 
            return  
        else:
            largest = max(input_list[:current_index + 1])   # ingore last elements that are already sorted
            index_largest = input_list.index(largest)
            if largest == input_list[current_index]:    # pass if element already in right position 
                pass
            else:   # switch elements
                temp = input_list[current_index]
                input_list[current_index] = largest
                input_list[index_largest] = temp         
            current_index -= 1  
            

main()