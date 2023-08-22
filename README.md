# Getting Started

### Install or update python
- if you don't have python installed, follow this [link](https://wiki.python.org/moin/BeginnersGuide/Download)
- if you do have python installed, check your python version
  - open your terminal and run `python3 --version`
  - update python if the version is < 3.9, [update link](https://programiz.pro/resources/update-python/)

### (optional but recommended) 
- create virtual environment. [what is a virtual environment?](https://docs.python.org/3/library/venv.html)
- run this command `python3 -m venv /path/to/new/virtual/environment` 
- activate your venv
  - Mac/Linux: `source path/to/your/venv/bin/activate`
  - Windows: `<environment-name>\Scripts\activate`, [troubleshooting](https://linuxhint.com/activate-virtualenv-windows/)

### Installation
- clone this repository
- if you have created venv, activate it now
- open your terminal and run `pip install -r requirements.txt`
- after the installation run `pip freeze`, output should look something like this:
```
contourpy==1.1.0
cycler==0.11.0
fonttools==4.42.0
imageio==2.31.1
kiwisolver==1.4.4
matplotlib==3.7.2
numpy==1.25.2
packaging==23.1
Pillow==10.0.0
pyparsing==3.0.9
PyQt5==5.15.9
PyQt5-Qt5==5.15.2
PyQt5-sip==12.12.2
python-dateutil==2.8.2
scipy==1.11.1
six==1.16.0
```