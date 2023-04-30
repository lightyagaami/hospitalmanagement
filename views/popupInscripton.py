from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QApplication
from controllers.database.user_controller import User
from views.appointmentWindow import AppointmentWindow


class TestDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Créer un compte')
        self.setFixedSize(500, 500)
        self.setStyleSheet("background-color: white;")

        # Créer des étiquettes et des champs de saisie pour les informations de l'utilisateur
        username_label = QLabel('Nom d\'utilisateur:')
        self.username_edit = QLineEdit()
        password_label = QLabel('Mot de passe:')
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        confirm_label = QLabel('Confirmer le mot de passe:')
        self.confirm_edit = QLineEdit()
        self.confirm_edit.setEchoMode(QLineEdit.Password)
        email_label = QLabel('Email:')
        self.email_edit = QLineEdit()
        phone_label = QLabel('Numéro de téléphone:')
        self.phone_edit = QLineEdit()
        address_label = QLabel('Adresse:')
        self.address_edit = QLineEdit()

        # Créer un espace réservé à la photo de profil et un bouton pour télécharger une photo
        profile_pic_label = QLabel()
        profile_pic_label.setPixmap(QPixmap('images/profile_pic_placeholder.png'))
        profile_pic_label.setFixedSize(150, 150)
        upload_btn = QPushButton('Télécharger une photo')

        # Créer des boutons pour soumettre ou annuler le processus d'enregistrement
        submit_btn = QPushButton('S\'inscrire')
        submit_btn.setStyleSheet("background-color: red; color: white;")

        cancel_btn = QPushButton('Annuler')
        cancel_btn.setStyleSheet("background-color: black; color: white;")

        # Créer une disposition horizontale pour la photo de profil
        pic_layout = QHBoxLayout()
        pic_layout.addWidget(profile_pic_label)
        pic_layout.addWidget(upload_btn)

        # Créer une disposition verticale pour les champs de saisie des informations de l'utilisateur
        input_layout = QVBoxLayout()
        input_layout.addWidget(username_label)
        input_layout.addWidget(self.username_edit)
        input_layout.addWidget(password_label)
        input_layout.addWidget(self.password_edit)
        input_layout.addWidget(confirm_label)
        input_layout.addWidget(self.confirm_edit)
        input_layout.addWidget(email_label)
        input_layout.addWidget(self.email_edit)
        input_layout.addWidget(phone_label)
        input_layout.addWidget(self.phone_edit)
        input_layout.addWidget(address_label)
        input_layout.addWidget(self.address_edit)

        # Créer une disposition horizontale pour les boutons
        button_layout = QHBoxLayout()
        button_layout.addWidget(submit_btn)
        button_layout.addWidget(cancel_btn)

        # Créer une présentation verticale pour l'ensemble du dialogue et ajouter les présentations horizontales et la présentation des données.
        layout = QVBoxLayout(self)
        layout.addLayout(pic_layout)
        layout.addLayout(input_layout)
        layout.addLayout(button_layout)

        # Définir la taille et le style de la police pour toutes les étiquettes et tous les champs de saisie
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        for label in self.findChildren(QLabel):
            label.setFont(font)
        for edit in self.findChildren(QLineEdit):
            edit.setFont(font)
            edit.setPlaceholderText('Entrez ' + edit.objectName().split('_')[0].capitalize())

        # Centrer le dialogue sur l'écran
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.move(QApplication.desktop().screen().rect().center() - self.rect().center())

        # Connecter le bouton Soumettre à la fonction d'ouverture de la fenêtre de rendez-vous
        # submit_btn.clicked.connect(self.open_appointment_window)
        submit_btn.clicked.connect(lambda: User.insertData(self))

        # Connecter le bouton Annuler à la fonction de fermeture de la fenêtre
        cancel_btn.clicked.connect(self.reject)

    def open_appointment_window(self):
        # Créer une instance de la fenêtre de rendez-vous et l'afficher
        self.appointmentwindow = AppointmentWindow(self)
        print("dialog")
        self.appointmentwindow.show()

    def show_appointment(self):
        self.user_page = AppointmentWindow(self)
        self.user_page.show()
