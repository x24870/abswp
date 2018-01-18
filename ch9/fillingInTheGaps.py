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
    
    #get matched filenames
    matchedlist = []
    for filename in os.listdir(folder):
        matched = prefixReg.findall(filename)
        if matched: matchedlist.append(matched[0]) 
    matchedlist = sorted(matchedlist, key=lambda matchedlist:int(matchedlist[2])) 
    print(matchedlist)                   

    if fillup == 'rename':
        lastNum = 0;
        pstNum = 0;
        
        for matched in matchedlist:
            pstNum = int(matched[2])
            if pstNum != lastNum + 1:
                newName = matched[1] + str(lastNum+1) + matched[3]
                print(matched[0] + ' modify to : ' + newName)
                #shutil.move(matched[0], newName)
            lastNum += 1
    elif fillup == 'add':
        presentNum = 1
        
        for matched in matchedlist:
            while(int(matched[2]) > presentNum):
                newFilename = matched[1] + str(presentNum) + matched[3]
                print('Add new file : ' + newFilename)
                #with open(newFilename, 'w') as file: pass
                presentNum += 1
            presentNum += 1
    else:
        print('Second parameter is invalid.')
        return
            
    
if __name__ == '__main__':
    fillupGaps('.')
