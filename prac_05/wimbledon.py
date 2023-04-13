def sortLinesAlphabetically(lines):
    lines = lines[1:]
    for i in range(len(lines)):
        lines[i] = lines[i][5:]

    lines.sort()
    return lines


def addElementToDict(line, country_to_winner):
    elements = line.split(",")
    if elements[0] in country_to_winner.keys():
        if elements[1] in country_to_winner[elements[0]].keys():
            country_to_winner[elements[0]][elements[1]] += 1
        else:
            country_to_winner[elements[0]][elements[1]] = 1
    else:
        country_to_winner[elements[0]] = {}
        country_to_winner[elements[0]][elements[1]] = 1

    return country_to_winner


def getPlayersAndCountries(country_to_winner):
    players = ""
    countries = ", ".join(country_to_winner.keys())
    for country in country_to_winner.keys():
        countryPlayers = "".join(key + " " + str(value) + "\n" for key, value in country_to_winner[country].items())
        players += countryPlayers

    return players, countries


def main():
    filename = "wimbledon.csv"

    countryToWinner = {}

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = sortLinesAlphabetically(in_file.readlines())

        for line in lines:
            countryToWinner = addElementToDict(line, countryToWinner)

    players, countries = getPlayersAndCountries(countryToWinner)

    print("\nWimbledon Champions: \n" + players)

    print("\nThese " + str(len(countryToWinner.keys())) + " countries have won Wimbledon: \n" + countries)


main()