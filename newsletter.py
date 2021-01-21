import schedule
import time
from bot import newsletter
print('schedule worked')

schedule.every().day.at("15:45").do(newsletter)

while True:
    schedule.run_pending()
    time.sleep(1)