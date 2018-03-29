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


# Create teams list
# -----------------
def create_teams_list(team_names, team_rosters):
    output_text = []

    for i in range( len(team_names) ):
        output_text.append(team_names[i])

        for player in team_rosters[i]:
            player_details = ", ".join(player.values())
            output_text.append(player_details)


    if len(team_rosters[len(team_names)]) != 0:
        output_text.append("Unallocated Players")
        for player in team_rosters[len(team_names)]:
            player_details = ", ".join(player.values())
            output_text.append(player_details)

    return output_text


# Write teams list to file
# ------------------------
def create_file(filename, datalist):
    with open(filename, 'w') as file_handle:
        for row in datalist:
            file_handle.write(row)
            file_handle.write("\n")

# Create filename from name
# -------------------------
def create_filename_from_player(player):
    name_components = player['Name'].split()
    joined_components = "_".join(name_components)
    return "{}.txt".format(joined_components)

# Create welcome letter
# ---------------------
def create_welcome_letter(team_name, player, first_practice_datetime):
    output_text = []
    output_text.append('Dear {}:'.format(player['Guardian Name(s)']))
    output_text.append('We are delighted to welcome {} to the {}.'.format(player['Name'], team_name))
    output_text.append("{}'s first practice will be on {}.".format(player['Name'], first_practice_datetime))
    output_text.append("Yours truly, League Coordinator")
    return output_text

# Create letters
# --------------
def create_letters(team_names, team_rosters, first_practice_datetime):
    for i in range(len(team_names)):
        for player in team_rosters[i]:
            letter = create_welcome_letter(team_name=team_names[i],
                                           player=player,
                                           first_practice_datetime=first_practice_datetime)
            filename = create_filename_from_player(player)
            create_file(filename=filename, datalist=letter)

        


if __name__ == "__main__":
    
    input_filename = 'soccer_players.csv'
    # input_filename = 'invalid_players.csv'
    output_filename = 'teams.txt'

    teams = ['Sharks',
             'Dragons',
             'Raptors',
            ]

    first_practice_datetime = "April 15, 2018"

    players = csv_to_dictlist(filename=input_filename)
    
    team_rosters = allocate_players(players=players, teams=teams)

    team_details = create_teams_list(team_rosters=team_rosters,
                                     team_names=teams)

    create_file(filename=output_filename, datalist=team_details)

    create_letters(team_names=teams,
                   team_rosters=team_rosters,
                   first_practice_datetime=first_practice_datetime)
