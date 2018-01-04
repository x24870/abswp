import re
import pyperclip

#inputStr = pyperclip.paste()
#print('input str is : \n', inputStr)


phoneNumRegex =  re.compile(r'''(
	(\d{3}|\(\d{3}\))? #area code
	(-|\s)? #separator
	(\d{6}) #phone number
)''', re.VERBOSE)
emailRegex = re.compile(r'[\w]+@[\w.]+')


phoneNum = phoneNumRegex.findall('Cell: 035-456789 Work: (888) 459881')
email = emailRegex.findall('x24870@gmail.com and 1100105338@gm.kuas.edu.tw')

print(phoneNum)
print(email)

phoneNumOutput = ''
for item in phoneNum:
    phoneNumOutput = phoneNumOutput + item[0] + '\n'
    
emailOutput = ''
for item in email:
    emailOutput = emailOutput + item + '\n'
    
print("Phone Numbers: \n", phoneNumOutput, "\n Emails: \n", emailOutput)

pyperclip.copy(phoneNumOutput + emailOutput)

