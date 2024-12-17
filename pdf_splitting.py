    #!/usr/bin/python
from PyPDF2 import PdfFileReader, PdfFileWriter
#split range
pgi=30 #start
pgf=37 #end

pdf_document = "test.pdf"
pdf = PdfFileReader(pdf_document)
pdf_writer = PdfFileWriter()
for page in range(pgi-1,pgf):
    current_page = pdf.getPage(page)
    pdf_writer.addPage(current_page)

with open(f'test-{pgi}-{pgf}.pdf', "wb") as out:
    pdf_writer.write(out)
