#Insert blank rows to specified .xlsx file
#Usage: python blankRowInserter.py N M FILE_NAME
#N: The row number to be insert
#M: How many blank rows insert to specified row number

import sys, openpyxl

def blankRowInserter(n, m, filename):
    sourceWb = openpyxl.load_workbook(filename)
    sourceSheet = sourceWb.active
    
    if n > sourceSheet.max_row:
        print('No need to insert blank rows.')
        return
    
    maxColLetter = openpyxl.utils.get_column_letter(sourceSheet.max_column)
    
    #if n < 1, insert blank row to first line
    fixedCells = None
    if n > 1:
        fixedCells = sourceSheet['A1': maxColLetter+str(n-1)]
    
    moveCells = sourceSheet['A'+str(n): maxColLetter+str(sourceSheet.max_row)]
    
    #write in new file
    outputWb = openpyxl.Workbook()
    outputSheet = outputWb.active
    
    if fixedCells:
        for row in range(1, n):
            for col in range(1, sourceSheet.max_column+1):
                colLetter = openpyxl.utils.get_column_letter(col)
                outputSheet[colLetter+str(row)] = fixedCells[row-1][col-1].value
                
    for row in range(n, sourceSheet.max_row+1):
        for col in range(1, sourceSheet.max_column+1):
            colLetter = openpyxl.utils.get_column_letter(col)
            #skip m rows
            outputSheet[colLetter+str(row+m)] = moveCells[row-n][col-1].value
    
    outputWb.save('inserted_' + filename)
    
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python blankRowInserter.py N M FILE_NAME')
    elif not sys.argv[3].endswith('.xlsx'):
        print('Only support *.xlsx file.')
    else:
        n = m = 0
        try:
            n = int(sys.argv[1])
            m = int(sys.argv[2])
        except:
            print('N and M must greater than 1')
        if n < 1 or m < 1:
            print('N and M must greater than 1')
        else:
            blankRowInserter(n, m, sys.argv[3])