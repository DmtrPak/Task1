import json #���������� ������ json
import re #���������� ������ re


data = json.loads() #������������� json 
#������ ���������� ��� ������ 
task1_1 = 0
task1_2 = 0
task1_3 = 0
task1_4 = 0
for i in data["streams"]:
    if i["name"] != "cam408_1_222":
        if re.match("...:\/\/239.100.1.6(.*)", i["url"]): #������� (239.100.1.6)
            task1_1 = task1_1 + 1
        if (i["url"] != "udp://239.100.1.6:1234") and re.match("...:\/\/239(.*)", i["url"]): #������������ 239 ����� 239.100.1.6
            task1_2 += 1
        if re.match("...:\/\/238.133(.*)", i["url"]): #������������ 238.133
            task1_3 += 1
        if re.match("...:\/\/238.133(.*)", i["url"]) !=  re.match("...:\/\/238(.*)", i["url"]) and re.match("...:\/\/238(.*)", i["url"]): #������������ 238 ��� 238.133
           task1_4 += 1
    
print(str("Task 1: " + str(task1_1)))
print(str("Task 2: " + str(task1_2)))
print(str("Task 3: " + str(task1_3)))
print(str("Task 4: " + str(task1_4)))