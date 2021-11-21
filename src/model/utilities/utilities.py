import re
'''
Utilities file for helper functions that the calculator would use

Author: Jason Yao
Date: 20/11/2021
'''

# Dictionary where the key is the month as a number and the value is the number of days in the month
daysInMonths = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}


# Alternative code to check days elapsed between 2 dates
def countDaysElapsed(firstDate, secondDate):
    daysElapsed = 0
    # Assume leap years will be handled by leap year calculation function findLeapYearDays
    if (firstDate[0] == 29 and firstDate[1] == 2):
        firstDate[0] = 28

    if (secondDate[0] == 29 and secondDate[1] == 2):
        secondDate[0] = 28

    # While the dates aren't equal, count the days
    while ((firstDate[0] != secondDate[0]) or (firstDate[1] != secondDate[1])
           or (firstDate[2] != secondDate[2])):
        # Increment days elapsed
        daysElapsed += 1
        firstDate[0] += 1
        # Check if the days have overflowed its limits for current month
        if (firstDate[0] > daysInMonths[firstDate[1]]):
            # Reset days and increment month
            firstDate[0] = 1
            firstDate[1] += 1
            # Check if the months have overflowed for the current year
            if (firstDate[1] > 12):
                # Reset month and increment year
                firstDate[1] = 1
                firstDate[2] += 1

    return daysElapsed


# Checks that the year is between 1901 and 2999
def checkYear(date):
    currentYear = date[2]  # The current year of the date as a num
    return (currentYear >= 1901 and currentYear <= 2999)


# Checks that the dates and months entered are logical.
# Month: Can't have a month bigger than 12 or lower than 1
# Date: Can't have a date bigger than 31 or lower than 1, and it also needs to be within the bounds of the current month
def checkDateMonth(date):
    currentDay = date[0]
    currentMonth = date[1]
    currentYear = date[2]
    isLeapYear = currentYear % 4 == 0
    if (currentMonth <= 12 and currentMonth >= 1 and currentDay > 0):
        # Account for leap year since Feb will have 29 days

        if (isLeapYear and currentMonth == 2):
            return (currentDay < 30)
        else:
            return (currentDay <= daysInMonths[currentMonth]
                    )  # Check if the day is within the month
    else:
        return False


# Completes checks on the date to see if it adheres to the guidelines stated
# True for matches date criteria
# False if the date is not correct
def checkDate(date):
    splitDate = splitDateString(date)

    regexCheck = matchRegex(date)
    if (regexCheck == ""):
        return False, "Regex"
    yearCheck = checkYear(splitDate)
    if (not yearCheck):
        return False, "Year"
    dateMonthCheck = checkDateMonth(splitDate)
    if (not dateMonthCheck):
        return False, "Date Month"

    return True, "Passed"


# Split the date string and turn it into an array of integers representing [dd, mm, yyyy]
def splitDateString(dateString):
    dateStringArray = dateString.split("/")

    return [int(itr) for itr in dateStringArray]


# Find the earliest date and return an array with earliest date as the 0th element
# and the later date as the 1st element
def findEarliestDate(date1, date2):
    # check current years
    if (date1[2] < date2[2]):
        return date1, date2
    elif (date1[2] == date2[2]):
        # Check the months and the days if the months are equal
        if (date1[1] < date2[1]):
            return date1, date2
        elif (date1[1] == date2[1]):
            if (date1[0] < date2[0]):
                return date1, date2
            else:
                return date2, date1
        else:
            return date2, date1
    else:
        return date2, date1


# Finds the number of leap year days within the 2 dates supplied
# If the dates supplied happen to be on a leap year, and miss the leap day, then don't count it
def findLeapYearDays(earlierDate, laterDate, earliestDateYears,
                     earliestDateMonths, laterDateYears, laterDateMonths,
                     laterDateDays):
    leapDays = 0
    while (earlierDate != laterDate):
        if (earlierDate % 4 == 0):
            leapDays += 1
        earlierDate += 1
    if (earlierDate == laterDate):
        if (earlierDate % 4 == 0):
            leapDays += 1

    # Check if the 2 dates start/end on any leap years, if they do, then check the month they start/end in
    # If they miss the leap year day (Feb 29th), then we subtract a day from the total leap year days found
    if (earliestDateYears % 4 == 0):
        if (earliestDateMonths > 2):
            leapDays -= 1
    if (laterDateYears % 4 == 0):
        if (laterDateMonths < 2
                or (laterDateMonths == 2 and laterDateDays <= 29)):
            leapDays -= 1
    return leapDays


# Matches the regex string for the date entered. It must be in the format dd/mm/yyyy
def matchRegex(date):
    try:
        dateFormatRegex = re.compile(
            r'^([0-9][0-9])[\/\\]([0-9][0-9])[\/\\]([1-9][0-9][0-9][0-9])')

        matchedItem = dateFormatRegex.search(date)
        return matchedItem.group()
    except:
        return ""
