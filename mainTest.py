"""
Tests the functionality of the logic to find the number of days elapsed between 2 given
dates in main.py

Author: Jason Yao
Date: 18/11/2021
"""
import unittest
from main import findDaysElapsed


class testDates(unittest.TestCase):
    """
    Test cases detailed in design document
    """
    def testCase1(self):
        firstDate = "02/06/1983"
        secondDate = "22/06/1983"
        expectedNumDays = 19

        self.assertEqual(findDaysElapsed(firstDate, secondDate), 19,
                         "There should be 19 days between these 2 dates")

    def testCase2(self):
        firstDate = "04/07/1984"
        secondDate = "25/12/1984"
        expectedNumDays = 173

        self.assertEqual(findDaysElapsed(firstDate, secondDate), 173,
                         "There should be 173 days between these 2 dates")

    def testCase3(self):
        firstDate = "03/01/1989"
        secondDate = "03/08/1983"
        expectedNumDays = 1979

        self.assertEqual(findDaysElapsed(firstDate, secondDate), 1979,
                         "There should be 1979 days between these 2 dates")

    # Test for a leap year
    def testCaseLeapYear(self):
        firstDate = "01/01/2020"
        secondDate = "01/01/2021"
        expectedNumDays = 19

        self.assertEqual(
            findDaysElapsed(firstDate, secondDate), 364,
            "There should be 364 days between these 2 dates, as there is a leap year included here"
        )


if __name__ == "__main__":
    unittest.main()
