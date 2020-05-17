import os
import requests
import json

riot_key = os.environ['RIOT_API']

dat_getter = open('data/players_data.json')

target_players = (json.loads(dat_getter))['players']

dat_getter.close()

def getMastersData(region):
    detect = []
    sorted_players = []
    url = "https://%s.api.riotgames.com/lor/ranked/v1/leaderboards/?api_key=%s" % (region, riot_key)
    data = json.loads(requests.get(url).text)
    for player in target_players[region]:
        for checker in data:
            if player['ingameID'] == checker['name']:
                detect.append({ "facebook":player["facebook"], "ingameID":player["ingameID"], "rank":checker["rank"]})
    return detect
