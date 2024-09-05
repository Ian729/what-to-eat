import requests, os, json, random

API_KEY = os.getenv("GAODE_API_KEY")
GEO = os.getenv("MY_LOCATION")
RADIUS = 1000
TYPE = "05" # Restaurant -> https://i.xdc.at/assets/images/poi-data/poi-type-list.pdf
PAGE_SIZE = "30"
SHOW_FIELDS = 'rating'
URL = f"https://restapi.amap.com/v3/place/around?key={API_KEY}&location={GEO}&radius={RADIUS}&types={TYPE}&page_size={PAGE_SIZE}&show_fields={SHOW_FIELDS}"

# get
response = json.loads(requests.get(URL).text)
# sort
restaurants = sorted(response["pois"], key=lambda x: x['biz_ext']["rating"] if x['biz_ext']["rating"] else "", reverse=True)
# random pick
name = random.choice([restaurant['name'] for restaurant in restaurants])
print(name)