# Display a notification suitab'le for the platform being run on
# Usage:
# from components.notification import Notification
# Notification('what you want said').notify()


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


class NotificationBase:

    def __init__(self, title='', message=''):
        self.title = title
        self.message = message

    def notify(self):
        ''' Echoes the message to the console '''
        print('Notification: {}\n{}'.format(self.title, self.message))


class NotificationAndroid(NotificationBase):

    def notify(self):
        ''' Displays a native Android notification '''
        AndroidString = autoclass('java.lang.String')
        PythonActivity = autoclass('org.renpy.android.PythonActivity')
        NotificationBuilder = autoclass('android.app.Notification$Builder')
        Drawable = autoclass('net.clusterbleep.notificationdemo.R$drawable')
        icon = Drawable.icon
        noti = NotificationBuilder(PythonActivity.mActivity)
        # noti.setDefaults(Notification.DEFAULT_ALL)
        noti.setContentTitle(AndroidString(self.title.encode('utf-8')))
        noti.setContentText(AndroidString(self.message.encode('utf-8')))
        noti.setSmallIcon(icon)
        noti.setAutoCancel(True)
        nm = PythonActivity.mActivity.getSystemService(
                    PythonActivity.NOTIFICATION_SERVICE)
        nm.notify(0, noti.build())

# UNTESTED !!!
# From http://stackoverflow.com/questions/12202983/\
# working-with-mountain-lions-notification-center-using-pyobjc

class NotificationOsx(NotificationBase):

    def notify(self):
        NSUserNotification = objc.lookUpClass('NSUserNotification')
        NSUserNotificationCenter = objc.lookUpClass('NSUserNotificationCenter')
        notification = NSUserNotification.alloc().init()
        notification.setTitle_(str(self.title))
        # notification.setSubtitle_(str(subtitle))
        notification.setInformativeText_(self.message)
        notification.setSoundName_("NSUserNotificationDefaultSoundName")
        # notification.setHasActionButton_(False)
        # notification.setOtherButtonTitle_("View")
        # notification.setUserInfo_({"action":"open_url", "value":url})
        NSUserNotificationCenter.defaultUserNotificationCenter().setDelegate_(self)
        NSUserNotificationCenter.defaultUserNotificationCenter().scheduleNotification_(notification)


class NotificationLinux(NotificationBase):

    def notify(self):
        SendNotify(self.title, self.message)


class NotificationWindows(NotificationBase):

    def notify(self):
        ''' Displays a notification using the win32 API '''
        balloon_tip = WindowsBalloonTip(self.title, self.message)



# Default to console
Notification = NotificationBase

# Platform-specific searches
if platform == "android":
    Notification = NotificationAndroid

if platform == "macosx":
    Notification = NotificationOsx

elif platform == "linux":
    Notification = NotificationLinux

elif platform == "win32":
    Notification = NotificationWindows
