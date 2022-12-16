import datetime
import json
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass
from functions import *



# -------------------------------------------
# Modify the holiday class to ho
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------
class Holiday:
      
    def __init__(self, name, date):
        self.name = name 
        self.date = datetime.date.fromisoformat(date)      
        # pass
    def __str__ (self):
        # String output
        string_date = str(self.date)
        return self.name, string_date
        # Holiday output when printed.
        # pass  
           
# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------
class HolidayList:
    def __init__(self):
       self.innerHolidays = []
       
   
    def addHoliday(self, holiday_obj):
        # Make sure holidayObj is an Holiday Object by checking the type
        if type(holiday_obj) != Holiday:
            raise 'Not a Holiday.'
        # Use innerHolidays.append(holidayObj) to add holiday
        else:
            new_holiday = holiday_obj.__str__()
            value = {'Name' : new_holiday[0], 'Date' : new_holiday[1]}
            if value in self.innerHolidays:
                print('That holiday is already in the list.')
            else:
                self.innerHolidays.append(value)
        # print to the user that you added a holiday
                day = new_holiday[0]
                print(f"You have successfully added {day} to the holiday list.")



    def findHoliday(self, HolidayName):
        # Find Holiday in innerHolidays
        for i in range(0, len(self.innerHolidays)): 
            for items in self.innerHolidays:
                if self.innerHolidays[i]['Name'] == HolidayName:
                    index = i
                    return self.innerHolidays[i]['Name'], index
                else:
                    pass
        # Return Holiday

    def removeHoliday(self, HolidayName):
        # Find Holiday in innerHolidays by searching the name and date combination.
        try:
            index = self.findHoliday(HolidayName)[1]
        # remove the Holiday from innerHolidays
            self.innerHolidays.pop(index)
        # inform user you deleted the holiday
            day = HolidayName
            print(f"You successfully deleted {day} from the holiday list.")
        except: print("Holiday not found")
        
    def read_json(self):  
        with open("holiday-seed.json", 'r') as f:
            holidays = json.load(f)
            # Use addHoliday function to add holidays to inner list.
            for i in range(0, len(holidays['holidays'])):
                seed_holidays = Holiday(holidays['holidays'][i]['name'], holidays['holidays'][i]['date'])
                self.addHoliday(seed_holidays)
  
        


    def save_to_json(self, filelocation):
        # Write out json file to selected file.
        holidays = {"Holidays" : self.innerHolidays}
        try:
            with open(filelocation, 'w') as f:
                json.dump(holidays, f, indent = 4)
        except: print("Not a vaild file location")
        
        
    def scrapeHolidays():
        pass
        # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
        # Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
        # Check to see if name and date of holiday is in innerHolidays array
        # Add non-duplicates to innerHolidays
        # Handle any exceptions.     

    def numHolidays(self):
        # Return the total number of holidays in innerHolidays
        return len(self.innerholidays)
        # pass
    
    def filter_holidays_by_week(year, week_number):
        pass
        # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
        # Week number is part of the the Datetime object
        # Cast filter results as list
        # return your holidays

    def displayHolidaysInWeek(holidayList):
        pass
        # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
        # Output formated holidays in the week. 
        # * Remember to use the holiday __str__ method.

    def getWeather(weekNum):
        pass
        # Convert weekNum to range between two days
        # Use Try / Except to catch problems
        # Query API for weather in that week range
        # Format weather information and return weather string.

    def viewCurrentWeek():
        pass
        # Use the Datetime Module to look up current week and year
        # Use your filter_holidays_by_week function to get the list of holidays 
        # for the current week/year
        # Use your displayHolidaysInWeek function to display the holidays in the week
        # Ask user if they want to get the weather
        # If yes, use your getWeather function and display results

    def Display(self):
        print(self.innerHolidays)





def main():
    pass
    # Large Pseudo Code steps
    # -------------------------------------
    # 1. Initialize HolidayList Object
    holiday_list = HolidayList()
    # 2. Load JSON file via HolidayList read_json function
    holiday_list.read_json()
    # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
    # 3. Create while loop for user to keep adding or working with the Calender
    while True:
    # 4. Display User Menu (Print the menu)
        with open("main-menu.txt", 'r') as f:
            main_menu = f.readlines()
            for words in main_menu:
                print(words)
    # 5. Take user input for their action based on Menu a
        action = input("Please select an option: ")
        bool, option = valid_input(action)
    # nd check the user input for errors
        if option == 1:
            name, date = option_one()
            # new_holiday = Holiday(name, date)
            new_holiday = Holiday(name, date)
            # HolidayList.addHoliday(new_holiday)
            holiday_list.addHoliday(new_holiday)
        if option == 2:
            name = option_two()
            holiday_list.removeHoliday(name)
        if option == 3:
            boolean, reply = option_three() 
            if boolean == True:
                if reply == 'y':
                    holiday_list.save_to_json('holiday.json')
                    print("Your changes have been saved")
                else:
                    print("Your changes have been canceled")
        if option == 4:
            option_four()
        if option == 5:
            boolean, reply = option_five()
            if boolean == True:
                if reply == 'y':
                    break
                else:
                    pass
        if bool == False:
            print("Not a valid option.")
    # elif valid_input(action)[0] == False:
    #     print('''

    #     Sorry, that is not a valid option.

    #     ''')
    #     main()
# 6. Run appropriate method from the HolidayList object depending on what the user input is
# 7. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 


if __name__ == "__main__":
    main();


# Additional Hints:
# ---------------------------------------------
# You may need additional helper functions both in and out of the classes, add functions as you need to.
#
# No one function should be more then 50 lines of code, if you need more then 50 lines of code
# excluding comments, break the function into multiple functions.
#
# You can store your raw menu text, and other blocks of texts as raw text files 
# and use placeholder values with the format option.
# Example:
# In the file test.txt is "My name is {fname}, I'm {age}"
# Then you later can read the file into a string "filetxt"
# and substitute the placeholders 
# for example: filetxt.format(fname = "John", age = 36)
# This will make your code far more readable, by seperating text from code.





