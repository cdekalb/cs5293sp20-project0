# Test to ensure the creation of a database

import project0
from project0 import main

def test_database_insertion():
    # Create a database
    db = project0.main.createdb()

    incidents = []

    # Create a sample incident
    incident1 = ('2/24/2020 0:04', '2020-00003064', '1932 E LINDSEY ST', 'Breathing Problems', 'EMSSTAT')
    
    incidents.append(incident1)

    # Populate database
    project0.main.populatedb(db, incidents)

    # Create cursor object to perform SQL commands
    c = db.cursor()

    # Initialize list to hold the tuples of nature and count query
    natureIncidents = []

    # Execute query to output the number of times a given nature appears in the
    # database
    for row in c.execute('SELECT * FROM incidents'):
        natureIncidents.append(row)

    assert natureIncidents != None, "Should not be empty"