import sys
import gi

gi.require_version("Notify", "0.7")
from gi.repository import Notify


class NotificationLinux:
    """ Displays a notification using the Gtk API """

    def __init__(self, message, **kwargs):
        app_name = kwargs.get("appname", sys.argv[0])
        title = kwargs.get("title", "")
        Notify.init(app_name)
        notification = Notify.Notification.new(title, message)
        notification.show()
