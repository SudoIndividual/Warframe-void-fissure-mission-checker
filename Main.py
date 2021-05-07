import requests
import json.tool
import time

#api used https://docs.warframestat.us/#tag/Worldstate/paths/~1{platform}~1events/get and https://www.callmebot.com/

mission = []
relic = []

platform = input("Input what platform are you on? (Selection: PC,PS4,XBOX or switch) : ")

if platform.lower() == "xbox":
    platform = "xb1"
elif platform.lower() == "pc":
    platform = "pc"
elif platform.lower() == "ps4":
    platform = "ps4"
elif platform.lower() == "switch":
    platform = "swi"

selection = input("Input what mission you want to get notified on? (Selection: normal,railjack or both) : ")

if selection.lower() == "normal":
    selection2 = input("Input what type of mission you want to get notified on?\n Selection:\nCapture\nExterminate\nHijack\nMobile Defense(MD)\nRescue\nSabotage (Assault, Deception, Hive, Orokin, Reactor, Sealab)\nSpy\nDefection\nDisruption\nDefense\nExcavation\nInterception\nSurvival\ninput: ")
    selection = "normal"
    split_input = selection2.split(",")
    for every_mission in split_input:
        every_mission_remove_whitespace = every_mission.replace(" ", "")
        mission.append(every_mission_remove_whitespace.lower())
    print("\n")
elif selection.lower() == "railjack":
    selection2 = selection2 = input("What mission?(Skirmish or valotile)")
    split_input = selection2.split(",")
    for every_mission in split_input:
        every_mission_remove_whitespace = every_mission.replace(" ", "")
        mission.append(every_mission_remove_whitespace.lower())


selection3 = input("What relic do you want?\n\nAxi\nMeso\nLith\ninput: ")
split_input2 = selection3.split(",")
for every_relic in split_input2:
    every_relic_remove_whitespace = every_relic.replace(" ", "")
    every_relic_capitalize = every_relic_remove_whitespace.capitalize()
    relic.append(every_relic_capitalize)

phone_number = input("what is your phone number? (input in universal format)")
api_key = input("input api key: ")

def send_message(message1,message2):
    requests.post("https://api.callmebot.com/whatsapp.php?phone=" + phone_number + "&text=" + message1 +"+"+ message2 + "&apikey=" + api_key)
while True:
    try:
        response = requests.get("https://api.warframestat.us/" + platform + "/fissures")
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    except:
        print("please input only seleted options in the bracket")
    
    data = json.loads(response.text)
    format_data = json.dumps(data,indent=2)
    split_data = format_data.split("{")
    def checkNormalFissureMission():
        for every_data in split_data:
            if '"isStorm": false' in every_data:
                print("Normal fissure mission:")
                print(every_data)
            else:
                pass
    def checkRailjackFissureMission():
        for every_data in split_data:
            if '"isStorm": true' in every_data:
                print("Railjack fissure mission:")
                print(every_data)
            else:
                pass
    def both():
        checkNormalFissureMission()
        checkRailjackFissureMission()
    if selection == "normal":
        for missions in mission:
                if "survival" in missions:
                    for every_data in split_data:
                        if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Survival"+'"' in every_data:
                            for relics in relic:
                                if '"' + "tier" + '"' + ":"+' "' + relics + '"' in every_data:
                                    send_message("Survival", relics)
                                    print("message send")
                elif "capture" in missions:
                    for every_data in split_data:
                        if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Capture"+'"' in every_data:
                                for relics in relic:
                                    if '"' + "tier" + '"' + ":"+' "' +relics + '"' in every_data:
                                        send_message("Capture", relics)
                                        print("message send")
                elif "exterminate" in missions:
                    for every_data in split_data:
                        if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Extermination"+'"' in every_data:
                                for relics in relic:
                                    if '"' + "tier" + '"' + ":"+' "' +relics + '"' in every_data:
                                        send_message("Exterminate", relics)
                                        print("message send")
                elif "hijack" in missions:
                    for every_data in split_data:
                        if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Hijack"+'"' in every_data:
                                for relics in relic:
                                    if '"' + "tier" + '"' + ":"+' "' +relics + '"' in every_data:
                                        send_message("Hijack", relics)
                                        print("message send")
                elif "md" in missions:
                    for every_data in split_data:
                        if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Mobile Defense"+'"' in every_data:
                                for relics in relic:
                                    if '"' + "tier" + '"' + ":"+' "' +relics + '"' in every_data:
                                        send_message("Mobile Defense", relics)
                                        print("message send")
                elif "rescue" in missions:
                    for every_data in split_data:
                        if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Rescue"+'"' in every_data:
                                for relics in relic:
                                    if '"' + "tier" + '"' + ":"+' "' +relics + '"' in every_data:
                                        send_message("Rescue", relics)
                                        print("message send")
                elif "sabotage" in missions:
                    for every_data in split_data:
                        if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Sabotage"+'"' in every_data:
                                for relics in relic:
                                    if '"' + "tier" + '"' + ":"+' "' +relics + '"' in every_data:
                                        send_message("Sabotage", relics)
                                        print("message send")
                elif "spy" in missions:
                    for every_data in split_data:
                        if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Spy"+'"' in every_data:
                                for relics in relic:
                                    if '"' + "tier" + '"' + ":"+' "' +relics + '"' in every_data:
                                        send_message("Spy", relics)
                                        print("message send")
                elif "defection" in missions:
                    for every_data in split_data:
                        if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Defection"+'"' in every_data:
                                for relics in relic:
                                    if '"' + "tier" + '"' + ":"+' "' +relics + '"' in every_data:
                                        send_message("Defection", relics)
                                        print("message send")
                elif "disruption" in missions:
                    for every_data in split_data:
                        if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Disruption"+'"' in every_data:
                                for relics in relic:
                                    if '"' + "tier" + '"' + ":"+' "' +relics + '"' in every_data:
                                        send_message("Disruption", relics)
                                        print("message send")
                elif "defense" in missions:
                    for every_data in split_data:
                        if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Defense"+'"' in every_data:
                                for relics in relic:
                                    if '"' + "tier" + '"' + ":"+' "' +relics + '"' in every_data:
                                        send_message("Defense", relics)
                                        print("message send")
                elif "excavation" in missions:
                    for every_data in split_data:
                        if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Excavation"+'"' in every_data:
                                for relics in relic:
                                    if '"' + "tier" + '"' + ":"+' "' +relics + '"' in every_data:
                                        send_message("Excavation", relics)
                                        print("message send")
                elif "interception" in missions:
                    for every_data in split_data:
                        if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Interception"+'"' in every_data:
                                for relics in relic:
                                    if '"' + "tier" + '"' + ":"+' "' +relics + '"' in every_data:
                                        send_message("Interception", relics)
                                        print("message send")
    elif selection == "railjack":
        for missions in mission:
            if "skirmish" in missions:
                for every_data in split_data:
                    if '"isStorm": True' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Skirmish"+'"' in every_data:
                            for relics in relic:
                                if '"' + "tier" + '"' + ":"+' "' +relics + '"' in every_data:
                                    send_message("Skirmish", relics)
                                    print("message send")
            elif "volatile" in missions:
                for every_data in split_data:
                    if '"isStorm": True' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Volatile"+'"' in every_data:
                            for relics in relic:
                                if '"' + "tier" + '"' + ":"+' "' +relics + '"' in every_data:
                                    send_message("Volatile", relics)
                                    print("message send")
    time.sleep(1800)




