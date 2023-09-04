import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.fuel_types = ['Petrol', 'Diesel']
        self.fuel_type_combo = QComboBox()
        self.fuel_type_combo.addItems(self.fuel_types)

        self.quantity_input = QLineEdit()
        self.price_input = QLineEdit()
        self.payment_method_combo = QComboBox()
        self.payment_method_combo.addItems(['Cash', 'Card'])

        self.total_cost_label = QLabel()

        self.purchase_button = QPushButton('Purchase')
        self.recent_purchases_button = QPushButton('Recent Purchases')
        self.cancel_button = QPushButton('Cancel')

        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel('Fuel Purchasing App'))
        self.layout.addWidget(QLabel('Fuel type:'))
        self.layout.addWidget(self.fuel_type_combo)
        self.layout.addWidget(QLabel('Quantity (Liters):'))
        self.layout.addWidget(self.quantity_input)
        self.layout.addWidget(QLabel('Price per liter:'))
        self.layout.addWidget(self.price_input)
        self.layout.addWidget(QLabel('Payment method:'))
        self.layout.addWidget(self.payment_method_combo)
        self.layout.addWidget(QLabel('Total Cost:'))
        self.layout.addWidget(self.total_cost_label)
        self.layout.addWidget(self.purchase_button)
        self.layout.addWidget(self.recent_purchases_button)
        self.layout.addWidget(self.cancel_button)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.purchase_button.clicked.connect(self.on_purchase_button_clicked)
        self.recent_purchases_button.clicked.connect(self.on_recent_purchases_button_clicked)
        self.cancel_button.clicked.connect(self.on_cancel_button_clicked)

    def on_purchase_button_clicked(self):
        fuel_type = self.fuel_type_combo.currentText()
        quantity = float(self.quantity_input.text())
        price = float(self.price_input.text())
        payment_method = self.payment_method_combo.currentText()
        total_cost = quantity * price
        self.total_cost_label.setText(str(total_cost))

        # Save receipt
        receipt = {'Fuel Type': fuel_type, 'Quantity': quantity, 'Price': price, 'Payment Method': payment_method,
                   'Total Cost': total_cost}
        with open('receipts.txt', 'a') as f:
            f.write(str(receipt) + '\n')

    def on_recent_purchases_button_clicked(self):
        try:
            with open('receipts.txt', 'r') as f:
                receipts = f.readlines()
            self.popup('Recent Purchases', '\n'.join(receipts))
        except:
            self.popup('Error', 'No recent purchases')

    def on_cancel_button_clicked(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
