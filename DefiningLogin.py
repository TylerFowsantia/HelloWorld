while True:
    home = (input("L or R?"))
    login_data = []


    def register():
        first_name = input("First name: ").capitalize()
        last_name = input("Last name: ").capitalize()
        print("------------------")
        username = input("Please input Username: ")
        password = input("Password: ")
        with open('hello.txt', 'a') as database:
            database.writelines(first_name + " " + last_name + " " + username + " " + password + "\n")
            print("--------------------")


    def login():
        login1 = input("User: ")
        login2 = input("Pass: ")
        with open('hello.txt', 'r') as test:
            for ree in test:
                ree = (ree.strip("\n"))
                login_data.append(ree.split())
                for item in login_data:
                    if login1 != item[2] and login2 != item[3]:
                        result = "Username and password are incorrect."
                    elif login1 != item[2] and login2 == item[3]:
                        result = "Username is incorrect."
                    elif login1 == item[2] and login2 != item[3]:
                        result = "Password is incorrect."
                    else:
                        result = "Welcome " + item[0].capitalize() + "."
                        break
        return print(result)


    if home == 'login' or home == 'l':
        login()
    elif home == 'register' or home == 'r':
        register()
    else:
        print("Please select an option.")
        continue

