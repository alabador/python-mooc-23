# Write your solution here
from datetime import datetime, timedelta

filename = input('filename: ')
starting_date_str = input("starting date: ")
starting_date = datetime.strptime(starting_date_str, "%d.%m.%Y")
screen_time = {}

days = int(input('days: '))

print("please type in screen time in minutes on each day (TV, PC, Mobile): ")
for i in range(days):
    add_day = timedelta(days=i)
    device_time = input(f"Screen time {starting_date + add_day}: ")
    screen_time[starting_date + add_day] = device_time.replace(' ', '/')

total_min = 0

for key in screen_time:
    current = screen_time[key]
    split = current.split('/')
    for i in split:
        actual_min = int(i)
        total_min += actual_min

avg_min = total_min / (days)

with open(filename, 'w') as time_log:
    start = datetime.strftime(starting_date, "%d.%m.%Y")
    end_date = starting_date + timedelta(days=days - 1)
    end_fixed = datetime.strftime(end_date, "%d.%m.%Y")
    time_log.write(f"Time period: {start}-{end_fixed}\n")
    time_log.write(f"Total minutes: {total_min}\n")
    time_log.write(f"Average minutes: {avg_min}\n")
    for key in screen_time:
        temp1 = datetime.strftime(key, "%d.%m.%Y")
        time_log.write(f"{temp1}: {screen_time[key]}\n")