centuries = int(input())
DAYS_IN_YEAR = 365.2422

years = centuries * 100
days = int(years * DAYS_IN_YEAR)
hours = days * 24
minutes = hours * 60
print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")