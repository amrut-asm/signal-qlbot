from pydbus import SessionBus
from gi.repository import GLib
import requests
import json
import time
import re

def construct_signal_string(servers):
    r_list = []
    for index, record in enumerate(servers, start=1):
        r_list.append(f"Server {index}")
        r_list.append("****************")
        r_list.append(record["sv_name"])
        r_list.append(" ")
        r_list.append(f'Map    :    {record["map"]}')
        r_list.append(" ")
        r_list.append(f'Type   :    {record["type"]}')
        r_list.append(" ")
        if(not record["players"]):
          r_list.append("Server is empty!")
          r_list.append(" ")
          continue 
        r_list.append(f'Score  :    {record["score"]}')
        r_list.append(" ")
        r_list.append(f'Players ({record["player_count"]})')
        r_list.append("---")
        r_list.append("\n".join(record["players"]))
        r_list.append(" ")
 
    return "\n".join(r_list)

def message_handler(timestamp, source, groupID, message, attachments):
    if (groupID == []):
        return

    if (message != ".ql"):
        return

    if ((signal.getGroupName(groupID) == "test") or (signal.getGroupName(groupID) == "quake 2.0")):
        URL = "https://ql.syncore.org/api/servers"
        payload = {'countries': 'IN'}
        try:
            response = requests.get(url=URL, params=payload)
        except:
            print("Failed to make request to a2sapi")
            return

        try:
            json_data = json.loads(response.text)
        except:
            return
    
        pattern = r'\^[1-7]'
        keys = ["sv_name", "player_count", "map", "type", "score", "players"]
        servers = []

        for sv_index in range(json_data["serverCount"]):
            sv_dict = {key: None for key in keys}
            players_list = [] 
            sv_info = json_data["servers"][sv_index]["info"]
            sv_players = json_data["servers"][sv_index]["players"]
            sv_rules = json_data["servers"][sv_index]["rules"]

            # Get server name
            r_sv_name = str(re.sub(pattern, '', sv_info["serverName"]))

            # Get player count
            r_player_count = int(sv_info["players"])

            # Get map name
            r_map = str(sv_info["map"])

            # Get game type
            r_type = str(sv_info["game"])

            # Get score
            r_score = str(sv_rules["g_redScore"]+":"+sv_rules["g_blueScore"])

            # Get names of players online
            # Sanitize names
            for player_index in sv_players:
                patched_name = re.sub(pattern, '', player_index["name"])
                if not patched_name:
                    patched_name = "UnnamedPlayer"
                players_list.append(str(patched_name))
            r_players = players_list

            sv_dict["sv_name"] = r_sv_name
            sv_dict["player_count"] = r_player_count
            sv_dict["map"] = r_map
            sv_dict["type"] = r_type
            sv_dict["score"] = r_score
            sv_dict["players"] = r_players
            servers.append(sv_dict)

        sorted_servers = sorted(servers, key=lambda x: x["player_count"])
        signal_text = construct_signal_string(sorted_servers)

    try:
        signal.sendGroupMessage(signal_text, [], groupID)
    except:
        print("Exception while sending message to group...")
    return


bus = SessionBus()
loop = GLib.MainLoop()

flag = 0
while(flag == 0):
    try:
        signal = bus.get('org.asamk.Signal')
        signal.onMessageReceived = message_handler
        flag = 1
    except:
        # Assume D-Bus session is not up yet
        print("D-Bus session bus is not up yet... sleeping")
        time.sleep(5)
        flag = 0

print("D-Bus session bus is up... entering event loop")
loop.run()
