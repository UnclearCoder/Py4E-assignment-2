# Time function
def add_time(time, add, day=None):
    # Split time and add
    time = time.split()
    add = add.split(':')
    term = time[1]
    time = time[0].split(':')
    days = 0
    # Convert to 24 hour time
    if term == 'PM' and time[0] != '12':
        time[0] = int(time[0]) + 12
    # Add time  
    time[0] = int(time[0]) + int(add[0])
    time[1] = int(time[1]) + int(add[1])
    # Convert to 12 hour time
    # check minutes
    if time[1] >= 60:
        time[0] = time[0] + 1
        time[1] = time[1] - 60
    # check hours and add days
    if time[0] >= 24:
        days = time[0] // 24
        time[0] = time[0] - (24 * days)
    # add daytime term
    if time[0] > 12:
        time[0] = time[0] - 12
        term = 'PM'
    elif time[0] == 12:
        term = 'PM'
    elif time[0] == 0:
        time[0] = 12
        term = 'AM'
    else:
        term = 'AM'
    
    # add day of the week
    if day != None:
        day = day.lower()
        week = {'sunday': 0, 'monday': 1, 'tuesday': 2, 'wednesday': 3,'thursday': 4, 'friday': 5, 'saturday': 6}
        day = week[day]
        day = day + days
        if day > 6:
            day = day - (7 * (day // 7))
        for key, value in week.items():
            if value == day:
                day = key.capitalize()
                break
    else:
        day = None

    # convert back to string
    time[0] = str(time[0])
    time[1] = str(time[1])
    if len(time[1]) == 1:
        time[1] = '0' + time[1]
    new_time = f'{time[0]}:{time[1]} {term}'
    if day != None:
        new_time = f'{new_time}, {day}'
    if days == 1:
        new_time = f'{new_time} (next day)'
    elif days > 1:
        new_time = f'{new_time} ({days} days later)'

    return new_time

if __name__ == '__main__':
    actual = add_time("11:59 PM", "24:05", "Wednesday")
    expected = "12:04 AM, Friday (2 days later)"
    print(actual)
    print(expected)
    print(actual == expected)