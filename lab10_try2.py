"""
This is a merge sort implementation.
Also returns the number of reverse lists
in the original list
Does not use any outside class
"""
def main():
    alist =[1, 2, 10, 4, 5, 8, 7]
    alist, inversions = mergeSort(alist,0)
    print(alist)
    print(inversions)


def mergeSort(data, inversions):
    # Sort using a merge sort
    if len(data) <=1:
        return data, inversions # cannot divide the list more
    middle = len(data)//2   # divide list into 2
    left, inversions = mergeSort(data[:middle], inversions)
    right, inversions = mergeSort(data[middle:], inversions)
    return merge(left,right,inversions)   # sort and merge

def merge(left,right, inversions):
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
            inversions += len(left)-i
            j+=1
    result += left[i:]
    result += right[j:]
    return result, inversions



main()