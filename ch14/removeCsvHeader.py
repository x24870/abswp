import os, csv

os.makedirs('headerRemoved', exist_ok=True)

csvFiles = [f for f in os.listdir() if f.endswith('.csv')]

for filename in csvFiles:
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        cvsRows = []
        
        for row in reader:
            if reader.line_num == 1: continue
            cvsRows.append(row)
        
        #write csv file
        with open(os.path.join('headerRemoved', filename), 'w', newline='') as hrCsvfile:
            writer = csv.writer(hrCsvfile)
            for row in cvsRows:
                writer.writerow(row)

