''' 
 This program reads books.txt and members.txt
 to get information about unreturned books from books.txt
 and get member's names from thier phone number using members.txt
 The program calculates the penalty for each culprit member 
 according to overdue days. 
 The program prints and records the data to summary.txt which includes
 culprit phone number, their name, total penalty issued,
 book code, and no.of days overdue 
'''

from datetime import date
def main():
    books_file = open("books.txt", "r")
    members_file = open("members.txt", "r")
    summary_file = open("summary.txt", "w")
    culprits_data = {}
    members_phone = {}
    summary = []
    today = date(2018,1,19)
    
    # read and store lines from books_file
    books_data = []
    for line in books_file:
        books_data.append(line)
        
    # get info from books_data
    for data in books_data: 
        # get book_code, book_price, member's ph no.
        # split date into year, month, day         
        data = data.strip("\n")
        code, price, due_date, phone_number = data.split(";")
        price = float(price)
        year, month, day = due_date.split("/")
        due_date = date(int(year), int(month), int(day))    # due_date into int 
        overdue_days = (today-due_date).days
        
        # decide penalty
        if overdue_days>0:
            penalty = overdue_days*0.25
        if overdue_days>90:
            penalty += price    # add full book price
        # store book info and price
        book_info = [penalty, price, overdue_days, code]
        
        # add book info to culprits_data dictionary 
        # using phone no. as key
        if phone_number not in culprits_data:
            culprits_data.update({phone_number : [book_info]})
        elif phone_number in culprits_data:
            culprits_data[phone_number].append(book_info)
        else:   # technically shouldn't happen
            print("Error: programing error adding phone#: " + phone_number)
    
    # read and store lines from members_file
    members_data = []
    for line in members_file:
        members_data.append(line)     
    # get info from members_data
    # add phone:name to members_phone dict
    for data in members_data:
        phone_number, member_name, address = data.split(",")
        members_phone.update({phone_number : member_name})
        
    # organize according to phone number 
    total_dues = 0
    for phone_number, all_data in culprits_data.items():
        all_books = ""
        penalty = 0
        for entry in all_data:
            # entry[3] is book code
            # entry[2] is over due days 
            to_add = "[%s](%d days); " % (entry[3], entry[2])
            all_books += to_add
            penalty += entry[0]
        # get member name from phone no.
        member_name = members_phone[phone_number]        
        # format phone no. to (xxx) xxx xxx
        phone_head = phone_number[:3]
        phone_middle = phone_number[3:6]
        phone_tail = phone_number[6:]
        phone_number = "(%s) %s %s" % (phone_head, phone_middle, phone_tail) 
        all_info = "|%s|%-30s|$%7.2f|%s" % (phone_number, member_name, penalty, all_books)
        total_dues += penalty
        summary.append(all_info)
    margin = "+--------------+------------------------------+--------+"
    header = "|%s|%-30s|%-8s|" % (" Phone Number ", " Name", " Due")
    footer = "|%s|%30s %8.2f|" % (" Total Dues   ", " $", total_dues)
    
    # sort entries is summary according to phone no.
    # print and write to summary_file
    summary.sort(key=lambda s: s.split()[1])    # sort using element at index 1
    print("%s \n%s \n%s" % (margin, header, margin))
    summary_file.write("%s \n%s \n%s \n" % (margin, header, margin))
    for entry in summary:
        print(entry)
        summary_file.write("%s\n" % entry)
    print("%s \n%s \n%s" % (margin, footer, margin))
    summary_file.write("%s \n%s \n%s" % (margin, footer, margin))
   
    books_file.close()
    members_file.close()
    summary_file.close

main()