from libraries import *

def main():

    outputLib.startupOutput()

    # Get the inital option selection from user 
    option = inputLib.initalOptionSelection()
    
    # Check which option to do
    match option:

        case 'r':
            outputLib.ingredientUsageOptions() #print options
            ingredientOption = inputLib.ingredientInputSelection()

            # Get <Ingredient> 
            if len(ingredientOption.split()) > 2: # if we have more than 2 parts to this string (ie. -g <ingredient>)
                parts = ingredientOption.split()
                if len(parts) == 2:
                    pass # TODO: Send parts[1] to the api to get that ingredient, handle errors
                else:
                    raise ValueError("Invalid amount of arguments given when getting ingredient or food")
                
            # quit app 
            elif ingredientOption == "q":
                return

            # Add 
            elif ingredientOption == "-a":
                outputLib.ingredientAddOptions() 
                ingredientAddOptions = inputLib.ingredientAddOptions() 

                pass # TODO: Send the info at ingredientAddOptions[0 - 3] to the api, handle errors 

            # Update
            elif ingredientOption == "-u":
                outputLib.ingredientUpdateOptions(True) 
                response = inputLib.ingredientUpdateGetName()

                pass # TODO: call api to check if response exists in database use get/ingredient

                # Call the following if the name is a valid entry in db 
                # outputLib.ingredientUpdateOptions(False)
                # updatedContent = inputLib.ingredientUpdateGetOthers()
                # updatedContent["name"] = response 

                # Call put api here and use updatedContent dict values to fill it in 

            # Get all ingredients 
            elif ingredientOption == "-g":
                pass #TODO: Return all ingredients on api call 

        case 'q': 
            return 
        case 'd':
            pass
        case _:
            raise ValueError("Incorrect option passed from input")
    

if __name__ == "__main__":
    main()