"""
    Author: Amin 
    Purpose: To take user input, send it to apis, and output what is returned 
    Bugs: None
    Acknowledgements: 
"""

# Seperate input getter to properly strip any inputs 
def getUserInput(prompt: str) -> str: 
    return input(prompt).strip()

# Gets initial input and checks it
def initalOptionSelection(): 
    response = getUserInput("Enter your option: ").lower() 
    if len(response) != 1:
        raise ValueError("Expected R or D as inputs, got improper length")
    if response == 'r' or response == 'd':
        return response
    else:
        raise ValueError("Expected R or D as inputs, got something else")

def ingredientInputSelection():
    response = getUserInput("Enter your options: ").lower()
    

