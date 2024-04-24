import json
file = open('ex5.json', 'r')
list = json.load(file)
file.close()  
for snacks in list:
    if snacks["name"] == "Old Fashioned":
        snacks["batters"]["batter"].append({"id": "5001", "type": "Tea"})
        break

file = open('ex5.json', 'w')
json.dump(list, file, indent=4)
file.close()  
