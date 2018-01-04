import re
import pyperclip


#Taiwan phone number format
phoneNumRegex =  re.compile(r'''(
	(\d{2,3}|\(\d{3}\))? #area code
	(-|\s)? #separator
	(\d{6,7}) #phone number
)''', re.VERBOSE)
emailRegex = re.compile(r'[\w]+@[\w.]+')

text = '''
Cell: 035-456789 Work: (888) 459881, another num:133-789654, this is a nnum: (444)-444444, Taiwan num: 12-3456789
x2487e2515s0@gmail.com and g04473@gm.ccu.edu.tw
'''

phoneNumOutput = ''
for item in phoneNumRegex.findall(text):
    phoneNumOutput = phoneNumOutput + item[1].strip('()') + '-' +  item[3] + '\n'
    
emailOutput = ''
for item in emailRegex.findall(text):
    emailOutput = emailOutput + item + '\n'
    
print("Phone Numbers: \n", phoneNumOutput, "\nEmails: \n", emailOutput)

pyperclip.copy(phoneNumOutput + emailOutput)

