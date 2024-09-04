"""
    Author: Amin 
    Purpose: To take user input, send it to apis, and output what is returned 
    Bugs: None
    Acknowledgements: 
"""

MAX_INGREDIENT_LENGTH_COMMAND = 28

MIN_INGREDIENT_COMMAND_LEN = 2

MAX_ADD_INGREDIENT_LEN = 41 # 25 for name + 6 for float amount (rounded to 2 dec) + 10 unit length max

MAX_ADD_INGREDIENTS_ARGS = 3

MAX_INGREDIENT_NAME_LEN = 25 

# Seperate input getter to properly strip any inputs 
def getUserInput(prompt: str) -> str: 
    return input(prompt).strip()

# Gets initial input and checks it
def initalOptionSelection(): 
    while True:
        response = getUserInput("Enter your option: ").lower() 
        if len(response) != 1:
            print("Expected R or D as inputs, got improper length")
        if response == 'r' or response == 'd' or response == 'q':
            print("")
            return response
        else:
            print("Expected R or or D as inputs, got something else")

def ingredientInputSelection():
    while True:
        response = getUserInput("Enter your options: ").lower()

        if response == 'q':
            return response

        # If the argument is less than the size of a command (like "-a")
        elif len(response) < MIN_INGREDIENT_COMMAND_LEN:
            print("Invalid agrument, please use flags provided")
        
        elif len(response.split()) == 2:
            if len(response) > MAX_INGREDIENT_LENGTH_COMMAND:
                print("Ingredient has too many characters")
            else:
                return response
        
        elif response == "-g" or response == "-a" or response == "-u":
            print("")
            return response

        # If command is not one the above 
        else:
            print("Invalid agrument, only -g, -a, -u allowed")
   
def ingredientAddOptions():

    while True:
        response = getUserInput(": ").lower()

        if len(response) > MAX_ADD_INGREDIENT_LEN: 
            print("Check length requirments again and re-enter")
        else: 
            parts = response.split()
            # Check if we have exactly MAX_ADD_INGREDIENTS_ARGS arguements  
            if len(parts) != MAX_ADD_INGREDIENTS_ARGS:
                print("Check that you have exactly 4 arguments")
            else:
                return parts          

def ingredientUpdateGetName():
    
    while True:
        response = getUserInput("Enter the ingredient to update: ").lower()

        if len(response) > MAX_INGREDIENT_NAME_LEN:
            print("Name too long, retry")
        else:
            return response

def ingredientUpdateGetOthers():

    while True:
        response = getUserInput("Enter values now: ").lower() 
        parts = response.split()
        dictToRet = {}

        if len(parts) != 2:
            print("Two arguments needed")
        else:
            try:
                value = float(parts[0])
                value = f"{value:.2f}"
                dictToRet["amount"] = value

                if len(parts[1]) > 10: 
                    print("Unit must be less than 10 chars long")
                else:
                    dictToRet["unit"] = parts[1]
                    return dictToRet
            except: 
                print("Something went wrong with your amount, check that its a number with maximum 2 decimal places")