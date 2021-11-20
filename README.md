# Date difference calculator

A date difference calculator to calculate the number of full days elapsed between a start
and end date given in the form dd/mm/yyyy.

This calculator will

- Only calculate days elapsed if the dates are between 01/01/1901 and 31/12/2999
- Not count partial days
- Allow for command line input of dates
- Validate that the dates coming from command line are in the format and boundaries expected
- Pass the following test cases:

1. 02/06/1983 - 22/06/1983: 19 days
2. 04/07/1984 - 25/12/1984: 173 days
3. 03/01/1989 - 03/08/1983: 1979 days

This calculator will also:

- Account for leap years
- Include extra tests for multiple scenarios to validate the functionality of the code
- Include tests that are created before the implementation of the code to validate functionality of the code
- Utilise as little internal/external libraries as possible
- The libraries that are currently used are:
- "re": For regex matching of the date string
- "os" & "sys": For folder structure and paths
- "unittest": For testing the implementation

To run the code:

1. Go to the root directory of the folder "./practical-test"
2. Run the command "python .\src\main.py" or if you're using an IDE, open the main.py file in ./src and run it using the IDE
3. Type in the 2 dates that you'd like to try in the command line
4. The days elapsed between the 2 dates will show in the command line interface

To test the code:

1. Go to the root directory of the folder "./practical-test"
2. Run the command "python .\src\tests\mainTest.py" or if you're using an IDE, open the mainTest.py file in ./src/tests and run it using the IDE
3. OK will be printed if all tests pass, and the number of tests run will be printed too

# Folder structure:

This code follows a pseudo-MVC style architecture where there is a controller(main), model and view to seperate information in the code.

practical-test
|-src
    |-model
        |-utilities
            |-utilities.py
        |-calculator.py
    |-view
        |-output.py
    |-tests
        |-mainTest.py
    |-main.py
|-README.md





