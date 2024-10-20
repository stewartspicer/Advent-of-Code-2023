class Card:
    def __init__(self, winning_numbers, given_numbers, card_id):
        self.winning_numbers = winning_numbers
        self.given_numbers = given_numbers
        self.id = card_id

    def get_match_count(self):
        matches = 0
        for winning_number in self.winning_numbers:
            if winning_number in self.given_numbers:
                matches += 1
        return matches

    def problem_one_score(self):
        matches = self.get_match_count()
        if matches == 0:
            return 0
        return pow(2, matches - 1)

def score_card_recursive(card, card_array):
    matches = card.get_match_count()
    if matches == 0:
        return 1

    starting_index = card.id + 1

    to_return = 1
    for index in range(starting_index, matches + starting_index):
        if index in card_array.keys():
            next_card = card_array[index]
            to_return += score_card_recursive(next_card, card_array)

    return to_return


def main():
    puzzle_input = open("Day4.txt").read()

    raw_cards = puzzle_input.split("\n")
    problem_one_score = 0
    card_array = {}
    for raw_card in raw_cards:
        [card_id_chunk, numbers_chunk] = raw_card.split(":")
        card_id = int(card_id_chunk.split(" ")[-1])

        [winning_numbers_raw, given_numbers_raw] = numbers_chunk.split(" | ")
        winning_numbers = []
        winning_numbers_array = winning_numbers_raw.split(" ")
        for winning_number in winning_numbers_array:
            if winning_number == "":
                continue
            winning_numbers.append(winning_number)

        given_numbers = []
        given_numbers_array = given_numbers_raw.split(" ")
        for given_number in given_numbers_array:
            if given_number == "":
                continue
            given_numbers.append(given_number)

        card = Card(winning_numbers, given_numbers, card_id)
        card_array[card.id] = card
        problem_one_score += card.problem_one_score()

    problem_two_score = 0
    for card in card_array.values():
        problem_two_score += score_card_recursive(card, card_array)

    print(problem_one_score)
    print(problem_two_score)

if __name__ == "__main__":
    main()