"""
Display a notification suitable for the platform being run on
Usage:
    from notify import Notification
    Notification('what you want said', title=':)', app_name='app name')
"""
import sys


# imports by Platform
if sys.platform == "linux":
    from .linux import NotificationLinux as notify
elif sys.platform == "win32":
    from .win32 import NotificationWindows as notify
else:
    raise RuntimeError("Unsupported operating system: {}".format(sys.platform))


def notification(message, title="", app_name=None):
    """ Displays a notification """
    notify(message, title, app_name)
