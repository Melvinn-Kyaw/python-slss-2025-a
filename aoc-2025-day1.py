# AOC Day 1
# Author: Melvin Kyaw
# 1 December

def part_one():
    cur_location = 50
    zeroes = 0

    with open("data/aoc-2025-day1.txt") as f:
        for line in f:
            direction = line[0]
            distance = int(line[1:])

            if direction == "R":
                cur_location += distance
            else:
                cur_location -= distance

            if cur_location % 100 == 0:
                zeroes += 1

    print(zeroes)

def part_two():
    pass

if __name__ == "__main__":
    part_one()
