import requests


#helpful repos and documentation:
# http://espn-fantasy-football-api.s3-website.us-east-2.amazonaws.com/
# https://github.com/cwendt94/espn-api
# https://www.fleaflicker.com/api-docs/index.html


# Goals for ESPN data:
# 1. get the end of year roster with names of players and origin
# 2. get transaction data from the year


def main():
    league_id = '986823'
    year = '2023'
    scoring_period_id = 19
    # url = f"https://fantasy.espn.com/apis/v3/games/ffl/leagueHistory/{league_id}?season_id={year}"

    #trying to get transaction data for players using this url directly below; new_url works for the rest of the script
    url = f"https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/{year}/segments/0/leagues/{league_id}?scoringPeriodId={scoring_period_id}"
    params = {
                'view': ['mTeam', 'mTransactions', 'mRoster', 'mStatus', 'mDraftDetail', 'mPendingTransactions',
                         'mPositionalRatings', 'mTransactions', 'mTransaction']#, 'mMatchup', 'mSettings', 'mStandings']
            }
    headers = {
        'Cookie': 'device_b212002c=8ce91300-7aed-47de-9ff8-a5f3dcfe2136; SWID=5E9DADBA-B003-413D-C18E-6275F2419E9A; AMCVS_EE0201AC512D2BE80A490D4C%40AdobeOrg=1; s_ecid=MCMID%7C42924780630337082723151427568090277438; AMCV_EE0201AC512D2BE80A490D4C%40AdobeOrg=-330454231%7CMCIDTS%7C19966%7CMCMID%7C42924780630337082723151427568090277438%7CMCAAMLH-1725590809%7C7%7CMCAAMB-1725590809%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1724993209s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.1.2; country=us; s_cc=true; ESPN-ONESITE.WEB-PROD-ac=XUS; ESPN-ONESITE.WEB-PROD.token=5=eyJhY2Nlc3NfdG9rZW4iOiJleUpyYVdRaU9pSm5kV1Z6ZEdOdmJuUnliMnhzWlhJdExURTJNakF4T1RNMU5EUWlMQ0poYkdjaU9pSkZVekkxTmlKOS5leUpxZEdraU9pSlVVRlZpVERreWVqSkthM2ROTkdFMFdFbG5lbVpCSWl3aWFYTnpJam9pYUhSMGNITTZMeTloZFhSb0xuSmxaMmx6ZEdWeVpHbHpibVY1TG1kdkxtTnZiU0lzSW1GMVpDSTZJblZ5Ympwa2FYTnVaWGs2YjI1bGFXUTZjSEp2WkNJc0ltbGhkQ0k2TVRjeU5EazROakF4TUN3aWJtSm1Jam94TnpJME9UZzBNVFV3TENKbGVIQWlPakUzTWpVd056STBNVEFzSW1Oc2FXVnVkRjlwWkNJNklrVlRVRTR0VDA1RlUwbFVSUzVYUlVJdFVGSlBSQ0lzSW1OaGRDSTZJbWQxWlhOMElpd2liR2xrSWpvaU4yVmlPV1l3T0RjdE56VTRNUzAwWTJaakxXRTRaalF0TlRFNE1ESXdaV1EyTkRZeUlpd2lhV1JsYm5ScGRIbGZhV1FpT2lJMlkyRXhaakl6WVMweU9EUm1MVFE0WkRJdFlqRTJZeTAzTkRjM1pEUTNZV1ZqT1RNaUxDSnpkV0lpT2lKN1FURXdOek0yUXpFdE56a3lOUzAwUkRVMkxUaEdNRE10TXpGRk56WkROVEE0TWprMWZTSjkuY0tBdGFBQnJzejgybWVJaXJUaGhtWUIwbG1oemtka2k5Z1RfcndwdXp3bnFtRC1YTHNEWUhCSVRBTWNSUkx6OUk2MS1oWm5JeGxTRldVLUgwQjI1ZmciLCJyZWZyZXNoX3Rva2VuIjoiZXlKcmFXUWlPaUpuZFdWemRHTnZiblJ5YjJ4c1pYSXRMVEUyTWpBeE9UTTFORFFpTENKaGJHY2lPaUpGVXpJMU5pSjkuZXlKcWRHa2lPaUp1WDNsaWVFbEJOR001YVZKSExVTlVRVnBxTkVSUklpd2ljM1ZpSWpvaWUwRXhNRGN6TmtNeExUYzVNalV0TkVRMU5pMDRSakF6TFRNeFJUYzJRelV3T0RJNU5YMGlMQ0pwYzNNaU9pSm9kSFJ3Y3pvdkwyRjFkR2d1Y21WbmFYTjBaWEprYVhOdVpYa3VaMjh1WTI5dElpd2lZWFZrSWpvaWRYSnVPbVJwYzI1bGVUcHZibVZwWkRwd2NtOWtJaXdpYVdGMElqb3hOekkwT1RnMk1ERXdMQ0p1WW1ZaU9qRTNNalE1T0RReE5UQXNJbVY0Y0NJNk1UYzBNRFV6T0RBeE1Dd2lZMnhwWlc1MFgybGtJam9pUlZOUVRpMVBUa1ZUU1ZSRkxsZEZRaTFRVWs5RUlpd2lZMkYwSWpvaWNtVm1jbVZ6YUNJc0lteHBaQ0k2SWpkbFlqbG1NRGczTFRjMU9ERXROR05tWXkxaE9HWTBMVFV4T0RBeU1HVmtOalEyTWlJc0ltbGtaVzUwYVhSNVgybGtJam9pTm1OaE1XWXlNMkV0TWpnMFppMDBPR1F5TFdJeE5tTXROelEzTjJRME4yRmxZemt6SW4wLlI1WHBzaXhGMm53VmpFbFBzZG5FNktsRFExU2dMY3FIZE9Jbl9OcWhwZWM5NjlvVmVzLWF5bmh0UzBOWFBoMWdOUHVQMmgxM2REbUN3WmpmSlg5LURBIiwic3dpZCI6IntBMTA3MzZDMS03OTI1LTRENTYtOEYwMy0zMUU3NkM1MDgyOTV9IiwidHRsIjo4NjM5OSwicmVmcmVzaF90dGwiOjE1NTUxOTk5LCJoaWdoX3RydXN0X2V4cGlyZXNfaW4iOjAsImluaXRpYWxfZ3JhbnRfaW5fY2hhaW5fdGltZSI6MTcyNDk4NDE1MDAwMCwiaWF0IjoxNzI0OTg2MDEwMDAwLCJleHAiOjE3MjUwNzI0MTAwMDAsInJlZnJlc2hfZXhwIjoxNzQwNTM4MDEwMDAwLCJoaWdoX3RydXN0X2V4cCI6MTcyNDk4NTk1MDAwMCwic3NvIjpudWxsLCJhdXRoZW50aWNhdG9yIjpudWxsLCJsb2dpblZhbHVlIjpudWxsLCJjbGlja2JhY2tUeXBlIjpudWxsLCJzZXNzaW9uVHJhbnNmZXJLZXkiOiJNMXpnY3BnczNYVWVyV0hfNXdaanJVTkhMUVJsRGRpTkZEVFV0QS0zM0VsRTZXYlZ3akNWdFYtSks1WGlWUzJxUkRaekhKaEcybTZOT1Z6NkZIeEdqUlRWNENxbFVXWFpiQV9aMk0xQm9DU21Wbno2OUFVIiwiY3JlYXRlZCI6IjIwMjQtMDgtMzBUMDI6NDY6NTEuMDQ5WiIsImxhc3RDaGVja2VkIjoiMjAyNC0wOC0zMFQwMjo0Njo1MS4wNDlaIiwiZXhwaXJlcyI6IjIwMjQtMDgtMzFUMDI6NDY6NTAuMDAwWiIsInJlZnJlc2hfZXhwaXJlcyI6IjIwMjUtMDItMjZUMDI6NDY6NTAuMDAwWiJ9|eyJraWQiOiJndWVzdGNvbnRyb2xsZXItLTE2MjAxOTM1NDQiLCJhbGciOiJFUzI1NiJ9.eyJqdGkiOiJLczNNMTYtOEhIZGJWQjJ5RHhEUWlBIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLnJlZ2lzdGVyZGlzbmV5LmdvLmNvbSIsImF1ZCI6IkVTUE4tT05FU0lURS5XRUItUFJPRCIsInN1YiI6IntBMTA3MzZDMS03OTI1LTRENTYtOEYwMy0zMUU3NkM1MDgyOTV9IiwiaWF0IjoxNzI0OTg2MDEwLCJuYmYiOjE3MjQ5ODQxNTAsImV4cCI6MTcyNTA3MjQxMCwiY2F0IjoiaWR0b2tlbiIsImlkZW50aXR5X2lkIjoiNmNhMWYyM2EtMjg0Zi00OGQyLWIxNmMtNzQ3N2Q0N2FlYzkzIn0.RgA2vQEj9GK29fdhisFeSYmzW_dzD2IPLJOeZtUqy7YgYb14d-cf-ssLfF8RQWhhdv7sfk2HfCtmGHqLcQErSw; check=true; userZip=60615; hashedIp=2ba0cac4f27d90e18ba35f286f7354c9da3afe38ddd81065670446b2d86b7462; _gcl_au=1.1.1987848994.1724986702; espnAuth={"swid":"{A10736C1-7925-4D56-8F03-31E76C508295}"}; _cb=3GKXFCzUEf6DbJa0p; IR_gbd=espn.com; tveProvider=Comcast_SSO; FCNEC=%5B%5B%22AKsRol9wsWW-yBiyKv1JZtitMY-7dtaXRu8k3nAvE868SvQ73J77u1oCuRPDQvZwA4TLKUSiUItEJByNNgwSxSqsdgnvdcyOk7fM5Q0L3kc0r0JOCKpLd0D7KZXFPJpoa7HCK8Lb37ej8D5LZPysQKeBnWhUyrxmRQ%3D%3D%22%5D%5D; mbox=session#5ed34f8eb9104a5bba05e3a90705e250#1724988803|PC#5ed34f8eb9104a5bba05e3a90705e250.34_0#1788231743; tveMVPDAuth=acc%2Csec%2Cespnews%2Cespn1%2Cespn3%2Cespn2%2Cespndeportes%2Cespnu; tveAuth=acc%2Csec%2Cespnews%2Cespn1%2Cespn3%2Cespn2%2Cespndeportes%2Cespnu; tveProviderName=Comcast_SSO; dtcAuth=; _fbp=fb.1.1724986945910.923785285926761454; AMCVS_5BFD123F5245AECB0A490D45%40AdobeOrg=1; AMCV_5BFD123F5245AECB0A490D45%40AdobeOrg=-1506532908%7CMCMID%7C42924780630337082723151427568090277438%7CMCIDTS%7C19966%7CvVersion%7C4.4.0%7CMCAID%7CNONE%7CMCOPTOUT-1724994146s%7CNONE%7CMCAAMLH-1725591746%7C7%7CMCAAMB-1725591746%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI; tvid=6db38ac3b46648648340b52481b9e488; s_c24_s=Less%20than%201%20day; block.check=false%7Cfalse; _cb_svref=https%3A%2F%2Ffantasy.espn.com%2Ffootball%2Fwelcome%3Fex_cid%3DFFL11_vanwelcome_url%26rand%3Dref~%257B%2522ref%2522%253A%2522https%253A%252F%252Fwww.google.com%252F%2522%257D; espn_s2=AEC6dq3KCHbPet3t96NIqnDxTytK2%2BkUDwHTFL46Mxl78tvYClmxcVy05Jbz4ouQMgb1Ph7wHLtGSJjVLm8u8FqbBP2CW6oCylBm%2BsYd4kFqwLdinbvdR9TE8ynT08hh8DTshc8FR4zQW6G1DhtqekbSJAqSad4eOWNtYdZinMuiMID0tqXjdaRoz4hSPD%2BST%2FiA16AhGv01xb0%2B9jOHbNRxNmUxQjxTfc8toVyyk6xpgAazoUK4T3qbsIRqUiy344l5vqJyzzkTBIcbfXwMwsoZdCdJIza1J9Opl904pwLKsg%3D%3D; ESPN-ONESITE.WEB-PROD.idn=00c9ec66c7; _pubcid=c834a577-be59-4dc7-9acb-cf45483cc2e5; _pubcid_cst=1izpLMgsJw%3D%3D; _cc_id=c9baa1a4fc9cc30ab0e4c3131b219d0; panoramaId_expiry=1725595550735; panoramaId=94451b972390af91df8e58dc50364945a70249246faef5ed0121fe36966344f4; panoramaIdType=panoIndiv; _ga_H0P43ZY447=GS1.1.1724990735.1.1.1724990967.0.0.0; _au_1d=AU1D-0100-001724986226-986KA6FA-P8OE; _v__chartbeat3=iUggiCfYYFHOIUDn; _ga=GA1.2.815892975.1724990735; _gid=GA1.2.640464972.1724991936; espn-prev-page=fantasy%3Afootball%3Aleague%3Arosters; _chartbeat2=.1710884378330.1724992178168.0000000000000001.DgUKaUCjPqpaDDPnaFDGQJgQCtyr0F.19; s_ensNR=1724992178322-Repeat; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Aug+29+2024+23%3A29%3A38+GMT-0500+(Central+Daylight+Time)&version=202407.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=0848b088-9a1f-4899-b61b-db0f136655ed&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CBG1145%3A1%2CC0002%3A1%2CC0004%3A1%2CC0005%3A1&AwaitingReconsent=false; s_gpv_pn=fantasy%3Afootball%3Aleague%3Arosters; s_c6=1724992178749-Repeat; IR_9070=1724992178784%7C0%7C1724992178784%7C%7C; __gads=ID=0e5a228ce21977e6:T=1724986701:RT=1724992179:S=ALNI_MarK_YQf3QzOAIeN7oAM7kUDUQkkQ; __gpi=UID=00000edec01c8a90:T=1724986701:RT=1724992179:S=ALNI_MZD6VkxJc3y77QYifj3QytlAu5ttg; __eoi=ID=87986a8839dae8d5:T=1724986701:RT=1724992179:S=AA-AfjY4Hulf-VIo28o3cEXdxi6_; cto_bundle=hgDDtl9TQk5ZN015dEVCQ3BwM3cybHExdyUyQlZDSDZLaGhPS3VoZ3liUlhzJTJGTWVSOGl4JTJGTmlWWER6M3JjakFscEdEZFN1bDNOeDFjeEpZY1NLSFBTMzhad2hDdnY0VUdpVWx5U3l4UW5jZjNSbzk2bnVkOUJqTlE3WTFmMnBlTjAlMkI5eHRqTzl6U1l1VjNRU1MzOGRVNGp6dHZOQlVuRXp6OHJwS0JUWWwxMHZLak5YdFc1Y1c2c2ppc2kxRTBVTXA0Q1I2Tw; s_c24=1724992335986; s_sq=wdgespcom%252Cwdgespge%3D%2526pid%253Dfantasy%25253Afootball%25253Aleague%25253Arosters%2526pidt%253D1%2526oid%253Dfunctionmr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DA'
    }
    new_url = f"https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/leagueHistory/{league_id}?season_id={year}"
    initial_response = requests.get(url, params=params, headers=headers)

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
        if year.get('seasonId') == 2023:
            puka = [x for x in year.get('draftDetail', {}).get('picks', {}) if x.get('playerId', '') == 4426515]
            print(puka)

    owner_ids_to_names = {y.get('id'): y.get('name') for y in [item for sublist in [x for x in owners_by_year_dictionary.values()] for item in sublist]}

    final_dict = {
        owner_ids_to_names.get(x, 'Ghost?'): owner_id_to_yearly_stats.get(x) for x in owner_id_to_yearly_stats.keys()
    }



    print("Let's see it!")



if __name__ == '__main__':
    main()