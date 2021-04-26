## Needs signal-cli (https://github.com/AsamK/signal-cli)

# signal-qlbot
* Get info about a quake live server (player names, map etc.) from your Signal group

# Modifications required

* Make sure you put in your signal bot's phone number in the script. Also, be sure to change the group name to your Signal group.

* Change the country code from 'IN' (India) to something else but make sure that country doesn't have a large number of servers. 

* For example, the US has a large number of servers and because of this the script will spam your Signal group with info about a dozen servers.

* Instead, you could just modify the request made to the Syncore API so that it returns info about only one server (or a few).

# Usage

* In a Signal group, type **.ql** and the bot running on your server will reply with the relevant server information
