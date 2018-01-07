import re

def regexVersionStrip(text, stripChar=None):
    if stripChar is not None:
        regex = re.compile('%s' %stripChar)
        return regex.sub('', text)
        
    else:
        fspaceRegex = re.compile(r'^\s*')
        bspaceRegex = re.compile(r'\s*$')
        
        text = fspaceRegex.sub('', text)
        text = bspaceRegex.sub('', text)
        
        return text
 
    
if __name__ == '__main__':
    text = '   This is example text   '
    print(text)
    print(regexVersionStrip(text))
    print(regexVersionStrip(text, 'example'))