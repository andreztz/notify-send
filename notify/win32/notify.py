"""
This module contains the code for the notification using the Win32 api.

From https://gist.github.com/BoppreH/4000505
http://timgolden.me.uk/pywin32-docs/win32gui__Shell_NotifyIcon_meth.html
http://timgolden.me.uk/pywin32-docs/PyNOTIFYICONDATA.html
"""
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
from win32gui import (
    NIF_ICON,
    NIF_MESSAGE,
    NIF_TIP,
    NIF_INFO,
    NIM_MODIFY,
    NIM_ADD,
    NIM_DELETE,
)

import win32con
import sys
import os


class Win32Notification:
    """Displays a notification using Win32 API.

    Paramters:

        summary (str): Summary text.
        message (str): The message body (optional).
        timeout (int): Timeout for ballon tooltip in milliseconds (optional).
        app_name (str): Caller app name. Defaults to 'notify-send'.
        tip (str): Tooltip text (optional)
        **kwargs: Aditional arguments (optional)
    """

    def __init__(self):
        self.message_map = {win32con.WM_DESTROY: self.OnDestroy}

    def __call__(self, summary, message="", timeout=2000, **kwargs):
        tip = kwargs.get("tip", "Balloon tooltip")

        # Register the Window class.
        wc = WNDCLASS()
        hinst = wc.hInstance = GetModuleHandle(None)
        wc.lpszClassName = "PythonTaskbar"
        wc.lpfnWndProc = self.message_map  # could also specify a wndproc.
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

        # Icons managment
        iconPathName = os.path.abspath(
            os.path.join(sys.path[0], "balloontip.ico")
        )
        icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE

        try:
            hicon = LoadImage(
                hinst, iconPathName, win32con.IMAGE_ICON, 0, 0, icon_flags
            )
        except Exception:
            hicon = LoadIcon(0, win32con.IDI_APPLICATION)

        flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
        nid = (self.hwnd, 0, flags, win32con.WM_USER + 20, hicon, "tooltip")

        # Notify
        Shell_NotifyIcon(NIM_ADD, nid)
        Shell_NotifyIcon(
            NIM_MODIFY,
            (
                self.hwnd,
                0,
                NIF_INFO,
                win32con.WM_USER + 20,
                hicon,
                tip,
                message,
                timeout,
                summary,
            ),
        )
        # Destroy
        DestroyWindow(self.hwnd)
        classAtom = UnregisterClass(classAtom, hinst)
        return True

    def OnDestroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, nid)
        PostQuitMessage(0)  # Terminate the app.
