# notify-send

![](header.png)

[![Upload Python Package](https://github.com/andreztz/notify-send/actions/workflows/python-publish.yml/badge.svg)](https://github.com/andreztz/notify-send/actions/workflows/python-publish.yml)

## Usage example


```python
    from notify import notification
    notification('summary text', message='message body', app_name='myapp')
```


## Installation

```sh
    pip install notify-send
```

### Prerequisites

#### Ubuntu

```sh
sudo apt install libcairo2-dev libgirepository1.0-dev
```
#### Arch Linux

```sh
sudo pacman -S gobject-introspection

```


## Development setup

```sh
    git clone https://github.com/andreztz/notify-send.git
    cd notify-send
    python -m venv venv
    source venv/bin/activate
    pip install -e .[dev]
```


## Meta

André P. Santos – [@ztzandre](https://twitter.com/ztzandre) – andreztz@gmail.com

Distributed under the MIT license. See `LICENSE` for more information.

[https://github.com/andreztz/notify-send](https://github.com/andreztz/)

## Contributing

1. Fork it (<https://github.com/andreztz/notify-send/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
