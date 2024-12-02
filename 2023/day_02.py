with open("./input.txt", "r") as f:
    lines = f.readlines()

colors = ["red", "green", "blue"]

target_bags = {"red": 12, "green": 13, "blue": 14}

possible_sum = 0

# part 1
for i, line in enumerate(lines):
    current_bags = {"red": 0, "green": 0, "blue": 0}
    text = line.rstrip()
    game_idx = i+1
    bags = text.replace(f"Game {game_idx}: ", "")
    sets = bags.split("; ")

    for cubes in sets:
        cubes = cubes.split(", ")
            
        for color in colors:
            for item in cubes:
                if color in item:
                    num_color = int(item.split(f" {color}")[0])
                    current_bags[color] = max(num_color, current_bags[color])              

    for x, y in zip(target_bags, current_bags):
        if target_bags[x] < current_bags[y]:
            add_to_bag = False
            break
        else:
            add_to_bag = True

    if add_to_bag:
        possible_sum += game_idx

print(possible_sum)

# part 2
power_sum = 0
for i, line in enumerate(lines):
    current_bags = {"red": 0, "green": 0, "blue": 0}
    text = line.rstrip()
    game_idx = i+1
    bags = text.replace(f"Game {game_idx}: ", "")
    sets = bags.split("; ")

    for cubes in sets:
        cubes = cubes.split(", ")
            
        for color in colors:
            for item in cubes:
                if color in item:
                    num_color = int(item.split(f" {color}")[0])
                    current_bags[color] = max(num_color, current_bags[color])              

    red_num = current_bags["red"]
    green_num = current_bags["green"]
    blue_num = current_bags["blue"]

    power = red_num * green_num * blue_num

    power_sum += power

print(power_sum)