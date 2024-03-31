import json
import pandas as pd


file_names = ["btn_prs","btn_rls","d_ccw","d_cw"]
sub_dict_names = ["Press","Release","CCW","CW"]

output_dict = {}

def fill_in_bytes(byte_set):
    """
    Fills in the trailing bytes of the 8 byte message with the max value. 
    """
    while len(byte_set) < 8:
        byte_set += [0xFF]
                
    return byte_set


for gen_index, file in enumerate(file_names):

    # Opening the csv with pandas
    with open(f"With No Studying/csv_sets/{file}.csv","r") as file:
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
        
        # If the data is a list of data bytes
        if isinstance(row_list,list):
            
            # Insert the cycles bytes as 0xFF
            row_list.insert(1,0xFF)
                
            # If this is a dial messages
            if len(row_list) > 5:
                speed_vals = row_list[4:]
                id = row_list[:4]
                lead_word = sub_dict_names[gen_index]
                
                for i, speed in enumerate(speed_vals):
                    idx = i + 1
                    output_dict[int(row)][f"{sub_dict_names[gen_index]}s{i}"] = fill_in_bytes(id+[speed])
                    
                # {f"{sub_dict_names[gen_index]}s{i+1}":fill_in_bytes(id+[speed])}
                continue
            
            # All other messages are button push / button pull
            else:
                msg_set = fill_in_bytes(row_list)

        # All other messages describe the missing bytes
        else:
            msg_set = row_list

        print(msg_set)
        output_dict[int(row)][sub_dict_names[gen_index]] = msg_set

with open("output.json","w") as file:
    json.dump(output_dict, file, indent=4)