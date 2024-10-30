import re
import time


def parse_puzzle_input() -> list:
    puzzle_input = open("Day5.txt")
    seeds = []
    seed_maps = {}
    intervals = {}

    current_map_name = ""
    for row in puzzle_input:
        if row.startswith("seeds:"):
            matches = re.findall(r"(\d+ \d+)", row)
            for pair in matches:
                seed_range_start, seed_range_length = list(map(int, re.findall(r"(\d+)", pair)))
                for seed in range(seed_range_start, seed_range_start + seed_range_length):
                    seeds.append(seed)
            # print(matches)
            # print(row)
            # exit()
            # row_stripped = row.split(":")[1].replace("\n", "").strip()
            # numbers = row_stripped.split(" ")
            # i = 0
            # while i < len(numbers) - 1:
            #     for seed in range(int(numbers[i]), int(numbers[i]) + int(numbers[i + 1])):
            #         seeds.append(int(seed))
            #     i += 2
            # for number in numbers:
            #     if number.strip().isnumeric():
            #         seeds.append(int(number))
        elif row == "" or row == "\n":
            current_map_name = ""
        elif row.replace(":", "").replace("-", "").replace(" ", "").strip().isalpha():
            current_map_name = row.split(" ")[0]
        else:
            row_numbers = list(map(int, re.findall(r"(\d+)", row)))

            range_destination = row_numbers[0]
            range_start = row_numbers[1]
            range_end = range_start + row_numbers[2] - 1
            if current_map_name not in intervals.keys():
                intervals[current_map_name] = {}

            intervals[current_map_name][range_destination] = [range_start, range_end]

            # if current_map_name in seed_maps.keys():
            #     seed_map = seed_maps[current_map_name]
            # else:
            #     seed_map = {}
            #
            # range_start = row_numbers[1]
            # range_length = row_numbers[2]
            #
            # for value in range(range_start, range_start + range_length):
            #     seed_map[value] = row_numbers[0] + (value - range_start)
            #
            # seed_maps[current_map_name] = seed_map


    return [seeds, intervals]

def map_seed(seed, seed_maps):
    for destination, this_map in seed_maps.items():
        range_start = this_map[0]
        range_end = this_map[1]
        if range_start <= seed <= range_end:
            return destination + (seed - range_start)

    return seed

def get_location_number(seed, seed_maps):
    soil_number = map_seed(seed, seed_maps['seed-to-soil'])
    fertilizer_number = map_seed(soil_number, seed_maps['soil-to-fertilizer'])
    water_number = map_seed(fertilizer_number, seed_maps['fertilizer-to-water'])
    light_number = map_seed(water_number, seed_maps['water-to-light'])
    temperature_number = map_seed(light_number, seed_maps['light-to-temperature'])
    humidty_number = map_seed(temperature_number, seed_maps['temperature-to-humidity'])
    return map_seed(humidty_number, seed_maps['humidity-to-location'])

def main():
    print("Parsing seeds. This is gonna take a minute")
    [seeds, maps] = parse_puzzle_input()
    print("Checking " + str(len(seeds)) + " seeds. This is gonna longer")

    lowest_location_number = 999999999999999999999999
    for seed in seeds:
        location_number = get_location_number(seed, maps)
        if location_number <= lowest_location_number:
            print("Found new lowest")
            lowest_location_number = location_number
    print(lowest_location_number)

if __name__ == "__main__":
    main()