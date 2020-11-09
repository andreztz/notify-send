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
    mod = import_module("." + platform, __package__)
except:
    raise RuntimeError("Unsupported operating system: {}".format(sys.platform))
else:
    send = getattr(mod, "{}Notification".format(platform.title()))()


class Notification:
    """
    Displays a notification.

    Args:
        message: The message body.
        title: The summary text (optional).
        timeout: notification length in milliseconds (optional).
        **kwargs: Additional arguments (optional).
    """

    def __init__(self, message, title="", timeout=None, **kwargs):
        self.message = message
        self.title = title
        self.timeout = timeout
        self.kwargs = kwargs

    def __call__(self):
        send(self.message, self.title, self.timeout, **self.kwargs)


def notification(message, title="", timeout=None, **kwargs):
    n = Notification(message, title, timeout, **kwargs)
    n()
