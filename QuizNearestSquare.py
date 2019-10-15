limit = 40
nearest_square = 0
x = 0
# write your while loop here
while nearest_square < limit:
    x += 1
    nearest_square = x ** 2
else:
    x -= 1
    nearest_square = x ** 2
print(nearest_square)
print("Square Root: ", x)
