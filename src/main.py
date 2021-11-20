"""
Main logic for functionality of finding the number of days elapsed between 2 
dates that are given in the format dd/mm/yyyy

Users can enter the date VIA the command line interface

Author: Jason Yao
Date: 18/11/2021
"""
import sys
import os

sys.path.append(os.getcwd())
from src.view.output import (initialPrint, logItem)
from src.model.calculator import findDaysElapsed
from src.model.utilities.utilities import checkDate


# Initialises the logic of the calculator
def initialise():

    initialPrint()
    # Flags to check if the dates have passed all checks and initialise dates
    allChecksPassedDate1 = False
    allChecksPassedDate2 = False
    date1 = ""
    date2 = ""
    # Check if the 1st date is valid
    while (not allChecksPassedDate1):
        date1 = input("Please input the 1st date in the format dd/mm/yyyy: ")
        try:
            allChecksPassedDate1, message = checkDate(date1)
            if (not allChecksPassedDate1):
                logItem(message)
        except:
            logItem("First Date")
    # Check if the 2nd date is valid
    while (not allChecksPassedDate2):
        date2 = input("Please input the 2nd date in the format dd/mm/yyyy: ")
        try:
            allChecksPassedDate2, message = checkDate(date2)
            if (not allChecksPassedDate2):
                logItem(message)
        except:

            logItem("Second Date")

    finalAnswer = findDaysElapsed(date1, date2)
    logItem("Final Answer", finalAnswer)


if __name__ == "__main__":

    initialise()
