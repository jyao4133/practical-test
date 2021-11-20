'''
Acts as the view for the calculator and displays error messages, prompts and the final output

Author: Jason Yao
Date: 20/11/2021
'''

# Prints out the initial starting message for the calculator to the console
def initialPrint():
    print("!Welcome to my calculator which checks days elapsed between 2 dates!")    
    print("RULES FOR DATES:")
    print("--------------------------------------------------------------------")
    print("- The date must be in the format  dd/mm/yyyy")
    print("- The date must be between 01/01/1901 - 31/12/2999")
    print("--------------------------------------------------------------------")    
    

# Prints specific messages depending on the type of message that is necessary
def logItem(type, item="Nothing"):
    
    match type:
        case "Final Answer":
            print(
        str(item) +
        " Days elapsed between the specified dates")
        case "First Date":
            print("The 1st date entered was in an invalid format, please try again")
        case "Second Date":
            print("The 2nd date entered was in an invalid format, please try again")
        case "Regex":
            print("The date format did not match dd/mm/yyyy, please try again")
        case "Date Month":
            print("The date had an invalid month or day, please try again")
        case "Year":
            print("The year given was not a valid year, please try again")
            