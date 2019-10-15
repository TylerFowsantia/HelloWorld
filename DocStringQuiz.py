def readable_timedelta(days):
    """Convert days to weeks variable and remaining days to remainder variable """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} days(s)".format(weeks, remainder)


print(readable_timedelta(20))
