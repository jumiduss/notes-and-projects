# Step 1
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

# Step 2
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text. 
#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable.

# Step 3
#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

# Step 4 
#TODO-1: Import and print the logo from art.py when the program starts.
#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#TODO-3: What happens if the user enters a number/symbol/space?
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?


logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


def check_error(shift_int,letter_position):
    position = 0
    if shift_int > 0 and (letter_position + shift_int) > 25:
        position = shift_int + letter_position - 26
    elif shift_int < 0 and (position + shift_int) < 0:
        position = shift + letter_position + 26
    else:
        position = shift_int + letter_position
    return position

def shifter(direction,text,shift,alphabet):

    return_string = ''
    shift = shift % 26

    shifted_type = 'encoded'
    if direction == 'decode':
        shift = 0 - shift
        shifted_type = 'decoded'

    if shift == 0:
        return_string = text
    else:
        for i in text:
            if i != ' ':
                position = alphabet.index(i)
                position = check_error(shift_int=shift,letter_position=position)
                loop_char = alphabet[position]   
            else:
                loop_char = ' '
            return_string += loop_char

    return print("The {} text is {}".format(shifted_type,return_string))

def main_program():

    mod_check = 105
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    while mod_check != 1:

        if (mod_check % 3) == 0:
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
            if direction in ['e','d','encode','decode']:
                mod_check /= 3
            else:
                print("Please chose a coding type that exists...")
                continue 

        if (mod_check % 5) == 0:
            text = input("Type your message:\n").lower()

            for i, letter in enumerate(text):
                if letter not in alphabet:
                    if letter != ' ':
                        print("Only use letters in the alphabet...")
                        print(alphabet)
                        break
                if i == (len(text) - 1):
                    mod_check /= 5
            continue
            
        if (mod_check % 7) == 0:
            shift = input("Type the shift number:\n")
            try:
                shift = int(shift)
            except ValueError:
                print("please provide a number...")
            else:
                mod_check /= 7

    shifter(direction=direction,text=text,shift=shift,alphabet=alphabet)

def pre_program():

    print(logo)
    play = True
    while play:
        main_program()
        incorrect = True
        while incorrect:
            choice = input("Would you like to code again? \n  (y)es or (n)o\n  ").lower()
            if choice not in ['y','n','yes','no']:
                print("Please choose (Y)ES or (N)O")
            elif choice in ['y','yes']:
                break
            else:
                play = False
                incorrect = False
    print("Thanks for playing!")

pre_program()