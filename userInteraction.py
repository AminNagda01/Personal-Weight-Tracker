from libraries import *

def main():

    # Get the inital option selection from user 
    try:
        option = inputLib.initalOptionSelection()
        print(option)
    except ValueError as e:
        print(e)
        return
    
    # Check what which option to do
    match option:
        case 'r':
            outputLib.ingredientUsageOptions() #print options
            ingredientOption = inputLib.ingredientInputSelection()

        case 'd':
            pass
        case _:
            raise ValueError("Incorrect option passed from input")
    

if __name__ == "__main__":
    main()