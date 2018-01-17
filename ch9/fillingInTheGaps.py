# Find certain prefix such as spam1.txt, spam2.txt, and so on. 
# In a single folder and locates any gaps in the numbering 
# (such as if there is a spam1.txt and spam3.txt but no spam2.txt). 
# Have the program rename all the later files to close this gap.

# Two ways to accomplish this goal, 
# First is rename following file names to follow previous file number.
# Second is add new file name to fill up the gap.


import os, re, shutil

def fillupGaps(folder, fillup = 'rename'):
    #first parameter is folder path, second is the way to fill up gaps
    #Two option 'rename' and 'add'
    
    prefixReg = re.compile(r'''(
            (^spam)    #start with 'spam'
            (\d+)      #number
            (.*\.txt$) #end with '.txt'
    )''', re.VERBOSE)
    
    if fillup == 'rename':
        lastNum = 0;
        pstNum = 0;
        
        for filename in os.listdir(folder):
            #print(filename)
            result = prefixReg.findall(filename)
            #print(result)
            
            if result:
                pstNum = result[0][2]
                pass
                if pstNum != lastNum + 1:
                    newName = result[0][1] + str(lastNum+1) + result[0][3]
                    print(result[0][0] + ' modify to : ' + newName)
                    #shutil.move(result[0][0], newName)
                lastNum += 1
    elif fillup == 'add':
        pass
    else:
        print('Second parameter is invalid.')
        return
            
    
if __name__ == '__main__':
    fillupGaps('.')