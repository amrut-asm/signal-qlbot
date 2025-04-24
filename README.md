## Needs signal-cli (https://github.com/AsamK/signal-cli)

# signal-qlbot
* Get info about a quake live server (player names, map etc.) from your Signal group

# Modifications required

## Folder: docker-image
1. In **docker-image/qlbot.conf** change \<phone-number\> to the number that you have registered using signal-cli (Check AsamK's documention on how to register)
2. Build docker image using `docker build -t signal-bot:latest .`

# General
* In docker-compose.yaml, specify the API URL that you'd like to invoke for server information
* Ensure folder `signal-cli` exists with data created after registration using signal-cli (Once you register your phone number with Signal using signal-cli, a folder at `$HOME/.local/share/signal-cli` will be generated. You must copy that directory into the directory containing docker-compose.yaml)

# Usage

* In a Signal group, type **.ql** and the bot running on your server will reply with the relevant server information
