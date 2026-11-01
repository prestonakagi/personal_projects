"""See if any overlaps in events during a day.
If there are, then list those events by priority."""

from datetime import datetime as dt
# import csv

from csv_read_process import read_and_process_csv

raw_events = read_and_process_csv("personal_projects\\convention_scheduling_2026") # relative path

print(raw_events)

NAME_INDEX = 0
DAY_INDEX = 1
START_TIME_INDEX = 2
END_TIME_INDEX = 3
ROOM_INDEX = 4
NICKNAME_ROOM_INDEX = 5
KIND_INDEX = 6
DAILY_PRIORITY_INDEX = 7

# For each day, make dictionary of day:[[start_times], [end_times]].
day_times_dict = {}

# get list of days and convert them to datetime obj
days_list = [dt.strptime(raw_events[i][DAY_INDEX], "%m/%d/%Y") for i in range(1, len(raw_events))]

unique_days_set = set(days_list)
# convert set to list and sorted ascending
unique_days = sorted(list(unique_days_set))
print(f"\n{unique_days=}")

time_lists = [[] for _ in range(len(unique_days) * 2)]
print(f"\n{len(days_list)=}\n{len(raw_events)=}\n{days_list=}")

# Convert times values to integers and append to respective lists.
for i, j in zip(range(0, (len(days_list) + 1)), range(1, (len(days_list) + 1))): # skip header row
    if days_list[i] == unique_days[0]:
        time_lists[0].append(int(raw_events[j][START_TIME_INDEX]))
        time_lists[1].append(int(raw_events[j][END_TIME_INDEX]))
    elif days_list[i] == unique_days[1]:
        time_lists[2].append(int(raw_events[j][START_TIME_INDEX]))
        time_lists[3].append(int(raw_events[j][END_TIME_INDEX]))
    elif days_list[i] == unique_days[2]:
        time_lists[4].append(int(raw_events[j][START_TIME_INDEX]))
        time_lists[5].append(int(raw_events[j][END_TIME_INDEX]))

# count number of events per day
day_one_count = len(time_lists[0])
day_two_count = len(time_lists[2])
day_three_count = len(time_lists[4])
# print(f"\n{day_one_count=} {time_lists[0]=}\n{day_two_count=} {time_lists[2]=}\n{day_three_count=} {time_lists[4]=}")

# bracket indexes of each day


"""
match #'Day':

case

case

case
"""