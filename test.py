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

def createLink(lat,lng):
    mapLink=f"https://www.google.com/maps/place/{lat}+{lng}"
    return mapLink
   
def nearby(find,adr,i) :

    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat_solve(adr)[0]},{lat_solve(adr)[1]}&radius=5000&types={find}&keyword=best&key=AIzaSyDFSNXLSQfHubvY3KZl9TiVXZR-R9uCXdY"

    payload={}
    headers = {}
   
    
    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = response.json()
    # print(len(json_response["results"]))
    flag=False
    if len(json_response["results"])>i:
        res_type= json_response["results"][i]["types"]
        if find in res_type:
            location = [json_response["results"][i]["geometry"]["location"]['lat'],json_response["results"][i]["geometry"]["location"]['lng']]
            repository=[createLink(location[0],location[1]),json_response["results"][i]["name"]]
            flag=True
        if not flag:
            repository=["--",f"Sorry there is no {find} in that given area"]
        return repository
    else:
        repository=["--",f"Sorry there is no {find} in that given area"]
        return repository

    # response=response.json.loads()

    # print(response.text)

    

    
# print(nearby("lodging","chinsurah",1))

# https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=34.2268475,77.56194189999999&radius=15000&type=bar&key=AIzaSyDFSNXLSQfHubvY3KZl9TiVXZR-R9uCXdY