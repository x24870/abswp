#Find all .xlsx file in current folder and transform to .csv file
#Every sheet in .xlsx file should be transform to a .csv file

import os, openpyxl, csv

xlsxFiles = [file for file in os.listdir() if file.endswith('xlsx')]

#print(xlsxFiles)

for file in xlsxFiles:
    wb = openpyxl.load_workbook(file)
    sheets = wb.worksheets
    for sheet in sheets:
        csvFilename = file[:-5]  + '_' + sheet.title + '.csv'
        print('create {}...'.format(csvFilename))
        with open(csvFilename, 'w', newline='') as csvFile:
            cvsWriter = csv.writer(csvFile)
            for rowNum in range(1, sheet.max_row+1):
                rowContent = []
                for colNum in range(1, sheet.max_column+1):
                    rowContent.append(sheet.cell(row=rowNum, column=colNum).value)
                cvsWriter.writerow(rowContent)
                    