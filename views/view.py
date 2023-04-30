from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QPushButton, QSpacerItem
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from controllers.database.user_controller import User
from views.popupInscripton import TestDialog


class MainWindow(QMainWindow):
    def __init__(self, Controller):
        super().__init__()
        self.controller = Controller
        self.setWindowTitle("IIT HEALTH CENTER")
        self.showMaximized()

        # Container 1
        container1 = QWidget()
        container1.setStyleSheet("background-color: white;")

        # Ajouter 3 étiquettes et deux zones d'entrée
        label = QLabel('CONNEXION')
        font = QFont('Arial', 20)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        label.setStyleSheet("color: black;")

        label1 = QLabel('Login :')
        font = QFont('Arial', 16)
        label1.setFont(font)
        label1.setStyleSheet("color: black;")
        self.input1 = QLineEdit()

        label2 = QLabel('Password :')
        label2.setFont(font)
        label2.setStyleSheet("color: black;")
        self.input2 = QLineEdit()
        self.input2.setEchoMode(QLineEdit.Password)

        label3 = QLabel('Créer un nouveau compte')
        font = QFont('Arial', 10)
        label3.setFont(font)
        label3.setAlignment(Qt.AlignmentFlag.AlignRight)
        label3.setStyleSheet("color: red; text-decoration: underline;")
        # label3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        label3.mousePressEvent = self.show_test_dialog

        # Ajouter des espaces
        spacer = QSpacerItem(40, 40)
        spacer2 = QSpacerItem(40, 20)

        # Ajouter un bouton
        button = QPushButton("Valider")
        button.setStyleSheet("""
            QPushButton {
                background-color: red;
                border: none;
                color: white;
                font-weight: bold;
                padding: 10px;
            }

            QPushButton:hover {
                background-color: #B30000;
            }

            QPushButton:pressed {
                background-color: #800000;
            }
        """)
        button.clicked.connect(lambda: User.loginUser(self))

        # Ajouter un layout vertical pour le container1
        container1_layout = QVBoxLayout()
        container1_layout.addItem(spacer2)
        container1_layout.addWidget(label)
        container1_layout.addItem(spacer)
        container1_layout.addWidget(label1)
        container1_layout.addWidget(self.input1)
        container1_layout.addItem(spacer)
        container1_layout.addWidget(label2)
        container1_layout.addWidget(self.input2)
        container1_layout.addItem(spacer)
        container1_layout.addWidget(button)
        container1_layout.addStretch()
        container1_layout.addWidget(label3)
        container1.setLayout(container1_layout)

        # Layout pour les deux containers
        container_layout = QHBoxLayout()
        container_layout.addStretch()
        container_layout.addWidget(container1)
        container_layout.addStretch()

        # Le conteneur de la fenêtre principale avec le layout pour les deux containers
        main_container = QWidget()
        main_container.setStyleSheet("background-color: black;")
        main_container.setLayout(container_layout)

        self.setCentralWidget(main_container)
        self.log = {'adjetey@gmail.com': 'password1', 'jaber@gmail.com': 'password2',
                    'moh@gmail.com': 'password3', 'gode@gmail.com': 'password4', 'max@gmail.com': 'password5'}

    def show_test_dialog(self, event):
        self.test_dialog = TestDialog()
        self.test_dialog.show()
