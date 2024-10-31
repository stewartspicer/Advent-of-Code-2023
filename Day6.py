import math
import re

class Race:
    def __init__(self, distance, time):
        self.distance = distance
        self.time = time

    def calculateDistance(self, hold_time):
        time_remaining = self.time - hold_time
        return time_remaining * hold_time

    def getFirstWinningTime(self):
        for time in range(0, self.time):
            distance = self.calculateDistance(time)
            if distance > self.distance:
                return time
    def getNumWaysToWin(self):
        #I feel like there's a smarter way to just determine this algebraically
        min_time = self.getFirstWinningTime()
        return self.time - (min_time * 2) + 1



def parseRaces() -> list:
    file = open("Day6.txt")
    races_part_one = []
    time_row, distance_row = file.readlines()
    times = list(map(int, re.findall(r"\d+", time_row)))
    distances = list(map(int, re.findall(r"\d+", distance_row)))
    for i, time in enumerate(times):
        distance = distances[i]
        race = Race(distance, time)
        races_part_one.append(race)

    #I know this is ugly, but I was having fun
    time_part_two = int("".join(list(map(str, times))))
    distance_part_two = int("".join(list(map(str, distances))))

    return [races_part_one, Race(distance_part_two, time_part_two)]



def main():
    [races, race_two] = parseRaces()
    print("Part one solution: " + str(math.prod([race.getNumWaysToWin() for race in races])))
    print("Part two solution: " + str(race_two.getNumWaysToWin()))

if __name__ == "__main__":
    main()