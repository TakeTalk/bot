from unittest import result
import requests
# import json

def lat_solve(adr) :
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={adr}&key=API_KEY"
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    json_response = response.json()
    repository1 = json_response["results"][0]["geometry"]["location"]["lat"]
    repository2 = json_response["results"][0]["geometry"]["location"]["lng"]
    
    loc = [repository1,repository2]
    return loc
  
def nearby(find,adr) :
    if find=='hotels' or find=='hotel':
        find='lodging'

    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat_solve(adr)[0]},{lat_solve(adr)[1]}&radius=20000&types={find}&keyword=best&key=API_KEY"

    payload={}
    headers = {}
   
    
    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = response.json()
    result= json_response["results"]
    return result


def createLink(lat,lng):
    mapLink=f"https://www.google.com/maps/place/{lat}+{lng}"
    return mapLink



def fetch(find,adr):
    total=nearby(find,adr)
    name=[]
    if(len(total)>=4):
        for i in range(0,4):
            loc=[total[i]["geometry"]["location"]['lat'],total[i]["geometry"]["location"]['lng']]
            loc_link=createLink(loc[0],loc[1])
            name.append([[total[i]["name"],total[i]["vicinity"],loc_link]])
    else:
        for i in range(0,len(total)):
            loc=[total[i]["geometry"]["location"]['lat'],total[i]["geometry"]["location"]['lng']]
            loc_link=createLink(loc[0],loc[1])
            name.append([[total[i]["name"],total[i]["vicinity"],loc_link]])
    
    return name

# print(len(fetch("restaurant","siuri")))
    

    
# print(nearby("restaurant","siuri"))

# https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=34.2268475,77.56194189999999&radius=15000&type=bar&key=API_KEY