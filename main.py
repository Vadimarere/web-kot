import vk_api
import random
import time
import datetime
token = "d5fa43392c8878ed152bed49d2d52ba01c54c9fdacc99ad7b1ea727864cac233ca10b00efc1310db92b45"


vk = vk_api.VkApi(token=token)

vk._auth_token()

data = {}
now = datetime.datetime.now()
timeA = now.hour

def construct(id,name,money,power):
    p = {}
    p["name"] = name
    p["money"] = money
    p["messegNumb"] = 0
    p["power"] = power

    data[id] = p
    print(data)

    return "normal"


while True:
    try:
        now = datetime.datetime.now()
        timeB = now.hour
        
        if timeA<timeB:
            timeA = timeB

            for i in data:
                data[i]["money"] = data[i]["money"] + data[i]["power"]
                print(data)
        
        elif (timeA>timeB) and (timeB == 0):
            timeA = 0
            for i in data:
                data[i]["money"] = data[i]["money"] + data[i]["power"]


        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет":
                
                n = 0
                for i in data:
                    if id == i :
                        n = 1
                if n == 0:
                    construct(id , id , 0 , 10)
                print(data)


                vk.method("messages.send", {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "кто я?":
                vk.method("messages.send", {"peer_id": id, "message": "ты хороший человек", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "стата":
                smg = str(data[id]["money"])+"$"
                smg = smg + "\n" + str(data[id]["power"]) + "доход/в час"
                vk.method("messages.send", {"peer_id": id, "message": smg, "random_id": random.randint(1, 2147483647)})

    except Exception as E:
        time.sleep(1)
