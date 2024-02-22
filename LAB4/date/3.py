from datetime import datetime

current_date = datetime.now()
current_date = current_date.replace(microsecond = 0)

print(current_date) 