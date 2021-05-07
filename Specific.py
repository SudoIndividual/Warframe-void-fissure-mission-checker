import requests
import json.tool
import time


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

phone_number = input("what is your phone number? (input in universal format)")

if selection.lower() == "normal":
    selection2 = input("Input what type of mission you want to get notified on?\n Selection:\nCapture\nExterminate\nHijack\nMobile Defense\nRescue\nSabotage (Assault, Deception, Hive, Orokin, Reactor, Sealab)\nSpy\nDefection\nDisruption\nDefense\nExcavation\nInterception\nSurvival\ninput: ")
    selection = "normal"
    if selection2.lower() == "survival":
        selection2 = "survival"
    elif selection2.lower() == "capture":
        selection2 = "capture"
    elif selection2.lower() == "exterminate":
        selection2 = "exterminate"
    elif selection2.lower() == "hijack":
        selection2 = "hijack"
    elif selection2.lower() == "mobiledefense":
        selection2 = "mobiledefense"
    elif selection2.lower() == "rescue":
        selection2 = "rescue"
    elif selection2.lower() == "sabotage":
        selection2 = "sabotage"
    elif selection2.lower() == "spy":
        selection2 = "spy"
    elif selection2.lower() == "defection":
        selection2 = "defection"
    elif selection2.lower() == "disruption":
        selection2 = "disruption"
    elif selection2.lower() == "defense":
        selection2 = "defense"
    elif selection2.lower() == "excavation":
        selection2 = "excavation"
    elif selection2.lower() == "interception":
        selection2 = "interception"
    print("\n")
    selection3 = input("What relic do you want?\n\nAxi\nMeso\nLith\ninput: ")
    if selection3.lower() == "lith":
        selection3 = "Lith"
    elif selection3.lower() == "meso":
        selection3 = "Meso"
    elif selection3.lower() == "axi":
        selection3 = "Axi"
elif selection.lower() == "railjack":
    selection2 = selection2 = input("What mission?(Skirmish or valotile)")
    if selection2.lower() == "skirmish":
        selection2 = "Skirmish"
    elif selection2.lower() == "volatile":
        selection2 = "volatile"
api_key = input("input api key: ")

def send_message():
    requests.post("https://api.callmebot.com/whatsapp.php?phone=" + phone_number + "&text=" + selection3 +"+"+ selection2 + "&apikey=" + api_key)
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
        if selection2 == "survival":
            for every_data in split_data:
                if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Survival"+'"' in every_data:
                    if '"' + "tier" + '"' + ":"+' "' +selection3 + '"' in every_data:
                        send_message()
                        print("message send")
        elif selection2 == "capture":
            if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Capture"+'"' in every_data:
                    if '"' + "tier" + '"' + ":"+' "' +selection3 + '"' in every_data:
                        send_message()
                        print("message send")
        elif selection2 == "exterminate":
            if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Extermination"+'"' in every_data:
                    if '"' + "tier" + '"' + ":"+' "' +selection3 + '"' in every_data:
                        send_message()
                        print("message send")
        elif selection2 == "hijack":
            if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Hijack"+'"' in every_data:
                    if '"' + "tier" + '"' + ":"+' "' +selection3 + '"' in every_data:
                        send_message()
                        print("message send")
        elif selection2 == "mobiledefense":
            if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Mobile Defense"+'"' in every_data:
                    if '"' + "tier" + '"' + ":"+' "' +selection3 + '"' in every_data:
                        send_message()
                        print("message send")
        elif selection2 == "rescue":
            if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Rescue"+'"' in every_data:
                    if '"' + "tier" + '"' + ":"+' "' +selection3 + '"' in every_data:
                        send_message()
                        print("message send")
        elif selection2 == "sabotage":
            if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Sabotage"+'"' in every_data:
                    if '"' + "tier" + '"' + ":"+' "' +selection3 + '"' in every_data:
                        send_message()
                        print("message send")
        elif selection2 == "spy":
            if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Spy"+'"' in every_data:
                    if '"' + "tier" + '"' + ":"+' "' +selection3 + '"' in every_data:
                        send_message()
                        print("message send")
        elif selection2 == "defection":
            if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Defection"+'"' in every_data:
                    if '"' + "tier" + '"' + ":"+' "' +selection3 + '"' in every_data:
                        send_message()
                        print("message send")
        elif selection2 == "disruption":
            if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Disruption"+'"' in every_data:
                    if '"' + "tier" + '"' + ":"+' "' +selection3 + '"' in every_data:
                        send_message()
                        print("message send")
        elif selection2 == "defense":
            if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Defense"+'"' in every_data:
                    if '"' + "tier" + '"' + ":"+' "' +selection3 + '"' in every_data:
                        send_message()
                        print("message send")
        elif selection2 == "excavation":
            if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Excavation"+'"' in every_data:
                    if '"' + "tier" + '"' + ":"+' "' +selection3 + '"' in every_data:
                        send_message()
                        print("message send")
        elif selection2 == "interception":
            if '"isStorm": false' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Interception"+'"' in every_data:
                    if '"' + "tier" + '"' + ":"+' "' +selection3 + '"' in every_data:
                        send_message()
                        print("message send")
    elif selection == "railjack":
        if selection2 == "skirmish":
            if '"isStorm": True' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Skirmish"+'"' in every_data:
                    if '"' + "tier" + '"' + ":"+' "' +selection3 + '"' in every_data:
                        send_message()
                        print("message send")
        elif selection2 == "volatile":
            if '"isStorm": True' in every_data and '"' + "missionType" + '"' + ":"+' "'+"Volatile"+'"' in every_data:
                    if '"' + "tier" + '"' + ":"+' "' +selection3 + '"' in every_data:
                        send_message()
                        print("message send")
    time.sleep(1800)




