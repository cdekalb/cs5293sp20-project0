# Test to ensure that data has been downloaded

import project0
from project0 import main

def test_download():
    url = "http://normanpd.normanok.gov/filebrowser_download/657/Public%20Records%20Archive/02_February%202020/2020-02-23%20Daily%20Incident%20Summary.pdf"
    data = project0.main.fetchincidents(url)
    assert data != None, "Should not be empty"
