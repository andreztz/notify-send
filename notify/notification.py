"""
Displays a notification suitable for the platform being run on.


Examples:
    ```
    from notify import notification
    notification('what you want said', title=':)')
    ```

License:

    `MIT, see LICENSE for more details.`
"""
import sys
from importlib import import_module

platform = sys.platform


try:
    modulo = import_module("." + platform, __package__)
except:
    raise RuntimeError("Unsupported operating system: {}".format(sys.platform))
else:
    send = getattr(modulo, "{}Notification".format(platform.title()))()


class Notification:
    """
    Displays a notification.

    Args:
        message: The text message body.
        app_name: Caller app name. Defaults to 'notify-send'
        title: Summary text (optional).
        timeout: Notification length in milliseconds (optional).
        **kwargs: Additional arguments (optional).
    """

    def __init__(self, message, title="", timeout=2000, **kwargs):
        self.message = message
        self.title = title
        self.timeout = timeout
        self.kwargs = kwargs

    def __call__(self):
        send(self.message, self.title, self.timeout, **self.kwargs)


def notification(message, title="", timeout=2000, **kwargs):
    Notification(message, title, timeout, **kwargs)()
