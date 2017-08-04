import sys
from PyQt5.QtWidgets import QSpinBox, QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, \
    QPlainTextEdit, QMessageBox, QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QFormLayout, QSizePolicy, QSpacerItem
from PyQt5.QtCore import pyqtSlot
from secretsharing import HexToHexSecretSharer
from PyQt5.QtCore import Qt
from mnemonic import Mnemonic

__version__ = '0.0.1'

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Multicrypt'
        self.left = 10
        self.top = 10
        self.width = 1100
        self.height = 500
        self.initUI()
        self.mm = Mnemonic()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        wid = QWidget(self)
        self.setCentralWidget(wid)
        main = QVBoxLayout()
        wid.setLayout(main)

        info_label = QLabel("Multicrypt is a utility that uses Shamir's secret sharing scheme to split a deterministic"
                            " wallet seed into several seeds in such a way that not all seeds are required to recover "
                            "the seed.\n\n"
                            "Instructions:\n"
                            "1. Open your wallet in Electrum and go to Wallet -> Seed. Copy and paste the seed into this application.\n"
                            "2. Adjust 'Shares Required' according to the number of shares you wish to require in order for you to be able to recover your seed.\n"
                            "3. Adjust 'Shares to Generate' according to the number of shares you wish to distribute.\n"
                            "4. Click on 'Encrypt'. You may verify that the secret shares are reversible using 'Decrypt'.\n"
                            "5. Distribute the secret shares to people you trust. Do not store all shares together digitally in one location.\n\n"
                            "Currently only Electrum deterministic wallets are supported.")

        info_label.setMinimumHeight(180)
        info_label.setAlignment(Qt.AlignTop)

        main.addWidget(info_label)

        self.conf_group = QGroupBox("Configuration")
        layout = QFormLayout()
        #layout.setFieldGrowthPolicy(layout.AllNonFixedFieldsGrow)
        layout.setFieldGrowthPolicy(layout.FieldsStayAtSizeHint)
        layout.setFormAlignment(Qt.AlignLeft)

        self.original = QLineEdit()
        self.original.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.original.setFixedWidth(960)

        layout.addRow(QLabel("Enter Seed"), self.original)

        self.shares_required = QSpinBox()
        self.shares_required.setRange(1, 8)
        self.shares_required.setValue(3)

        self.shares_to_generate = QSpinBox()
        self.shares_to_generate.setRange(1, 8)
        self.shares_to_generate.setValue(8)


        layout.addRow(QLabel("Shares Required"), self.shares_required)
        layout.addRow(QLabel("Shares to Generate"), self.shares_to_generate)

        self.conf_group.setLayout(layout)

        main.addWidget(self.conf_group)

        shares_layout = QFormLayout()
        shares_layout.setFieldGrowthPolicy(layout.AllNonFixedFieldsGrow)
        self.shares_group = QGroupBox("Shares")

        # Create textbox
        self.textboxes = []
        for i in range(8):
            qle = QLineEdit()
            self.textboxes.append(qle)
            shares_layout.addRow(QLabel("Share %s" % (i+1)), qle)

        self.shares_group.setLayout(shares_layout)

        buttons_layout = QHBoxLayout()

        self.button_enc = QPushButton('Encrypt', self)
        self.button_enc.clicked.connect(self.encrypt)
        buttons_layout.addWidget(self.button_enc)

        self.button_dec = QPushButton('Decrypt', self)
        self.button_dec.clicked.connect(self.decrypt)
        buttons_layout.addWidget(self.button_dec)

        about_label = QLabel("For more information, go to: <a href='https://github.com/ronreiter/multicrypt'>https://github.com/ronreiter/multicrypt</a>")
        about_label.setTextFormat(Qt.RichText)
        about_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        about_label.setOpenExternalLinks(True)
        about_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        about_label.setAlignment(Qt.AlignRight)

        buttons_layout.addWidget(about_label)
        #buttons_layout.addSpacerItem(QSpacerItem(900, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        main.addWidget(self.shares_group)

        main.addLayout(buttons_layout)


        self.show()



    @pyqtSlot()
    def encrypt(self):
        if not self.original.text():
            return

        try:
            val = hex(self.mm.mnemonic_decode(self.original.text()))[2:]
        except ValueError:
            QMessageBox.question(self, 'Error', "The seed you entered is invalid.", QMessageBox.Ok, QMessageBox.Ok)
            return

        shares = HexToHexSecretSharer.split_secret(val, self.shares_required.value(), self.shares_to_generate.value())

        for share_no in range(len(shares)):

            ssint = int(shares[share_no].replace("-", "0"), 16)
            ss = self.mm.mnemonic_encode(ssint)
            self.textboxes[share_no].setText(ss)

        self.original.setText("")


    @pyqtSlot()
    def decrypt(self):
        shares = [x.text() for x in self.textboxes if x.text()]
        if not shares:
            return

        hex_shares = []
        for share in shares:
            hex_share = hex(self.mm.mnemonic_decode(share))[2:]
            hex_share = hex_share[0] + "-" + hex_share[2:]
            hex_shares.append(hex_share)

        decrypted = HexToHexSecretSharer.recover_secret(hex_shares)
        self.original.setText(self.mm.mnemonic_encode(int(decrypted, 16)))
        for tb in self.textboxes:
            tb.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())