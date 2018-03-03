import openpyxl
import pprint

wb = openpyxl.load_workbook('censuspopdata.xlsx')

sheet = wb.active

countyData = {}

for row in range(2, sheet.max_row+1):
    state = sheet['B'+str(row)].value
    county = sheet['C'+str(row)].value
    pop = sheet['D'+str(row)].value
    
    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    
    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)

print('Writing results...')
with open('census2010.py', 'w') as file:
    file.write('All data = ' + pprint.pformat(countyData))
print('Done')