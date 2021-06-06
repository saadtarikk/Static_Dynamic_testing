import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card = Card("Spades", 1)
        self.card1 = Card("Hearts", 5)
        self.card2 = Card("Diamonds", 3)
        self.cards = [self.card, self.card1, self.card2]

    def test_check_for_ace(self):
        self.assertEqual(1, self.card.value)

    def test_highest_card(self):
        self.assertEqual("Hearts", self.card1.suit)

    def test_cards_total(self):
        cardgame = CardGame()
        self.assertEqual("You have total of, 9",
                         cardgame.cards_total(self.cards))
