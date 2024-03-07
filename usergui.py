import dotenv
import os.path
import file_handler

class user_workflow():
    def error_handling():
        print("Something went wrong :(")

    def eval_input(input):
        if (input == "1"):
            #add function for last used settings
            print ("tbd")
        elif (input == "2"):
            user_workflow.dl_menu()
        elif (input == "3"):
            user_workflow.file_menu()
        elif (input == "y"):
            return True
        elif (input == "n"):
            return False
        elif (input == "h"):
            user_workflow.help_menu()
        else:
            user_workflow.error_handling()
        return
    
    def start_menu():
        if os.path.exists('.env'):
            pass
        else:
            file_handler.file_setup()

        print ("Welcome to Magic: The Gathering Card Details\n") #TODO
        print ("In case you are unsure what to do, press h for help or read the ReadMe\n") #TODO
        print ("\n")
        print ("1: Download with last used settings\n2: Download latest bulk file\n3: Change file settings\nh: Help Menu\n")
        choice_input = input()

        user_workflow.eval_input(choice_input)
    
    def dl_menu():
        print ("Do you want to download the Default Cards from Scryfall? (y/n): ")
    
        DC_input = input()
        DC_val = user_workflow.eval_input(DC_input)

        if (DC_val == False):
            print ("Do you want to download All Cards from Scryfall? (y/n): ")
            AC_input = input()
            AC_val = user_workflow.eval_input(AC_input)
    
    def help_menu():
        print ("This is the help menu.")

    def file_menu():
        print ("In this menu a myriad of file options can be set.")
        file_handler.file_change()