from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1)

today_upd = today.strftime("%d-%m-%Y")
yesterday_upd = yesterday.strftime("%d-%m-%Y")
tomorrow_upd = tomorrow.strftime("%d-%m-%Y")

print("Yesterday date:", yesterday_upd)
print("Current date: ", today_upd)
print("Tomorrow date: ", tomorrow_upd)