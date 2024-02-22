from abc import ABC, abstractmethod
from enum import Enum, unique
from random import shuffle

from typing import List, Optional


@unique
class Suit(Enum):
    Club = 0
    Diamond = 1
    Heart = 2
    Spade = 3


SUIT_REPR = {
    Suit.Spade: 's',
    Suit.Club: 'c',
    Suit.Heart: 'h',
    Suit.Diamond: 'd'
}


class Card(ABC):
    def __init__(self, c: int, s: Suit):
        self._face_value = c
        self._suit = s
        self.__available = True

    @abstractmethod
    def value(self):
        raise NotImplementedError

    def is_available(self) -> bool:
        return self.__available

    def mark_unavailable(self):
        self.__available = False

    def mark_available(self):
        self.__available = True

    def print(self):
        face_values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        f_v = face_values[self._face_value - 1]
        s_r = SUIT_REPR[self._suit]
        print(f'{f_v}{s_r}', end=' ')


class BlackJackCard(Card):
    def __init__(self, c: int, s: Suit):
        super().__init__(c, s)

    def value(self) -> int:
        if self.is_ace():
            return 1
        elif self.is_face_card():
            return 10
        else:
            return self._face_value

    def min_value(self):
        if self.is_ace():
            return 1
        else:
            return self.value()

    def max_value(self):
        if self.is_ace():
            return 11
        else:
            return self.value()

    def is_ace(self) -> bool:
        return self._face_value == 1

    def is_face_card(self) -> bool:
        return 11 <= self._face_value <= 13


class Hand:
    def __init__(self):
        self.cards = []  # type: Optional[List[Card]]

    def score(self) -> int:
        score = 0
        for card in self.cards:
            score += card.value()
        return score

    def add_card(self, card: Card):
        self.cards.append(card)

    def print(self):
        for card in self.cards:
            card.print()


class BlackJackHand(Hand):
    def score(self):
        scores = self.possible_scores()
        max_under = -1
        min_over = pow(2, 31) - 1
        for score in scores:
            if 21 < score < min_over:
                min_over = score
            elif 21 >= score > max_under:
                max_under = score
        return min_over if max_under == -1 else max_under

    def possible_scores(self) -> List[int]:
        scores = []
        if self.cards is None or not len(self.cards):
            return scores
        for card in self.cards:
            self.add_card_to_score_list(card, scores)
        return scores

    def add_card_to_score_list(self, card: BlackJackCard, scores: List[int]) -> None:
        if len(scores) == 0:
            scores.append(0)
        for i, score in enumerate(scores):
            scores[i] = scores[i] + card.min_value()
            if card.min_value() != card.max_value():
                scores.append(scores[i] + card.max_value())

    def busted(self) -> bool:
        return self.score() > 21

    def is_black_jack(self):
        if not self.cards:
            return False
        elif len(self.cards) != 2:
            return False
        first, second = self.cards[0], self.cards[1]
        return (first.is_ace() and second.is_face_card()) or (first.is_face_card() and second.is_ace())


class Deck:
    def __init__(self):
        self.cards = None
        self.dealt_index = 0  # Marks first undealt card

    def set_deck_of_cards(self, deck_of_cards):
        self.cards = deck_of_cards

    def shuffle(self) -> None:
        shuffle(self.cards)

    def remaining_cards(self):
        return len(self.cards) - self.dealt_index

    def deal_card(self):
        if self.remaining_cards() == 0:
            return None

        card = self.cards[self.dealt_index]
        card.mark_unavailable()
        self.dealt_index += 1

        return card

    def print(self):
        for card in self.cards:
            card.print()


class BlackJackGameAutomator:
    HIT_UNTIL = 16

    def __init__(self, num_players: int):
        self.hands = [None] * num_players
        for i in range(len(self.hands)):
            self.hands[i] = BlackJackHand()
        self.deck = None

    def deal_initial(self) -> bool:
        for hand in self.hands:
            card1 = self.deck.deal_card()
            card2 = self.deck.deal_card()
            if card1 is None or card2 is None:
                return False
            hand.add_card(card1)
            hand.add_card(card2)
        return True

    def initialize_deck(self):
        cards = []
        for i in range(1, 14):
            for j in range(0, 4):
                cards.append(BlackJackCard(i, Suit(j)))

        self.deck = Deck()
        self.deck.set_deck_of_cards(cards)
        self.deck.shuffle()

    def print_hands_and_score(self):
        for i in range(len(self.hands)):
            print(f'Hand {i} ({self.hands[i].score()}): ', end='')
            self.hands[i].print()
            print(' ')

    def get_black_jacks(self) -> List[int]:
        winners = []
        for i, hand in enumerate(self.hands):
            if hand.is_black_jack():
                winners.append(i)
        return winners

    def play_hand(self, hand):
        while hand.score() < self.HIT_UNTIL:
            card = self.deck.deal_card()
            if not card:
                return False
            hand.add_card(card)
        return True

    def play_all_hands(self):
        for hand in self.hands:
            if not self.play_hand(hand):
                return False
        return True

    def get_winners(self):
        winners = []
        winning_score = 0
        for i, hand in enumerate(self.hands):
            if not hand.busted():
                if hand.score() > winning_score:
                    winning_score = hand.score()
                    winners.clear()
                    winners.append(i)
                elif hand.score() == winning_score:
                    winners.append(i)
        return winners


def question(num_hunds) -> None:
    automator = BlackJackGameAutomator(num_hunds)
    automator.initialize_deck()
    success = automator.deal_initial()
    if not success:
        print('Error. Out of cards.')
    else:
        print('-- Initial --')
        automator.print_hands_and_score()
        black_jacks = automator.get_black_jacks()
        if len(black_jacks) > 0:
            print(f'Blackjack at: {*black_jacks,}\n')
        else:
            success = automator.play_all_hands()
            if not success:
                print('Error. Out of cards.')
            else:
                print(f'\n -- Completed Game --')
                automator.print_hands_and_score()
                winners = automator.get_winners()
                if len(winners) > 0:
                    print(f'Winners: {*winners,}\n')
                else:
                    print('Draw. All players have busted.')


if __name__ == '__main__':
    num_hands = 5
    question(num_hands)
