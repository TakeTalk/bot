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
    if find=='restaurants' or find=='restaurant':
        find='food|restaurant'
    if find=='hospitals' or find=='hospital':
        find='doctor|hospital|medicine'
    if find=='banks' or find=='bank':
        find='bank|finance'
    if find=='atm' or find=='atms':
        find='bank|finance|atm'
    range=5000
    result= []
    while len(result)<9:
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat_solve(adr)[0]},{lat_solve(adr)[1]}&radius={range}&types={find}&keyword=best&key=API_KEY"

        payload={}
        headers = {}
    
        
        response = requests.request("GET", url, headers=headers, data=payload)
        json_response = response.json()
        result= json_response["results"]
        range=range+1000

    return result


def createLink(lat,lng):
    mapLink=f"https://www.google.com/maps/place/{lat}+{lng}"
    return mapLink


#ARKA
def fetch(find,adr):
    total=nearby(find,adr)
    print(len(total))
    name=[]
    i=0
    while (len(name)<5):
        if (total[i]["business_status"]=="OPERATIONAL"):
            loc=[total[i]["geometry"]["location"]['lat'],total[i]["geometry"]["location"]['lng']]
            loc_link=createLink(loc[0],loc[1])
            name.append([total[i]["name"],total[i]["vicinity"],total[i]["rating"],loc_link])
            i+=1
    for k in range(0,len(name)-1):
        for j in range(k+1,len(name)):
            if(name[k][2]<name[j][2]):
                temp=name[k]
                name[k]=name[j]
                name[j]=temp
    return name


# print(fetch("restaurant","kolkata"))
    

    
# print(nearby("restaurant","siuri"))

# https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=34.2268475,77.56194189999999&radius=15000&type=lodging&key=API_KEY'