def startupOutput():
    print("Welcome to the weight loss app")
    print("What would you like to do?")
    print("Get, add, update, or delete an ingredient/recipe? Type 'R'")
    print("Get, add, update, or delete a day? Type 'D'")
    print("Do CTRL + C or type q in any input to quit at anytime")

def ingredientUsageOptions():
    print("What option do you want to do?")
    print("Get specific ingredient or food: -g <INGREDIENT> (Note max of 25 characters)")
    print("Get all ingredients or foods: -g")
    print("Add new ingredient or food: -a")  # Then we should ask name, amount, and unit seperately 
    print("Update ingredient: -u") # Similar to -a, but also allow for there to be no input for or unit     

def ingredientAddOptions():
    print("Enter information as follows: <NAME> <AMOUNT> <UNIT>")
    print("Name must be less than 25 characters, amount a decimal or whole number (no fractions)")
    # if time permits, add a statement here about all units allowed and validation for it in user interaction .py 

def ingredientUpdateOptions(flag):
    if flag == True:
        print("For the following, the name must be less than 25 characters")
    else:
        print("Enter the following: <AMOUNT> <UNIT>")
        print("Amount is a float with 2 points of precsion")

