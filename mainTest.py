"""
Tests the functionality of the logic to find the number of days elapsed between 2 given
dates in main.py

Author: Jason Yao
Date: 18/11/2021
"""
import unittest
from main import findDaysElapsed
from utilities.utilities import checkDate


class testDates(unittest.TestCase):
    """
    Test cases detailed in design document
    """
    def testCase1(self):
        firstDate = "02/06/1983"
        secondDate = "22/06/1983"
        expectedNumDays = 19

        self.assertEqual(findDaysElapsed(firstDate,
                                         secondDate), expectedNumDays,
                         "There should be 19 days between these 2 dates")

    def testCase2(self):
        firstDate = "04/07/1984"
        secondDate = "25/12/1984"
        expectedNumDays = 173

        self.assertEqual(findDaysElapsed(firstDate,
                                         secondDate), expectedNumDays,
                         "There should be 173 days between these 2 dates")

    def testCase3(self):
        firstDate = "03/01/1989"
        secondDate = "03/08/1983"
        expectedNumDays = 1979

        self.assertEqual(findDaysElapsed(firstDate,
                                         secondDate), expectedNumDays,
                         "There should be 1979 days between these 2 dates")

    def testCase4(self):
        firstDate = "01/01/1989"
        secondDate = "31/12/1990"
        expectedNumDays = 728

        self.assertEqual(findDaysElapsed(firstDate,
                                         secondDate), expectedNumDays,
                         "There should be 728 days between these 2 dates")

    def testCase5(self):
        firstDate = "07/03/1983"
        secondDate = "05/03/1984"
        expectedNumDays = 363

        self.assertEqual(findDaysElapsed(firstDate,
                                         secondDate), expectedNumDays,
                         "There should be 363 days between these 2 dates")

    def testCase6(self):
        firstDate = "05/03/1983"
        secondDate = "05/03/1984"
        expectedNumDays = 365

        self.assertEqual(
            findDaysElapsed(firstDate, secondDate), expectedNumDays,
            "There should be 365 days between these 2 dates (1 year)")

    def testCaseLargeRange(self):
        firstDate = "01/01/1901"
        secondDate = "31/12/2010"
        expectedNumDays = 40175

        self.assertEqual(findDaysElapsed(firstDate,
                                         secondDate), expectedNumDays,
                         "There should be 40175 days between these 2 dates")

    # Test for a leap year
    def testCaseLeapYear(self):
        firstDate = "01/01/2020"
        secondDate = "01/01/2021"
        expectedNumDays = 365

        self.assertEqual(
            findDaysElapsed(firstDate, secondDate), expectedNumDays,
            "There should be 365 days between these 2 dates, as there is a leap year included here"
        )

    # Test for a missed leap year
    def testCaseMissedLeapYear(self):
        firstDate = "01/03/2020"
        secondDate = "01/01/2021"
        expectedNumDays = 305

        self.assertEqual(
            findDaysElapsed(firstDate, secondDate), expectedNumDays,
            "There should be 305 days between these 2 dates, as the extra day in the 2020 leap year was missed"
        )


class testErrorChecking(unittest.TestCase):
    """
    Test cases for invalid dates
    """
    def testInvalidDateYear1(self):

        date = "21/01/3001"

        self.assertEqual(checkDate(date), False,
                         "Should be false as year is over 2999")

    def testInvalidDateYear2(self):

        date = "21/01/1900"

        self.assertEqual(checkDate(date), False,
                         "Should be false as year is under 1901")

    def testInvalidDateDay1(self):

        date = "32/01/1950"

        self.assertEqual(checkDate(date), False,
                         "Should be false as the date is 32nd")

    def testInvalidDateDay2(self):

        date = "00/01/1950"

        self.assertEqual(checkDate(date), False,
                         "Should be false as the date is the 0th")

    def testInvalidDateNonLeap(self):

        date = "29/02/2001"

        self.assertEqual(checkDate(date), False,
                         "Should be false as 2001 is not a leap year")

    def testDateLeapYear(self):

        date = "29/02/2000"

        self.assertEqual(checkDate(date), True,
                         "Should be true as 2000 is a leap year")


if __name__ == "__main__":
    unittest.main()
