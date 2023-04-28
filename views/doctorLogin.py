from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QPushButton, QSpacerItem
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout

class DoctorLoginPage(QMainWindow):
    def __init__(self, Controller):
        super().__init__()
        self.controller = Controller
        self.setWindowTitle("Connexion - Docteur")
        # Container 1
        container1 = QWidget()
        container1.setStyleSheet("background-color: white;")
        container1.setFixedHeight(200)
        container1.setFixedWidth(400)

        # Ajouter une étiquette
        label = QLabel('Connexion - Docteur')
        font = QFont('Arial', 20)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        # Ajouter un formulaire de connexion
        username_label = QLabel('Nom d\'utilisateur :')
        self.username_input = QLineEdit()
        password_label = QLabel('Mot de passe :')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        login_button = QPushButton("Se connecter")
        login_button.clicked.connect(self.on_login_button_clicked)

        # Ajouter un layout pour le formulaire de connexion
        grid_layout = QGridLayout()
        grid_layout.addWidget(username_label, 0, 0)
        grid_layout.addWidget(self.username_input, 0, 1)
        grid_layout.addWidget(password_label, 1, 0)
        grid_layout.addWidget(self.password_input, 1, 1)
        grid_layout.addWidget(login_button, 2, 0, 1, 2)

        # Ajouter un layout vertical pour le container1
        self.container1_layout = QVBoxLayout()  # corriger le nom du layout
        self.container1_layout.addWidget(label)
        self.container1_layout.addLayout(grid_layout)
        self.container1_layout.addStretch()
        container1.setLayout(self.container1_layout)  # corriger le nom du layout

        # Layout pour les deux containers
        container_layout = QHBoxLayout()
        container_layout.addStretch()
        container_layout.addWidget(container1)
        container_layout.addStretch()

        # Le conteneur de la fenêtre principale avec le layout pour les deux containers
        main_container = QWidget()
        main_container.setStyleSheet("background-color: red")
        main_container.setLayout(container_layout)

        self.setCentralWidget(main_container)
        self.credentials = {'user1': 'password1', 'user2': 'password2', 'user3': 'password3', 'user4': 'password4', 'user5': 'password5'}

    def on_login_button_clicked(self):
        # Récupérer les informations de connexion
        username = self.username_input.text()
        password = self.password_input.text()

        if username in self.credentials and self.credentials[username] == password:
            # Rediriger vers la page du docteur
            self.close()
            self.doctor_page = DoctorLoginPage(Controller=self.controller)
            self.doctor_page.show()
        else:
            # Afficher un message d'erreur
            error_label = QLabel('Nom d\'utilisateur ou mot de passe incorrect.')
            error_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
            error_label.setStyleSheet("color: red;")
            self.container1_layout.addWidget(error_label)

