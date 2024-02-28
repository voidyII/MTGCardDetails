from webreq import api_call

def error_handling():
    print("Something went wrong :(")

def boolval_input(input):
    if (input == "y"):
        return True
    elif (input == "n"):
        return False
    else:
        error_handling()
        return

def user_workflow():
    print ("Welcome to Magic: The Gathering Card Details\n") #TODO
    print ("In case you are unsure what to do, press h for help or read the ReadMe file\n") #TODO
    print ("Do you want to download the Default Cards from Scryfall? (y/n): ")
    
    DC_input = input()
    DC_val = boolval_input(DC_input)

    if (DC_val == False):
        print ("Do you want to download All Cards from Scryfall? (y/n): ")
        AC_input = input()
        AC_val = boolval_input(AC_input)

    #TODO