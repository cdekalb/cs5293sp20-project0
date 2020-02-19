

import tempfile
fp = tempfile.TemporaryFile()

# Write the pdf data to a temp file
fp.write(data.read())

# Set the curser of the file back to the begining
fp.seek(0)

# Read the PDF
pdfReader = PdfFileReader(fp)
pdfReader.getNumPages()

# Get the first page
page1 = pdfReader.getPage(0).extractText()
# ...
