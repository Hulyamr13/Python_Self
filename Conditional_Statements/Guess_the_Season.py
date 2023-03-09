# Get month and date inputs
month = input().lower()
date = int(input())

# Determine the season based on the given date and month
if (month == 'december' and date >= 21) or month == 'january' or month == 'february' or (month == 'march' and date < 20):
    season = 'winter'
elif (month == 'march' and date >= 20) or month == 'april' or month == 'may' or (month == 'june' and date < 21):
    season = 'spring'
elif (month == 'june' and date >= 21) or month == 'july' or month == 'august' or (month == 'september' and date < 22):
    season = 'summer'
elif (month == 'september' and date >= 22) or month == 'october' or month == 'november' or (month == 'december' and date < 21):
    season = 'autumn'

# Output the season name in pascal case
print(season.capitalize())
