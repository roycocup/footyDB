import requests
from cached import cached
from pprint import pprint
import pandas as pd


def get_env():
    keys = {}
    with open('.env', 'r') as f:
        ln = f.readline().split("=")
        keys[ln[0]] = ln[1]
    return keys

def call(url:str, params=[]):
    keys = get_env()
    headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': keys['RAID_API_KEY']
    }
    
    return requests.request("GET", url, headers=headers, params=params)

@cached()
def get_stats(team_id: int, league_id: int, season_year: int): 
    url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"
    params = {"league":league_id,"season":season_year,"team":team_id}
    return call(url=url, params=params).json()

@cached()
def get_leagues(country:str):
    url = "https://api-football-v1.p.rapidapi.com/v3/leagues"
    params = {"country":country}
    return call(url=url, params=params).json()

@cached()
def get_league_by_id(team_id:int):
    url = "https://api-football-v1.p.rapidapi.com/v3/leagues"
    params = {"id":team_id}
    return call(url=url, params=params).json()

@cached()
def get_team_info(league:int, season:int=2021):
    url = "https://api-football-v1.p.rapidapi.com/v3/teams"
    params = {"league":league, "season":season}
    return call(url=url, params=params).json()

@cached()
def get_league_by_season(season:int=2021):
    url = "https://api-football-v1.p.rapidapi.com/v3/leagues"
    params = {"season":season}
    return call(url=url, params=params).json()

@cached()
def get_player_stats_by_league(league:int, season:int=2021):
    url = "https://api-football-v1.p.rapidapi.com/v3/players"
    params = {"league":league,"season":season}
    return call(url=url, params=params).json()

@cached()
def get_players_stat_by_team(team_id: int, season:int=2021):
    url = "https://api-football-v1.p.rapidapi.com/v3/players"
    params = {"team":team_id,"season":season}
    return call(url=url, params=params).json()

def p(o):
    pprint(o)
    quit()

if __name__ == "__main__":
    leagues = get_leagues(country="england")
    all_leagues = []
    for league in leagues['response']:
        details = league['league']
        details['country_code'] = league['country']['code']
        details['country_name'] = league['country']['name']
        all_leagues.append(details)
    
    # primeira liga - 94
    # premier league - 39

    # resp = get_team_info(season=2020, league=39)
    # p([{"team_name":x['team']['name'], "team_id":x['team']['id']} for x in resp['response']])
    # p(get_stats(team_id=33, league_id=39, season_year=2021))
    # resp = get_team_info(season=2021, league=39)
    # p([{"team_name":x['team']['name'], "team_id":x['team']['id']} for x in resp['response']])
    # p(get_players_stat_by_team(team_id=33))
    r = get_players_stat_by_team(team_id=33)
    p(r['response'])
    

    
    