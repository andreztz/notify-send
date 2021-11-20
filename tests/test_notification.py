from notify import Notification
from notify import notification


def test_if_notification_is_callable():
    assert callable(notification)


def test_notification_function():
    notification("hello world", title="optinal")


def test_notification_class():
    Notification("Hello World", title="optional")()
    
