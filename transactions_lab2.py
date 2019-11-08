# This program reads accounts.txt file
# and performs requested transactions
# that are also valid
# until the user types Stop

def main():
    
    # check if file exists 
    try:
        # read and store data by line        
        accounts_file = open("accounts.txt", "r")
        all_accounts = {}
        for line in accounts_file:
            line.strip()
            account_name, current_amount = line.split(":")
            #check if amount is float
            try:
                current_amount = float(current_amount)
                all_accounts.update({account_name:current_amount})
            except ValueError:
                pass
        
        # perform transactions
        continue_program = True
        input_name = ""
        while continue_program==True:
            input_name = input("Enter account name, or 'Stop' to exit: ")
            if input_name in all_accounts:
                input_amount = input("Enter transaction amount: ")
                try:
                    input_amount = float(input_amount)
                    current_amount = all_accounts.get(input_name) + input_amount
                    print("New balance for account %s: %0.2f" % (input_name, current_amount))                
                    all_accounts.update({input_name:current_amount})
                except ValueError:
                    print("Illegal value for transaction, transaction canceled")
            elif input_name.lower() == "stop":
                continue_program = False
            else:
                print("Account does not exist, transaction canceled")
                
        accounts_file.close()
            
    except:
        print(" File does not exist")

main()