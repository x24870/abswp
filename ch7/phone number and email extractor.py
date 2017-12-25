import re
import pyperclip

print('input str is : ', pyperclip.paste())

phoneNumRegex =  re.compile(r'\d{3}-\d{3}-\d{4}')
emailRegex = re.compile(r'[\w]+@[\w.]+')

phoneNum = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
email = emailRegex.findall('x24870@gmail.com and 1100105338@gm.kuas.edu.tw')

print(phoneNum)
print(email)

phoneNumOutput = ''
for item in phoneNum:
    phoneNumOutput = phoneNumOutput + item + '\n'
    
emailOutput = ''
for item in email:
    emailOutput = emailOutput + item + '\n'
    
print(phoneNumOutput, emailOutput)

pyperclip.copy(phoneNumOutput + emailOutput)

