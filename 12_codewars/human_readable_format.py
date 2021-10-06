# https://www.codewars.com/kata/52742f58faf5485cae000b9a/python

def format_duration(seconds):
    result = []

    # years, days, hours, minutes, seconds
    numbers = [0, 0, 0, 0, 0]
    words = ['years', 'days', 'hours', 'minutes', 'seconds']
    words_single = ['year', 'day', 'hour', 'minute', 'second']

    # NOW
    if seconds == 0:
        return 'now'
    # years
    numbers[0] = seconds // (365 * 24 * 3600)
    seconds = seconds % (365 * 24 * 3600)
    # days
    numbers[1] = seconds // (24*3600)
    seconds = seconds % (24*3600)
    # hours
    numbers[2] = seconds // 3600
    seconds = seconds % 3600
    
    # minutes
    numbers[3] = seconds // 60
    seconds = seconds % 60
    # seconds
    numbers[4] = seconds % 60

    
    
    for index, number in enumerate(numbers):
        result.append(str(number) + ' '+ (words_single[index] if number == 1 else words[index])) if number > 0 else None
    
    result = ', '.join(result[:-1]) + ' and ' + result[-1] if len(result) > 1 else result[0]
    

    return result
if __name__ == '__main__':
    print(format_duration(1))
    print(format_duration(62))
    print(format_duration(120))
    print(format_duration(3600))
    print(format_duration(3662))

