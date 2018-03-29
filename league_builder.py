import csv


# Read the CSV data
# -----------------
def csv_to_dictlist(filename):
    output_dictlist = []

    with open(filename, newline='') as csv_file:
        dict_reader = csv.DictReader(csv_file)
        rows = list(dict_reader)
        for row in rows:
            output_dictlist.append(row)

    return output_dictlist


# Split players into experienced and inexperienced
# ------------------------------------------------
def split_players(players):
    experienced = []
    inexperienced = []
    invalid = []

    for player in players:
        if player['Soccer Experience'] == 'YES':
            experienced.append(player)
        elif player['Soccer Experience'] == 'NO':
            inexperienced.append(player)
        else:
            invalid.append(player)

    return (experienced, inexperienced, invalid)

# Allocate players to teams
# -------------------------
def allocate_players(players, teams):
    (experienced, inexperienced, invalid) = split_players(players)

    team_rosters = []
    for team in teams:
        team_rosters.append([])
    team_index = 0

    while len(experienced) % len(teams) != 0:
        # the experienced players cannot be evenly allocated to teams
        last_player = experienced.pop()
        invalid.append(last_player)
    for player in experienced:
        team_rosters[team_index].append(player)
        team_index = (team_index + 1) % len(teams)

    while len(inexperienced) % len(teams) != 0:
        # the inexperienced players cannot be evenly allocated to teams
        last_player = inexperienced.pop()
        invalid.append(last_player)
    for player in inexperienced:
        team_rosters[team_index].append(player)
        team_index = (team_index + 1) % len(teams)

    team_rosters.append(invalid)

    return team_rosters



if __name__ == "__main__":
    
    filename = 'soccer_players.csv'
    # filename = 'invalid_players.csv'

    teams = ['Sharks',
             'Dragons',
             'Raptors',
            ]

    players = csv_to_dictlist(filename=filename)
    allocated_players = allocate_players(players, teams)

    for i in range(len(teams)):
        print(teams[i])
        print("=" * len(teams[i]))
        for player in allocated_players[i]:
            print(player['Name'])
    if len(allocated_players[len(teams)]) != 0:
        print("INVALID PLAYERS")
        print("===============")
        for player in allocated_players[len(teams)]:
            print(player['Name'])


