tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

colwidth = [0] * len(tableData)

#find maximun width of each colume
for lst in range(len(tableData)):
    width = 0
    for item in tableData[lst]:
        if len(item) > width: width = len(item)
    colwidth[lst] = width

print(colwidth)

#print with specified format
for col in range(len(tableData[0])):
    text = ''
    for raw in range(len(tableData)):
        text = text + tableData[raw][col].ljust(colwidth[raw]+1, " ")
    print(text)