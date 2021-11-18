"""
Main logic for functionality of finding the number of days elapsed between 2 
dates that are given

Users can enter the date VIA the command line interface



Author: Jason Yao
Date: 18/11/2021
"""

from utilities.utilities import (splitDateString, findEarliestDate,
                                 findLeapYearDays, daysInMonths)


# Finds the number of days elapsed between 2 given dates
def findDaysElapsed(firstDate, secondDate):

    # Convert the date in a dd/mm/yyyy format into integers
    firstDateNumArr = splitDateString(firstDate)
    secondDateNumArr = splitDateString(secondDate)

    # Find the earliest date and return an array with earliest date as the 0th element
    # and the later date as the 1st element
    earliestDate, laterDate = findEarliestDate(firstDateNumArr,
                                               secondDateNumArr)

    earliestDateDays = earliestDate[0]
    earliestDateMonths = earliestDate[1]
    earliestDateYears = earliestDate[2]

    laterDateDays = laterDate[0]
    laterDateMonths = laterDate[1]
    laterDateYears = laterDate[2]

    yearDifference = laterDateYears - earliestDateYears
    daysElapsedFromYears = 0
    daysElapsed = 0
    firstIteration = True

    # Find the number of leap days that occur in the period specified
    leapYearDays = findLeapYearDays(earliestDateYears, laterDateYears)
    print(leapYearDays)
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
        # Add the latest date days if both months are the same (final iteration)

        # Add the days from each month (Excluding leap years) and iterate the current month
        else:
            daysElapsed += daysInMonths[currentMonth]

        currentMonth += 1
        # reset month iterator if we roll over from December to January
        if (currentMonth is 13):
            currentMonth = 1
    # Handle days elapsed during a year
    if (laterDateYears != earliestDateYears and yearDifference != 1):
        numberOfYearsElapsed = laterDateYears - earliestDateYears
        daysElapsedFromYears = (numberOfYearsElapsed - 1) * 365
        daysElapsed = daysElapsed + daysElapsedFromYears
    elif (yearDifference == 1):
        # Check if more than a year has passed (365+ days)
        if (earliestDateMonths < laterDateMonths
                or (earliestDateMonths == laterDateMonths
                    and earliestDateDays < earliestDateYears)):
            daysElapsed = 365 + daysElapsed

    # If we have a date 1 day from eachother, we want to not count them as they're partial
    if (daysElapsed == 1 or daysElapsed == 0):
        return 0
    # Remove 1 day as we aren't counting partial days
    else:
        daysElapsed -= 1
    # Increment the leap year days found
    daysElapsed += leapYearDays
    # Returning the absolute value as we're considering the days elapsed due to years as a negative weight
    return abs(daysElapsed)


def main():
    # TODO: Allow for command line inputs
    # TODO: Check command line input data structure to make sure the format is in dd/mm/yyyy
    # TODO: Check the date is between 01/01/1901 - 31/12/2999
    tempDate1 = "01/03/2020"
    tempDate2 = "01/01/2021"

    print(findDaysElapsed(tempDate1, tempDate2))


if __name__ == "__main__":
    main()
