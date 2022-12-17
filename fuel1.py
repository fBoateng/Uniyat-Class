# price of diesel per litre 14.481
# price of diesel per gallon 14.481

# price of petrol per litre 11.501
# price of petrol per gallon 43.536

# amount_being_bought = float(input('Please enter the amount you are buying? '))


# def conv():
#    litre = amount_being_bought / 11.501
#       return litre


# petrol = conv()
# print(petrol)


'''def qnty_litre():
    user_input = input('Please are you buying per litre or per gallon? ')
    if user_input == 'litre':
        fuelamount = float(input('How much are you buying? '))
        try:
            if user_input == 'litre':
                litre = fuelamount / 11.501
        except:
            if user_input < price_per_litre:
                print('Amount can not be purchased.')
    return litre


def qnty_gallon():
    user_input = input('Please are you buying per litre or per gallon? ')
    if user_input == 'gallon':
        fuelamount = float(input('How much are you buying? '))
        if user_input == 'gallon':
            gallon = fuelamount / 43.536
    return gallon'''

'''price_per_litre = 11.501


def qnty_purchased():
    user_input = float(input('How much are you buying? '))
    if user_input <= price_per_litre:
        print('Invalid Amount entered.')
    amount_purchased = user_input / price_per_litre
    print(f'You are buying {user_input} cedis worth {amount_purchased} litres.)


qnty_purchased()'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget


class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Empty Window in PyQt')


        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec_())







