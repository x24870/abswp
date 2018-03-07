import PyPDF2, os

pdfFIles = []
    
for file in os.listdir():
    if file.endswith('.pdf'): pdfFIles.append(file)
    
pdfFIles.sort(key=str.lower)
print(pdfFIles)

pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdfFIles:
    with open(filename, 'rb') as file:
        pdfReader = PyPDF2.PdfFileReader(filename)
        #loop each page
        for pageNum in range(1, pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(pageNum))

with open('output.pdf', 'wb') as outputFile:
    pdfWriter.write(outputFile)