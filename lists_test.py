#lists
'''
def main():
    list1 = ['cat', 'dog', 'mouse', 'rabbit', 'parrot']
    
    for animal in list1:
        print(animal)
        
    print('********************')
        
    for i in range(4):
        print(i, list1[i])
    
main()
'''

def main():
    
    num = 4
    ans = SomeAlgorithm(num)
    print(ans)
    


def SomeAlgorithm(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        ans1 = SomeAlgorithm(num-1)
        ans2 = SomeAlgorithm(num-2)
        ans3 = 2*ans1 + ans2                 
        return ans3
    
main()