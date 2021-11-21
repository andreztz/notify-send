## `Notification`


Displays a notification.

**Paramters:**

| Name     | Type | Description                                                  |
| ---------|------|--------------------------------------------------------------|
| summary  | str  | The summary text                                             |
| message  | str  | The message body (optional)                                  |
| timeout  | int  | Notification length in milliseconds (optional)               |
| app_name | str  | Caller app name                                              |
|\*\*kwargs|      | Additional arguments (optional)                              |


## Linux

This module contains the code for the notification using Gtk api.


### `LinuxNotification`


Displays a notification using the Gtk API.

**Paramters:**

| Name     |  Type     | Description                                    |
| ---------|-----------|------------------------------------------------|
| summary  | str       | The summary text                               |
| message  | str       | The message body (optional)                    |
| timeout  | int       | The timeout in milliseconds (optional)         |
| app_name | str       | Caller app name                                |
| image    | str       | The icon filename or icon theme-compliant name |


## Windows


This module contains the code for the notification using Win32 api.


### `Win32Notification`


Displays a notification using the Win32 API.

**Paramters:** 

| Name     |  Type     | Description                                           |
| ---------|-----------|-------------------------------------------------------|
| summary  | str       | The summary text                                      |
| message  | str       | The message body (optional)                           |
| timeout  | int       | Timeout in milliseconds (optional)                    |
| tip      | str       | Tooltip text (optional)                               |
