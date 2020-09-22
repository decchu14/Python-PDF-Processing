import sys
import PyPDF2

# need to pass arguements through command line
inputs = sys.argv[1:]

# function to merge pdf files


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()  # instanciating writer object
    for pdf in pdf_list:  # looping through all the files
        merger.append(pdf)  # appending files one by one into merger object

    # writing merger object which consists of merged pdfs into new fi;e called super.pdf
    merger.write('super.pdf')


# function call which passes all the pdf files which are passed through command line
pdf_combiner(inputs)
