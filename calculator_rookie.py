from Stack import Stack
def main():
    infix = input()
    postfix = []
    operator_tokens = "+-*/%" 
    digit_tokens = "123456789"    
    sorting_stack = Stack()
    answer = "nope"
    infix_to_postfix(infix, postfix, sorting_stack, operator_tokens, digit_tokens)
    print(postfix)
    while len(postfix) > 1: 
        for token in postfix:
            if str(token) in operator_tokens:
                operator = token 
                found2 = False
                i=1
                while not found2:
                    if str(postfix[postfix.index(token)-i]) in digit_tokens:
                        second = postfix.pop(postfix.index(token)-i)
                        found2 = True
                    else:
                        i += 1
                found1 = False
                while not found1:
                    if str(postfix[postfix.index(token)-i]) in digit_tokens:
                        first = postfix.pop(postfix.index(token)-1)
                        found1 = True
                    else:
                        i += 1
                answer = operation(int(first), int(second), operator)
                postfix[postfix.index(token)] = answer
    print(answer)
def operation(first, second, operator):
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        return first / second
    if operator == "%":
        return first % second
    
def infix_to_postfix(infix, postfix, sorting_stack, operator_tokens, digit_tokens):
    # determine precedence using dict
    precedence = {}
    precedence["("] = 1
    precedence["+"] = 2
    precedence["-"] = 2
    precedence["*"] = 3
    precedence["/"] = 3
    precedence["%"] = 3
    # get a string of allowed tokens
    infix_tokens = list(infix)
    for token in infix_tokens: 
        if token in digit_tokens:
            postfix.append(int(token))
        elif token == "(":
            sorting_stack.push(token)
        elif token == ")":  # add to stck if closing bracket
            recent_token = sorting_stack.pop()
            while recent_token != "(":  # add until ( found
                postfix.append(recent_token)
                recent_token = sorting_stack.pop()
        elif token in operator_tokens:
            while not sorting_stack.is_empty() and precedence[sorting_stack.peek()] >= precedence[token]:   # pop out operands with higher precedence 
                postfix.append(sorting_stack.pop())
            sorting_stack.push(token)   # add operand
    while not sorting_stack.is_empty():
        postfix.append(sorting_stack.pop()) # add elements from stack to postfix list
    return postfix

main()