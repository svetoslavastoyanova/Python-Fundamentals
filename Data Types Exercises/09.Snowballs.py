n = int(input())
max = -9999
result = 0
max_snow = 0
max_time = 0
max_quality = 0

for snow in range(1, n + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    result = (snowball_snow//snowball_time) ** snowball_quality
    if result > max:
        max = result
        max_snow = snowball_snow
        max_time = snowball_time
        max_quality = snowball_quality
print(f"{max_snow} : {max_time} = {max} ({max_quality})")