## Needs signal-cli (https://github.com/AsamK/signal-cli)

# signal-qlbot
* Get info about a quake live server (player names, map etc.) from your Signal group

# Modifications required

* In **docker-image/qlbot.conf** change <phone-number> to the number that you have registered using signal-cli (Check AsamK's documention on how to register)

* In docker-compose.yaml, specify the API URL that you'd like to invoke for server information

# Usage

* In a Signal group, type **.ql** and the bot running on your server will reply with the relevant server information
