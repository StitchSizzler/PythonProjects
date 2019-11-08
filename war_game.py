"""
War (cards game) implementation 
"""
import random

def main():
    # prompt for file and read it
    input_file = input("Enter file name: ")
    deck = []
    user_deck = CircularQueue(52)
    computer_deck = CircularQueue(52)
    
    # try opening the file
    try:
        deck_file = open(input_file, "r")
    except:
        raise Exception("Input file not found")
    
    get_deck(deck_file, deck)    # validate cards
    divide_deck(deck, user_deck, computer_deck)    # distribute cards to user1 and user2
    war = prompt_for_war()  # input from user
    end_game = False
    cards_on_table = OnTable()
    
    # play game until over
    while not end_game:
        
        # place top card from each player to table
        card1 = user_deck.dequeue()
        cards_on_table.place(1, card1, False)    # player, card, hidden
        card2 = computer_deck.dequeue()
        cards_on_table.place(2, card2, False)    # player, card, hidden
        
        print(str(cards_on_table))  # display cards
        print("Player1: %d cards" % user_deck.size())
        print("Player2: %d cards" % computer_deck.size()) 
        input("Press Enter to continue \n")  
        
        # compare ranks
        higher = compare_cards(card1, card2)
        if higher == 1: # player 1 higher
            # give all cards to player 1
            cards = cards_on_table.clean_table() 
            for card in cards:
                user_deck.enqueue(card)
        elif higher == -1:   # player 2 higher
            # give all cards to player 2
            cards = cards_on_table.clean_table()             
            for card in cards:
                computer_deck.enqueue(card)  
        else:
            # WAR: both cards are equal rank
            print("WAR")
            
            face_down1 = True
            for i in range(war):    # get war cards from player 1
                if user_deck.isEmpty():
                    face_down1 = False
                else:
                    card = user_deck.dequeue()
                    cards_on_table.place(1, card, True)            
            if not face_down1:
                # if player 1 doesn't have enough cards
                cards = cards_on_table.clean_table()
                for card in cards:
                    computer_deck.enqueue(card)  # player 2 gets all cards from table
                print("Player 1 ran out of cards.")
                end_game = True     
            else:
                face_down2 = True
                for i in range(war):    # get war cards from player 2
                    if computer_deck.isEmpty():
                        face_down2 = False
                    else:
                        card = computer_deck.dequeue()
                        cards_on_table.place(2, card, True)
                if not face_down2:
                    # if player 2 doesn't have enough cards
                    cards = cards_on_table.clean_table()
                    for card in cards:
                        user_deck.enqueue(card)  # player 1 gets all cards from table
                    print("Player 2 ran out of cards")
                    end_game = True                    
        
        if user_deck.isEmpty() or computer_deck.isEmpty():  # check if anyone ran out of cards
            end_game = True
    
    if user_deck.size() > computer_deck.size(): # check for winner
        print("The user won")
    else:
        print("The computer won")
    deck_file.close()
        
def get_deck(deck_file, deck):
    # get cards and validate them
    for card in deck_file:
        card = card.upper()    # convert to upper case
        card = card.strip()
        # check if proper fromat (int/K/Q/J/A, char) and len=2
        length = len(card)==2
        if length:
            num = ((card[0]).isdigit()) or card[0]in["A","K","Q","J"]                         
            alpha = card[1]in["D","C","H","S"]
        if length and num and alpha:    # if all conditions met
            if card not in deck:
                deck.append(card)  
            else:
                raise Exception("Repeated card: %s" % card)
        else:
            
            if len(card)!=0:  # ignore blank lines
                raise Exception("Illegal card: %s" % card)
        # check if exactly 52 cards:
    if len(deck)!=52:
        # technically cannot happen if above exceptions work
        raise Exception("Illegal amount of cards")    
    
def divide_deck(deck, user_deck, computer_deck):
    # divide cards b/w user and player
    rand = random.randint(0,1)
    if rand == 1:
        user = True
    else:
        user = False
    for card in deck:
        if user:
            user_deck.enqueue(card)
            user = False
        else:
            computer_deck.enqueue(card)
            user = True
            
def prompt_for_war():
    # ask user to play war with 1, 2 or 3 cards
    valid = False
    while valid==False:
        war = input("Would you like to play a war with one, two, or three cards face-down?(1/2/3): ")
        if war in ["1","2","3"]:
            war = int(war)
            valid = True
        else:
            print("Please enter a number from 1-3.")
    return war

def compare_cards(first_card, second_card):
    # compare rank of two cards (the first character)
    # return 0 for equal
    # return 1 if first card is higher
    # return -1 if second card is higher
    cards = [first_card, second_card]
    card_ranks = [None, None]
    rank = {}   # dict to hold ranks of cards that are not int
    rank["A"] = 14
    rank["K"] = 13
    rank["Q"] = 12
    rank["J"] = 11
    rank["0"] = 10    # remember 0 is actually 10
    for card in range(len(cards)):  # make loop to advoid repeated code
        # get nth item's first character
        if cards[card][0].isdigit() and (cards[card][0]!="0"): # rank is 2-9
            card_ranks[card] = int(cards[card][0])
        elif cards[card][0] in rank:    # A,K,Q,J,or 10
            card_ranks[card] = rank[cards[card][0]]
        else:
            raise Exception("Unexpected programming error :( ")
    # compare ranks
    if card_ranks[0]>card_ranks[1]:
        return 1
    elif card_ranks[0]<card_ranks[1]:
        return -1
    elif card_ranks[0]==card_ranks[1]:
        return 0
    else:
        raise Exception("Unexpected error comparing cards")        
    
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class OnTable:
    
    # constructor, which creates a new object OnTable 
    def __init__(self):
        self.__cards = []
        self.__faceUp = []
        
    def place(self, player, card , hidden):
        # player1 cards added to front of list
        # player2 cards added to end of list   
        # add value of faceUp accourdingly 
        if hidden:
            self.up = False     # face-down
        else:
            self.up = True     # face-up        
        if player == 1:    # if player 1, add to front
            self.__cards.insert(0, card)
            self.__faceUp.insert(0, self.up)
        else:   # if player 2, add to back
            self.__cards.append(card)
            self.__faceUp.append(self.up) 
            
    def clean_table(self):
        # returns list of all cards in list __cards
        # all cards made face-up
        # reset __cards and __faceUp
        cards = self.__cards
        self.__cards = []
        self.__faceUp = []
        return cards
    
    def __str__(self):
        # string representation of cards on table
        # hidden cards displayed as XX
        str_exp = "["
        for index in range(len(self.__cards)):
            if index > 0:
                str_exp += ", "
            if self.__faceUp[index] == True:
                str_exp += self.__cards[index]
            else:
                str_exp += "XX"
        return str_exp + "]"        

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class CircularQueue:
    
    # a circular queue implementaion 
    # Constructor, which creates a new empty queue:
    def __init__(self, capacity):
        if type(capacity) != int or capacity<=0:
            raise Exception ("Capacity Error")
        self.__items = []
        self.__capacity = capacity
        self.__count=0
        self.__head=0
        self.__tail=0
        
    def enqueue(self, item):
        # Adds a new item to the back of the queue, and returns nothing        
        if self.__count== self.__capacity:
            raise Exception('Error: Queue is full')
        if len(self.__items) < self.__capacity:
            self.__items.append(item)
        else:
            self.__items[self.__tail]=item
        self.__count +=1
        self.__tail=(self.__tail +1) % self.__capacity

    def dequeue(self):
        # Removes and returns the front-most item in the queue.
        # Returns nothing if the queue is empty.        
        if self.__count == 0:
            raise Exception('Error: Queue is empty')
        item= self.__items[self.__head]
        self.__items[self.__head]=None
        self.__count -=1
        self.__head=(self.__head+1) % self.__capacity
        return item

    def peek(self):
        # Returns the front-most item in the queue, and DOES NOT change the queue.        
        if self.__count == 0:
            raise Exception('Error: Queue is empty')
        return self.__items[self.__head] 

    def isEmpty(self):
        # Returns True if the queue is empty, and False otherwise:        
        return self.__count == 0

    def isFull(self):
        # Returns True if the queue is full, and False otherwise:        
        return self.__count == self.__capacity

    def size(self):
        # Returns the number of items in the queue:        
        return self.__count

    def capacity(self):
        # Returns the capacity of the queue:        
        return self.__capacity   

    def clear(self):
        # Removes all items from the queue, and sets the size to 0
        # clear() should not change the capacity        
        self.__items = []
        self.__count=0
        self.__head=0
        self.__tail=0

    def __str__(self):
        # Returns a string representation of the queue:        
        str_exp = "]"
        i=self.__head
        for j in range(self.__count):
            str_exp += str(self.__items[i]) + " "
            i=(i+1) % self.__capacity
        return str_exp + "]"

    def __repr__(self):
        # Returns a string representation of the object CircularQueue
        return str(self.__items) + " H=" + str(self.__head) + " T="+str(self.__tail) + " ("+str(self.__count)+"/"+str(self.__capacity)+")"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
main()