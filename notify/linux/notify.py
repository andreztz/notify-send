import os
import gi

gi.require_version('Notify', '0.7')
from gi.repository import Notify


class SendNotify:

    def __init__(self, msg, body):

        Notify.init('Tradutor')
        notification = Notify.Notification.new(msg, body)
        notification.show()
