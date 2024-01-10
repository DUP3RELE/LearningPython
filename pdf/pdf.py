import PyPDF2
import sys

imputs = sys.argv[1:]

# with open('pdf/dummy.pdf', 'rb') as file:
#   reader = PyPDF2.PdfReader(file)
#   page = reader.pages[0]
#   print(page.rotate(180))
#   writer = PyPDF2.PdfWriter()
#   writer.add_page(page)
#   with open('pdf/tilt.pdf', 'wb') as new_file:
#     writer.write(new_file)

def pdf_combiner(pdf_list):
  merger = PyPDF2.PdfMerger()
  for pdf in pdf_list:
    print(pdf)
    merger.append(pdf)
  merger.write('pdf/super.pdf')

pdf_combiner(imputs)