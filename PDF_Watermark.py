import PyPDF2
# opening the super.pdf file in read binary form and instanciating template as reader object
template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
#  opening the wtr.pdf file in read binary form and instanciating watermark as reader object
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
# instanciating writer object
output = PyPDF2.PdfFileWriter()

# getting the number of pages of template object which consists of super.pdf file and looping that many times
for i in range(template.getNumPages()):
    # each page assigning into page variable
    page = template.getPage(i)
    # merging template page which is super.pdf into wtr.pdf page
    page.mergePage(watermark.getPage(0))
    # adding all the merged pdf into output
    output.addPage(page)

    # opening watermarked_output.pdf in write binary form as file
    with open('watermarked_output.pdf', 'wb') as file:
        # writing output which has merged super.pdf and wtr.pdf pages into new file called watermarked_output.pdf
        output.write(file)
