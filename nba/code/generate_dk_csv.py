import json
import sys

import pandas as pd


# lineup is a pandas dataframe, uses depth first search
# positions order = ['PG', 'SG', 'SF', 'PF', 'C', 'G', 'F', 'UTIL']
# this uses depth first search to associate players with positions
def lineup_to_positions(lineup, positions, i=0):
    r = True
    for p in positions:
        if p is None:
            r = False
    if r:
        return positions

    if lineup.at[i, 'PG'] and positions[0] is None:
        positions[0] = lineup.at[i, 'Name']
        a = lineup_to_positions(lineup, i=i+1, positions=positions)
        if a is None:
            positions[0] = None
        else:
            return a

    if lineup.at[i, 'SG'] and positions[1] is None:
        positions[1] = lineup.at[i, 'Name']
        a = lineup_to_positions(lineup, i=i+1, positions=positions)
        if a is None:
            positions[1] = None
        else:
            return a

    if lineup.at[i, 'SF'] and positions[2] is None:
        positions[2] = lineup.at[i, 'Name']
        a = lineup_to_positions(lineup, i=i+1, positions=positions)
        if a is None:
            positions[2] = None
        else:
            return a    

    if lineup.at[i, 'PF'] and positions[3] is None:
        positions[3] = lineup.at[i, 'Name']
        a = lineup_to_positions(lineup, i=i+1, positions=positions)
        if a is None:
            positions[3] = None
        else:
            return a

    if lineup.at[i, 'C'] and positions[4] is None:
        positions[4] = lineup.at[i, 'Name']
        a = lineup_to_positions(lineup, i=i+1, positions=positions)
        if a is None:
            positions[4] = None
        else:
            return a

    if (lineup.at[i, 'PG'] or lineup.at[i, 'SG']) and positions[5] is None:
        positions[5] = lineup.at[i, 'Name']
        a = lineup_to_positions(lineup, i=i+1, positions=positions)
        if a is None:
            positions[5] = None
        else:
            return a

    if (lineup.at[i, 'PF'] or lineup.at[i, 'SF']) and positions[6] is None:
        positions[6] = lineup.at[i, 'Name']
        a = lineup_to_positions(lineup, i=i+1, positions=positions)
        if a is None:
            positions[6] = None
        else:
            return a

    if positions[7] is None:
        positions[7] = lineup.at[i, 'Name']
        a = lineup_to_positions(lineup, i=i+1, positions=positions)
        if a is None:
            positions[7] = None
        else:
            return a

    return None

# translates players to their corresponding ids
# checks with user to correct any discrepancies in name between rotogrinders and draftkings
def lineup_to_ids(lineup):
    if lineup is None:
        return None
    id_lineup = [None] * 8
    for i in range(len(lineup)):
        j = csv.index[csv['Name'] == lineup[i]].tolist()
        if j == []:
            if lineup[i] in js:
                j = csv.index[csv['Name'] == js[lineup[i]]].tolist()
                if j == []:
                    del js[lineup[i]]
                else:
                    id_lineup[i] = csv.at[j[0], 'ID']
            else:
                n = ''
                while n == '' or csv.index[csv['Name'] == n].tolist() == []:
                    n = input('{} >> '.format(lineup[i]))
                    if n == '~~~~':
                        return None
                    else:
                        nlist = csv.index[csv['Name'] == n].tolist()
                        if nlist != []:
                            print('accepted')
                            id_lineup[i] = csv.at[nlist[0], 'ID']
                            js[lineup[i]] = n
                        else:
                            print('not accepted')
        else:
            id_lineup[i] = csv.at[j[0], 'ID']
    
    return id_lineup


# generates draftkings csv to upload, given solution lineups
def generate_csv(lineups):
    js = {}
    with open('player_names.json') as f:
        js = json.loads(f.read())

    csv = pd.read_csv('dk_salaries.csv', skiprows=7)

    # final dataframe to turn into csv and upload to draftkings
    df = pd.DataFrame(columns=['PG', 'SG', 'SF', 'PF', 'C', 'G', 'F', 'UTIL'])

    j = 0
    for i in range(len(lineups)):
        lineups[i].index = [0, 1, 2, 3, 4, 5, 6, 7]
        a = lineup_to_ids(lineup_to_positions(lineups[i], positions=[None]*8))
        if a is not None:
            df.loc[i] = a
            j += 1

    df.to_csv('dk_upload.csv', index=None)

    with open('draftkings_infrastructure/player_names.json', 'w') as f:
        f.write(json.dumps(js))
