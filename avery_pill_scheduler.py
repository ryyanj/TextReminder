import atexit
import logging
from pytz import timezone
import pytz
import os
from twilio.rest import Client
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

#######REMEMBER WHEN DEBUGGING THE SCHEDULER MESSAGES WITH TWILIO IT TAKES UP TO TWO MINUTES FOR THE CODE TO BE FULLY DEPLOYED#######

logging.basicConfig()
utc = pytz.utc
# Find these values at https://twilio.com/user/account
account_sid = os.environ.get('ACCOUNT_SID', None)
auth_token = os.environ.get('AUTH_TOKEN', None)
client = Client(account_sid, auth_token)
scheduler = BackgroundScheduler()
class AveryPillScheduler():

    def avery_pill_job(self):
        scheduler.start()
        scheduler.add_job(
            func=self.print_pill_message,
            #use this timer when daylight savings time ends in November 
            trigger=CronTrigger(year='*', month='*', day='*', week='*', day_of_week='*', hour='16', minute='30', second='00',timezone=utc),
            #use this timer when daylight savings time begins in March 
            #trigger=CronTrigger(year='*', month='*', day='*', week='*', day_of_week='*', hour='15', minute='30', second='00',timezone=utc),
            id='printing_job',
            name='Print pill message every day at 11:30 AM Eastern Time',
            replace_existing=True)
        #UTC IS FIVE HOURS AHEAD BUT WHEN DAYLIGHT SAVINGS TIME KICKS IN AROUND MARCH IT IS ONLY 4 HOURS AHEAD!!!
        # Shut down the scheduler when exiting the app
        atexit.register(lambda: scheduler.shutdown())

    def print_pill_message(self):
        print('pill func was called')
        #+14782513043 - ryyan's phone number
        #+14782922142 - twilio number
        #+12514228131 - avery's phone number
        try:
            client.api.account.messages.create(to="+12514228131",
                                               from_="+14782922142",
                                               body="Don't forget to take your pill babe! I love you! ")
            print('sent successfully')
        except Exception as error:
            print(error)
