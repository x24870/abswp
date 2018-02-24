import sys, webbrowser, pyperclip

def mapit(addr):
    print(addr)
    webbrowser.open('https://www.google.com/maps/place/' + addr)

if __name__ == '__main__':
    if(len(sys.argv) > 1):
        # Get address from cmd
        addr = ' '.join(sys.argv[1:])
    else:
        addr = pyperclip.paste()
        
mapit(addr)