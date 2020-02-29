# Project 0

Class:
CS 5293

Author:
Creighton DeKalb

# Project Summary

The purpose of this project is to take data from a pdf file, extract the data into a readable format, insert the data into a database, and perform a query on the database to gain the desired information. The pdf file from which the project is designed to extract data is the Norman Police Department Incident Summary for a given day. From one of these pdf files, the code is designed to provide the list of the nature of incidents for that day, along with the number of times the incident nature appears in the incident summary. The list of currently available daily incident reports can be found at http://normanpd.normanok.gov/content/daily-activity.

# Installing

In order to run this project, the user needs to install pipenv. This can be done in the command line using the command:

    pipenv install

# Prerequisites

To access the project, the user must navigate to the command line and run the command:

    git clone https://github.com/cdekalb/cs5293sp20-project0.git

# Tests

TODO: Discuss tests

To run the tests, the user must navigate to the command line and run the command:

    pipenv run pytest

# Deployment

TODO: Explain code

To run the code, navigate from the command line to the cs5293sp20-project0 directory in which all the project files exist. In the command line, enter the following:

    pipenv run python project0/main.py --incidents <url>

This command will run the main.py file in the project0 directory, with the arguments '--incidents', to indicate that we desire incidents informtation, and url, which will be the string of the url needed to access the pdf file.

# Assumptions

## For this project, a number of assumptions were made:

   1: The link for the pdf file to be examined will be a url from the Norman Police Department website as provided in the project description.

   2: The data in the pdf being examined will have five columns.

   3: The first column of the data will not have any missing values, and each value must take the value of a date and time, e.g. MM/DD/YYYY HH:MinMin.

   4: There can exist missing data, however the column in which the data does not appear will not be the first column.

   5: If there is missing data within a row, it is acceptable to omit the entire row, regardless of the data that is present in the row.

