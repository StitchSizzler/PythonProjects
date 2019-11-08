"""
This is a merge sort implementation.
Also returns the number of reverse lists
in the original list 
Uses class to keep track of count
""" 
def main():
    count = Count()
    alist = [1, 2, 10, 4, 5, 8, 7]
    alist = mergeSort(alist, count)
    print(alist)
    print(count.getCount())

def mergeSort(data, count):
    # Sort using a merge sort
    if len(data) <=1:
        return data # cannot divide the list more
    middle = len(data)//2   # divide list into 2
    left = mergeSort(data[:middle], count)
    right = mergeSort(data[middle:], count)
    return merge(left,right,count)    # sort and merge

def merge(left,right, count):
    # sort and merge
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right): # iterate len of the smaller list 
        # (data from the remaining (long) list is then copied as it is)
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            inver = len(left)-i
            count.addCount(inver)
            j+=1
    result += left[i:]
    result += right[j:]
    return result

class Count:
    
    def __init__(self):
        self.inversions = 0
    
    def addCount(self, count):
        self.inversions += count
    
    def getCount(self):
        return self.inversions

main()