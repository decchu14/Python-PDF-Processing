import PyPDF2

with open('PDF_Folder/dummy.pdf', 'rb') as file:
    # print(file)
    reader = PyPDF2.PdfFileReader(file)  # instanciating reader object
    print(reader.numPages)  # printing the number of pages
    print(reader.getPage(0))  # prints the page object

    # to rotate the page first need to get the page because the pdf can have many pages
    page = reader.getPage(0)
    # rotates the pdf page in computer which will not affect the dummy.pdg file
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()  # instanciating writer object
    writer.addPage(page)  # adding the tilted pdf to writer object
    # opening the tilt.pdf as new_file, if tilt.pdf does not exist then it will create a new pdf file  because of wb
    with open('tilt.pdf', 'wb') as new_file:
        # writing the writer object which consists of tilted pdf into new_file which is tilt.pdf
        writer.write(new_file)
