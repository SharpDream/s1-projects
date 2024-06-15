# first pip install pypdf to access the pdf's then,
# from pypdf import PdfMerger for importing the merger
# learn more about the pypdf at: https://pypi.org/project/pypdf/

from pypdf import PdfMerger


# This program will merge 2 pdf into 1:
# For example 1.pdf and 2.pdf will be merged to merged.pdf

AllPdf = ["1.pdf", "2.pdf"]

merger = PdfMerger()

for NewPdf in AllPdf:
    merger.append(NewPdf)

merger.write("merged.pdf")  # name of new merged pdf
merger.close()


# but it gives us an error that:
# so we can also use PdfWriter instead of PdfMerger()
