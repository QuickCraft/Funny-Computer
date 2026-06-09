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
#commands
command = input("C:/ ")

if command == "run":
    print("Executing 'run'")
    print("Checking Software Requirements")
    print("Checking Hardware Requirements")
    print("Checking Server Requirements")
    print("Checking Client Requirements")
    print("All Systems Functional")

else:
        print("Invalid Command")

command = input("C:/ ")

if command == "hacker_man":
    print("Executing 'hacker_man'")
    print("Checking Software Requirements")
    print("Checking Hardware Requirements")
    print("Checking Server Requirements")
    print("Checking Client Requirements")
    print("All Systems Functional")
else:
    print("Invalid Command")


command = input("C:/ ")

if command == "shut_down":
    print("Shuting Down Python Inc. OS")
else:
    print("Invalid Command")

url = "https://www.onlineide.pro/playground/python"
webbrowser.open_new_tab(url)