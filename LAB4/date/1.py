from datetime import datetime, timedelta

today = datetime.now()
fivedays = today - timedelta(days = 5)

fivedays_upd = fivedays.strftime("%d-%m-%Y")

print(fivedays_upd)