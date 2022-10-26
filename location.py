from unittest import result
import requests
# import json

def lat_solve(adr) :
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={adr}&key=AIzaSyDFSNXLSQfHubvY3KZl9TiVXZR-R9uCXdY"
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
    range=1000
    result= []
    while len(result)<9:
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat_solve(adr)[0]},{lat_solve(adr)[1]}&radius={range}&types={find}&keyword=best&key=AIzaSyDFSNXLSQfHubvY3KZl9TiVXZR-R9uCXdY"

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



def fetch(find,adr):
    total=nearby(find,adr)
    print(len(total))
    name=[]
   
    return name


# print(fetch("restaurant","kolkata"))
    

    
# print(nearby("restaurant","siuri"))

# https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=34.2268475,77.56194189999999&radius=15000&type=lodging&key=AIzaSyDFSNXLSQfHubvY3KZl9TiVXZR-R9uCXdY