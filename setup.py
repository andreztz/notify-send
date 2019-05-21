import subprocess

from setuptools import setup
from setuptools import find_packages
from setuptools.command.develop import develop


class PostDevelopCommand(develop):
    def run(self):
        """
        Note: this class solves the installation problem
        of pycairo and pygobject in development mode.
        ModuleNotFoundError: No module named 'cairo'
        """
        print("*" * 80)
        subprocess.call("pip install -r requirements.txt".split(" "))
        print("*" * 80)
        develop.run(self)


def readme():
    with open("README.md") as f:
        return f.read()


def required():
    with open("requirements.txt") as f:
        return f.read().splitlines()


setup(
    name="notify-send",
    version="0.0.8",
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
    install_requires=required(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
    ],
    cmdclass={"develop": PostDevelopCommand},
)
