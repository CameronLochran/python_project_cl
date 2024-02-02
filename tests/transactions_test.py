import unittest
from models.transactions import Transactions

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.transaction1 = Transactions(49.99, 69)

    def test_a_transaction(self):
        self.assertEqual("transaction", self.transaction1.amount)

    def test_a_transaction(self):
        self.assertEqual("id", self.transaction1.id)