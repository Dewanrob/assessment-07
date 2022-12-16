def valid_input(num):
    if num.isdigit() == True and int(num) in [i for i in range(1,6)]:
        option = int(num)
        return True, option
    else: 
        return False, num

def valid_reply(reply):
    if str in ['yn']:
        return True, reply
    else:
        return False, reply


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
    reply = input("Are you sure you want to save your changes? [y/n]: ")
    return reply

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
    if valid_reply(reply) == True:
        return True, reply
    else:
        return False, reply
