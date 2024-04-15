import os

root_path = r"/home/jd/Documents/GitRepo/notes-and-projects/Studying Notes/Python/Fluent Python/"
os.system(f"cd '{root_path}'")

for i in range(1,25):
    current_folder = f'Chapter_{i:>02}'
    os.system(f"mkdir {current_folder}")
    os.system(f"touch {current_folder}/notes.txt {current_folder}/scratch_pad.py")