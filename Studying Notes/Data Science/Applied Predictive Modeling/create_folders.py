import os

dir_path = "/home/jd/Documents/GitRepo/notes-and-projects/Studying Notes/Data Science/Applied Predictive Modeling"
os.chdir(dir_path)
for i in range(21):
    if i > 2:
        chapter_name = f'chapter_{i}'
        folder_path = f"sections/{chapter_name}"
        try:
            os.mkdir(folder_path)
        except FileExistsError:
            print("Already_Made")
        finally:
            rel_file_path = f"{folder_path}/{chapter_name}.tex"
            with open(rel_file_path, 'w') as file:
                print(f"\\subfile({rel_file_path})")
                file.writelines([
                    "\\documentclass[../main.tex]{subfiles}\n",
                    "\\begin{document}\n",
                    "\n\n\n\n\n\n\n",
                    "text\n"
                    "\\end{document}"
                ])