import time
import psutil
from plyer import notification

plugin = False

battery = psutil.sensors_battery()
percent = battery.percent

def popup(message):
    notification.notify(
        title = "Battery Percentage",
        message = message,
        timeout = 20
    )


# if percent < 50:
#     popup("Less than 50\n"+str(percent)+"% Battery percent remaining")
# else:
#     popup("More than 50\n"+str(percent)+"% Battery percent remaining")

def checker():

    if percent > 80:
        popup("Please plug out your charger\n"+str(percent)+"% Battery percent remaining")
    else:
        popup("Keep on charging\n"+str(percent)+"% Battery percent remaining")

    time.sleep(300)
    return checker()


checker()