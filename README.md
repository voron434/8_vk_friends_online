# Watcher of Friends Online

This script could show you your friends online in vk.com

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

Then you must register your own app [here](https://vk.com/apps?act=manage), then press "edit" on your app and find there APP_ID on page Settings. Then you must add this APP_ID as an [environment variable](https://en.wikipedia.org/wiki/Environment_variable).   

How to do this on [Windows 10](https://superuser.com/questions/949560/how-do-i-set-system-environment-variables-in-windows-10) or [Ubuntu](https://help.ubuntu.com/community/EnvironmentVariables)

# Usage
  ```$ python3 vk_friends_online.py 
  Login: <your login>  
  Password (would be invisible): <your password>
  Your pc-online friends:
  Илья Осипов
  Your mobile-online friends:
  Влад Агафонов
  Инна Шарудина
  ```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
