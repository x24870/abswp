#Find the password of an encrypted pdf file by brute-force method
#The password must be a word
#This program will read in a dictionary and try every word to decrypt the pdf file
#Usage: python bruteForcePdfPwBreaker.py PDF_FILE

import PyPDF2, sys

def pdfPwBreaker(pdfFileName):
    with open(pdfFileName, 'rb') as pdfFile:
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        
        with open('dictionary.txt', 'r') as dictionary:
            content = dictionary.readlines()
            
            for word in content:
                if word.endswith('\n'): word = word[:-1]
                if pdfReader.decrypt(word.upper()) == 1:
                    print('The password of {} is {}'.format(pdfFileName, word.upper()))
                    break
                elif pdfReader.decrypt(word.lower()) == 1:
                    print('The password of {} is {}'.format(pdfFileName, word.lower()))
                    break
                else:
                    print('{} fail'.format(word))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python bruteForcePdfPwBreaker.py PDF_FILE')
    elif not sys.argv[1].endswith('.pdf'):
        print('Only support .pdf file')
    else:
        pdfPwBreaker(sys.argv[1])

                    
