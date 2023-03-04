# Import the required Module
import tabula as tabula
# Read a PDF File
df = tabula.read_pdf("/home/flavia/Desktop/crawler/pdf/pdf103.pdf", pages='all')[0]
# convert PDF into CSV
tabula.convert_into("/home/flavia/Desktop/crawler/pdf/pdf103.pdf", "/home/flavia/Desktop/crawler/csv/pdf103.csv", output_format="csv", pages='all')
print(df)
