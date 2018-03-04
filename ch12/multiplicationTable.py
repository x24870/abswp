#Create a spreadsheet contain n * n multiplication table
#Usage: python multiplicationTable.py POS_NUMBER

import sys, openpyxl

def multiplicationTable(n):
    wb = openpyxl.Workbook()
    sheet = wb.active
    
    bfont = openpyxl.styles.Font(name='Times New Roman', bold=True)
    for i in range(2, n+2):
        colLetter = openpyxl.utils.get_column_letter(i)
        sheet[colLetter+'1'] = i - 1
        sheet[colLetter+'1'].font = bfont
        sheet['A'+str(i)] = i - 1
        sheet['A'+str(i)].font = bfont
        
    
    for col in range(2, n+2):
        colLetter = openpyxl.utils.get_column_letter(col)
        for row in range(2, n+2):
            sheet[colLetter+str(row)] = (row-1) * (col-1)
            
    
    wb.save('multiplicationTable.xlsx')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python multiplicationTable.py POS_NUMBER')
    else:
        try:
            n = int(sys.argv[1])
            if n < 0:
                print('POS_NUMBER must > 0.')
            else:
                multiplicationTable(n)
        except Exception as exc:
            print(exc)
            