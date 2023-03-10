import datetime
import json
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass
from functionality.functions import *
import re




class Holiday:
      
    def __init__(self, name, date):
        self.name = name 
        self.date = datetime.date.fromisoformat(date)      
        
    def __str__ (self):
        # String output
        string_date = str(self.date)
        return self.name, string_date
        # Holiday output when printed.
        
           

class HolidayList:
    def __init__(self):
       self.innerHolidays = []
       
   
    def addHoliday(self, holiday_obj):
        # Make sure holidayObj is an Holiday Object by checking the type
        if type(holiday_obj) != Holiday:
            raise 'Not a valid holiday.'
        else:
            new_holiday = holiday_obj.__str__()
            # Using the Holiday string method to create a list of dictionaries of holiday content
            value = {'Name' : new_holiday[0], 'Date' : new_holiday[1]}
            if value in self.innerHolidays:
                print('That holiday is already in the list.')
            else:
                self.innerHolidays.append(value)
                # print to the user that you added a holiday
                day = new_holiday[0]
                print(f"You have successfully added {day} to the holiday list.")



    def findHoliday(self, HolidayName, Date):
        # Find Holiday in innerHolidays
        for i in range(0, len(self.innerHolidays)): 
            for items in self.innerHolidays:
                if self.innerHolidays[i]['Name'] == HolidayName and self.innerHolidays[i]['Date'] == Date:
                    index = i
                    # Return Holiday
                    return self.innerHolidays[i]['Name'], self.innerHolidays[i]['Date'], index
                else:
                    pass

    def removeHoliday(self, HolidayName, Date):
        # Find Holiday in innerHolidays by searching the name and date combination.
        try:
            index = self.findHoliday(HolidayName, Date)[2]
            # remove the Holiday from innerHolidays
            self.innerHolidays.pop(index)
            day = HolidayName
            # inform user you deleted the holiday
            print(f"You successfully deleted {day} from the holiday list.")
        except: print("Holiday not found")
        
    def read_json(self):
        # Read in things from json file location
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
        
    def scrapeHolidays(self):
        results = []
        for year in range (2020,2025):
            url = 'https://www.timeanddate.com/holidays/us/' + str(year)
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            holiday_html = soup.find_all(['td', 'th'])
            # This returns a dictionary of holidays
            for i in range(0, len(holiday_html)):
                try:
                    results.append(
                        { 
                        'Date'      : str(year) + '-' + datetime.datetime.strptime(holiday_html[i-2].get_text()[0:3], '%b').strftime('%m') 
                                        + '-' + datetime.datetime.strptime(holiday_html[i-2].get_text()[3:5], '%d').strftime('%d'), 
                        'Name'      : holiday_html[i].find('a', href = re.compile('holidays')).get_text(),
                        'Type'      : holiday_html[i+1].get_text(),
                        'Details'   : holiday_html[i+2].get_text().replace('\xa0', '')
                        }   
                    )
                except:
                    pass
        for i in range (0, len(results)):
            holiday = Holiday(results[i]['Name'], results[i]['Date'])
            self.addHoliday(holiday)

    def numHolidays(self):
        # Return the total number of holidays in innerHolidays
        return int(len(self.innerHolidays))
        

    def filter_holidays_by_week(self, year, week_number):
        try:
            results = []
            for i in range(0, len(self.innerHolidays)):
                if week_year(self.innerHolidays[i]['Date'])[0] == week_number and week_year(self.innerHolidays[i]['Date'])[1] == year:
                    results.append(self.innerHolidays[i])
            # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
            # Week number is part of the the Datetime object
            sorted_results = sorted(results, key = lambda calendar_date: calendar_date['Date'])
            self.innerHolidays = sorted(self.innerHolidays, key = lambda calendar_date: calendar_date['Date'])
            # Cast filter results as list
            holidays = []
            for i in range (0, len(sorted_results)):
                holidays.append((sorted_results[i]['Name'], sorted_results[i]['Date']))
            # return your holidays
            return holidays
        except: "\n Invalid week, year combination."

    def displayHolidaysInWeek(self, year, week_number):
        # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
        holidayList = self.filter_holidays_by_week(year, week_number)
        try:
            calendar_year = year
            calendar_week = week_number
            print(f"These are the holidays for {calendar_year} week #{calendar_week}:")
            for i in range(0, len(holidayList)):
                print(holidayList[i][0], holidayList[i][1])
        except: print("Something went wrong")
        # self.filter_holidays_by_week(year, week_number)
        # Output formated holidays in the week. 
        # * Remember to use the holiday __str__ method.

    def getWeather(weekNum):
        pass
        # Convert weekNum to range between two days
        # Use Try / Except to catch problems
        # Query API for weather in that week range
        # Format weather information and return weather string.

    def viewCurrentWeek(self):
        pass
        # Use the Datetime Module to look up current week and year
        current_week = datetime.date.today().isocalendar()[1]
        current_year = datetime.date.today().isocalendar()[0]
        # Use your filter_holidays_by_week function to get the list of holidays 
        # for the current week/year
        # Use your displayHolidaysInWeek function to display the holidays in the week
        week = current_week
        self.displayHolidaysInWeek(current_year, current_week)
        # Ask user if they want to get the weather
        # If yes, use your getWeather function and display results





def main():
    # Large Pseudo Code steps
    # -------------------------------------
    # 1. Initialize HolidayList Object
    holiday_list = HolidayList()
    # 2. Load JSON file via HolidayList read_json function
    holiday_list.read_json()
    # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
    holiday_list.scrapeHolidays()
    initial_length = holiday_list.numHolidays()
    # 3. Create while loop for user to keep adding or working with the Calender
    with open("text/start-up.txt", 'r') as f:
        start_up = f.readlines()
        for words in start_up:
            print(words.format(count = initial_length))
    input('Press enter to continue: ')

    while True:
        # 4. Display User Menu (Print the menu)
        with open("text/main-menu.txt", 'r') as f:
            main_menu = f.readlines()
            for words in main_menu:
                print(words)
        # 5. Take user input for their action based on Menu a
        # check the user input for errors
        action = input("\n Please select an option: ")
        option = valid_input(action)
        if option == 1:
            name, date = option_one()
            try:
                # new_holiday = Holiday(name, date)
                new_holiday = Holiday(name, date)
                # HolidayList.addHoliday(new_holiday)
                holiday_list.addHoliday(new_holiday)
            except: print("\n Not a valid holiday")
        if option == 2:
            name = option_two()
            holiday_list.removeHoliday(name)
        if option == 3:
            reply = option_three() 
            if reply == 'y':
                holiday_list.save_to_json('holiday.json')
                initial_length = holiday_list.numHolidays()
                print("\n Your changes have been saved")
            elif reply == 'n':
                print("\n Your changes have been canceled")
            else:
                print('\n Not a valid option.')
                pass
        if option == 4:
            year, week = option_four()
            if week == '':
                holiday_list.viewCurrentWeek()
            else:
                holiday_list.displayHolidaysInWeek(year, week)    
        if option == 5:
            reply = option_five()
            if reply == 'y':
                final_length = holiday_list.numHolidays()
                if  final_length > initial_length:
                    print("\n You have made changes, if you were to leave now, they would be unsaved")
                    second_chance = input('\n Are you sure you want to exit? [y/n]')
                    if second_chance == 'y':
                            print("Fare thee well!")
                            break
                    elif second_chance == 'n':
                            continue
                    else:
                            print('That is not a valid input')
                else:
                    break
                break
            elif reply == 'n':
                pass
            else:
                print('Not a valid option.')
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




