# Test to validate the dataPattern regular expressionx

from project0 import main

def test_date_time():

    assert datePatten.match("02/20/2020 20:20"), "Each value in the first column of the data should be in Date / Time format"

if __name__ == "__main__":
    test_date_time()
    print("Date / Time format of the first column is confirmed")