'''
This prgram runs a calculator. The input expressions
are extracted from a file and the infix is first 
converted to postfix using a stack. Another stack is
then used to do the math. Details of algorithm can 
be found in the lecture notes. 
'''

from Stack import Stack
def main():
    input_file = open("math_input_file.txt", "r")
    # read file line by line
    for expression in input_file:
        # remove \n form end of every line 
        infix = expression.strip()
        print("input expression:", infix)
        postfix = []
        operator_tokens = "+-*/%" 
        digit_tokens = "123456789"    
        sorting_stack = Stack()
        answer = "error"
        infix_to_postfix(infix, postfix, sorting_stack, operator_tokens, digit_tokens)
        print(postfix)
        answer = evaluation(postfix, operator_tokens, digit_tokens)
        print("answer:", float(answer), "\n")
    
def evaluation(postfix, operator_tokens, digit_tokens):
    op_stack = Stack()
    # deal with each character
    for token in postfix:
        # check if character is an operand
        # push operand to stack
        if str(token) in digit_tokens:
            op_stack.push(token)
        # check if character is an operator 
        # pop operands from stack to evaluate 
        elif token in operator_tokens:
            second = op_stack.pop()
            first = op_stack.pop()
            answer = operation(first, second, token)
            # push result to stack
            op_stack.push(answer)
    return op_stack.pop()
    
def operation(first, second, operator):
    # do math
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