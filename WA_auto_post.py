from datetime import datetime, timedelta
from random import randint
from time import sleep
import pywhatkit as wk
import codecs

# read data from file and split into list of strings
with open('phones and groups.txt', 'r') as f:
    data = f.read().splitlines()

# read the message from a file including emoji
with codecs.open('message.txt', 'r', 'utf-8') as f:
    msg = f.read()

# print the time when while loop starts
print('Started at: ' + str(datetime.now()))

# for each 50 lines in data, send a message to the phone or group and after that take a 30 minutes break and repeat
while len(data) > 0:
    # check length of data and if it less than 50 set variable to length of data
    if len(data) < 50:
        num = len(data)
    # if data is more than 50, set variable to 50
    else:
        num = 50
    for i in range(0, num):
        # get current time, add random seconds between 90 and 120 to it and split it into hours, and minutes # this script will automatically send the message add some more time 
        time = datetime.now() + timedelta(seconds=randint(90, 120))
        hours = time.hour
        minutes = time.minute
        # specify if data[0] is a phone number or group id
        if data[0].startswith('+'):
            wk.sendwhatmsg(data[0], message=msg, time_hour=hours, time_min=minutes)
        else:
            wk.sendwhatmsg_to_group(data[0], message=msg, time_hour=hours, time_min=minutes)
        # print the phone number or group id and the message that was sent and time it was sent
        print(f'Message was sent to {data[0]}, the message {msg}, sent in {hours}:{minutes}')

        # remove the first element of the list
        data.pop(0)
    # stop program for 30 minutes if data is more than 50
    if len(data) > 0:
        print('Stoping for 30 minutes')
        sleep(1800)
    # print the time when the program stopped
    print(f'Program stopped at {datetime.now()}')
    # print the number of lines left in the list
    print(f'{len(data)} lines left')
    # print a new line
    print()
    # print a line of dashes
    print('-' * 50)
    # print a new line
    print()
# after while is finished, print the time when the program finished
print(f'Program finished at {datetime.now()}')



