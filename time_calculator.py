# Time function
def add_time(time, add, day=None):
    # fix for parrameters: time, add, day
    if day is None:
        ctx = True
        day = 'Monday'
    else:
        ctx = False
    suffix = None
    metric = ''
    day = day.capitalize()
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Extraction for data and check for errors
    for i in week:
        if day == i:
            day = week.index(i)
    if type(day) != int:
        print('Error: invalid metric')
        quit()
    time = time.split()
    if time[1].upper() == 'PM':
        suffix = 2
    if time[1].upper() == 'AM':
        suffix = 1
    if type(suffix) != int:
        print('Error: please specify if it\'s "AM" or "PM"')
        quit()

    # check for valid time and change into int
    time = time[0].split(':')
    for index, value in enumerate(time):
        try:
            time[index] = int(value)
        except ValueError:
            print('Error: please specify a valid time')
            quit()
    # convert hour to minutes
    time = time[0] * 60 + time[1]

    # convert add time into minutes and check for errors
    add = add.split()
    add = add[0].split(':')
    for index, value in enumerate(add):
        try:
            add[index] = int(value)
        except ValueError:
            print('Error: please specify a valid time')
            quit()
    add = int(add[0]) * 60 + int(add[1])

    # new time
    unit = time + add
    hour = unit // 60
    minutes = unit % 60

    # change from minutes to hour
    if hour > 1:
        suffix = suffix + hour // 12
        hour = hour - (hour // 12) * 12
    if hour == 0:
        hour = 12
    if suffix % 2 == 0:
        suffix1 = 'PM'
    else:
        suffix1 = 'AM'
    if 2 < suffix <= 4:
        metric = '(Next day)'
        day = day + 1
    if suffix > 4:
        suffix = suffix // 2
        metric = f'({suffix} days later)'
        day = day + suffix
    if day > 6:
        day = day - 7 * (day // 6)

    # print the result
    if ctx is True:
        solution = f'{hour}'.zfill(2) + ':' + f'{minutes}'.zfill(2) + f' {suffix1}' + f' {metric}'
        return solution
    else:
        solution = f'{hour}'.zfill(2) + ':' + f'{minutes}'.zfill(2) + f' {suffix1},' + f' {week[day]}' + f' {metric}'
        return solution

if __name__ == '__main__':
    print(add_time("6:30 PM", "205:12"))
