import os
os.chdir('C:/Users/delhivery/Desktop/adrs_trial_aug_19')
req = open("request.json")
req_json = req.readlines()
req_json = req_json[1]

import requests
c=requests.post("http://162.243.40.17:8080/route-planner/rest/vehiclerouting/solution/solve",req_json,headers={"content-type":"application/json"})
r = requests.get("http://162.243.40.17:8080/route-planner/rest/vehiclerouting/solution",headers={"Cookie":c.headers['Set-Cookie']})
resp = r.content

data = json.loads(resp)
order = data["vehicleRouteList"][0]["customerList"]
locations = [[str(item["id"]),str(item["latitude"]),str(item["longitude"])] for item in order]

outfile = open("route.csv","w")
outfile.write("id,lat,long")
outfile.write("\n")
for item in locations:
    outfile.write(",".join(item))
    outfile.write("\n")
    
outfile.close()
