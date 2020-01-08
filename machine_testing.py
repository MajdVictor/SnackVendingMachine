import unittest
from snacks_vending_machine import ValidateMoney, SnackSlot, MoneySlot

class MachineTesting(unittest.TestCase):

    def setUp(self):

        self.money_validation = ValidateMoney()
        self.snack_slot = SnackSlot()
        self.note_slot = MoneySlot('notes')
        self.coin_slot = MoneySlot('coins')

    def test_add_amount(self):

        self.money_validation.add_to_amount(15)
        result = self.money_validation.return_amount()
        self.assertEqual(result, 15)

    def test_snack_coordinates(self):

        x,y = self.snack_slot.get_snack_coordinates(25)
        self.assertEqual(x, 5)
        self.assertEqual(y, 5)

        result = self.snack_slot.get_snack_coordinates(0)
        self.assertFalse(result)

        result = self.snack_slot.get_snack_coordinates(26)
        self.assertFalse(result)
    
    def test_check_money_validity(self):

        result = self.money_validation.check_if_money_valid(self.coin_slot, 0.1)
        self.assertTrue(result)

        result = self.money_validation.check_if_money_valid(self.coin_slot, 0.3)
        self.assertFalse(result)

        result = self.money_validation.check_if_money_valid(self.note_slot, 20)
        self.assertTrue(result)

        result = self.money_validation.check_if_money_valid(self.note_slot, 60)
        self.assertFalse(result)

    def test_dispense_snack(self):

        self.snack_slot.fill_snacks_slot()

        self.snack_slot.dispense_snack(1)
        
        first_snack_quantity = self.snack_slot.return_snack_dict()
        self.assertEqual(first_snack_quantity[(1,1)][0], 4)




if __name__ == "__main__":
    unittest.main()
    
    

