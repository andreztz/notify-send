# -- coding: utf-8 --
# From https://gist.github.com/BoppreH/4000505

from win32api import GetModuleHandle
from win32gui import WNDCLASS
from win32gui import Shell_NotifyIcon
from win32gui import RegisterClass
from win32gui import CreateWindow
from win32gui import UpdateWindow
from win32gui import PostQuitMessage
from win32gui import UnregisterClass
from win32gui import DestroyWindow
from win32gui import LoadIcon
from win32gui import LoadImage
from win32gui import NIF_ICON, NIF_MESSAGE, NIF_TIP, NIF_INFO, NIM_MODIFY, NIM_ADD, NIM_DELETE

import win32con
import sys, os
import struct
import time


class NotificationWindows:
    def __init__(self, message, title):

        message_map = {win32con.WM_DESTROY: self.OnDestroy}
        # Register the Window class.
        wc = WNDCLASS()
        hinst = wc.hInstance = GetModuleHandle(None)
        wc.lpszClassName = "PythonTaskbar"
        wc.lpfnWndProc = message_map  # could also specify a wndproc.
        classAtom = RegisterClass(wc)
        # Create the Window.
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = CreateWindow(
            classAtom,
            "Taskbar",
            style,
            0,
            0,
            win32con.CW_USEDEFAULT,
            win32con.CW_USEDEFAULT,
            0,
            0,
            hinst,
            None,
        )
        UpdateWindow(self.hwnd)
        iconPathName = os.path.abspath(os.path.join(sys.path[0], "balloontip.ico"))
        icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
        try:
            hicon = LoadImage(hinst, iconPathName, win32con.IMAGE_ICON, 0, 0, icon_flags)
        except:
            hicon = LoadIcon(0, win32con.IDI_APPLICATION)
        flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
        nid = (self.hwnd, 0, flags, win32con.WM_USER + 20, hicon, "tooltip")
        Shell_NotifyIcon(NIM_ADD, nid)
        Shell_NotifyIcon(
            NIM_MODIFY,
            (
                self.hwnd,
                0,
                NIF_INFO,
                win32con.WM_USER + 20,
                hicon,
                "Balloon  tooltip",
                message,
                200,
                title,
            ),
        )
        time.sleep(10)
        DestroyWindow(self.hwnd)
        UnregisterClass(classAtom, hinst)

    def OnDestroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, nid)
        PostQuitMessage(0)  # Terminate the app.


def run_balloon_tip(message, **kwargs):
    w = NotificationWindows(message, **kwargs)


if __name__ == "__main__":
    run_balloon_tip(message="Here is a balloon tip", title="Demonstration")
