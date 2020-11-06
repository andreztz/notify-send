"""
This module contains the code for the notification using the Gtk api.

https://lazka.github.io/pgi-docs/#Notify-0.7/classes/Notification.html
https://lazka.github.io/pgi-docs/Notify-0.7/classes/Notification.html#Notify.Notification.set_app_name
"""
import sys
import gi

gi.require_version("Notify", "0.7")

from gi.repository import Notify
from gi.repository import GdkPixbuf


class LinuxNotification:
    """Displays a notification using the Gtk API.

    Args:
        app_name: The application name to use for this notification.
        title: The summary text.
        message: The message body text.
        image: The icon filename or icon theme-compliant name
    """

    def __call__(
        self,
        message,
        title="",
        image="dialog-information",
        app_name=None,
        **kwargs
    ):

        app_name = app_name or sys.argv[0]
        Notify.init(app_name)
        n = Notify.Notification.new(title, message, image)
        n.show()
