import openpyxl

PRICE_UPDATES = {'Garlic': 3.07,
                 'Celery': 99.19,
                 'Lemon': 1.27}

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.active

for row in range(2, sheet.max_row+1):
    produceName = sheet['A'+str(row)].value
    print(produceName)
    if produceName in PRICE_UPDATES:
        sheet['B'+str(row)] = PRICE_UPDATES[produceName]
        
wb.save('updatedProduceSales.xlsx')