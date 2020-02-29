import argparse
# import project0
import urllib.request
import tempfile
import PyPDF2
import re
import sqlite3

def fetchincidents(url):

    # Downloads data from the url to an object data that can be read later
    data = urllib.request.urlopen(url).read()

    return data

def extractincidents(data):

    # Create a temporary file
    fp = tempfile.TemporaryFile()

    # Write the pdf data to a temp file
    fp.write(data)

    # Set the curser of the file back to the beginning
    fp.seek(0)

    # Read the PDF
    pdfReader = PyPDF2.PdfFileReader(fp)

    # Initialize list of pages to read in data
    page = []

    # Get number of pages
    numPages = pdfReader.getNumPages()

    # Initialize a list to hold each list containing a row of data
    totalPage = []

    # Initialize a list to temporarily hold each row of data as it is being read in
    tempPage = []
    
    for i in range(numPages):
        
        # Iteratively store the pages
        page.append(pdfReader.getPage(i).extractText())

        if i == 0:
            # Remove the last 2 lines from the first page that contained unnecessary information 
            # from the pdf
            page[i] = "\n".join(page[i].split("\n")[0:-3])

            # Add back the trailing newline charcter that was removed above
            page[i] = page[i] + '\n'

        if i == numPages - 1:
            # Remove the time stamp at the bottom of the last page of the pdf
            page[i] = "\n".join(page[i].split("\n")[0:-2])

        # Edge case for datum that contain newline characters
        page[i] = page[i].replace(' \n', ' ')

        # Edge case for datum that contain coordinates
        page[i] = page[i].replace('-\n', '-')

        # Split the data on newline characters
        newLineSplit = page[i].split('\n')

        # Create regular expression for the date format
        dateRegEx = r"(\d{1,2}\/\d{1,2}\/\d{4} \d{1,2}:\d{1,2})"
        datePattern = re.compile(dateRegEx)

        # Counter for column of data; Set to 5 so that the code for the insertion of data into 
        # list format assumes the next expected data is a date
        count = 0
        # Boolean stating whether the current row being operated on is the header
        isHeader = True

        # Loop over each datum in the data
        for text in newLineSplit:
            # Check if the current row is the header
            if(isHeader):
                # Append the current datum to tempPage list
                tempPage.append(text)
                # Evaluate next column
                count += 1
                # Check if the datum is the last in the row
                if(count == 5):
                    # Empty the tempPage list
                    tempPage.clear()
                    # Leave the header row
                    isHeader = False
                # Evaluate each datum in the header row before moving on to 
                # incidence data
                continue

            # Check if the current datum matches the date regular expression
            if(datePattern.match(text)):
                # Check if the number of columns in the previous row is not five
                if(count != 5):
                    # Let user know there is missing data for Date / Time of 
                    # the previous row
                    print("Missing data for Date / Time: " + tempPage[0] + "; Row omitted")
                    # Omit the row
                    tempPage.clear()
                # Check if tempPage list is not empty
                if(tempPage != []):
                    # Append a copy of tempPage to the totalPage list
                    totalPage.append(tempPage.copy())
                    # Empty the tempPage list
                    tempPage.clear()
                # Reset count to 0
                count = 0
            # Append a copy of tempPage to the totalPage list
            tempPage.append(text)
            # Evaluate next column
            count += 1

        # Initialize list to hold tuples of the data
        incidentTuples = []

        for i in range(len(totalPage)):
            # Iteratively store each row of data as a tuple
            incidentTuples.append(tuple(totalPage[i]))

    return incidentTuples

def createdb():
    # Create connection object that represents the database
    db = sqlite3.connect('normanpd.db')

    # Create cursor object to perform SQL commands
    c = db.cursor()

    # Clear incidents table if it exists already
    c.execute('''DROP TABLE IF EXISTS incidents''')

    # Create new incidents table
    c.execute('''CREATE TABLE incidents (
    incident_time TEXT,
    incident_number TEXT,
    incident_location TEXT,
    nature TEXT,
    incident_ori TEXT
    )''')

    # Save the changes to the database
    db.commit()

    return db

def populatedb(db, incidents):

    # Create cursor object to perform SQL commands
    c = db.cursor()

    # Insert the data into the incidents table
    for i in range(len(incidents)):
        c.executemany('INSERT INTO incidents VALUES (?,?,?,?,?)', (incidents[i],))

    # Save the changes to the database
    db.commit

    return db

def status(db):

    # Create cursor object to perform SQL commands
    c = db.cursor()

    # Initialize list to hold the tuples of nature and count query
    natureIncidents = []
    # Initialize list to hold the list of nature and count query after the tuples
    # of natureIncidents[] are converted to lists
    natureIncidentsList = []

    # Execute query to output the number of times a given nature appears in the
    # database
    for row in c.execute('SELECT nature, COUNT(*) FROM incidents GROUP BY nature ORDER BY nature'):
        natureIncidents.append(row)    
    
    # Store tuples of natureIncidents as a list
    # Convert the second element in each list from integer to string
    # Print the pipe separated nature and its corresponding count value 
    for i in range(len(natureIncidents)):
        natureIncidentsList.append(list(natureIncidents[i]))
        natureIncidentsList[i][1] = str(natureIncidentsList[i][1])
        print("|".join(natureIncidentsList[i]))

def main(url):
    # Download data
    data = fetchincidents(url)

    # Extract Data
    incidents = extractincidents(data)
	
    # Create Dataase
    db = createdb()
	
    # Insert Data
    populatedb(db, incidents)
	
    # Print Status
    status(db)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, 
        help="The incident summary url.")
     
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)
