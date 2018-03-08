#Decrypt all pdf files in current folder and subfolder

import PyPDF2, os

PASSWORD = 'password'

for foldername, subfolders, filenames in os.walk(os.path.abspath('.')):
    print(foldername)
    for filename in filenames:
        if filename.endswith('_encrypted.pdf'):
            print('Find encrypted pdf file {}'.format(filename))
            absFilename = os.path.join(foldername, filename)
            
            with open(absFilename, 'rb') as pdfFile:
                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                try:
                    pdfReader.decrypt(PASSWORD)
                except:
                    print("Can't decrypt {}".format(absFilename))
                    continue
                
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
                
                outputFilename = absFilename[:-14] + '.pdf'
                with open(outputFilename, 'wb') as dePdfFile:
                    print('Create pdf file: {}'.format(outputFilename))
                    pdfWriter.write(dePdfFile)
