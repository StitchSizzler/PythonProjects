# this program adds all the elements in an array recursively 

def main():
    an_array = [5, 7, 2, 4]
    index = len(an_array)-1
    print(index)
    sum = get_sum(an_array, index)
    print(sum)

def get_sum(an_array, index):
    sum = 0
    if index == 0:
        return an_array[index]
    if index > 0:
        sum = an_array[index] + get_sum(an_array, index-1)
    return sum

main()