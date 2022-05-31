# Time function
def add_time(time, add):
    # extract the data and check for errors
    suffix = None
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
        if hour == 0:
            hour = 12
        hour = hour - (hour // 12) * 12

    if suffix % 2 == 0:
        suffix = 'PM'
    else:
        suffix = 'AM'
    solution = f'{hour}'.zfill(2) + ':' + f'{minutes}'.zfill(2) + f' {suffix}'
    return solution


print(add_time("12:50 pm", '25:30'))
