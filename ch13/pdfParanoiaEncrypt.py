import PyPDF2, os

PASSWORD = 'password'
#Encrypt all pdf files in current folder and subfolder

#walk trough specified folder and subfolder to encrypted pdf files
for folderName, subfolders, filenames in os.walk(os.path.abspath('.')):
    for filename in filenames:
        if filename.endswith('.pdf'):
            absFilename = os.path.join(folderName, filename)
            print('Find {}'.format(absFilename))
            with open(absFilename, 'rb') as pdfFile:
                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                pdfWriter = PyPDF2.PdfFileWriter()
                
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
                pdfWriter.encrypt(PASSWORD)
                
                outputFilename = absFilename[:-4] + '_encrypted' + '.pdf'
                with open(outputFilename, 'wb') as outputFile:
                    print('Create encrypted pdf file {}'.format(outputFilename))
                    pdfWriter.write(outputFile)
                    
                #check encrypted pdf files before delete orginal pdf file
                with open(outputFilename, 'rb') as enPdfFile:
                    enPdfReader = PyPDF2.PdfFileReader(enPdfFile)
                    try:
                        enPdfReader.decrypt(PASSWORD)
                    except:
                        print('Decrypt {} fail!'.format(outputFilename))
                        continue
                #close origin pdf file
                
            print('delete {}'.format(absFilename))
            os.remove(absFilename)
               
            
            

