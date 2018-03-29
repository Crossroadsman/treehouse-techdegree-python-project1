import csv

filename = 'soccer_players.csv'

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

    for player in players:
        if player['Soccer Experience'] == 'YES':
            experienced.append(player)
        elif player['Soccer Experience'] == 'NO':
            inexperienced.append(player)
        else:
            raise ValueError("{}'s experience is {}, which is an invalid value".format(player['Name'], player['Soccer Experience']))

    return (experienced, inexperienced)


if __name__ == "__main__":

    players = csv_to_dictlist(filename=filename)

    (experienced, inexperienced) = split_players(players)

    print("EXPERIENCED:")
    print("============")
    for player in experienced:
        for key in player.keys():
            print("{}: {}".format(key, player[key]))
    print("INEXPERIENCED:")
    print("==============")
    for player in inexperienced:
        for key in player.keys():
            print("{}: {}".format(key, player[key]))

