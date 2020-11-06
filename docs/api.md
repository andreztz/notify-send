
## `Notification`

Displays a notification.


**Paramters:**

| Name     | type | description                                                  |
| ---------|------|--------------------------------------------------------------|
| title    | str  | The summary text (optional).                                 |
| message  | str  | The message body                                             |
|\*\*kwargs|      | Additional arguments (optional)                              |

## Linux

This module contains the code for the notification using the Gtk api.

### `LinuxNotification`

Displays a notification using the Gtk API.

**Paramters:**

| Name     |  Type     | Description                                           |
| ---------|-----------|------------------------                               |
| app_name | str       | The application name to use for this notification.    |
| title    | str       | The summary text                                      |
| message  | str       | The message body text                                 |
| image    | str       | The icon filename or icon theme-compliant name        |


## Windows

This module contains the code for the notification using the Win32 api.


### `Win32Notification`


Displays a notification using the Win32 API.

**Paramters:** 

| Name     |  Type     | Description                                           |
| ---------|-----------|-------------------------------------------------------|
| tip      | str       | Tooltip text (optional)                               |
| timeout  | int       | Timeout for ballon tooltip in milliseconds (optional) |
| title    | str       | Title for ballon tooltip (optional)                   |
| message  | str       | Balloon tooltip text (optional)                       |



