# Import the required Module
import tabula as tabula
# Read a PDF File
df = tabula.read_pdf("/home/user/Desktop/crawler/pdf/pdf103.pdf", pages='all')[0]
# convert PDF into CSV
tabula.convert_into("/home/user/Desktop/crawler/pdf/pdf103.pdf", "/home/user/Desktop/crawler/csv/pdf103.csv", output_format="csv", pages='all')
print(df)
