# write your function here
def readable_timedelta(days):
    while days >= 7:
        week = days // 7
        days = days % 7
        return print(f"{week} week(s) and {days} day(s).")
    else:
        return print(f"{days} day(s).")


# test your function
print(readable_timedelta(14))
