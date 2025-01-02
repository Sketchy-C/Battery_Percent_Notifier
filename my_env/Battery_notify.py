import time
import psutil
from plyer import notification


battery = psutil.sensors_battery()
percent = battery.percent

def popup(message):
    notification.notify(
        title = "Battery Percentage",
        message = message,
        timeout = 20
    )


if percent < 50:
    popup("Less than 50\n"+str(percent)+"% Battery percent remaining")
else:
    popup("More than 50\n"+str(percent)+"% Battery percent remaining")

