
import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "DRINK WATER !!",
            message = "Just a gentle reminder for you - You need to drink water right now.",
            app_icon = "glassicon.ico",
            timeout = 5
        )
        time.sleep(60*60) #This makes the code to run every hour and remind you.