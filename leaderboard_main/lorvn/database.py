import os
import requests
import json

riot_key = os.environ['RIOT_API']

dat_getter = open(os.path.join(os.path.dirname(__file__) , 'data/players_data.json'))

target_players = (json.loads(dat_getter.read()))['players']

dat_getter.close()

def getMastersData(region):
    detect = []
    sorted_players = []
    url = "https://%s.api.riotgames.com/lor/ranked/v1/leaderboards/?api_key=%s" % (region, riot_key)
    data = json.loads(requests.get(url).text)
    for player in target_players[region]:
        print(player)
        #for checker in data:
            #if player['ingameID'] == checker['name']:
            #    detect.append({ "facebook":player["facebook"], "ingameID":player["ingameID"], "rank":checker["rank"]})
    return detect
