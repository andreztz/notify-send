"""
Display a notification suitable for the platform being run on

Usage:
    from notify import notification
    notification('what you want said', title=':)', app_name='app name')
"""
import sys
from importlib import import_module


try:
    mod = import_module("." + sys.platform, __package__)
except:
    raise RuntimeError("Unsupported operating system: {}".format(sys.platform))


notification = getattr(mod, "Notification")

