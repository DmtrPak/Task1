import json #connect the json module
import re #connect the re module


data = json.loads() #serialize json 
# create variables for tasks
check = 0
task1_1 = 0
task1_2 = 0
task1_3 = 0
task1_4 = 0
task1_5_854x480 = 0
task1_5_865x482 = 0
task1_5_960x540 = 0
task1_5_720x576 = 0
task1_5_1280x720 = 0
task1_5_1920x1080 = 0
for i in data["streams"]:
    if not (i["media_info_json"]["tracks"][check]["height"]):
        check += 1
        if not (i["media_info_json"]["tracks"][check]["height"]):
            break
    if (i["media_info_json"]["tracks"][check]["height"] == 480) :
        task1_5_854x480 += 1    

    print(str(i["streams"][0]["media_info_json"]["tracks"][check]["height"]))
    if i["name"] != "cam408_1_222":
        if re.match("...:\/\/239.100.1.6(.*)", i["url"]): #offline (239.100.1.6)
            task1_1 = task1_1 + 1
        else: 
            if (i["url"] != "udp://239.100.1.6:1234") and re.match("...:\/\/239(.*)", i["url"]): #starting 239 with out 239.100.1.6
                task1_2 += 1
            else:
                if re.match("...:\/\/238.166(.*)", i["url"]): #starting 238.166
                    task1_3 += 1
                else:
                    if re.match("...:\/\/238.166(.*)", i["url"]) is  None and re.match("...:\/\/238(.*)", i["url"]): #starting 238 with out 238.166
                        task1_4 += 1


print(str("Task 1: " + str(task1_1)))
print(str("Task 2: " + str(task1_2)))
print(str("Task 3: " + str(task1_3)))
print(str("Task 4: " + str(task1_4)))
print(str("Task 5: " + str(task1_5_854x480)))
