import re

def strongPasswordDetection():
    #let user enter passward
    password = input('''Please enter a password with at least one number,
                     one upper charactor and one lower charactor.\n''')
    
    print('entered password: ', password)
    
    #check password
    numRegex = re.compile(r'[0-9]')
    upperRegex = re.compile(r'[A-Z]')
    lowerRegex = re.compile(r'[a-z]')
    
    number = numRegex.findall(password)
    upperChar = upperRegex.findall(password)
    lowerChar = lowerRegex.findall(password)
    
    if not number:
        print('You must enter a number at least.')
        return 0
    elif not upperChar:
        print('You must enter a upper charactor at least.')
        return 0
    elif not lowerChar:
        print('You must enter a lower charactor at least.')
        return 0
    else:
        print('Strong password!')
        return 1

if __name__ == '__main__':
    print(strongPasswordDetection())