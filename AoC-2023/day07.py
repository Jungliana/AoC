from collections import defaultdict
from typing import Self


class Hand:
    CARD_DICT = {"A": 14,
                 "K": 13,
                 "Q": 12,
                 "J": 11,
                 "T": 10}

    def __init__(self, cards: str, bet: int) -> None:
        self.cards = cards
        self.bet = int(bet)
        self.type = self.define_type()
        self.card_values = self.translate_cards()

    def translate_cards(self) -> list[int]:
        return [(Hand.CARD_DICT.get(n, n) if n in Hand.CARD_DICT else int(n)) for n in self.cards]

    def define_type(self) -> int:
        counter_dict = defaultdict(int)
        for letter in self.cards:
            counter_dict[letter] += 1
        dict_len = len(counter_dict.keys())
        dict_sorted = sorted(counter_dict.values())

        if dict_len == 1:
            return 7
        if dict_len == 2:
            if dict_sorted == [1, 4]:
                return 6
            return 5
        if dict_len == 3:
            if dict_sorted == [1, 1, 3]:
                return 4
            return 3
        if dict_len == 4:
            return 2
        return 1

    def __str__(self) -> str:
        return f'cards: {self.cards}, bet: {self.bet}, type: {self.type}, values: {self.card_values}'

    def __lt__(self, other: Self) -> bool:
        if self.type == other.type:
            for selfvalue, othervalue in zip(self.card_values, other.card_values):
                if selfvalue != othervalue:
                    return selfvalue < othervalue
        return self.type < other.type


def read_data(path: str) -> list[list[str]]:
    lines = []
    with open(path, encoding="ASCII") as file:
        for line in file:
            lines.append(line.rstrip().split())
    return lines


def solve_part1(data) -> int:
    hand_objs = [Hand(data[0], data[1]) for data in data]
    hand_objs.sort()
    bet_sum = 0
    for i, hand in enumerate(hand_objs):
        bet_sum += (i+1) * hand.bet
    return bet_sum


def solve_part2(data):
    pass


if __name__ == "__main__":
    data_input = read_data("AoC-2023/inputs/input07.txt")
    print(f'Part 1 solution: {solve_part1(data_input)}')
    print(f'Part 2 solution: {solve_part2(data_input)}')
