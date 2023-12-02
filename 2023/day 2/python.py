import re

try:
    with open('input.txt') as file:
        l = [(i.rstrip('\n')) for i in file.readlines()]
except FileNotFoundError:
    with open('day 2/input.txt') as file:
        l = [(i.rstrip('\n').split('')) for i in file.readlines()]


games = []

# parsing games
for line in l:
    game_id = line.split(':')[0]
    pulls = line.split(':')[1].split(';')

    e = []
    for pull in pulls:
        d = {}
        for i in pull.split(','):
            d[i.split()[1]] = i.split()[0]
        e.append(d) 

    games.append(e) 


def part1(): 
    games_max = []

    for game in games:
        game_max = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        for pull in game:
            for key, value in pull.items():
                if int(value) > int(game_max[key]):
                    game_max[key] = value

        games_max.append(game_max)

    max_values = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    possible_games = []

    for i in range(len(games_max)):
        possible = True
        for key, value in games_max[i].items():
            if int(value) > max_values[key]:
                possible = False

        if possible:
            possible_games.append(i+1)

    print("Part 1: ", sum(possible_games))


def part2(): 
    games_min = []

    for game in games:
        game_max = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        for pull in game:
            for key, value in pull.items():
                if int(value) > int(game_max[key]):
                    game_max[key] = value

        games_min.append(game_max)

    total = 0
    for game in games_min:
        power = 1
        for value in game.values():
            power *= int(value)

        total += power

    print("Part 2: ", total)


if __name__ == "__main__":
    part1()
    part2()
