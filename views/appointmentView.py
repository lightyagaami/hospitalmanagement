from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem
import sys


class AppointmentView(QWidget):
    def __init__(self, doctor, appointments):
        super().__init__()
        self.setWindowTitle('Appointment View')
        self.setFixedSize(600, 400)

        # Ajouter une étiquette pour le nom du médecin
        doctor_label = QLabel('Doctor: ' + doctor)

        # Ajouter un tableau pour afficher les rendez-vous pris
        table_widget = QTableWidget()
        table_widget.setColumnCount(2)
        table_widget.setHorizontalHeaderLabels(['Date', 'Patient'])
        table_widget.setRowCount(len(appointments))
        for row, appointment in enumerate(appointments):
            date_item = QTableWidgetItem(appointment['date'])
            patient_item = QTableWidgetItem(appointment['patient'])
            table_widget.setItem(row, 0, date_item)
            table_widget.setItem(row, 1, patient_item)
        table_widget.sortItems(0)

        # Ajouter un bouton pour fermer la fenêtre
        close_btn = QPushButton('Close')
        close_btn.setStyleSheet("background-color: #ff9f40; color: white;")
        close_btn.clicked.connect(self.close)

        # Ajouter des présentations verticales pour les éléments de l'interface
        doctor_layout = QHBoxLayout()
        doctor_layout.addWidget(doctor_label)
        table_layout = QVBoxLayout()
        table_layout.addWidget(table_widget)
        button_layout = QHBoxLayout()
        button_layout.addWidget(close_btn)

        # Ajouter une présentation verticale pour les présentations horizontales
        layout = QVBoxLayout(self)
        layout.addLayout(doctor_layout)
        layout.addLayout(table_layout)
        layout.addLayout(button_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    appointments = [{'date': '2023-04-01 10:00', 'patient': 'John Doe'},
                    {'date': '2023-04-01 11:00', 'patient': 'Jane Doe'},
                    {'date': '2023-04-02 09:00', 'patient': 'Bob Smith'}]
    doctor = 'Dr. Smith'
    appointment_view = AppointmentView(doctor, appointments)
    appointment_view.show()
    sys.exit(app.exec_())
