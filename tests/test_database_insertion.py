# Test to ensure the creation of a database

import sqlite3

def createdb():
    # Create connection object that represents the database
    db = sqlite3.connect('normanpd.db')

    # Create cursor object to perform SQL commands
    c = db.cursor()

    # Clear incidents table if it exists already
    c.execute('''DROP TABLE incidents''')

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

def test_database_creation(db, incidents):
    createdb()
    populatedb(db, incidents)

    # Create cursor object to perform SQL commands
    c = db.cursor()

    # Initialize list to hold the tuples of nature and count query
    natureIncidents = []

    # Execute query to output the number of times a given nature appears in the
    # database
    for row in c.execute('SELECT * FROM incidents'):
        natureIncidents.append(row)

    assert natureIncidents != None, "Should not be empty"

if __name__ == "__main__":
    url = "http://normanpd.normanok.gov/filebrowser_download/657/2020-02-20%20Daily%20Incident%20Summary.pdf"
    test_database_creation(url)
    print("Data successfully inserted into database")