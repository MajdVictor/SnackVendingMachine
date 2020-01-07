import unittest
from snacks_vending_machine import ValidateMoney,SnackSlot

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
    
    def test_check_snack_availability(self):
        
if __name__ == "__main__":
    unittest.main()
    
    

