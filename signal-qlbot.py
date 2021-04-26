import requests
import json

def msgRcv (timestamp, source, groupID, message, attachments):
   if (groupID == []):
      return

   if (message != ".ql"):
      return

   if (signal.getGroupName(groupID) == "<insert group name here>"):
      URL = "https://ql.syncore.org/api/servers"
      payload = {'countries' : 'IN'}
      response = requests.get(url=URL, params=payload)
      json_data = json.loads(response.text)
      for sv_index in range(0,json_data["serverCount"]):
      	payload_list = []
	final_string = ''
      	payload_list.append("Server Name")
      	payload_list.append("-----------")
      	payload_list.append(json_data["servers"][sv_index]["info"]["serverName"])
      	payload_list.append(" ")
	payload_list.append("Map   :   " + (json_data["servers"][sv_index]["info"]["map"]).title())
	payload_list.append(" ")
	payload_list.append("Type  :   " + (json_data["servers"][sv_index]["info"]["game"]))
	payload_list.append(" ")
	payload_list.append("Score :   " + (json_data["servers"][sv_index]["rules"]["g_redScore"]) + ":" + (json_data["servers"][sv_index]["rules"]["g_blueScore"]))
	payload_list.append(" ")
      	payload_list.append("Players online")
      	payload_list.append("--------------")
      	payload_list.append(str(json_data["servers"][sv_index]["info"]["players"]))
      	payload_list.append(" ")
      	payload_list.append("Players List")
      	payload_list.append("------------")
      	for player_index in json_data["servers"][sv_index]["players"]:
        	payload_list.append(player_index["name"])
      	final_string = "\n".join(payload_list)
      	signal.sendGroupMessage(final_string, [], groupID)

   return

from pydbus import SystemBus
from gi.repository import GLib

bus = SystemBus()
loop = GLib.MainLoop()

signal = bus.get('org.asamk.Signal', '/org/asamk/Signal/_<insert phone number here>')

signal.onMessageReceived = msgRcv
loop.run()
