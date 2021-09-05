def time_extract(start):   # Extract input
    start_time, ampm = start.split()
    hour, minute = start_time.split(':')
    return hour, minute, ampm


def add_time(start, duration, starting=None):  # return new_time
    hour, minute, ampm = time_extract(start)
    hour_duration, min_duration = duration.split(':')
    temp_ampm = ampm

    res_hour = int(hour) + int(hour_duration)
    res_min = int(minute) + int(min_duration)
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',\
                 'Friday', 'Saturday', 'Sunday']
    period = 0  # variable to check new days

    if res_min >= 60:
        res_min -= 60
        res_hour += 1

    temp = res_hour

    while res_hour > 12:
        res_hour -= 12

    while temp >= 12:
        temp -= 12
        ampm = 'AM' if ampm == 'PM' else 'PM'
        period += 1

    if period % 2 != 0:  # Check new day
        if temp_ampm == 'PM':
            period += 1
        else:
            period -= 1

    day_count = int(period / 2)

    if starting:
        week_day_index = week_days.index(starting.lower().capitalize())
        new_day_index = week_day_index + day_count
        week_day = week_days[new_day_index % 7]
        new_week = ', ' + str(week_day)
    else:
        new_week = ''
    if day_count == 0:
        days = ''
    elif day_count == 1:
        days = ' (next day)'
    else:
        days = f' ({day_count} days later)'

    new_time = f'{res_hour }:{str(res_min).zfill(2)} {ampm}{new_week}{days}'

    return new_time