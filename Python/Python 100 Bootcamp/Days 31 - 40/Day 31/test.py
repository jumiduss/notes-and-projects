import json

top_words = {}
with open("data/greek_10k.json", "r") as file_to_read:
    top_words = json.load(file_to_read)
    
# with open("password/data.json", "r") as data_file:
#     # json.dump(new_data, data_file, indent=4)
#     data = json.load("password/data.json")

# for key in top_words.keys():
#     if not top_words[key]["has_learned"]:
#         print(key)

print([key for key in top_words.keys() if not top_words[key]["has_learned"]])