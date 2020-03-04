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

There are four test files in the project: 
- test_download.py

The download test uses a provided url to download the data into an object. The test asserts that the object is not empty to ensure that data has been downloaded.

- test_date_time.py

The date/time test defines the regular expression that the date/time data is supposed to match. The test takes in an example tuple, and asserts that the first datum matches the regular expression.

- test_extract.py

The extract test downloads the data and uses the PyPDF2 package to extract the data into a readable format. The test mirrors the extractincidents method in the main.py file, but only uses the first page. The test extracts the data into tuples using the extractincidents method in the main file and asserts that the list of tuples is not empty.

- test_database_insertion.py

The database insertion test creates a database and uses a sample tuple to be inserted into the database. The test inserts the tuple into the database, then performs a query to select all rows in the database, and finally asserts that the result of the query is not empty. 

To run the tests, the user must navigate to the command line and run the command:

    pipenv run python -m pytest

# Deployment

The main file downloads data, extracts the data, creates a database, stores the data into the database, then performs a query on the database to retrieve the incident natures sorted alphabetically along with each incident nature's count in the database.

The main file is split up into six methods, not including the main method. The execution and explanation for these methods are as follows:

- fetchincidents(url)

The fetchincidents method takes in a url and returns an object containing the data from the url.

- dateTimeRegEx()

The dateTimeRegEx method creates an object that stores the regular expression of the desired date/time format for the data.

- extractincidents(data)

The extractincidents method takes in a data object, reads the data from the PDF into a readable format, cleans the data to be inserted, then passes through each row of data and creates tuples of each row.

- createdb()

The createdb method creates a database for the tuples to be stored.

- poplatedb(db, incidents)

The populatedb method populates the database with the extracted tuples from extractincidents.

- status(db)

The status method takes in a database, performs the desired query, then prints the output of the query into a pipe separated form.

To run the code, navigate from the command line to the cs5293sp20-project0 directory in which all the project files exist. In the command line, enter the following:

    pipenv run python project0/main.py --incidents <url>

This command will run the main.py file in the project0 directory, with the arguments '--incidents', to indicate that we desire incidents informtation, and url, which will be the string of the url needed to access the pdf file.

# Assumptions and Bugs

## For this project, a number of assumptions were made:

   1: The link for the pdf file to be examined will be a url from the Norman Police Department website as provided in the project description.

   2: The data in the pdf being examined will have five columns.

   3: The first column of the data will not have any missing values, and each value must take the value of a date and time, e.g. MM/DD/YYYY HH:MinMin.

   4: There can exist missing data, however the column in which the data does not appear will not be the first column.

   5: If there is missing data within a row, it is acceptable to omit the entire row, regardless of the data that is present in the row.

## Bugs

In the PDF, a number of bugs could arise. The most common bug found in the PDFs used to make this project was missing data in the rows. The code is designed to check that each row has exactly five data, and if it finds that there are not five data, that given row is omitted.

