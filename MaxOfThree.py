while True:
    def findmax(num1, num2, num3):
        if num1.isnumeric() and num2.isnumeric() and num3.isnumeric():
            num1, num2, num3 = int(num1), int(num2), int(num3)
            if num1 > num2 and num1 > num3:
                return print(f"The maximum number is {num1}. \n")
            elif num2 > num1 and num2 > num3:
                return print(f"The maximum number is {num2}. \n")
            elif num3 > num1 and num3 > num2:
                return print(f"The maximum number is {num3}. \n")
            else:
                return print("2 or 3 Numbers are equal. \n")
        else:
            return print("Not number(s). \n")


    findmax(input("Value 1: "), input("Value 2: "), input("Value 3: "))
