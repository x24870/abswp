# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import re, shutil, os

usDatereg = re.compile(r"""                     # groupNum
    ^(.*?)           # all text before date       (1)
    ((0|1)?\d)-      # 1 or 2 digits for month    (2 (3)
    ((0|1|2|3)?\d)-   # 1 or 2 digits for day     (4 (5))              
    ((19|20)\d\d)    # 4 digits for year          (6 (7))
    (.*?)$            # all text after date       (8)
""", re.VERBOSE)

files = os.listdir()

print(files)

for file in files:
    usDate = usDatereg.search(file)
    print(usDate)
    if usDate:
        #change to eu date
        beforeDate = usDate.group(1)
        month = usDate.group(2)
        day = usDate.group(4)
        year = usDate.group(6)
        afterDate = usDate.group(8)
        
        euDate = beforeDate + day + '-' + month + '-' + year + afterDate
        
        print('Rename %s to %s' % (usDate.group(0), euDate))
        
        shutil.move(usDate.group(0), euDate)