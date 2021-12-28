import json #connect the json module
import re #connect the re module


data = json.loads() #serialize json 
# create variables for tasks
check = 0
task1_1 = 0
task1_2 = 0
task1_3 = 0
task1_4 = 0
task1_5 = {
            "854x480": 0,
            "856x480": 0,
            "960x540": 0,
            "720x576": 0,
            "1280x720": 0,
            "1920x1080": 0
    }
for i in data["streams"]:
    if re.match("cam(.*)", i["name"]) is None:
        if i["name"] != "ohotnik_i_rybolov_319":
            if i["media_info_json"]["tracks"][check]["content"] != "video":
                check += 1
                if i["media_info_json"]["tracks"][check]["content"] != "video":
                    check += 1
            if (i["media_info_json"]["tracks"][check]["pixel_width"] == 854):
                task1_5["854x480"] += 1   
            if (i["media_info_json"]["tracks"][check]["pixel_width"] == 856):
                task1_5["856x480"] += 1
            if (i["media_info_json"]["tracks"][check]["pixel_width"] == 960):
                task1_5["960x540"] += 1
            if (i["media_info_json"]["tracks"][check]["pixel_width"] == 720):
                task1_5["720x576"] += 1
            if (i["media_info_json"]["tracks"][check]["pixel_width"] == 1280):
                task1_5["1280x720"] += 1
            if (i["media_info_json"]["tracks"][check]["pixel_width"] == 1920):
                task1_5["1920x1080"] += 1
            check = 0


        if re.match("...:\/\/239.100.1.6(.*)", i["url"]): #offline (239.100.1.6)
            task1_1 = task1_1 + 1
        else: 
            if (i["url"] != "udp://239.100.1.6:1234") and re.match("...:\/\/239(.*)", i["url"]): #starting 239 with out 239.100.1.6
                task1_2 += 1
            else:
                if re.match("...:\/\/238.166(.*)", i["url"]): #starting 238.166
                    task1_3 += 1
                else:
                    if re.match("...:\/\/238.166(.*)", i["url"]) is None and re.match("...:\/\/238(.*)", i["url"]):  #starting 238 with out 238.166
                        task1_4 += 1
       # print(i["name"])

print(str("Task 1: " + str(task1_1)))
print(str("Task 2: " + str(task1_2)))
print(str("Task 3: " + str(task1_3)))
print(str("Task 4: " + str(task1_4)))
print(str("854x480: " + str(task1_5["854x480"])))
print(str("856x480: " + str(task1_5["856x480"])))
print(str("960x540: " + str(task1_5["960x540"])))
print(str("720x576: " + str(task1_5["720x576"])))
print(str("1280x720: " + str(task1_5["1280x720"])))
print(str("1920x1080: " + str(task1_5["1920x1080"])))
