"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    
    #The months with 31 days in it
    days_list = [1, 3, 5, 7, 8, 10, 12]
    
    #Checks if the month has 31 days based on the list
    if month in days_list:
        return 31
    #If month is February, checks whether it is a leap year or not
    elif month == 2:
        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28
    #If the above are not true, then the month has 30 days
    else:
        return 30


def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    
    #Checks if the year, month, and days are valid
    is_year_valid = datetime.MINYEAR <= year <= datetime.MAXYEAR
    is_month_valid = 1 <= month <= 12
    is_day_valid = 1 <= day <= days_in_month(year, month)
    
    
    #Returns the corresponding boolean based on the validity
    if is_year_valid and is_month_valid and is_day_valid:
        return True
    else:
        return False
    

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    
    #Checks if the dates are valid
    if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2):
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)
        
        #Checks whether the second date is earlier than first date, returns 0 if true
        if date2 < date1:
            return 0
        
        #Gets the days between the two dates
        difference = date2 - date1 
        
        return difference.days
    
    #Default return if invalid
    return 0
    
def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    
    #Check if the input date is valid
    if is_valid_date(year, month, day):
        birthday = datetime.date(year, month, day)
        today = datetime.date.today()
        
        #Checks if the birthdate is in the future
        if birthday > today:
            return 0
        
        return days_between(year, month, day, today.year, today.month, today.day)

    #Default return if invalid
    return 0
