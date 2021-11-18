# notify-send

![](header.png)


## Prerequisites


### Ubuntu

```
$ sudo apt install libcairo2-dev libgirepository1.0-dev
```

## Archlinux


```
$ sudo pacman -S gobject-introspection
```



## Installation

```sh
    pip install notify-send
```

## Usage example

```python
    from notify import notification
    notification('body message', title='optinal')
```

## Development setup

```sh
    git clone https://github.com/andreztz/notify-send.git
    cd notify-send
    poetry install
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
