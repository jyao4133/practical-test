"""
Main logic for functionality of finding the number of days elapsed between 2 
dates that are given

Users can enter the date VIA the command line interface

TODO: Put into folder structure and refactor some functions to different files

Author: Jason Yao
Date: 18/11/2021
"""

from utilities.utilities import (splitDateString, findEarliestDate,
                                 findLeapYearDays, checkDate, daysInMonths)


def initialise():
    print("RULES FOR DATES:")
    print("---------------------------------------------------")
    print("- The date must be in the format  dd/mm/yyyy")
    print("- The date must be between 01/01/1901 - 31/12/2999")

    # Flags to check if the dates have passed all checks and initialise dates
    allChecksPassedDate1 = False
    allChecksPassedDate2 = False
    date1 = ""
    date2 = ""

    while (not allChecksPassedDate1):
        date1 = input("Please input the 1st date in the format dd/mm/yyyy: ")
        try:
            allChecksPassedDate1 = checkDate(date1)
        except:
            print(
                "The 1st date entered was in an invalid format, please try again"
            )

    while (not allChecksPassedDate2):
        date2 = input("Please input the 2nd date in the format dd/mm/yyyy: ")
        try:
            allChecksPassedDate2 = checkDate(date2)
        except:
            print(
                "The 2nd date entered was in an invalid format, please try again"
            )
    print(
        str(findDaysElapsed(date1, date2)) +
        " Days elapsed between the specified dates")


# Finds the number of days elapsed between 2 given dates
def findDaysElapsed(firstDate, secondDate):

    # Convert the date in a dd/mm/yyyy format into integers
    firstDateNumArr = splitDateString(firstDate)
    secondDateNumArr = splitDateString(secondDate)

    # Find the earliest date and return an array with earliest date as the 0th element
    # and the later date as the 1st element
    earliestDate, laterDate = findEarliestDate(firstDateNumArr,
                                               secondDateNumArr)

    # Assign days/months/years to variables for each date entered for clarity
    earliestDateDays = earliestDate[0]
    earliestDateMonths = earliestDate[1]
    earliestDateYears = earliestDate[2]

    laterDateDays = laterDate[0]
    laterDateMonths = laterDate[1]
    laterDateYears = laterDate[2]

    yearDifference = laterDateYears - earliestDateYears
    daysElapsed = 0
    firstIteration = True

    # Find the number of leap days that occur in the period specified
    leapYearDays = findLeapYearDays(earliestDateYears, laterDateYears)
    # Check if the 2 dates start/end on any leap years, if they do, then check the month they start/end in
    # If they miss the leap year day (Feb 29th), then we subtract a day from the total leap year days found
    if (earliestDateYears % 4 == 0):
        if (earliestDateMonths > 2):
            leapYearDays -= 1
    if (laterDateYears % 4 == 0):
        if (laterDateMonths < 2
                or (laterDateMonths == 2 and laterDateDays < 29)):
            leapYearDays -= 1

    # If both months are equal, ie both May or August
    if (laterDateMonths == earliestDateMonths):
        daysElapsed += (laterDateDays - earliestDateDays)
    # Add the final months number of elapsed days if the months aren't equal
    else:
        daysElapsed += laterDateDays

    currentMonth = earliestDateMonths
    # Loop through the months and add all days together
    while (currentMonth != laterDateMonths):
        # Perform days in month - the current earliest date day if we're in our first iteration
        if (firstIteration):
            daysElapsed += (daysInMonths[currentMonth] - earliestDateDays)
            firstIteration = False
        # Add the days from each month (Excluding leap years) and iterate the current month
        else:
            daysElapsed += daysInMonths[currentMonth]
        currentMonth += 1
        # reset month iterator if we roll over from December to January
        if (currentMonth is 13):
            currentMonth = 1

    # Handle days elapsed during a year if more than a year has been elapsed since earliest date
    monthDifference = earliestDateMonths - laterDateMonths
    dayDifference = earliestDateDays - laterDateDays
    overAYear = False
    # monthDifference < 0 checks if there's more than a year elapsed
    # monthDifference == 0 and dayDifference < 0 if there's more than a year elapsed
    if (monthDifference < 0 or (monthDifference == 0 and dayDifference < 0)):
        overAYear = True
    elif (dayDifference == 0 and monthDifference == 0):
        overAYear = True

    # Adds days depending on the amount of years elapsed
    if (overAYear):
        daysElapsed += 365 * yearDifference
    elif (not overAYear and monthDifference == 0 and dayDifference > 0):
        daysElapsed += 365 * yearDifference
    else:
        daysElapsed += 365 * (yearDifference - 1)

    # If we have a date 1 day from eachother, we want to not count them as they're partial
    if (daysElapsed == 1 or daysElapsed == 0):
        return 0
    # Remove 1 day as we aren't counting partial days
    else:
        daysElapsed -= 1
    # Increment the leap year days found
    daysElapsed += leapYearDays
    # Returning the absolute value as may become negative
    return abs(daysElapsed)


if __name__ == "__main__":

    initialise()
