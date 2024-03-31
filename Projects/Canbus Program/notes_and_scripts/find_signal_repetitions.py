import pandas as pd
import json
import sys
# df = pd.read_csv("Controller Reverse Engineering 01.csv", index_col=False)
# new_df = df[['Time Stamp','ID']]

# # Used to create json of time stamps where the broadcast repeats
# pattern_to_match = [1537,1540,1547,1549,1552,1555,1569,1665,1697]
# repeated_frames_index = []

# def find_broadcast_pattern(index,frame):
    
#     new_set = frame.iloc[[index,index+1,index+2,index+3,index+4,index+5,index+6,index+7,index+8]]
    
#     is_matching = True
#     i=0
#     while is_matching:
#         if i == 9:
#             break
        
#         if int(new_set.iloc[i,1],16) != pattern_to_match[i]:
#             is_matching = False
#             break
        
#         i+=1
    
#     if is_matching:
#         repeated_frames_index.append(str(frame.iloc[index,0]))

# for idx in range(0,len(df)-10,):
#     find_broadcast_pattern(idx,new_df)

# with open("notes/repetition_times.json", "w") as file:
#     json.dump(repeated_frames_index,file)
# repeated_deltas_in_seconds = []


# Opens the json list and computes the time deltas

df = pd.read_json("notes/repetition_times.json")

deltas = []
delta_ranges = []
for i in range(0, len(df)-1):
    this_time_stamp = int(df.iloc[i,0])
    next_time_stamp = int(df.iloc[i+1,0])
    this_delta = next_time_stamp - this_time_stamp
    deltas.append(this_delta)
    if this_delta < 525000:
        delta_ranges.append((this_time_stamp,next_time_stamp))        
            
with open("notes/repetition_deltas.json", "w") as file:
    json.dump(deltas,file)


def reduce_ranges(tuple_list):

    if len(tuple_list) < 2:
        return[tuple_list]
    
    a = tuple_list.pop(0)
    b = tuple_list.pop(0)
    
    
    if a[1] == b[0]:
        new_list = [(a[0],b[1])] + tuple_list
        return reduce_ranges(new_list)
    else:
        return [a] + reduce_ranges([b] + tuple_list)
    
sys.setrecursionlimit(10000)
reduced_range = reduce_ranges(delta_ranges)

with open("notes/test_dict.json","w") as file:
    json.dump(reduced_range, file, indent=4)

# new_range_set = []
# range_change = True
# num_changes = 0

# while range_change:
#     for i in range(0,len(delta_ranges)-1):
#         this_range = delta_ranges[i][1]
#         this_range_min_incl = this_range[0]
#         this_range_max_excl = this_range[1]
        
#         next_range = delta_ranges[i+1]
#         next_range_min_incl = next_range[0]
#         next_range_max_excl = next_range[1]
        
#         if this_range_max_excl == next_range_min_incl:
#             new_range_set.append((this_range_min_incl,next_range_max_excl))
#             num_changes += 1
    
#     if num_changes == 0:
#         range_change = False
