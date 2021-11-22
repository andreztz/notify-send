"""
Displays a notification suitable for the platform being run on.


Examples:
    ```
    from notify import notification
    notification('summary text', message='message body', app_name='myapp')
    ```

License:

    `MIT, see LICENSE for more details.`
"""
import sys
from importlib import import_module

platform = sys.platform


try:
    modulo = import_module("." + platform, __package__)
except Exception:
    raise RuntimeError("Unsupported operating system: {}".format(platform))
else:
    caller = getattr(modulo, "{}Notification".format(platform.title()))()


class Notification:
    """
    Displays a notification.

    Args:
        summary (str): Summary text.
        message (str): The message body (optional).
        timeout (int): Notification length in milliseconds (optional).
        app_name (str): Caller app name. Defaults to 'notify-send'.
        **kwargs: Additional arguments (optional).
    """

    def __init__(self, summary, message="", timeout=2000, **kwargs):
        self.summary = summary
        self.message = message
        self.timeout = timeout
        self.kwargs = kwargs

    def __call__(self):
        status = caller(
            self.message, self.summary, self.timeout, **self.kwargs
        )
        return status


def notification(summary, message="", timeout=2000, **kwargs):
    status = Notification(summary, message, timeout, **kwargs)()
    return status
