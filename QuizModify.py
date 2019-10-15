usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
for name in range(len(usernames)):
    usernames[name] = usernames[name].lower().replace(' ', '_')
print(usernames)