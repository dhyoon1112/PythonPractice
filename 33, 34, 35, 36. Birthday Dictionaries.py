import json
import datetime
import calendar
from bokeh.plotting import figure, show, output_file
from collections import Counter


# Saving data to a json file
birthdaylist = {'Daniel Y': '1994-05-02', 'Ben Franklin': '1706-01-17'}

with open('info.json', 'w') as f:
    json.dump(birthdaylist, f)


def birthdays2():

    with open('info.json','r') as b:
        info = json.load(b)

    print("Welcome to the Birthday Dictionary, we have the birthdays of...")
    for _ in info.keys():
        print(_)

    while True:
        answer = input("Who's Birthday would you like to see? ")

        if answer in info:
            print("{}'s birthday is {}".format(answer,info[answer]))
            break
        
        else:
            print("{} is not a valid entry".format(answer))


def addbirthday():

    with open('info.json','r') as b:
        info = json.load(b)

    answer = input("The following birthdays are available: " + str([_ for _ in info.keys()]) + "\n" + "Do you wish to add another Birthday? (Yes or No) ")

    while True:
        
        if answer == "Yes":
            newname = input("What is the name? ")
            newbday = input("What is the Birthday? (YYYY-MM-DD) ")
            info[newname] = newbday

            with open('info.json','w') as b:
                json.dump(info, b)

            break

        elif answer == "No":
            break


def monthcounter():
    
    with open('info.json','r') as b:
        info = json.load(b)

    x = [datetime.datetime.strptime(info[_], "%Y-%m-%d").month for _ in info.keys()]
    xcounter = Counter(x)
    
    y = [xcounter[_] for _ in x]

    '''
    for _ in x:
        print("There are {} birthday(s) in {}".format(xcounter[_],calendar.month_name[_]))
    '''

    p = figure()
    p.vbar(x=x, top=y, width=.5)
    show(p)


birthdays2()
addbirthday()
monthcounter()


''' Saving to the json file
birthdaylist = {'Daniel Y': '1994-05-02', 'Ben Franklin': '1706-01-17'}

with open('info.json', 'w') as f:
    json.dump(birthdaylist, f)
'''


'''Birthday List without the json file
def birthdays():
    
    bdays = {'Daniel Y': '1994-05-02', 'Ben Franklin': '1706-01-17'}

    print("Welcome to the Birthday Dictionary, we have the birthdays of...")
    for _ in bdays.keys():
        print(_)

    while True:
        answer = input("Who's Birthday would you like to see? ")

        if answer in bdays:
            print("{}'s birthday is {}".format(answer,bdays[answer]))
            break
        else:
            print("{} is not a valid entry".format(answer))
'''
