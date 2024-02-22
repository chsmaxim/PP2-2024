from datetime import datetime, timedelta

current_date = datetime.now()
threedays = current_date + timedelta(days = 3)

date_difference = threedays - current_date
date_difference_sec = date_difference.total_seconds()

print("date difference in sec: ", date_difference_sec)