#password 

PASSWORD = {'email':'emailpassword',
            'cloud drover':'clouddriverpassword',
            'blog':'blogpassword'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('Usage: py.pw [account] - copy the password to clipboard')
    sys.exit()
    
account = sys.argv[1]
    
if account in PASSWORD:
    pyperclip.copy(PASSWORD.get(account))
    print('Password for' + account + 'has copied to clipboard')
else:
    print("can't find correspoind value")