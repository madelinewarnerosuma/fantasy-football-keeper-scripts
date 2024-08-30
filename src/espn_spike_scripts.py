import requests


#helpful repos and documentation:
# http://espn-fantasy-football-api.s3-website.us-east-2.amazonaws.com/
# https://github.com/cwendt94/espn-api
# https://www.fleaflicker.com/api-docs/index.html

def main():
    league_id = '986823'
    year = '2022'
    # url = f"https://fantasy.espn.com/apis/v3/games/ffl/leagueHistory/{league_id}?season_id={year}"
    params = {
                'view': ['mTeam']# , 'mRoster']#, 'mMatchup', 'mSettings', 'mStandings']
            }
    new_url = f"https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/leagueHistory/{league_id}?season_id={year}"
    initial_response = requests.get(new_url, params=params)

    response_json = initial_response.json()
    print(response_json)


if __name__ == '__main__':
    main()