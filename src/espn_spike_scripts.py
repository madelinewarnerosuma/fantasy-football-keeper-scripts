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
    # print(response_json)
    owners_by_year_dictionary, owner_id_to_yearly_stats = {}, {}
    for year in response_json:
        owners_by_year_dictionary[year.get('seasonId')] = [{
            'id': x.get('id'), 'name': f"{x.get('firstName', '')} {x.get('lastName', '')}"
        } for x in year.get('members', [])]

        for x in year.get('teams', []):
            if x.get('primaryOwner') not in owner_id_to_yearly_stats:
                owner_id_to_yearly_stats[x.get('primaryOwner', '')] = {year.get('seasonId', ''): {
                    'team_name': x.get('name'),
                    'final_position': x.get('rankCalculatedFinal'),
                    'points': x.get('points'),
                    'playoff_seed': x.get('playoffSeed')
                }}
            else:
                owner_id_to_yearly_stats[x.get('primaryOwner')][year.get('seasonId', '')] = {
                    'team_name': x.get('name'),
                    'final_position': x.get('rankCalculatedFinal'),
                    'points': x.get('points'),
                    'playoff_seed': x.get('playoffSeed')
                }

    owner_ids_to_names = {y.get('id'): y.get('name') for y in [item for sublist in [x for x in owners_by_year_dictionary.values()] for item in sublist]}

    final_dict = {
        owner_ids_to_names.get(x, 'Ghost?'): owner_id_to_yearly_stats.get(x) for x in owner_id_to_yearly_stats.keys()
    }


    print("Let's see it!")



if __name__ == '__main__':
    main()