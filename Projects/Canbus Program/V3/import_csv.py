import json
import pandas as pd


file_names = ["btn_prs","btn_rls","d_ccw","d_cw"]
sub_dict_names = ["Press","Release","CCW","CW"]

output_dict = {}

def fill_in_bytes(byte_set):
    """
    Fills in the trailing bytes of the 8 byte message with the max value. 
    """
    
    work_set = byte_set
    
    while len(work_set) < 8:
        work_set += [0xFF]
                
    return work_set

for gen_index, file in enumerate(file_names):

    # Opening the csv with pandas
    with open(f"csv_sets/{file}.csv","r") as file:
        file_info = pd.read_csv(file,index_col="Button")
        file_info.drop('Byte 1', axis=1, inplace=True)

    # Iterating over all rows
    for row,data in file_info.iterrows():

        # If the button doesn't exist, create it, otherwise, add this sub category
        
        if int(row) not in list(output_dict.keys()):
            output_dict[int(row)] = {sub_dict_names[gen_index]:{}}
        else:
            output_dict[int(row)][sub_dict_names[gen_index]] = {}

        # Test if the byte sets are complete.
        try:
            # Setting completed set to 
            row_list = [int(byte_val,16) for byte_val in data if isinstance(byte_val,str)]
            
        except (TypeError, ValueError):
            # Setting incomplete sets to the description string
            row_list = data.iloc[0]

        # If this is a button push / pull message
        if isinstance(row_list,list) and len(row_list) > 6:
            msg_set = []
            
            # Creating 3 messages based on the speed
            for i in range(3,6):
                speed_msg = [row_list[0],0xFF,row_list[1],row_list[2]]
                msg_set.append(fill_in_bytes(speed_msg))

        # The only other data messages are dial messages
        elif isinstance(row_list,list):
            row_list.insert(1,0xFF)
            msg_set = fill_in_bytes(row_list)

        # All other messages describe the missing bytes
        else:
            msg_set = row_list

        print(msg_set)
        output_dict[int(row)][sub_dict_names[gen_index]] = msg_set

with open("output.json","w") as file:
    json.dump(output_dict, file, indent=4)