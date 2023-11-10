# Скласти програму, яка переводить час із секунд, визначаючи повну кількість годин хвилин і секунд 
# (наприклад, час 5000 секунд це 1 година 23 хвилини 20 секунд 5000=1*3600+2*60+20).
# Input - 5000
# Otput_hours - 1
# Otput_minutes - 23
# Otput_seconds - 20

SECOND_IN_HOUR = 3600
SECOND_IN_MINUTE = 60

seconds_amount = int(input("Enter amount of second: "))

hours = seconds_amount//SECOND_IN_HOUR
minutes = (seconds_amount % SECOND_IN_HOUR) // SECOND_IN_MINUTE
seconds = seconds_amount % SECOND_IN_MINUTE

print(f"Seconds amount {seconds_amount}: hours = {hours}, minutes = {minutes}, seconds = {seconds}")