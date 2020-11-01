from setuptools import setup
from setuptools import find_packages
from setuptools.command.develop import develop


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="notify-send",
    version="0.0.15",
    description="notify-send notify.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="alert inform informer notify notify-send",
    platforms=["Linux", "Windows"],
    author="Andre P. Santos",
    author_email="andreztz@gmail.com",
    url="https://github.com/andreztz/notify-send",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "pypiwin32==223; sys_platform == 'win32'",
        "pywin32==228; sys_platform == 'win32'",
        "pycairo>=1.18.1; sys_platform == 'linux'",
        "PyGObject>=3.34.0; sys_platform == 'linux'",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
    ],
)
