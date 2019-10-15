def upper_lower(string):
    return print("Lowercase:", sum(map(str.islower, string)), "\n", print("Uppercase:", sum(map(str.isupper, string))))


upper_lower("The Quick Brown Fox")