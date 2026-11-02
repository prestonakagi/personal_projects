"""See if any overlaps in events during a day.
If there are, then list highest priority of each group of overlapping events."""

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
print(f"\n{day_one_count=} {time_lists[0]=}\n{day_two_count=} {time_lists[2]=}\n{day_three_count=} {time_lists[4]=}")

# bracket indexes of each day
# day_one_overlap_indexes, day_two_overlap_indexes, day_three_overlap_indexes = [], [], []

def find_day_overlap_indexes(day_start_times, day_end_times):
    '''
    csv file should have each day's events' times in ascending order.
    Compare start and end times of events in a day 
    and return a list of lists of indexes, 
    and each inner list contains indexes of events that overlap each other.
    
    Parameters:
    day_start_times: list of integers of events' start times in 24 hr format
    day_end_times: list of integers of events' end times in 24 hr format    
    '''
    groups_of_events = []
    overlapping_events_indexes = []
    for i in range(len(day_start_times) - 1):
        if day_start_times[i + 1] <= day_start_times[i] <= day_end_times[i + 1] and day_start_times[i + 1] <= day_end_times[i] <= day_end_times[i + 1]:
            overlapping_events_indexes.append(i)
            overlapping_events_indexes.append(i + 1)
        elif day_start_times[i] <= day_start_times[i + 1] <= day_end_times[i]:
            overlapping_events_indexes.append(i)
            overlapping_events_indexes.append(i + 1)
        elif day_start_times[i] <= day_end_times[i + 1] <= day_end_times[i]:
            overlapping_events_indexes.append(i)
            overlapping_events_indexes.append(i + 1)
        else:
            # make overlapping_events_indexes into a set, then a list.
            unique_overlapping_events_indexes = list(set(overlapping_events_indexes))
            groups_of_events.append(unique_overlapping_events_indexes)
            overlapping_events_indexes = [] # reset indexes list

    # compare second last start time to last start time and potentially append to overlapping_events_indexes
    if day_start_times[-1] <= day_start_times[-2] <= day_end_times[-1] and day_start_times[-1] <= day_end_times[-2] <= day_end_times[-1]:
        overlapping_events_indexes.extend([(len(day_start_times) - 2), (len(day_start_times) - 1)])
        unique_overlapping_events_indexes = sorted(list(set(overlapping_events_indexes)))
        groups_of_events.append(unique_overlapping_events_indexes)
        overlapping_events_indexes = [] # reset indexes list
    elif day_start_times[-2] <= day_start_times[-1] <= day_end_times[-2]:
        overlapping_events_indexes.extend([(len(day_start_times) - 2), (len(day_start_times) - 1)])
        unique_overlapping_events_indexes = sorted(list(set(overlapping_events_indexes)))
        groups_of_events.append(unique_overlapping_events_indexes)
        overlapping_events_indexes = [] # reset indexes list
    elif day_start_times[-2] <= day_end_times[-1] <= day_end_times[-2]:
        overlapping_events_indexes.extend([(len(day_start_times) - 2), (len(day_start_times) - 1)])
        unique_overlapping_events_indexes = sorted(list(set(overlapping_events_indexes)))
        groups_of_events.append(unique_overlapping_events_indexes)
        overlapping_events_indexes = [] # reset indexes list
    # append to overlapping_events_indexes regardless if entered any of above conditionals.
    else:
        # make overlapping_events_indexes into a set, then a list, then sorted the list.
        unique_overlapping_events_indexes = sorted(list(set(overlapping_events_indexes)))
        groups_of_events.append(unique_overlapping_events_indexes)
        overlapping_events_indexes = [] # reset indexes list

    # Remove empty inner lists: an empty list [] evaluates to False, while a list with elements evaluates to True
    clean_groups_of_events = [x for x in groups_of_events if x]
   
    return clean_groups_of_events

day_one_overlap_indexes = find_day_overlap_indexes(time_lists[0], time_lists[1])
print(f"\n{day_one_overlap_indexes=}")
day_two_overlap_indexes = find_day_overlap_indexes(time_lists[2], time_lists[3])
print(f"\n{day_two_overlap_indexes=}")
day_three_overlap_indexes = find_day_overlap_indexes(time_lists[4], time_lists[5])
print(f"\n{day_three_overlap_indexes=}")

# use overlap indexes to iterate thru raw events and list priority numbers
def get_overlap_highest_priority(raw_events, day_overlap_indexes, day_number: int):
    '''
    For one day, for each group of overlapping events, finds lowest number of priority (highest priority) and 
    returns raw events index for the event with highest priority.

    Parameters:
    raw_events: read_and_process_csv function's list of lists
    day_overlap_indexes: find_day_overlap_indexes functions's list of lists
    days_number: number of day of schedule, integer of 1 or greater with 1 being first day.

    Return: list of integer indexes that have highest priority of each overlap group
    '''
    highest_priority_indexes = []
    groups_priorities = []
    days_counts =[0, day_one_count, day_two_count] # don't add last day's count to list
    day_count_sum = sum(days_counts[0:day_number])

    for i in range(len(day_overlap_indexes)):
        for overlap_index in day_overlap_indexes[i]:
            # add 1 to overlap_index to skip header row. add day_count_sum to start at first event of day, if overlap_index = 0.
            groups_priorities.append(raw_events[1 + day_count_sum + overlap_index][DAILY_PRIORITY_INDEX])
        # get minimum value in priorities list, then get its index
        lowest_number_priority = min(groups_priorities)
        lowest_number_priority_index = groups_priorities.index(lowest_number_priority)
        highest_priority_indexes.append(day_overlap_indexes[i][lowest_number_priority_index])
        # reset groups_priorities
        groups_priorities = []

    return highest_priority_indexes

day_two_priority_event_indexes = get_overlap_highest_priority(raw_events, day_two_overlap_indexes, 2)
# print(f"\n{day_two_priority_event_indexes=}")
# TODO: when printing or gathering from raw_events, add one to each of ..._priority_event_indexes to skip header row.
day_one_priority_event_indexes = get_overlap_highest_priority(raw_events, day_one_overlap_indexes, 1)
day_three_priority_event_indexes = get_overlap_highest_priority(raw_events, day_three_overlap_indexes, 3)
print(f"\n{day_one_priority_event_indexes=}\n{day_two_priority_event_indexes=}\n{day_three_priority_event_indexes=}")

# for each day and each overlapping events, print all overlapping events' names and then the event with highest priority and all its info.
def display_overlapping_events_and_highest_priorities(raw_events, day_overlap_indexes, overlap_highest_priorities, date: str, day_number: int):
    '''
    For each day and each overlapping events, 
    print all overlapping events' names and 
    then the event with highest priority and all its info.

    Parameters:
    raw_events: read_and_process_csv function's list of lists
    day_overlap_indexes: find_day_overlap_indexes functions's list of lists
    overlap_highest_priorities: get_overlap_highest_priority functions's list of indexes
    date: string of date
    days_number: number of day of schedule, integer of 1 or greater with 1 being first day.
    '''
    # for raw_events's outer list, add one to each of indexes to skip header row. add day_count_sum to start at first event of day, if overlap_index = 0.
    # days_counts: list of all day_count (Example: global variable day_one_count)
    days_counts =[0, day_one_count, day_two_count] # don't add last day's count to list
    day_count_sum = sum(days_counts[0:day_number])
    # overlapping_events_names = [raw_events[1 + day_count_sum + n][NAME_INDEX] for group in day_overlap_indexes for n in group]
    overlapping_events_names = []
    for group in day_overlap_indexes:
        overlapping_events_names.append("-" * 70) # to delineate groups of overlapping events in a day.
        for n in group:
            overlapping_events_names.append(raw_events[1 + day_count_sum + n][NAME_INDEX])

    highest_priorities_events = [] # will be list of str
    priority_event_info = ""
    for row in overlap_highest_priorities:
        for i in range(7):
            # add day_count_sum to start at first event of day, if overlap_index = 0.
            priority_event_info += (raw_events[1 + day_count_sum + row][i] + "  ")
        highest_priorities_events.append(priority_event_info)
        priority_event_info = "" # reset

    print(f"\nOn {date}, the following events overlap:")
    for event in overlapping_events_names:
        print(f"{event}")
    print(f"\nThe following events in respective overlaps have top priority:")
    for i in range(7):
        print(f"{raw_events[0][i]}", end=" ") # header row except priority
    for whole_event in highest_priorities_events:
        print(f"\n{whole_event}")

day_one_priorities_display = display_overlapping_events_and_highest_priorities(raw_events, day_one_overlap_indexes, day_one_priority_event_indexes, "03DEC26", 1)
day_two_priorities_display = display_overlapping_events_and_highest_priorities(raw_events, day_two_overlap_indexes, day_two_priority_event_indexes, "04DEC26", 2)
day_three_priorities_display = display_overlapping_events_and_highest_priorities(raw_events, day_three_overlap_indexes, day_three_priority_event_indexes, "05DEC26", 3)