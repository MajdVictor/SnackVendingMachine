import unittest
from snacks_vending_machine import ValidateMoney, SnackSlot, MoneySlot

class MachineTesting(unittest.TestCase):

    def test_add_amount(self):

        validate_obj = ValidateMoney()
        validate_obj.add_to_amount(15)
        result = validate_obj.return_amount()
        self.assertEqual(result, 15)

    def test_snack_coordinates(self):

        snack_slot = SnackSlot()

        x,y = snack_slot.get_snack_coordinates(25)
        self.assertEqual(x, 5)
        self.assertEqual(y, 5)

        result = snack_slot.get_snack_coordinates(0)
        self.assertFalse(result)

        result = snack_slot.get_snack_coordinates(26)
        self.assertFalse(result)
    
    def test_check_money_validity(self):

        coin_slot = MoneySlot('coins')
        money_validation = ValidateMoney()

        result = money_validation.check_if_money_valid(coin_slot, 0.1)
        self.assertTrue(result)

        result = money_validation.check_if_money_valid(coin_slot, 0.3)
        self.assertFalse(result)

        note_slot = MoneySlot('notes')

        result = money_validation.check_if_money_valid(note_slot, 20)
        self.assertTrue(result)

        result = money_validation.check_if_money_valid(note_slot, 60)
        self.assertFalse(result)

    def test_dispense_snack(self):

        snack_slot = SnackSlot()
        snack_slot.fill_snacks_slot()
        snack_slot.dispense_snack(1)
        first_snack_quantity = snack_slot.return_snack_dict()
        self.assertEqual(first_snack_quantity[(1,1)][0], 4)




if __name__ == "__main__":
    unittest.main()
    
    

