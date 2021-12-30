"""
This module contains the code for the notification using Gtk api.

https://lazka.github.io/pgi-docs/#Notify-0.7/classes/Notification.html
https://lazka.github.io/pgi-docs/Notify-0.7/classes/Notification.html#Notify.Notification.set_app_name
"""
import gi

gi.require_version("Notify", "0.7")

from gi.repository import Notify
from gi.repository import GdkPixbuf


class LinuxNotification:
    """Displays a notification using the Gtk API.

    Args:
        summary (str): The summary text.
        message (str): The message body.
        timeout (int): The timeout in milliseconds (optional)
        app_name (str): Caller app name.
        image (str): The icon filename or icon theme-compliant name
    """

    def __call__(self, summary, message="", timeout=2000, **kwargs):
        app_name = kwargs.get("app_name", "notify-send")
        image = kwargs.get("image", "dialog-information")
        Notify.init(app_name)
        n = Notify.Notification.new(message, summary, image)
        n.set_timeout(timeout)
        success = n.show()
        return success
