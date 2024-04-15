import numpy as np

def hex_spacing():
    num = 6
    offset = 4
    
    while num >= 0:
        yield num * " "
        num -= 2
        
    while num < 0 and num > -8:
        yield (num + offset) * " "
        offset += 4
        num -= 2

def hex_length(set):
    num = 0
    while num < len(set):
        yield set[num]
        num += 1


def square_spacing(n:int):
    num = 0
    while num < (n * 3):
        yield ''
        num += 1
    

def square_length(n:int):
    num = 0
    while num < n:
        yield n
        num += 1



def diagram(set,row_len,row_type):
    
    if row_type == 'hex':
        string_set = [f"<{entry}>" for entry in set]
        spacing = hex_spacing()
        this_row_count = hex_length(row_len)
    
    elif row_type == 'grid':
        string_set = [f"[{entry}]" for entry in set]
        spacing = square_spacing(row_len)
        this_row_count = square_length(row_len)
    else:
        return "not a grid type"
    
    print_str = ''
    row_entry_count = 0
    max_entry_count = next(this_row_count)
    
    for str_entry in string_set:
        if row_entry_count == 0:
            lead_space = f"\n{next(spacing)}"
        else:
            lead_space = ''
        row_entry_count += 1
        
        print_str += lead_space + f"{str_entry}".ljust(4)
        if row_entry_count == max_entry_count:
            row_entry_count = 0
            try:
                max_entry_count = next(this_row_count)
            except StopIteration:
                continue

    return print_str


def user_choices(directions, ids, r_len, r_type):
    
    user_choices = list(tuple(ids))
    choice_number = 0
    print(diagram(user_choices,r_len, r_type))
    
    while True:

        print(f"For cell {ids[choice_number]}")
        current_choice = choose_direction(directions)
        user_choices[choice_number] = current_choice
        choice_number += 1
        if choice_number == len(ids):
            break
    print(diagram(user_choices,r_len,r_type))
    return user_choices

def choose_cell(cell_ids):
    while True:
        cell_choice = input('Which cell would you like to edit?\n')
        if cell_choice not in cell_ids:
            print("Not a valid choice")
            continue
        return cell_ids.index(cell_choice)

def choose_direction(dir_set):
    dirs = "[" + ",".join(dir_set) + "]"
    while True:
        user_dir = input(f"Choose a direction from {dirs}: ")
        
        if user_dir not in dir_set:
            continue
        
        return dir_set.index(user_dir)
    
def update_choices(cell_ids, directions, user_choices):
    
    while True:
        response = input('Would you like to update a cell? (y/n)')
        
        if response not in ['y','n']:
            print("Not a valid choice")
            continue
        elif response == 'n':
            break
        else:
            cell_position = choose_cell(cell_ids)
            user_choices[cell_position] = choose_direction(directions)









valid_directions = ['n','e','s','w']
cell_ids = ['a','b','c','d','e','f','g','h','i']
row_length = 3
row_type = 'grid'

choices = user_choices(valid_directions,cell_ids,row_length,row_type)
update_choices(cell_ids,valid_directions,choices)


system = np.array([
    [1,1,0,1,1,0,0,0,0],
    [1,1,1,1,1,1,0,0,0],
    [0,1,1,0,1,1,0,0,0],
    [1,1,0,1,1,0,1,1,0],
    [1,1,1,1,1,1,1,1,1],
    [0,1,1,0,1,1,0,1,1],
    [0,0,0,1,1,0,1,1,0],
    [0,0,0,1,1,1,1,1,1],
    [0,0,0,0,1,1,0,1,1]])

solution = np.linalg.solve(system,choices)

solution = solution.tolist()
print(solution)

for i, cell in enumerate(solution):
    solution[i] = (
        360 * np.cos((cell) * (np.pi / 2)),
        360 * np.cos((cell) * (np.pi / 2))
    )

print(diagram(solution, row_length, row_type))