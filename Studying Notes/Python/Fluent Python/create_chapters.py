

# STEP 1: Create the File Path

import fitz
import os
import json

pdf_file_path = r"/home/jd/Documents/Books_and_PDFs/Textbooks/Programming/Python/fluent_python_second_edition.pdf"
root_path = r"/home/jd/Documents/GitRepo/notes-and-projects/Studying Notes/Python/Fluent Python/test"
os.system(f"cd '{root_path}'")

reader = fitz.open(pdf_file_path)

toc_list = reader.get_toc()

def toc_item(the_list):
    """Returns a list item"""
    n = 0
    length = len(toc_list)
    while n < length:
        yield the_list[n]
        n += 1
    raise IndexError

def get_head(value):
    return int(value)

toc_iter = toc_item(toc_list)
next_iter = next(toc_iter)
current_iter = 0
notes_lines = []
notebook_blocks = []
markdown_source: str = ''
markdown_cell = {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
}

code_cell = {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {},
   "outputs": [],
   "source": []
}
notebook_dict = {
 "cells": [
  
  ],
 "metadata": {
  "kernelspec": {
   "display_name": "projects",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

while True:

    current_iter = next_iter
    
    try:
        next_iter = next(toc_iter)
    except IndexError:
        next_iter = 0

    if get_head(current_iter) == 1:
        
        folder_name = current_iter[1]
        os.mkdir(folder_name)
        
        if next_iter not in [0, 1]:
            os.chdir(folder_name)
    
    elif get_head(current_iter) == 2:
        
        if get_head(next_iter) < get_head(current_iter):
            with open('notes.txt', 'w') as notes:
                notes.writelines(notes_lines)
            with open('examples.ipynb', 'w') as examples:
                json.dump(notebook_dict,)
                
                
            os.chdir("../")