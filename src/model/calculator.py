'''
Contains the calculator logic and returns the number of days elapsed between 2 dates

Author: Jason Yao
Date: 20/11/2021
'''

from src.model.utilities.utilities import (splitDateString, findEarliestDate,
                                           findLeapYearDays, calculateMonths,
                                           calculateYears)


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

    # Find the number of leap days that occur in the period specified
    leapYearDays = findLeapYearDays(earliestDateYears, laterDateYears,
                                    earliestDateYears, earliestDateMonths,
                                    laterDateYears, laterDateMonths,
                                    laterDateDays)

    # If both months are equal, ie both May or August
    if (laterDateMonths == earliestDateMonths):
        daysElapsed += (laterDateDays - earliestDateDays)
    # Add the final months number of elapsed days if the months aren't equal
    else:
        daysElapsed += laterDateDays

    # Loop through the months and add all days together
    daysElapsed = calculateMonths(earliestDateMonths, laterDateMonths,
                                  earliestDateDays, daysElapsed)

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
    daysElapsed = calculateYears(overAYear, daysElapsed, yearDifference,
                                 monthDifference, dayDifference)

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
