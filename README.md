
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
sudo apt update
sudo apt upgrade

sudo apt install libffi-dev
sudo apt install python3-cffi
sudo apt install python3-pip

sudo pip3 install -U setuptools
sudo pip3 install discord.py
```

## Run Bot

```
python3 wheebo.py
```