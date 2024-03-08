import os

def file_setup():
    print ("Please enter the file directory for output files (leave blank to use Downloads directory): ")
    path_input = input()
    if (path_input == ""):
        filepath = os.getcwd()
    elif (os.path.isdir(path_input) == True):
        filepath = path_input
    else:
        print ("error, directory does not exist")

    print ("Do you want to save the output as json (leave blank for default format)? (y/n): ")
    jsonformat_input = input()
    if (jsonformat_input == "y"):
        jsonformat = True
    elif (jsonformat_input == "n"):
        jsonformat = False
    elif (jsonformat_input == ""):
        jsonformat = True
    else:
        print ("error") #error handling work tbd

    print ("Do you want to save the output as csv (leave blank for default format)? (y/n): ")
    csvformat_input = input()
    if (csvformat_input == "y"):
        csvformat = True
    elif (csvformat_input == "n"):
        csvformat = False
    elif (csvformat_input == ""):
        csvformat = False
    else:
        print ("error") #error handling work tbd

    with open(".env", "w") as temp_outf:
        temp_outf.write(f"path={filepath}")
        temp_outf.write(f"jsonformat={jsonformat}")
        temp_outf.write(f"csvformat={csvformat}")

def file_change():
    print ("tbd, change file settings")