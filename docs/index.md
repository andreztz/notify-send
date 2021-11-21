# Overview

Displays a notification suitable for the platform being run on.

## Example

```python
from notify import notification
notification('summary text', message='message body', app_name='myapp')
```

## Installation

```bash
$ pip install notify-send
```

### Prerequisites

#### Ubunut

```
$ sudo apt install libcairo2-dev libgirepository1.0-dev
```

#### Arch Linux

```
$ sudo pacman -S gobject-introspection
```


* [Notification](api.md#notification)
* [Notification Linux](api.md#linux)
* [Notification Windows](api.md#windows)


## License

MIT, see LICENSE for more details.
