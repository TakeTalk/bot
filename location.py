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
   
def nearby(f,adr,i) :

    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat_solve(adr)[0]},{lat_solve(adr)[1]}&radius=5000&types={f}&keyword=best&key=AIzaSyDFSNXLSQfHubvY3KZl9TiVXZR-R9uCXdY"

    payload={}
    headers = {}
   
    
    response = requests.request("GET", url, headers=headers, data=payload)
    # json_response = response.json() 
    # repository = json_response["results"][i]["name"]

    # response=response.json.loads()
    print(response.text)
    # return repository
    


   
nearby("restaurant","kolkata",5)

# https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=34.2268475,77.56194189999999&radius=15000&type=bar&key=AIzaSyDFSNXLSQfHubvY3KZl9TiVXZR-R9uCXdY