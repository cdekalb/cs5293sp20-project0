# Test to validate the dataPattern regular expressionx

import project0
from project0 import main

def test_date_time():
    datePattern = project0.main.dateTimeRegEx()
    assert datePattern.match("02/20/2020 20:20"), "Each value in the first column of the data should be in Date / Time format"
