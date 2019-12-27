import unittest
from snacks_vending_machine import ValidateMoney

class MachineTesting(unittest.TestCase):

    def test_add_amount(self):
        validate_obj = ValidateMoney()
        validate_obj.add_to_amount(15)
        result = validate_obj.return_amount()
        self.assertEqual(result, 15)

if __name__ == "__main__":
    unittest.main()
    
    

