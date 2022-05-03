# Time function
def add_time(time, add):
    # convert time into minutes
    time = time.split()
    time = time[0].split(':')
    time = int(time[0]) * 60 + int(time[1])
    # convert add time into minutes
    add = add.split()
    add = add[0].split(':')
    add = int(add[0]) * 60 + int(add[1])
    # new time
    hour = (time + add) // 60
    minutes = (time + add) % 60
    solution = f'{hour}:{minutes}'
    return solution


print(add_time("3:00 PM", '3:10'))
