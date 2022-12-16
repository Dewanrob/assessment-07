def valid_input(num):
    if num.isdigit() == True and int(num) in [i for i in range(1,6)]:
        option = int(num)
        return option
    else: 
        print("Not a valid option")


def option_one():
    print('''
        Add a Holiday
        =============
        ''')
    name = input("Holiday Name: ")
    date = input("Holiday Date (YYYY-MM-DD): ")
    return name, date

def option_two():
    print('''
        Remove a Holiday
        ================
        ''')
    name = input("Enter holiday name: ")
    return name

def option_three():
    print('''
        Save Holiday List
        =================
        ''')
    action = input("Are you sure you want to save your changes? [y/n]: ")
    return action

def option_four():
    print('''
        View Holidays
        =============
        ''')
    year = input('Which year?: ')
    week = input('Which week? #[1-52, Leave blank for the current week]: ')
    return year, week

def option_five():
    print('''
        Exit
        ====
        ''')
    reply = input("Are you sure you want to exit? [y/n]: ")
    return reply
