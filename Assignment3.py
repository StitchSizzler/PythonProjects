import random


class OnTable:
    def __init__(self):
        self.__cards = []
        self.__faceUp = []

    def place(self, player, card, hidden):
        if player == 1:
            self.__cards.insert(0, card)
        else:
            self.__cards.append(card)
        self.__faceUp.append(hidden)

    def cleanTable(self):
        cards = list(self.__cards)
        self.__cards = []
        self.__faceUp = []
        return cards

    def getCards(self):
        return self.__cards

    def __str__(self):
        str_exp = "["
        for j in range(len(self.__cards)):
            if j != len(self.__cards)-1:
                if self.__faceUp[j]:
                    str_exp += str(self.__cards[j]) + ", "
                else:
                    str_exp += "XX"
            else:
                if self.__faceUp[j]:
                    str_exp += str(self.__cards[j])
                else:
                    str_exp += "XX"
        return str_exp + "]"

class CircularQueue:
    def __init__(self, capacity):
        if type(capacity) != int or capacity <= 0:
            raise Exception("CapacityError")
        self.__items = []
        self.__capacity = capacity
        self.__count = 0
        self.__head = 0
        self.__tail = 0

    def enqueue(self, item):
        if self.__count == self.__capacity:
            raise Exception('Error: Queue is full')

        if len(self.__items) < self.__capacity:
            self.__items.append(item)
        else:
            self.__items[self.__tail] = item
        self.__count += 1
        self.__tail = (self.__tail + 1) % self.__capacity

    def dequeue(self):
        if self.__count == 0:
            raise Exception('Error: Queue is empty')

        item = self.__items[self.__head]
        self.__items[self.__head] = None
        self.__count -= 1
        self.__head = (self.__head + 1) % self.__capacity
        return item

    def peek(self):
        if self.__count == 0:
            raise Exception('Error: Queue is empty')

        return self.__items[self.__head]

    def isEmpty(self):
        return self.__count == 0

    def isFull(self):
        return self.__count == self.__capacity

    def size(self):
        return self.__count

    def capacity(self):
        return self.__capacity

    def clear(self):
        self.__items = []

        self.__count = 0
        self.__head = 0
        self.__tail = 0

    def __str__(self):
        str_exp = "]"

        i = self.__head
        for j in range(self.__count):
            str_exp += str(self.__items[j]) + " "
        i = (i + 1) % self.__capacity
        return str_exp + "]"

def get_deck():
    valid_deck = False
    while not valid_deck:
        filename = input("Please enter the name of the file: ")
        try:
            deck_file = open(filename, 'r')
            deck = deck_file.read()
            deck_file.close()
            cards = deck.splitlines()
            valid_deck = True
        except:
            print("File not found.")
            valid_deck = False

        problem = False
        if len(cards) != 52:
            print("There are not enough cards in the deck, try again.")
            valid_deck = False
        if valid_deck:
            for c in cards:
                try:
                    if c[0] not in 'KQJA234567890':
                        valid_deck = False
                        problem = True
                    elif c[1] not in 'DCHS':
                        valid_deck = False
                        problem = True
                except:
                    valid_deck = False
                    problem = True
        if problem:
            print("There was a problem in the deck, please try again.")

    return(cards)

def deal_cards(deck):
    h1 = CircularQueue(52)
    h2 = CircularQueue(52)
    for c in deck[::2]:
        h1.enqueue(c)
    for c in deck[1::2]:
        h2.enqueue(c)
    n = random.randint(0, 1)

    if n == 0:
        return h1, h2
    else:
        return h2, h1

def compare(card1, card2):
    ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K', 'A')
    if ranks.index(card1[0]) > ranks.index(card2[0]):
        return 1
    elif ranks.index(card2[0]) > ranks.index(card1[0]):
        return -1
    else:
        return 0

def display(cardsOnTable, hand1, hand2):
    print(cardsOnTable)
    print("Player1: ", hand1.size(), " cards", sep='')
    print("Player2: ", hand2.size(), " cards", sep='')
    input("Press return key to continue.")

def game():
    deck = get_deck()
    hands = deal_cards(deck)
    p1_hand = hands[0]
    cpu_hand = hands[1]

    valid = False
    while not valid:
        war_value = input("How many cards would you like to play face down for a war?\n1. One card\n"
                              "2. Two cards\n3. Three cards\n")
        try:
            if war_value in '123':
                war_value = int(war_value)
                valid = True
        except:
            continue

    endGame = False
    cardsOnTable = OnTable()
    while not endGame:
        faceUp1 = p1_hand.dequeue()
        cardsOnTable.place(1, faceUp1, True)
        faceUp2 = cpu_hand.dequeue()
        cardsOnTable.place(2, faceUp2, True)
        display(cardsOnTable, p1_hand, cpu_hand)
        if compare(faceUp1, faceUp2) == 1:
            #print("p1 wins")
            for c in cardsOnTable.getCards():
                print(c)
                p1_hand.enqueue(c)
            #print(p1_hand)
            #print(cpu_hand)
        elif compare(faceUp1, faceUp2) == -1:
            #print("cpu wins")
            for c in cardsOnTable.getCards():
                cpu_hand.enqueue(c)
            #print(cpu_hand)
            #print(p1_hand)
        else:
            faceDown1 = []
            try:
                for _ in range(war_value):
                    faceDown1.append(p1_hand.dequeue())
            except:
                for c in cardsOnTable.getCards():
                    cpu_hand.enqueue(c)
                for c in p1_hand.size():
                    cpu_hand.enqueue(p1_hand.dequeue())
                endGame = True
            else:
                faceDown2 = []
                try:
                    for _ in range(war_value):
                        faceDown2.append(cpu_hand.dequeue())
                except:
                    for c in cardsOnTable.__cards:
                        p1_hand.enqueue(c)
                    for c in cpu_hand.size():
                        p1_hand.enqueue(cpu_hand.dequeue())
                    endGame = True

game()