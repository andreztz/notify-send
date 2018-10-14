"""
Display a notification suitable for the platform being run on
Usage:
    from notify import Notification
    Notification('what you want said')
"""

from sys import platform


# Platform-specific imports
if platform == "android":
    from jnius import autoclass

if platform == "macosx":
    import Foundation
    import objc
    import AppKit

elif platform == "linux":
    from .linux.notify import SendNotify

elif platform == "win32":
    from .win32 import WindowsBalloonTip


class NotificationAndroid:
    def __call__(self, title, message):
        """ Displays a native Android notification """
        AndroidString = autoclass("java.lang.String")
        PythonActivity = autoclass("org.renpy.android.PythonActivity")
        NotificationBuilder = autoclass("android.app.Notification$Builder")
        Drawable = autoclass("net.clusterbleep.notificationdemo.R$drawable")
        icon = Drawable.icon
        noti = NotificationBuilder(PythonActivity.mActivity)
        # noti.setDefaults(Notification.DEFAULT_ALL)
        noti.setContentTitle(AndroidString(title.encode("utf-8")))
        noti.setContentText(AndroidString(message.encode("utf-8")))
        noti.setSmallIcon(icon)
        noti.setAutoCancel(True)
        nm = PythonActivity.mActivity.getSystemService(
            PythonActivity.NOTIFICATION_SERVICE
        )
        nm.notify(0, noti.build())


# UNTESTED !!!
# From http://stackoverflow.com/questions/12202983/\
# working-with-mountain-lions-notification-center-using-pyobjc


class NotificationOsx:
    def __call__(self, title, message):
        NSUserNotification = objc.lookUpClass("NSUserNotification")
        NSUserNotificationCenter = objc.lookUpClass("NSUserNotificationCenter")
        notification = NSUserNotification.alloc().init()
        notification.setTitle_(str(title))
        # notification.setSubtitle_(str(subtitle))
        notification.setInformativeText_(message)
        notification.setSoundName_("NSUserNotificationDefaultSoundName")
        # notification.setHasActionButton_(False)
        # notification.setOtherButtonTitle_("View")
        # notification.setUserInfo_({"action":"open_url", "value":url})
        NSUserNotificationCenter.defaultUserNotificationCenter().setDelegate_(
            self
        )
        NSUserNotificationCenter.defaultUserNotificationCenter().scheduleNotification_(
            notification
        )


class NotificationLinux:
    """ Displays a notification using the Gtk API """

    def __call__(self, title, message):
        SendNotify(title, message)


class NotificationWindows:
    """ Displays a notification using the win32 API """

    def __call__(self, title, message):
        WindowsBalloonTip(title, message)


# Platform-specific searches
if platform == "android":
    Notification = NotificationAndroid()

if platform == "macosx":
    Notification = NotificationOsx()

elif platform == "linux":
    Notification = NotificationLinux()

elif platform == "win32":
    Notification = NotificationWindows()
