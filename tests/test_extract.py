# Test to ensure the extraction of the first page of data

import project0
from project0 import main

def test_extract():
    url = "http://normanpd.normanok.gov/filebrowser_download/657/Public%20Records%20Archive/02_February%202020/2020-02-23%20Daily%20Incident%20Summary.pdf"

    # Download data
    data = project0.main.fetchincidents(url)

    # Extract data
    incidentTuples = project0.main.extractincidents(data)

    assert incidentTuples != None, "Should not be empty"
