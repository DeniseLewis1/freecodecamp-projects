def add_time(start, duration, start_day=None):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    start_hour = int(start.split(":")[0])
    start_minute = int(start.split()[0].split(":")[1])
    start_time_of_day = start.split()[1]
    duration_hour = int(duration.split(":")[0])
    duration_minute = int(duration.split(":")[1])

    new_minute = start_minute + duration_minute 
    new_hour = start_hour + duration_hour
    new_time_of_day = "AM"
    days_later = 0
    
    # Convert hours to 24-hour format
    if start_time_of_day == "PM":
        new_hour += 12

    # Adjust minutes if calculated value is greater than or equal to 60
    if new_minute >= 60:
        new_hour += new_minute // 60
        new_minute %= 60
    
    # Add '0' before minute if calculated value is less than 10
    if new_minute < 10:
        new_minute = '0' + str(new_minute)

    # Adjust hours if calculated value is greater than or equal to 24
    if new_hour >= 24:
        days_later = new_hour // 24
        new_hour %= 24
    
    # Convert hours to 12-hour format
    if new_hour > 12:
        new_hour -= 12
        new_time_of_day = "PM"
    elif new_hour == 12:
        new_time_of_day = "PM"
    elif new_hour == 0:
        new_hour = 12
        new_time_of_day = "AM"

    new_time = str(new_hour) + ":" + str(new_minute) + " " + new_time_of_day

    # Display day of week in result if start day is provided
    if start_day:
        new_day_index = (days.index(start_day.capitalize()) + days_later) % 7
        new_time += f", {days[new_day_index]}"

    # Display days later
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 0:
        new_time += f" ({days_later} days later)"

    return new_time

print(add_time('2:59 AM', '9:01', 'saturDay'))