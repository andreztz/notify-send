"""
Display a notification suitable for the platform being run on
Usage:
    from notify import Notification
    Notification('what you want said')
"""
import sys


# imports by Platform
if sys.platform == "linux":
    from .linux import NotificationLinux as send
elif sys.platform == "win32":
    from .win32 import NotificationWindows as send
else:
    raise RuntimeError("Unsupported operating system: {}".format(sys.platform))


class Notification:
    """ Displays a notification """

    def __call__(self, message, **kwargs):
        send(message, **kwargs)


Notification = Notification()
