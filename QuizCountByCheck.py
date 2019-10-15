start_num = 0
end_num = 20
count_by = 2
break_num = 0
# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to
#   check against end_num
if end_num > start_num:
    while break_num <= end_num:
        break_num = break_num + count_by
        result = break_num
else:
    result = "Your start number is greater than your end number. Please change the value."

print(result)
