import sys
import gi

gi.require_version("Notify", "0.7")

from gi.repository import Notify


def Notification(message, title="", app_name=None):
    """ Displays a notification using the Gtk API """
    app_name = app_name or sys.argv[0]
    Notify.init(app_name)
    n = Notify.Notification.new(title, message)
    n.show()
