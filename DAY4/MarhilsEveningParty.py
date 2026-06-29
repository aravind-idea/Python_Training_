day = input("enter day").strip()
att = int(input("enter attendees"))

def csp(day, attendees):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday"]
    weekends = ["Friday", "Saturday", "Sunday"]

    if day not in weekdays and day not in weekends:
        return "invalid"

    if day in weekdays:
        if 700 <= att <= 1000:
            return "successful"
        else:
            return "unsuccessful"

    if day in weekends:
        if att >= 1500:
            return "successful"
        else:
            return "unsuccessful"

