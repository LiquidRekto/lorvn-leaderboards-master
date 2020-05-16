import os
import requests
import json

riot_key = os.environ['RIOT_API']

def getMastersData(region):
    url = "https://%s.api.riotgames.com/lor/ranked/v1/leaderboards/?api_key=%s" % (region, riot_key)
    data = json.loads(requests.get(url).text)
    for player in data["players"]:
        print(player)
