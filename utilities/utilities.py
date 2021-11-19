import re

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


# Checks that the year is between 1901 and 2999
def checkYear(date):
    currentYear = date[2]  # The current year of the date as a num
    return (currentYear >= 1901 and currentYear <= 2999)


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
        print("Month was not a number between 1-12 or the day was invalid")
        return False


# Completes checks on the date to see if it adheres to the guidelines stated
def checkDate(date):
    splitDate = splitDateString(date)
    regexCheck = matchRegex(date)
    yearCheck = checkYear(splitDate)
    dateMonthCheck = checkDateMonth(splitDate)
    if ((regexCheck is not "") and yearCheck and dateMonthCheck):
        return True

    print("Your date was invalid. Please enter it again")
    return False


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

        if (date1[1] < date2[1]):
            return date1, date2

        elif (date1[1] == date2[1]):

            if (date1[0] < date2[0]):
                return date1, date2

        else:
            return date2, date1

    else:
        return date2, date1


def findLeapYearDays(earlierDate, laterDate):
    leapDays = 0
    while (earlierDate != laterDate):
        if (earlierDate % 4 == 0):
            leapDays += 1
        earlierDate += 1
    if (earlierDate == laterDate):
        if (earlierDate % 4 == 0):
            leapDays += 1
    return leapDays


def matchRegex(date):
    try:
        dateFormatRegex = re.compile(
            r'^([0-3][0-9])[\/\\]([0-1][0-9])[\/\\]([1-2][0-9][0-9][0-9])')

        matchedItem = dateFormatRegex.search(date)
        return matchedItem.group()
    except:
        print("Your entered date did not match the format dd/mm/yyyy")
        return ""
