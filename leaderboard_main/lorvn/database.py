import os
import requests
import json

riot_key = os.environ['RIOT_API']

dat_getter = open(os.path.join(os.path.dirname(__file__) , 'data/players_data.json'))

target_players = (json.loads(dat_getter.read()))['players']

dat_getter.close()

def getMastersData(region, state):
    counter = 0
    detect = []
    sorted_players = []
    url = "https://%s.api.riotgames.com/lor/ranked/v1/leaderboards/?api_key=%s" % (region, riot_key)
    data = json.loads(requests.get(url).text)
    for player in target_players[region]:
        for checker in data["players"]:
            if player["ingameID"] == checker["name"]:
                detect.append({ "facebook":player["facebook"], "ingameID":player["ingameID"], "rank":checker["rank"]})
                counter += 1
    def sorter(e):
        return e["rank"]
    detect.sort(key=sorter)
    if (state == "list"):
        return detect
    elif (state == "count"):
        return counter


def getMastersCount(region):
    url = "https://%s.api.riotgames.com/lor/ranked/v1/leaderboards/?api_key=%s" % (region, riot_key)
    data = json.loads(requests.get(url).text)
    return len(data["players"])

