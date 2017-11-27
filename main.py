def collatz_sequence():
    num = input("Please enter an positive integer\n")
    
    print(num.isdigit())
    
    while not num.isdigit():
        num = input("Invalid input, please re-enter.\n")
    else:
        print("Input number is: ", num)
        num = int(num)
        
    while num > 1:
        if num % 2:
            num = num * 3 + 1
        else:
            num /= 2
        print(num)


collatz_sequence()            
    