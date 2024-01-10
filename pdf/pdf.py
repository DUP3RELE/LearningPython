import PyPDF2

with open('pdf/dummy.pdf', 'rb') as file:
  reader = PyPDF2.PdfReader(file)
  page = reader.pages[0]
  print(page.rotate(180))
  writer = PyPDF2.PdfWriter()
  writer.add_page(page)
  with open('pdf/tilt.pdf', 'wb') as new_file:
    writer.write(new_file)
    