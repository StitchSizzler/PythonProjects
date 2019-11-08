def main():
    terms = 9
    x = 0
    y = 1
    count = 0
    if terms < 1:
        print("...")
    elif terms == 1:
        print("the answer is ", x)  # ans = 0
    else:
        while count < terms:
            result= x+y
            x = y
            y = result
            count += 1
        print("the answer is ", result)
        
main()