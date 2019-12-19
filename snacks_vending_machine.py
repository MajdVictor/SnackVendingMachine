import random

class SnackSlot:
    
    def __init__(self):
        self.__snack_items = {}

    def fill_snacks_slot(self):
        ''' This function is used to create the snacks dictionary.
        Keys are tuples(x, y). x and y represent the coordinates of a specific snack.
        values are lists of two indices, 1st index is the quantity of a specific snack and 2nd index is the price of the snack.'''
        
        for x in range(5):
            for y in range(5):
                self.__snack_items[(x + 1, y + 1)] = [5, random.randint(1, 60)]

    def print_snack_dict(self):
        ''' prints out the dictionary and used for testing purposes '''

        print(self.__snack_items)
    
    def get_snack_coordinates(self, num):
        ''' This functions returns the coordinates (x, y) of the chosen snack (1-25).
        It returns False if the num is less than 0 or more than 25 '''

        if 0 < num <= 5:
            x = 1
            y = num

            if y == 0:
                y = 5

            return x, y

        elif 5 < num <= 25:
            if num % 5 == 0:
                x = num // 5
            else:
                x = (num // 5) + 1

            y = num % 5

            if y == 0:
                y = 5

            return x, y

        else:
            return False
    
    def check_snack_availability(self, num):
        ''' This function returns True if the quantity of the chosen snack is more than 0 or the number of a snack exists.
        Otherwise, it returns False '''
        
        if self.get_snack_coordinates(num):
            x, y = self.get_snack_coordinates(num)

        else:
            return False

        if (x, y) in self.__snack_items.keys() and self.__snack_items[
            (x, y)][0] > 0:

            return self.__snack_items[(x, y)]

        return False

    def dispense_snack(self, num):
        ''' This function decreases the quantity of a snack by 1'''

        # checking snack availability
        x, y = self.get_snack_coordinates(num)

        if self.check_snack_availability(num):
            self.__snack_items[(x, y)][0] -= 1
            
        else:
            print('Snack is unavailable!\n')
    
    def display_snacks(self):
        '''Prints out the snacks board'''

        z = 1
        for i in range(5):
            for x in range(5):
                if z < 10:
                    print('0' + str(z) + '|', end='')
                else:
                    print(str(z) + '|', end='')

                z += 1
            print('\n')
    

class MoneySlot:
    ''' Money Slot class '''

    def __init__(self, payment_method):

        self.payment_method = payment_method


class ValidateMoney:
    
    amount = 0
    currency = 'USD'
    coins = [0.1, 0.2, 0.5, 1]
    notes = [20, 50]

    def return_amount(self):
        '''The function returns the accumulated amount of money when the user inserts money'''

        return round(self.amount, 1)

    def add_to_amount(self, money_inserted):
        self.amount += money_inserted

    def check_if_money_valid(self, money_slot_object, money_inserted):
        '''Checks money validity (coins: 10- 20- 50 cents or $1, bank notes: $20 or $50, and cards).'''
        if money_slot_object.payment_method == 'coins':

            if money_inserted in self.coins:
                self.add_to_amount(money_inserted)
                return True
            else:
                print('only coins:[0.1, 0.2, 0.5, 1] can be used!\n')
                return False

        elif money_slot_object.payment_method == 'notes':
            if money_inserted in self.notes:
                self.add_to_amount(money_inserted)
                return True
            else:
                print('You can only use $20 and $50\n')
                return False


if __name__ == "__main__":

    snack_slot = SnackSlot()
    snack_slot.fill_snacks_slot() 
    snack_slot.display_snacks()
    money_validation = ValidateMoney()
    amount = 0 # the accumulated amount

    #asking the user to enter the snack's number.
    while True:
        try:
            snack_number = int(input('Pick one of the snacks above: '))
            break
        except:
            print ('Please enter a numeric value.\n')
            continue
    #returning the snack's quantity and price 
    unit = snack_slot.check_snack_availability(snack_number)

    if unit:
        print('Snack is available and costs: $', unit[1], '\n')
    #if the snack doesn't exist ,the system keeps asking the user to enter a correct number or a different snack
    else:
        while snack_number > 25 or snack_number < 1:
            print("Snack isn't available\n")

            try:
                snack_number = int(input('Pick one of the snacks above: '))
                unit = snack_slot.check_snack_availability(snack_number)

                if unit:
                    break
                continue
            
            except:
                continue

        unit = snack_slot.check_snack_availability(snack_number)
        print('Snack is available and costs: $', unit[1])

    #The user chooses the payment method 
    payment_method = input('please choose a payment method \n(1) coins\n(2) Bank notes\n(3) Cards\n(4) Cancel\n-----> ')
       
    if payment_method == '1':
        money_slot = MoneySlot('coins')

    elif payment_method == '2':
        money_slot = MoneySlot('notes')

    elif payment_method == '3':
        #assuming the card is valid and has enough balance
        amount = float(unit[1])
        print('Paid: $', amount)

    elif payment_method == '4':
        exit()

    else:
        print('No such option!')
        exit()

    #The while block keeps looping and asking the user to insert money until the accumulated amount
    #is equal to the snack's price.

    while float(amount) < float(unit[1]):
        
        try:
            x = float(input('please insert the money: '))
            pass
        except:
            print('enter a numerical value!\n')
            continue
        
        #displaying the accumulated amount of money
        if money_validation.check_if_money_valid(money_slot, x):
            print('accumulated amount: ', money_validation.return_amount(), '\n')

        amount = money_validation.return_amount()

        #breaking the loop if the amount is equal to the snack's price and displaying the change on the screen
        if amount > unit[1]:
            print('Change: ', round(amount - unit[1], 1))
            break

    print('Get your snack and have a nice day!')
    snack_slot.dispense_snack(snack_number)