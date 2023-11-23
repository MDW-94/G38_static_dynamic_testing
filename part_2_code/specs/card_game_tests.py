import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Spade", 1)
        self.card2 = Card("Heart", 10)
        self.card3 = Card("Club", 5)


    def testAceCanBeChecked(self):
        test = CardGame.check_for_ace(self, self.card1)
        self.assertEqual(True, test)

    def testRetrieveHighestCard(self):
        test = CardGame.highest_card(self, self.card2, self.card3)
        self.assertEqual(self.card2, test)

    def testCardsTotal(self):
        cards = [self.card1, self.card2, self.card3]
        test = CardGame.cards_total(self, cards)
        self.assertEqual("You have a total of 16", test)

