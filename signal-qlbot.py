from pydbus import SessionBus
from gi.repository import GLib
import requests
import json
import time
import re


def msgRcv(timestamp, source, groupID, message, attachments):
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
        ap_list = []
        for sv_index in range(0, json_data["serverCount"]):
            payload_list = []
            final_string = ''
            ap_list.append("Server {0}".format(sv_index+1))
            ap_list.append("**********************************")
            ap_list.append(" ")
            # Print server name
            payload_list.append("Server Name")
            payload_list.append("-----")
            pattern = r'\^[1-7]'
            sv_mod_name = re.sub(
                pattern, '', json_data["servers"][sv_index]["info"]["serverName"])
            payload_list.append(sv_mod_name)
            payload_list.append(" ")

            # Player count
            count = int(json_data["servers"][sv_index]["info"]["players"])

            # Don't print details if players online are 0
            if (count == 0):
                payload_list.append("Server is empty!")
                payload_list.append(" ")
                final_string = "\n".join(payload_list)
                #signal.sendGroupMessage(final_string, [], groupID)
                ap_list.append(final_string)
                continue

            # Print map name
            payload_list.append(
                "Map   :   " + (json_data["servers"][sv_index]["info"]["map"]).title())
            payload_list.append(" ")

            # Print game type
            payload_list.append(
                "Type  :   " + (json_data["servers"][sv_index]["info"]["game"]))
            payload_list.append(" ")

            # Print score
            payload_list.append("Score :   " + (json_data["servers"][sv_index]["rules"]["g_redScore"]) + ":" + (
                json_data["servers"][sv_index]["rules"]["g_blueScore"]))
            payload_list.append(" ")

            # Print number of players online
            payload_list.append("Players Online")
            payload_list.append("-----")
            payload_list.append(
                str(json_data["servers"][sv_index]["info"]["players"]))
            payload_list.append(" ")

            # Print names of players online
            payload_list.append("Players List")
            payload_list.append("-----")
            for player_index in json_data["servers"][sv_index]["players"]:
                pattern = r'\^[1-7]'
                re_patched_name = re.sub(pattern, '', player_index["name"])
                if not re_patched_name:
                    re_patched_name = "UnnamedPlayer"
                payload_list.append(re_patched_name)
            payload_list.append(" ")

            final_string = "\n".join(payload_list)
            ap_list.append(final_string)

    fstring = "\n".join(ap_list)
    try:
        signal.sendGroupMessage(fstring, [], groupID)
    except:
        print("Exception while sending message to group...")
    return


bus = SessionBus()
loop = GLib.MainLoop()

flag = 0
while(flag == 0):
    try:
        signal = bus.get('org.asamk.Signal')
        signal.onMessageReceived = msgRcv
        flag = 1
    except:
        print("D-Bus session bus is not up yet... sleeping")
        time.sleep(5)
        flag = 0

print("D-Bus session bus is up... entering event loop")
loop.run()
