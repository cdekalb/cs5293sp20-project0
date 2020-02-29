# Test to ensure that data has been downloaded

from project0 import main

def test_download(url):
    data = fetchincidents(url)
    assert data != None, "Should not be empty"

if __name__ == "__main__":
    url = "http://normanpd.normanok.gov/filebrowser_download/657/2020-02-20%20Daily%20Incident%20Summary.pdf"
    test_download(url)
    print("Data successfully downloaded")

