from pync import Notifier
import time

while True:
    Notifier.notify("Please sip some water!", title="💧 Water Reminder")
    time.sleep(60*30)
