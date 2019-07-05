def end(day):
    weekend=["Sunday","Saturday"]
    weekday=["Monday","Tuesday","Wednesday","Thursday","Friday"]
    if day in weekends:
        return ("yes")
    elif day in weekdays:
        return ("no")
    else:
        return ("Invalid")
day=str(input())
print(end(day))
