from PyPDF2 import PdfFileReader, PdfFileWriter
import template

template.make()

base_filepath = "./special_moerirekisho.pdf"
data_filepath = "./template.pdf"
output_filepath = "./merge.pdf"

with open(base_filepath, mode='rb') as bf, open(data_filepath, mode='rb') as df, open(output_filepath, mode='wb') as of:
  data_reader = PdfFileReader(df)
  data_page = data_reader.getPage(0)

  reader = PdfFileReader(bf)
  writer = PdfFileWriter()

  for page_num in range(0, reader.numPages):
    obj = reader.getPage(page_num)
    obj.mergePage(data_page)
    writer.addPage(obj)

  writer.write(of)
