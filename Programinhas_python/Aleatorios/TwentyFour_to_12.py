def real_clock(time24: str) -> str('hh:mm'):
    if ':' not in time24 or time24.count(':') > 1:
        return 'Formato inválido'

    hour, minute = time24.split(':')
    hour = int(hour)
    
    if hour > 23 or hour < 1 or int(minute) > 59:
        return 'Hora inválida'
    if hour > 12:
        hour = str(hour - 12) + ':' + minute + 'PM'
    else:
        hour = str(hour) + ':' + minute + 'AM'
    return hour
