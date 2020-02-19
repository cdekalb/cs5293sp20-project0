
# Test to ensure that the function downloads data

def test_download():
    url = ("http://normanpd.normanok.gov/filebrowser_download/657/2020-02-11%20Daily%20Incident%20Summary.pdf")
    data = urllib.request.urlopen(url).read()
    assert data != None, "Should not be empty"

if __name__ == "__main__":
    test_download()
    print("Data successfully downloaded")

