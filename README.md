
# WheeBo Discord Bot

## Configure App

* create app on the the [Discord Developer Console](https://discord.com/developers/applications)
* add bot to the app
* add bot to the server

```
https://discord.com/api/oauth2/authorize?client_id=${CLIENT_ID}&scope=bot&permissions=1
```
> replace the CLIENT_ID variable with the app specific client id

## Bot Dependencies

```
# system update
sudo apt update

# system upgrade
sudo apt upgrade

# https://github.com/pypa/pip
sudo apt install python3-pip

# https://github.com/python-cffi
sudo apt install python3-cffi

# https://github.com/pypa/setuptools
sudo pip3 install -U setuptools

# https://github.com/Rapptz/discord.py
sudo pip3 install discord.py
```

## Run Bot

```
python3 wheebo.py
```