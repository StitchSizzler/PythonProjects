
import random
import webbrowser

def main():
    
    valid = False
    while valid == False:
        user = input("Enter a number: ")
        try:
            user = int(user)
            valid = True
        except:
            pass
        
    #webbrowser.open("https://en.wikipedia.org/wiki/Main_Page")
    
    """
    aList = [0, 1, 2, 3, 4]
    aList.reverse()
    print(type(aList))
    """
    '''
    try:
        print(1/1)
        print("This is ignored")
    except KeyError:
        print("ignore")
    except ZeroDivisionError as e:
        print("Argument invalid:", e)
    else:
        print("This shouldn't run?")
    finally:
        print("This is good")
    print("I guess this is still supposed to run???")
       ''' 
    
'''
    date = "2018/01/12"
    y,m,y = date.split("/")
    print(y)
    
    nums = "123"
    nums = nums*3
    print(nums)

    animal = "is cat"
    new_cat = Kitty(animal)
    new_cat.type_of_kitty()
    
class Kitty:
    def __init__(self, cat):
        self.cat = cat
    def type_of_kitty(self):
        print("Nyan Cat", self.cat)
        
    text = "7802002990"
    phone_head = text[:3]
    phone_middle = text[3:6]
    phone_tail = text[6:]
    phone_no = "(%s) %s %s" % (phone_head, phone_middle, phone_tail)
    phone_no = "%-30s" % phone_no
    cat = "dyusfyfyjfdgdjdjhyj"
    cat = "%-30s" % cat
    print(phone_no, 123)
    print(cat, 123)
    
    board = [0, 1, 2, 3, 4, "x", "x", 7, 8, 9]
    ch = "x"
    ans = test(ch, board)
    print(ans)
    
def test(ch, board):
    ch=ch
    board=board
    win = False
    # check horizontal win
    i=9
    while i>0:
        if ch==board[i-2]==board[i-1]==board[i]:
            win = True
            return win
        else:
            i -= 3
    return win

    # check vertical win
    i=9
    while i>0:
        if ch==board[i]==board[i-3]==board[i-6]:
            win = True
            return win
        else:
            i-=1
    # check diagonal win:
    i=9
    if ch==board[i]==board[i-4]==board[i-8]:
        win = True
        return win
    elif ch==board[i-2]==board[4]==board[i-6]:
        win = True
        return win
    else:
        return win  
'''


main()

