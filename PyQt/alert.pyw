import sys
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *

app = QApplication(sys.argv)

try:
    due = QTime.currentTime()
    message = "Alert!"
    if len(sys.argv) < 2:
        raise ValueError
    hours, mins = sys.argv[1].split(":")
    due = QTime(int(hours), int(mins))
    while QTime.currentTime() < due:
        print "ping"
        if not due.isValid():
            raise ValueError
        if len(sys.argv) > 2:
            message = " ".join(sys.argv[2:])
        time.sleep(20) # 20 seconds
except ValueError:
    message = "Usage: alert.pyw HH:MM [optional message]" # 24hr clock


label = QLabel("<font color=red size=72><b>" + message + "</b></font>")
label.setWindowFlags(Qt.SplashScreen)
label.show()
QTimer.singleShot(60000, app.quit) # 1 minute
app.exec_()
