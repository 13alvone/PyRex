<p align="center">
  <img height="100" src="https://github.com/user0706/PyRex/blob/master/icons/windowIcon.png?raw=true">
</p>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![python-version](https://img.shields.io/badge/Python-3.6|3.7-<COLOR>.svg)](https://www.python.org/)  [![Qt](https://img.shields.io/badge/GUI%20by-Qt%20Designer-orange)](https://doc.qt.io/qt-5/qtdesigner-manual.html)  [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/) [![PyPI status](https://img.shields.io/pypi/status/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
## Description
PyRex is a tool for visual testing Python regular expression.
<br>Based on the re python package, combined with the Qt user interface, it allows a visual display of the results of a regular expression pattern.

:warning: **This is a beta version and probably contains some bugs. In that case, please [report the new issue](https://github.com/user0706/PyRex/issues).**

## Prerequisites
After opening the downloaded repository in cmd *(Windows)*/terminal *(Linux/MacOS)*, to install the necessary packages for PyRex operation, enter the following command:
```python
pip install -r requirements.txt --no-index --find-links file:///tmp/packages
```
## How to run PyRex?
Execute the following commands in cmd *(Windows)*/terminal *(Linux/MacOS)*:

- Download repository
```
git clone https://github.com/user0706/PyRex.git
```
- Entry into the download repository
```
cd PyRex
```
- Start the program
```
python main.py
(if not, try python3)
```

## What's new:
- Test_string highlighting features

## Screenshots
![](https://github.com/user0706/PyRex/blob/feature/test-string-highlighting/Example.png?raw=true)

## To-Do
- [ ] Fill groups in real-time in pattern areas
- [ ] Fill the matched groups in the test string area in real time
- [ ] Display match results in real time
- [ ] Code generator
