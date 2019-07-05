def end(day):
    weekend=["Sunday","Saturday"]
    weekday=["Monday","Tuesday","Wednesday","Thursday","Friday"]
    if day in weekend:
        return ("yes")
    elif day in weekday:
        return ("no")
    else:
        return ("Invalid")
day=str(input())
print(end(day))
