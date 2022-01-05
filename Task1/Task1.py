import json #connect the json module
import re #connect the re module


data = json.loads() #serialize json 
# create variables for tasks
check = 0
task1_1 = 0
task1_2 = 0
task1_3 = 0
task1_4 = 0
task1_5 = {}
for i in data["streams"]:
    if re.match("cam(.*)", i["name"]) is None:
        if i["name"] != "ohotnik_i_rybolov_319":
            if i["media_info_json"]["tracks"][check]["content"] != "video":
                check += 1
                if i["media_info_json"]["tracks"][check]["content"] != "video":
                    check += 1
            conc = str(i["media_info_json"]["tracks"][check]["pixel_width"]) + "x" + str(i["media_info_json"]["tracks"][check]["pixel_height"])
            if conc in task1_5:
                task1_5[conc] += 1
            else:
                task1_5[conc] = 1 
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

print(str("Task 1: " + str(task1_1)))
print(str("Task 2: " + str(task1_2)))
print(str("Task 3: " + str(task1_3)))
print(str("Task 4: " + str(task1_4)))
print("Task 5:")
for key, value in task1_5.items():
        print(key, value)
