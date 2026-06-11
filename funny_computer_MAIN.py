import webbrowser


#username
username = input("Username: ")

if username == "Admin":
    print("Valid Username")
    print(" ")
else:
    print("Invalid Username")
    
#password
password = input("Password: ")

if password == "Admin":
    print("Valid Password")
    print(" ")
else:
    print("Invalid Password")

print("Welcome to Python Inc. OS")

# Command loop - allows commands in any order
while True:
    command = input("C:/ ")
    
    if command == "run":
        print("Executing 'run'")
        print("Checking Software Requirements")
        print("Checking Hardware Requirements")
        print("Checking Server Requirements")
        print("Checking Client Requirements")
        print("All Systems Functional")
    
    elif command == "hacker_man":
        print("Executing 'hacker_man'")
        print("Checking Software Requirements")
        print("Checking Hardware Requirements")
        print("Checking Server Requirements")
        print("Checking Client Requirements")
        print("All Systems Functional")
    
    elif command == "shut_down":
        print("Shuting Down Python Inc. OS")
        break  # Exit the loop and end the program
    
    else:
        print("Invalid Command")
