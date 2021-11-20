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
        app_name: Caller app name.
        title: The summary text.
        timeout: Timeout for notification in milliseconds (optional)
        message: The text message body.
        image: The icon filename or icon theme-compliant name
    """

    def __call__(
        self,
        message,
        title="",
        timeout=2000,
        **kwargs
    ):
        app_name = kwargs.get('app_name', 'notify-send')
        image = kwargs.get('image', 'dialog-information')

        Notify.init(app_name)
        n = Notify.Notification.new(title, message, image)
        n.set_timeout(timeout)
        n.show()
