while True:
    login = input("Login or Register? ").lower()
    login_data = []
    if login == 'register' or login == 'r':
        first_name = input("First Name: ").capitalize()
        last_name = input("Last Name: ").capitalize()
        print("-----------------")
        username = input("Please provide Username: ")
        password = input("Password: ")
        with open('data.txt', 'a') as database:
            database.writelines(first_name + " " + last_name + " " + username + " " + password + "\n")
            print("--------------------")
            continue
    elif login == 'login' or login == 'l':
        login_user = input("Username: ")
        login_password = input("Password: ")
        with open('data.txt', 'r') as base:
            for line in base:
                line = (line.strip("\n"))
                login_data.append(line.split())
                for item in login_data:
                    if login_user != item[2] and login_password != item[3]:
                        result = "Username and password are incorrect."
                    elif login_user != item[2] and login_password == item[3]:
                        result = "Username is incorrect."
                    elif login_user == item[2] and login_password != item[3]:
                        result = "Password is incorrect."
                    else:
                        result = "Welcome " + item[0].capitalize() + "."
                        break
        print(result)
    else:
        print("Please input an option.")
        print("------------------")
        continue
