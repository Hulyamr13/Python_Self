good_morning = 'Good Morning!'
good_afternoon = 'Good Afternoon!'
good_evening = 'Good Evening!'
invalid_hour = 'You typed in an invalid hour!'

hour = int(input())

if hour < 0 or hour > 24:
    print(invalid_hour)
else:
    if hour < 9:
        print(good_morning)
    elif hour < 18:
        print(good_afternoon)
    else:
        print(good_evening)
