from setuptools import setup
from setuptools import find_packages


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="notify-send",
    version="0.0.19",
    description="notify-send notify.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="alert inform informer notify notify-send",
    platforms=["Linux", "Windows"],
    author="Andre P. Santos",
    author_email="andreztz@gmail.com",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "pypiwin32==223; sys_platform == 'win32'",
        "pywin32==302; sys_platform == 'win32'",
        "pycairo>=1.18.1; sys_platform == 'linux'",
        "PyGObject>=3.34.0; sys_platform == 'linux'",
    ],
    extras_require={
        "dev": [
            "pytest",
        ],
        "build": [
            "build",
            "twine"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
    ],
    project_urls={
        "Source": "https://github.com/andreztz/notify-send/",
        "Documentation": "https://andreztz.github.io/notify-send/",
    },
)
