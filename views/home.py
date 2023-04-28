from PyQt5.QtWidgets import QComboBox, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QPushButton,QSpacerItem
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout

import sys

from views.view import MainWindow
from views.doctorLogin import DoctorLoginPage

class HomeWindow(QMainWindow):
    def __init__(self,Controller):
        super().__init__()
        self.controller = Controller
        self.setWindowTitle("HOSPITAL MANAGEMENT")
        # Container 1
        container1 = QWidget()
        container1.setStyleSheet("background-color: white;")
        container1.setFixedHeight(400)
        container1.setFixedWidth(400)

            # Ajouter une étiquette
        label = QLabel('Vous êtes :')
        font = QFont('Arial', 20)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        # Ajouter des boutons
        button_utilisateur = QPushButton("Utilisateur")
        button_utilisateur.clicked.connect(self.on_utilisateur_button_clicked)

        button_caissiere = QPushButton("Caissière")
        button_caissiere.clicked.connect(self.on_caissiere_button_clicked)

        button_docteur = QPushButton("Docteur")
        button_docteur.clicked.connect(self.on_docteur_button_clicked)

        button_administrateur = QPushButton("Administrateur")
        button_administrateur.clicked.connect(self.on_administrateur_button_clicked)

        # Ajouter un layout pour les boutons
        grid_layout = QGridLayout()
        grid_layout.addWidget(button_utilisateur, 0, 0)
        grid_layout.addWidget(button_caissiere, 0, 1)
        grid_layout.addWidget(button_docteur, 1, 0)
        grid_layout.addWidget(button_administrateur, 1, 1)

        # Ajouter un layout vertical pour le container1
        container1_layout = QVBoxLayout()
        container1_layout.addWidget(label)
        container1_layout.addLayout(grid_layout)
        container1.setLayout(container1_layout)

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

    def on_utilisateur_button_clicked(self):
        self.close()
        self.user_page = MainWindow(Controller=self.controller)
        self.user_page.show()

    def on_caissiere_button_clicked(self):
        # TODO : Ajouter la fonctionnalité pour la caissière
        pass

    def on_docteur_button_clicked(self):
        self.close()
        self.doctor_login_page = DoctorLoginPage(Controller=self.controller)
        self.doctor_login_page.show()

    def on_administrateur_button_clicked(self):
        # TODO : Ajouter la fonctionnalité pour l'administrateur
        pass

