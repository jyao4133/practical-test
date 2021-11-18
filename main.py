"""
Main logic for functionality of finding the number of days elapsed between 2 
dates that are given

Users can enter the date VIA the command line interface

Author: Jason Yao
Date: 18/11/2021
"""

from utilities.utilities import (splitDateString, findEarliestDate,
                                 daysInMonths)


# Finds the number of days elapsed between 2 given dates
def findDaysElapsed(firstDate, secondDate):

    # Convert the date in a dd/mm/yyyy format into integers
    firstDateNumArr = splitDateString(firstDate)
    secondDateNumArr = splitDateString(secondDate)

    # Find the earliest date and return an array with earliest date as the 0th element
    # and the later date as the 1st element
    earliestDate, laterDate = findEarliestDate(firstDateNumArr,
                                               secondDateNumArr)

    print(earliestDate, laterDate)
    earliestDateDays = earliestDate[0]
    earliestDateMonths = earliestDate[1]
    earliestDateYears = earliestDate[2]

    laterDateDays = laterDate[0]
    laterDateMonths = laterDate[1]
    laterDateYears = laterDate[2]

    daysElapsed = 0
    firstIteration = True

    # If both months are equal, ie both May or August
    if (laterDateMonths is earliestDateMonths):
        daysElapsed += (laterDateDays - earliestDateDays)
    # Add the final months number of elapsed days if the months aren't equal
    else:
        daysElapsed += laterDateDays

    # Loop through the months and add all days together
    while (earliestDateMonths < laterDateMonths):
        # Perform days in month - the current earliest date day if we're in our first iteration
        if (firstIteration):
            daysElapsed += (daysInMonths[earliestDateMonths] -
                            earliestDateDays)
            firstIteration = False
        # Add the latest date days if both months are the same (final iteration)

        # Add the days from each month (Excluding leap years) and iterate the current month
        else:
            daysElapsed += daysInMonths[earliestDateMonths]

        earliestDateMonths += 1
        # reset month iterator if we roll over from December to January
        if (earliestDateMonths is 13):
            earliestDateMonths = 1

    # If we have a date 1 day from eachother, we want to not count them as they're partial
    if (daysElapsed is 1):
        return 0
    # Remove 1 day as we aren't counting partial days
    else:
        daysElapsed -= 1
    return daysElapsed


def main():
    tempDate1 = "04/07/1984"
    tempDate2 = "25/12/1984"

    print(findDaysElapsed(tempDate1, tempDate2))


if __name__ == "__main__":
    main()
