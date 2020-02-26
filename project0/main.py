import argparse
import project0
import urllib.request
import tempfile
import PyPDF2


def fetchincidents(url):
    # Sets the string url to link
    link = (url)
    # Downloads data from the url to an object data that can be read later
    data = urllib.request.urlopen(link).read()

    fp = tempfile.TemporaryFile()
    # Write the pdf data to a temp file
    fp.write(data)
    # Set the curser of the file back to the begining
    fp.seek(0)
    # Read the PDF
    pdfReader = PyPDF2.PdfFileReader(fp)
    pdfReader.getNumPages()
    # Get the first page
    page1 = pdfReader.getPage(0).extractText()
    # ...
    print(page1)


def main(url):
    # Download data
    project0.fetchincidents(url)

    # Extract Data
    incidents = project0.extractincidents()
	
    # Create Dataase
    db = project0.createdb()
	
    # Insert Data
    project0.populatedb(db, incidents)
	
    # Print Status
    project0.status(db)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, 
                         help="The arrest summary url.")
     
    args = parser.parse_args()
    if args.arrests:
        main(args.arrests)
