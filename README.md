## Needs signal-cli (https://github.com/AsamK/signal-cli)

## Signal-cli needs to be started with the the dbus interface and in daemon mode!

# signal-qlbot
* Get info about a quake live server (player names, map etc.) from your Signal group

# Modifications required

* Change the country code from 'IN' (India) to something else but make sure that country doesn't have a large number of servers. 

* For example, the US has a large number of servers and because of this the script will spam your Signal group with info about a dozen servers.

* Instead, you could just modify the request made to the Syncore API so that it returns info about only one server (or a few).

# Usage

* In a Signal group, type **.ql** and the bot running on your server will reply with the relevant server information
