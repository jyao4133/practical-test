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
    12: 31
}


# Split the date string and turn it into an array of integers representing [dd, mm, yyyy]
def splitDateString(dateString):
    dateStringArray = dateString.split("/")

    return [int(itr) for itr in dateStringArray]


# Find the earliest date and return an array with earliest date as the 0th element
# and the later date as the 1st element
def findEarliestDate(date1, date2):
    # check current years
    print(date1[2] == date2[2])
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