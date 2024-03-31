import pandas as pd
from numpy import nan
import json

file_names = ["buttons_press.csv","buttons_release.csv","dials_ccw.csv","dials_cw.csv"]
section_names = ["Press","Release","CCW","CW"]
dict_set = {}

for i in range(len(section_names)):
    # Selecting the file based on for loop index i
    this_file = file_names[i]
    
    # Creating a pandas data frame with a standardized index value across all sets, and then replaces any nan.
    data_frame = pd.read_csv(f"csv_sets/{this_file}", sep=',').set_index(['Button'])
    data_frame.replace({nan: ""},inplace=True)
    
    # Iterates through the rows with the csv-set
    for j, data in data_frame.iterrows():
        
        # If the index does not currently exist in the dictionary, add it.
        if j not in dict_set.keys():
            dict_set[j]={}
            
        # Turns the sheet's row data into a list
        data_list = data.to_list()
        
        # Initiates the return list with blanks due to csvs only being populated with critical bytes
        return_list = [0xFF]*7
                
        # This cleans the byte data when values are unknown, or when buttons do not use can communications.
        try:
            int(data_list[2])
            for idx,k in enumerate(data_list):
                if k == "":
                    continue
                elif k == "cycles":
                    return_list[idx] = k
                else:
                    return_list[idx] = int(k,16)
                    
            dict_set[j][section_names[i]] = return_list
            

        except (TypeError,ValueError):
            if data_list[2] == "No Response":
                dict_set[j][section_names[i]] = "Needs Testing"
            else:
                dict_set[j][section_names[i]] = data_list[2]




with open("testing.json","w")as file:
    json.dump(dict_set,file,indent=4)

