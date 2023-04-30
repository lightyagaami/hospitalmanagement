class Users():
    def __init__(self, username, password, address, numero_telephone):
        self.id = None  # Nouvelle colonne "id"
        self.username = username
        self.password = password
        self.address = address
        self.numero_telephone = numero_telephone


class Doctor():
    def __init__(self, nom, specialite):
        self.id = None  # Nouvelle colonne "id"
        self.nom = nom
        self.specialite = specialite


class Appointment:
    def __init__(self, patient, docteur, date, heure):
        self.id = None  # Nouvelle colonne "id"
        self.patient = patient
        self.docteur = docteur
        self.date = date
        self.heure = heure
