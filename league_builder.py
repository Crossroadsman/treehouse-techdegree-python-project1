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


if __name__ == "__main__":

    players = csv_to_dictlist(filename=filename)

    for player in players:
        for key in player.keys():
            print("{}: {}".format(key, player[key]))


