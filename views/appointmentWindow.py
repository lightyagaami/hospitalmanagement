import datetime
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QPushButton, QDateEdit, QFormLayout
from PyQt5.QtWidgets import QTimeEdit

from views.appointmentView import AppointmentView


class AppointmentWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Prendre rendez-vous')
        self.setFixedSize(600, 400)

    # Ajouter des étiquettes pour les champs de saisie
        name_label = QLabel('Nom complet:')
        doctor_label = QLabel('Docteur:')
        date_label = QLabel('Date:')
        time_label = QLabel('Heure:')
        disease_label = QLabel('Maladie:')

        # Ajouter des champs de saisie pour les informations du patient
        self.name_input = QLineEdit()
        self.doctor_input = QLineEdit()
        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.time_input = QTimeEdit()
        self.time_input.setDisplayFormat('HH:mm')
        self.disease_input = QLineEdit()

        # Ajouter un bouton pour soumettre les informations du rendez-vous
        submit_btn = QPushButton('Soumettre')
        submit_btn.setStyleSheet("background-color: #4CAF50; color: white;")
        submit_btn.clicked.connect(self.submit_appointment)

        # Ajouter une présentation verticale pour les champs de saisie
        form_layout = QFormLayout()
        form_layout.addRow(name_label, self.name_input)
        form_layout.addRow(doctor_label, self.doctor_input)
        form_layout.addRow(date_label, self.date_input)
        form_layout.addRow(time_label, self.time_input)
        form_layout.addRow(disease_label, self.disease_input)

        # Ajouter une présentation horizontale pour le bouton de soumission
        button_layout = QHBoxLayout()
        button_layout.addWidget(submit_btn)

        # Ajouter une présentation verticale pour les présentations horizontales
        layout = QVBoxLayout(self)
        layout.addLayout(form_layout)
        layout.addLayout(button_layout)

        # Initialiser la liste des rendez-vous
        self.appointment_list = [{'date': '2023-04-01 10:00', 'patient': 'John Doe', 'disease': 'Aucune'},
                                 {'date': '2023-04-01 11:00', 'patient': 'Jane Doe', 'disease': 'Fièvre'},
                                 {'date': '2023-04-02 09:00', 'patient': 'Bob Smith', 'disease': 'Toux'}]

    def submit_appointment(self):
        # Récupérer les informations du rendez-vous depuis les champs de saisie
        name = self.name_input.text()
        doctor = self.doctor_input.text()
        date = self.date_input.date().toString('yyyy-MM-dd')
        time = self.time_input.time().toString('HH:mm')
        disease = self.disease_input.text()  # Récupérer la maladie

        # Ajouter le rendez-vous à la liste des rendez-vous
        self.appointment_list.append({'patient': name, 'doctor': doctor, 'date': date + ' ' + time, 'disease': disease})

        # Créer la page AppointmentView avec tous les rendez-vous classés par heure
        appointments = sorted(self.appointment_list, key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%d %H:%M'))
        self.appointment_view = AppointmentView(doctor, appointments)
        self.appointment_view.show()
