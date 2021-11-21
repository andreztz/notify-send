from notify import Notification
from notify import notification


def test_if_notification_is_callable():
    assert callable(notification)


def test_notification_function():
    status = notification("hello world", message="optinal")
    assert status is True


def test_notification_class():
    status = Notification("Hello World", message="optional")()
    assert status is True
